"""Create a conservative evidence inventory for the narrative review.

The inventory separates bibliographic verification from full-text analytical
coding.  Title-level rules are used only for routing; method, assumptions,
and limitations remain explicitly pending unless the source is an official
standard or an openly inspectable reference artifact.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


BIB = Path("manuscript/references.bib")
OUT = Path("manuscript/supplement/evidence-matrix.csv")
MANIFEST = Path("manuscript/supplement/full-text-acquisition-manifest.csv")


def parse_entries(text: str) -> list[dict[str, str]]:
    starts = list(re.finditer(r"(?m)^@(\w+)\{([^,]+),", text))
    entries: list[dict[str, str]] = []
    for index, start in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        block = text[start.start():end]
        row = {"entry_type": start.group(1), "source_id": start.group(2).strip()}
        for field in ("title", "author", "year", "journal", "booktitle", "doi", "url", "howpublished"):
            match = re.search(rf"(?ms)^\s*{field}\s*=\s*\{{(.*?)\}}\s*,?\s*$", block)
            row[field] = re.sub(r"[{}]", "", match.group(1)).strip() if match else ""
        entries.append(row)
    return entries


def has(text: str, *terms: str) -> bool:
    return any(term in text for term in terms)


def classify(entry: dict[str, str]) -> dict[str, str]:
    title = entry["title"].lower()
    source_id = entry["source_id"]
    standard = source_id.startswith(("w3c", "threegpp", "hyperledger", "ietf")) or has(title, "nist", "architecture for internet of things")
    review = has(title, "survey", "review", "taxonomy", "state-of-the-art", "state of the art", "comprehensive")
    dataset = has(title, "dataset", "benchmark", "ciciot", "ton_iot", "edge-iiot")
    simulator = has(title, "simulator", "airsim", "ns-3", "simulation")

    if standard:
        source_type = "official standard/specification"
    elif review:
        source_type = "peer-reviewed review"
    elif dataset:
        source_type = "peer-reviewed dataset/benchmark"
    elif simulator:
        source_type = "peer-reviewed tool/platform paper"
    else:
        source_type = "peer-reviewed primary study"

    air = has(title, "uav", "drone", "aerial", "flying", "uas ", "airsim")
    underwater = has(title, "underwater", "subsea", "acoustic", "uuv", "auv", "ocean")
    maritime = has(title, "maritime", "marine", "ship", "surface vehicle")
    general_iot = has(title, "internet of things", "iot", "iiot", "blockchain") and not (air or underwater or maritime)
    domains = []
    if air: domains.append("air")
    if maritime: domains.append("surface/maritime")
    if underwater: domains.append("underwater")
    if general_iot: domains.append("general IoT/distributed systems")
    domain = "; ".join(domains) or "cross-cutting security/trust"

    platforms = []
    if air: platforms.append("UAV/UAS")
    if maritime: platforms.append("USV/maritime infrastructure")
    if underwater: platforms.append("UUV/IoUT")
    if not platforms: platforms.append("generic IoT/edge/ledger node")

    mission = "cross-domain mission assurance"
    if has(title, "search", "rescue", "detecting humans"): mission = "maritime search and rescue/observation"
    elif has(title, "navigation", "localization", "positioning"): mission = "navigation/localization"
    elif has(title, "data collection", "routing", "communication", "network"): mission = "communications/data collection"
    elif has(title, "supply chain", "shipping", "port"): mission = "maritime logistics"

    objects = []
    if has(title, "identity", "authentication", "authorization", "zero trust", "attestation"): objects += ["entity", "platform/device"]
    if has(title, "communication", "network", "routing", "jamming", "spoofing"): objects.append("link/path")
    if has(title, "data", "provenance", "information fusion", "dataset", "benchmark"): objects.append("data product")
    if has(title, "trust", "reputation") and not objects: objects = ["entity", "platform/device"]
    if has(title, "blockchain") and not objects: objects = ["data product", "entity"]
    trust_object = "; ".join(dict.fromkeys(objects)) or "contextual/background"

    layers = []
    if has(title, "sensor", "fusion", "detect", "spoofing", "navigation"): layers.append("observation validity")
    if has(title, "provenance", "integrity", "authentication", "attestation", "secure data"): layers.append("commitment/provenance integrity")
    if has(title, "blockchain", "consensus", "fabric", "distributed ledger"): layers.append("ledger/governance consistency")
    if has(title, "trust", "decision", "mission", "resilience"): layers.append("mission-use suitability")
    assurance_layer = "; ".join(dict.fromkeys(layers)) or "foundational/contextual"

    stages = []
    if has(title, "identity", "authentication", "authorization", "attestation", "zero trust"): stages.append("admission/authentication")
    if has(title, "sensor", "observation", "detect", "dataset"): stages.append("sensing/collection")
    if has(title, "communication", "network", "routing", "maritime"): stages.append("transmission/relay")
    if has(title, "fusion", "analytics", "sharing", "provenance"): stages.append("processing/fusion/sharing")
    if has(title, "decision", "mission", "trust"): stages.append("decision/action")
    if has(title, "blockchain", "audit", "revocation", "governance"): stages.append("audit/revocation/recovery")
    lifecycle_stage = "; ".join(dict.fromkeys(stages)) or "cross-lifecycle"

    threat_terms = []
    for needle, label in (
        ("spoof", "spoofing"), ("jamming", "jamming"), ("attack", "cyberattack"),
        ("security", "multiple security threats"), ("privacy", "privacy exposure"),
        ("byzantine", "Byzantine behavior"), ("intrusion", "intrusion"),
    ):
        if needle in title: threat_terms.append(label)
    threat = "; ".join(threat_terms) or "not title-coded"

    trust_method = "not applicable/title-insufficient"
    if has(title, "subjective logic"): trust_method = "subjective logic"
    elif has(title, "eigentrust"): trust_method = "spectral reputation"
    elif has(title, "beta reputation"): trust_method = "Bayesian/Beta reputation"
    elif has(title, "hidden markov"): trust_method = "hidden Markov model"
    elif has(title, "deep learning", "machine learning", "deep "): trust_method = "machine learning"
    elif has(title, "trust", "reputation"): trust_method = "trust/reputation method; full-text coding pending"

    blockchain_role = "not central"
    if has(title, "blockchain", "distributed ledger", "hyperledger", "fabric"):
        blockchain_role = "ledger-supported trust/audit/data sharing; exact design pending full-text coding"
    elif has(title, "provenance"):
        blockchain_role = "possible provenance anchor; source does not necessarily require a ledger"

    if standard:
        evidence = "normative or architectural specification"
        maturity = "operational standard/specification"
        assumptions = "scope and conformance conditions stated by issuing organization"
        limitations = "not evidence of performance in UAV-USV-UUV missions"
        coding_status = "official text inspected; analytical mapping is authors' synthesis"
    elif dataset or simulator:
        evidence = "artifact and reported baseline/tool evaluation"
        maturity = "benchmark/tool"
        assumptions = "deployment representativeness requires mission-specific validation"
        limitations = "does not by itself validate cross-domain mission trust or ledger behavior"
        coding_status = "bibliographic metadata verified; artifact/full text to be rechecked before submission"
    else:
        evidence = "reported analysis/evaluation; detail reserved pending full-text check"
        maturity = "pending full-text classification"
        assumptions = "pending full-text coding"
        limitations = "pending full-text coding; no detailed claim drawn from title alone"
        coding_status = "bibliographic metadata verified; full-text analytical coding pending"

    return {
        "source_id": source_id,
        "source_type": source_type,
        "domain": domain,
        "platform": "; ".join(platforms),
        "mission": mission,
        "trust_object": trust_object,
        "assurance_layer": assurance_layer,
        "lifecycle_stage": lifecycle_stage,
        "evidence": evidence,
        "threat": threat,
        "trust_method": trust_method,
        "blockchain_role": blockchain_role,
        "assumptions": assumptions,
        "evaluation_maturity": maturity,
        "limitations": limitations,
        "coding_status": coding_status,
        "title": entry["title"],
        "year": entry["year"],
        "doi_or_url": entry["doi"] or entry["url"],
    }


def main() -> None:
    entries = parse_entries(BIB.read_text(encoding="utf-8"))
    rows = [classify(entry) for entry in entries]
    fields = list(rows[0])
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)

    priority_terms = ("survey", "review", "uav", "underwater", "maritime", "trust", "provenance", "attestation", "zero trust", "blockchain")
    priority = []
    for entry in entries:
        title = entry["title"].lower()
        if any(term in title for term in priority_terms) and not entry["source_id"].startswith(("w3c", "threegpp", "hyperledger", "ietf")):
            priority.append({
                "source_id": entry["source_id"],
                "title": entry["title"],
                "doi_or_url": entry["doi"] or entry["url"],
                "priority": "high" if any(term in title for term in ("survey", "review", "uav", "underwater", "maritime")) else "medium",
                "status": "obtain and inspect lawful full text before final evidence coding",
            })
    with MANIFEST.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(priority[0]))
        writer.writeheader()
        writer.writerows(priority)
    print(f"Wrote {len(rows)} evidence rows and {len(priority)} acquisition records")


if __name__ == "__main__":
    main()
