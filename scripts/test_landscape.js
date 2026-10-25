const assert=require('node:assert/strict');
const d=require('../landscape.json');
const {percentile,metrics,quadrant}=require('../radar-core.js');
const globalRows=metrics(d,'global'),cnRows=metrics(d,'cn');
const row=(rows,id)=>rows.find(r=>r.id===id);
assert.equal(percentile(null,[1,2]),null);
assert.equal(percentile(2,[1,2,2,4]),50);
assert.equal(quadrant(null,80),'待补证据');
assert.equal(row(globalRows,'foundation').amount,97000);
assert.equal(row(globalRows,'foundation').valuation,965000); // latest per company
assert.equal(row(globalRows,'foundation').valuationN,1);
assert.equal(row(globalRows,'foundation').y,null); // failed search excluded
assert.equal(row(cnRows,'evaluation').amount,null); // talks are not completed
assert.equal(row(cnRows,'evaluation').countX,null); // missing is not zero
assert.equal(row(cnRows,'memory').amount,null); // coarse is not a number
assert.equal(row(cnRows,'memory').events.length,1);
assert.equal(row(globalRows,'memory').amount,20); // not headline 24M
assert.equal(row(globalRows,'evaluation').amount,200);
assert.equal(row(globalRows,'embodied').amount,740);
assert.equal(row(globalRows,'inference').measured.some(e=>e.id==='fireworks-c'),false);
assert.equal(row(metrics(d,'global',true),'synthetic').amount,null);
assert.equal(row(metrics(d,'global',false,true),'science').amount,null);
assert.equal(row(metrics(d,'global',false,true),'inference').amount,1505);
assert.equal(row(metrics(d,'global',true),'inference').events.length,row(globalRows,'inference').events.length);
for(const r of cnRows){const g=row(globalRows,r.id);assert.ok(g.events.length>=r.events.length);if(r.amount!==null)assert.ok(g.amount>=r.amount);}
console.log('PASS: 19+ scoring, missingness, dedup, valuation, classification and sensitivity assertions');
