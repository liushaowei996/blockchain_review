# Supplementary Note S3: Supporting evidence and source notes

This note summarizes the findings, assumptions, and source locations supporting the review's method and resource comparisons.

## Reference scope

The review draws on 141 references: 130 scholarly papers and book chapters, one book, and 10 standards, technical reports, or other official technical references. The English-language literature mainly covers 2016-2026, with earlier foundational contributions on reputation, distributed-system limits, provenance, and consensus. Its themes include unmanned-system cooperation and security, underwater communications, trust and reputation, provenance, attestation, zero trust, and permissioned-ledger governance.

Research studies provide models, protocols, implementations, datasets, and evaluation results. Reviews connect these contributions within their application domains. Standards, architectural recommendations, and implementation documentation provide technical definitions and design guidance, with conformance requirements determined by each document's status and scope.

## Method and resource comparisons

The following comparisons identify the evidence supporting each claim and the conditions under which it applies. Page numbers count from the first page of each document; printed pagination may differ.

| Source ID | Pages and sections | Evidence and scope |
|---|---|---|
| hayat2016survey | p.1; p.8 §V; p.14 §VI; pp.20–27 §VII and Table III | Application-specific communication and QoS requirements; air-domain review. |
| hadi2023comprehensive | pp.8–10 §§3.1–3.3; pp.17–19 §5; p.22 §6.10 | UAV vulnerability taxonomy and deployment constraints for emerging defenses. |
| li2023survey | p.7 §3.4.3; pp.7–8 §4 and Figure 4 | Early-stage heterogeneous maritime cooperation and an illustrative one-USV/two-UAV platform. |
| arifeen2020hidden | p.3 HMM construction and illustration | Random-probability numerical illustration using ten observations; field diagnosis requires calibration. |
| jiang2020dynamic | p.3; p.6 §V; p.8 §VI | Acoustic-loss ambiguity, MATLAB evaluation, and attack-free initial training assumptions. |
| zhu2024design | pp.8–9 §IV | Trust evidence, evaluation, propagation, and update modules in a design-guideline review. |
| tan2022blockchain | p.3; p.9 performance setup | Cloud peers, base-station coverage, and Fabric 1.4.0 authentication prototype. |
| karmakar2024blockchain | p.14 §§VII-E/VII-F; p.17 conclusion | EVM/Truffle prototype and simulation; cross-domain authentication proposed as future work. |
| ott2023universal | pp.8–9 §6.1.1 and Table 1 | Platform-dependent mutual-TLS measurements for same-host SNP VMs and firmware TPM; ARM PSA handshake latency requires separate measurement. |
| zhang2020analysis | pp.2–3 §2; pp.3–4 §3 and Table 1; p.5 §4 | Consensus-family comparison with table percentages interpreted under the stated assumptions. |
| alsaedi2020ton | p.6 §IV | Cyber-range telemetry, host, and network collection. |
| ferrag2022edge | p.2; pp.7–9 §III | Seven-layer IoT/IIoT testbed and collection architecture. |
| semanjski2020use | pp.3–7 §2 | Synthetic training and two real-world spoofing/meaconing validation datasets. |
| shah2018airsim | pp.11–13 §4 (printed pp.631–633) | Selected simulated/physical quadrotor and sensor comparisons. |
| manhaes2016uuv | pp.3–5 §III; p.6 §IV; pp.6–7 §V; p.7 §VI | Hydrodynamics, sensors, ROS modules and use cases; dynamic validation is ongoing; representing waves/turbulence requires extensions to the implemented current model. |
| martin2017aqua | pp.5–8 §5 | Simulator memory, scalability, and performance evaluation. |

The L0-L5 categories denote complementary forms of evidence, with quality and applicability assessed for each claim. A prototype may also supply simulation results; a formal guarantee requires its own proof and assumptions. The reported configurations delimit each result. Cross-domain transfer requires validation under the target mission's channel, resource, timing, and governance conditions.

## Additional findings and architectural boundaries

- `kamvar2003eigentrust`: EigenTrust defines relative spectral reputation and uses pretrusted peers (pp.2-3, Sections 4.2-4.5). Interpreting its score as a mission-success probability requires an explicit event model and calibration.
- `varga2022seadronessee`: SeaDronesSee provides maritime UAV footage, metadata, and visual detection and tracking benchmarks (pp.3-5, Sections 3-4 and Table 3).
- `neto2023ciciot2023`: CICIoT2023 provides IoT traffic and attack data with baseline intrusion-detection evaluations (p.3, Section 3; pp.13-16, Sections 4-5).
- `gilbert2002brewer`: The [CAP analysis](https://www.cs.princeton.edu/courses/archive/spring21/cos418/papers/cap.pdf), Sections 2 and 3.1, establishes the incompatibility of atomic consistency and availability under arbitrary partitions in its asynchronous model. Availability concerns eventual request completion; a hard deadline guarantee requires an additional timing condition.
- [RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html), Sections 4, 7, and 10, separates attestation evidence, appraisal, and relying-party decisions and specifies freshness considerations.
- [PROV-DM](https://www.w3.org/TR/prov-dm/) relates entities, activities, and agents. An OAL principal usually maps to a PROV agent, while a data product maps to a PROV entity.
- [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) describes policy-based access decisions using subject, device, and contextual evidence.
- [NISTIR 8202](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf) distinguishes recording sensor inputs from establishing whether they reflect physical events.
- [RFC 9019](https://www.rfc-editor.org/rfc/rfc9019.html) defines firmware-update roles, manifests, authorization, and device constraints.
- [Hyperledger Fabric ordering documentation](https://hyperledger-fabric.readthedocs.io/en/latest/orderer/ordering_service.html) distinguishes ordering from transaction validation and commitment. Application-state changes require successful validation after block inclusion.
