# OAL extraction and reproducibility

The analytical sample contains 23 purposively selected original mechanism studies and 49 claim records. It is a disclosed subset of a narrative review, not a census of all research cited by the original manuscript. `original-citation-disposition.csv` records the role of all 141 original references, including 14 mechanism candidates outside completed full-text coding. Their exclusion limits numerical coverage claims. Full-text PDFs are retained privately and are not distributed.

`oal-study-mapping.csv` is the manually prepared analytical input. Each row contains a study identifier, stable bibliography key, domain, scoped mechanism claim, one object, one assurance layer, the lifecycle stages supported by that claim, the reported evidence profile, and a passage locator. The profile describes the method and setting supporting the named mechanism. It does not validate every surrounding architectural claim or imply integrated maritime assurance.

Objects: E entity/principal; P executing platform/device; L link/path; D versioned data product. Layers: O observation validity; C commitment/provenance integrity; G shared ledger/governance consistency; M mission-use suitability. Stages: A admission; S sensing; T transmission; F processing/fusion/sharing; D decision/action; R audit/revocation/recovery. D has a different meaning on the object and lifecycle axes.

L0 = concept/architecture; L1 = mathematical, formal or security analysis; L2 = simulation or recorded-data evaluation; L3 = implemented prototype/testbed; L4 = operating trial with specified physical conditions; L5 = sustained multi-party operation with duration and governance history. These are complementary forms, not quality ranks. Multiple forms may be assigned. No blanket L4 is assigned merely because hardware or a recorded field dataset was used.

The heatmap expands only the lifecycle list within each claim row, then counts distinct study IDs per exact object/layer/stage cell. It never crosses unrelated object, layer and stage labels. It has 96 possible cells and 20 nonempty cells in this sample. Counts overlap and cannot be summed to obtain a study count. A zero means no coded claim, without deciding whether that cell is applicable to every mission or absent from the field.

Coding is a single extraction pass checked against source passages and aggregation rules; no independent duplicate coding or inter-rater agreement is claimed. Some cited full texts are author manuscripts, with locations given by their PDF pagination. The ARCADIAN-IoT stable key retains `2022` although its chapter is cited by the 2023 print/copyright year. The digital-twin paper uses the available author-manuscript version. Interpretation of ambiguous deployment descriptions is deliberately narrow and documented in the scope column.

Reproduce the numerical outputs with Python 3.10 or later and `cryptography`:

```
python supplementary/replay_case.py
python supplementary/build_figures.py --data-only
```

Run from the manuscript directory or use absolute script paths. The replay regenerates the CSV/JSON results and verifies signatures, tamper rejection, Merkle branches, arrival-order invariance and duplicate handling, signer subsets, the local-authority example, and serialization accounting. The public deterministic keys are test fixtures. Consensus and Fabric are not executed; latency sensitivity inputs are assumptions. ML-DSA is included only through standardized signature-length arithmetic.

The editable artwork is supplied in `figures/Figures-revised.vsdx`, with one page per figure. The original Visio layout, colors and diagram geometry are retained where they convey the same content. Figure 3 pairs the OAL framework schematic with a heatmap whose cell values follow `oal-cell-counts.csv`; `mapping-summary.json` exposes its aggregate counts. All 96 displayed cells have been checked against the claim CSV. If the coding changes, update the corresponding heatmap cells in the drawing before re-exporting it.

To export the seven figure pages, run `python supplementary/build_figures.py` on Windows with Microsoft Visio installed, or run `supplementary/export_visio_figures.ps1` directly. The export script opens the drawing read-only and produces PDFs with selectable vector text and diagram geometry. Figure 2 retains the original raster lighthouse illustration; Figures 1 and 3–7 contain no raster images. Figure 7 uses native Visio shapes and connectors in place of the former photo-realistic illustrations, with no photographic, stock or generated-image assets in that figure. The supplied PDFs can be used to compile the manuscript on any OS without Visio.

`protocol-specification.txt` defines the proposed Fabric application, placement, state, endorsement, constrained verification and matched log baseline. `consensus-requirements.csv` records family-specific assumptions and scenario decisions. The schema and byte counts are reproducible; full Fabric envelopes and operational performance require implementation measurement.
