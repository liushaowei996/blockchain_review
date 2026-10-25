# Anonymous MDPI Blockchains Review Package

## Cover-letter policy verified on 30 September 2026

The [Blockchains Instructions for Authors](https://www.mdpi.com/journal/blockchains/instructions#coverletter) require the cover letter to include every author's full name and affiliation, together with details of identifying information removed from the manuscript. The journal uses double-anonymized peer review; the manuscript remains anonymous, while the cover letter supplies the author information to the Editorial Office. Prior submissions of the manuscript to MDPI must be disclosed. Suggested or excluded reviewers belong in the submission system.

The completed letter is `../../output/pdf/cover-letter-blockchains.pdf`; its editable text is `cover-letter.txt`. It contains a one-page submission letter followed by author information and declarations. Upload both pages together in the Cover Letter field. The Special Issue remains "Feature Papers in Blockchains 2026", following the existing submission plan. The [journal's Special Issues list](https://www.mdpi.com/journal/blockchains/special_issues) listed this issue as open, with a 31 December 2026 deadline, when checked.

The existing `cover-letter-anonymous.tex`, its PDF copies, and cover letters inside the dated archives are superseded historical templates. Do not submit them. Upload the completed cover letter separately from the anonymous manuscript source archive. The package builder now excludes cover letters; historical ZIP files have not been altered.

Author names and affiliations follow the information supplied on 30 September. Chengnian Long's email, `longcn@sjtu.edu.cn`, was confirmed by the user and is also listed on his [official university profile](https://sais.sjtu.edu.cn/faculty/636.html). The company name "SF Technology Co., Ltd." appears in SF's [English service agreement](https://cdn-fusionwork.sf-express.com/v1.2/AUTH_FS-BASE-SERVER-PRD-DR/sfosspublic001/forespace-next-service-agreement-en-us.html). The supplied Shenzhen office address and postal code 518057 match the company's [English annual report](https://ir.sf-express.com/media/taphlcnt/2022-annual-report-e.pdf). The institute's postal code 222061 is recorded in its [CHSI admissions notice](https://yz.chsi.com.cn/sch/viewBulletin--infoId-2613916908,categoryId-480659,schId-368165,mindex-12.dhtml).

The user confirmed unpublished status, exclusive submission, all-author approval, and no prior MDPI submissions or related versions. CRediT roles were drafted at the user's request according to author order: the first author leads literature investigation, drafting, and visualization; the second contributes to conceptualization and methodology; all authors participate in review and editing; the corresponding author provides conceptual guidance and supervision. The letter retains the manuscript's no-conflict declaration. Funding is omitted at the user's explicit request; the letter makes no claim that the research received no funding. No acknowledgment was added.

To rebuild the letter, run `python scripts/build_cover_letter.py` from the repository root with ReportLab installed. The renderer embeds the Windows Times New Roman fonts; `--font-dir` can specify another directory containing those font files.

## Current version: refined layout, writing and evidence schematic, 25 October 2026

The current clean and marked manuscripts each have 31 pages, 123 cited references, seven Visio-exported figures and twelve tables. A disclosed full-text sample of 39 mechanism studies supplies 89 OAL claim records. The revision includes a partition/revocation/reconciliation illustration, a coalition ledger specification, a matched validating-log baseline, a requirement-driven consensus comparison and reproducible supplemental calculations. The source-text estimate falls from 13,389 to 9,936 words (25.8%) using the same procedure on both versions.

Use `../../output/blockchain-review-layout-refined-source-20261025.zip` for the current anonymous source package. It contains the clean manuscript and supplementary files. The independent reviewer replies are in `../../review/revision-1/`. The clean PDF is `../../output/pdf/blockchain-mission-trust-review-layout-refined.pdf`; the companion `blockchain-mission-trust-review-layout-refined-marked.pdf` highlights rewritten body text in blue, with figures and tables retaining publication styling. It omits deletions and is not a word-level redline. Detailed change locations and the evidence boundaries are recorded in `../../review/revision-1/README.md`.

This round places Figure 5 at 90% of the text width with its discussion on page 14 and brings Tables 2 and 9 onto text pages. Thirty-three local prose edits remove repeated defensive framing and revision-process commentary while retaining evidence gaps, validation conditions and substantive limitations; the audit is `../../review/revision-1/writing-audit-20261025.txt`. Figure 7 now uses six native Visio text-and-box panels with straight arrows to relate inputs, reasoning or evaluation, and outputs. Its category colors remain. Only Figure 7's PDF and native page change in this round; Figures 1–6 remain byte-identical to the expanded OAL version. Reviewer 2's response is synchronized with these changes.

The September archives, earlier October source archives and cover letter remain historical submission records. The present revision does not update or submit the cover letter. The current figure PDFs are exported from the supplied multipage Visio source, whose original uploaded file is unchanged. Figures 1–6 preserve the established artwork, including enlarged labels, corrected wording, the populated heatmap paired with the OAL schematic and revised comparator labels. The October 22 simplified drawings are superseded. Earlier image masters and slide files elsewhere in the repository describe historical versions.

## Build

From the extracted package root, run:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The official MDPI template was obtained on 6 August 2026. Its archived download SHA-256 is `44A9464C06E724889E1496A73BE0E6F81099D534BCC9A3DA94B99B52F0ECC563`. The existing compatibility shims address the locally installed older MiKTeX/LaTeX combination. The revision was also built from an isolated copy of the packaged sources.

## Contents

- `main.tex`, `sections/`, `references.bib`, `main.bbl`, and `main.pdf`: editable clean source and compiled manuscript.
- `main-marked.tex`: generated companion with section-level blue highlighting; compile separately when needed.
- `Definitions/`: MDPI class, bibliography style, and template assets.
- `figures/`: seven publication PDFs with vector geometry and text, plus the editable `Figures-revised.vsdx`. Figure 2 retains one raster lighthouse illustration; Figures 1 and 3–7 contain no raster images.
- `supplementary/`: claim/study/reference-role registers, coding decisions, expansion screening, stratified and sensitivity outputs, codebook, query records, consensus requirements, application specification, executable replay, computed results, OAL aggregation script, Figure 7 native-page builder and Visio PDF export script.

Run `python supplementary/replay_case.py`, `python supplementary/build_figures.py --data-only`, and `python supplementary/analyze_oal.py` from an extracted manuscript package with Python 3.10 or later and `cryptography` installed. Exporting the editable figure pages additionally requires Microsoft Visio for Windows: run `python supplementary/build_figures.py` without `--data-only`, or invoke `supplementary/export_visio_figures.ps1`. Manuscript compilation uses the supplied PDFs and does not require Visio. For a data change, run `supplementary/update_oal_visio.ps1` to update and export only Figure 3; its Python helper preserves all other native pages. To regenerate Figure 7's text-and-box schematic, run `python supplementary/update_evidence_visio.py`, then `./supplementary/export_visio_figures.ps1 -FigureNumbers 7`; the other six pages and PDFs are preserved. The scripts identify their own paths. The replay runs synthetic rule checks; it does not run Fabric, consensus or a field trial. Full texts, temporary extraction files, credentials, identifying cover letters and Git history are excluded from the archive.

## Evidence status

The original OpenAlex discovery date is 6 August 2026. Targeted expansion checks extend through 25 October 2026. The bibliography's 123 references contain 39 coded mechanisms and 84 contextual/evaluation sources. Nineteen coded studies target UAV, AIS or underwater applications; twenty supply transferable mechanisms. Four of the 14 previously uncoded original candidates were recovered; ten remain incompletely accessible. The source/version, screening and coding registers expose these choices. Descriptive sensitivity checks include all 39 leave-one-out maps. The sole L4 assignment is scoped to a bounded physical UAV-node experiment and also tested under an L3-only reading. Empty cells, absent L5 and unobserved integrated mission validation describe the extracted sample, not the whole literature.
