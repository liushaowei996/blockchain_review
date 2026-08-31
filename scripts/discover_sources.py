"""Discover candidate literature through the OpenAlex API.

This is a corpus-building helper, not part of the submitted manuscript. It uses
curl for transport because the host Python installation has no configured CA
bundle. Results are normalized and deduplicated by DOI/OpenAlex identifier.
"""

from __future__ import annotations

import csv
import json
import subprocess
import tempfile
import urllib.parse
from pathlib import Path


QUERIES = [
    "blockchain UAV survey",
    "blockchain unmanned aerial vehicle security",
    "blockchain UAV swarm",
    "UAV swarm security survey",
    "unmanned aerial vehicle trust management reputation",
    "UAV data provenance blockchain",
    "maritime blockchain survey",
    "maritime IoT blockchain security",
    "Internet of Underwater Things security survey",
    "underwater acoustic network security survey",
    "underwater wireless sensor network trust management",
    "UUV security trust",
    "UAV USV UUV cooperative systems",
    "air surface underwater heterogeneous unmanned systems",
    "cross-domain unmanned systems UAV USV UUV",
    "blockchain trust management IoT survey",
    "IoT trust reputation survey taxonomy",
    "dynamic trust management IoT Bayesian subjective logic",
    "zero trust architecture IoT review",
    "remote attestation IoT survey RATS",
    "data provenance IoT survey W3C PROV",
    "blockchain data provenance IoT",
    "blockchain off-chain storage IoT survey",
    "permissioned blockchain IoT resource constrained",
    "blockchain network partition finality",
    "blockchain governance permissioned consortium",
    "multi-sensor fusion trust reliability adversarial",
    "data trustworthiness sensor fusion provenance",
    "UAV GNSS spoofing survey",
    "underwater acoustic jamming security",
    "UAV USV cooperative search review",
    "UAV UUV cross-domain communication",
]


def fetch(query: str) -> dict:
    params = {
        "search": query,
        "filter": "from_publication_date:2016-01-01",
        "sort": "relevance_score:desc",
        "per-page": "25",
        "mailto": "review@example.com",
    }
    url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as handle:
        temp_path = Path(handle.name)
    try:
        subprocess.run(
            ["curl.exe", "-sS", "--retry", "4", "-L", "-o", str(temp_path), url],
            check=True,
        )
        return json.loads(temp_path.read_text(encoding="utf-8"))
    finally:
        temp_path.unlink(missing_ok=True)


def main() -> None:
    rows: dict[str, dict] = {}
    for query in QUERIES:
        payload = fetch(query)
        for rank, work in enumerate(payload.get("results", []), start=1):
            doi = (work.get("doi") or "").removeprefix("https://doi.org/").lower()
            key = doi or work.get("id", "")
            if not key:
                continue
            source = ((work.get("primary_location") or {}).get("source") or {}).get(
                "display_name", ""
            )
            oa = work.get("open_access") or {}
            best = work.get("best_oa_location") or {}
            row = rows.setdefault(
                key,
                {
                    "key": key,
                    "doi": doi,
                    "year": work.get("publication_year", ""),
                    "title": work.get("title", ""),
                    "source": source or "",
                    "type": work.get("type", ""),
                    "oa_status": oa.get("oa_status", ""),
                    "oa_url": best.get("pdf_url") or best.get("landing_page_url") or "",
                    "cited_by": work.get("cited_by_count", 0),
                    "best_rank": rank,
                    "queries": set(),
                },
            )
            row["queries"].add(query)
            row["best_rank"] = min(int(row["best_rank"]), rank)

    output = Path("tmp/source_candidates.tsv")
    output.parent.mkdir(parents=True, exist_ok=True)
    ordered = sorted(rows.values(), key=lambda row: (-int(row["cited_by"] or 0), row["title"]))
    with output.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "key",
                "doi",
                "year",
                "title",
                "source",
                "type",
                "oa_status",
                "oa_url",
                "cited_by",
                "best_rank",
                "queries",
            ],
            delimiter="\t",
        )
        writer.writeheader()
        for row in ordered:
            serial = dict(row)
            serial["queries"] = " | ".join(sorted(row["queries"]))
            writer.writerow(serial)
    print(f"Wrote {len(ordered)} candidates to {output}")


if __name__ == "__main__":
    main()
