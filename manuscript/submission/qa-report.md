# Build and Quality Report

## 30 September 2026: Cover-Letter Policy and Draft

The journal-specific Instructions for Authors were checked for the cover-letter requirements and double-anonymized review policy. The new `cover-letter-draft.txt` uses the current manuscript title and describes its narrative review, conceptual framework, illustrative example, and evaluation agenda. A separate review checked the scientific descriptions against the manuscript. All six supplied authors and their affiliation mapping are recorded, with author order, romanization, remaining metadata, and declarations explicitly pending confirmation. The draft is not a submission-ready final letter.

The package builder now excludes cover letters. A temporary build verified 27 publication files, ZIP CRC integrity, and byte-for-byte agreement between every archived file and its manuscript source. Additional checks passed for the letter's title, six author names, corresponding-author email, pending-data labels, absence of the former promise to defer author information until after review, and `git diff --check`. The manuscript and existing dated archives were not changed. The older anonymous cover-letter artifacts are marked as superseded in `README.md`.

## 29 September 2026: Title and Wording Revision

The revised title is "Blockchain-Assisted Mission Trust in Air--Surface--Underwater Unmanned Systems: A Review and Conceptual Framework." Two passages in Section 3 clarify the participating research institutions and supporting observations from independent sensors or platforms. The cover-letter title and the English title and Chinese interpretation in the reading guide are synchronized.

The manuscript and cover letter compiled successfully from an isolated copy of the publication sources. The manuscript has 37 A4 pages, and the cover letter has one page. The static audit passes with 141 bibliography entries and 141 unique cited entries, with no missing figures, unresolved references, duplicate labels, or tool placeholders. The compiled bibliography is byte-identical to the preceding version. The final build logs contain no undefined citations or references, duplicate-label warnings, overfull boxes, or underfull boxes. The manuscript build retains the existing LaTeX release-version notice.

PDF text and metadata checks confirm the new title and both revised passages. All 37 manuscript pages were rendered and reviewed in contact sheets; full-page inspection covered pages 1, 5, and 6 and the cover letter. The title, affected paragraphs, figures, tables, and page boundaries are correctly placed. Delivered PDF copies match the isolated build byte for byte. The 29 September source package is checked against the explicit publication-file list and the workspace files.

- Manuscript SHA-256: `bc139dc08e7b4b1dfa170b9cc28b3b1fa3be46636154401d70d6ccbdc60c31e4`.
- Cover-letter SHA-256: `17689cbbbbbfbc02f7832b582da397a237f4ab6e03e95adcc9561eda9c97c74e`.
- Source package: `blockchain-review-anonymous-submission-package-20260929.zip`.

The remainder of this file preserves the 7 September validation record; its page counts, hashes, and package descriptions refer to that earlier version.

---

Validation date: 7 September 2026 (Asia/Shanghai).
Target: MDPI Blockchains, narrative Review, anonymous submit mode.

## Final artifacts

- Manuscript: 38 A4 pages after the language revision.
- Approximate English manuscript words: 13,837 using the repository's static estimator.
- Abstract: 191 words, one paragraph; keywords: 8.
- Bibliography and unique cited entries: 141 each.
- Figures: 7, using the image-generated raster artwork from the preceding figure revision. The current PNG masters and image-only PDF wrappers for Figures 4, 6, and 7 are included.
- Editable LaTeX tables: 8.
- Both supplementary CSVs: 141 source identifiers, matching the bibliography exactly.
- Retained cited-source full-text artifacts: 73, including 9 official references.
- Detailed comparison records: 16, each with a page/section locator; additional targeted checks are recorded separately.
- Final manuscript SHA-256: `7b5427285300c3691ddeb56c23a66256f97bf7eb8041f4b080e9951454e1b17e`.
- Dated source package: `blockchain-review-anonymous-submission-package-20260907.zip`.

## Language and content verification

The language revision covers the abstract, eleven manuscript sections, figure/table captions, and Supplementary Note S3. It presents contributions, scope, and evidence conditions directly and uses literature, mechanisms, analytical results, and evaluation procedures as the principal subjects. Section 10 is titled “Scope and Applicability of the Review and Framework.”

Comparison with the preceding manuscript confirms identical citation sequences, labels and cross-references, figure-inclusion commands, displayed equations, inline mathematical expressions, and numeric-token counts in each of the twelve manuscript source files. The order of model version 4.2 and UAV-7 changes within one rewritten sentence; the qualified dependency has the same meaning. Manual comparison confirms the six research hypotheses retain their directions, comparators, outcomes, and experimental conditions. The CTG example retains its gates, acquisition-age intervals, common-localization concern, and preauthorized fallback decision.

The bibliography, generated bibliography text, two CSV inventories, and all figure assets retain their preceding contents. Supplementary Note S3 retains the exact discovery queries and all sixteen source identifiers and page/section locators. Scientific conditions concerning causality, evidence dependence, calibration, timing, governance, and transfer are expressed as requirements for the corresponding claims.

## Build and static checks

The current manuscript compiled successfully with `latexmk -pdf -interaction=nonstopmode -halt-on-error` from an isolated copy of the publication sources. The abbreviation heading and table are grouped to keep them on the same page. The final manuscript log has zero undefined citations/cross-references, duplicate-label warnings, overfull boxes, underfull boxes, or BibTeX warnings. All PDF font resources are embedded Type 1 fonts. The cover template and figure wrappers retain their successful builds from the preceding revisions.

The local TeX distribution emits an existing package/kernel-version notice and MiKTeX host-support/locale diagnostics. Compilation completed successfully. The manuscript PDF and its delivered output copy are byte-identical to the isolated build.

The static manuscript audit checks citation resolution, bibliography identities, labels, figure paths, tool placeholders, supplementary source identifiers, and locators for detailed coded records. All checks passed. The language/content invariants, supplementary query/locator comparison, and `git diff --check` also passed.

## Visual inspection

All 38 final pages were rendered to PNG and inspected in page contact sheets. Full-page checks covered the title and abstract, the CTG decision example, the revised scope section, and the declarations/abbreviation transition. Figures, captions, tables, reference entries, and page margins remain legible and correctly placed. The abbreviation heading and its complete table share page 32. Page checks found intact glyphs, clear spacing, and correctly bounded text and artwork.

The seven figure images preserve the preceding visual style and scientific distinctions. The prior image revision verified the exact match between the decoded pixels in the three replacement PDF wrappers and their PNG masters. This language revision retains those assets.

## Package and anonymity

The package contains the final PDF, manuscript sources, bibliography, figure PDFs, current PNG masters and generation prompts, supporting CSV/Markdown files, and cover template. An explicit publication-source file list defines its contents; publisher reference full texts, temporary files, caches, and Git history remain outside the package. The internal SHA-256 manifest supports file-level verification. Package integrity, manifest entries, and agreement with the workspace files were checked. The compiled TeX, bibliography, and figure inputs match the delivered source inputs.

PDF text/metadata and distributed source checks confirm anonymous author metadata and the absence of local account paths, identifying repository URLs, and unresolved tool citation tokens. The discovery record and scientific evidence retain their preceding status; this revision concerns language and its resulting layout. Supplementary Note S3 and `review-20260907.md` document the source scope and revision history. Submission preparation items appear in `submission-checklist.md`.
