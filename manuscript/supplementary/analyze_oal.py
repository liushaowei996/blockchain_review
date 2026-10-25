"""Validate OAL inputs and reproduce stratified/sensitivity summaries (stdlib only)."""
from pathlib import Path
import collections
import csv
import json

DATA = Path(__file__).resolve().parent
LEVELS = [f"L{i}" for i in range(6)]


def read_csv(name):
    with (DATA / name).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def summarize(claims):
    cells, profiles = collections.defaultdict(set), collections.defaultdict(set)
    for row in claims:
        for stage in row["lifecycle_stages"].split(";"):
            cells[row["object"], row["assurance"], stage].add(row["study_id"])
        for level in row["evidence_levels"].split(";"):
            profiles[level].add(row["study_id"])
    return {
        "studies": len({r["study_id"] for r in claims}),
        "claim_records": len(claims),
        "nonempty_cells": len(cells),
        "top_cell_count": max(map(len, cells.values()), default=0),
        "top_cells": ";".join("/".join(k) for k, v in sorted(cells.items())
                              if len(v) == max(map(len, cells.values()), default=0)),
        **{level: len(profiles[level]) for level in LEVELS},
    }


def write_csv(name, rows):
    with (DATA / name).open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=rows[0])
        writer.writeheader()
        writer.writerows(rows)


def main():
    claims = read_csv("oal-study-mapping.csv")
    register = read_csv("oal-study-register.csv")
    refs = read_csv("current-reference-roles.csv")
    studies = {r["study_id"]: r for r in register}
    assert len(studies) == len(register), "Duplicate study identifier"
    assert len({r["reference_key"] for r in register}) == len(register)
    assert {r["study_id"] for r in claims} == set(studies)
    assert {r["reference_key"] for r in refs if r["numerically_coded"] == "true"} == {r["reference_key"] for r in register}
    signatures = set()
    for row in claims:
        assert row["reference_key"] == studies[row["study_id"]]["reference_key"]
        assert row["object"] in "EPLD" and row["assurance"] in "OCGM"
        assert set(row["lifecycle_stages"].split(";")) <= set("ASTFDR")
        assert set(row["evidence_levels"].split(";")) <= set(LEVELS)
        assert all(row[k].strip() for k in ["claim", "evidence_locator", "evidence_scope"])
        signature = tuple(row.items())
        assert signature not in signatures, "Duplicate claim record"
        signatures.add(signature)

    profiles = {sid: set().union(*(set(r["evidence_levels"].split(";")) for r in claims if r["study_id"] == sid)) for sid in studies}
    conceptual = {sid for sid, p in profiles.items() if p == {"L0"}}
    direct = {sid for sid, r in studies.items() if r["stratum"] == "direct_domain"}
    consensus = {"S35", "S36", "S37", "S38"}
    proxy = {sid for sid, r in studies.items() if r["domain_proxy"] == "true"}
    variants = [
        ("all", "All coded studies", claims),
        ("direct_domain", "UAV, maritime AIS and intended underwater applications", [r for r in claims if r["study_id"] in direct]),
        ("transferable", "Transferable mechanisms including four generic consensus comparators", [r for r in claims if r["study_id"] not in direct]),
        ("without_four_consensus", "Exclude S35-S38; retain existing Fabric and application mechanisms", [r for r in claims if r["study_id"] not in consensus]),
        ("without_concept_only", "Exclude studies whose entire profile is L0", [r for r in claims if r["study_id"] not in conceptual]),
        ("direct_without_proxy", "Exclude terrestrial-data proxy S34 from direct-domain stratum", [r for r in claims if r["study_id"] in direct - proxy]),
        ("identity_as_entity", "Reassign P/C/A rows of S01-S03 to E/C/A; deduplicate at cell level", [dict(r, object="E") if r["study_id"] in {"S01", "S02", "S03"} and (r["object"], r["assurance"], r["lifecycle_stages"]) == ("P", "C", "A") else r for r in claims]),
        ("physical_trial_as_testbed", "Treat bounded physical UAV-node experiment S31 as L3 only", [dict(r, evidence_levels=";".join(level for level in r["evidence_levels"].split(";") if level != "L4")) if r["study_id"] == "S31" else r for r in claims]),
    ]
    output = [dict(variant=name, definition=definition, **summarize(rows)) for name, definition, rows in variants]
    write_csv("oal-sensitivity.csv", output)
    leave_one_out = [dict(omitted_study=sid, **summarize([r for r in claims if r["study_id"] != sid])) for sid in sorted(studies)]
    write_csv("oal-leave-one-out.csv", leave_one_out)

    # Co-occurrence is a candidate interface, never proof of a validated handover.
    layer_sets = {sid: {r["assurance"] for r in claims if r["study_id"] == sid} for sid in studies}
    bridges = []
    for left, right in [("O", "C"), ("O", "M"), ("C", "G"), ("C", "M"), ("G", "M")]:
        ids = sorted(sid for sid, layers in layer_sets.items() if {left, right} <= layers)
        bridges.append(dict(layer_pair=left + "/" + right, study_count=len(ids), study_ids=";".join(ids), interpretation="Study-level co-occurrence only; no inferred validation of a cross-layer transition"))
    write_csv("oal-layer-cooccurrence.csv", bridges)
    summary = dict(
        references=len(refs), coded_studies=len(studies), contextual_references=len(refs)-len(studies),
        direct_domain_studies=len(direct), transferable_studies=len(studies)-len(direct),
        concept_only_studies=sorted(conceptual),
        leave_one_out_nonempty_cells=[min(r["nonempty_cells"] for r in leave_one_out), max(r["nonempty_cells"] for r in leave_one_out)],
        leave_one_out_top_cells=sorted({r["top_cells"] for r in leave_one_out}),
        L4_studies=sorted(sid for sid, levels in profiles.items() if "L4" in levels),
        interpretation="Descriptive inclusion/coding sensitivity; not a confidence interval, meta-analysis, or validation of OAL effectiveness.",
    )
    (DATA / "oal-analysis-summary.json").write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
