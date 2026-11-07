#!/usr/bin/env python3
"""Alternativas de diseño: bienvenida (titular uniforme) y clínica a todo el ancho."""
import io, contextlib, re
with contextlib.redirect_stdout(io.StringIO()):
    import build2 as B
IM=B.IMGS; T=B.T
css_fonts=B.FONTS
CSS=r'''
:root{--ink:#0C141E;--deep:#19222E;--navy:#2A3649;--azul:#5D768C;--steel:#94B4CC;--lb:#CAD3DD;--ice:#E3EBF3;--gold:#D2B58A;--cream:#EDE5DA;--paper:#FBF9F6;
--serif:"Mencken Std",Georgia,serif;--serifi:"Mencken Std Head","Mencken Std",Georgia,serif;--sans:"Poppins","Helvetica Neue",Arial,sans-serif;--ease:cubic-bezier(.2,.7,.1,1);color-scheme:dark}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;background:var(--ink);color:var(--cream);font:300 17px/1.55 var(--sans);overflow-x:hidden;-webkit-font-smoothing:antialiased}
body::before{content:"";position:fixed;inset:0 0 auto;height:env(safe-area-inset-top,0px);background:var(--ink);z-index:90}
h1,h2,p{margin:0}a{color:inherit;text-decoration:none}button{font:inherit;color:inherit;background:none;border:0;padding:0;cursor:pointer}
em{font-family:var(--serifi);font-style:italic;font-weight:800}
:focus-visible{outline:2px solid var(--gold);outline-offset:4px}
[data-lang="es"] .en,[data-lang="en"] .es{display:none!important}
.pad{padding-left:max(24px,4vw,env(safe-area-inset-left,0px));padding-right:max(24px,4vw,env(safe-area-inset-right,0px))}
.logo{display:block;aspect-ratio:1361/580;background:center/contain no-repeat;width:190px}
.eyebrow{font:500 clamp(15px,1.3vw,19px)/1.3 var(--sans);letter-spacing:.14em;text-transform:uppercase}
.btn{display:inline-flex;align-items:center;gap:12px;border-radius:999px;padding:17px 32px;font:500 15px/1 var(--sans);border:1px solid transparent;transition:background .3s,transform .3s}
.btn.cream{background:var(--cream);color:var(--navy)}.btn.ghost{border-color:rgba(237,229,218,.55);color:#fff}.btn.navy{background:var(--navy);color:var(--cream)}
.btn:hover{transform:translateY(-2px)}.btn svg{width:16px;height:16px}
/* barra de opciones */
.opts{position:fixed;left:50%;transform:translateX(-50%);top:calc(14px + env(safe-area-inset-top,0px));z-index:80;display:flex;gap:6px;padding:5px;border-radius:999px;background:rgba(25,34,46,.78);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);border:1px solid rgba(202,211,221,.22)}
.opts button{padding:10px 18px;border-radius:999px;font:500 13px/1 var(--sans);color:var(--lb);letter-spacing:.02em}
.opts button[aria-pressed="true"]{background:var(--cream);color:var(--navy)}
.opts .sep{width:1px;background:rgba(202,211,221,.25);margin:4px 4px}
.view[hidden]{display:none}
/* jerarquía de revista */
.hk .es,.hk .en{display:flex;flex-direction:column;align-items:flex-start}
.hk .k1,.hk .k3{font:400 clamp(28px,4.4vw,74px)/1.08 var(--serif)}
.hk .k2{display:block;font:400 clamp(72px,15.2vw,244px)/.84 var(--serif);margin:.02em 0 .06em -.03em}
.hk .k2 em{font-weight:800}
.hk .k3{display:block}.hk .k3 em.k4{font-size:1.6em;font-weight:800;line-height:.9}
/* ============ OPCIÓN 1 ============ */
.h1o{position:relative;min-height:100svh;display:flex;align-items:flex-end;background:var(--ink) url({{IMG:viaje}}) center/cover;isolation:isolate;overflow:hidden}
.h1o::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(180deg,rgba(12,20,30,.35) 0%,rgba(12,20,30,.28) 45%,rgba(12,20,30,.78) 100%)}
.h1o .in{width:100%;padding-block:150px 90px}
.h1o h1{letter-spacing:-.01em;margin:26px 0 38px;line-height:1;color:var(--cream);text-shadow:0 1px 18px rgba(12,20,30,.4)}.h1o .k2 em{color:#fff}.h1o .k4{color:var(--steel)}
.h1o .cta{display:flex;flex-wrap:wrap;gap:14px}
.walk{position:relative;height:520svh;background:var(--ink)}
.walk .stk{position:sticky;top:0;height:100svh;overflow:hidden}
.walk .tr{display:flex;height:100%;width:max-content;will-change:transform}
.room{position:relative;flex:none;width:100vw;height:100%;background:center/cover;isolation:isolate}
.room::before{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(12,20,30,.62) 0%,rgba(12,20,30,.18) 55%,rgba(12,20,30,0) 100%)}
.room .tx{position:absolute;left:max(24px,5vw);bottom:clamp(60px,12vh,130px);max-width:min(760px,86vw)}
.room .n{font:500 clamp(15px,1.3vw,19px)/1 var(--sans);letter-spacing:.14em;margin-bottom:18px;color:#fff;text-shadow:0 1px 12px rgba(12,20,30,.5)}
.room h2{font:700 clamp(44px,7vw,112px)/1 var(--serif);text-shadow:0 1px 18px rgba(12,20,30,.4)}
.room p{margin-top:20px;font-size:clamp(17px,1.5vw,22px);color:#fff;max-width:30em;text-shadow:0 1px 12px rgba(12,20,30,.5)}
.walk .bar{position:absolute;left:max(24px,5vw);right:max(24px,5vw);bottom:34px;height:2px;background:rgba(237,229,218,.25)}
.walk .bar i{display:block;height:100%;width:100%;background:var(--cream);transform-origin:0 50%;transform:scaleX(0)}
.walk .lab{position:absolute;top:calc(88px + env(safe-area-inset-top,0px));left:max(24px,5vw);font:500 13px/1 var(--sans);letter-spacing:.14em;text-transform:uppercase;color:#fff;text-shadow:0 1px 10px rgba(12,20,30,.6)}
/* ============ OPCIÓN 2 ============ */
.v2{background:var(--paper);color:var(--navy)}
.h2o{padding-top:150px}
.h2o .eyebrow{color:var(--navy)}
.h2o h1{letter-spacing:-.01em;margin:26px 0 44px;line-height:1;color:var(--navy)}.h2o .k4{color:var(--azul)}
.h2o .row{display:flex;flex-wrap:wrap;justify-content:space-between;gap:20px 40px;align-items:center;padding-bottom:44px}
.h2o .row p{max-width:34em;font-size:clamp(17px,1.5vw,21px);color:#34445A}
.h2o .band{height:min(72svh,720px);background:var(--navy) url({{IMG:hall}}) center 40%/cover;position:relative}
.cl2{position:relative;height:100svh;min-height:640px;background:var(--ink);overflow:hidden;isolation:isolate}
.cl2 .ph{position:absolute;inset:0;background:center/cover;opacity:0;transform:scale(1.06);transition:opacity .9s var(--ease),transform 1.6s var(--ease)}
.cl2 .ph.on{opacity:1;transform:scale(1)}
.cl2::after{content:"";position:absolute;inset:0;z-index:1;background:linear-gradient(270deg,rgba(12,20,30,.7) 0%,rgba(12,20,30,.2) 45%,rgba(12,20,30,0) 70%)}
.cl2 .head{position:absolute;z-index:2;left:max(24px,4vw);top:clamp(90px,13vh,140px);color:#fff;text-shadow:0 1px 14px rgba(12,20,30,.5)}
.cl2 .head h2{font:700 clamp(40px,6vw,96px)/1 var(--serif);margin-top:16px}
.cl2 ol{list-style:none;margin:0;padding:0;position:absolute;z-index:2;right:max(24px,4vw);top:50%;transform:translateY(-50%);width:min(520px,80vw)}
.cl2 li button{display:flex;align-items:baseline;gap:20px;width:100%;text-align:left;padding:18px 0;border-bottom:1px solid rgba(255,255,255,.28);color:rgba(255,255,255,.7);transition:color .3s,padding .4s var(--ease)}
.cl2 li button .k{font:500 14px/1 var(--sans);letter-spacing:.12em;min-width:2em}
.cl2 li button .t{font:700 clamp(26px,3vw,46px)/1.05 var(--serif);text-shadow:0 1px 12px rgba(12,20,30,.45)}
.cl2 li button[aria-pressed="true"],.cl2 li button:hover{color:#fff;padding-left:14px}
.cl2 .cap{position:absolute;z-index:2;left:max(24px,4vw);bottom:clamp(36px,8vh,80px);font:300 clamp(17px,1.5vw,22px)/1.45 var(--sans);color:#fff;max-width:26em;text-shadow:0 1px 12px rgba(12,20,30,.5)}
@media (max-width:900px){
  .room::before{background:linear-gradient(0deg,rgba(12,20,30,.7) 0%,rgba(12,20,30,.1) 60%,rgba(12,20,30,0) 100%)}
  .walk{height:440svh}
  .cl2 ol{top:auto;bottom:90px;right:max(24px,4vw);left:max(24px,4vw);transform:none;width:auto}
  .cl2 li button{padding:12px 0}.cl2 li button .t{font-size:26px}
  .cl2 .cap{display:none}
  .cl2::after{background:linear-gradient(0deg,rgba(12,20,30,.75) 0%,rgba(12,20,30,.1) 60%,rgba(12,20,30,0) 100%)}
  .cl2 .head{top:100px}
}
@media (max-width:1000px){.hk .k2{font-size:clamp(56px,15.2vw,150px)}}
@media (max-width:600px){.opts button{padding:8px 10px;font-size:11px;white-space:nowrap}.opts{gap:2px;padding:4px}}
@media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.cl2 .ph{transition:none}}
'''
CSS=re.sub(r'\{\{IMG:(\w+)\}\}',lambda m:'"'+IM[m.group(1)]+'"',CSS)
ARW=B.ARW
rooms=[('noche',T('Sala de terapias','Therapy room'),T('Un espacio de descanso con vista a Medellín.','A resting space with a view of Medellín.')),
       ('adn',T('Sala de medición','Measurement room'),T('Mediciones de grado clínico.','Clinical-grade measurements.')),
       ('consul',T('Consultorio','Consulting room'),T('Evaluación médica en una primera consulta de mínimo 2 horas.','Medical evaluation in a first visit of at least 2 hours.')),
       ('hall',T('Pasillo','Hallway'),T('Cada espacio, pensado alrededor del paciente.','Every space, designed around the patient.')),
       ('espera',T('Sala de espera','Waiting room'),T('Atención bilingüe en español e inglés.','Bilingual care in Spanish and English.'))]
RMS=''.join(f'<section class="room" style="background-image:url({IM[k]})"><div class="tx"><div class="n">0{i+1} / 05</div><h2>{t}</h2><p>{d}</p></div></section>' for i,(k,t,d) in enumerate(rooms))
LIST=''.join(f'<li><button type="button" data-i="{i}" aria-pressed="{"true" if i==0 else "false"}"><span class="k">0{i+1}</span><span class="t">{t}</span></button></li>' for i,(k,t,d) in enumerate(rooms))
PHS=''.join(f'<div class="ph{" on" if i==0 else ""}" style="background-image:url({IM[k]})"></div>' for i,(k,t,d) in enumerate(rooms))
CAPS=''.join(f'<p class="cap" data-c="{i}"{"" if i==0 else " hidden"}>{d}</p>' for i,(k,t,d) in enumerate(rooms))
H1=T('<span class="k1">Más años</span><span class="k2"><em>saludables</em>,</span><span class="k3">diseñados desde tu <em class="k4">biología</em>.</span>','<span class="k1">More</span><span class="k2"><em>healthy</em></span><span class="k3">years, designed around your <em class="k4">biology</em>.</span>')
LOGO=f'<span class="logo" style="background-image:url({IM["logo_w"]})" role="img" aria-label="Longevity Clinical Institute"></span>'
LOGON=f'<span class="logo" style="background-image:url({IM["logo_n"]})" role="img" aria-label="Longevity Clinical Institute"></span>'
BODY=f'''<div class="opts" role="group" aria-label="Opciones de diseño">
<button type="button" data-view="1" aria-pressed="true">{T('Opción 1 · Cinematográfica','Option 1 · Cinematic')}</button>
<button type="button" data-view="2" aria-pressed="false">{T('Opción 2 · Editorial','Option 2 · Editorial')}</button><span class="sep"></span>
<button type="button" data-lang="es" aria-pressed="true">ES</button><button type="button" data-lang="en" aria-pressed="false">EN</button></div>

<div class="view" id="v1">
<header class="pad" style="position:absolute;z-index:5;left:0;right:0;top:calc(66px + env(safe-area-inset-top,0px))">{LOGO}</header>
<section class="h1o"><div class="in pad"><div class="eyebrow">{T('Medellín · Longevity Clinical Institute','Medellín · Longevity Clinical Institute')}</div>
<h1 class="hk">{H1}</h1><div class="cta"><a class="btn cream" href="#">{T('Agendar valoración','Book an assessment')} {ARW}</a><a class="btn ghost" href="#rec1">{T('Recorre la clínica','Walk through the clinic')}</a></div></div></section>
<section class="walk" id="rec1"><div class="stk"><div class="lab">{T('La clínica · recorrido','The clinic · walkthrough')}</div><div class="tr" id="tr">{RMS}</div><div class="bar"><i id="bar"></i></div></div></section>
</div>

<div class="view v2" id="v2" hidden>
<section class="h2o"><div class="pad"><div style="margin-bottom:60px">{LOGON}</div>
<div class="eyebrow">{T('Medellín · Longevity Clinical Institute','Medellín · Longevity Clinical Institute')}</div>
<h1 class="hk">{H1}</h1>
<div class="row"><p>{T('Medicina de precisión: medición de grado clínico, evidencia científica rigurosa y una atención diseñada alrededor de tu biología.','Precision medicine: clinical-grade measurement, rigorous scientific evidence and care designed around your biology.')}</p>
<a class="btn navy" href="#">{T('Agendar valoración','Book an assessment')} {ARW}</a></div></div><div class="band" role="img" aria-label=""></div></section>
<section class="cl2"><div class="head"><div class="eyebrow">{T('La clínica','The clinic')}</div><h2>{T('Elige un espacio','Choose a space')}</h2></div>{PHS}<ol>{LIST}</ol>{CAPS}</section>
</div>'''
JS=r'''
(function(){
var root=document.documentElement;function $(s,c){return (c||document).querySelector(s)}function $$(s,c){return [].slice.call((c||document).querySelectorAll(s))}
function clamp(v,a,b){return Math.max(a,Math.min(b,v))}
document.addEventListener('click',function(e){var b=e.target.closest('[data-view]');if(b){var v=b.getAttribute('data-view');$$('[data-view]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});$('#v1').hidden=v!=='1';$('#v2').hidden=v!=='2';window.scrollTo(0,0);setTimeout(fitH,60);return}
 b=e.target.closest('[data-lang]');if(b){var l=b.getAttribute('data-lang');root.setAttribute('data-lang',l);root.lang=l;setTimeout(fitH,30);$$('[data-lang]').forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});return}
 b=e.target.closest('.cl2 li button');if(b)sel(+b.getAttribute('data-i'));if(e.target.closest('a[href="#"]'))e.preventDefault()});
root.setAttribute('data-lang','es');
function fitH(){$$('.hk').forEach(function(h){var el=[].slice.call(h.children).filter(function(c){return getComputedStyle(c).display!=='none'})[0];if(!el)return;var k1=el.querySelector('.k1'),k2=el.querySelector('.k2'),k3=el.querySelector('.k3');if(!k2||!k3)return;var host=h.parentElement,cs=getComputedStyle(host),avail=host.clientWidth-parseFloat(cs.paddingLeft)-parseFloat(cs.paddingRight);[k1,k2,k3].forEach(function(k){if(k){k.style.display='inline-block';k.style.whiteSpace='nowrap';k.style.alignSelf='flex-start'}});k3.style.fontSize='';var s3=parseFloat(getComputedStyle(k3).fontSize),w3=k3.getBoundingClientRect().width,lim=Math.min(avail,innerWidth*(innerWidth<1000?.9:.62));if(w3>lim){s3=s3*lim/w3;k3.style.fontSize=s3+'px';w3=k3.getBoundingClientRect().width}if(k1)k1.style.fontSize=s3+'px';k2.style.fontSize='200px';var w2=k2.getBoundingClientRect().width;k2.style.fontSize=(200*w3/w2)+'px'})}
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fitH);addEventListener('resize',fitH);setTimeout(fitH,200);
function sel(i){$$('.cl2 .ph').forEach(function(p,k){p.classList.toggle('on',k===i)});$$('.cl2 li button').forEach(function(x,k){x.setAttribute('aria-pressed',String(k===i))});$$('.cl2 .cap').forEach(function(c,k){c.hidden=k!==i})}
$$('.cl2 li button').forEach(function(b){b.addEventListener('mouseenter',function(){sel(+b.getAttribute('data-i'))})});
var tr=$('#tr'),bar=$('#bar'),walk=$('.walk'),tk=false;
function frame(){tk=false;if($('#v1').hidden)return;var r=walk.getBoundingClientRect(),vh=innerHeight,n=$$('.room').length,p=clamp(-r.top/(walk.offsetHeight-vh),0,1);
 tr.style.transform='translateX('+(-p*(n-1)*innerWidth)+'px)';bar.style.transform='scaleX('+p+')'}
addEventListener('scroll',function(){if(!tk){tk=true;requestAnimationFrame(frame)}},{passive:true});addEventListener('resize',frame);frame();
})();
'''
html=f'<title>LCI Alternativas de Diseño</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n<style>\n{css_fonts}\n{CSS}\n</style>\n{BODY}\n<script>\n{JS}\n</script>\n'
open('alt.html','w').write(html); print(round(len(html)/1e6,2),'MB')
