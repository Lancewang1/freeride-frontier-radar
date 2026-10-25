# FREERIDE AI · 合成数据投资研究工作台

[在线 DEMO](https://lancewang1.github.io/freeride-frontier-radar/) · [完整深研](SYNTHETIC_DEEPDIVE.md) · [论文复核台账](synthetic-evidence.json)

当前 v0.5 聚焦合成数据。此前三个案例已撤出当前版本；Git 历史保留旧提交。中国/全球四象限仍可交互对照，默认选择合成数据。客户材料与下载论文全文未发布。

## 本轮交付

- 8篇核心论文的方法、结果、反证、投资含义和验证实验；2篇来自原检索名单，6篇补充机制/反证。均未独立复现，也未逐项审查全部补充材料和证明。
- 原合成数据40条地域记录，去重38篇，全部完成标题级归类；不把其余记录冒充精读。
- 中国/全球TAM与CAGR来源对照，明确第三方预测及同页口径差异；分离宽市场与窄产品。
- 可编辑TAM/SAM/SOM计算器、交付容量上限、数量/单价增长敏感性及JSON导出。所有输入为假设，非采购普查。
- 产业链图、竞争与平台替代、上下游CR5定义和数据缺口、单位经济性及30天验证方案。

研究判断：优先验证工业视觉任务中的生成＋真实验收闭环，机器人迁移验证次之。尚未证明低拥挤或商业成立。CR5缺少细分收入与总市场分母，保留未知；不以五个公司名字或融资份额代替。

## 运行与更新

```sh
python -m http.server 8000
```

打开 localhost:8000。无外部模型API、无账号后端、无后台自动研究。当前助手承担研究工作；页面展示已审阅公开快照。

`landscape.json`是原四象限快照；`SYNTHETIC_DEEPDIVE.md`是本轮研究源文件；`synthetic-evidence.json`是公开阅读台账。`synthetic-report.html`由Markdown生成，用于浏览器展示。重新生成需`pip install markdown`后运行`python scripts/build_synthetic.py`，公开checkout可使用已有台账中的来源哈希，不需要私有PDF。

`python scripts/refresh_landscape.py`只更新待审文件，遇限流停止；`python scripts/build_landscape.py`生成原四象限报告和融资CSV，不替代本轮深研。原统计窗口2025-10-01至2026-09-30，本轮补充历史论文不计入该窗口热度。会议/访谈覆盖不对称，尚未纳入技术分数。

## 检查

```sh
python scripts/test_landscape.py
node scripts/test_landscape.js
node scripts/test_synthetic.js
node --check synthetic.js
python scripts/test_browser.py
```

浏览器测试需Playwright和本机Edge；默认localhost:8000，可用`FR_DEMO_URL`覆盖。检查论文台账、计算器零值/无效输入/地域切换、下载、四象限与移动端。源码MIT；第三方论文和商业报告版权归原作者，本仓库仅发布原创分析与链接。
