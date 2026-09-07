# Build and Quality Report

Validation date: 7 September 2026 (Asia/Shanghai).
Target: MDPI Blockchains, narrative Review, anonymous submit mode.

## Final artifacts

- Manuscript: 39 A4 pages.
- Approximate English manuscript words: 13,840 using the repository's static estimator.
- Abstract: 187 words, one paragraph; keywords: 8.
- Bibliography and unique cited entries: 141 each.
- Figures: 7; current editable vector Figures 4, 6, and 7; retained raster Figures 1, 2, 3, and 5.
- Editable LaTeX tables: 8.
- Both supplementary CSVs: 141 source identifiers, matching the bibliography exactly.
- Retained cited-source full-text artifacts: 73, including 9 official references.
- Detailed comparison records: 16, each with a page/section locator; additional targeted checks are recorded separately.
- Final manuscript SHA-256: `ac6125c226dbd781a000e4d3a21bd12744e5cd584b352a879e72f8696d38d2dd`.
- Dated source package: `blockchain-review-anonymous-submission-package-20260907.zip`.

## Verification

The manuscript and cover template compiled successfully with `latexmk -pdf -interaction=nonstopmode -halt-on-error` from an isolated package copy. The final log has zero undefined citations/cross-references, duplicate-label warnings, overfull boxes, underfull boxes, or BibTeX warnings. All PDF fonts are embedded Type 1 fonts; the template's former bitmap sans-serif metadata font was replaced with its scalable counterpart.

The local TeX distribution emits an existing package/kernel-version notice and MiKTeX host-support/locale diagnostics. These did not prevent compilation. The final manuscript and the copy in the delivered output directory are byte-identical to the isolated build.

The static manuscript audit exits unsuccessfully on missing citations, duplicate labels or bibliography keys, absent figure files, unresolved tool placeholders, mismatched supplementary source IDs, or detailed coded records without locators. All checks passed. The corrected Zhang bibliography override was checked against the retained metadata cache, and evidence-inventory regeneration was verified to preserve identical outputs. `git diff --check` passed.

## Visual inspection

All 39 final pages were rendered to PNG. Pages 1-18 and 19-30 received independent layout checks; pages 31-39, the declarations, abbreviations, and references were checked during integration. Full-size checks covered the title, assessment/decision equation, descriptive comparison, all revised figures, compact tables, worked decision trace, research propositions, and cover template. No clipping, overlaps, broken labels, missing glyphs, or unreadable diagram text were found.

Floating placement and ragged table columns reduced unnecessary white space and uneven word spacing. The abbreviation heading stays with its table. Figure 4 separates causal hypotheses from evidence status; Figure 6 presents conditional ledger selection and alternatives; Figure 7 shows all six non-cumulative evidence categories.

## Package and anonymity

The package includes the final PDF, current source files, bibliography, figure PDFs and editable sources, supporting CSV/Markdown files, and cover template. Only explicit publication-source file types are included; logs, caches, Git history, local reference full texts, and temporary material are excluded. Its internal SHA-256 manifest permits file-level verification. Packaged source files and final PDFs were checked against the workspace copies, and PDF/source checks found no local account name, identifying repository URL, or unresolved tool citation token. Author metadata remains anonymous.

## Scientific scope of this revision

This was a substantive narrative-review revision with targeted primary-source checks, not a repeat of the complete discovery search or a new integrated empirical evaluation. Sixteen detailed comparison records do not represent uniform coding of the full corpus. Supplementary Note S3 and `review-20260907.md` document the changes and evidence boundaries. Remaining author and submission decisions are listed in `submission-checklist.md`.
