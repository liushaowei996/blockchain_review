# Supplementary Note S3: discovery and evidence traceability

Version: 7 September 2026. This note accompanies the narrative review and Tables S1 and S2.

## Discovery and selection

The retained discovery helper uses OpenAlex topical search with `from_publication_date:2016-01-01`, relevance sorting, and at most 25 records per query. It deduplicates by DOI or OpenAlex identifier. The retained candidate export and Crossref metadata cache were produced on 6 August 2026. Search-result limits and relevance ranking constrain recall; the dated export does not establish an exhaustive publication-date census. Earlier foundational references and official documents were selected separately.

The six discovery themes were UAV blockchain/security; maritime and underwater communication/security; heterogeneous vehicle cooperation; trust/reputation; provenance/attestation/zero trust; and ledger architecture/governance. The exact query strings were:

```text
blockchain UAV survey
blockchain unmanned aerial vehicle security
blockchain UAV swarm
UAV swarm security survey
unmanned aerial vehicle trust management reputation
UAV data provenance blockchain
maritime blockchain survey
maritime IoT blockchain security
Internet of Underwater Things security survey
underwater acoustic network security survey
underwater wireless sensor network trust management
UUV security trust
UAV USV UUV cooperative systems
air surface underwater heterogeneous unmanned systems
cross-domain unmanned systems UAV USV UUV
blockchain trust management IoT survey
IoT trust reputation survey taxonomy
dynamic trust management IoT Bayesian subjective logic
zero trust architecture IoT review
remote attestation IoT survey RATS
data provenance IoT survey W3C PROV
blockchain data provenance IoT
blockchain off-chain storage IoT survey
permissioned blockchain IoT resource constrained
blockchain network partition finality
blockchain governance permissioned consortium
multi-sensor fusion trust reliability adversarial
data trustworthiness sensor fusion provenance
UAV GNSS spoofing survey
underwater acoustic jamming security
UAV USV cooperative search review
UAV UUV cross-domain communication
```

Retention was purposive, according to relevance to an assurance claim, operational condition, implementation assumption, or evaluation resource. The project does not contain a completed multi-database systematic-screening protocol, a full exclusion log, or duplicate human coding records. The source inventory therefore supports bounded conceptual comparisons rather than estimates of literature prevalence or pooled performance. The September revision checked selected claims and added the primary CAP analysis; it did not rerun the complete discovery search.

## Meaning of the inventory fields

Table S1 includes all 141 bibliography entries. `classification_basis` distinguishes title/bibliographic routing from source-specific analytical overrides. Domain, object, and lifecycle labels produced from titles are discovery aids; they are not verified scores of a paper's full coverage. In particular, an absent label is not evidence that a mechanism is absent from the paper.

Table S2 now covers the same 141 entries rather than the previous 119-entry keyword-filtered acquisition queue. Its priority is a routing convenience, not a source-quality rating. Full-text availability and coding are separate columns in both tables. The September reconciliation records 73 retained cited-source artifacts: 64 scholarly sources and 9 official references. The 33-source August acquisition batch is included in those 73. File availability does not establish that all claims or editions have been analyzed.

Sixteen sources retain detailed coding for the selected method/resource comparisons. The other inventory records comprise 17 previously screened sources without detailed coding, 31 additional retained scholarly artifacts without completed coding, 10 official references, 66 bibliographic records awaiting detailed coding, and the newly checked foundational CAP analysis. These categories sum to 141; availability is a separate overlapping attribute. A targeted check elsewhere in this note does not automatically promote a record to completed full-paper coding.

The official-reference category includes technical reports, architectural RFCs, recommendations, specifications, and implementation documentation. It does not imply that all documents have standards-track status, provide empirical validation, or use interchangeable conformance semantics. The retained 3GPP artifacts are TS 22.119 v19.0.0 and TS 22.125 v19.2.0; those versions do not establish the latest release at submission time.

Mekdad's UAV review and Wang's consensus survey are retained as author/preprint versions of the cited work. The 2013 subjective-logic draft is not substituted for the retained 2016 book edition. Reproducing a claim check requires matching the cited work and inspected version; PDF page numbers below refer to the locally retained edition and may differ from printed pagination.

## Locators for the 16 detailed comparison records

These locators were checked against the retained full texts during the September revision. They identify passages supporting the review's selected claims; they are not exhaustive extraction sheets or independent replication of source experiments. The `claim_locator` column in Table S1 carries the same pointers.

| Source ID | One-based PDF pages and section | Claim supported and scope |
|---|---|---|
| hayat2016survey | p.1 abstract; p.8 §V; p.14 §VI; pp.20–27 §VII and Table III | Application-specific communication and QoS requirements; air-domain review. |
| hadi2023comprehensive | pp.8–10 §§3.1–3.3; pp.17–19 §5; p.22 §6.10 | UAV vulnerability taxonomy and deployment constraints for emerging defenses. |
| li2023survey | p.7 §3.4.3; pp.7–8 §4 and Figure 4 | Early-stage heterogeneous maritime cooperation and an illustrative one-USV/two-UAV platform. |
| arifeen2020hidden | p.3 HMM construction and illustration | Random-probability numerical illustration using ten observations; no calibrated field diagnosis. |
| jiang2020dynamic | p.3; p.6 §V; p.8 §VI | Acoustic-loss ambiguity, MATLAB evaluation, and attack-free initial training assumptions. |
| zhu2024design | pp.8–9 §IV | Trust evidence, evaluation, propagation, and update modules in a design-guideline review. |
| tan2022blockchain | p.3; p.9 performance setup | Cloud peers, base-station coverage, and Fabric 1.4.0 authentication prototype. |
| karmakar2024blockchain | p.14 §§VII-E/VII-F; p.17 conclusion | EVM/Truffle prototype and simulation; cross-domain authentication proposed as future work. |
| ott2023universal | pp.8–9 §6.1.1 and Table 1 | Platform-dependent mutual-TLS measurements; same-host SNP VMs versus firmware TPM; ARM PSA handshake latency unmeasured. |
| zhang2020analysis | pp.2–3 §2; pp.3–4 §3 and Table 1; p.5 §4 | Consensus-family comparison under stated assumptions; table percentages are not universal guarantees. |
| alsaedi2020ton | p.6 §IV | Cyber-range telemetry, host, and network collection. |
| ferrag2022edge | p.2; pp.7–9 §III | Seven-layer IoT/IIoT testbed and collection architecture. |
| semanjski2020use | pp.3–7 §2 | Synthetic training and two real-world spoofing/meaconing validation datasets. |
| shah2018airsim | pp.11–13 §4 (printed pp.631–633) | Selected simulated/physical quadrotor and sensor comparisons. |
| manhaes2016uuv | pp.3–5 §III; p.6 §IV; pp.6–7 §V; p.7 §VI | Hydrodynamics, sensors, ROS modules and use cases; dynamic validation remains ongoing; waves/turbulence are outside the implemented current model. |
| martin2017aqua | pp.5–8 §5 | Simulator memory, scalability, and performance evaluation. |

Source claims about test conditions remain separate from the review's proposed OAL mappings and cross-domain transfer requirements. The L0–L5 labels denote evidence categories, not an ordinal quality score; a prototype record may also carry simulation evidence without inheriting a formal proof.

## Additional targeted checks

- `zhang2022blockchain`: final issue metadata was corrected to 2023, 24(2), 2322–2331 using the [authors' Durham institutional record](https://durham-repository.worktribe.com/output/1206869/a-blockchain-based-authentication-scheme-and-secure-architecture-for-iot-enabled-maritime-transportation-systems). The citation key retains its early-access year for stability. The publisher page was access-limited and Crossref still returned early-access metadata at the check date.

- `kamvar2003eigentrust`: PDF pp.2–3, §§4.2–4.5 support relative spectral reputation and pretrusted peers, rather than calibrated mission probability.
- `varga2022seadronessee`: PDF pp.3–5, §§3–4 and Table 3 support footage, metadata, and benchmark tasks.
- `neto2023ciciot2023`: PDF p.3 §3 and pp.13–16 §§4–5 support the dataset and baseline-evaluation description.
- `gilbert2002brewer`: [primary author paper](https://www.cs.princeton.edu/courses/archive/spring21/cos418/papers/cap.pdf), §§2 and 3.1, defines atomic consistency, availability, and the asynchronous impossibility result. Its availability definition is not a hard deadline guarantee.
- [RFC 9334](https://www.rfc-editor.org/rfc/rfc9334.html), §§4, 7, and 10, supports separation of evidence, appraisal, relying decisions, and freshness conditions.
- [PROV-DM](https://www.w3.org/TR/prov-dm/) supports entity/activity/agent semantics. An OAL principal usually maps to a PROV agent; the two uses of “entity” are not synonyms.
- [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final), [NISTIR 8202](https://nvlpubs.nist.gov/nistpubs/ir/2018/nist.ir.8202.pdf), [RFC 9019](https://www.rfc-editor.org/rfc/rfc9019.html), and [Fabric ordering documentation](https://hyperledger-fabric.readthedocs.io/en/latest/orderer/ordering_service.html) were consulted for architectural boundaries, update roles, and ordering/commit semantics.

Publisher full texts and temporary extraction files are retained outside the distributed source package. The accompanying bibliography supplies the publication identifiers for all source IDs above.
