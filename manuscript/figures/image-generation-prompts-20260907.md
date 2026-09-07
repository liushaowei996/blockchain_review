# Image-generated figure revision — 7 September 2026

Figures 4, 6, and 7 were regenerated using the built-in image generation tool. No CLI/API fallback or post-generation pixel editing was used. The selected PNGs are copied unchanged into `manuscript/figures/`; the standalone TeX files only wrap those pixels in publication PDFs.

## Selected assets and checks

| Figure | Raster master | Publication PDF | Scientific checks |
|---|---|---|---|
| 4 | `figure-04-dependency-threat.png` | `figure-04-dependency-threat.pdf` | Five object/exposure associations; no exposure-to-exposure arrows; causal hypotheses separated from unknown evidence; secondary dependency routed above the objects. |
| 6 | `figure-06-blockchain-boundary.png` | `figure-06-blockchain-boundary.pdf` | Two complementary responsibility groups; joint control and absence of an agreed custodian shown together; witnessed logs and replicated databases retained as comparators. |
| 7 | `figure-07-evidence-maturity.png` | `figure-07-evidence-maturity.pdf` | All six categories, L0–L5, shown in equally sized panels; rigor, environmental fit, scope and duration assessed separately; no cumulative staircase. |

The matching project masters are also saved under `output/imagegen/figure-concepts/`. Original target artwork belongs to the pre-style-revision version; Figures 2 and 5 provide retained style references. Historical TikZ drawing sources are not used to render the manuscript.

## Prompts submitted to the built-in tool

### Figure 4 — initial generation

Input 1: original `figure-04-dependency-threat.png` (edit target). Input 2: retained `figure-02-assurance-chain.png` (style reference).

```text
Use case: scientific-educational, edit and redesign an existing manuscript infographic.
Input image 1 is the edit target: original dependency/threat figure. Input image 2 is a style reference from the same manuscript.
Create one final publication-ready wide landscape image. Match the warm-white background, deep navy bold sans-serif typography, restrained teal/cyan/violet/gold palette, coral exposure accents, dimensional circular icon medallions, raised soft-edged nameplates, and very subtle shadows of these references. Preserve their premium scientific editorial illustration style. Render crisp high resolution with large readable labels and ample whitespace.
Redesign the CONTENT as follows; the scientific distinctions are essential.
TOP: exactly five equally sized object stations in one horizontal row with attractive simple 2.5D medallion icons. Labels left to right: "Entity"; "Platform / Device"; "Link / Path"; "Data Product"; "Consumer". Under Consumer add the small role label "(entity role)". Solid navy arrows between adjacent stations point ONLY left to right, with exact labels above the four arrows: "controls", "uses", "transmits", "consumed by". Add a separate thin navy connector from Platform / Device to Data Product beneath the main row, arrowhead at Data Product, labelled "observes / transforms"; route it without crossing text or obscuring Link / Path.
MIDDLE: five small coral-accented icon cards directly under the corresponding five stations, with exact labels "Credential misuse"; "Endpoint compromise"; "Delay / route manipulation"; "False or stale product"; "Unsafe relying decision". Each card has exactly ONE short dashed coral arrow pointing UP to its corresponding top station. These five arrows associate exposures with objects. There must be NO arrows, lines, chains, or implied propagation connecting the coral cards to each other. Visually separate the thin secondary dependency connector from the coral arrows using generous vertical spacing.
BOTTOM: two clearly separate rounded soft-shadow panels. Left panel is wider, heading "Causal hypotheses"; inside are two equally prominent illustrated icon groups labelled "Adversarial manipulation" and "Benign degradation", with one shared short note "Causes may coexist". Right panel heading "Evidence status"; a single uncertainty/document icon labelled "Unknown", with note "Insufficient evidence". Unknown must be INSIDE only the Evidence status panel and must NEVER appear as a third causal hypothesis.
At the foot, one restrained line of large legible text: "Dependencies identify exposure; causation requires evidence."
Do not add a figure number, page title, other words, logo, watermark, cryptocurrency imagery, weapons, dense paragraphs, upward progress ladders, or decorative wiring. Ensure all specified words are spelled accurately and all labels are horizontally readable. Preserve style, change the described content and layout.
```

### Figure 4 — final routing correction

Input: the preceding generated Figure 4. This edit produced the selected master.

```text
Edit this scientific infographic with one targeted routing correction. Preserve all words, spelling, icons, typography, colors, panels, illustration style, and horizontal object positions. Preserve the five equal top stations and all lower content.
MOVE the entire thin curved navy dependency connector labelled "observes / transforms" FROM its current place below the top nameplates TO a NEW clear white margin ABOVE the top five circular icons. Expand the canvas upward slightly to create generous room. In that new upper margin, this thin navy connector must start at the TOP of the Platform / Device medallion (second station), travel horizontally above the row, and end with a downward-pointing arrowhead at the TOP of the Data Product medallion (fourth station). Place the label "observes / transforms" centered ABOVE this upper connector. It must not touch or cross any icon or any other label, and it must have exactly one arrowhead, at Data Product.
Completely erase the OLD curved connector and its label from the space between the nameplates and coral exposure cards.
In that now empty space, extend the dashed coral arrow above "Delay / route manipulation" upward to just below the "Link / Path" nameplate, to match the other four dashed coral arrows. All FIVE coral arrows must be parallel vertical upward arrows of matching length, each clearly pointing to its own top object, with no intervening text or other line. Do not link the coral cards to one another.
This precise change must leave the existing main left-to-right arrow chain, causal hypotheses panel, evidence status panel, and footer intact. Maintain the wide landscape composition and print readability. Add no other text or diagram elements.
```

### Figure 6 — initial generation

Input 1: original `figure-06-blockchain-boundary.png` (edit target). Input 2: retained `figure-02-assurance-chain.png` (style reference).

```text
Use case: scientific-educational, edit and redesign an existing manuscript infographic.
Input image 1 is the edit target: original blockchain-boundary infographic. Input image 2 is a supporting style reference from the same manuscript.
Produce one final wide landscape scholarly infographic in exactly this visual family: warm-white background, navy bold sans-serif labels, ocean teal and muted amber/violet, polished yet restrained 2.5D illustrative icons, softly raised circular hubs and small rounded plates, delicate shadows, clear geometry and generous whitespace. High resolution, all text large and print-readable.
Retain the recognizable two cooperating hubs in the top approximately two thirds, but implement these exact contents.
LEFT teal group: hub label "Ledger-supported records". Four surrounding icon-and-label satellites with exact labels "Membership + authority", "Provenance commitments", "Policy + model versions", "Audit + reconciliation". Below this group, a short note "Under declared trust assumptions".
RIGHT amber/violet group: hub label "Complementary controls". Four surrounding icon-and-label satellites with exact labels "Physical validation", "Endpoint protection", "Local safety + deadlines", "Privacy + governance". Below this group, a short note "For physical and mission-use claims".
A small, clearly separate connector between the two groups reads "Mission assurance". The two groups are complementary, not sequential. Leave space around the center and do not overlap labels, lines or icons. Use clear grouping, soft graphical detail, and the reference's balance.
Completely REMOVE the original bottom governance decision tree. REPLACE it with two clean full-width softly shaded horizontal bands:
Band 1, short heading "Ledger candidate when". Show two equally important condition chips side by side joined by a conspicuous PLUS sign: "Joint control of state transitions" + "No agreed custodian". Both must be visibly required together, not an either/or fork. Do not imply these conditions automatically establish superiority.
Band 2, short heading "Compare alternatives". Show two equal illustrative choices: "Witnessed signed logs" and "Replicated databases". At the bottom of this band place the short shared note "Match faults, availability, workload, and resources".
No arrows from independent parties directly to a ledger; no one-authority versus many-authorities tree; no winner badge; no blockchain superiority claim. Do not add a figure number, other text, page title, logo, watermark, cryptocurrency imagery, weapons, or decorative circuitry. Accurate spelling and large horizontal text. Preserve visual style, replace the scientific selection logic as described.
```

### Figure 7 — initial generation

Input 1: original `figure-07-evidence-maturity.png` (edit target). Input 2: retained `figure-05-ctg-reasoning-loop.png` (style reference).

```text
Use case: scientific-educational, edit and substantially redesign an existing manuscript infographic.
Input image 1 is the edit target: old evidence staircase. Input image 2 is a style reference from the same manuscript. Keep the warm-white background, navy sans-serif typography, blue/teal/gold/violet scientific editorial palette, attractive small 2.5D illustrative vignettes, gentle soft shadows, and polished restrained depth. REPLACE the staircase completely with SIX equally prominent rounded panels in a balanced flat 2-by-3 grid. Every panel has the same dimensions, same visual weight, same internal icon/vignette scale, same baseline within its row. No ascending terraces, arrows, connecting paths, growing heights, progress bars, cumulative tiers or increasing-quality implication.
This image is a landscape journal figure with a clear heading "Evidence profile for one scoped claim". Under the heading one brief line "Record each applicable category".
Exactly six equal panels, left to right in reading order:
Top left: category title "L0  Conceptual argument", small elegant lightbulb-and-architecture vignette; short descriptor "Use cases + rationale".
Top middle: title "L1  Analytical evidence", small elegant mathematical-model/checking vignette WITHOUT arbitrary readable equations; descriptor "Properties + assumptions".
Top right: title "L2  Simulation or data", small computer showing a stylized simulation map with data points; descriptor "Models + data origin".
Bottom left: title "L3  Prototype or testbed", small lab components and interface-testing vignette; descriptor "Configuration + workload".
Bottom middle: title "L4  Field trial", small maritime sensor/ship/shore vignette with a drone, no weapons; descriptor "Operating conditions".
Bottom right: title "L5  Sustained operation", small shore-control building and shared network/calendar vignette; descriptor "Duration + failures + recovery".
Use consistent understated colored category tabs and spacious title layout, allowing titles to wrap into two lines. Do not visually privilege the final category.
Below the grid, a single slim neutral panel headed "Assess separately", containing three equally weighted label groups separated by modest vertical separators: "Rigor + uncertainty" | "Environmental fit" | "Scope + duration".
At the very bottom, a clean navy sentence: "Categories are complementary, not cumulative."
All text must be spelled correctly and easily readable in journal print. Use only the specified words; no figure number, logo, watermark, ladder, ascending arrangement, direction arrows, progress rhetoric, cryptocurrency or weapons. The three added meanings L5, independent rigor, and noncumulative categories are mandatory. Preserve reference illustration style, redesign the layout and labels.
```
