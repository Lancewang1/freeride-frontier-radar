const assert=require('node:assert/strict');
const {marketCalc}=require('../synthetic.js');
const base={accounts:600,price:80000,qualified:40,share:15,capacity:30,volumeGrowth:15,priceGrowth:-5};
let r=marketCalc(base);assert.equal(r.tam,48000000);assert.equal(r.sam,19200000);assert.equal(r.som,2400000);assert.equal(r.customers,30);assert.ok(Math.abs(r.impliedCagr-9.25)<1e-9);
r=marketCalc({...base,capacity:100});assert.equal(r.customers,36);assert.equal(r.som,2880000);
r=marketCalc({...base,qualified:0});assert.equal(r.sam,0);assert.equal(r.som,0);
r=marketCalc({...base,volumeGrowth:0,priceGrowth:0});assert.equal(r.fiveYearPool,r.tam);assert.equal(r.impliedCagr,0);
r=marketCalc({...base,volumeGrowth:10,priceGrowth:-20});assert.ok(r.impliedCagr<0);assert.ok(r.fiveYearPool<r.tam);
console.log('PASS: units, capacity cap, zero demand, flat growth, price erosion and CAGR composition');
