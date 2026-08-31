"""Static quality checks for the LaTeX review manuscript."""

from __future__ import annotations

import re
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

for marker in ("turn0", "turn1", "PRISMA", "scoping review", "systematic review", "U+2011"):
    print(f"Marker {marker!r}: {text.lower().count(marker.lower())}")
