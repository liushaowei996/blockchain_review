"""Update native Figure 3 values in VSDX without changing any other page.

Standard-library XML/ZIP editing preserves original shapes and connections.
Run update_oal_visio.ps1 to update and export the page with Microsoft Visio.
"""
from pathlib import Path
from zipfile import ZipFile
from xml.dom import minidom
import argparse
import csv
import json
import os
import tempfile

DATA = Path(__file__).resolve().parent


def children(node, name):
    return [n for n in node.childNodes if n.nodeType == n.ELEMENT_NODE and n.localName == name]


def text_content(node):
    return "".join(n.data if n.nodeType in (n.TEXT_NODE, n.CDATA_SECTION_NODE)
                   else text_content(n) for n in node.childNodes)


def set_text(node, text):
    # Keep cp/pp/tp format markers and existing character sections.
    for n in list(node.childNodes):
        if n.nodeType in (n.TEXT_NODE, n.CDATA_SECTION_NODE):
            node.removeChild(n)
    node.appendChild(node.ownerDocument.createTextNode(text + "\n"))


def set_cell(parent, name, value, formula=None):
    matches = [n for n in children(parent, "Cell") if n.getAttribute("N") == name]
    cell = matches[0] if matches else parent.ownerDocument.createElement("Cell")
    if not matches:
        cell.setAttribute("N", name)
        parent.appendChild(cell)
    cell.setAttribute("V", value)
    if formula is None:
        if cell.hasAttribute("F"):
            cell.removeAttribute("F")
    else:
        cell.setAttribute("F", formula)


def update(source):
    with (DATA / "oal-cell-counts.csv").open(encoding="utf-8", newline="") as stream:
        expected = {(r["object"], r["assurance"], r["stage"]): int(r["study_count"]) for r in csv.DictReader(stream)}
    assert len(expected) == 96
    summary = json.loads((DATA / "mapping-summary.json").read_text(encoding="utf-8"))
    with ZipFile(source) as archive:
        infos = archive.infolist()
        parts = {info.filename: archive.read(info) for info in infos}
    page = minidom.parseString(parts["visio/pages/page4.xml"])
    found = {}
    for shape in page.getElementsByTagName("Shape"):
        cells = {c.getAttribute("N"): c.getAttribute("V") for c in children(shape, "Cell")}
        texts = children(shape, "Text")
        if not texts:
            continue
        text = text_content(texts[0]).strip()
        if abs(float(cells.get("Width", 0)) - 1.75) < 1e-6 and abs(float(cells.get("Height", 0)) - .265) < 1e-6:
            col = round((float(cells["PinX"]) - 3) / 1.75 - .5)
            row = round((5.5 - float(cells["PinY"])) / .265 - .5)
            assert 0 <= col < 6 and 0 <= row < 16
            key = "EPLD"[row // 4], "OCGM"[row % 4], "ASTFDR"[col]
            number = expected[key]
            set_text(texts[0], str(number))
            ratio = number / max(1, max(expected.values()))
            rgb = tuple(round(base - delta * ratio) for base, delta in [(241, 201), (246, 130), (248, 112)])
            set_cell(shape, "FillForegnd", "#%02X%02X%02X" % rgb, "RGB(%d,%d,%d)" % rgb)
            for section in children(shape, "Section"):
                if section.getAttribute("N") == "Character":
                    for char_row in children(section, "Row"):
                        color = (255, 255, 255) if ratio >= .55 else (31, 78, 109)
                        set_cell(char_row, "Color", "#%02X%02X%02X" % color, "RGB(%d,%d,%d)" % color)
                        set_cell(char_row, "Style", "1" if number else "0")
            found[key] = number
        elif text.startswith("(b) Coverage of"):
            set_text(texts[0], f"(b) Coverage of {summary['studies']} full-text studies / {summary['claim_records']} claim records")
        elif text.startswith("Evidence profiles"):
            set_text(texts[0], "Evidence profiles (overlap):  " + "    ".join(f"L{i}  {summary['evidence_profiles'][f'L{i}']}" for i in range(6)))
    assert found == expected
    parts["visio/pages/page4.xml"] = page.toxml(encoding="utf-8")
    for name in ["docProps/core.xml", "docProps/app.xml"]:
        xml = minidom.parseString(parts[name])
        for node in list(xml.documentElement.childNodes):
            if node.nodeType != node.ELEMENT_NODE:
                continue
            if node.localName in ["creator", "lastModifiedBy"]:
                for child in list(node.childNodes):
                    node.removeChild(child)
                node.appendChild(xml.createTextNode("Anonymous authors"))
            elif node.localName in ["Template", "Company", "Manager"]:
                node.parentNode.removeChild(node)
        parts[name] = xml.toxml(encoding="utf-8")
    handle, temporary = tempfile.mkstemp(suffix=".vsdx", dir=source.parent)
    os.close(handle)
    try:
        with ZipFile(temporary, "w") as archive:
            for info in infos:
                archive.writestr(info, parts[info.filename])
        with ZipFile(temporary) as archive:
            assert archive.testzip() is None
        os.replace(temporary, source)
    finally:
        if os.path.exists(temporary):
            os.remove(temporary)
    print("Updated 96 native cells, heading and evidence profiles; other page XML is unchanged.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path, default=DATA.parent / "figures/Figures-revised.vsdx")
    update(parser.parse_args().source.resolve())
