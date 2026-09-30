# Anonymous MDPI Blockchains Review Package

## Cover-letter policy verified on 30 September 2026

The [Blockchains Instructions for Authors](https://www.mdpi.com/journal/blockchains/instructions#coverletter) require the cover letter to include every author's full name and affiliation, together with details of identifying information removed from the manuscript. The journal uses double-anonymized peer review; the manuscript remains anonymous, while the cover letter supplies the author information to the Editorial Office. Prior submissions of the manuscript to MDPI must be disclosed. Suggested or excluded reviewers belong in the submission system.

The completed letter is `../../output/pdf/cover-letter-blockchains.pdf`; its editable text is `cover-letter.txt`. It contains a one-page submission letter followed by author information and declarations. Upload both pages together in the Cover Letter field. The Special Issue remains "Feature Papers in Blockchains 2026", following the existing submission plan. The [journal's Special Issues list](https://www.mdpi.com/journal/blockchains/special_issues) listed this issue as open, with a 31 December 2026 deadline, when checked.

The existing `cover-letter-anonymous.tex`, its PDF copies, and cover letters inside the dated archives are superseded historical templates. Do not submit them. Upload the completed cover letter separately from the anonymous manuscript source archive. The package builder now excludes cover letters; historical ZIP files have not been altered.

Author names and affiliations follow the information supplied on 30 September. Chengnian Long's email, `longcn@sjtu.edu.cn`, was confirmed by the user and is also listed on his [official university profile](https://sais.sjtu.edu.cn/faculty/636.html). The company name "SF Technology Co., Ltd." appears in SF's [English service agreement](https://cdn-fusionwork.sf-express.com/v1.2/AUTH_FS-BASE-SERVER-PRD-DR/sfosspublic001/forespace-next-service-agreement-en-us.html). The supplied Shenzhen office address and postal code 518057 match the company's [English annual report](https://ir.sf-express.com/media/taphlcnt/2022-annual-report-e.pdf). The institute's postal code 222061 is recorded in its [CHSI admissions notice](https://yz.chsi.com.cn/sch/viewBulletin--infoId-2613916908,categoryId-480659,schId-368165,mindex-12.dhtml).

The user confirmed unpublished status, exclusive submission, all-author approval, and no prior MDPI submissions or related versions. CRediT roles were drafted at the user's request according to author order: the first author leads literature investigation, drafting, and visualization; the second contributes to conceptualization and methodology; all authors participate in review and editing; the corresponding author provides conceptual guidance and supervision. The letter retains the manuscript's no-conflict declaration. Funding is omitted at the user's explicit request; the letter makes no claim that the research received no funding. No acknowledgment was added.

To rebuild the letter, run `python scripts/build_cover_letter.py` from the repository root with ReportLab installed. The renderer embeds the Windows Times New Roman fonts; `--font-dir` can specify another directory containing those font files.

## Current version

The 30 September 2026 package, `blockchain-review-anonymous-submission-package-20260930.zip`, contains the same 37-page manuscript and publication sources as the 29 September package, with both obsolete anonymous cover-letter files removed. The completed, identifying cover letter is supplied separately.

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
