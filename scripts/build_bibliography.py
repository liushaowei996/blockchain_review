"""Build a verified BibTeX library from a curated DOI list.

Crossref metadata are fetched through curl, normalized, and written to the
manuscript bibliography. Non-Crossref standards are maintained as explicit
manual records at the end of this file.
"""

from __future__ import annotations

import html
import json
import re
import subprocess
import tempfile
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


DOIS = [
    # Closest UAV/blockchain/security reviews and representative systems.
    "10.1109/OJVT.2023.3295208",
    "10.1016/j.vehcom.2020.100249",
    "10.1016/j.comcom.2020.01.023",
    "10.1016/j.comnet.2023.109626",
    "10.1145/3703625",
    "10.1016/j.jnca.2023.103607",
    "10.1109/TNSM.2022.3213370",
    "10.1109/COMST.2016.2560343",
    "10.1109/ACCESS.2019.2909530",
    "10.1007/s11370-022-00452-4",
    "10.1109/ACCESS.2021.3072030",
    "10.1016/j.jisa.2020.102670",
    "10.1002/ett.3706",
    "10.1109/WoWMoM.2019.8793027",
    "10.1109/TMC.2023.3319544",
    "10.3390/app122010524",
    "10.1109/MNET.011.2000210",
    "10.1016/j.compeleceng.2022.107847",
    "10.1109/JIOT.2022.3142251",
    "10.1109/TITS.2021.3136304",
    "10.1109/JIOT.2020.3020819",
    "10.1016/j.comcom.2020.07.042",
    "10.1109/ACCESS.2019.2930774",
    "10.1016/j.adhoc.2018.11.010",
    "10.1049/blc2.12050",
    "10.1109/AIBThings63359.2024.10863717",
    "10.1016/j.jnca.2024.103932",
    # Air-surface-underwater context and maritime communications/security.
    "10.1109/OJCOMS.2022.3225590",
    "10.1109/TCST.2023.3323766",
    "10.1109/TVT.2022.3220856",
    "10.1016/j.oceaneng.2023.115359",
    "10.3390/s23104643",
    "10.3390/s23177321",
    "10.1109/COMST.2021.3053118",
    "10.1109/COMST.2021.3134955",
    "10.1007/s12145-021-00762-8",
    "10.1109/ACCESS.2019.2928876",
    "10.3390/app10041256",
    "10.1109/TVT.2020.2991983",
    "10.1016/j.oceaneng.2022.112020",
    "10.3389/frobt.2021.616950",
    "10.3390/jmse9111314",
    "10.3390/jmse11040704",
    "10.3390/jmse11071336",
    "10.1109/ACCESS.2024.3360133",
    "10.1016/j.oceaneng.2025.123867",
    "10.1016/j.future.2024.03.046",
    "10.1007/s10257-020-00480-6",
    "10.1016/j.tre.2019.09.020",
    "10.1109/TITS.2022.3159485",
    "10.1109/TGCN.2022.3163596",
    "10.1109/COMST.2018.2864127",
    "10.1002/ett.4203",
    "10.1109/OJCOMS.2024.3474290",
    "10.3390/s18113907",
    "10.1007/s11831-019-09354-8",
    "10.1016/j.adhoc.2019.101935",
    "10.1109/ACCESS.2018.2818110",
    "10.1109/COMST.2024.3389728",
    "10.1109/TVT.2020.2999566",
    "10.1145/3377049.3377054",
    # Trust, reputation, zero trust, and uncertainty.
    "10.1109/JIOT.2023.3237893",
    "10.1016/j.jnca.2019.102409",
    "10.1186/s13677-023-00416-8",
    "10.1109/ACCESS.2021.3066457",
    "10.1109/ACCESS.2020.2969820",
    "10.1016/j.comnet.2021.108558",
    "10.1186/s13673-019-0183-8",
    "10.1016/j.jpdc.2019.10.006",
    "10.1016/j.jksuci.2021.09.004",
    "10.1186/s13677-021-00247-5",
    "10.1109/ACCESS.2022.3174679",
    "10.1109/OJCOMS.2023.3244274",
    "10.6028/NIST.SP.800-207",
    "10.6028/NIST.IR.8259A",
    "10.17487/RFC9334",
    "10.1007/978-3-319-42337-1",
    "10.1109/HICSS.2002.994181",
    "10.1145/775152.775242",
    # Provenance, attestation, IoT-blockchain integration, and ledger design.
    "10.1145/3190508.3190538",
    "10.6028/NIST.IR.8202",
    "10.1109/COMST.2018.2886932",
    "10.1016/j.future.2018.05.046",
    "10.1016/j.future.2017.08.020",
    "10.1109/ACCESS.2019.2896108",
    "10.1109/ACCESS.2021.3065880",
    "10.1109/ACCESS.2020.3007251",
    "10.1016/j.icte.2019.08.001",
    "10.1145/3054977.3055003",
    "10.3390/s19102228",
    "10.1186/s40537-021-00505-y",
    "10.1007/s11280-019-00746-1",
    "10.1145/3593294",
    "10.1109/ACCESS.2018.2887201",
    "10.1162/dint_a_00119",
    "10.1007/s11280-021-00869-4",
    "10.1145/3600160.3600171",
    "10.1007/978-3-031-20936-9_28",
    "10.3390/fi17020085",
    "10.1109/MIC.2021.3059320",
    "10.3390/s20102990",
    "10.1109/ACCESS.2020.3037474",
    "10.1016/j.bcra.2021.100006",
    "10.1109/ACCESS.2019.2936094",
    "10.1016/j.tele.2018.11.006",
    "10.1109/ACCESS.2019.2956748",
    "10.1016/j.bcra.2021.100027",
    "10.1016/j.jnca.2020.102857",
    "10.1016/j.jnca.2020.102693",
    "10.1016/j.giq.2017.09.007",
    "10.1016/j.marpol.2020.104265",
    "10.1109/ACCESS.2020.2968492",
    "10.1016/j.ijinfomgt.2017.12.005",
    "10.1109/MITP.2017.3051335",
    "10.3390/s22124394",
    "10.1016/j.jksuci.2021.08.005",
    "10.3390/app11209372",
    "10.1145/343477.343502",
    # Evidence maturity, sensor fusion, spoofing, datasets, and simulators.
    "10.1016/j.inffus.2021.10.007",
    "10.1109/ACCESS.2021.3089847",
    "10.1109/JIOT.2022.3195320",
    "10.3390/s20041171",
    "10.3390/s24134210",
    "10.3390/ijgi9010006",
    "10.1109/TSMC.2017.2681698",
    "10.1609/aaai.v36i7.20724",
    "10.3390/s25196033",
    "10.3390/s23135941",
    "10.1109/ACCESS.2020.3022862",
    "10.1109/ACCESS.2022.3165809",
    "10.1145/3148675.3148679",
    "10.1007/978-3-319-67361-5_40",
    "10.1109/OCEANS.2016.7761080",
]


MANUAL_ENTRIES = r"""
@misc{w3c2013provdm,
  author       = {{World Wide Web Consortium}},
  title        = {{PROV-DM}: The {PROV} Data Model},
  year         = {2013},
  howpublished = {W3C Recommendation},
  url          = {https://www.w3.org/TR/prov-dm/},
  note         = {Accessed 6 August 2026}
}

@misc{w3c2013provo,
  author       = {{World Wide Web Consortium}},
  title        = {{PROV-O}: The {PROV} Ontology},
  year         = {2013},
  howpublished = {W3C Recommendation},
  url          = {https://www.w3.org/TR/prov-o/},
  note         = {Accessed 6 August 2026}
}

@misc{threegpp22125,
  author       = {{3rd Generation Partnership Project}},
  title        = {Unmanned Aerial System ({UAS}) Support in {3GPP}; Stage 1},
  year         = {2026},
  howpublished = {3GPP TS 22.125},
  url          = {https://www.3gpp.org/dynareport/22125.htm},
  note         = {Specification record accessed 6 August 2026}
}

@misc{threegpp22119,
  author       = {{3rd Generation Partnership Project}},
  title        = {Maritime Communication Services over {3GPP} System},
  year         = {2026},
  howpublished = {3GPP TS 22.119},
  url          = {https://www.3gpp.org/dynareport/22119.htm},
  note         = {Specification record accessed 6 August 2026}
}

@misc{hyperledger2026fabric,
  author       = {{Hyperledger Foundation}},
  title        = {Hyperledger Fabric Documentation: Ordering Service},
  year         = {2026},
  url          = {https://hyperledger-fabric.readthedocs.io/en/latest/orderer/ordering_service.html},
  note         = {Accessed 6 August 2026}
}

@misc{ietf2020suit,
  author       = {Moran, Brendan and Tschofenig, Hannes and Brown, David and Meriac, Milos},
  title        = {A Firmware Update Architecture for Internet of Things},
  year         = {2021},
  howpublished = {RFC 9019},
  doi          = {10.17487/RFC9019},
  url          = {https://www.rfc-editor.org/rfc/rfc9019}
}

@inproceedings{varga2022seadronessee,
  author       = {Varga, Leon Amadeus and Kiefer, Benjamin and Messmer, Martin and Zell, Andreas},
  title        = {{SeaDronesSee}: A Maritime Benchmark for Detecting Humans in Open Water},
  booktitle    = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision},
  year         = {2022},
  pages        = {2260--2270},
  url          = {https://openaccess.thecvf.com/content/WACV2022/html/Varga_SeaDronesSee_A_Maritime_Benchmark_for_Detecting_Humans_in_Open_Water_WACV_2022_paper.html}
}
""".strip()


def fetch_crossref(doi: str) -> dict:
    encoded = urllib.parse.quote(doi, safe="")
    url = f"https://api.crossref.org/works/{encoded}?mailto=review@example.com"
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as handle:
        path = Path(handle.name)
    try:
        subprocess.run(
            ["curl.exe", "-sS", "--retry", "4", "-L", "-o", str(path), url],
            check=True,
        )
        payload = json.loads(path.read_text(encoding="utf-8"))
        if payload.get("status") != "ok":
            raise ValueError(f"Crossref status is {payload.get('status')}")
        return payload["message"]
    finally:
        path.unlink(missing_ok=True)


def clean(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", html.unescape(value or ""))
    value = value.replace("\u2010", "-").replace("\u2011", "-")
    value = value.replace("\u2012", "-").replace("\u2013", "--").replace("\u2014", "---")
    value = value.replace("\u2212", "-").replace("\u00a0", " ")
    value = re.sub(r"\s+", " ", value).strip()
    for old, new in [("&", r"\&"), ("%", r"\%"), ("#", r"\#"), ("_", r"\_")]:
        value = value.replace(old, new)
    return value


def issued_year(message: dict) -> int:
    for field in ("published-print", "published-online", "issued", "created"):
        parts = ((message.get(field) or {}).get("date-parts") or [])
        if parts and parts[0] and parts[0][0] is not None:
            return int(parts[0][0])
    return 0


def make_key(message: dict, doi: str, used: set[str]) -> str:
    authors = message.get("author") or []
    family = clean((authors[0].get("family") if authors else "source")).lower()
    family = re.sub(r"[^a-z0-9]+", "", family) or "source"
    year = issued_year(message) or "nd"
    title = clean((message.get("title") or ["work"])[0]).lower()
    words = [w for w in re.findall(r"[a-z0-9]+", title) if w not in {"a", "an", "the", "of", "on", "for", "and", "in", "to"}]
    stem = (words[0] if words else re.sub(r"\W+", "", doi)[-6:])[:18]
    base = f"{family}{year}{stem}"
    key = base
    suffix = 2
    while key in used:
        key = f"{base}{suffix}"
        suffix += 1
    used.add(key)
    return key


def bibtex_entry(message: dict, doi: str, used: set[str]) -> tuple[str, str]:
    crossref_type = message.get("type", "journal-article")
    entry_type = {
        "journal-article": "article",
        "proceedings-article": "inproceedings",
        "book-chapter": "incollection",
        "book": "book",
        "report": "techreport",
        "posted-content": "misc",
    }.get(crossref_type, "misc")
    key = make_key(message, doi, used)
    fields: list[tuple[str, str]] = []
    authors = message.get("author") or []
    if authors:
        author_text = " and ".join(
            ", ".join(filter(None, [clean(a.get("family", "")), clean(a.get("given", ""))]))
            for a in authors
        )
        fields.append(("author", author_text))
    title = clean((message.get("title") or [""])[0])
    fields.extend([("title", "{" + title + "}"), ("year", str(issued_year(message)))])
    container = clean((message.get("container-title") or [""])[0])
    if entry_type == "article" and container:
        fields.append(("journal", container))
    elif entry_type in {"inproceedings", "incollection"} and container:
        fields.append(("booktitle", container))
    for source, target in (("volume", "volume"), ("issue", "number"), ("page", "pages"), ("publisher", "publisher")):
        if message.get(source):
            if source == "publisher" and entry_type == "techreport":
                target = "institution"
            fields.append((target, clean(str(message[source]))))
    fields.extend([("doi", doi), ("url", f"https://doi.org/{doi}")])
    width = max(len(name) for name, _ in fields)
    body = ",\n".join(f"  {name.ljust(width)} = {{{value}}}" for name, value in fields)
    return key, f"@{entry_type}{{{key},\n{body}\n}}"


def main() -> None:
    unique_dois = list(dict.fromkeys(doi.lower() for doi in DOIS))
    entries: list[str] = []
    metadata: dict[str, dict] = {}
    failures: list[str] = []
    used: set[str] = set()
    key_map: dict[str, str] = {}
    fetched: dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=8) as executor:
        future_map = {executor.submit(fetch_crossref, doi): doi for doi in unique_dois}
        completed = 0
        for future in as_completed(future_map):
            doi = future_map[future]
            completed += 1
            try:
                fetched[doi] = future.result()
                print(f"Fetched {completed}/{len(unique_dois)}: {doi}", flush=True)
            except Exception as exc:
                failures.append(f"{doi}\t{type(exc).__name__}: {exc}")
                print(f"FAILED {doi}: {exc}", flush=True)

    for index, doi in enumerate(unique_dois, start=1):
        if doi not in fetched:
            continue
        try:
            message = fetched[doi]
            key, entry = bibtex_entry(message, doi, used)
            key_map[doi] = key
            metadata[doi] = message
            entries.append(entry)
            print(f"[{index}/{len(unique_dois)}] {key}", flush=True)
        except Exception as exc:  # corpus build must report every unresolved DOI
            failures.append(f"{doi}\t{type(exc).__name__}: {exc}")
            print(f"[{index}/{len(unique_dois)}] FAILED {doi}: {exc}", flush=True)

    Path("manuscript/references.bib").write_text(
        "% Generated from Crossref metadata; verified on 2026-08-06.\n\n"
        + "\n\n".join(entries)
        + "\n\n"
        + MANUAL_ENTRIES
        + "\n",
        encoding="utf-8",
    )
    Path("tmp/crossref_metadata.json").write_text(
        json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    Path("tmp/citekeys.json").write_text(
        json.dumps(key_map, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    Path("tmp/doi_failures.txt").write_text("\n".join(failures), encoding="utf-8")
    print(f"Wrote {len(entries)} Crossref entries and {len(failures)} failures")


if __name__ == "__main__":
    main()
