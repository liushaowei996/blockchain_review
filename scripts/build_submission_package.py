"""Package only the files needed by the current anonymous submission."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
MANUSCRIPT = ROOT / "manuscript"

# Keep an explicit list: working figures, internal reports, and build products
# must not enter the submission archive when new files appear in the repository.
PACKAGE_FILES = (
    "main.tex",
    "main.pdf",
    "main.bbl",
    "references.bib",
    "Definitions/mdpi.cls",
    "Definitions/mdpi.bst",
    "Definitions/journalnames.tex",
    "Definitions/logo-mdpi.eps",
    "Definitions/logo-mdpi-eps-converted-to.pdf",
    "sections/01-introduction.tex",
    "sections/02-scope.tex",
    "sections/03-context.tex",
    "sections/04-landscapes.tex",
    "sections/05-oal.tex",
    "sections/06-dependencies.tex",
    "sections/07-blockchain.tex",
    "sections/08-evaluation.tex",
    "sections/09-discussion.tex",
    "sections/10-limitations.tex",
    "sections/11-conclusions.tex",
    "figures/figure-01-reference-architecture.pdf",
    "figures/figure-02-assurance-chain.pdf",
    "figures/figure-03-oal-framework.pdf",
    "figures/figure-04-dependency-threat.pdf",
    "figures/figure-05-ctg-reasoning-loop.pdf",
    "figures/figure-06-blockchain-boundary.pdf",
    "figures/figure-07-evidence-maturity.pdf",
    "supplement/evidence-matrix.csv",
    "supplement/review-method-and-coding-notes.md",
    "submission/cover-letter-anonymous.tex",
    "submission/cover-letter-anonymous.pdf",
)


def build_package(destination: Path) -> None:
    missing = [name for name in PACKAGE_FILES if not (MANUSCRIPT / name).is_file()]
    if missing:
        raise FileNotFoundError(f"Missing submission files: {missing}")

    destination.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(destination, "w", compression=ZIP_DEFLATED, compresslevel=9) as archive:
        for name in sorted(PACKAGE_FILES):
            # Fixed timestamps and permissions make identical inputs reproducible.
            entry = ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            archive.writestr(
                entry, (MANUSCRIPT / name).read_bytes(),
                compress_type=ZIP_DEFLATED, compresslevel=9,
            )

    with ZipFile(destination) as archive:
        if archive.testzip() is not None:
            raise RuntimeError("Submission archive failed its CRC check")
        if archive.namelist() != sorted(PACKAGE_FILES):
            raise RuntimeError("Submission archive differs from the file list")
        for name in PACKAGE_FILES:
            if archive.read(name) != (MANUSCRIPT / name).read_bytes():
                raise RuntimeError(f"Packaged file differs from its source: {name}")

    print(f"Verified {len(PACKAGE_FILES)} files: {destination}")
    print(f"Archive size: {destination.stat().st_size:,} bytes")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="Destination ZIP path")
    args = parser.parse_args()
    build_package(args.output.resolve())
