(function(){
'use strict';
var root=document.documentElement;
var RM=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
var FINE=window.matchMedia('(pointer:fine)').matches;
function $(s,c){return (c||document).querySelector(s)}
function $$(s,c){return Array.prototype.slice.call((c||document).querySelectorAll(s))}
function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
function lerp(a,b,t){return a+(b-a)*t}
function sget(k){try{return localStorage.getItem(k)}catch(e){return null}}
function sset(k,v){try{localStorage.setItem(k,v)}catch(e){}}

/* ---------- language ---------- */
function setLang(l){
  root.setAttribute('data-lang',l); root.lang=l; sset('lci-lang',l);
  $$('[data-setlang]').forEach(function(b){b.setAttribute('aria-pressed',String(b.getAttribute('data-setlang')===l))});
  if(window.fitHeroes)setTimeout(window.fitHeroes,30);
}
document.addEventListener('click',function(e){
  var b=e.target.closest('[data-setlang]'); if(b){setLang(b.getAttribute('data-setlang'));return}
  b=e.target.closest('[data-group] > button'); if(b&&!b.disabled){
    $$('button',b.parentNode).forEach(function(x){x.setAttribute('aria-pressed','false')}); b.setAttribute('aria-pressed','true');return}
  b=e.target.closest('[data-rail]'); if(b){var r=$('.rail');r.scrollBy({left:(b.getAttribute('data-rail')==='next'?1:-1)*Math.min(520,r.clientWidth*.8),behavior:RM?'auto':'smooth'});return}
  if(e.target.closest('.burger')){toggleMenu();return}
  if(e.target.closest('.mclose')){toggleMenu(false);return}
  if(e.target.closest('.mnav a')){toggleMenu(false)}
});
setLang(sget('lci-lang')==='en'?'en':'es');

var menu=$('.mnav');
function toggleMenu(f){
  var open=f===undefined?!menu.classList.contains('open'):f;
  menu.classList.toggle('open',open); document.body.style.overflow=open?'hidden':'';
  var bg=$('.burger'); if(bg) bg.setAttribute('aria-expanded',String(open));
}


/* ---------- entrada del logo ---------- */
(function(){
  var intro=$('#intro'); if(!intro) return;
  function done(){root.classList.remove('js-intro');intro.style.display='none';document.body.style.overflow=''}
  if(RM||!root.classList.contains('js-intro')){done();return}
  var il=$('#il'),iw=$('#iw'),ish=$('.ish',intro),irl=$('.irl',intro),ibg=$('.ibg',intro),target=$('.top .logo');
  if(!il.animate||!target){done();return}
  var E='cubic-bezier(.2,.7,.1,1)';
  il.animate([{clipPath:'inset(0 100% 0 0)',filter:'blur(14px)',opacity:0,transform:'scale(1.07)'},{clipPath:'inset(0 0% 0 0)',filter:'blur(0px)',opacity:1,transform:'scale(1)'}],{duration:1500,delay:400,easing:E,fill:'forwards'});
  irl.animate([{opacity:0,transform:'scaleX(0)'},{opacity:1,transform:'scaleX(1)'}],{duration:1100,delay:1500,easing:E,fill:'forwards'});
  ish.animate([{opacity:1,backgroundPosition:'130% 0'},{opacity:1,backgroundPosition:'-30% 0'}],{duration:1200,delay:1900,easing:'ease-in-out',fill:'forwards'});
  setTimeout(function(){
    var a=il.getBoundingClientRect(),b=target.getBoundingClientRect();
    var s=b.width/a.width,dx=b.left-a.left,dy=b.top-a.top;
    irl.animate([{opacity:1},{opacity:0}],{duration:400,fill:'forwards'});
    iw.animate([{transform:'translate(0,0) scale(1)'},{transform:'translate('+dx+'px,'+dy+'px) scale('+s+')'}],{duration:1150,easing:'cubic-bezier(.65,0,.35,1)',fill:'forwards'});
    ibg.animate([{opacity:1},{opacity:0}],{duration:950,delay:250,easing:'ease-out',fill:'forwards'});
    setTimeout(done,1180);
  },3350);
})();

/* ---------- split words (hero + headings) ---------- */
function split(el){
  var i=0,last=null;
  (function walk(n){
    Array.prototype.slice.call(n.childNodes).forEach(function(c){
      if(c.nodeType===3){
        var f=document.createDocumentFragment();
        c.nodeValue.split(/(\s+)/).forEach(function(p){
          if(!p) return;
          if(/^\s+$/.test(p)){f.appendChild(document.createTextNode(' '));return}
          if(/^[.,;:!?]+$/.test(p)&&last){last.textContent+=p;return}
          var w=document.createElement('span'); w.className='w';
          var s=document.createElement('i'); s.textContent=p; s.style.setProperty('--i',i++);
          w.appendChild(s); f.appendChild(w); last=s;
        });
        n.replaceChild(f,c);
      } else if(c.nodeType===1 && c.tagName!=='BR') walk(c);
    });
  })(el);
}
if(!RM) $$('.hero .split > span').forEach(split);


/* ---------- titular: "saludables" con el mismo ancho que la línea de abajo ---------- */
function fitHeroes(){
  $$('.hero h1, .hk').forEach(function(h){
    var el=Array.prototype.slice.call(h.children).filter(function(c){return getComputedStyle(c).display!=='none'})[0]; if(!el) return;
    var k1=el.querySelector('.k1'),k2=el.querySelector('.k2'),k3=el.querySelector('.k3'); if(!k2||!k3) return;
    var host=h.parentElement,cs=getComputedStyle(host),avail=host.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight);
    [k1,k2,k3].forEach(function(k){if(k){k.style.display='inline-block';k.style.whiteSpace='nowrap';k.style.alignSelf='flex-start'}});
    k3.style.fontSize='';var s3=parseFloat(getComputedStyle(k3).fontSize),w3=k3.getBoundingClientRect().width;
    var lim=Math.min(avail,window.innerWidth*(window.innerWidth<1000?.9:.62));
    if(w3>lim){s3=s3*lim/w3;k3.style.fontSize=s3+'px';w3=k3.getBoundingClientRect().width}
    if(k1)k1.style.fontSize=s3+'px';
    k2.style.fontSize='200px';var w2=k2.getBoundingClientRect().width;
    k2.style.fontSize=(200*w3/w2)+'px';
  });
}
window.fitHeroes=fitHeroes;
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fitHeroes);
window.addEventListener('resize',function(){clearTimeout(window.__fh);window.__fh=setTimeout(fitHeroes,60)});
setTimeout(fitHeroes,300);setTimeout(fitHeroes,1500);

/* ---------- reveal ---------- */
var rvIO=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in-v');rvIO.unobserve(e.target)}})},{threshold:.12});
$$('.rv').forEach(function(el){rvIO.observe(el)});

/* ---------- cursor + magnetic ---------- */
var tx=0,ty=0,mx=0,my=0;
window.addEventListener('pointermove',function(e){tx=(e.clientX/window.innerWidth-.5)*2;ty=(e.clientY/window.innerHeight-.5)*2},{passive:true});
if(FINE&&!RM){
  var cur=document.createElement('div'); cur.className='cur'; document.body.appendChild(cur);
  var cx=0,cy=0,px=0,py=0,shown=false;
  window.addEventListener('pointermove',function(e){px=e.clientX;py=e.clientY;if(!shown){cx=px;cy=py;shown=true;cur.classList.add('on')}
    cur.classList.toggle('big',!!e.target.closest('a,button,.node,.slide,.portrait'));
    $$('[data-mag]').forEach(function(m){var r=m.getBoundingClientRect(),dx=e.clientX-(r.left+r.width/2),dy=e.clientY-(r.top+r.height/2);
      if(Math.hypot(dx,dy)<r.width*.75){m.style.transform='translate('+dx*.22+'px,'+dy*.3+'px)'}else{m.style.transform=''}});
  },{passive:true});
  document.addEventListener('pointerleave',function(){cur.classList.remove('on');shown=false});
  (function loop(){cx=lerp(cx,px,.18);cy=lerp(cy,py,.18);cur.style.transform='translate('+cx+'px,'+cy+'px)';requestAnimationFrame(loop)})();
  $$('[data-mag]').forEach(function(m){m.style.transition='transform .35s cubic-bezier(.2,.7,.1,1),background .3s,color .3s,border-color .3s'});
}

/* ---------- helix ---------- */
(function(){
  var cv=$('#helix'); if(!cv) return;
  var ctx=cv.getContext('2d'); var W=0,H=0,narrow=false,dust=[],on=true,t0=performance.now();
  function size(){
    var r=cv.getBoundingClientRect(),d=Math.min(window.devicePixelRatio||1,2);
    W=r.width;H=r.height;cv.width=Math.round(W*d);cv.height=Math.round(H*d);ctx.setTransform(d,0,0,d,0,0);narrow=W<1000;
    dust=[];for(var i=0;i<(narrow?40:90);i++)dust.push({x:Math.random(),y:Math.random(),z:Math.random(),s:Math.random()*.00006+.00002,p:Math.random()*6.28});
    if(RM)draw(t0+4200);
  }
  function dot(x,y,r,col,a){
    ctx.fillStyle='rgba('+col+','+(a*.15).toFixed(3)+')';ctx.beginPath();ctx.arc(x,y,r*3.4,0,6.2832);ctx.fill();
    ctx.fillStyle='rgba('+col+','+a.toFixed(3)+')';ctx.beginPath();ctx.arc(x,y,r,0,6.2832);ctx.fill();
  }
  function draw(now){
    var t=(now-t0)/1000;
    mx=lerp(mx,tx,.05);my=lerp(my,ty,.05);
    ctx.clearRect(0,0,W,H);ctx.globalCompositeOperation='lighter';
    var cxp=W*(narrow?.5:.71),cyp=H*(narrow?.36:.5),len=H*(narrow?.78:1.2),R=Math.min(W,H)*(narrow?.2:.165);
    var lean=-.42+mx*.1,tilt=.3+my*.22,rot=t*.36+(window.scrollY||0)*.0016+mx*.5;
    var N=narrow?72:130,TURNS=2.4;
    var cl=Math.cos(lean),sl=Math.sin(lean),ct=Math.cos(tilt),st=Math.sin(tilt);
    function P(i,s){
      var u=i/N,a=u*TURNS*6.2832+rot+s*Math.PI;
      var x=Math.cos(a)*R,z=Math.sin(a)*R,y=(u-.5)*len;
      var y2=y*ct-z*st,z2=y*st+z*ct,sc=900/(900+z2);
      var X=x*sc,Y=y2*sc;
      return {x:cxp+X*cl-Y*sl,y:cyp+X*sl+Y*cl,z:z2};
    }
    var i,s,p,A,B;
    for(i=0;i<=N;i+=3){
      A=P(i,0);B=P(i,1);
      var gold=(i/3)%9===4,al=clamp(.2-((A.z+B.z)/2)/R*.1,.06,.38);
      ctx.strokeStyle=gold?'rgba(210,181,138,'+Math.min(.85,al*2.4).toFixed(3)+')':'rgba(148,180,204,'+al.toFixed(3)+')';
      ctx.lineWidth=gold?1.5:1;ctx.beginPath();ctx.moveTo(A.x,A.y);ctx.lineTo(B.x,B.y);ctx.stroke();
      if(gold){dot(A.x,A.y,3,'210,181,138',.95);dot(B.x,B.y,3,'210,181,138',.95)}
    }
    for(s=0;s<2;s++)for(i=0;i<=N;i++){
      p=P(i,s);var near=clamp((-p.z/R+1)/2,0,1);
      dot(p.x,p.y,(1.1+near*2.5)*(narrow?.85:1),s?'148,180,204':'237,229,218',.22+near*.72);
    }
    for(i=0;i<dust.length;i++){
      var d=dust[i],yy=((d.y-t*d.s*60)%1+1)%1,xx=((d.x+Math.sin(t*.2+d.p)*.01)%1+1)%1;
      dot(xx*W+mx*18*d.z,yy*H+my*12*d.z,.6+d.z*1.1,'202,211,221',.12+.3*d.z*(.6+.4*Math.sin(t*1.4+d.p)));
    }
    ctx.globalCompositeOperation='source-over';
  }
  function loop(now){if(on&&!document.hidden)draw(now);requestAnimationFrame(loop)}
  new IntersectionObserver(function(es){on=es[0].isIntersecting}).observe(cv);
  window.addEventListener('resize',size);size();
  if(!RM)requestAnimationFrame(loop);
})();


/* ---------- bloodstream: video de Veo como secuencia de fotogramas ligada al scroll ---------- */
(function(){
  var cv=$('#cells'),js=$('#zframes'); if(!cv||!js) return;
  var src=[];try{src=JSON.parse(js.textContent)}catch(e){} if(!src.length) return;
  window.__vframes=true;
  var ctx=cv.getContext('2d'),imgs=src.map(function(u){var im=new Image();im.decoding='async';im.src=u;return im}),W=0,H=0,cur=0,tgt=0,on=false,lastI=-1,t0=performance.now();
  function ready(im){return im&&im.complete&&im.naturalWidth}
  function size(){var r=cv.getBoundingClientRect(),d=Math.min(window.devicePixelRatio||1,1.5);W=Math.round(r.width*d);H=Math.round(r.height*d);cv.width=W;cv.height=H;lastI=-1;paint(true)}
  function paint(force){
    var sv=window.__sv||0,t=(performance.now()-t0)/1000,N=imgs.length;
    var f=Math.max(0,Math.min(N-1,cur+Math.sin(t*.45)*1.4));
    var i0=Math.floor(f),i1=Math.min(N-1,i0+1),a=f-i0;
    var A=imgs[i0],B=imgs[i1];if(!ready(A))return;
    var z=1+Math.min(.1,sv*.012);
    function put(im,al){var s=Math.max(W/im.naturalWidth,H/im.naturalHeight)*z,w=im.naturalWidth*s,h=im.naturalHeight*s;ctx.globalAlpha=al;ctx.drawImage(im,(W-w)/2,(H-h)/2,w,h)}
    put(A,1);if(a>.03&&ready(B))put(B,a);ctx.globalAlpha=1;
  }
  window.__setFrames=function(p){tgt=Math.max(0,Math.min(1,p))*(imgs.length-1)};
  function loop(){cur+=(tgt-cur)*.14;window.__sv=(window.__sv||0)*.93;if(on)paint(false);requestAnimationFrame(loop)}
  new IntersectionObserver(function(es){on=es[0].isIntersecting}).observe(cv);
  window.addEventListener('resize',size);size();
  if(RM){cur=tgt=imgs.length*.4;} else requestAnimationFrame(loop);
})();

/* ---------- células madre y exosomas (canvas provisional, colores naturales) ---------- */
(function(){
  var cv=$('#cells'); if(!cv||window.__vframes) return;
  var ctx=cv.getContext('2d'),W=0,H=0,narrow=false,cells=[],dust=[],on=false,last=0,t0=performance.now();
  function mk(c){c.a=Math.random()*6.2832;c.r=.1+Math.pow(Math.random(),.75)*.9;c.z=c.z===undefined?Math.random():1;c.kind=Math.random()<.16?1:0;c.sp=.6+Math.random()*.8;c.s=c.kind?(1.5+Math.random()*.7):(.22+Math.random()*.42);c.ph=Math.random()*6.28}
  function size(){var r=cv.getBoundingClientRect(),d=Math.min(window.devicePixelRatio||1,2);W=r.width;H=r.height;cv.width=Math.round(W*d);cv.height=Math.round(H*d);ctx.setTransform(d,0,0,d,0,0);narrow=W<900;
    cells=[];for(var i=0;i<(narrow?110:230);i++){var c={};mk(c);cells.push(c)}
    dust=[];for(i=0;i<(narrow?50:120);i++)dust.push({a:Math.random()*6.28,r:Math.random(),z:Math.random()});
    if(RM)draw(t0+3000,.016)}
  function proj(a,r,z){var p=1/(z*3+.2);return {x:W/2+Math.cos(a)*r*p*W*.17,y:H/2+Math.sin(a)*r*p*H*.24,p:p}}
  function draw(now,dt){
    var t=(now-t0)/1000;
    var g=ctx.createRadialGradient(W/2,H/2,0,W/2,H/2,Math.max(W,H)*.65);
    g.addColorStop(0,'#FFE6C0');g.addColorStop(.16,'#F0B070');g.addColorStop(.4,'#B8662C');g.addColorStop(.72,'#5A2410');g.addColorStop(1,'#220B06');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
    ctx.globalCompositeOperation='lighter';
    dust.forEach(function(d){d.z-=dt*.05;if(d.z<.03){d.z=1;d.a=Math.random()*6.28}var q=proj(d.a,d.r,d.z);
      ctx.fillStyle='rgba(255,226,190,'+(.3*Math.min(1,(1-d.z)*2)).toFixed(3)+')';ctx.beginPath();ctx.arc(q.x,q.y,Math.min(2,.4+q.p*.4),0,6.28);ctx.fill()});
    ctx.globalCompositeOperation='source-over';
    cells.sort(function(a,b){return b.z-a.z});
    cells.forEach(function(c){
      c.z-=dt*.075*c.sp; if(c.z<.025){mk(c)}
      var q=proj(c.a,c.r,c.z), sz=c.s*q.p*H*.034; if(sz<1.2||q.p>3.9) return;
      var fade=Math.min(1,(1-c.z)*3.2)*Math.min(1,(4.3-q.p)*1.6);
      var wob=1+Math.sin(t*1.3+c.ph)*.025;
      ctx.save();ctx.translate(q.x,q.y);ctx.globalAlpha=Math.max(0,fade*.95);
      if(c.kind){ /* célula madre: esfera perlada con núcleo */
        var rg=ctx.createRadialGradient(-sz*.3,-sz*.35,sz*.05,0,0,sz*wob);
        rg.addColorStop(0,'rgba(255,248,238,.96)');rg.addColorStop(.55,'rgba(238,208,188,.9)');rg.addColorStop(.9,'rgba(214,166,146,.88)');rg.addColorStop(1,'rgba(255,236,220,.95)');
        ctx.fillStyle=rg;ctx.beginPath();ctx.arc(0,0,sz*wob,0,6.2832);ctx.fill();
        var ng=ctx.createRadialGradient(sz*.04,sz*.02,0,0,0,sz*.4);ng.addColorStop(0,'rgba(176,118,104,.85)');ng.addColorStop(.7,'rgba(196,140,124,.55)');ng.addColorStop(1,'rgba(214,166,146,0)');
        ctx.fillStyle=ng;ctx.beginPath();ctx.arc(0,0,sz*.4,0,6.2832);ctx.fill();
        ctx.lineWidth=Math.max(1,sz*.05);ctx.strokeStyle='rgba(255,252,246,.55)';ctx.beginPath();ctx.arc(0,0,sz*.97*wob,3.5,5.4);ctx.stroke();
      } else { /* exosoma: vesícula translúcida con borde brillante */
        var eg=ctx.createRadialGradient(-sz*.25,-sz*.3,sz*.05,0,0,sz);
        eg.addColorStop(0,'rgba(255,246,232,.85)');eg.addColorStop(.7,'rgba(246,214,184,.45)');eg.addColorStop(1,'rgba(255,240,224,.8)');
        ctx.fillStyle=eg;ctx.beginPath();ctx.arc(0,0,sz,0,6.2832);ctx.fill();
        ctx.lineWidth=Math.max(.8,sz*.12);ctx.strokeStyle='rgba(255,252,244,.7)';ctx.beginPath();ctx.arc(0,0,sz*.94,0,6.2832);ctx.stroke();
      }
      ctx.restore();
    });
    ctx.globalAlpha=1;
  }
  function loop(now){var dt=Math.min(.05,(now-last)/1000||.016);last=now;var sv=window.__sv||0;window.__sv=sv*.93;if(on&&!document.hidden)draw(now,dt*(1+Math.min(8,sv)));requestAnimationFrame(loop)}
  new IntersectionObserver(function(es){on=es[0].isIntersecting}).observe(cv);
  window.addEventListener('resize',size);size();
  if(!RM)requestAnimationFrame(loop);
})();

/* ---------- giant marquee ---------- */
(function(){
  var tr=$('.bigmq .tr'); if(!tr||RM) return; var x=0,last=performance.now(),ly=window.scrollY||0,on=false,half=0;
  function m(){half=tr.scrollWidth/2}
  new IntersectionObserver(function(es){on=es[0].isIntersecting;m()}).observe(tr.parentNode);
  window.addEventListener('resize',m);m();
  (function loop(now){
    var dt=Math.min(.05,(now-last)/1000);last=now;var y=window.scrollY||0,dy=y-ly;ly=y;
    if(on&&half){x+=dt*60+Math.abs(dy)*.9;x%=half;tr.style.transform='translateX('+(-x)+'px)'}
    requestAnimationFrame(loop)})(last);
})();

/* ---------- chapters ---------- */
(function(){
  var vis=$('.vis'); if(!vis) return;
  var steps=$$('.step'),phs=$$('.ph',vis),num=$('.vnum b');
  function set(i){
    vis.setAttribute('data-i',i);
    phs.forEach(function(p,k){p.classList.toggle('on',k===i)});
    steps.forEach(function(s,k){s.classList.toggle('on',k===i)});
    num.textContent='0'+(i+1);
  }
  var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)set(steps.indexOf(e.target))})},{rootMargin:'-45% 0px -45% 0px'});
  steps.forEach(function(s){io.observe(s)});set(0);
})();

/* ---------- orbit map ---------- */
(function(){
  var cv=$('#orbit'); if(!cv) return;
  var ctx=cv.getContext('2d'),nodes=$$('.node'),pds=$$('.pd'),W=0,H=0,sel=0,on=true;
  var pos=nodes.map(function(n){return{x:parseFloat(n.getAttribute('data-x'))/100,y:parseFloat(n.getAttribute('data-y'))/100}});
  function select(i){sel=i;nodes.forEach(function(n,k){n.classList.toggle('on',k===i);n.setAttribute('aria-pressed',String(k===i))});pds.forEach(function(p,k){p.classList.toggle('on',k===i)})}
  nodes.forEach(function(n,k){
    n.addEventListener('mouseenter',function(){select(k)});
    n.addEventListener('focus',function(){select(k)});
    n.addEventListener('click',function(){select(k)});
  });
  function size(){var r=cv.getBoundingClientRect(),d=Math.min(window.devicePixelRatio||1,2);W=r.width;H=r.height;cv.width=Math.round(W*d);cv.height=Math.round(H*d);ctx.setTransform(d,0,0,d,0,0);if(RM)draw(0)}
  function draw(now){
    var t=now/1000;ctx.clearRect(0,0,W,H);ctx.globalCompositeOperation='lighter';
    var c={x:W/2,y:H/2},k,j;
    ctx.lineWidth=1;ctx.strokeStyle='rgba(148,180,204,.16)';ctx.beginPath();
    for(k=0;k<pos.length;k++){var q=pos[k];k?ctx.lineTo(q.x*W,q.y*H):ctx.moveTo(q.x*W,q.y*H)}
    ctx.closePath();ctx.stroke();
    [.18,.3,.42].forEach(function(r){ctx.beginPath();ctx.arc(c.x,c.y,r*W,0,6.2832);ctx.strokeStyle='rgba(148,180,204,.08)';ctx.stroke()});
    for(k=0;k<pos.length;k++){
      var X=pos[k].x*W,Y=pos[k].y*H,act=k===sel;
      var g=ctx.createLinearGradient(c.x,c.y,X,Y);g.addColorStop(0,'rgba(237,229,218,'+(act?.7:.12)+')');g.addColorStop(1,'rgba(148,180,204,'+(act?.9:.3)+')');
      ctx.strokeStyle=g;ctx.lineWidth=act?1.8:1;ctx.beginPath();ctx.moveTo(c.x,c.y);ctx.lineTo(X,Y);ctx.stroke();
      for(j=0;j<3;j++){var u=((t*(act?.34:.16)+j/3+k*.17)%1);
        var px=lerp(c.x,X,u),py=lerp(c.y,Y,u),a=Math.sin(u*Math.PI)*(act?1:.5);
        ctx.fillStyle='rgba(237,229,218,'+(a*.9).toFixed(3)+')';ctx.beginPath();ctx.arc(px,py,act?2.6:1.7,0,6.2832);ctx.fill();
        ctx.fillStyle='rgba(148,180,204,'+(a*.18).toFixed(3)+')';ctx.beginPath();ctx.arc(px,py,act?9:5,0,6.2832);ctx.fill()}
    }
    ctx.globalCompositeOperation='source-over';
  }
  function loop(now){if(on&&!document.hidden)draw(now);requestAnimationFrame(loop)}
  new IntersectionObserver(function(es){on=es[0].isIntersecting}).observe(cv);
  window.addEventListener('resize',size);size();select(0);
  if(!RM)requestAnimationFrame(loop);
})();


/* ---------- recorrido 3D de la clínica (estilo Street View) ---------- */
(function(){
  var sec=$('#clinica'),cv=$('#tourgl'); if(!sec||!cv||!window.THREE) return;
  var data;try{data=JSON.parse($('#tourdata').textContent)}catch(e){return}
  var rooms=data.rooms,idx={};rooms.forEach(function(r,i){idx[r.k]=i});
  var R;try{R=new THREE.WebGLRenderer({canvas:cv,antialias:true})}catch(e){return}
  R.setPixelRatio(Math.min(window.devicePixelRatio||1,1.75));R.outputColorSpace=THREE.SRGBColorSpace;
  var scene=new THREE.Scene(),cam=new THREE.PerspectiveCamera(58,1,.1,50);cam.rotation.order='YXZ';
  var texs=[],aspect=[],loader=new THREE.TextureLoader();
  rooms.forEach(function(r,i){var t=loader.load(r.src,function(tx){aspect[i]=tx.image.width/tx.image.height;fit()});t.colorSpace=THREE.SRGBColorSpace;t.anisotropy=4;texs[i]=t});
  var geo=new THREE.PlaneGeometry(1,1);
  function mk(z){var m=new THREE.Mesh(geo,new THREE.MeshBasicMaterial({transparent:true,opacity:1,depthWrite:false}));m.position.z=z;scene.add(m);return m}
  var mA=mk(-1),mB=mk(-1.002);mB.visible=false;mA.material.map=texs[0];
  var cur=0,W=1,H=1,tr=null,on=false,hs=[];
  var D2R=Math.PI/180,TH=2*Math.tan(40*D2R);
  function size(i){var a=aspect[i]||.8,vw=TH*(W/H),h=Math.max(TH*1.2,(vw*1.2)/a);return [h*a,h]}
  function setBase(m,i){m.userData.s=size(i)}
  function fit(){setBase(mA,cur);if(tr)setBase(mB,tr.to);apply()}
  function apply(){var k=tr?tr.kA:1,s=mA.userData.s||size(cur);mA.scale.set(s[0]*k,s[1]*k,1);if(tr){var kb=tr.kB,sb=mB.userData.s||size(tr.to);mB.scale.set(sb[0]*kb,sb[1]*kb,1)}}
  function resize(){var r=sec.getBoundingClientRect();W=Math.max(1,r.width);H=Math.max(1,r.height);R.setSize(W,H,false);cam.aspect=W/H;cam.updateProjectionMatrix();fit()}
  /* lista de espacios */
  var list=$('#tlist'),capEl=$('#tcap');
  list.innerHTML=rooms.map(function(r,i){return '<li><button type="button" data-i="'+i+'"><span class="k">0'+(i+1)+'</span><span class="t"><span class="es">'+r.es+'</span><span class="en">'+r.en+'</span></span></button></li>'}).join('');
  function mark(i){$$('#tlist button').forEach(function(b,k){b.setAttribute('aria-current',String(k===i))});capEl.innerHTML='<span class="es">'+rooms[i].ces+'</span><span class="en">'+rooms[i].cen+'</span>'}
  /* puntos de avance */
  var hotsEl=$('#hots');
  function buildHots(i){hotsEl.innerHTML='';hs=rooms[i].hs.map(function(h){var b=document.createElement('button');b.type='button';b.className='hs';b.setAttribute('data-to',h.to);
    b.innerHTML='<i></i><span class="es">→ '+h.les+'</span><span class="en">→ '+h.len+'</span>';hotsEl.appendChild(b);return {el:b,u:h.u,v:h.v}})}
  var vec=new THREE.Vector3();
  function placeHots(){var s=mA.userData.s||size(cur),k=tr?0:1;hs.forEach(function(h){
    vec.set((h.u-.5)*s[0],(.5-h.v)*s[1],-1).project(cam);
    var ok=vec.z<1&&Math.abs(vec.x)<1.05&&Math.abs(vec.y)<1.05;
    h.el.style.opacity=ok?k:0;h.el.style.pointerEvents=ok&&k?'auto':'none';
    h.el.style.transform='translate('+((vec.x+1)/2*W-25)+'px,'+((1-vec.y)/2*H-25)+'px)'})}
  /* mirada: cursor + arrastre con inercia */
  var tx=0,ty=0,ox=0,oy=0,vx=0,vy=0,down=false,lx=0,ly=0,moved=0;
  sec.addEventListener('pointerdown',function(e){if(e.target.closest('button'))return;down=true;moved=0;lx=e.clientX;ly=e.clientY;sec.classList.add('drag')});
  window.addEventListener('pointermove',function(e){var r=sec.getBoundingClientRect();tx=((e.clientX-r.left)/r.width-.5)*2;ty=((e.clientY-r.top)/r.height-.5)*2;
    if(down){var dx=e.clientX-lx,dy=e.clientY-ly;lx=e.clientX;ly=e.clientY;moved+=Math.abs(dx)+Math.abs(dy);vx=dx*.0022;vy=dy*.0016;oy=Math.max(-.3,Math.min(.3,oy+vx));ox=Math.max(-.14,Math.min(.14,ox+vy))}});
  window.addEventListener('pointerup',function(){down=false;sec.classList.remove('drag')});
  /* transición: se entra al espacio actual y se emerge en el siguiente */
  function ease(t){return t<.5?4*t*t*t:1-Math.pow(-2*t+2,3)/2}
  function go(i){if(tr||i===cur||i<0||i>=rooms.length)return;
    if(RM){cur=i;mA.material.map=texs[i];setBase(mA,i);apply();buildHots(i);mark(i);return}
    mB.material.map=texs[i];mB.material.opacity=0;mB.visible=true;tr={to:i,t0:performance.now(),dur:1700,kA:1,kB:1.4};setBase(mB,i);mark(i);apply()}
  function endTr(){var i=tr.to;cur=i;mA.material.map=texs[i];mA.material.opacity=1;setBase(mA,i);mB.visible=false;tr=null;oy=0;ox=0;apply();buildHots(i)}
  document.addEventListener('click',function(e){var b=e.target.closest('#tlist button');if(b)go(+b.getAttribute('data-i'));b=e.target.closest('.hs');if(b&&moved<6)go(idx[b.getAttribute('data-to')])});
  /* ciclo de dibujo (solo si la sección está en pantalla) */
  function frame(now){
    requestAnimationFrame(frame);if(!on||document.hidden)return;
    if(tr){var p=Math.min(1,(now-tr.t0)/tr.dur);
      tr.kA=1+.42*ease(Math.min(1,p/.62));tr.kB=1.4-.4*ease(Math.max(0,(p-.3)/.7));
      var f=ease(Math.max(0,Math.min(1,(p-.3)/.4)));mB.material.opacity=f;mA.material.opacity=1-f;apply();if(p>=1)endTr()}
    var t=now/1000,drift=RM?0:Math.sin(t*.35)*.012;
    ox*=down?1:.985;oy*=down?1:.992;
    cam.rotation.y=-(tx*.07)+oy*-1+drift;cam.rotation.x=-(ty*.035)-ox;
    placeHots();R.render(scene,cam);
  }
  new IntersectionObserver(function(es){on=es[0].isIntersecting;if(on)resize()},{rootMargin:'200px'}).observe(sec);
  window.addEventListener('resize',resize);resize();mark(0);buildHots(0);requestAnimationFrame(frame);
})();

/* ---------- scrubbed mission ---------- */
var scrubs=[];
$$('.scrub > span').forEach(function(el){
  var words=el.textContent.trim().split(/\s+/);el.textContent='';
  words.forEach(function(w,i){var s=document.createElement('span');s.textContent=w;el.appendChild(s);if(i<words.length-1)el.appendChild(document.createTextNode(' '))});
  scrubs.push($$('span',el));
});
if(RM) scrubs.forEach(function(ws){ws.forEach(function(w){w.classList.add('lit')})});

/* ---------- portrait tilt ---------- */
(function(){
  var t=$('.tilt'),p=$('.portrait'); if(!t||!FINE||RM) return;
  t.addEventListener('pointermove',function(e){var r=t.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
    p.style.transform='rotateY('+(x*12)+'deg) rotateX('+(-y*9)+'deg)'});
  t.addEventListener('pointerleave',function(){p.style.transform=''});
})();

/* ---------- gallery drag ---------- */
(function(){
  var rail=$('.rail'); if(!rail) return; var down=false,sx=0,sl=0;
  rail.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse')return;down=true;sx=e.clientX;sl=rail.scrollLeft;rail.classList.add('drag')});
  window.addEventListener('pointermove',function(e){if(down)rail.scrollLeft=sl-(e.clientX-sx)});
  window.addEventListener('pointerup',function(){down=false;rail.classList.remove('drag')});
  rail.addEventListener('scroll',function(){queue()},{passive:true});
})();

/* ---------- scroll loop ---------- */
var diveSec=$('.dive'),win=$('.dive .win'),cvs=$('#cells'),dcap=$('.dive .cap'),dchip=$('.dive .chip'),beats=$$('.beat'),ringsSec=$('.rings-s'),rgs=$$('.rg i'),top_=$('.top'),prog=$('.prog'),wm=$('.wm'),misSec=$('.mis'),travBg=$('.trav .bg'),travSec=$('.trav'),slides=$$('.slide .im'),ticking=false;
function queue(){if(!ticking){ticking=true;requestAnimationFrame(frame)}}
function frame(){
  ticking=false;
  var y=window.scrollY||0,vh=window.innerHeight,dh=document.documentElement.scrollHeight-vh;
  top_.classList.toggle('s',y>40);
  var vy=Math.abs(y-(window.__ly===undefined?y:window.__ly));window.__ly=y;window.__sv=Math.max(window.__sv||0,Math.min(12,vy*.12));
  prog.style.transform='scaleX('+(dh>0?clamp(y/dh,0,1):0)+')';
  if(!RM){
    if(misSec){
      var r=misSec.getBoundingClientRect(),p=clamp((vh*.8-r.top)/(vh*.2+r.height),0,1);
      scrubs.forEach(function(ws){var n=Math.round(p*ws.length*1.05);ws.forEach(function(w,i){w.classList.toggle('lit',i<n)})});
      if(wm)wm.style.transform='translate(calc(-50% + '+((r.top-vh/2)*.18).toFixed(1)+'px),-50%)';
    }
    if(diveSec){
      var dr=diveSec.getBoundingClientRect(),p=clamp(-dr.top/(dr.height-vh),0,1);
      var e=clamp(p/.42,0,1);e=e<.5?4*e*e*e:1-Math.pow(-2*e+2,3)/2;
      var nar=window.innerWidth<900;
      if(window.__setFrames)window.__setFrames(p);
      win.style.clipPath='none';
      cvs.style.transform='scale('+lerp(1.22,1,e).toFixed(4)+')';
      dcap.style.opacity=clamp(1-p/.11,0,1);dchip.style.opacity=clamp(1-p/.08,0,1);
      var segs=[[.14,.40],[.42,.68],[.70,.97]];
      beats.forEach(function(b,i){var o=clamp((p-segs[i][0])/.04,0,1)*clamp((segs[i][1]-p)/.04,0,1);b.style.opacity=o;b.style.transform='translate(-50%,-50%) scale('+(.94+o*.06)+')'});
    }
    if(ringsSec){
      var rr2=ringsSec.getBoundingClientRect(),q=clamp((vh-rr2.top)/(vh+rr2.height),0,1);
      rgs.forEach(function(r,i){r.style.transform='scale('+(.78+q*.42*(1+i*.03)).toFixed(3)+')'});
    }
    if(travSec){var tr=travSec.getBoundingClientRect();travBg.style.transform='translateY('+(((tr.top+tr.height/2)-vh/2)*-.08).toFixed(1)+'px)'}
    slides.forEach(function(im){var r2=im.parentNode.getBoundingClientRect();if(r2.right<-200||r2.left>window.innerWidth+200)return;
      im.style.transform='translateX('+(((r2.left+r2.width/2)-window.innerWidth/2)*-.06).toFixed(1)+'px)'});
  }
}
window.addEventListener('scroll',queue,{passive:true});window.addEventListener('resize',queue);
frame();
})();
