'use strict';
// Deliberately no invented empirical scores: sample coordinates are opt-in.
const radarTopics = [
 ['foundation','基础模型训练','模型','通用预训练与基础模型开发；不包括推理服务'],
 ['inference','推理优化','算力','推理运行时、压缩与调度；不包括基础芯片融资'],
 ['memory','Agent 记忆','Agent','持久记忆、检索与状态管理'],
 ['evaluation','模型评测与审计','工具','模型评估、在线质检与人工审计路由'],
 ['identity','Agent 身份与授权','工具','身份、权限与执行治理；包括撤销完成证明'],
 ['synthetic','合成数据','数据','用于训练与验证的数据生成和质量控制'],
 ['science','科学实验自动化','应用','实验编排、测量分析与异常处理'],
 ['embodied','机器人基础模型','模型','面向机器人感知、规划与控制的模型']
];
// Synthetic fixture only, not estimates of the named markets.
const radarFixture = [[88,89,94,92],[68,78,81,87],[35,66,56,79],[25,72,43,85],[24,46,38,74],[48,59,62,76],[30,39,49,63],[79,83,87,89]];
let radarSelected='evaluation';
function radarInit(){
 const host=document.querySelector('#landscape');
 host.innerHTML=`<div class="section-top"><div><p class="eyebrow">CHINA × GLOBAL / SAME TAXONOMY</p><h2>同一方向，两张技术—资本地图</h2></div><span class="pill">口径草案 v0.3 · 2026.10.25</span></div>
 <p>先看全景，再进入技术活跃、资本关注较低的候选区。中国与全球使用相同领域分类和时间窗口；全球包含中国，不是“中国以外”。</p>
 <div class="radar-controls"><label>选择同一方向 <select id="radar-topic">${radarTopics.map(t=>`<option value="${t[0]}">${t[1]}</option>`).join('')}</select></label><label>数据模式 <select id="radar-mode"><option value="evidence">真实证据 · 尚不具备排名条件</option><option value="sample">交互演示 · 全部坐标为虚构样例</option></select></label></div>
 <div id="radar-notice" class="warning" role="status"></div><div class="radar-pair"><div><h3>中国</h3><div id="radar-cn"></div></div><div><h3>全球（含中国）</h3><div id="radar-world"></div></div></div>
 <div class="panel" id="radar-comparison"></div>
 <details open><summary>统计与可比性规则</summary><div class="two"><div class="panel"><h3>相同窗口、相同分类</h3><p>拟统计窗口：2025-10-01 至 2026-09-30，按月更新。技术事件以首次公开日期，融资以首次可核验公告日期计入。跨期更新不重复算新增事件。</p><p>中国技术信号以主要贡献机构位于中国大陆为口径；跨国合作按参与机构国家分数计数。中国融资按获投企业主要经营实体位于中国大陆，不按投资人国籍。港澳台另设地域标签，纳入全球。</p><p>分类以技术活动与公司主营用途人工核验。同一融资事件设唯一ID，跨方向分配权重合计为1；无法拆分则保留“多方向未分配”，不重复归集。</p></div><div class="panel"><h3>两地定位，比较当地相对位置</h3><p>两张图分别在同一组领域内计算百分位，50分为相对中位边界。70分代表当地样本中的相对位置，不代表中国与全球的绝对金额相同。</p><p>联动详情同时展示原始论文/机构数、融资金额/事件数、披露率和样本量，避免把百分位差当绝对规模差。全球含中国，两图不是独立样本。</p><p>先覆盖完整候选领域再排名。未采集、未披露和确认为零分开记录；任一核心指标缺失则不落点。已观测的零融资也不自动等于没有资本关注。</p></div></div></details>
 <details><summary>轴如何计算：可审阅的初版方案</summary><div class="two"><div class="panel"><h3>纵轴 · 技术活跃度</h3><p>40% 论文与独立团队 + 30% 研讨会/技术报告 + 30% 业界访谈/讨论。每类先去重，计独立事件与独立参与机构，再转成当地领域集合中的百分位；各子项等权。权重为待验证设定，不是科学常数。</p><p>只纳入实质技术内容。转载、同一报告重复演讲、论文版本合并；机构自有宣传与独立讨论分开标注。部署与实际采用另列，不将讨论热度称为成熟度。</p></div><div class="panel"><h3>横轴 · 资本关注度</h3><p>60% 已披露股权融资总额 + 20% 融资事件数 + 20% 独立获投企业数，各自计算当地百分位再加权。排除债务、补贴、并购和二级市场市值，单独列示。</p><p>融资按公告日汇率折算美元，同时保留原币及汇率来源。估值另列投前/投后中位数与样本数，不相加，也不混用；披露不足不能据此给低分。展示最大一笔融资占比。</p><p>对权重变化±10个百分点及去除最大融资事件进行敏感性检查；象限不稳定的方向进入待核验，不直接列为优先投资。</p></div></div></details>
 <h3>数据覆盖与候选目录</h3><p>目前只有局部论文研究与待研材料，尚无按上述窗口完成的两地全量技术事件和融资登记簿。下列方向均未达到可比较条件；原来三个深研案例归入对应的父级领域，不预先判定属于左上象限。</p><div class="radar-table-wrap"><table class="radar-table"><thead><tr><th>领域</th><th>分类边界</th><th>中国</th><th>全球</th></tr></thead><tbody>${radarTopics.map(t=>`<tr><td>${t[1]}</td><td>${t[3]}</td><td>待补数据</td><td>待补数据</td></tr>`).join('')}</tbody></table></div>`;
 document.querySelector('#radar-topic').value=radarSelected;
 document.querySelector('#radar-topic').onchange=e=>{radarSelected=e.target.value;radarRender();};
 document.querySelector('#radar-mode').onchange=radarRender;
 radarRender();
}
function radarRender(){
 const demo=document.querySelector('#radar-mode').value==='sample';
 document.querySelector('#radar-notice').textContent=demo?'虚构样例模式：仅演示双图联动。所有方向坐标均为测试数据，不代表实际融资、技术热度或投资机会。':'真实证据模式：两地指标尚未完成采集，暂不绘制方向坐标。空白表示未知，不是零；不能据此筛选投资象限。';
 for(const [region,offset] of [['cn',0],['world',2]]){
  const points=demo?radarTopics.map((t,i)=>{const x=70+radarFixture[i][offset]*3.5,y=350-radarFixture[i][offset+1]*2.8;return `<g class="radar-point ${t[0]===radarSelected?'chosen':''}" data-topic="${t[0]}" role="button" tabindex="0" aria-label="${t[1]}，虚构样例"><circle cx="${x}" cy="${y}" r="${t[0]===radarSelected?9:6}"/><text x="${x-8}" y="${y-13}" text-anchor="end">${t[1]}</text></g>`;}).join(''):'';
  document.querySelector('#radar-'+region).innerHTML=`<svg class="radar-svg" viewBox="0 0 480 420" role="group" aria-label="${region==='cn'?'中国':'全球'}四象限${demo?'，虚构样例':'，待补数据'}"><rect x="70" y="70" width="175" height="140" fill="#dfecd6"/><rect x="245" y="70" width="175" height="140" fill="#e6eae4"/><rect x="70" y="210" width="175" height="140" fill="#f2f0e6"/><rect x="245" y="210" width="175" height="140" fill="#f5e9da"/><path d="M70 70V350H420 M245 70V350 M70 210H420" fill="none" stroke="#8a9a8a"/><g class="quadrant-label"><text x="82" y="93">重点发现区</text><text x="257" y="93">共识竞争区</text><text x="82" y="332">早期观察区</text><text x="257" y="332">预期先行区</text></g><g class="axis-label"><text x="65" y="375">0</text><text x="237" y="375">50</text><text x="405" y="375">100</text><text x="32" y="355">0</text><text x="27" y="215">50</text><text x="20" y="75">100</text><text x="160" y="405">资本关注度 →</text><text x="72" y="40">技术活跃度 ↑</text></g>${!demo?'<text x="245" y="190" text-anchor="middle" fill="#596b59">数据未齐，不落点</text>':points}</svg>`;
 }
 document.querySelectorAll('.radar-point').forEach(p=>{const choose=()=>{radarSelected=p.dataset.topic;document.querySelector('#radar-topic').value=radarSelected;radarRender();};p.onclick=choose;p.onkeydown=e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();choose();}};});
 const index=radarTopics.findIndex(t=>t[0]===radarSelected),topic=radarTopics[index];
 document.querySelector('#radar-comparison').innerHTML=`<h3>联动比较 · ${topic[1]}</h3><p>${topic[3]}</p><div class="two"><div><strong>中国</strong><p>${demo?'样例资本分 '+radarFixture[index][0]+' / 技术分 '+radarFixture[index][1]:'技术分：未知 · 资本分：未知'}</p></div><div><strong>全球（含中国）</strong><p>${demo?'样例资本分 '+radarFixture[index][2]+' / 技术分 '+radarFixture[index][3]:'技术分：未知 · 资本分：未知'}</p></div></div><p class="muted">真实原始指标：论文与独立机构数、技术讨论次数、融资总额、融资事件数、估值中位数与披露率均待按统一窗口核验。${demo?'不要依据样例分数做投资判断。':'当前不能断言该方向在中国或全球属于哪个象限。'}</p>`;
}
radarInit();
