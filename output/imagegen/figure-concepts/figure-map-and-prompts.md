# Manuscript Figure Assets

These seven raster figures were generated with the built-in image generation tool and selected for the manuscript after checking terminology, arrow direction, grouping, and consistency with the captions and surrounding text. Figures 2 and 4 were regenerated from blank prompts to correct semantic ambiguity; the other five generated originals were retained. The final PNG files are wrapped without content edits in PDF containers under `manuscript/figures/` and inserted into the LaTeX manuscript. The earlier TikZ files remain in the repository as historical working sources but are not used by the manuscript.

| Figure | Disposition |
|---|---|
| 1 | Existing generated original retained |
| 2 | Regenerated from a blank prompt |
| 3 | Existing generated original retained |
| 4 | Regenerated from a blank prompt |
| 5 | Existing generated original retained |
| 6 | Existing generated original retained |
| 7 | Existing generated original retained |

## Shared visual direction

- Use case: scientific-educational / scholarly journal infographic
- Canvas: wide landscape on a warm-white background
- Style: premium editorial scientific infographic with crisp geometry, restrained 2.5D depth, consistent icons, generous whitespace, and print-readable labels
- Palette: navy, ocean teal, cyan, muted orange, violet, slate, and limited coral accents
- Constraints: no logos, watermarks, equations, decorative circuitry, military weapons, cryptocurrency branding, or dense paragraph text

## Figure 1 — Cross-domain reference architecture

File: `figure-01-reference-architecture.png`

Prompt: Show three operating domains with UAVs and satellite/HAPS in the sky, a USV or buoy gateway at the surface, and UUV/AUV platforms underwater. Place shore services, policy and permissioned-ledger peers, an encrypted evidence store, and an auditor to the right. Connect them with visually distinct radio, optical, acoustic, and intermittent governance links. Enclose the system in a subtle assurance-and-governance plane. Use the labels `UAV`, `Satellite / HAPS`, `USV Gateway`, `UUV / AUV`, `Shore Services`, `Policy + Ledger`, `Evidence Store`, `Auditor`, and `Assurance + Governance`.

## Figure 2 — Four-layer assurance chain

File: `figure-02-assurance-chain.png`

Final prompt: Create a wide scholarly infographic with exactly four equal claim gateways connected left to right: `Observation Validity`, `Commitment + Provenance Integrity`, `Ledger + Governance Consistency`, and `Mission-Use Suitability`, ending in a small unlabeled decision beacon. Put `Physical Corroboration`, `Privacy Controls`, `Endpoint Integrity`, and `Context + Consequence` in one separate full-width band titled `Complementary Evidence and Controls`. The band supports the complete chain collectively: do not align or connect any lower tile with a specific upper claim. Use large horizontal labels, restrained 2.5D depth, consistent icons, and a warm-white journal background; add no other text, logos, watermarks, equations, cryptocurrency symbols, or military imagery.

## Figure 3 — Object–Assurance–Lifecycle framework

File: `figure-03-oal-framework.png`

Prompt: Build an isometric translucent analytical lattice with three visible dimensions. Across the top, show trust objects `Entity`, `Platform / Device`, `Link / Path`, and `Data Product`. Vertically, show assurance layers `Observation`, `Provenance`, `Ledger + Governance`, and `Mission Use`. Along the depth/timeline, show `Admit`, `Sense`, `Relay`, `Fuse + Share`, `Decide + Act`, and `Audit + Recover`. Enclose the lattice in a cross-cutting assurance and governance envelope without filling every cell with text.

## Figure 4 — Dependency and threat propagation

File: `figure-04-dependency-threat.png`

Final prompt: Create a wide scholarly infographic with three separated tiers. The top dependency chain is `Entity` → `Platform / Device` → `Link / Path` → `Data Product` → `Mission Consumer`, with arrow labels `controls`, `uses`, `transmits`, and `consumed by`, plus a thin secondary arrow from `Platform / Device` to `Data Product` labeled `observes / transforms`. The middle tier is the continuous muted-coral dashed chain `Credential Theft` → `Endpoint Capture` → `Jamming / Route Attack` → `Poisoning / Stale Replay` → `Unsafe Allocation`. The bottom is one full-width panel titled `Parallel Causal Interpretations` with equal lenses `Malicious`, `Benign-Degraded`, and `Unknown`. Associate the entire middle chain with the panel through one bracket; do not connect an individual stage to an individual interpretation. Use large horizontal labels, restrained 2.5D depth, consistent icons, and a warm-white journal background; add no other text, logos, watermarks, equations, military weapons, circuitry, or cryptocurrency imagery.

## Figure 5 — CTG reasoning loop

File: `figure-05-ctg-reasoning-loop.png`

Prompt: Create a clockwise circular loop of exactly eight stations: `Evidence Capture`, `Reliability Appraisal`, `Object-State Inference`, `Dependency Propagation`, `Uncertainty Expression`, `Policy Action`, `Accountable Audit`, and `Operational Feedback`. Put a distinct central hub containing `Context`, `Time`, and `Mission`. Keep all outer labels horizontal and make the center visually separate from the loop.

## Figure 6 — Blockchain assurance boundary

File: `figure-06-blockchain-boundary.png`

Prompt: Separate two cooperating responsibility groups. The blue-teal `Permissioned Ledger` hub contains only `Membership + Authority`, `Provenance Commitments`, `Version Coordination`, and `Audit + Reconciliation`. The amber-violet `Complementary Assurance` hub contains only `Physical Validation`, `Endpoint Protection`, `Real-Time Safety`, and `Privacy + Governance`. Connect the hubs through `Integrated Mission Assurance`. In a separate bottom strip, split `Governance Structure` into exactly two unambiguous branches: `Independent Parties` → `Permissioned Ledger`; `Single Accountable Authority` → `Authenticated Database`.

## Figure 7 — Evidence-maturity ladder

File: `figure-07-evidence-maturity.png`

Prompt: Create six ascending terraces from lower left to upper right: `Concept`, `Analysis`, `Simulation`, `Prototype`, `Field Trial`, and `Deployment`. Increase implementation detail, environmental realism, organizational participation, and operational duration at each level. Add a rising ribbon labeled `Increasing Ecological Evidence` and a continuous foundation labeled `Preserve Clarity + Traceability`.

## Integration notes

- The PNG files are the raster masters; the PDF files contain the same pixels without post-generation image editing.
- Preserve semantic grouping and arrow direction if a figure is regenerated later.
- Retain the manuscript captions as the authoritative descriptions.
