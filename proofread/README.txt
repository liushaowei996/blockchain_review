PRODUCTION PROOF CORRECTIONS — AUTHOR REVIEW DRAFT
Prepared: 2 November 2026

Files
blockchains-4630703.tex       Corrected consolidated source; all changes highlighted.
proofreading-responses.txt   English replies to all 42 production queries.
pending-author-information.txt  Chinese checklist of remaining author confirmations.
reference-verification.txt   Findings and source links for all 49 highlighted references.
reference-verification.json  The same reference audit in structured form.
changes-from-production.diff Complete textual difference from the received TeX.
proofreading-validation.txt  Compilation, cross-reference and layout checks.
Definitions/ and figures/    Unmodified production dependencies.

The corrected 31-page PDF is in:
../output/pdf/blockchains-4630703-author-corrected.pdf

The received PDF, manuscript.v5.zip, references.bib and sections/ are retained as
original attachments. The corrected consolidated TeX contains its bibliography;
the received references.bib and sections/ are not build inputs and were not edited.

Before returning the proof to production
Resolve Q01, Q02, Q03, Q25 and Q26 using pending-author-information.txt, then update
the corresponding TeX comments and response statuses and recompile. No email has
been sent. The current source contains the affiliations and CRediT roles recorded
in the original submission cover letter; funding and final-version agreement
still require the authors' input.

Build from this directory (with a working LaTeX installation), using a distinct
jobname so that the original received PDF is never overwritten. Run twice:
  pdflatex -interaction=nonstopmode -halt-on-error -jobname=blockchains-4630703-author-corrected blockchains-4630703.tex
An existing temporary directory can additionally be supplied with -output-directory.
For this review, compilation outputs were directed to tmp/proofread-work/build,
and only the final PDF was copied to output/pdf/.
