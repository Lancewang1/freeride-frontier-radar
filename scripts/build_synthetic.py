"""Build the public reading ledger and HTML from reviewed notes; no network calls."""
from pathlib import Path
import json, re, markdown
ROOT=Path(__file__).resolve().parents[1]
PRIVATE=ROOT.parent/'tmp'/'synthetic-deep'
existing=json.loads((ROOT/'synthetic-evidence.json').read_text(encoding='utf8')) if (ROOT/'synthetic-evidence.json').exists() else None
raw=json.loads((ROOT/'landscape.json').read_text(encoding='utf8'))
records={}
for q in raw['papers']:
    if q['topic']!='synthetic':continue
    for r in q['records']:
        key=r['url'].lower()
        if key not in records:records[key]={**r,'regions':[]}
        records[key]['regions'].append(q['region'])
def category(title):
    t=title.lower()
    if any(x in t for x in ['tumor','medical','health','cognitive','eeg','biomedical','cancer','clinical','breast','delirium']):return '医疗与健康'
    if any(x in t for x in ['facial','face image']):return '人脸与表情'
    if any(x in t for x in ['robot perception']):return '机器人感知'
    if any(x in t for x in ['finance','tabular']):return '结构化/金融数据'
    if 'synthetic trust' in t:return '评论与治理'
    return '工业、科学与其他视觉应用'
for r in records.values():
    r['category']=category(r['title'])
    r['status']='标题级归类；未精读，不据此提取效果'
    r['relevance']='属于广义合成数据；不自动属于可外购的AI训练数据产品市场'
    if r['title'].startswith(('SynFER','Scaling Tumor')):r['status']='已核读全文中的方法、实验与结论；未复现'
    if r['category'] in ['评论与治理']:r['relevance']='不能作为算法性能或商业采用证据'
ids=['self-instruct','textbooks','collapse','accumulate','domain-randomization','mimicgen','synfer','tumor']
titles=['Self-Instruct','Textbooks Are All You Need','The Curse of Recursion: Training on Generated Data Makes Models Forget','Is Model Collapse Inevitable?','Domain Randomization','MimicGen','SynFER','Scaling Tumor Segmentation']
pages=['3–5, 8','4–7, 11–14','3–5, 10–12','3–7, §3','4–6','3–8','4–8','3–4, 7–8']
papers=[]
for i,(k,title,locator) in enumerate(zip(ids,titles,pages),1):
    meta=json.loads((PRIVATE/(k+'.json')).read_text(encoding='utf8')) if PRIVATE.exists() else existing['reviewed_papers'][i-1]
    papers.append({'id':f'P{i}','title':title,'url':meta['url'],'sha256':meta['sha256'],'locators':locator,'status':'全文核心章节核读，未独立复现','supplement':'未逐项核查所有补充材料与证明','origin':'原有检索名单' if i>=7 else '本轮补充机制/反证；不计入热度窗口'})
sources=[]
for k in ['market-gvr','market-mam','china-market','nvidia','mostly','tonic','lightwheel']:
    meta=json.loads((PRIVATE/(k+'.json')).read_text(encoding='utf8')) if PRIVATE.exists() else next(x for x in existing['commercial_sources'] if x['id']==k)
    sources.append({'id':k,**meta,'status':'公开网页已读；不是付费报告或独立产品验收'})
ledger={'as_of':'2026-10-25','raw_regional_records':40,'unique_records':len(records),'reviewed_papers':papers,'triage':list(records.values()),'commercial_sources':sources,'reproduction_count':0}
(ROOT/'synthetic-evidence.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2),encoding='utf8')
report=(ROOT/'SYNTHETIC_DEEPDIVE.md').read_text(encoding='utf8')
html=markdown.markdown(report,extensions=['tables','toc'])
(ROOT/'synthetic-report.html').write_text(html,encoding='utf8')
brief=(ROOT/'CLIENT_BRIEF.md').read_text(encoding='utf8')
(ROOT/'client-brief.html').write_text(markdown.markdown(brief,extensions=['tables','toc']),encoding='utf8')
print(f'{len(records)} unique triaged records, {len(papers)} core fulltext reviews, 0 reproductions')
