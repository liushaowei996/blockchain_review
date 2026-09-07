# Manuscript Figure Assets

All seven current figures use artwork generated with the built-in image generation tool. On 7 September 2026, Figures 4, 6, and 7 were regenerated to match the retained artwork while preserving the preceding scientific revision. The final PNG files are wrapped without pixel edits in PDF containers under `manuscript/figures/` and inserted into the manuscript. The TeX wrappers for Figures 4, 6, and 7 now embed the supplied PNGs; all TikZ drawing sources are historical working versions. No CLI/API fallback was used.

| Figure | Disposition |
|---|---|
| 1 | Regenerated from a blank prompt to clarify flow and color semantics |
| 2 | Regenerated from a blank prompt |
| 3 | Regenerated from a blank prompt to correct axis geometry |
| 4 | Regenerated on 7 September; causal hypotheses and evidence status separated; final routing correction applied |
| 5 | Existing generated original retained |
| 6 | Regenerated on 7 September; conditional ledger selection and alternatives retained |
| 7 | Regenerated on 7 September; six equally prominent, non-cumulative evidence categories |

## Shared visual direction

- Use case: scientific-educational / scholarly journal infographic
- Canvas: wide landscape on a warm-white background
- Style: premium editorial scientific infographic with crisp geometry, restrained 2.5D depth, consistent icons, generous whitespace, and print-readable labels
- Palette: navy, ocean teal, cyan, muted orange, violet, slate, and limited coral accents
- Constraints: no logos, watermarks, equations, decorative circuitry, military weapons, cryptocurrency branding, or dense paragraph text

## Figure 1 — Cross-domain reference architecture

File: `figure-01-reference-architecture.png`

Final prompt: Generate a brand-new, deliberately simplified cross-domain mission-trust reference architecture with exactly three columns inside a dashed `Assurance + Governance` enclosure: `MISSION PLATFORMS` contains `UAV`, `Satellite / HAPS`, `USV Gateway`, and `UUV / AUV`; `EDGE + SHORE` contains `Shore Services` and `Encrypted Evidence Store`; `SHARED TRUST SERVICES` contains `Policy + Ledger` and `Auditor`. Use neutral gray topology lines and the tags `RADIO` and `ACOUSTIC / OPTICAL` for communication media. Use solid teal left-to-right arrows only for data and evidence: `TELEMETRY + MISSION DATA` to shore services, `SIGNED LOGS + ENCRYPTED CONTENT` to the evidence store, and `COMMITMENTS + STATE UPDATES` to policy and ledger. Use one separate dashed violet right-to-left lane for `POLICY + MEMBERSHIP + REVOCATION`, and local dotted slate bidirectional links for audit and reconciliation. Put the three arrow meanings in one bottom legend. Every colored line must begin and end on its named group or node; forbid crossings, empty-space endpoints, perimeter-spanning loops, additional arrow colors, duplicate arrows, tiny text, decorative circuitry, cryptocurrency symbols, weapons, logos, and watermarks.

## Figure 2 — Four-layer assurance chain

File: `figure-02-assurance-chain.png`

Final prompt: Create a wide scholarly infographic with exactly four equal claim gateways connected left to right: `Observation Validity`, `Commitment + Provenance Integrity`, `Ledger + Governance Consistency`, and `Mission-Use Suitability`, ending in a small unlabeled decision beacon. Put `Physical Corroboration`, `Privacy Controls`, `Endpoint Integrity`, and `Context + Consequence` in one separate full-width band titled `Complementary Evidence and Controls`. The band supports the complete chain collectively: do not align or connect any lower tile with a specific upper claim. Use large horizontal labels, restrained 2.5D depth, consistent icons, and a warm-white journal background; add no other text, logos, watermarks, equations, cryptocurrency symbols, or military imagery.

## Figure 3 — Object–Assurance–Lifecycle framework

File: `figure-03-oal-framework.png`

Final prompt: Create a geometrically explicit three-dimensional OAL lattice with a four-column by four-row front face and six distinct planes receding into depth. `TRUST OBJECTS` must run horizontally across the front face with `Entity`, `Platform / Device`, `Link / Path`, and `Data Product`. `ASSURANCE LAYERS` must run vertically with `Observation Validity`, `Commitment + Provenance Integrity`, `Ledger + Governance Consistency`, and `Mission-Use Suitability`. `MISSION LIFECYCLE` must run diagonally away into perspective with `Admit`, `Sense`, `Relay`, `Fuse + Share`, `Decide + Act`, and `Audit + Recover`. The lifecycle axis must be oblique in the page projection and must never be parallel to, or presented as another horizontal row beneath, the trust-object axis. Surround the complete lattice with a dashed envelope labeled `Cross-Cutting Assurance + Governance`. Use large print-readable labels, restrained translucent depth, and no cell text, extra labels, logos, watermarks, equations, military imagery, or cryptocurrency symbols.

## Figure 4 — Dependencies and illustrative exposures

File: `figure-04-dependency-threat.png`

The current image shows five object stations and five separate exposure arrows. Causal hypotheses and evidence status occupy separate panels; `Unknown` is an epistemic label. The secondary operational dependency is routed above the objects. The exact initial prompt and final image-generation routing edit are recorded in [the September prompt set](../../../manuscript/figures/image-generation-prompts-20260907.md#figure-4--initial-generation).

## Figure 5 — CTG reasoning loop

File: `figure-05-ctg-reasoning-loop.png`

Prompt: Create a clockwise circular loop of exactly eight stations: `Evidence Capture`, `Reliability Appraisal`, `Object-State Inference`, `Dependency Propagation`, `Uncertainty Expression`, `Policy Action`, `Accountable Audit`, and `Operational Feedback`. Put a distinct central hub containing `Context`, `Time`, and `Mission`. Keep all outer labels horizontal and make the center visually separate from the loop.

## Figure 6 — Blockchain assurance boundary

File: `figure-06-blockchain-boundary.png`

The current image distinguishes ledger-supported records from complementary controls. A ledger is a candidate when joint control of state transitions and no agreed custodian occur together. Witnessed signed logs and replicated databases are shown as alternatives to compare under matched conditions. See [the exact final prompt](../../../manuscript/figures/image-generation-prompts-20260907.md#figure-6--initial-generation).

## Figure 7 — Claim-specific evidence profile

File: `figure-07-evidence-maturity.png`

The current image uses six equally sized illustrated panels for L0–L5. Rigor and uncertainty, environmental fit, and scope and duration are assessed separately. The categories are explicitly complementary rather than cumulative. See [the exact final prompt](../../../manuscript/figures/image-generation-prompts-20260907.md#figure-7--initial-generation).

## Integration notes

- The PNG files are the raster masters; the PDF files contain the same pixels without post-generation image editing.
- Copies of the current Figure 4, 6, and 7 PNGs and their PDF-only TeX wrappers are included in the submission sources so those figure PDFs can be rebuilt from the extracted package.
- Preserve semantic grouping and arrow direction if a figure is regenerated later.
- Retain the manuscript captions as the authoritative descriptions.
