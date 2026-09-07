# Anonymous MDPI Blockchains Review Package

## Current version

The 7 September 2026 revision is a narrative Review and conceptual synthesis. It includes a revised OAL assessment/decision interface, a bounded CTG worked example, conditional ledger-selection criteria, and a claim-specific evidence profile. A subsequent figure-style revision regenerated Figures 4, 6, and 7 with the built-in image generation tool to match the retained artwork while preserving the revised scientific distinctions. No new integrated experiment or performance result is reported.

## Build

From the extracted package root, run:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The official MDPI template was obtained on 6 August 2026. Its archived download SHA-256 is `44A9464C06E724889E1496A73BE0E6F81099D534BCC9A3DA94B99B52F0ECC563`. The existing compatibility shims address the locally installed older MiKTeX/LaTeX combination. The revision was also built from an isolated copy of the packaged sources.

## Contents

- `main.tex`, `sections/`, `references.bib`, `main.bbl`, and `main.pdf`: editable source and compiled manuscript.
- `Definitions/`: MDPI class, bibliography styles, and assets.
- `figures/`: seven publication PDFs containing image-generated raster artwork. Figures 4, 6, and 7 include the current PNG masters, standalone PDF wrappers, and `image-generation-prompts-20260907.md`. All TikZ drawing sources are historical working versions and are not used by the manuscript.
- `supplement/evidence-matrix.csv`: 141-source inventory with routing basis, availability, coding status, and selected claim locators.
- `supplement/full-text-acquisition-manifest.csv`: the same 141 sources with separate availability and coding fields.
- `supplement/review-method-and-coding-notes.md`: Supplementary Note S3, including the discovery query set and source locators.
- `submission/cover-letter-anonymous.tex` and `.pdf`: cover-letter template.
- `submission/review-20260907.md`: Chinese review and revision record.
- `submission/qa-report.md` and `submission-checklist.md`: validation results and author actions.

Standalone wrappers for Figures 4, 6, and 7 can be compiled with `pdflatex` from `figures/`; they embed the supplied PNG pixels without drawing or editing image content. The figure PDFs are already supplied. Publisher reference full texts, temporary extraction files, and Git history are excluded.

## Evidence status

The inventory records 73 retained cited-source full-text artifacts, including nine official references. The 33-source acquisition batch completed in August is a subset of these 73. Sixteen sources have detailed coding for selected comparisons. Further targeted checks and the newly added foundational CAP analysis are recorded separately; availability and selective checking do not imply full-corpus analytical coverage.

The principal discovery cutoff remains 6 August 2026. The September revision performed targeted source and specification checks without repeating the complete discovery search. Remaining submission decisions include current journal/issue requirements, author metadata, disclosures, and any further literature refresh.
