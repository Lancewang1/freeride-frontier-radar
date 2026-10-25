# FREERIDE 中国与全球技术—资本地图

公开证据版 v0.4 · 2026-10-25

统计窗口：2025-10-01 至 2026-09-30。全球包含中国。

## 结论先行

本轮完成了可复现的公开样本版地图，而不是全市场普查。8个领域、16组论文检索、22条融资/观察记录、12项会议或技术讨论旁证。没有证据证明任何方向已是低拥挤的确定投资机会。

1. 合成数据在当前中外金额样本图均进入技术高/样本资本低区域。但可计量融资集中于光轮智能的单笔合并公告，剔除最大一笔后无可计金额，因此只能列为第一补证候选，不能视为稳定发现。应继续拆分合成文本、仿真数据和评测反馈，避免异质性混在一起。

2. 推理服务中外都有大额融资。硅基流动超20亿元人民币B轮，Fireworks 15.05亿美元D轮。该方向已有资本跟进，新增投资需寻找技术路线或单位经济性差异，而不是泛赛道叙事。

3. 评测并非无人投资：LMArena 1.5亿美元A轮、Patronus 5000万美元B轮；中国UniPat拟3亿美元的交易在读到的正文中仍处于谈判。不能把拟融资记作完成，也不能把没有已完成样本误解成低关注。

4. Agent记忆在中国已有亿元级融资报道，全球有Mem0 A轮；身份授权有Hush与Cymphony。窄切口仍可研究，但本轮未显示它们具备“技术高普及、资本低关注”的稳健证据。

5. 自主实验室存在Lila扩募及中国融资事件。此前仪器异常处理案例有研究价值，但不能据此推断整个实验室方向属于目标象限。

## 下一轮验证工作包

- 优先A：合成数据的质量验证与结果反馈。先补充海外融资及中国模糊金额，拆分仿真与文本数据；验证合成数据能否提升真实留出任务，控制泄漏、分布偏移和同质化。访谈模型训练团队，拿到训练预算、数据采购和可复现实验。若增益只发生在相似基准或大平台可免费覆盖，停止独立产品判断。

- 优先B：业务结果驱动的在线审计。属于评测方向内部切口，不把母赛道称为冷门。用独立标签、随机抽查基线和全成本衡量质量与人工节约。具体30天方案见历史研究案例。

- 观察C：可治理长期记忆与跨网关权限。分别检验冲突记忆更新、遗忘和迁移，以及撤销后的实际效果观察。现有平台融资和内置功能是替代风险；先找企业愿付费的失败案例，而非先写大市场故事。

## 统计方法

技术轴：同一地区的7个有效领域OpenAlex检索命中量百分位。基础模型检索出现误匹配，保留原始记录但不参与技术排序、不落点。技术轴不是完整的论文+会议+访谈综合指标，也不是采用率。

资本轴：可计量且已完成报道的融资金额样本百分位；可切换为已核验公告事件数。合并公告计1事件，金额以百万原币与美元表示。每笔按公司主标签归类一次，不能理解为全部资金用于该技术。

百分位公式：100 × [比该值小的领域数 + (同值领域数−1)/2] ÷ (有效领域数−1)。未知不入分母。两地金额有效领域分母不同，图中明确显示；排名只在样本中有意义。

敏感性：可只用精确披露金额，或剔除每方向最大一笔。剔除后无可计金额时保留未知，而非0。估值只用每家企业最近一次明确投后美元估值求中位数，样本量同步展示，投前/未说明及洽谈估值不参与。

## 原始指标对照

|领域|中国论文命中|全球论文命中|中国可计金额 USD m|全球可计金额 USD m|中国公告数|全球公告数|

|---|---:|---:|---:|---:|---:|---:|

|基础模型训练|626|3085|2,000.00|97,000.00|1|3|

|推理优化与服务|731|2399|296.02|1,801.02|1|2|

|Agent 长期记忆|137|525|未知|20.00|1|2|

|模型评测与审计|75|696|未知|200.00|0|2|

|Agent 身份与授权|17|208|未知|55.00|0|2|

|合成数据|165|2409|145.58|145.58|2|2|

|自主实验室|5|150|未知|115.00|2|3|

|机器人基础模型|436|1205|140.00|740.00|2|3|

金额为已收录可计量部分，含约数/明确下界/推导增量，不是精确行业总额。数量级披露不强行数值化。基础模型论文命中不合格，仅展示用于审计。

## 对原始新闻做了哪些修正

- Mem0标题2400万美元包含种子轮与A轮，本期计A轮2000万美元。

- Fireworks C轮含primary/secondary混合，无法拆分则排除；D轮按公告15.05亿美元。

- Lila A轮最终350百万美元中，235百万美元首关在2025年9月，本期仅计115百万美元增量；官网不同页面有10月10日/15日差异，均在窗口内。

- 光轮智能A++及A+++合并公告10亿元，不重复计两笔；MemTensor亿元级、戴纳近亿元等保留模糊状态。

- 瑞莱智慧为泛AI安全相邻供给，不把其全部融资归入Agent身份授权；UniPat谈判交易不计入完成统计。

## 融资事件证据

### Anthropic · 2026-02-12 · completed

方向：基础模型训练；地域：US；金额：30000 百万 USD；口径：exact。

包含此前宣布的微软/NVIDIA部分投资，不重复另计；公司整体融资，不代表全部用于预训练。

> We have raised $30 billion in Series G funding

[原文](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation)；SHA256 `193db46d1c8fec5dbb99be0d2e09e43ac3d62d55f2360974cb547e743b702152`

### Anthropic · 2026-05-28 · completed

方向：基础模型训练；地域：US；金额：65000 百万 USD；口径：exact。

包含150亿美元已承诺的hyperscaler投资，不重复另计。

> Anthropic has raised $65 billion in Series H funding

[原文](https://www.anthropic.com/news/series-h)；SHA256 `14e29a288337ad6f8ba0e2afbe8c062d40083a4645b5d2f77e865a118ad4a1c3`

### Moonshot AI · 2026-05-07 · completed

方向：基础模型训练；地域：CN；金额：2000 百万 USD；口径：approx。

报道引述融资顾问及领投方；约数，不是精确银行交割金额。

> has raised about $2 billion at a valuation of $20 billion

[原文](https://techcrunch.com/2026/05/07/chinas-moonshot-ai-raises-2b-at-20b-valuation-as-demand-for-open-source-ai-skyrockets/)；SHA256 `38d41ec166e715f2d0b4e4faa086d9b7f2f423293af4bd3a6e029a6620d568ff`

### Fireworks AI · 2025-10-28 · excluded

方向：推理优化与服务；地域：US；金额：250 百万 USD；口径：mixed-secondary。

新股与老股混合，无法拆分，默认不纳入新增融资金额与有效事件数。

> This round, which includes primary and secondary funding

[原文](https://fireworks.ai/blog/fireworks-ai-series-c-funding)；SHA256 `65ac190f159b95313d3a8fd04c439315eb45892e3a5ccf04a11fe8ad07dbe158`

### Fireworks AI · 2026-07-15 · completed

方向：推理优化与服务；地域：US；金额：1505 百万 USD；口径：exact。

按公司公告金额1505百万美元，不用新闻标题的四舍五入1500。

> Fireworks announced a $1.505 billion Series D at a $17.5 billion valuation

[原文](https://fireworks.ai/blog/fireworks-series-d-funding)；SHA256 `afccfa97698f6137ef9cc8e1412f8f464ceece9e33bc2e6b71fc69a44204a323`

### 硅基流动 · 2026-06-16 · completed

方向：推理优化与服务；地域：CN；金额：2000 百万 CNY；口径：lower-bound。

金额记下界，图中合计为已核验金额下界；不能当行业总融资。

> 完成超20亿元人民币B轮融资

[原文](https://www.21jingji.com/article/20260616/herald/66474a56fcc6d4037f0f3bafdc8af90e.html)；SHA256 `8409b64c2554b0928daf9ed6d98741cfda81593cff2ffac26a5fc702ab7d536e`

### Mem0 · 2025-10-28 · completed

方向：Agent 长期记忆；地域：US；金额：20 百万 USD；口径：exact。

2400万美元标题含未公告的历史种子轮；本轮仅计2000万美元。

> a $20 million Series A

[原文](https://techcrunch.com/2025/10/28/mem0-raises-24m-from-yc-peak-xv-and-basis-set-to-build-the-memory-layer-for-ai-apps/)；SHA256 `517a0fedd94d9ed35fb490554f7fce6aaa59d2376c0ca9dd133043c0e811e7b4`

### 记忆张量 MemTensor · 2026-07-20 · completed

方向：Agent 长期记忆；地域：CN；金额：数量级/未知 百万 CNY；口径：coarse。

亿元级不擅自变成精确1亿元；只计1个已核验事件。主营记忆基础设施，也开发基模，完整归类仅作关联公司统计，不是用途分摊。

> 宣布完成亿元 Pre-A 轮融资

[原文](https://www.leiphone.com/category/industrynews/opQqNuktWFDh1i0X.html)；SHA256 `9343e2d9e6cbecc68de6c297c437dbe512bd00e301928e52ed3077bde6a42837`

### Patronus AI · 2026-06-25 · completed

方向：模型评测与审计；地域：US；金额：50 百万 USD；口径：exact。

公司从静态评测延伸至训练仿真环境；归类边界存在变化。

> announce our $50M Series B

[原文](https://www.patronus.ai/news/announcing-our-50m-series-b)；SHA256 `5a02b69953d69726343e322125d118eab01338b6dd624fc6843c91d93075652a`

### LMArena · 2026-01-06 · completed

方向：模型评测与审计；地域：US；金额：150 百万 USD；口径：exact。

2025年5月1亿美元种子轮在窗口外，不计入。

> raised a $150 million Series A at a post-money valuation of $1.7 billion

[原文](https://techcrunch.com/2026/01/06/lmarena-lands-1-7b-valuation-four-months-after-launching-its-product/)；SHA256 `697d3fb00befc4cb5c095d9357dfb892efc0d70a8ca6e83078afcc5dd14255fe`

### UniPat AI · 2026-09-11 · watch

方向：模型评测与审计；地域：CN；金额：300 百万 USD；口径：proposed。

报道的拟融资3亿美元、拟估值25亿美元，不计已完成融资或已实现估值。

> 交易仍在谈判，具体条款尚未最终确定

[原文](https://www.36kr.com/p/3977467794069126)；SHA256 `430012401982de71da8da7b220efcea220313ab47ccf46d9c5a739671585e776`

### Hush Security · 2026-07-28 · completed

方向：Agent 身份与授权；地域：IL；金额：30 百万 USD；口径：exact。

累计4100万美元不重复计；产品涉及Agent权限、注册与kill switch，非纯撤销证明。

> raising $30 million in a Series A funding round

[原文](https://www.securityweek.com/hush-security-raises-30-million-for-ai-agent-governance/)；SHA256 `4da173dd98ef31bc0fd3f0342cdba9ff3c563afcbd2d8a53629832d85f6975b3`

### Cymphony · 2026-09-10 · completed

方向：Agent 身份与授权；地域：US/IL；金额：25 百万 USD；口径：exact。

媒体报道，公司跨纽约/特拉维夫；超过1亿美元投后估值是下界，未作为精确估值纳入。

> Cymphony has secured $25 million in Series A funding

[原文](https://finance.yahoo.com/technology/ai/articles/cymphony-raises-25m-agent-identity-092720701.html)；SHA256 `d785c0c9d662a139cccbb7bee210f8276e0efe6c00d1152ce4d23f21e99348fa`

### 瑞莱智慧 · 2026-07-21 · adjacent

方向：Agent 身份与授权；地域：CN；金额：数量级/未知 百万 CNY；口径：coarse。

相邻AI安全公司，包含对抗测试、隐私与AIGC检测；不足以把全部资金归给Agent身份授权，排除主统计。

> 数亿元规模的B1轮和B2轮

[原文](https://news.pedaily.cn/202607/566619.shtml)；SHA256 `1c0f92d1b8c998bf8b160d25ffd9e978523b7a16349ebb4316d64d0967d98f64`

### 光轮智能 · 2026-03-12 · completed

方向：合成数据；地域：CN；金额：1000 百万 CNY；口径：exact。

两个轮次合并公告，不拆成两个金额/两个公告事件。仿真、数据和评测复合业务，按数据基础设施主标签计一次。

> 光轮智能完成10亿元A++及A+++轮融资

[原文](https://www.ncsti.gov.cn/kjdt/scyq/zgckxc/zgcdt/202603/t20260312_240699.html)；SHA256 `a43b77a5878dd59446a903a35071bf4dba0bb91dcdcc16f7363579ce491e87b1`

### 数创弧光 DataArc · 2026-07-13 · completed

方向：合成数据；地域：CN；金额：数量级/未知 百万 CNY；口径：coarse。

金额与估值均只有数量级，不填精确值；文内历史种子轮累计不重复计。

> 数千万元 级 新一轮融资

[原文](https://finance.sina.com.cn/wm/2026-07-13/doc-inihspyr7506463.shtml)；SHA256 `bc9155d4a4444180f28fe66af41b33d609b84f807334f8092cb3b7a673f13ba9`

### Lila Sciences · 2025-10-10 · completed

方向：自主实验室；地域：US；金额：115 百万 USD；口径：derived-increment。

本期只计350−235=115百万美元增量；9月15日首关235在窗口外。官网显示10月10日，旧公告更新称10月15日，日期存在5天差异但均在窗口内。

> close of our $350M Series A

[原文](https://www.lila.ai/news/announcing-the-close-of-our-series-a)；SHA256 `da3becc85bf05a51dfe76c6cc5b9ab832cf2d9316f1fc70b582bed52b53596f2`

[首关交叉核验](https://www.lila.ai/news/series-a-235-million)

### 戴纳科技 · 2026-04-03 · completed

方向：自主实验室；地域：CN；金额：数量级/未知 百万 CNY；口径：coarse。

按已读取正文日期4月3日，搜索发现页为4月2日；近亿元未定义为精确值。自动化实验室平台，不是纯异常处理模块。

> 完成近亿元B+轮融资

[原文](https://eu.36kr.com/zh/p/3750417621795588)；SHA256 `05d7f46e6e4498907778169d54b803b4e76164c5729d1c29d22617028274eb7e`

### 和光智成 · 2026-08-06 · completed

方向：自主实验室；地域：CN；金额：数量级/未知 百万 CNY；口径：coarse。

金额模糊，只计事件；AI材料研发和自主实验室一体化。

> 完成天使轮数千万融资

[原文](https://finance.sina.com.cn/tech/roll/2026-08-06/doc-inimknci3838292.shtml)；SHA256 `42d593c701544168042d577d31d89f97f085a7dddfd8fe613c55015e70ec0236`

### X Square Robot · 2026-01-13 · completed

方向：机器人基础模型；地域：CN；金额：140 百万 USD；口径：exact。

通用具身模型及机器人平台，不能将金额当成纯模型研发预算。

> raised $140M in Series A++ funding

[原文](https://www.finsmes.com/2026/01/x-square-robot-raises-140m-in-series-a-funding.html)；SHA256 `48e5a11c909f71a90f400825ef06e1b7c70959582055838cc1098f33d1a32a3f`

### 极佳视界 · 2026-03-13 · completed

方向：机器人基础模型；地域：CN；金额：数量级/未知 百万 CNY；口径：coarse。

近10亿元不是精确10亿元，金额不纳入；模型与本体复合公司。

> 完成近10亿元Pre-B轮融资

[原文](https://www.ncsti.gov.cn/kjdt/yqdy/yqdt/202603/t20260313_240825.html)；SHA256 `03a7d1692655c737f373010d2de53d740b2411e2350e9fc6c89a1c61257ca85e`

### Physical Intelligence · 2025-11-21 · completed

方向：机器人基础模型；地域：US；金额：600 百万 USD；口径：exact。

按读取报道日期；正文估值单位缺漏，不擅自补成精确估值。

> raised $600 million in a funding round led by CapitalG

[原文](https://news.crunchbase.com/venture/biggest-funding-rounds-ai-fintech-lambda/)；SHA256 `b4d15200997faf501bd99b9253e80b80b84baccb3f4557894a3c029fc3dee9e8`

## 论文检索登记

- 机器人基础模型 / cn / 436：`"vision-language-action" OR "robot foundation model"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22vision-language-action%22+OR+%22robot+foundation+model%22%2Cauthorships.institutions.country_code%3Acn&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 机器人基础模型 / global / 1205：`"vision-language-action" OR "robot foundation model"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22vision-language-action%22+OR+%22robot+foundation+model%22&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 模型评测与审计 / cn / 75：`"LLM evaluation" OR "language model evaluation" OR "LLM judge"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22LLM+evaluation%22+OR+%22language+model+evaluation%22+OR+%22LLM+judge%22%2Cauthorships.institutions.country_code%3Acn&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 模型评测与审计 / global / 696：`"LLM evaluation" OR "language model evaluation" OR "LLM judge"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22LLM+evaluation%22+OR+%22language+model+evaluation%22+OR+%22LLM+judge%22&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 基础模型训练 / cn / 626：`("pretraining" OR "pre-training" OR "scaling") AND ("language model" OR "LLM")`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%28%22pretraining%22+OR+%22pre-training%22+OR+%22scaling%22%29+AND+%28%22language+model%22+OR+%22LLM%22%29%2Cauthorships.institutions.country_code%3Acn&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；低精度：抽查发现global-scale、非预训练等误匹配；不纳入技术百分位和象限，仅作融资参照。

- 基础模型训练 / global / 3085：`("pretraining" OR "pre-training" OR "scaling") AND ("language model" OR "LLM")`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%28%22pretraining%22+OR+%22pre-training%22+OR+%22scaling%22%29+AND+%28%22language+model%22+OR+%22LLM%22%29&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；低精度：抽查发现global-scale、非预训练等误匹配；不纳入技术百分位和象限，仅作融资参照。

- Agent 身份与授权 / cn / 17：`"agent security" OR "agent authorization" OR "agent identity"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22agent+security%22+OR+%22agent+authorization%22+OR+%22agent+identity%22%2Cauthorships.institutions.country_code%3Acn&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- Agent 身份与授权 / global / 208：`"agent security" OR "agent authorization" OR "agent identity"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22agent+security%22+OR+%22agent+authorization%22+OR+%22agent+identity%22&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 推理优化与服务 / cn / 731：`"LLM inference" OR "speculative decoding" OR "KV cache"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22LLM+inference%22+OR+%22speculative+decoding%22+OR+%22KV+cache%22%2Cauthorships.institutions.country_code%3Acn&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 推理优化与服务 / global / 2399：`"LLM inference" OR "speculative decoding" OR "KV cache"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22LLM+inference%22+OR+%22speculative+decoding%22+OR+%22KV+cache%22&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- Agent 长期记忆 / cn / 137：`"agent memory" OR ("long-term memory" AND ("LLM" OR "language model" OR "agent"))`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22agent+memory%22+OR+%28%22long-term+memory%22+AND+%28%22LLM%22+OR+%22language+model%22+OR+%22agent%22%29%29%2Cauthorships.institutions.country_code%3Acn&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- Agent 长期记忆 / global / 525：`"agent memory" OR ("long-term memory" AND ("LLM" OR "language model" OR "agent"))`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22agent+memory%22+OR+%28%22long-term+memory%22+AND+%28%22LLM%22+OR+%22language+model%22+OR+%22agent%22%29%29&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 自主实验室 / cn / 5：`"self-driving lab" OR "autonomous laboratory"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22self-driving+lab%22+OR+%22autonomous+laboratory%22%2Cauthorships.institutions.country_code%3Acn&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 自主实验室 / global / 150：`"self-driving lab" OR "autonomous laboratory"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22self-driving+lab%22+OR+%22autonomous+laboratory%22&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 合成数据 / cn / 165：`"synthetic data"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22synthetic+data%22%2Cauthorships.institutions.country_code%3Acn&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

- 合成数据 / global / 2409：`"synthetic data"`；[API](https://api.openalex.org/works?filter=from_publication_date%3A2025-10-01%2Cto_publication_date%3A2026-09-30%2Ctitle.search%3A%22synthetic+data%22&per-page=20&select=id%2Cdoi%2Ctitle%2Cpublication_date%2Cauthorships%2Cprimary_location&sort=cited_by_count%3Adesc)；关键词检索代理，非人工确认全量；排名可能受检索口径影响。

## 会议与技术讨论旁证

NeurIPS 2025官方列表包含56个独立workshop，本次阅读8个详情。另记录4项中国企业技术讨论/访谈，与融资报道同文者不当独立来源，也不进入评分。

- [Embodied World Models for Decision Making](https://neurips.cc/virtual/2025/workshop/109532)：2025-12；NeurIPS全球会议旁证；不按举办地归为中国或美国技术贡献；仅表示主题有组织讨论。

- [AI4Mat-NeurIPS-2025: NeurIPS 2025 Workshop on AI for Accelerated Materials Design](https://neurips.cc/virtual/2025/workshop/109538)：2025-12；NeurIPS全球会议旁证；不按举办地归为中国或美国技术贡献；仅表示主题有组织讨论。

- [ML for Systems](https://neurips.cc/virtual/2025/workshop/109537)：2025-12；NeurIPS全球会议旁证；不按举办地归为中国或美国技术贡献；仅表示主题有组织讨论。

- [Workshop on Multi-Turn Interactions in Large Language Models](https://neurips.cc/virtual/2025/workshop/109539)：2025-12；NeurIPS全球会议旁证；不按举办地归为中国或美国技术贡献；仅表示主题有组织讨论。

- [The First Workshop on Efficient Reasoning](https://neurips.cc/virtual/2025/workshop/109556)：2025-12；NeurIPS全球会议旁证；不按举办地归为中国或美国技术贡献；仅表示主题有组织讨论。

- [Workshop on Scaling Environments for Agents](https://neurips.cc/virtual/2025/workshop/109540)：2025-12；NeurIPS全球会议旁证；不按举办地归为中国或美国技术贡献；仅表示主题有组织讨论。

- [Evaluating the Evolving LLM Lifecycle:  Benchmarks, Emergent Abilities, and Scaling](https://neurips.cc/virtual/2025/workshop/109549)：2025-12；NeurIPS全球会议旁证；不按举办地归为中国或美国技术贡献；仅表示主题有组织讨论。

- [AI for Science: The Reach and Limits of AI for Scientific Discovery](https://neurips.cc/virtual/2025/workshop/109578)：2025-12；NeurIPS全球会议旁证；不按举办地归为中国或美国技术贡献；仅表示主题有组织讨论。

- [记忆张量 MemTensor · 技术路线讨论](https://www.leiphone.com/category/industrynews/opQqNuktWFDh1i0X.html)：2026-07-20；中国企业；与融资报道同文，不当作独立第二来源，不计入技术分数。

- [戴纳科技 · 技术路线讨论](https://eu.36kr.com/zh/p/3750417621795588)：2026-04-03；中国企业；与融资报道同文，不当作独立第二来源，不计入技术分数。

- [数创弧光 DataArc · 技术路线讨论](https://finance.sina.com.cn/wm/2026-07-13/doc-inihspyr7506463.shtml)：2026-07-13；中国企业；与融资报道同文，不当作独立第二来源，不计入技术分数。

- [硅基流动 · 技术路线讨论](https://www.21jingji.com/article/20260616/herald/66474a56fcc6d4037f0f3bafdc8af90e.html)：2026-06-16；中国企业；与融资报道同文，不当作独立第二来源，不计入技术分数。

## 限制与下一步

- 技术纵轴仅用OpenAlex检索命中量作为代理，尚未混入不可比的访谈/会议覆盖；不是实际采用率或成熟度。

- 中国论文口径为至少一个OpenAlex机构country_code=CN；全球含中国。不是按作者姓名、新闻语言或论文下载地点判定。缺失机构信息会漏记中国贡献。

- OpenAlex publication_date可能是期刊正式出版时间而非首次预印本时间；只取聚合count，未做全库版本合并。

- 每个查询保留最多20条按引用量排序的记录供审阅，非随机样本，不能由样本精度推算全库准确率。基础模型检索发现污染，主动不落点。

- 融资为人工检索核验样本，公开披露选择偏差大。本文不声称任何方向融资覆盖完整，也不把未收录事件算作零。

- 每笔关联公司融资只分配一个主标签；金额是公司融资，不是该技术方向的预算。复合业务分类是研究判断。

- 金额总和为可计量已披露部分，含明确下界/约数，并非精确行业总额。数千万/亿元级等模糊披露不转换为数字。

- 没有两个同口径历史快照，不绘制趋势箭头或假增长率。融资估值不是市场容量，未计算无依据的TAM/CAGR/CR5。

本轮OpenAlex额外检索遇到429限流，因此未继续重试或将缺失返回写作零。Wind返回余额不足，本报告使用用户指定的公开融资新闻；不冒充付费数据库结果。

要从本版升级为投资级排名，需要完整领域词表、均衡多源融资检索、人工实体去重、机构国家补全、季度重复快照，以及由预算负责人验证的买方需求。市场容量/CAGR/CR5不能从融资金额推导。