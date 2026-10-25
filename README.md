# FREERIDE Frontier Radar

**[打开在线 DEMO](https://lancewang1.github.io/freeride-frontier-radar/)** · **[本轮研究报告](LANDSCAPE_REPORT.md)** · **[融资台账 CSV](funding-ledger.csv)** · **[证据快照 JSON](landscape.json)**

v0.4 · 2026-10-25。面向一级市场基金的技术—资本研究工具：先比较中国与全球的同一技术领域，再查看证据、分类边界与验证问题。

## 本轮交付

- 8个候选领域，中国 / 全球（含中国）联动四象限。
- 16组真实OpenAlex检索请求、最多20条/组代表记录及机构信息。
- 22条融资与观察记录：19条已完成融资报道，另有洽谈、混合新老股和相邻业务排除记录。
- 12项会议或技术讨论旁证：8个NeurIPS workshop详情、4项中国企业技术材料/访谈；不把覆盖不完整的讨论强行打分。
- 融资金额/公告事件数切换、精确披露模式、剔除最大一笔敏感性检查。
- 逐条来源、有限原文引句、来源哈希、原币金额、汇率、估值口径与排除原因；CSV / JSON下载。
- 保留早期三方向深研案例、浏览器本地复核与备忘录导出，明确标为历史研究而非最新筛选结果。

## 结论与边界

**这是一版完整可运行、可审计的公开样本工具，不是全市场普查或投资级排名。** 主图已删除虚构坐标。融资是人工检索核验样本，未收录不代表零。技术轴暂用论文检索量代理，未声称已经量化所有研讨会、访谈与采用情况。基础模型查询发现误匹配，主动退出技术评分，保留融资参照。

合成数据在当前两地样本中进入目标区域，但剔除最大融资后数据不足，不能确认低拥挤；推理服务有明显资本跟进；评测、记忆、实验室和身份安全均已有融资。详细结果、原始指标与下一步验证工作包见报告。

窗口为2025-10-01至2026-09-30；读取日2026-10-25。中国论文指至少一个机构country_code=CN，融资按企业主要经营地。全球包含中国。主图分别计算当地有效领域百分位，分母可见；相同分数不代表相同绝对规模。

市场容量、真实CAGR与CR5不能从融资金额推导，未编造这些数值。研究由当前助手完成，未接外部模型API。没有后台自动推理或已启用的定时任务。

## 本地运行

Python 3.10+；运行应用不需要安装依赖或提供密钥。

```sh
python -m http.server 8000 --bind 127.0.0.1
```

打开 http://localhost:8000 。不要直接双击HTML，浏览器会限制JSON加载。

```sh
# 导出已审阅台账与本轮报告
python scripts/build_landscape.py
# 新论文统计进入private/landscape-pending.json，不覆盖已审阅快照
python scripts/refresh_landscape.py
# arXiv 新信号，进入待研队列
python scripts/collect.py
```

刷新脚本遇到429会停止，不绕过限流、不把失败记作零。2026-10-25本轮补充OpenAlex查询已遇到429。Wind接口返回余额不足，因此本轮使用公开新闻，并未冒充Wind数据库结果。

## 验证

```sh
python scripts/test_data.py
python scripts/test_landscape.py
node scripts/test_landscape.js
```

页面通过Edge / Playwright验证双图联动、敏感性开关、未知值、台账筛选、导出、旧研究视图及移动端布局。详见 [验证记录](VALIDATION.md)。

可选复跑UI测试：安装Python `playwright`，在已有Edge的机器启动本地8000端口服务，再运行 `python scripts/test_browser.py`。可通过环境变量 `FR_DEMO_URL` 指定测试地址；下载与截图写入已忽略的 `test-results/`。

`workflow-templates/` 是未启用的可选Actions模板；当前发布凭据没有workflow scope。GitHub Pages直接发布main分支。自动化采集与自动发布是不同动作，新的材料必须复核。

## 文件与来源

- `landscape.json`：本轮原始检索结果、融资事件、来源指纹、FX与讨论旁证。
- `radar-core.js`：缺失值处理、计分、估值去重与敏感性逻辑。
- `landscape-ui.js`：地图、来源台账、筛选与下载。
- `data.json` / `app.js`：2026-10-23早期研究案例。
- `pending.json`：独立arXiv待研材料，不直接进入已审阅地图。

不含客户原始材料、基金配置、本机数据库、下载论文或密钥。公开快照不包含完整新闻正文。复核记录仅存当前浏览器，不自动上传。

## 许可

原创代码使用MIT。研究说明引用时注明FREERIDE AI；第三方论文、有限引句、新闻和元数据的权利归原作者，MIT不授予这些第三方材料的权利。OpenAlex元数据采用其CC0政策，查询覆盖与解析质量仍需复核。
