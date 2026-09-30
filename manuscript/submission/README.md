# Anonymous MDPI Blockchains Review Package

## Cover-letter policy verified on 30 September 2026

The [Blockchains Instructions for Authors](https://www.mdpi.com/journal/blockchains/instructions#coverletter) require the cover letter to include every author's full name and affiliation, together with details of identifying information removed from the manuscript. The journal uses double-anonymized peer review; the manuscript remains anonymous, while the cover letter supplies the author information to the Editorial Office. Prior submissions of the manuscript to MDPI must be disclosed. Suggested or excluded reviewers belong in the submission system.

`cover-letter-draft.txt` contains the revised letter body and explicit fields for the missing author information and declarations. It is **not ready for submission** until those fields and author confirmations are complete. The Special Issue follows the existing plan and requires confirmation from the authors. The [journal's Special Issues list](https://www.mdpi.com/journal/blockchains/special_issues) listed "Feature Papers in Blockchains 2026" as open, with a 31 December 2026 deadline, when checked.

The existing `cover-letter-anonymous.tex`, its PDF copies, and cover letters inside the dated archives are superseded historical templates. Do not submit them. Upload the completed cover letter separately from the anonymous manuscript source archive. The package builder now excludes cover letters; historical ZIP files have not been altered.

Author names and supplied affiliations in the draft come from the authors' 30 September message; order and romanization await confirmation. Chengnian Long's email is supported by his [official university profile](https://sais.sjtu.edu.cn/faculty/636.html). The company name "SF Technology Co., Ltd." appears in SF's [English service agreement](https://cdn-fusionwork.sf-express.com/v1.2/AUTH_FS-BASE-SERVER-PRD-DR/sfosspublic001/forespace-next-service-agreement-en-us.html); the authors' preferred address and postal code remain to be confirmed. No funding, contribution, publication-history, or approval facts have been inferred from author affiliations.

## Current version

The 29 September 2026 revision adopts the title "Blockchain-Assisted Mission Trust in Air--Surface--Underwater Unmanned Systems: A Review and Conceptual Framework." Section 3.1 identifies research institutions operating unmanned platforms among the participating organizations, and Section 3.3 specifies supporting observations from independent sensors or platforms. The cover letter and Chinese reading-guide title are synchronized. The current manuscript has 37 pages; the updated publication files are packaged in `blockchain-review-anonymous-submission-package-20260929.zip`.

The 7 September 2026 revision is a narrative Review and conceptual synthesis. It includes a revised OAL assessment/decision interface, a bounded CTG worked example, conditional ledger-selection criteria, and a claim-specific evidence profile. The figure-style revision regenerated Figures 4, 6, and 7 with the built-in image generation tool to match the retained artwork while preserving the revised scientific distinctions. The subsequent language revision presents the contribution, scope, and evidence conditions directly, with literature, mechanisms, and analytical results as the principal subjects. The scientific claims, research propositions, mathematical expressions, numerical examples, cited sources, and figure artwork retain their preceding content.

## Build

From the extracted package root, run:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The official MDPI template was obtained on 6 August 2026. Its archived download SHA-256 is `44A9464C06E724889E1496A73BE0E6F81099D534BCC9A3DA94B99B52F0ECC563`. The existing compatibility shims address the locally installed older MiKTeX/LaTeX combination. The revision was also built from an isolated copy of the packaged sources.

## Contents

- `main.tex`, `sections/`, `references.bib`, `main.bbl`, and `main.pdf`: editable source and compiled manuscript.
- `Definitions/`: MDPI class, bibliography styles, and assets.
- `figures/`: seven publication PDFs containing image-generated raster artwork. Figures 4, 6, and 7 include the current PNG masters, standalone PDF wrappers, and `image-generation-prompts-20260907.md`. Historical TikZ drawing sources document earlier working versions; the manuscript uses the supplied figure PDFs.
- Historical archives include `submission/cover-letter-anonymous.tex` and `.pdf`; these templates are superseded and must be removed before using an old archive for submission. The current package builder excludes cover letters.
- `submission/review-20260907.md`: Chinese review and revision record.
- `submission/qa-report.md` and `submission-checklist.md`: validation results and author actions.

Standalone wrappers for Figures 4, 6, and 7 can be compiled with `pdflatex` from `figures/`; they embed the supplied PNG pixels without drawing or editing image content. The figure PDFs are already supplied. Publisher reference full texts, temporary extraction files, and Git history are excluded.

## Evidence status

The principal discovery cutoff remains 6 August 2026. The September scientific revision performed targeted source and specification checks using the August discovery export as its retrieval baseline. The figure and language revisions refine the presentation of that synthesis. Submission preparation includes confirmation of current journal/issue requirements, author metadata, disclosures, and the timing of any further literature refresh.
