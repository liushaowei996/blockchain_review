"""Reproduce OAL counts and export the retained Visio artwork.

Use --data-only on any OS to regenerate the numerical outputs. Exporting the
editable drawings requires Microsoft Visio for Windows; manuscript compilation
uses the supplied PDFs and does not require Visio.
"""
from pathlib import Path
import argparse
import collections
import csv
import json
import os
import shutil
import subprocess

DATA = Path(__file__).resolve().parent


def aggregate():
    with (DATA / "oal-study-mapping.csv").open(encoding="utf-8") as stream:
        claims = list(csv.DictReader(stream))
    cells = collections.defaultdict(set)
    levels = collections.defaultdict(set)
    for claim in claims:
        for stage in claim["lifecycle_stages"].split(";"):
            cells[claim["object"], claim["assurance"], stage].add(claim["study_id"])
        for level in claim["evidence_levels"].split(";"):
            levels[level].add(claim["study_id"])
    rows = []
    for obj in "EPLD":
        for assurance in "OCGM":
            for stage in "ASTFDR":
                studies = cells[obj, assurance, stage]
                rows.append(dict(object=obj, assurance=assurance, stage=stage,
                                 study_count=len(studies),
                                 study_ids=";".join(sorted(studies))))
    with (DATA / "oal-cell-counts.csv").open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)
    summary = dict(studies=len({c["study_id"] for c in claims}),
                   claim_records=len(claims),
                   nonempty_cells=sum(r["study_count"] > 0 for r in rows),
                   evidence_profiles={level: len(levels[level]) for level in ("L0", "L1", "L2", "L3", "L4", "L5")})
    (DATA / "mapping-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    return summary


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-only", action="store_true")
    args = parser.parse_args()
    print(aggregate())
    if not args.data_only:
        if os.name != "nt":
            raise SystemExit("Visio export requires Windows and Microsoft Visio. Use --data-only to reproduce counts; the supplied figure PDFs remain usable.")
        shell = shutil.which("pwsh") or shutil.which("powershell")
        if not shell:
            raise SystemExit("PowerShell is required for Visio export.")
        subprocess.run([shell, "-NoProfile", "-NonInteractive", "-File", str(DATA / "export_visio_figures.ps1")], check=True)
