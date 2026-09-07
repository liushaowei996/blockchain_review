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

# Reconciled against the retained source artifacts on 7 September 2026.
# Presence is acquisition evidence, not evidence of completed analytical coding.
PREVIOUSLY_RETAINED = {
    "aaqib2023iot", "adam2024state", "ali2019applications", "androulaki2018hyperledger",
    "baciu2025secure", "bae2023survey", "dang2022deep", "figueiredo2022arcadian",
    "hafeez2023blockchain", "han2022identity", "hang2019design", "hardjono2021towards",
    "honarpajooh2021iot", "hu2020survey", "jahanbakht2021internet", "kale2023provenance",
    "kamvar2003eigentrust", "khan2020iot", "lashkari2021comprehensive", "liu2022trusted",
    "liu2023survey", "mekdad2023survey", "mui2003computational", "neto2023ciciot2023",
    "nomikos2023survey", "rado2024recent", "rahman2020secure", "varga2022seadronessee",
    "wang2019survey", "wibisono2023survey", "xue2021distributed",
}
OFFICIAL_RETAINED = {
    "birkholz2023remote", "fagan2020iot", "hyperledger2026fabric", "ietf2020suit",
    "rose2020zero", "threegpp22119", "threegpp22125", "w3c2013provdm", "w3c2013provo",
}
OFFICIAL_SOURCES = OFFICIAL_RETAINED | {"yaga2018blockchain"}

# One-based pages of the lawfully retained PDF edition; see Supplementary Note S3.
CLAIM_LOCATORS = {
    "hayat2016survey": "PDF p.1 abstract; p.8 Section V; p.14 Section VI; pp.20-27 Section VII and Table III",
    "hadi2023comprehensive": "PDF pp.8-10 Sections 3.1-3.3; pp.17-19 Section 5; p.22 Section 6.10",
    "li2023survey": "PDF p.7 Section 3.4.3; pp.7-8 Section 4 and Figure 4",
    "arifeen2020hidden": "PDF p.3 HMM construction and numerical illustration",
    "jiang2020dynamic": "PDF p.3 acoustic-loss limitation; p.6 Section V; p.8 Section VI training assumptions",
    "zhu2024design": "PDF pp.8-9 Section IV trust-management modules",
    "tan2022blockchain": "PDF p.3 system assumptions; p.9 performance setup and Fabric 1.4.0",
    "karmakar2024blockchain": "PDF p.14 Sections VII-E/VII-F; p.17 conclusion",
    "ott2023universal": "PDF pp.8-9 Section 6.1.1 and Table 1; configurations and unmeasured ARM PSA latency",
    "zhang2020analysis": "PDF pp.2-3 Section 2; pp.3-4 Section 3 and Table 1; p.5 Section 4",
    "alsaedi2020ton": "PDF p.6 Section IV cyber-range collection",
    "ferrag2022edge": "PDF p.2 seven-layer description; pp.7-9 Section III architecture",
    "semanjski2020use": "PDF pp.3-7 Section 2 training and real-world validation datasets",
    "shah2018airsim": "PDF pp.11-13 Section 4 (printed pp.631-633), component comparison with real flights",
    "manhaes2016uuv": "PDF pp.3-5 Section III; p.6 Section IV; pp.6-7 Section V; p.7 Section VI validation limits",
    "martin2017aqua": "PDF pp.5-8 Section 5 simulator evaluation",
}


FULLTEXT_ACQUIRED = {
    "ahmed2019trust", "alladi2019blockchain", "alladi2020applications", "alsaedi2020ton",
    "arifeen2020hidden", "bellini2020blockchain", "ferrag2022edge", "hadi2023comprehensive",
    "hawashin2024blockchain", "hayat2016survey", "jiang2019securing", "jiang2020dynamic",
    "jsang2016subjective", "junior2021survey", "karmakar2024blockchain", "li2023survey",
    "manhaes2016uuv", "martin2017aqua", "mehta2020blockchain", "ott2023universal",
    "pan2023data", "reyna2018blockchain", "semanjski2020use", "shafique2021detecting",
    "shah2018airsim", "syed2022zero", "tan2022blockchain", "uddin2021survey",
    "veith2023road", "wang2025survey", "wei2022reliable", "zhang2020analysis",
    "zhu2024design",
}


FULLTEXT_OVERRIDES = {
    "hayat2016survey": {
        "evidence": "application taxonomy plus quantified mission, data, network, and QoS requirements",
        "evaluation_maturity": "review-level synthesis with reported quantitative requirements",
        "assumptions": "civil UAV applications; communication requirements vary by mission and network role",
        "limitations": "air-domain communications review; does not validate cross-domain assurance",
    },
    "hadi2023comprehensive": {
        "evidence": "review taxonomy of software, hardware, and communication vulnerabilities, attacks, and defenses",
        "evaluation_maturity": "peer-reviewed review-level synthesis",
        "assumptions": "primarily civilian/commercial UAV systems and published countermeasures",
        "limitations": "blockchain and other emerging defenses are not evidence of real-time deployment in highly mobile UAVs",
    },
    "li2023survey": {
        "evidence": "review of UAV, USV, UUV, and heterogeneous maritime search plus an illustrative USV--UAV platform",
        "evaluation_maturity": "review-level synthesis with limited platform integration",
        "assumptions": "maritime search missions and platform capabilities reported in the surveyed literature",
        "limitations": "heterogeneous cooperative application remains early-stage and does not include mission-trust validation",
    },
    "arifeen2020hidden": {
        "evidence": "HMM construction using packet-loss/error observations plus MATLAB numerical illustration and analytical cipher cost",
        "evaluation_maturity": "analytical and numerical illustration (evidence categories L1 and L2)",
        "assumptions": "packet loss/error discriminate malicious from trustworthy state; illustration uses random probabilities and ten observations",
        "limitations": "no calibrated attack/environment separation or representative underwater deployment",
    },
    "jiang2020dynamic": {
        "evidence": "C4.5 classification of data-, link-, and node-based trust evidence with simulated attack and energy comparisons",
        "evaluation_maturity": "software simulation (evidence category L2)",
        "assumptions": "base station performs classification; initial training assumes attack-free deployment and initially unpolluted trust evidence",
        "limitations": "actual underwater applicability not tested; acoustic loss can make normal nodes appear untrustworthy",
    },
    "zhu2024design": {
        "source_type": "peer-reviewed review",
        "evidence": "UWSN trust-management taxonomy, process decomposition, method comparison, and design guidelines",
        "evaluation_maturity": "review-level synthesis",
        "assumptions": "published UWSN trust models are comparable through common evidence/evaluation/propagation stages",
        "limitations": "does not itself validate an integrated mission-trust implementation",
    },
    "tan2022blockchain": {
        "evidence": "Fabric 1.4 smart-contract prototype plus formal/security analysis and simulated cryptographic cost comparisons",
        "evaluation_maturity": "prototype and simulation (evidence categories L2 and L3 for authentication service only)",
        "assumptions": "cloud-hosted peers, sufficient peer availability, and base-station coverage across the mission area",
        "limitations": "explicitly unsuitable where UAVs cannot reach blockchain services; no observation or cross-domain mission validation",
    },
    "karmakar2024blockchain": {
        "evidence": "PUF mutual authentication, EVM smart-contract implementation, and simulated cost/throughput/delay comparisons",
        "evaluation_maturity": "prototype and simulation (evidence categories L2 and L3 for authentication service only)",
        "assumptions": "cloud-hosted peers, ground-station controller, modeled mobility, and K-means cluster formation",
        "limitations": "cross-domain authentication is future work; no underwater, governance, or mission-outcome evaluation",
    },
    "ott2023universal": {
        "evidence": "implemented hardware-agnostic attestation for TPM, AMD SEV-SNP, and ARM PSA with latency, size, and security evaluation",
        "evaluation_maturity": "multi-platform prototype (evidence category L3)",
        "assumptions": "trusted hardware roots, signed reference manifests, TLS 1.3, and valid appraisal metadata",
        "limitations": "cloud/edge testbed; timings depend on same-host SNP VMs versus firmware TPM; ARM PSA handshake latency unmeasured; no sensor calibration or physical-truth guarantee",
    },
    "zhang2020analysis": {
        "source_type": "peer-reviewed review/analysis",
        "evidence": "comparative analysis of probabilistic- and absolute-finality consensus families",
        "evaluation_maturity": "analytical comparison",
        "assumptions": "consensus protocols compared under their stated fault and membership models",
        "limitations": "not an unmanned-system or partitioned-mission benchmark",
    },
    "alsaedi2020ton": {
        "evidence": "labeled IoT/IIoT telemetry, operating-system logs, and network traffic from the UNSW Canberra cyber range",
        "evaluation_maturity": "public dataset with baseline machine-learning evaluation",
        "assumptions": "cyber-range devices and attacks represent target anomaly classes",
        "limitations": "no maritime physics, vehicle dependencies, ledger, or mission outcomes",
    },
    "ferrag2022edge": {
        "source_type": "peer-reviewed dataset/benchmark",
        "evidence": "purpose-built seven-layer IoT/IIoT testbed dataset with centralized and federated learning baselines",
        "evaluation_maturity": "public dataset/testbed with baseline evaluation",
        "assumptions": "testbed protocols, devices, and attack labels transfer to the target deployment",
        "limitations": "no cross-media maritime mission, vehicle dynamics, or governance behavior",
    },
    "semanjski2020use": {
        "evidence": "supervised models trained on synthetically manipulated signals and validated on two distinct real-world GNSS spoofing/meaconing datasets",
        "evaluation_maturity": "recorded real-world signal evaluation (evidence category L2)",
        "assumptions": "selected features and labeled signal-manipulation events transfer to the target receiver/context",
        "limitations": "single signal family and experimental context; no endpoint, ledger, or mission-lifecycle integration",
    },
    "shah2018airsim": {
        "evidence": "high-frequency physics and visual simulation with hardware-in-the-loop support and selected real-flight comparisons",
        "evaluation_maturity": "simulation/tool with component validation",
        "assumptions": "vehicle, environment, and sensor models adequately represent the intended air scenario",
        "limitations": "does not natively model underwater acoustic links or consortium governance",
    },
    "manhaes2016uuv": {
        "evidence": "Gazebo/ROS package for hydrodynamics, thrusters, sensors, disturbances, intervention, and multi-robot scenarios",
        "evaluation_maturity": "open simulation/tool platform",
        "assumptions": "configured hydrodynamic and sensor models represent the target vehicle/environment",
        "limitations": "simulated dynamics and sensors require field validation; no trust or ledger semantics",
    },
    "martin2017aqua": {
        "source_type": "peer-reviewed tool/platform paper",
        "evidence": "ns-3 underwater-network simulator architecture with protocol support and reported experimental comparison",
        "evaluation_maturity": "network simulation/tool evaluation",
        "assumptions": "channel, protocol, topology, and traffic models represent the target underwater network",
        "limitations": "network abstraction does not establish observation truth or integrated mission assurance",
    },
}


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
    standard = source_id in OFFICIAL_SOURCES
    review = has(title, "survey", "review", "taxonomy", "state-of-the-art", "state of the art", "comprehensive") or source_id == "pan2023data"
    dataset = has(title, "dataset", "benchmark", "ciciot", "ton_iot", "edge-iiot")
    simulator = has(title, "simulator", "airsim", "ns-3", "simulation")

    if standard:
        source_type = "official standard, technical report, or architecture/documentation"
    elif entry["entry_type"] == "book":
        source_type = "scholarly book"
    elif entry["entry_type"] in {"misc", "techreport"}:
        source_type = "report/preprint/reference; publication status requires source-specific check"
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
        maturity = "normative or architectural reference; no empirical maturity assigned"
        assumptions = "scope and conformance conditions stated by issuing organization"
        limitations = "not evidence of performance in UAV-USV-UUV missions"
        coding_status = "official reference inspected; analytical mapping is authors' synthesis"
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

    result = {
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
        "classification_basis": "bibliographic/title routing; not a full-text coverage judgment",
        "full_text_status": "retained full-text artifact not recorded; inspect source before detailed claims",
        "claim_locator": CLAIM_LOCATORS.get(source_id, "not assigned; consult Supplementary Note S3 for targeted checks"),
    }
    if source_id in PREVIOUSLY_RETAINED | FULLTEXT_ACQUIRED | OFFICIAL_RETAINED:
        result["full_text_status"] = "lawful full-text artifact retained; inventory reconciled 7 September 2026"
    if source_id in PREVIOUSLY_RETAINED:
        result["coding_status"] = "lawful full-text artifact retained; claim-level coding pending"
    if source_id in FULLTEXT_ACQUIRED:
        result["coding_status"] = "lawful full text acquired and screened; fine-grained analytical coding pending"
    if source_id in FULLTEXT_OVERRIDES:
        result.update(FULLTEXT_OVERRIDES[source_id])
        result["coding_status"] = "lawful full text inspected; claim-level coding completed for review scope"
        result["classification_basis"] = "full-text overrides for evidence, assumptions, maturity, limitations; remaining categories are routing"
    if standard:
        result["classification_basis"] = "official source identity; OAL categories are authors' analytical mapping"
    if source_id == "gilbert2002brewer":
        result.update({
            "source_type": "peer-reviewed foundational analysis",
            "evidence": "formal definitions in Section 2 and impossibility theorem in Section 3.1",
            "evaluation_maturity": "formal analysis under stated asynchronous-network assumptions",
            "assumptions": "atomic (linearizable) read/write object; every request at a non-failing node terminates; arbitrary message loss",
            "limitations": "not a mission-safety theorem or a bound on response time; does not compare ledger deployments",
            "coding_status": "primary text inspected online; foundational claim checked 7 September 2026",
            "full_text_status": "author paper inspected via university-hosted PDF; no retained local artifact recorded",
            "classification_basis": "primary text Sections 2 and 3.1; OAL transfer is authors' synthesis",
            "claim_locator": "Sections 2 and 3.1; university-hosted author PDF pp.2-4; https://www.cs.princeton.edu/courses/archive/spring21/cos418/papers/cap.pdf",
        })
    return result


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
    for entry, row in zip(entries, rows):
        title = entry["title"].lower()
        priority.append({
                "source_id": entry["source_id"],
                "title": entry["title"],
                "doi_or_url": entry["doi"] or entry["url"],
                "priority": "high" if any(term in title for term in ("survey", "review", "uav", "underwater", "maritime")) else "medium" if any(term in title for term in priority_terms) else "background",
                "status": row["full_text_status"],
                "coding_status": row["coding_status"],
            })
    with MANIFEST.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(priority[0]))
        writer.writeheader()
        writer.writerows(priority)
    print(f"Wrote {len(rows)} evidence rows and {len(priority)} acquisition records")


if __name__ == "__main__":
    main()
