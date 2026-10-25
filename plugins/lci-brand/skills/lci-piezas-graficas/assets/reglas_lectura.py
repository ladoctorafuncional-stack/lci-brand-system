"""REGLAS DE LECTURA Y MÁRGENES — Dra. Carolina, 10-oct-2026 (tras revisar el feed publicado en el celular).

Se inyectan en TODA pieza (marca.lienzo las añade al <head>) y corren al cargar las fuentes, ANTES de OPTICA_JS:
  1. PISO tipográfico (a 1080 px de ancho; escala con el ancho):
       · ningún texto por debajo del de la cápsula de contacto  → 19 px  (referencias [n]: 20 px, data-rol="ref")
       · rótulos/eyebrows/etiquetas (versalitas o tracking)     → 22 px
       · cuerpo de texto (≥28 caracteres, no display)            → 27 px
     Si el texto vive en un grupo que escala en em (conector, timeline), se agranda el grupo entero ([data-escala]).
  2. PILA de líneas ([data-pila="0.30"]): en un bloque de líneas de distinto tamaño, el aire de TINTA entre cada
     línea (descendentes de la de arriba → ascendentes de la de abajo) es IGUAL en todo el bloque
     (= valor × cuerpo más pequeño del bloque). Corrige el caso «Even after adjusting for BMI / up to 2×».
  3. ZONA SEGURA: margen = 10 % del lado MÁS CORTO en los 4 lados (post 1080×1350 → 108 px; story 1080×1920 →
     108 px; cuadrado 1200 → 120 px; banner 1200×630 → 63 px; portada 851×315 → 32 px). Todo texto, logo y
     recuadro queda dentro; solo la cápsula de contacto / web vive en la banda del margen inferior, centrada.
     El JS empuja hacia adentro cualquier bloque de texto que se salga y deja aviso en window.__lci_avisos.
"""
MARGEN = 0.10

def margen(w, h):
    return round(MARGEN * min(w, h))

REGLAS_JS = r'''<script>/* REGLAS DE LECTURA Y MÁRGENES LCI (10-oct-2026) */
(function(){
function txtEls(root){var out=[];root.querySelectorAll('*').forEach(function(e){
  for(var i=0;i<e.childNodes.length;i++){var n=e.childNodes[i];if(n.nodeType===3&&n.textContent.trim()){out.push(e);break;}}});return out;}
function run(){
  var L=document.getElementById('lienzo');if(!L)return;var R=L.getBoundingClientRect(),W=R.width,H=R.height,k=W/1080;
  var m=Math.round(0.10*Math.min(W,H));window.__lci_margen=m;window.__lci_avisos=[];
  var FL={gen:19*k,ref:20*k,label:22*k,body:27*k};
  /* 1 · PISO */
  txtEls(L).forEach(function(e){
    if(e.closest('.pill,[data-libre]'))return;
    var cs=getComputedStyle(e),fs=parseFloat(cs.fontSize),t=(e.textContent||'').trim();
    var rr=e.closest('[data-rol]'),rol=rr?rr.getAttribute('data-rol'):'';
    var ls=parseFloat(cs.letterSpacing)||0,fl;
    if(rol==='ref')fl=FL.ref;
    else if(rol==='label'||cs.textTransform==='uppercase'||ls/fs>0.06)fl=FL.label;
    else if(rol==='body'||(t.length>=28&&fs<44))fl=FL.body;
    else fl=FL.gen;
    if(fs+0.3<fl){var g=e.closest('[data-escala]');
      if(g){var gf=parseFloat(getComputedStyle(g).fontSize);g.style.fontSize=(gf*fl/fs).toFixed(1)+'px';}
      else e.style.fontSize=fl.toFixed(1)+'px';}
  });
  /* 2 · PILA */
  var c=document.createElement('canvas').getContext('2d');
  function met(e){var cs=getComputedStyle(e);c.font=cs.fontStyle+' '+cs.fontWeight+' '+cs.fontSize+' '+cs.fontFamily;
    var t=(e.textContent||'').trim()||'H',mm=c.measureText(t);return{a:mm.actualBoundingBoxAscent,d:mm.actualBoundingBoxDescent,fs:parseFloat(cs.fontSize)};}
  function mark(e,end){var s=document.createElement('span');s.style.cssText='display:inline-block;width:0;height:0;vertical-align:baseline';
    var tgt=e;while(tgt.lastElementChild&&getComputedStyle(tgt.lastElementChild).display==='block')tgt=end?tgt.lastElementChild:tgt.firstElementChild;
    if(end)tgt.appendChild(s);else tgt.insertBefore(s,tgt.firstChild);var y=s.getBoundingClientRect().bottom;s.remove();return y;}
  document.querySelectorAll('[data-pila]').forEach(function(p){
    var ch=[].slice.call(p.children).filter(function(x){return (x.textContent||'').trim();});if(ch.length<2)return;
    var ms=ch.map(met),fmin=Math.min.apply(null,ms.map(function(x){return x.fs;}));
    var tgt=parseFloat(p.getAttribute('data-pila')||'0.30')*fmin;
    for(var i=1;i<ch.length;i++){if(ch[i].querySelector('[data-resaltado]')||ch[i-1].querySelector('[data-resaltado]'))continue;  /* la barra conserva su propio aire */
      var b0=mark(ch[i-1],true),b1=mark(ch[i],false);
      var gap=(b1-ms[i].a)-(b0+ms[i-1].d);var mt=parseFloat(getComputedStyle(ch[i]).marginTop)||0;
      ch[i].style.marginTop=(mt+(tgt-gap)).toFixed(1)+'px';}
  });
  /* 3 · ZONA SEGURA */
  function absAnc(e){var a=e;while(a&&a!==L){var ar=a.getBoundingClientRect();if(getComputedStyle(a).position==='absolute'&&!(ar.width>=W-2&&ar.height>=H-2))return a;a=a.parentElement;}return null;}
  for(var pass=0;pass<3;pass++){
    txtEls(L).forEach(function(e){
      if(e.closest('.pill,[data-libre]'))return;
      var r=document.createRange();r.selectNodeContents(e);var b=r.getBoundingClientRect();if(!b.width)return;
      var x0=b.left-R.left,x1=b.right-R.left,y0=b.top-R.top,y1=b.bottom-R.top,a=absAnc(e);
      if(!a){if(x0<m-1||x1>W-m+1)window.__lci_avisos.push('margen lateral: '+(e.textContent||'').trim().slice(0,30));return;}
      var cs=getComputedStyle(a),fse=parseFloat(getComputedStyle(e).fontSize);
      if(fse>=56&&(x1-x0)>W-2*m){e.style.fontSize=(fse*(W-2*m)/(x1-x0)*0.985).toFixed(1)+'px';return;}  /* titular display: se ajusta el cuerpo, no se parte */
      if(x0<m-1){a.style.left=(parseFloat(cs.left)+(m-x0)).toFixed(0)+'px';}
      if(x1>W-m+1){if(cs.right!=='auto'&&a.style.right!=='')a.style.right=(parseFloat(cs.right)+(x1-(W-m))).toFixed(0)+'px';
        else a.style.maxWidth=(a.getBoundingClientRect().width-(x1-(W-m))).toFixed(0)+'px';}
      if(y0<m-1&&cs.top!=='auto'){a.style.top=(parseFloat(cs.top)+(m-y0)).toFixed(0)+'px';}
      if(pass===2&&(y1>H-m+1)&&!e.closest('[data-rol="pie"]'))window.__lci_avisos.push('margen inferior: '+(e.textContent||'').trim().slice(0,30));
    });
  }
  window.__lci_listo=true;
}
function go(){if(document.fonts&&document.fonts.ready)document.fonts.ready.then(run);else run();}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',go);else go();
})();</script>'''
