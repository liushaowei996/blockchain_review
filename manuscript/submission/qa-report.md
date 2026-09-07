# Build and Quality Report

Validation date: 7 September 2026 (Asia/Shanghai).
Target: MDPI Blockchains, narrative Review, anonymous submit mode.

## Final artifacts

- Manuscript: 38 A4 pages after the image-style revision.
- Approximate English manuscript words: 13,840 using the repository's static estimator.
- Abstract: 187 words, one paragraph; keywords: 8.
- Bibliography and unique cited entries: 141 each.
- Figures: 7; all use image-generated raster artwork. Figures 4, 6, and 7 were regenerated for the current revision; their PNG masters and image-only PDF wrappers are included.
- Editable LaTeX tables: 8.
- Both supplementary CSVs: 141 source identifiers, matching the bibliography exactly.
- Retained cited-source full-text artifacts: 73, including 9 official references.
- Detailed comparison records: 16, each with a page/section locator; additional targeted checks are recorded separately.
- Final manuscript SHA-256: `8b189b978db3daf68a9682debc5269b2f2a803e7c4eaf866dc73470bc5481c90`.
- Dated source package: `blockchain-review-anonymous-submission-package-20260907.zip`.

## Verification

The current manuscript compiled successfully with `latexmk -pdf -interaction=nonstopmode -halt-on-error` from an isolated package copy. The three image-only figure wrappers also compiled successfully with `pdflatex`; the cover template retains its successful build from the preceding review round. The final manuscript log has zero undefined citations/cross-references, duplicate-label warnings, overfull boxes, underfull boxes, or BibTeX warnings. All PDF font resources are embedded Type 1 fonts.

The local TeX distribution emits an existing package/kernel-version notice and MiKTeX host-support/locale diagnostics. These did not prevent compilation. The final manuscript and the copy in the delivered output directory are byte-identical to the isolated build.

The static manuscript audit exits unsuccessfully on missing citations, duplicate labels or bibliography keys, absent figure files, unresolved tool placeholders, mismatched supplementary source IDs, or detailed coded records without locators. All checks passed again after the figure replacement. `git diff --check` passed. The bibliography-override and evidence-inventory regeneration checks belong to the preceding scientific revision; those inputs were not modified in this image-style revision.

Each new figure PDF contains one embedded raster image. Its decoded RGB pixels match the corresponding PNG master exactly; the PNG copies in the manuscript and project image-generation directory are byte-identical. Native dimensions are 1647 × 955 (Figure 4), 1694 × 928 (Figure 6), and 1536 × 1024 (Figure 7). No post-generation pixel editing was performed.

## Visual inspection

All 38 current pages were rendered to PNG and inspected in page contact sheets, including the title, tables, declarations, abbreviations, and references. Pages 15, 19, and 23 received additional full-page checks for Figures 4, 6, and 7, their captions, and surrounding layout. The native generated images were also inspected for spelling, arrow endpoints, grouping, and scientific meaning. No clipping, overlaps, broken labels, or missing glyphs were found.

The abbreviation heading stays with its table. Figure 4 separates causal hypotheses from evidence status, and its secondary dependency connector is routed above the object row so every exposure arrow points clearly to its own object. Figure 6 presents conditional ledger selection and alternatives and now uses the full text width. Figure 7 shows all six non-cumulative evidence categories in equally sized illustrated panels. The three figures match the warm-white background, navy/teal palette, and restrained dimensional icon style of the retained artwork.

## Package and anonymity

The package includes the final PDF, current source files, bibliography, figure PDFs, the three revised PNG masters and their exact generation prompts, supporting CSV/Markdown files, and cover template. Only explicit publication-source file types are included; logs, caches, Git history, local reference full texts, and temporary material are excluded. Its internal SHA-256 manifest permits file-level verification. Packaged source files and final PDFs were checked against the workspace copies, and PDF/source checks found no local account name, identifying repository URL, or unresolved tool citation token. Author metadata remains anonymous.

## Scientific scope of this revision

The preceding narrative-review revision included targeted primary-source checks. The subsequent image-style revision changes the three figures and Figure 6's insertion width; manuscript claims and captions retain the preceding revision. The discovery search and empirical evaluation were not repeated. Sixteen detailed comparison records do not represent uniform coding of the full corpus. Supplementary Note S3 and `review-20260907.md` document the changes and evidence boundaries. Remaining author and submission decisions are listed in `submission-checklist.md`.
