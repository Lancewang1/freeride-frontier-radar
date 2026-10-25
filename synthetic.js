'use strict';
const se=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const presets={cn:[[200,30000,25,10,10],[600,80000,40,15,30],[1200,150000,50,20,60]],global:[[1000,50000,25,10,20],[3000,120000,40,15,60],[6000,200000,50,20,120]]};
function marketCalc(x){
 const {accounts,price,qualified,share,capacity,volumeGrowth,priceGrowth}=x;
 const tam=accounts*price,sam=tam*qualified/100,customers=Math.min(accounts*qualified/100*share/100,capacity),som=customers*price;
 const factor=(1+volumeGrowth/100)*(1+priceGrowth/100);
 return {tam,sam,customers,som,fiveYearPool:tam*factor**5,impliedCagr:(factor-1)*100};
}
if(typeof module!=='undefined')module.exports={marketCalc};
if(typeof document!=='undefined'){
 const fields=['accounts','price','qualified','share','capacity','volumeGrowth','priceGrowth'];
 function inputs(){return Object.fromEntries(fields.map(id=>[id,Number(document.getElementById(id).value)]));}
 function calculate(){
  if(fields.some(id=>{const e=document.getElementById(id);return e.value===''||!e.checkValidity();})){document.querySelector('#market-results').textContent='请输入范围内的有效数值。';return;}
  const r=marketCalc(inputs()),money=n=>(n/1e6).toLocaleString('zh-CN',{maximumFractionDigits:3})+' 百万美元';
  document.querySelector('#market-results').innerHTML=[['理论 TAM',money(r.tam)],['可服务 SAM',money(r.sam)],['第3年 SOM 年收入',money(r.som)],['第3年可交付账户',r.customers.toLocaleString('zh-CN',{maximumFractionDigits:1})],['五年后理论收入池',money(r.fiveYearPool)],['假设隐含 CAGR',r.impliedCagr.toFixed(2)+'%']].map(([a,b])=>`<div class="metric"><small>${a}</small><strong>${b}</strong><small>情景假设 · 非市场事实</small></div>`).join('');
 }
 function preset(){presets[document.querySelector('#market-region').value][Number(document.querySelector('#market-scenario').value)].forEach((v,i)=>document.getElementById(fields[i]).value=v);calculate();}
 document.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>{document.getElementById(b.dataset.view).scrollIntoView({behavior:'instant',block:'start'});document.querySelectorAll('[data-view]').forEach(x=>x.classList.toggle('active',x===b));});
 document.querySelectorAll('#market-model input').forEach(x=>x.oninput=calculate);
 document.querySelector('#market-region').onchange=preset;document.querySelector('#market-scenario').onchange=preset;
 document.querySelector('#export-market').onclick=()=>{if(fields.some(id=>!document.getElementById(id).checkValidity()||document.getElementById(id).value===''))return;const u=URL.createObjectURL(new Blob([JSON.stringify({status:'analyst_assumptions_not_market_facts',region:document.querySelector('#market-region').value,inputs:inputs(),outputs:marketCalc(inputs())},null,2)],{type:'application/json'}));const a=document.createElement('a');a.href=u;a.download='synthetic-market-scenario.json';a.click();setTimeout(()=>URL.revokeObjectURL(u),1000);};
 preset();
 Promise.all([fetch('synthetic-report.html').then(r=>{if(!r.ok)throw Error('报告加载失败');return r.text();}),fetch('synthetic-evidence.json').then(r=>{if(!r.ok)throw Error('台账加载失败');return r.json();})]).then(([html,e])=>{
  document.querySelector('#deep-report').innerHTML=html;
  const heads=[...document.querySelectorAll('#deep-report h2')];document.querySelector('#report-index').innerHTML=heads.map(h=>`<a href="#${h.id}">${se(h.textContent)}</a>`).join('');
  document.querySelector('#reading-summary').textContent=`原有40条地域记录 → ${e.unique_records}篇去重记录完成标题归类；8篇核心章节研究，其中2篇来自原名单、6篇补充；0篇独立复现。`;
  document.querySelector('#reading-ledger').innerHTML=e.reviewed_papers.map(p=>`<details class="source"><summary>${se(p.id)} · ${se(p.title)}</summary><p>${se(p.status)} · ${se(p.origin)}</p><p>关键定位：PDF ${se(p.locators)}；${se(p.supplement)}</p><a href="${se(p.url)}" target="_blank" rel="noopener">论文原文 ↗</a><div class="hash">SHA256 ${se(p.sha256)}</div></details>`).join('');
  const render=()=>{const q=document.querySelector('#paper-query').value.toLowerCase();document.querySelector('#paper-audit').innerHTML=e.triage.filter(r=>(r.title+r.category+r.status).toLowerCase().includes(q)).map(r=>`<div class="source"><span class="pill">${se(r.category)}</span><p><a href="${se(r.url)}" target="_blank" rel="noopener">${se(r.title)}</a></p><p>${se(r.status)}</p><small>${se(r.regions.join(' / '))} · ${se(r.relevance)}</small></div>`).join('');};document.querySelector('#paper-query').oninput=render;render();
 }).catch(e=>document.querySelector('#deep-report').textContent=e.message);
}
