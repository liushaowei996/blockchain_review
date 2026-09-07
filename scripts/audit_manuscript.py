"""Static quality checks for the LaTeX review manuscript."""

from __future__ import annotations

import re
import csv
import sys
from pathlib import Path


ROOT = Path("manuscript")
files = [ROOT / "main.tex", *sorted((ROOT / "sections").glob("*.tex"))]
text = "\n".join(path.read_text(encoding="utf-8") for path in files)
bib = (ROOT / "references.bib").read_text(encoding="utf-8")
bib_keys = set(re.findall(r"(?m)^@\w+\{([^,]+),", bib))
cites = []
for group in re.findall(r"\\cite\w*\{([^}]+)\}", text):
    cites.extend(key.strip() for key in group.split(","))
cited = set(cites)
missing = sorted(cited - bib_keys)
uncited = sorted(bib_keys - cited)

plain = re.sub(r"%.*", " ", text)
plain = re.sub(r"\\(?:cite\w*|ref|eqref|label|input|textit|textbf|emph|term|Title|Author|AuthorNames|address|corres|keyword|caption|section|subsection|supplementary|authorcontributions|funding|institutionalreview|informedconsent|dataavailability|acknowledgments|conflictsofinterest)\{[^{}]*\}", " ", plain)
plain = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^]]*\])?", " ", plain)
plain = re.sub(r"[^A-Za-z0-9'-]+", " ", plain)
words = re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", plain)

abstract_match = re.search(r"\\abstract\{(.*?)\}\s*\\keyword", text, re.S)
abstract_words = re.findall(r"\b[A-Za-z][A-Za-z'-]*\b", abstract_match.group(1)) if abstract_match else []

labels = re.findall(r"\\label\{([^}]+)\}", text)
duplicates = sorted({label for label in labels if labels.count(label) > 1})
refs = set(re.findall(r"\\(?:ref|eqref)\{([^}]+)\}", text))
undefined_refs = sorted(refs - set(labels))

print(f"TeX files: {len(files)}")
print(f"Approximate manuscript words: {len(words)}")
print(f"Abstract words: {len(abstract_words)}")
print(f"Bibliography entries: {len(bib_keys)}")
print(f"Unique cited entries: {len(cited)}")
print(f"Missing citation keys: {missing}")
print(f"Uncited bibliography entries ({len(uncited)}): {uncited}")
print(f"Duplicate labels: {duplicates}")
print(f"Undefined refs: {undefined_refs}")

placeholders = re.findall(r"turn\d+(?:search|view|fetch)\d+|U\+2011|\u2011", text)
print(f"Unresolved tool/character placeholders: {placeholders}")

graphics = re.findall(r"\\includegraphics(?:\[[^]]*\])?\{([^}]+)\}", text)
missing_graphics = [name for name in graphics if not (ROOT / name).is_file()]
all_bib_keys = re.findall(r"(?m)^@\w+\{([^,]+),", bib)
duplicate_bib = sorted({key for key in all_bib_keys if all_bib_keys.count(key) > 1})
errors = [name for name, value in {
    "missing citations": missing, "uncited entries": uncited,
    "duplicate labels": duplicates, "undefined refs": undefined_refs,
    "missing figures": missing_graphics, "duplicate bibliography keys": duplicate_bib,
    "placeholders": placeholders,
}.items() if value]
for filename in ("evidence-matrix.csv", "full-text-acquisition-manifest.csv"):
    with (ROOT / "supplement" / filename).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    ids = [row["source_id"] for row in rows]
    if len(ids) != len(set(ids)) or set(ids) != bib_keys:
        errors.append(f"{filename} bibliography/identity mismatch")
    print(f"{filename}: {len(ids)} unique-source records; bibliography match={set(ids) == bib_keys}")
    if filename == "evidence-matrix.csv":
        retained = sum("artifact retained;" in row["full_text_status"] for row in rows)
        coded = sum("claim-level coding completed" in row["coding_status"] for row in rows)
        missing_locators = [row["source_id"] for row in rows if "claim-level coding completed" in row["coding_status"] and row["claim_locator"].startswith("not assigned")]
        print(f"Retained full-text artifacts: {retained}; detailed coded sources: {coded}")
        if missing_locators:
            errors.append(f"coded sources without locators: {missing_locators}")
print(f"Missing figures: {missing_graphics}")
print(f"Audit failures: {errors}")
sys.exit(bool(errors))
