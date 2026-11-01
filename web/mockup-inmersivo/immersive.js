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
var top_=$('.top'),prog=$('.prog'),wm=$('.wm'),misSec=$('.mis'),travBg=$('.trav .bg'),travSec=$('.trav'),slides=$$('.slide .im'),ticking=false;
function queue(){if(!ticking){ticking=true;requestAnimationFrame(frame)}}
function frame(){
  ticking=false;
  var y=window.scrollY||0,vh=window.innerHeight,dh=document.documentElement.scrollHeight-vh;
  top_.classList.toggle('s',y>40);
  prog.style.transform='scaleX('+(dh>0?clamp(y/dh,0,1):0)+')';
  if(!RM){
    if(misSec){
      var r=misSec.getBoundingClientRect(),p=clamp((vh*.8-r.top)/(vh*.2+r.height),0,1);
      scrubs.forEach(function(ws){var n=Math.round(p*ws.length*1.05);ws.forEach(function(w,i){w.classList.toggle('lit',i<n)})});
      if(wm)wm.style.transform='translate(calc(-50% + '+((r.top-vh/2)*.18).toFixed(1)+'px),-50%)';
    }
    if(travSec){var tr=travSec.getBoundingClientRect();travBg.style.transform='translateY('+(((tr.top+tr.height/2)-vh/2)*-.08).toFixed(1)+'px)'}
    slides.forEach(function(im){var r2=im.parentNode.getBoundingClientRect();if(r2.right<-200||r2.left>window.innerWidth+200)return;
      im.style.transform='translateX('+(((r2.left+r2.width/2)-window.innerWidth/2)*-.06).toFixed(1)+'px)'});
  }
}
window.addEventListener('scroll',queue,{passive:true});window.addEventListener('resize',queue);
frame();
})();
