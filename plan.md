# MDPI *Blockchains* 混合研究论文实施计划

## 1. 目标与论文定位

- 按 **Research Article** 投稿，而非 Review：MDPI 明确规定 Review 不应呈现新的未发表数据；Article 可以同时包含系统映射综述、原创方法、原型和实验。[MDPI Article Types](https://www.mdpi.com/about/article_types)
- 暂定英文标题：**From Ledger Consensus to Mission Trust: A Systematic Mapping and Experimental Framework for Blockchain-Assisted Air-Surface-Underwater Unmanned Systems**。
- 聚焦 UAV-USV-UUV、卫星/岸基协同，以海洋观测、巡检和搜救为公开应用背景，不扩展到地面无人系统或武器任务。
- 核心论点是区分并连接三类保证：

  \[
  \text{Observation Trust}\rightarrow\text{Submission Trust}\rightarrow\text{Ledger Consensus}
  \]

  区块链负责多组织共享状态、审计和分区后对账，不被描述为传感器物理真值的证明工具。
- 目标规模为英文正文约 13,000-15,000 词，约 8-10 幅图、8-12 张表；区块链机制贯穿研究问题、架构、方法和实验，以符合 *Blockchains* 关于新型区块链架构、模型、安全、数据治理及关键基础设施的范围。[Blockchains Aims & Scope](https://www.mdpi.com/journal/blockchains/about)

## 2. 系统映射综述与论文结构

### 2.1 检索协议

- 在正式筛选前完成 OSF 时间戳登记并设置 embargo，审稿阶段使用匿名链接，接收后公开。
- 主语料限定为 2016 年至最终检索日的英文同行评议期刊和会议论文。
- 用户提供 Scopus、Web of Science、IEEE Xplore、ACM Digital Library 四库完整导出，以及合法取得的非开放全文。
- 更早的奠基论文和 NIST、IETF、W3C、3GPP、Hyperledger 等标准作为独立背景语料，不混入 PRISMA 统计。
- 设置两条检索轨道：
  - “无人系统 x blockchain/DLT/smart contract x trust/security/provenance/data sharing”；
  - “无人系统 x dynamic trust/reputation/zero trust/attestation/provenance x context/uncertainty”。
- 按 DOI、规范化题名、年份和第一作者去重；保留数据库来源、筛选阶段和逐篇排除理由，并进行前后向引文追踪。

### 2.2 研究问题

- **RQ1：** 现有研究覆盖了哪些物理域、无人平台、任务与数据生命周期阶段？
- **RQ2：** 实体、设备、链路和数据分别使用了哪些信任证据、更新机制与不确定性表达？
- **RQ3：** 攻击如何跨越对象传播，并最终影响数据融合、访问控制和任务决策？
- **RQ4：** 区块链在身份、证明、溯源、撤销、策略和审计中分别提供什么保证，又不能提供什么保证？
- **RQ5：** 现有研究采用了哪些数据集、仿真器、原型、指标和复现材料，其评价成熟度如何？
- **RQ6：** 哪些经证据支持的研究空白可以转化为参考架构、CTG-Trust 设计要求和实验假设？

### 2.3 文献编码

每篇文献至少编码以下字段：

- 标识信息：内部 study ID、DOI、题名、年份、期刊/会议、文献类型；
- 场景信息：物理域、平台、任务、单域或跨域；
- 信任信息：信任对象、生命周期、证据类型、更新机制、不确定性；
- 安全信息：攻击者、威胁、攻击路径、缓解机制；
- 区块链信息：区块链角色、许可模式、共识、链上数据、链下数据、智能合约；
- 评价信息：数据集、仿真器、节点规模、基线、指标、实验成熟度；
- 质量信息：方法透明度、威胁模型完整度、结果有效性、复现性、局限说明。

### 2.4 筛选与 AI 披露

- 采用“一名人工作者 + AI 辅助”流程：AI 只做预标注、候选排除理由和一致性检查，人工作者确认每条最终决定。
- 人工作者确认全部全文纳入和排除决定；15% 分层样本进行延迟重复判定并报告内部一致性。
- 保存筛选提示、模型信息、日期、人工覆盖记录和排除理由。
- AI 使用声明由作者在正式投稿时根据 MDPI 政策和投稿系统要求另行填写；当前匿名稿不预置工具或用途表述。[MDPI AI Policy](https://www.mdpi.com/ethics#_bookmark10)
- 所有“现有研究通常”“多数方法”“明显缺少”等结论必须由编码比例、证据表或明确引用支持，不沿用 `deep-research-report.md` 中的 `turn...` 占位引用。

### 2.5 论文结构

1. Introduction
2. Review Protocol and Study Design
3. Systematic Mapping Results
4. Guarantee Model and Object-Centric Threat Taxonomy
5. CTG-Trust and Partition-Aware Audit Protocol
6. Experimental Methods
7. Experimental Results
8. Discussion and Research Agenda
9. Threats to Validity
10. Conclusions

## 3. 原创贡献

### 3.1 三阶段保证模型

建立以下三个不能相互替代的保证阶段：

1. **Observation Trust：** 评价物理观测、传感器状态、时空合理性和跨源一致性；
2. **Submission Trust：** 评价提交实体、采集设备、数字签名、传输路径和来源链；
3. **Ledger Consensus：** 评价多组织对记录顺序、状态、撤销和审计事件的一致性。

为每个阶段明确：保证内容、成立假设、不保证内容、失败模式、可观测证据和责任主体。

### 3.2 四类信任对象

- **实体：** 操作者、组织、自治智能体及其身份、角色、授权和行为；
- **设备：** UAV、USV、UUV、传感器、边缘节点及其软硬件完整性和健康度；
- **链路：** 水声、无线、卫星和跨介质路径的质量、安全和环境一致性；
- **数据：** 原始观测、处理结果、来源图、版本、质量、新鲜性和任务适用性。

控制策略、模型、智能合约和软件服务作为可版本化的控制工件映射到设备状态或数据/策略工件，不随意增加第五种信任对象。

### 3.3 CTG-Trust

将现有 CTG-Trust 重构为可计算的上下文时序因子图：

- 实体、设备、链路和数据分别维护 `TRUSTED`、`BENIGN_DEGRADED`、`COMPROMISED`、`RECOVERING` 隐状态；
- 环境、任务风险、拓扑和网络分区作为显式上下文变量；
- 实体控制设备、设备生成数据、链路传输数据、来源活动加工数据均以因子表示；
- 每条证据携带唯一 lineage，禁止 Beta、时序和图传播重复使用同一证据；
- 证据可靠性和模型参数在训练/验证数据上估计，并通过参数采样传播不确定性；
- 输出状态后验、后验熵、不确定性区间、解释原因和任务期望效用；
- 期望效用明确区别于“对象可信概率”；
- 策略阈值、恢复滞回和“未知”状态均在验证集上校准，并在测试前冻结。

### 3.4 分区感知审计协议

- 边缘节点维护带序列号和签名的追加日志；
- 断连期间按批次计算 Merkle 根；
- 重连后向联盟链提交根、序列范围、事件数、模型版本、策略版本和时间信息；
- 支持成员资格、签名、序列连续性、重复批次、过期授权和包含证明验证；
- 链上仅存伪名、摘要、粗粒度状态和审计元数据，不保存原始遥测或精确信任分数；
- 原始证据、证明和传感数据保存在链下，并通过 inclusion proof 与链上根关联。

### 3.5 固定接口

#### `EvidenceEvent`

- `event_id`
- `subject_id`
- `object_type`
- `source_id`
- `evidence_type`
- `observed_at`
- `value`
- `reliability`
- `context`
- `parent_ids`
- `payload_hash`
- `signer`

#### `TrustEstimate`

- `posterior_by_state`
- `expected_utility`
- `uncertainty_interval`
- `entropy`
- `state`
- `top_reasons`
- `model_version`

#### `PolicyDecision`

- `action`
- `obligations`
- `policy_version`
- `expires_at`
- `reason_codes`

#### `AnchorBatch`

- `batch_id`
- `signer`
- `first_sequence`
- `last_sequence`
- `event_count`
- `merkle_root`
- `model_hash`
- `policy_hash`
- `generated_at`
- `partition_id`

#### `InclusionProof`

- `batch_id`
- `event_hash`
- `siblings`
- `path`

### 3.6 贡献追踪

建立“综述证据 -> 设计要求 -> CTG-Trust 机制 -> 实验场景 -> 结果指标”的追踪矩阵，确保原创框架由系统综述导出，而不是与综述部分割裂。

## 4. 实验计划

### 4.1 E1：UAV-NIDD 公开数据外部验证

- 使用公开 UAV-NIDD 数据校准设备和链路层证据；
- 按完整文件、采集会话或攻击场景划分训练、验证和测试，禁止随机行级切分；
- 若数据缺少稳定会话标识，则采用按文件分组或 leave-one-scenario-out 方式；
- 基础异常检测器保持简单、可解释，并在验证集上做概率校准；
- 所有信任基线接收相同的底层证据，避免输入不公平；
- 该实验仅验证 UAV 设备/链路证据，不宣称完整验证海空潜跨域模型。

主要指标：AUROC、AUPRC、F1、Brier Score、ECE、检测时延和误隔离率。

### 4.2 E2：跨域事件与网络仿真

主场景拓扑：

- UAV x 4；
- USV x 2；
- UUV x 4；
- 岸基节点 x 1；
- 卫星链路作为受限远程连接抽象。

本机完成事件生成、CTG-Trust 和任务仿真；阿里云使用 ns-3 与固定提交版本的 Aqua-Sim FG 生成水下声学链路轨迹，并记录版本、提交 SHA、配置和随机种子。

核心场景：

1. 正常环境变化与证据缺失；
2. 海况/噪声引起的良性链路退化；
3. USV 选择性转发和跨域观测偏置；
4. 合法设备生成带有效签名的假数据；
5. UUV 开关攻击与恢复期；
6. Sybil 身份和共谋推荐；
7. 网络分区、撤销延迟和重连；
8. 环境退化与恶意行为同时发生；
9. 模型参数失配和未见攻击强度；
10. 任务风险等级切换。

### 4.3 E3：任务闭环

- 构造多源海上异常/目标定位任务；
- UAV、USV、UUV 提供不同噪声、时延和覆盖范围的观测；
- 将对象后验用于多源融合权重、异常隔离和二次验证请求；
- 与均匀融合、仅质量加权、静态信誉和理想 Oracle 比较。

主要指标：定位 RMSE、错误决策率、任务完成时间、有效观测覆盖率、集群存活率和攻击期间累计任务效用损失。

### 4.4 E4：Fabric SmartBFT 审计原型

- 使用 Hyperledger Fabric 3.x SmartBFT；
- 采用 4 个排序节点，满足 `3f + 1` 且容忍 `f = 1`；
- 多组织配置至少包含两个应用组织和分离的排序成员身份；
- SmartBFT 用于匹配排序节点可能失陷的威胁模型。[Fabric BFT Ordering Service](https://hyperledger-fabric.readthedocs.io/en/latest/orderer/ordering_service.html)

比较三种记录模式：

1. 合成原始事件逐条上链，仅作为性能上界基线；
2. 每个事件摘要逐条上链；
3. Merkle 批量摘要上链。

固定实验参数：

- 批量大小：1、10、50；
- 输入速率：25、100、250 events/s；
- 网络条件：正常、100 ms 延迟加 1% 丢包、边缘断连 60 s；
- 故障条件：单个排序节点停止或严重延迟；
- 每个配置至少重复 5 次。

主要指标：吞吐、p50/p95/p99 确认时延、积压新鲜度、断连恢复时间、链增长、CPU、内存和单事件通信开销。

功能与安全测试：

- 篡改单条事件；
- 删除或重排事件；
- 重放和重复批次；
- 无效签名；
- 非连续序列号；
- 过期模型或策略版本；
- 错误 inclusion proof；
- 单个排序节点不可用；
- 超过容错上限时只声明丧失活性，不伪造安全结论。

### 4.5 基线与消融

固定基线：

- Static-Trust；
- Weighted-Sum；
- Beta-only；
- HMM-only；
- Direct-only / No-Graph；
- Blockchain-only；
- Oracle，仅作为理论上界。

固定消融：

- 移除环境上下文；
- 移除跨对象因子；
- 移除时序因子；
- 移除不确定性策略；
- 不使用恢复滞回；
- 不做证据 lineage 去重。

### 4.6 统计方案

- 主实验先用 10 个种子估计方差；
- 按配对中等效应、80% power、`alpha = 0.05` 计算正式重复数；
- 正式重复数最低 30、最高 100；
- 报告 bootstrap 95% CI、配对 Wilcoxon、Holm 多重比较校正和效应量；
- 所有参数、阈值和攻击配置在验证阶段冻结；
- 若 CTG-Trust 未优于基线，保留并解释负面结果，不在测试集上反复调参；
- 所有图表必须由固定脚本从原始结果重新生成。

### 4.7 云端条件

阿里云默认配置：

- Ubuntu 22.04 LTS；
- 16 vCPU；
- 64 GB RAM；
- 至少 200 GB SSD；
- 无需 GPU；
- 允许出站网络、Docker 和编译工具链。

凭据、访问密钥和实例私有信息不得进入源码、日志、论文或匿名归档。

### 4.8 非核心线下/HIL 实验规程

另行交付详细规程，供用户后续补充：

- 水声通信机或声学信道实测；
- PX4 SITL/HIL 和飞控遥测；
- TPM/TEE 远程证明；
- USV/UUV 中继和跨介质网关；
- 实际功耗与证明时延。

GNSS/RF 欺骗只允许线缆注入、软件仿真或屏蔽环境，不安排开放环境辐射实验。这些数据不作为本次投稿的必需依赖，取得后可按统一数据模式补充分析。

统一线下数据字段至少包含：

```text
scenario_id, run_id, timestamp, object_id, object_type, domain,
environment_parameters, channel_parameters, ground_truth_state,
attack_type, attack_start, attack_end, raw_evidence,
evidence_reliability, network_measurements, trust_output,
policy_action, mission_outcome, cpu, memory, energy,
communication_cost, calibration_record, time_sync_error
```

## 5. LaTeX 与投稿格式

- 使用执行时最新的官方 MDPI ACS 模板；当前入口为 [Blockchains ACS LaTeX ZIP](https://res.mdpi.com/data/MDPI_template_ACS.zip?v=20260728)。
- 固定并记录模板下载日期、版本和文件校验和。
- 文档类采用：

  ```latex
  \documentclass[blockchains,article,submit,moreauthors]{Definitions/mdpi}
  ```

- 仅生成双匿名稿：作者、单位、基金、身份化仓库链接和 PDF 元数据不进入交付稿。
- 用户选择不在本项目中生成真实作者版本；真实作者信息和 CRediT 最终内容由用户后续加入。
- 摘要控制在约 200 词以内，使用单段 Background-Methods-Results-Conclusions 逻辑但不加小标题。
- 设置 3-10 个关键词。
- 使用 MDPI ACS 数字编号制和 BibTeX；正文、图题和表题中的文献按首次出现顺序编号。
- 保留并填写匿名化的 Author Contributions 占位说明、Funding、Data Availability、Acknowledgments 和 Conflicts of Interest；GenAI 使用声明由作者在正式投稿时填写。[Blockchains Instructions](https://www.mdpi.com/journal/blockchains/instructions)
- 概念图、架构图和流程图采用可复现的矢量源；实验图由代码生成，同时导出投稿所需高分辨率版本。
- 不使用 AI 生成的装饰性科研图片，不复制未经许可的既有图表。

## 6. 项目产物

### 6.1 论文

- 可编译 LaTeX 源；
- `references.bib`；
- 匿名 PDF；
- 全部图、表及可编辑源；
- MDPI 投稿 ZIP；
- 匿名 cover letter 模板和投稿检查表。

### 6.2 系统综述材料

- OSF 登记协议；
- 四库检索式和导出说明；
- 原始导出文件清单与校验和；
- 去重后的主语料；
- 标题/摘要和全文筛选表；
- 排除理由；
- 编码手册与质量评价；
- PRISMA 流程图和 checklist；
- 文献到结论的证据追踪表。

### 6.3 软件与实验材料

- CTG-Trust 实现；
- 事件生成器；
- UAV-NIDD 处理脚本；
- ns-3/Aqua-Sim FG 配置；
- Fabric SmartBFT 网络配置与 chaincode；
- 分析、统计和绘图脚本；
- 固定随机种子和实验配置；
- 环境锁文件、容器定义和运行说明；
- 原始结果、汇总结果、数据字典和校验和；
- 线下/HIL 实验规程。

### 6.4 开放与匿名策略

- 投稿阶段生成不含作者身份的只读审稿归档；
- OSF 登记在接收前保持 embargo，并提供匿名只读链接；
- 接收后再公开 GitHub；
- 经用户授权后在 Zenodo 冻结正式版本并生成 DOI；
- 未获授权前不执行任何外部公开上传。

## 7. 实施顺序与门槛

### 阶段 A：项目与协议

1. 初始化隔离项目结构和版本控制；
2. 下载并固定官方 MDPI 模板；
3. 编写检索式、纳排标准、编码手册和统计分析计划；
4. 生成 OSF embargo 登记材料；
5. 等待用户完成登记并提供四库导出。

### 阶段 B：系统映射

1. 合并、规范化和去重；
2. AI 辅助预筛；
3. 用户/作者完成人工确认；
4. 全文编码和质量评价；
5. 生成 PRISMA、证据图谱和研究空白；
6. 在提交前 14 天内执行最终补检并重新生成全部计数。

若发现已有工作同时覆盖四对象动态因子图、三阶段保证边界和分区感知 Merkle 审计，不再宣称整体方法首创，而是暂停原创性表述并重新定位贡献。

### 阶段 C：方法与本地实验

1. 固化 CTG-Trust 数学定义和接口；
2. 开发测试驱动的事件生成与推断代码；
3. 完成 UAV-NIDD 回放；
4. 完成本机跨域仿真、基线、消融和任务融合；
5. 完成 Fabric SmartBFT 原型和小规模基准。

现有 Docker 用户资产不得改动；全部容器、网络、卷和 Compose project 使用独立命名空间。

### 阶段 D：云端实验

1. 获得用户阿里云权限后创建隔离实例；
2. 构建固定版本的 ns-3/Aqua-Sim FG；
3. 执行规模化 Monte Carlo、网络条件和敏感性实验；
4. 将原始输出、日志、资源计量和校验和同步回项目；
5. 关闭或释放不再使用的云资源，并向用户报告。

### 阶段 E：写作与交付

1. 先写 Methods 和 Results，再完成 Introduction、Discussion 和 Abstract；
2. 将每个结论绑定到文献证据或实验输出；
3. 完成全部图表、补充材料、数据声明和 AI 披露；
4. 构建 LaTeX 并执行自动检查；
5. 将 PDF 全页渲染为 PNG 进行视觉检查并迭代修复；
6. 生成匿名投稿 ZIP、审稿归档和交付说明。

## 8. 验收标准

### 8.1 科学与文献

- 所有引用均具有可核验的作者、题名、出处和 DOI/稳定 URL；
- 不存在 `turn...`、`TODO citation` 或虚构文献；
- 技术结论优先回到原始论文、数据集论文和官方标准；
- 所有综述性比例均能从编码数据重新计算；
- PRISMA 数量、筛选表和正文一致；
- 不把区块链一致性表述为传感器数据真值；
- 不把期望效用表述为后验概率；
- 不把 SmartBFT 的理论容错保证冒充实验发现。

### 8.2 软件与实验

- 全新环境可以按文档复现实验和全部图表；
- 单元测试、集成测试和数据模式测试通过；
- 数据划分无会话泄漏或行级泄漏；
- 随机种子、参数、版本和结果校验和齐备；
- 测试集参数未被用于调优；
- 正面与负面结果均如实保留；
- 统计检验、置信区间和效应量与原始结果一致。

### 8.3 LaTeX 与 PDF

- `latexmk` 可无错误完成构建；
- 无未定义引用、重复标签或缺失图片；
- 无明显 overfull、文字裁切、图表重叠或不可读字符；
- 图表标签不小于 8 pt，轴、单位、图例和说明完整；
- 页眉、页脚、页码、章节和参考文献视觉正确；
- PDF 和源码不包含作者姓名、单位、邮箱、用户名或身份化仓库地址；
- 投稿 ZIP 包含全部编译依赖且不包含缓存、密钥、原始数据库受限全文或 Git 历史。

## 9. 已确认的假设与用户输入

- 稿件类型：混合 Research Article；
- 应用范围：海空潜协同；
- 文献语种：仅英文；
- 数据库：Scopus、Web of Science、IEEE Xplore、ACM DL 四库完整包；
- 筛选：一名人工作者 + AI 辅助；
- 协议登记：OSF embargo 至接收；
- 实验强度：本地原型 + 阿里云高保真网络仿真；
- 区块链：Hyperledger Fabric 3.x SmartBFT 主实验；
- 公开数据：UAV-NIDD 主验证；
- HIL：不作为本次投稿的强制条件，但提供完整线下规程；
- 产物发布：匿名审稿包，接收后再公开 GitHub/Zenodo；
- 作者信息：本项目只生成匿名稿，不生成真实作者版本；
- 用户后续需提供：四库导出、必要全文、人工筛选确认、阿里云权限；
- 所有实验结论以实际数据为准，不预设 CTG-Trust 必须优于全部基线。
