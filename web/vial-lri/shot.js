const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1080,height:1350}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(['error','warning'].includes(m.type()))errs.push(m.text())});
const q=process.argv[2]||'label=A';const out=process.argv[3]||'still.png';
const t0=Date.now();await p.goto('file://'+process.cwd()+'/vial.html?'+q);await p.waitForFunction('window.ready===true',null,{timeout:120000});
await p.screenshot({path:out});console.log('ms',Date.now()-t0,errs.slice(0,4));await b.close()})();
