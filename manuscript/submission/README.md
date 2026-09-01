# Anonymous MDPI Blockchains Review Package

## Build

From the package root, run:

```powershell
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The manuscript uses the official MDPI ACS template downloaded on 6 August 2026. The downloaded ZIP had SHA-256:

`44A9464C06E724889E1496A73BE0E6F81099D534BCC9A3DA94B99B52F0ECC563`

`main.tex` includes two inert compatibility shims for an observed MiKTeX 24.3 mismatch between a 2023 LaTeX kernel and 2026 releases of `marginnote`/`colortbl`. Current TeX distributions that already define those interfaces ignore the shims.

## Package contents

- `main.tex`: anonymous MDPI manuscript entry point.
- `sections/`: eleven editable narrative-review sections.
- `figures/`: seven editable TikZ vector figures.
- `Definitions/`: official MDPI class, bibliography style, and assets.
- `references.bib`: 140-entry ACS-style bibliography source.
- `supplement/evidence-matrix.csv`: conservative source inventory and analytical routing.
- `supplement/full-text-acquisition-manifest.csv`: items requiring lawful full-text inspection before final evidence coding.
- `submission/cover-letter-anonymous.tex`: editable anonymous cover-letter template.
- `submission/submission-checklist.md`: pre-submission verification list.

## Evidence status

The manuscript is a complete, compilable narrative-review draft. Bibliographic metadata and citations are verified, lawful full texts have been obtained for all 33 sources in the priority acquisition set, and 16 sources supporting method-specific comparisons have received claim-level coding. The remaining screened records provide discovery and thematic context and form a transparent roadmap for subsequent analytical coding.
