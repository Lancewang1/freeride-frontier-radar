# FREERIDE Frontier Radar

Research snapshot: 2026-10-23

三项待验证的技术投资假设；并非全市场排名或投资推荐

## 1. 在线审计路由

以审计策略、真实结果反馈和版本化证据为产品核心，嵌入已有业务流程。最值得先验证，是因为可使用历史决策日志进行低成本影子实验，且人工复核成本较易计量。竞争壁垒更可能来自业务标签闭环与集成，而非单独的路由公式。

每轮接收一个决策及置信度，低于阈值时审计，高于阈值时仍以最低概率 γ 抽查。用审计发现的错误作逆概率加权更新阈值。保留随机探索能减少只看到被选中样本的偏差。

研究判断 TRL 3–4；尚无本研究核验的生产部署

- 论文将 Err(T) 定义为预期漏审错误数 / 预期总错误数，而不是所有决策中的错误率，也不是每次运行均满足的风险上限。 [Reliable AI-Assisted Decisions via Selective Auditing](https://arxiv.org/abs/2610.31662) PDF pp.2–4, §2–3, Theorem 1

- 加法阈值方法的界为 |Err(T)−α| ≤ (1/η+1/γ)/nT。只有当预期错误数 nT 随 T 线性增长时，文中给出 O(1/T) 收敛；错误稀少时保证可能较弱。 [Reliable AI-Assisted Decisions via Selective Auditing](https://arxiv.org/abs/2610.31662) PDF pp.3–4

- 作者明确假设审计者总是正确、各次审计成本相同。文本标注实验以更强模型充当审计者，并非已验证的专家真值。 [Reliable AI-Assisted Decisions via Selective Auditing](https://arxiv.org/abs/2610.31662) PDF pp.11,13, §6.2–7

- 独立反证论文构造了离线证据相同但部署结果相反的世界；在线监控仍要求稳定分组结果、无偏缺失等条件。 [Post-Audit Mirage: Identifiability Limits of Offline Agent Verification](https://arxiv.org/abs/2610.31130) PDF pp.2–3, Theorem 1 / monitoring

### unknowns

- 真实审计者错误、延迟标签、不同严重度损失如何改变保证？

- 面对稀有重大错误，足够的样本和随机抽查成本是否抵消节约？

- 可校准置信度是否必须使用昂贵的第二模型？

- 流程平台是否已经用规则与人工抽样满足采购需求？

### alternatives

- 固定比例随机抽查：解释简单，是必须击败的低成本基线。

- 静态置信阈值 + 人工复核：集成成本低，但漂移与选择偏差需要处理。

- 全量专家审计：质量参照；必须用独立裁决衡量专家自身误差。

- 现有质检/流程平台内置路由：可能吸收功能；当前未核验具体厂商采购价格。

### plan

- 第1–7天：找3个复核团队，取得去标识历史日志；冻结错误定义、严重度、专家分歧裁决和样本切分。

- 第8–14天：按时间留出测试集；比较随机抽查、静态阈值和在线路由，禁止用未来标签调参。

- 第15–21天：只做影子路由；分组报告审计率、漏审率、置信区间、延迟和专家一致性。

- 第22–30天：核算全成本，争取有预算负责人签署的付费试点范围。

### gates

- 建议门槛：保持预先约定的漏审容忍度，人工审计量相对随机基线下降≥20%，且净节约为正。

- 罕见重大错误证据不足时继续人工兜底，不把零观察错误视为零风险。

- 若无独立标签、客户无法同意错误定义、或内置功能足够便宜，则停止独立产品立项。

未知：新论文不等于低拥挤；缺少融资、采购及竞品收入时间序列

上游按目标客户实际推理支出统计模型供应商 CR5；下游按该审计软件细分市场采购额统计客户 CR5。两者分母、地域、年度均缺失，因此均未知；不能用通用大模型份额替代。

单客月净收益 = 决策量 × (原复核率−新复核率) × 单次复核成本 − 额外推理费 − 标签质控费 − 摊销集成费。例：10万次 × 20个百分点 × 5元 − 2万元 = 8万元/月，全部为演示假设，未计事故损失，不是报价。

{'accounts': 500, 'price': 20, 'penetration': 10, 'growth': 20, 'unit': '企业', 'note': '500 家可服务企业 × 20 万元年费是假设的软件收入池，不是观测 TAM；10% 渗透对应假设 ARR。企业数、年费和增长必须用访谈与订单替换。'}

上游: 模型与置信分数 → 业务事件日志 → 专家标签
切入层: 随机抽查 + 预算控制 + 漂移监控 + 证据版本
下游: 企业质检 / 合规运营 / 标注团队（买方假设）

## 2. 跨网关撤销完成证明

在现有身份系统之上提供撤销验收与结果证据层，回答某个冻结网关集合、调用集合和时间窗内是否完成撤销。先卖验收测试和取证能力，再验证持续运行监控的预算；不要一开始替换整个 IAM。

区分 C0 issuer commit、C1 queued、C2 transport ack、C3 persisted、C4 gateway enforced、C5 effect prevented。完成需要所有已声明网关的执行回执和独立效果观察，窗口关闭后才给出有限范围的完成判断。冲突证据拒收，已观察到的违规不能被后到回执抹去。

研究判断 TRL 4；生产可观测性与互操作性待验证

- 作者的 monitor 冻结网关、调用向量和时间窗；C0–C2 由调用方提供证据标识，monitor 不独立证明 issuer/transmitter。未知网关与未来调用不在完成声明内。 [Revocation Is Not Complete at Receipt: An Executable Outcome Contract for Distributed Agent-Tool Gateways](https://arxiv.org/abs/2610.15991) PDF pp.2–3, §2.1–2.2

- 112/225=49.78% 的效果提交来自预设拓扑：两个 receiver 之一管理四个网关及112个向量；不是生产环境的事故概率。 [Revocation Is Not Complete at Receipt: An Executable Outcome Contract for Distributed Agent-Tool Gateways](https://arxiv.org/abs/2610.15991) PDF pp.3,8, §3.3 / §7

- MCPMark 闭环执行中，selective C3 产生145个效果；正常 C4 暴露31次调用并全部拒绝。但任务验证仅4/60 arms通过，两组调用群体不同，不应据此计算通用风险降低率。 [Revocation Is Not Complete at Receipt: An Executable Outcome Contract for Distributed Agent-Tool Gateways](https://arxiv.org/abs/2610.15991) PDF pp.1,8

- 作者不主张新撤销原语或 Keycloak 缺陷；50% suppression 下存在机制成本失败，外部工作负载的预设优势假设也失败。 [Revocation Is Not Complete at Receipt: An Executable Outcome Contract for Distributed Agent-Tool Gateways](https://arxiv.org/abs/2610.15991) PDF pp.2–3, §2.4 / §3.2

### unknowns

- 如何发现未登记网关？独立效果观察能否覆盖外部 SaaS、副作用和长事务？

- 断网 fail-closed 的业务可用性损失由谁承担？

- 时间同步、重启、重复消息、网关替换后，证据边界是否仍可信？

- 单次集成维护成本是否使产品退化为定制安全咨询？

### alternatives

- 短寿命令牌、每次调用在线校验、fail-closed：减少旧权限窗口，但增加依赖与可用性成本。

- Keycloak / CAEP / SSF 提供身份与信号传输；是否可补齐效果观察须在目标部署中验证。

- OpenA2A AIM：公开 README 提供身份、capability authorization 与审计；已构成相邻功能供给，不能称无人竞争。

- MVAR：README 展示执行防火墙与 witness；未独立运行其安全测试，也未证明跨网关撤销等价性。

### plan

- 第1–7天：访谈3个跨网关部署，冻结撤销对象、可接受延迟、效果类型与责任人。

- 第8–14天：在沙盒复现 receiver 已持久化但部分网关未更新；用独立文件/数据库观察效果。

- 第15–21天：增加重启、丢消息、未知网关、时钟偏差与观察丢失；比较短令牌和在线校验基线。

- 第22–30天：在第二类网关验证适配复用；测p95延迟、可用性、控制流量、证据完整率和维护人天。

### gates

- 建议门槛：预注册故障矩阵中不出现错误 complete；观测不全应返回 unknown，违规证据不可被覆盖。

- 两类网关总接入≤10人天、额外p95延迟≤客户预定SLO；这些为试点门槛，不是文献结果。

- 如果必须信任无法独立观测的效果、现有平台可低成本满足、或无人为证据付费，停止独立产品。

未知：Agent 身份与授权已有开源供给；窄切口是否低拥挤仍需专利、采购和融资调查

上游按目标部署的 IAM/网关采购额、下游按该完成证明产品细分采购额定义 CR5；暂无可比销售数据，均未知。GitHub 项目数量或 stars 不能充当营收份额。

单客年度贡献 = 订阅与验收收入 − 部署人天成本 − 持续适配成本 − 证据存储/观测成本。先检验2类异构网关接入是否可复用。避免用未观测的安全事故减少金额证明 ROI。

{'accounts': 200, 'price': 40, 'penetration': 10, 'growth': 25, 'unit': '大型部署客户', 'note': '仅是假设年度软件收入池；不把整个 IAM 或网络安全市场视为可服务市场。验收服务收入与经常性订阅应分别核算。'}

上游: IAM / 令牌签发 → CAEP / SSF → 网关与策略引擎
切入层: 执行回执 + 独立效果观察 + 有界验收契约
下游: 企业安全 / IAM 平台 / Agent 工具运营（买方假设）

## 3. 科学仪器异常处理

从一个高频、可审计的分析失败类型切入，做实验室软件的异常处理模块，而不是泛化科学家 Agent。第三优先级源于独立真值、仪器适配和跨材料迁移验证更贵；若能取得数据及领域伙伴，优先级可上调。

原始光谱与物理模型保持不变；先运行确定性分析，失败时只调整允许的拟合窗口/质量阈值，最多三次修复，记录理由与参数。返回 ACCEPT、REPAIR_ACCEPT 或 NaN。NaN 是有意拒答，不应作为必须消灭的失败。

研究判断 TRL 3–4；未验证持续在线实验室运行

- 203条 β-Ga2O3 光谱中，原脚本183条成功、20条失败；作者报告保留183条、恢复16条、4条NaN。16/20是异常子集恢复率，不是全部样本精度。 [Autonomous adaptive spectral analysis with an LLM agent for self-driving laboratories](https://arxiv.org/abs/2610.25619) PDF pp.1,8

- 16个修复中9个只放松R²阈值至0.989–0.994；2个移动窗口、1个调整宽度、4个组合调整。应比较确定性参数搜索，不能把全部收益归因于LLM。 [Autonomous adaptive spectral analysis with an LLM agent for self-driving laboratories](https://arxiv.org/abs/2610.25619) PDF p.7, §3

- 每个样本为独立会话，禁止使用历史Urbach能量、历史NaN标签与外部搜索；最多三次修复。公开补充材料提供指令。 [Autonomous adaptive spectral analysis with an LLM agent for self-driving laboratories](https://arxiv.org/abs/2610.25619) PDF pp.3–4,13+, Supplementary Note S1

- 作者明确未证明能识别数值上成功但物理错误的结果，且限于一种光学描述符和一次材料实验。 [Autonomous adaptive spectral analysis with an LLM agent for self-driving laboratories](https://arxiv.org/abs/2610.25619) PDF p.8, §4

- Self-Building Labs 覆盖布局、数字孪生、机器人技能与流程；粉末称量研究需要联合优化工具形态和控制，提示平台捆绑及硬件定制两项风险。 [Self-Building Labs](https://arxiv.org/abs/2610.23826) PDF p.1；另见 powder PDF p.1

### unknowns

- 独立专家是否认为恢复值在物理上正确，而不只是R²较高？

- 随机种子/模型版本改变后，接受、修复、拒答是否稳定？

- 推理时间、成本、专家异步复核和停机节约尚未量化。

- 原始数据代码仓库可访问，但未执行作者工作流；不能称独立复现成功。

### alternatives

- 确定性参数网格搜索 + 物理约束 + NaN：首要基线，成本低且可重复。

- 领域专家检查异常：提供独立裁决与真实人工工时。

- 仪器厂商内置算法 / 实验室编排平台：可能捆绑该功能。

- Self-Building Labs 等平台研究：是潜在集成方也可能吸收异常处理层，未核验商业采购情况。

### plan

- 第1–7天：取得两种仪器/材料的去标识历史样本；同时收集显式失败和隐藏物理错误。

- 第8–14天：专家盲审建立接受/修复/拒答真值；比较固定网格搜索、专家和受限Agent。

- 第15–21天：跨时间/材料留出；重复运行至少5次，测不支持值接受率、有效恢复率及决策稳定性。

- 第22–30天：影子接入真实流程；冻结物理规则，核算专家工时和每仪器适配成本。

### gates

- 建议门槛：独立盲审中不支持数值不能增加；相对确定性搜索的额外净收益为正。

- 第二仪器适配≤10人天，专家工时节约≥30%；均为试点目标，并非已实现结果。

- 若恢复主要来自放松阈值、无法优于规则基线、或物理错误未被识别，应降级为确定性软件功能。

未知：自驱实验室已有平台研究，异常处理模块的独立市场尚未确认

应按具体仪器类别及地域计算上游设备销售CR5，按该异常分析软件采购额计算下游CR5；不可把全部科学仪器市场合并。目前无统一口径销售分母，均未知。

年节约 = 异常次数 × 可安全自动处理比例 × 每次节约人工小时 × 专家小时成本 + 可核验停机节约 − 推理/质控/适配成本。不要把16/20直接迁移成客户的可处理比例。

{'accounts': 300, 'price': 15, 'penetration': 10, 'growth': 15, 'unit': '实验室站点', 'note': '站点数 × 每站点软件年费为演示假设。多仪器一站点需去重；一次性定制、硬件收入不计入订阅池。'}

上游: 仪器 / 原始测量 → 确定性分析代码 → 领域约束
切入层: 受限修复 + 物理验证 + 拒答 + 追溯记录
下游: 材料研发实验室 / 仪器软件 / CRO（买方假设）