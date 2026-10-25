# Build and Quality Report

## 25 October 2026: Retained Visio Artwork and Targeted Figure Revisions

The seven publication figures are exported from the supplied multipage Visio source. Inspection confirms that the original PDFs already contained vector text and diagram geometry. The revised drawing preserves the original architecture, claim gates, dependency icons, eight-stage CTG loop, two-hub ledger/control structure, and six evidence-profile cards. Labels and spacing are enlarged in Figures 1, 4, 5 and 6; Figure 2 and Figure 4 spelling is corrected. Figure 3 combines the original OAL schematic with the populated heatmap, and Figure 6 uses the matched policy-validating witnessed-log comparator. Figure 7 replaces only the six photo-realistic illustrations with native Visio schematics. The response to Reviewer 2, Comment 9, describes this provenance and the actual changes.

All seven PDFs have selectable vector text. Raster-image object counts are 0, 1, 0, 0, 0, 0 and 0; the remaining image is the original lighthouse illustration in Figure 2. The native heatmap's 96 cell values agree with `oal-cell-counts.csv`. Regenerated OAL CSV/JSON files match the preceding source package byte for byte. The source extraction, replay implementation, numerical results and bibliography are unchanged. The original supplied VSDX remains byte-identical, with SHA-256 `91304529a425d154163223a774fcee4e22eb62b87cd8483b8683990ced26d17e`. The revised VSDX contains anonymous document properties and is included with a read-only PDF export script.

Both manuscript versions compile from an isolated copy of the explicitly listed package files. Each has 30 pages, 111 cited references, seven figures and ten tables. The static word estimate is 9,771, a 27.0% reduction from the same 13,389-word baseline. There are no missing citations, unresolved references, duplicate labels, missing figures, tool placeholders, overfull boxes or oversized floats. The existing LaTeX release-version notice and one underfull box remain. The bibliography is byte-identical to the supplied BBL. All 30 clean and 30 marked pages were reviewed in rendered sheets; the seven figure pages were also checked at full-page scale. Figures 1–4 and 6–7 use the MDPI template's extended figure width; Figure 5 uses the body width.

The two independent MDPI-template replies have 3 and 9 pages. This update changes only `word/document.xml` in each file and preserves the other 26 parts byte for byte. Black reviewer-comment paragraphs, general-evaluation ratings and English-language assessments remain unchanged. The modified replies were rendered with LibreOffice 26.8.0.3 and all 12 pages inspected. The final word-estimate correction changes only page 8 of Reviewer 2's rendered reply. Figure 3 descriptions and Reviewer 2's figure-provenance response agree with the revised artwork.

The dated source archive contains 46 files, including `figures/Figures-revised.vsdx` and `supplementary/export_visio_figures.ps1`. ZIP CRC and manifest checks pass, and every archive member agrees byte for byte with the isolated build inputs/results. Final artifact hashes and individual figure checks are recorded in `../../review/revision-1/verification.json`. The dated records below describe earlier artifact states.

## 22 October 2026: First Review Revision

The revision applies OAL to 23 full-text mechanism studies through 49 scoped claim records, replaces the empty grid with a generated heatmap, specifies a coalition provenance/revocation application, and adds an executable synthetic replay. The ledger and policy-validating witnessed-log paths share the same evidence and authorization rules. The manuscript reports their equality under those rules and confines implementation comparisons to explicitly stated assumptions. It does not report a Fabric deployment, consensus benchmark or sea trial.

The source-text estimate is 13,389 words at the pre-revision baseline (`bfb8054`) and 9,743 in the revision, using the same static estimator: a 27.2% reduction. This contemporaneous baseline count supersedes the earlier 7 September estimate for the present comparison. The current manuscript has 29 pages, 111 resolved/used bibliography entries, seven vector figures and ten tables. The full-text sample and 14 original mechanism candidates outside completed numerical coding are disclosed in the paper and supplementary citation dispositions. No retrospective systematic-screening flow or independent duplicate coding is claimed.

`audit_manuscript.py` passes with no missing/unused citations, duplicate labels, unresolved references, missing figures or tool placeholders. The clean manuscript builds successfully from the working sources and from an independently extracted source package. The rebuilt bibliography matches the supplied BBL byte for byte. The final build logs have no undefined citations/references, duplicate-label warnings or overfull boxes. One underfull box and the existing MiKTeX host-support/LaTeX-kernel notices do not prevent compilation. PDF metadata retain anonymous authors.

The source archive contains 44 explicitly listed files. ZIP CRC, manifest and source-byte agreement checks pass. The replay and drawing scripts run from the extracted package; all supplemental CSV/JSON outputs reproduce byte for byte. Checks cover Ed25519 verification and altered-record rejection, Merkle inclusion and malformed/padding-index rejection, six arrival orders and duplicate handling, all 16 signer subsets, local expiry, exact application serialization and 63 assumed quorum/partition combinations. The heatmap has 20 nonempty cells; overlapping evidence profiles are L0=4, L1=6, L2=13, L3=11, L4=0 and L5=0. All seven figure PDFs contain selectable vector text and zero raster images. Their source uses programmatic drawing with no photographic or generated-image assets.

The two independent response DOCXs use the supplied MDPI review-article template. All supplied reviewer comments are preserved verbatim after whitespace normalization. The supplied screenshots record significance/organization/scientific-soundness/reference ratings of 3/4/4/5 for Reviewer 1 and 4/4/3/3 for Reviewer 2, each out of five. Both reviewers select “The English is fine and does not require any improvement.” The general-evaluation table and English-language response now reflect these assessments; the earlier missing-rating explanations are removed. Package checks confirm that only `word/document.xml` and `word/settings.xml` change, with 25 original ZIP parts preserved byte for byte. The original template SHA-256 remains `06c3fc33ddac695e6054116a649efde95ac069f9613a1026576ba5fc20d99e23`. LibreOffice 26.8.0.3 is installed at `C:/Program Files/LibreOffice/program/soffice.exe` and was used to render the replies. Template/content comparisons use `render_and_diff.py`; final pagination is additionally rendered and inspected. The final replies have 3 and 9 pages. Paragraph-sized template rows keep reply paragraphs intact across page breaks. The final marked manuscript was also inspected across all 29 pages. Artifact hashes and the compact verification record are in `../../review/revision-1/verification.json`.

The clean manuscript was inspected across all 29 rendered pages, with full-page checks of the evidence heatmap, consensus table, protocol and communication budget. The companion marked manuscript uses section-level blue body text and retains publication styling for figures and tables; it is explicitly labeled as an addition/rewrite view, not a word-level deletion redline. Revision locations and unresolved empirical work are listed in `../../review/revision-1/README.md`. Historical figures, archives and cover-letter files are not part of the current source package. Full texts, extraction files and temporary rendering artifacts remain outside Git.

## 30 September 2026: Completed Identifying Cover Letter

The user supplied all six authors and their affiliations, confirmed Chengnian Long's correspondence address, confirmed unpublished and exclusive-submission status and all-author approval, and confirmed no prior MDPI submissions or related versions. The user authorized a CRediT allocation based on author order, reported no acknowledgment, and explicitly requested omission of funding from the cover letter. The final letter follows these instructions, retains the existing Special Issue destination and manuscript no-conflict declaration, and contains no funding statement. Postal codes were checked against SF's official reports and the institute's CHSI admissions notice, linked in `README.md`.

`cover-letter.txt` replaces the provisional draft. `output/pdf/cover-letter-blockchains.pdf` contains two A4 pages: the submission letter and a page of author information and declarations. Both final pages were rendered and visually inspected; text, spacing, page boundaries, and affiliations are legible, with no clipping or overlap. The PDF's extracted text exactly matches the editable text after whitespace normalization, and the Times New Roman font subsets are embedded. Checks passed for the six authors, dual affiliation of the first author, correspondence address, three postal codes, and absence of placeholders, funding text, and acknowledgments. An independent content review confirmed the conceptual and narrative scope of the scientific claims.

The new `blockchain-review-anonymous-submission-package-20260930.zip` contains 27 files. Its manifest is identical to the 29 September archive except for removal of the two obsolete anonymous cover-letter files. Every retained file is byte-identical to the corresponding earlier archive entry. ZIP CRC checks and `git diff --check` pass. The manuscript itself has not been edited by this cover-letter task.

- Cover-letter PDF SHA-256: `2dc2c008f85bd3732635d143f19d791dfa44cc8b4f4296211b97409e5cca412a`.
- Anonymous source ZIP SHA-256: `e475b93a3146cdf22c592dafd394c2186dcd861b7238c0041f2c1e90c8e3c0a3`.

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
