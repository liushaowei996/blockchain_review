"""Build the Chinese translation and append it to the unchanged English proof.

Requires XeLaTeX and pypdf. Run from any directory. The Chinese text reuses
the original English figures, as requested; captions are translated.
"""
from pathlib import Path
import argparse
import hashlib
import json
import logging
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "proofread/internal-approval"
SOURCE = ROOT / "proofread/blockchains-4630703.tex"
ENGLISH = ROOT / "output/pdf/blockchains-4630703-author-corrected.pdf"
BUILD = ROOT / "tmp/pdfs/internal-approval/build"
OUTPUT = ROOT / "output/pdf/blockchains-4630703-internal-approval-en-zh.pdf"


def uncomment(text):
    # TeX consumes the end-of-line with a comment. Keeping comment-only
    # newlines would introduce spurious paragraphs inside reference entries.
    return re.sub(r"(?<!\\)%[^\n]*(?:\n|$)", "", text)


def bibliography():
    text = uncomment(SOURCE.read_text(encoding="utf-8"))
    body = text.split(r"\begin{thebibliography}{999}", 1)[1].split(r"\end{thebibliography}", 1)[0]
    entries = re.findall(r"(\\bibitem\[.*?)(?=\\bibitem\[|\Z)", body, re.S)
    keys = [re.search(r"\]\{([^}]+)\}", e).group(1) for e in entries]
    assert len(entries) == len(set(keys)) == 123
    return keys, entries


def prepare_references():
    keys, entries = bibliography()
    titles = json.loads((PROJECT / "reference-titles-zh.json").read_text(encoding="utf-8"))
    assert set(titles) == set(keys), (set(keys) - set(titles), set(titles) - set(keys))
    output = [r"\begin{thebibliography}{123}"]
    for key, entry in zip(keys, entries):
        # Retain bibliographic identifiers and names verbatim; translate generic
        # bibliographic phrases as well as supplying every title in Chinese.
        entry = entry.replace("Available online:", "在线地址：").replace("Online specification record.", "在线规范目录记录。")
        entry = entry.replace("(accessed on 6 August 2026)", "（访问日期：2026 年 8 月 6 日）")
        entry = entry.replace("(accessed on 25 October 2026)", "（访问日期：2026 年 10 月 25 日）")
        entry = entry.replace("(accessed on 22 October 2026)", "（访问日期：2026 年 10 月 22 日）")
        output.extend([entry.strip(), "\\newblock \\textit{题名中译：}" + titles[key] + "。", ""])
    output.append(r"\end{thebibliography}")
    reference_text = "\n".join(line.rstrip() for line in "\n".join(output).splitlines()) + "\n"
    (PROJECT / "references-zh.tex").write_text(reference_text, encoding="utf-8")


def verify_structure():
    original = uncomment(SOURCE.read_text(encoding="utf-8"))
    chinese = "\n".join(p.read_text(encoding="utf-8") for p in sorted((PROJECT / "sections").glob("*.tex")))
    chinese += (PROJECT / "backmatter.tex").read_text(encoding="utf-8")
    source_body = original.split(r"\section{Introduction}", 1)[1].split(r"\begin{thebibliography}", 1)[0]
    keys = lambda s: re.findall(r"\\label\{([^}]+)\}", s)
    assert set(keys(source_body)) == set(keys(chinese)), "Cross-reference label coverage differs"
    citations = lambda s: [x.strip() for g in re.findall(r"\\cite[pt]?\{([^}]+)\}", s) for x in g.split(",")]
    from collections import Counter
    assert Counter(citations(source_body)) == Counter(citations(chinese)), "Citation occurrences differ"
    inline_math = lambda s: re.findall(r"(?<!\\)\$([^$]+)\$", s)
    assert Counter(inline_math(source_body)) == Counter(inline_math(chinese)), "Inline mathematical expressions differ"
    expected = {"sections": 11, "subsections": 29, "figures": 7, "tables": 12, "equations": 1}
    counts = {
        "sections": len(re.findall(r"\\section\{", chinese)),
        "subsections": len(re.findall(r"\\subsection\{", chinese)),
        "figures": chinese.count(r"\begin{figure}"),
        "tables": chinese.count(r"\begin{table}"),
        "equations": chinese.count(r"\begin{equation}"),
    }
    for k in expected:
        if k == "subsections":
            expected[k] = len(re.findall(r"\\subsection\{", source_body))
    assert counts == expected, (counts, expected)
    assert not re.search(r"TODO|TBD|待翻译|占位", chinese)
    return counts


def build():
    from pypdf import PdfReader, PdfWriter
    prepare_references()
    counts = verify_structure()
    BUILD.mkdir(parents=True, exist_ok=True)
    for turn in range(3):
        cmd = ["xelatex", "-interaction=nonstopmode", "-halt-on-error", "-file-line-error", f"-output-directory={BUILD}", "main.tex"]
        run = subprocess.run(cmd, cwd=PROJECT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        (BUILD / f"pass-{turn + 1}.txt").write_bytes(run.stdout)
        if run.returncode:
            raise RuntimeError(run.stdout.decode("utf-8", errors="replace")[-6000:])
    log = (BUILD / "main.log").read_text(encoding="utf-8", errors="replace")
    errors = [line for line in log.splitlines() if re.search(r"undefined|Missing character|Overfull|multiply defined", line, re.I)]
    if errors:
        raise RuntimeError("Unresolved typesetting diagnostics:\n" + "\n".join(errors))
    english, chinese = PdfReader(ENGLISH), PdfReader(BUILD / "main.pdf")
    assert len(english.pages) == 31, "Update the Chinese start page when the English proof changes"
    merge_logger = logging.getLogger("pypdf")
    merge_logger.addHandler(logging.FileHandler(BUILD / "merge.log", mode="w", encoding="utf-8"))
    merge_logger.propagate = False
    writer = PdfWriter()
    writer.append(english, outline_item="英文原稿 / English original", import_outline=True)
    writer.append(chinese, outline_item="中文全文翻译 / Chinese translation", import_outline=True)
    writer.add_metadata({"/Title": "Blockchain-Assisted Mission Trust | 公司内部发表前审批（英文及中文全文）",
                         "/Author": "Shaowei Liu; Jing Wu; Tanren Liu; Shengqiang He; Yakun Ren; Chengnian Long",
                         "/Subject": "English author-corrected proof dated 2026-11-02 followed by its complete Chinese translation"})
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("wb") as f:
        writer.write(f)
    merged = PdfReader(OUTPUT)
    assert len(merged.pages) == len(english.pages) + len(chinese.pages)
    def annotation_count(page):
        annotations = page.get("/Annots", [])
        return len(annotations.get_object() if hasattr(annotations, "get_object") else annotations)
    for source_pdf, offset in ((english, 0), (chinese, len(english.pages))):
        for i, page in enumerate(source_pdf.pages):
            assert annotation_count(page) == annotation_count(merged.pages[offset + i]), "Annotation count changed"
        for name, destination in source_pdf.named_destinations.items():
            assert name in merged.named_destinations, f"Missing destination: {name}"
            actual = merged.get_destination_page_number(merged.named_destinations[name])
            expected = offset + source_pdf.get_destination_page_number(destination)
            assert actual == expected, (name, actual, expected)
    for a, b in zip(english.pages, merged.pages[:len(english.pages)]):
        assert a.get_contents().get_data() == b.get_contents().get_data(), "English page content stream changed"
        assert a.extract_text() == b.extract_text(), "English text changed"
    for page in chinese.pages:
        assert len(page.extract_text().strip()) > 50, "Unexpected blank/near-empty Chinese page"
        assert "�" not in page.extract_text(), "Replacement character in Chinese PDF"
    report = {"english_source": str(ENGLISH.relative_to(ROOT)),
              "english_sha256": hashlib.sha256(ENGLISH.read_bytes()).hexdigest(),
              "source_tex_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
              "english_pages": len(english.pages), "chinese_pages": len(chinese.pages),
              "total_pages": len(merged.pages), "structure": counts,
              "reference_count": 123, "english_page_streams_unchanged": True,
              "citation_occurrences_match": True, "cross_reference_labels_match": True,
              "inline_math_expressions_match": True, "figures": "Unmodified English originals, with Chinese captions",
              "named_destination_pages_match": True,
              "annotation_counts_preserved": True,
              "typesetting_errors": errors, "output_sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}
    (PROJECT / "verification.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--list-references", action="store_true")
    args = parser.parse_args()
    if args.list_references:
        keys, entries = bibliography()
        for i, (key, entry) in enumerate(zip(keys, entries), 1):
            print(i, key, re.sub(r"\s+", " ", entry.split(r"\newblock")[1]).strip())
    else:
        build()
