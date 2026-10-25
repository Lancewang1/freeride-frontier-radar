'use strict';
(function(root){
 function percentile(v,vs){if(v===null||!vs.length)return null;return 100*(vs.filter(x=>x<v).length+(vs.filter(x=>x===v).length-1)/2)/Math.max(1,vs.length-1);}
 function metrics(data,region,drop=false,strict=false){
  const rows=data.topics.map(t=>{
   const paper=data.papers.find(p=>p.topic===t.id&&p.region===region);
   const events=data.funding.filter(e=>e.topic===t.id&&e.status==='completed'&&(region==='global'||e.country==='CN'));
   let measured=events.filter(e=>e.usd_m!==null&&(!strict||e.amount_kind==='exact'));
   if(drop&&measured.length){const largest=measured.reduce((a,b)=>a.usd_m>=b.usd_m?a:b);measured=measured.filter(e=>e.id!==largest.id);}
   const amount=measured.length?measured.reduce((a,e)=>a+e.usd_m,0):null;
   const latest=new Map();for(const e of events.filter(e=>e.valuation!==null&&e.valuation_type==='post-money'&&e.currency==='USD').sort((a,b)=>a.date.localeCompare(b.date)))latest.set(e.company,e.valuation);
   const vals=[...latest.values()].sort((a,b)=>a-b),n=vals.length;
   return {...t,paper,paperCount:paper?.count??null,validTech:t.id!=='foundation'&&paper?.count!==undefined,events,measured,amount,companies:new Set(events.map(e=>e.company)).size,valuation:n?(vals[Math.floor((n-1)/2)]+vals[Math.floor(n/2)])/2:null,valuationN:n,largestShare:amount?100*Math.max(...measured.map(e=>e.usd_m))/amount:null,hasNonExact:measured.some(e=>e.amount_kind!=='exact'),disclosure:events.length?events.filter(e=>e.usd_m!==null).length/events.length:null};
  });
  const tech=rows.filter(r=>r.validTech).map(r=>r.paperCount),money=rows.filter(r=>r.amount!==null).map(r=>r.amount),counts=rows.filter(r=>r.events.length).map(r=>r.events.length);
  return rows.map(r=>({...r,y:r.validTech?percentile(r.paperCount,tech):null,x:percentile(r.amount,money),countX:r.events.length?percentile(r.events.length,counts):null,techN:tech.length,moneyN:money.length,countN:counts.length}));
 }
 function quadrant(x,y){if(x===null||y===null)return '待补证据';return x<50?(y>=50?'技术高 / 样本资本低':'技术低 / 样本资本低'):(y>=50?'技术高 / 样本资本高':'技术低 / 样本资本高');}
 const api={percentile,metrics,quadrant};if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.RadarCore=api;
})(typeof globalThis!=='undefined'?globalThis:this);
