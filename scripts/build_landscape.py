"""Validate and export the reviewed snapshot; no inferred financial facts."""
import csv
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]


def main():
    d=json.loads((ROOT/'landscape.json').read_text(encoding='utf-8'))
    names={t['id']:t['name'] for t in d['topics']}
    fields=['id','company','topic','country','date','amount','currency','amount_kind','usd_m','status','valuation','valuation_type','url','note']
    with (ROOT/'funding-ledger.csv').open('w',encoding='utf-8-sig',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');writer.writeheader();writer.writerows(d['funding'])
    out=['# FREERIDE 中国与全球技术—资本地图','公开证据版 v0.4 · 2026-10-25','统计窗口：2025-10-01 至 2026-09-30。全球包含中国。',
         '## 结论先行',
         '本轮完成了可复现的公开样本版地图，而不是全市场普查。8个领域、16组论文检索、22条融资/观察记录、12项会议或技术讨论旁证。没有证据证明任何方向已是低拥挤的确定投资机会。',
         '1. 合成数据在当前中外金额样本图均进入技术高/样本资本低区域。但可计量融资集中于光轮智能的单笔合并公告，剔除最大一笔后无可计金额，因此只能列为第一补证候选，不能视为稳定发现。应继续拆分合成文本、仿真数据和评测反馈，避免异质性混在一起。',
         '2. 推理服务中外都有大额融资。硅基流动超20亿元人民币B轮，Fireworks 15.05亿美元D轮。该方向已有资本跟进，新增投资需寻找技术路线或单位经济性差异，而不是泛赛道叙事。',
         '3. 评测并非无人投资：LMArena 1.5亿美元A轮、Patronus 5000万美元B轮；中国UniPat拟3亿美元的交易在读到的正文中仍处于谈判。不能把拟融资记作完成，也不能把没有已完成样本误解成低关注。',
         '4. Agent记忆在中国已有亿元级融资报道，全球有Mem0 A轮；身份授权有Hush与Cymphony。窄切口仍可研究，但本轮未显示它们具备“技术高普及、资本低关注”的稳健证据。',
         '5. 自主实验室存在Lila扩募及中国融资事件。此前仪器异常处理案例有研究价值，但不能据此推断整个实验室方向属于目标象限。',
         '## 下一轮验证工作包',
         '- 优先A：合成数据的质量验证与结果反馈。先补充海外融资及中国模糊金额，拆分仿真与文本数据；验证合成数据能否提升真实留出任务，控制泄漏、分布偏移和同质化。访谈模型训练团队，拿到训练预算、数据采购和可复现实验。若增益只发生在相似基准或大平台可免费覆盖，停止独立产品判断。',
         '- 优先B：业务结果驱动的在线审计。属于评测方向内部切口，不把母赛道称为冷门。用独立标签、随机抽查基线和全成本衡量质量与人工节约。具体30天方案见历史研究案例。',
         '- 观察C：可治理长期记忆与跨网关权限。分别检验冲突记忆更新、遗忘和迁移，以及撤销后的实际效果观察。现有平台融资和内置功能是替代风险；先找企业愿付费的失败案例，而非先写大市场故事。',
         '## 统计方法',
         '技术轴：同一地区的7个有效领域OpenAlex检索命中量百分位。基础模型检索出现误匹配，保留原始记录但不参与技术排序、不落点。技术轴不是完整的论文+会议+访谈综合指标，也不是采用率。',
         '资本轴：可计量且已完成报道的融资金额样本百分位；可切换为已核验公告事件数。合并公告计1事件，金额以百万原币与美元表示。每笔按公司主标签归类一次，不能理解为全部资金用于该技术。',
         '百分位公式：100 × [比该值小的领域数 + (同值领域数−1)/2] ÷ (有效领域数−1)。未知不入分母。两地金额有效领域分母不同，图中明确显示；排名只在样本中有意义。',
         '敏感性：可只用精确披露金额，或剔除每方向最大一笔。剔除后无可计金额时保留未知，而非0。估值只用每家企业最近一次明确投后美元估值求中位数，样本量同步展示，投前/未说明及洽谈估值不参与。',
         '## 原始指标对照',
         '|领域|中国论文命中|全球论文命中|中国可计金额 USD m|全球可计金额 USD m|中国公告数|全球公告数|',
         '|---|---:|---:|---:|---:|---:|---:|']
    for t in d['topics']:
        p={r['region']:r['count'] for r in d['papers'] if r['topic']==t['id']}
        es=[e for e in d['funding'] if e['topic']==t['id'] and e['status']=='completed'];cn=[e for e in es if e['country']=='CN']
        def total(rows):
            vs=[e['usd_m'] for e in rows if e['usd_m'] is not None]
            return f'{sum(vs):,.2f}' if vs else '未知'
        out.append(f"|{t['name']}|{p['cn']}|{p['global']}|{total(cn)}|{total(es)}|{len(cn)}|{len(es)}|")
    out+=['金额为已收录可计量部分，含约数/明确下界/推导增量，不是精确行业总额。数量级披露不强行数值化。基础模型论文命中不合格，仅展示用于审计。','## 对原始新闻做了哪些修正',
          '- Mem0标题2400万美元包含种子轮与A轮，本期计A轮2000万美元。',
          '- Fireworks C轮含primary/secondary混合，无法拆分则排除；D轮按公告15.05亿美元。',
          '- Lila A轮最终350百万美元中，235百万美元首关在2025年9月，本期仅计115百万美元增量；官网不同页面有10月10日/15日差异，均在窗口内。',
          '- 光轮智能A++及A+++合并公告10亿元，不重复计两笔；MemTensor亿元级、戴纳近亿元等保留模糊状态。',
          '- 瑞莱智慧为泛AI安全相邻供给，不把其全部融资归入Agent身份授权；UniPat谈判交易不计入完成统计。',
          '## 融资事件证据']
    for e in d['funding']:
        out += [f"### {e['company']} · {e['date']} · {e['status']}",f"方向：{names[e['topic']]}；地域：{e['country']}；金额：{e['amount'] if e['amount'] is not None else '数量级/未知'} 百万 {e['currency']}；口径：{e['amount_kind']}。",e['note'],f"> {e['quote']}",f"[原文]({e['url']})；SHA256 `{e['source_hash']}`"]
        if e.get('support_url'):out.append(f"[首关交叉核验]({e['support_url']})")
    out+=['## 论文检索登记']
    for p in d['papers']:out += [f"- {names[p['topic']]} / {p['region']} / {p['count']}：`{p['query']}`；[API]({p['url']})；{p['quality']}。"]
    out+=['## 会议与技术讨论旁证','NeurIPS 2025官方列表包含56个独立workshop，本次阅读8个详情。另记录4项中国企业技术讨论/访谈，与融资报道同文者不当独立来源，也不进入评分。']
    out += [f"- [{s['title']}]({s['url']})：{s['date']}；{s['scope']}。" for s in d.get('discussions',[])]
    out+=['## 限制与下一步']+['- '+s for s in d['limitations']]
    out+=['本轮OpenAlex额外检索遇到429限流，因此未继续重试或将缺失返回写作零。Wind返回余额不足，本报告使用用户指定的公开融资新闻；不冒充付费数据库结果。','要从本版升级为投资级排名，需要完整领域词表、均衡多源融资检索、人工实体去重、机构国家补全、季度重复快照，以及由预算负责人验证的买方需求。市场容量/CAGR/CR5不能从融资金额推导。']
    (ROOT/'LANDSCAPE_REPORT.md').write_text('\n\n'.join(out),encoding='utf-8')
    print(f"Exported {len(d['funding'])} event records and research report")


if __name__=='__main__':main()
