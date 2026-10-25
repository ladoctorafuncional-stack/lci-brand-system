"""Efectos de marca LCI 2026 para DOCUMENTOS (planes, handouts, reportes, brochures, presentaciones HTML).

Estándar aprobado por la Dra. (oct 2026): el feed de Instagram de 42 publicaciones es el PISO de calidad
para todo LCI. Los documentos ya no pueden salir planos (solo texto + tablas sobre blanco): deben usar el
mismo lenguaje visual — fotos tratadas, vidrio estriado, degradados de marca, ondas, cifras gigantes,
tarjetas de vidrio, cápsulas, conectores de nodos — adaptado a lectura e impresión.
Referencia visual: lci-piezas-graficas/references/estandar-visual-2026/ (grid + 42 posts).

Uso (junto con brand.py, NO lo reemplaza):
    import sys; sys.path.insert(0, '<ruta>/lci-design-system/assets')
    import brand as B, efectos_lci as E
    css  = E.css()                                  # añadir DESPUÉS de B.base_css()
    hero = E.hero(E.foto(ruta, 'calido'), 'Tu plan de', 'nutrición.', 'Eyebrow', 'Subtítulo')
    body = hero + ... + E.cifras([...]) + E.banda(E.vidrio(ruta, tinte='azul'), 'Titular', 'acento') + B.footer()
    html = B.html_doc('Título', body).replace('</style>', css + '</style>', 1)

Todos los fondos se generan en Python y se embeben en base64 (documento autocontenido, imprimible).
Las funciones de imagen vienen del motor de piezas (recetas_feed.py del skill hermano lci-piezas-graficas):
una sola implementación para redes y documentos.
"""
import os, sys, glob

def _ruta_piezas():
    aqui = os.path.dirname(os.path.abspath(__file__))
    cands = [os.path.join(aqui, '..', '..', 'lci-piezas-graficas', 'assets')]
    for pat in ('/mnt/skills/**/lci-piezas-graficas/assets', os.path.expanduser('~/.claude/**/lci-piezas-graficas/assets'),
                '/root/.claude/**/lci-piezas-graficas/assets'):
        cands += glob.glob(pat, recursive=True)
    for c in cands:
        if os.path.exists(os.path.join(c, 'recetas_feed.py')):
            return os.path.abspath(c)
    raise FileNotFoundError('No encuentro lci-piezas-graficas/assets (recetas_feed.py). Debe estar instalado el plugin lci-suite.')

sys.path.insert(0, _ruta_piezas())
import recetas_feed as R   # noqa: E402  (trae marca.py)

# ───────── IMÁGENES (data URIs) ─────────
def foto(path, modo='azul', crop=None, blur=0):
    """Tratamiento de marca obligatorio: bw | azul | frio | calido | ambar | claro | natural (solo tour clínica).
    En planes de nutrición la comida va con brand.lci_treat 'grade' (cálida, apetitosa) — no con estos modos."""
    return R.tratar(path, modo, crop=crop, blur=blur)

def vidrio(path, tinte='azul', crop=None, w=1600, h=600, tiras=34):
    """Vidrio estriado (reeded glass) a medida de una banda de documento."""
    return R.vidrio(path, crop=crop, tinte=tinte, tiras=tiras, w=w, h=h)

def movimiento(path, tinte='azul', crop=None):
    return R.movimiento(path, tinte=tinte, crop=crop)

def fondo(nombre='noche', w=1600, h=700, seed=1):
    """Degradado malla con grano: noche | acero | aurora | niebla (claro)."""
    return R.gradiente(nombre, seed=seed, w=w, h=h)

def ondas(w=1600, h=700, nivel=0.55, calor=True, seed=2):
    return R.ondas(seed=seed, w=w, h=h, nivel=nivel, calor=calor)

def microscopia(w=1600, h=700, seed=5):
    return R.bacterias(seed=seed, w=w, h=h)

pildora = R.pildora   # palabra dentro de cápsula fina en línea con el texto

def barra(txt, fs_px, color='#2A3649', fondo='rgba(93,118,140,.46)', borde=None, rol='elegante'):
    """Barra / caja de resaltado que ABRAZA el texto (regla oct-2026, medida en Paola 'are cellular messengers'):
    de la punta de los ascendentes a la base de los descendentes, sin aire vertical; nunca resaltados 'altos'.
    Debajo de una palabra con descendentes usar margin-top = R.M.aire_desc(palabra, fs_palabra)."""
    return R.M.barra(txt, fs_px, R.M.it_css(rol, fs_px, color), fondo=None if borde else fondo, borde=borde)

# ───────── CSS DE COMPONENTES ─────────
def css():
    return """
/* ===== efectos_lci (estándar visual 2026) — interlineado según INTERLINEADO-BLINDADO.md ===== */
.fx-hero{position:relative;min-height:440px;padding:56px 56px 48px;color:#fff;display:flex;flex-direction:column;
  justify-content:flex-end;background-size:cover;background-position:center;border-radius:0;overflow:hidden}
.fx-hero:before{content:"";position:absolute;inset:0;background:linear-gradient(100deg,rgba(18,24,34,.92) 0%,
  rgba(18,24,34,.70) 45%,rgba(18,24,34,.15) 100%)}
.fx-hero>*{position:relative}
.fx-hero .fx-logo{position:absolute;top:40px;left:56px;height:62px}
.fx-eyebrow{font-family:'Poppins',sans-serif;font-weight:300;font-size:.95rem;letter-spacing:.02em;color:#CAD3DD;margin-bottom:10px}
.fx-h1{font-family:'Mencken Std',serif;font-weight:700;font-size:3.6rem;line-height:.98;margin:0;color:#fff}
.fx-h1 .it{display:block;font-family:'Mencken Std Head','Mencken Std',serif;font-style:italic;font-weight:800;color:#9FB2C6}
.fx-sub{font-family:'Poppins',sans-serif;font-weight:300;font-style:italic;font-size:1.08rem;line-height:1.32;color:#E3EBF3;margin-top:1.35em;max-width:520px}
.fx-band{position:relative;margin:34px 0;padding:46px 52px;min-height:220px;color:#fff;display:flex;align-items:center;
  background-size:cover;background-position:center;border-radius:14px;overflow:hidden;break-inside:avoid}
.fx-band:before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(18,24,34,.78),rgba(18,24,34,.25))}
.fx-band>*{position:relative;max-width:620px}
.fx-band .t{font-family:'Mencken Std',serif;font-weight:700;font-size:2.1rem;line-height:1.05}
.fx-band .t .it{font-family:'Mencken Std Head',serif;font-style:italic;font-weight:800;color:#9FB2C6}
.fx-band p{font-family:'Poppins',sans-serif;font-weight:300;color:#E3EBF3;margin:1.35em 0 0;font-size:1rem;line-height:1.4}
.fx-cifras{display:grid;grid-template-columns:repeat(var(--n,3),1fr);gap:18px;margin:28px 0;break-inside:avoid}
.fx-cifra{position:relative;border-radius:14px;padding:26px 24px 22px;color:#fff;overflow:hidden;background-size:cover;
  background-position:center;min-height:170px}
.fx-cifra:before{content:"";position:absolute;inset:0;background:rgba(14,20,30,.35)}
.fx-cifra>*{position:relative}
.fx-cifra .n{font-family:'Mencken Std',serif;font-weight:700;font-size:3.4rem;line-height:.9;color:#fff}
.fx-cifra .n small{font-family:'Mencken Std Head',serif;font-style:italic;font-weight:800;font-size:1.4rem;color:#9FB2C6;margin-left:4px}
.fx-cifra .l{font-family:'Poppins',sans-serif;font-weight:300;font-size:.9rem;color:#E3EBF3;margin-top:10px;line-height:1.35}
.fx-vidrio{background:rgba(237,229,218,.80);color:#2A3649;border-radius:14px;padding:22px 26px;
  box-shadow:0 18px 40px -18px rgba(10,16,26,.55);border:1px solid rgba(255,255,255,.55)}
.fx-vidrio.oscuro{background:rgba(18,26,40,.55);color:#fff;border:1px solid rgba(202,211,221,.28);backdrop-filter:blur(8px)}
.fx-pasos{position:relative;margin:30px 0 30px 14px;padding-left:34px;border-left:1.5px solid #5D768C;break-inside:avoid}
.fx-paso{position:relative;margin:0 0 22px}
.fx-paso:before{content:"";position:absolute;left:-41px;top:.55em;width:11px;height:11px;border-radius:50%;
  background:#5D768C;box-shadow:0 0 0 5px rgba(93,118,140,.18)}
.fx-paso .k{font-family:'Mencken Std Head',serif;font-style:italic;font-weight:400;-webkit-text-stroke:.35px #5D768C;
  color:#5D768C;font-size:1.02rem}
.fx-paso .t{font-family:'Mencken Std',serif;font-weight:700;font-size:1.3rem;color:#2A3649;line-height:1.15}
.fx-paso p{font-family:'Poppins',sans-serif;font-weight:300;margin:4px 0 0;color:#3b4658;line-height:1.4}
.fx-circulos{display:grid;grid-template-columns:repeat(2,minmax(0,280px));justify-content:center;gap:34px;margin:28px 0;break-inside:avoid}
.fx-circulo{aspect-ratio:1/1;border-radius:50%;display:flex;flex-direction:column;justify-content:center;align-items:center;
  text-align:center;padding:12%;border:1.5px solid #9FB2C6;background:radial-gradient(circle at 35% 30%,#f7f9fb,#e3e9ef 70%);
  box-shadow:0 22px 40px -24px rgba(42,54,73,.55)}
.fx-circulo .t{font-family:'Mencken Std Head',serif;font-style:italic;font-weight:400;-webkit-text-stroke:.5px #2A3649;
  font-size:1.5rem;color:#2A3649}
.fx-circulo p{font-family:'Poppins',sans-serif;font-weight:300;font-size:.9rem;color:#3b4658;margin:8px 0 0;line-height:1.4}
.fx-refs{font-family:'Poppins',sans-serif;font-weight:300;font-size:.72rem;color:#6b7686;margin-top:10px}

/* --- Diagramaciones de revista (oct 2026): línea divisoria, recuadro-tarjeta, marco con conector --- */
/* LÍNEA DIVISORIA = réplica EXACTA en ratios de la receta aprobada r_derecha ('What is social jet lag?').
   Medido en la pieza aprobada (titular 66px): todo en em del titular (--fs): bold lh 1.00 · acento it 800 acero lh 1.04 ·
   filete 1.5px blanco 85% al ANCHO DEL BLOQUE (9.0em) con aire 0.515em arriba / 0.394em abajo · texto Poppins it 300
   acero 0.4545em lh 1.40.
   La versión en otro idioma es IDÉNTICA: mismo ancho de bloque, misma alineación, mismos aires — solo cambia el texto. */
.fx-linea{--fs:2.4rem;font-size:var(--fs);width:9em;max-width:100%;text-align:left}
.fx-linea .t{font-family:'Mencken Std',serif;font-weight:700;font-size:1em;line-height:1.0;color:#fff}
.fx-linea .t .it{display:block;font-family:'Mencken Std Head',serif;font-style:italic;font-weight:800;line-height:1.04;color:#9FB2C6}
.fx-linea hr{border:0;height:1.5px;background:rgba(255,255,255,.85);margin:.515em 0 .394em;width:100%;max-width:none}
.fx-linea p{font-family:'Poppins',sans-serif;font-weight:300;font-style:italic;color:#9FB2C6;margin:0;font-size:.4545em;line-height:1.4}
.fx-linea.claro .t{color:#2A3649}.fx-linea.claro .t .it{color:#5D768C}.fx-linea.claro hr{background:rgba(42,54,73,.35)}.fx-linea.claro p{color:#3b4658}
.fx-tarjeta-r{border:1px solid rgba(202,211,221,.35);border-radius:16px;padding:30px 34px;background:rgba(14,22,34,.42);
  backdrop-filter:blur(10px);color:#fff;box-shadow:0 24px 50px -28px rgba(0,0,0,.6)}
.fx-tarjeta-r .rot{font-family:'Poppins',sans-serif;font-weight:400;font-size:.72rem;letter-spacing:.12em;color:#CAD3DD;text-transform:uppercase}
.fx-tarjeta-r .t{font-family:'Poppins',sans-serif;font-weight:500;font-size:2.3rem;line-height:1.05;margin:6px 0 12px}
.fx-tarjeta-r ul{list-style:none;margin:0;padding:0}.fx-tarjeta-r li{font-family:'Poppins',sans-serif;font-weight:300;margin:4px 0;padding-left:16px;position:relative}
.fx-tarjeta-r li:before{content:"";position:absolute;left:0;top:.62em;width:5px;height:5px;border-radius:50%;background:#D2B58A}
.fx-tarjeta-r hr{border:0;height:1px;background:rgba(202,211,221,.30);margin:18px 0}
.fx-tarjeta-r p{font-family:'Poppins',sans-serif;font-weight:300;margin:0;color:#E3EBF3;line-height:1.4}
.fx-marco{border:1.5px solid rgba(159,178,198,.75);padding:34px 40px 36px;display:inline-block;background:rgba(9,14,24,.30);color:#fff}
.fx-marco .t{font-family:'Mencken Std',serif;font-weight:700;font-size:2.6rem;line-height:.98}
.fx-marco .t .it{display:block;font-family:'Mencken Std Head',serif;font-style:italic;font-weight:800;color:#9FB2C6}
.fx-marco .r{font-family:'Mencken Std',serif;font-weight:400;font-size:1.5rem;line-height:1.08;margin-top:12px}
.fx-conx{display:grid;grid-template-columns:46px 1fr;gap:0 24px;margin:0 0 0 60px}
.fx-conx .ln{border-left:1.5px solid rgba(159,178,198,.8);border-top:1.5px solid rgba(159,178,198,.8);border-bottom:1.5px solid rgba(159,178,198,.8);position:relative}
.fx-conx .ln:before,.fx-conx .ln:after{content:"";position:absolute;left:-4.5px;width:7px;height:7px;border-radius:50%;background:#9FB2C6}
.fx-conx .ln:before{top:-4px}.fx-conx .ln:after{bottom:-4px}
.fx-conx .it{font-family:'Poppins',sans-serif;font-style:italic;font-weight:300;color:#E3EBF3;margin:12px 0}
@media print{.fx-hero,.fx-band,.fx-cifra{-webkit-print-color-adjust:exact;print-color-adjust:exact}}
"""

# ───────── COMPONENTES HTML ─────────
def hero(fondo_uri, bold, acento, eyebrow='', sub='', logo_uri=None):
    lg = f'<img class="fx-logo" src="{logo_uri}">' if logo_uri else ''
    eb = f'<div class="fx-eyebrow">{eyebrow}</div>' if eyebrow else ''
    sb = f'<div class="fx-sub">{sub}</div>' if sub else ''
    return (f'<section class="fx-hero" style="background-image:url(\'{fondo_uri}\')">{lg}{eb}'
            f'<h1 class="fx-h1">{bold}<span class="it">{acento}</span></h1>{sb}</section>')

def banda(fondo_uri, bold, acento='', texto=''):
    ac = f' <span class="it">{acento}</span>' if acento else ''
    tx = f'<p>{texto}</p>' if texto else ''
    return f'<section class="fx-band" style="background-image:url(\'{fondo_uri}\')"><div><div class="t">{bold}{ac}</div>{tx}</div></section>'

def cifras(items, fondos=None):
    """items: [(numero, unidad, texto)]; fondos: lista de data URIs (p. ej. fondo('noche',seed=i))."""
    fondos = fondos or [fondo(n, w=700, h=500, seed=i) for i, n in enumerate(['noche', 'acero', 'aurora'] * 3)]
    cs = ''.join(f'<div class="fx-cifra" style="background-image:url(\'{fondos[i % len(fondos)]}\')">'
                 f'<div class="n">{n}<small>{u}</small></div><div class="l">{t}</div></div>' for i, (n, u, t) in enumerate(items))
    return f'<div class="fx-cifras" style="--n:{len(items)}">{cs}</div>'

def pasos(items):
    """items: [(rotulo, titulo, texto)] → línea de tiempo con nodos (conector Paola)."""
    return '<div class="fx-pasos">' + ''.join(
        f'<div class="fx-paso"><div class="k">{k}</div><div class="t">{t}</div><p>{p}</p></div>' for k, t, p in items) + '</div>'

def circulos(a_tit, a_txt, b_tit, b_txt):
    return (f'<div class="fx-circulos"><div class="fx-circulo"><div class="t">{a_tit}</div><p>{a_txt}</p></div>'
            f'<div class="fx-circulo"><div class="t">{b_tit}</div><p>{b_txt}</p></div></div>')

def tarjeta(html, oscuro=False):
    return f'<div class="fx-vidrio{" oscuro" if oscuro else ""}">{html}</div>'


# ───────── DIAGRAMACIONES DE REVISTA (oct 2026) ─────────
def linea(bold, acento, texto, claro=False, fs='2.4rem'):
    """Titular bold + acento itálico, LÍNEA DIVISORIA y texto (réplica en ratios de r_derecha 'What is social jet lag?').
    Igual en todos los idiomas: misma geometría, solo cambia el texto. Saltos de línea con <br> como en el original."""
    return (f'<div class="fx-linea{" claro" if claro else ""}" style="--fs:{fs}"><div class="t"><span data-opt style="display:block">{bold}</span><span class="it" data-opt>{acento}</span></div>'
            f'<hr><p>{texto}</p></div>')

def recuadro(rotulo, titulo, vinetas, texto, refs=''):
    """Recuadro-tarjeta de vidrio oscuro (ref. 'Gut bacteria'): rótulo en versal discreta, título Poppins,
    viñetas mínimas (punto oro pequeño), filete divisorio y texto de cierre. Va sobre un fondo con efecto."""
    lis = ''.join(f'<li>{v}</li>' for v in vinetas)
    return (f'<div class="fx-tarjeta-r"><div class="rot">{rotulo}</div><div class="t">{titulo}</div><ul>{lis}</ul>'
            f'<hr><p>{texto} {refs}</p></div>')

def marco(bold, acento, regular='', lista=None):
    """Marco de filete recto (ref. 'The brain ages too' de Paola): titular dentro del recuadro de línea simple y,
    debajo, conector de nodos con viñetas discretas en itálica."""
    reg = f'<div class="r">{regular}</div>' if regular else ''
    con = ''
    if lista:   # conector de Paola: una rama por ítem alineada con su 1ª línea (verificado ±1px)
        con = f'<div style="margin-left:3.6em">{R.M.conector(lista, fs=17, color="#E3EBF3")}</div>'
    return f'<div><div class="fx-marco"><div class="t">{bold}<span class="it">{acento}</span></div>{reg}</div>{con}</div>'


# ───────── INTERLINEADO BLINDADO (oct 2026) ─────────
def ritmo(fs_titular, fs_cuerpo):
    """Medidas de interlineado aprobadas (px). Ver lci-piezas-graficas/references/estandar-visual-2026/INTERLINEADO-BLINDADO.md."""
    return R.M.ritmo(fs_titular, fs_cuerpo)


OPTICA_JS = R.M.OPTICA_JS
def documento(B, titulo, body):
    """B.html_doc + CSS de efectos + alineación óptica. USAR SIEMPRE para documentos con efectos_lci."""
    return B.html_doc(titulo, body).replace('</style>', css() + '</style>', 1).replace('</body>', OPTICA_JS + '</body>', 1)
