# -*- coding: utf-8 -*-
"""Kit de marca LCI — sistema gráfico elevado (estilo Paola / Ikigai)."""
import json, os

_A = json.load(open(os.path.join(os.path.dirname(__file__), 'assets.json')))
F = _A['fonts']; L = _A['logos']

def _face(key):
    f = F[key]
    return (f"@font-face{{font-family:'{f['family']}';font-style:{f['style']};"
            f"font-weight:{f['weight']};font-display:swap;"
            f"src:url(data:{f['mime']};base64,{f['data']}) format('{f['fmt']}');}}")

def fonts_css():
    return "\n".join(_face(k) for k in F)

# Logos as data URIs
LOGO_LEFT      = f"data:image/png;base64,{L['left']}"        # LONGEVITY CLINICAL INSTITUTE (blanco)
LOGO_SEAL      = f"data:image/png;base64,{L['seal_t']}"      # CAROLINA RODRÍGUEZ, MD (crema, transparente)
LOGO_LEFT_NAVY = f"data:image/png;base64,{L['left_navy']}"
LOGO_SEAL_NAVY = f"data:image/png;base64,{L['seal_navy']}"

# ---------- Paleta de marca ----------
PALETTE = """
:root{
  --navy:#2A3649; --navy-2:#222d3d; --navy-deep:#19222e; --navy-soft:#36445a;
  /* azul medio #5D768C = color de contraste/secundario oficial del brandbook
     (resaltar: texto-acento, subrayados; oro siempre como apoyo, nunca dominante).
     --blue-deep/--blue-ink se conservan como alias del oficial por retrocompatibilidad. */
  --blue:#CAD3DD; --blue-mid:#5D768C; --blue-deep:#5D768C; --blue-ink:#5D768C;
  --gold:#D2B58A; --gold-deep:#b9966a; --gold-soft:#e3cdac;
  --cream:#EDE5DA; --beige:#f7f1e9; --beige-2:#efe5d6; --paper:#fbf8f3;
  --ink:#2A3649; --ink-soft:#55617a; --line:#dcd0bd; --white:#fff;
}
"""

def base_css():
    """CSS completo: fuentes + paleta + sistema de componentes elevado."""
    return f"""
{fonts_css()}
{PALETTE}
*{{margin:0;padding:0;box-sizing:border-box;}}
html{{-webkit-print-color-adjust:exact;print-color-adjust:exact;}}
body{{font-family:'Poppins',sans-serif;font-weight:300;color:var(--ink);
  background:var(--paper);line-height:1.6;font-size:15px;-webkit-font-smoothing:antialiased;}}
.serif{{font-family:'Mencken Std',serif;}}
.serif-it{{font-family:'Mencken Std Head','Mencken Std',serif;font-style:italic;}}
.wrap{{max-width:900px;margin:0 auto;}}
strong,b{{font-weight:600;}}

/* ===== HERO (estilo editorial Paola) ===== */
.hero{{position:relative;background:
   radial-gradient(120% 90% at 80% 0%, #33425a 0%, var(--navy) 42%, var(--navy-deep) 100%);
   color:#fff;padding:46px 54px 52px;overflow:hidden;}}
.hero::after{{content:"";position:absolute;inset:0;
   background:radial-gradient(60% 70% at 18% 18%, rgba(202,211,221,.10), transparent 60%);
   pointer-events:none;}}
.hero-top{{display:flex;justify-content:space-between;align-items:flex-start;
   position:relative;z-index:2;margin-bottom:30px;}}
.hero-top img.seal{{height:78px;}}
.eyebrow{{font-size:.62rem;letter-spacing:.42em;text-transform:uppercase;
   color:var(--gold);font-weight:500;}}
.hero-doc{{text-align:right;}}
.hero-doc .tag{{font-size:.6rem;letter-spacing:.34em;text-transform:uppercase;
   color:var(--blue);font-weight:400;line-height:1.9;}}
.hero h1{{position:relative;z-index:2;font-family:'Mencken Std',serif;font-weight:700;
   font-size:3.15rem;line-height:1.04;letter-spacing:.01em;}}
.hero h1 .accent{{font-family:'Mencken Std Head','Mencken Std',serif;font-style:italic;
   color:var(--blue);}}
.hero .sub{{position:relative;z-index:2;margin-top:14px;font-size:1.02rem;font-weight:300;
   color:var(--blue);max-width:560px;}}
.hero .sub .serif-it{{color:#fff;}}
.hairline{{height:1px;background:linear-gradient(90deg,transparent,var(--gold),transparent);
   border:0;margin:26px 0;opacity:.7;}}

/* framed accent (caja con borde — motivo Paola) */
.framed{{display:inline-block;border:1.5px solid var(--blue-mid);
   padding:6px 16px;border-radius:3px;}}

/* tarjeta de paciente (glass) */
.patient-card{{position:relative;z-index:2;margin-top:30px;display:grid;
   grid-template-columns:1fr 1fr;gap:2px;background:rgba(255,255,255,.10);
   border:1px solid rgba(202,211,221,.28);border-radius:14px;overflow:hidden;
   backdrop-filter:blur(2px);}}
.patient-card .cell{{padding:14px 20px;background:rgba(25,34,46,.30);}}
.patient-card .k{{font-size:.58rem;letter-spacing:.22em;text-transform:uppercase;
   color:var(--gold);font-weight:500;}}
.patient-card .v{{font-size:.96rem;color:#fff;font-weight:400;margin-top:2px;}}

/* ===== SECTION HEADER ===== */
.section{{padding:40px 54px;}}
.section.alt{{background:var(--beige);}}
.sec-head{{display:flex;align-items:center;gap:16px;margin-bottom:26px;}}
.sec-ico{{width:50px;height:50px;border-radius:14px;flex-shrink:0;
   background:linear-gradient(145deg,var(--gold-soft),var(--gold) 55%,var(--gold-deep));
   display:flex;align-items:center;justify-content:center;
   box-shadow:0 6px 16px rgba(42,54,73,.22),0 1px 0 rgba(255,255,255,.6) inset,
              0 -2px 4px rgba(160,128,96,.4) inset;}}
.sec-ico svg{{width:25px;height:25px;stroke:#fff;fill:none;stroke-width:1.7;}}
.sec-head .t{{font-family:'Mencken Std',serif;font-weight:700;font-size:1.7rem;
   color:var(--navy);padding-bottom:7px;border-bottom:2px solid var(--blue-mid);}}
.sec-head .t .it{{font-family:'Mencken Std Head','Mencken Std',serif;font-style:italic;
   color:var(--gold-deep);}}
.lead{{font-size:.97rem;color:var(--ink-soft);margin-bottom:22px;max-width:760px;}}

/* ===== CARDS ===== */
.card{{background:#fff;border-radius:16px;padding:26px 28px;
   box-shadow:0 2px 4px rgba(42,54,73,.06),0 10px 28px rgba(42,54,73,.09),
              0 1px 0 rgba(255,255,255,.8) inset;}}
.card+.card{{margin-top:18px;}}
.note{{background:var(--beige);border-left:4px solid var(--gold);border-radius:10px;
   padding:18px 22px;font-size:.92rem;color:var(--ink-soft);}}
.note b{{color:var(--navy);}}

.dark-card{{background:linear-gradient(150deg,var(--navy-soft),var(--navy) 60%,var(--navy-2));
   color:var(--blue);border-radius:16px;padding:26px 30px;border:1px solid rgba(210,181,138,.25);
   box-shadow:0 12px 30px rgba(25,34,46,.3);}}
.dark-card h3{{font-family:'Mencken Std',serif;color:#fff;font-size:1.35rem;font-weight:700;
   margin-bottom:6px;}}
.dark-card h3 .it{{font-family:'Mencken Std Head',serif;font-style:italic;color:var(--blue);}}
.dark-card p{{font-weight:300;}} .dark-card strong{{color:var(--gold-soft);}}

.warn{{background:#fff;border:1px solid var(--gold);border-radius:12px;padding:16px 20px;
   margin-top:16px;}}
.warn .wh{{color:var(--gold-deep);font-weight:600;font-size:.82rem;letter-spacing:.04em;
   text-transform:uppercase;margin-bottom:8px;}}
.warn ul{{list-style:none;font-size:.88rem;color:var(--ink-soft);}}
.warn li{{padding:3px 0 3px 22px;position:relative;}}
.warn li::before{{content:"✕";position:absolute;left:0;color:#b35a4e;font-weight:600;}}

/* ===== BRACKET CONNECTOR (motivo Paola) ===== */
.bracket{{display:grid;grid-template-columns:34px 1fr;gap:0 18px;align-items:stretch;
   margin:20px 0;}}
.bracket .line{{border-left:1.5px solid var(--blue-mid);border-top:1.5px solid var(--blue-mid);
   border-bottom:1.5px solid var(--blue-mid);border-radius:2px;position:relative;}}
.bracket .line::before,.bracket .line::after{{content:"";position:absolute;left:-4px;
   width:7px;height:7px;border-radius:50%;background:var(--blue-mid);}}
.bracket .line::before{{top:-4px;}} .bracket .line::after{{bottom:-4px;}}
.bracket .items{{padding:4px 0;}}
.bracket .items .it{{font-size:.96rem;color:var(--navy);margin:6px 0;}}
.bracket .items .it .lead-w{{font-family:'Mencken Std Head',serif;font-style:italic;
   color:var(--blue-mid);}}

/* ===== ICON RING ROW (motivo Paola "Benefícios") ===== */
.ring-row{{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;text-align:center;margin:8px 0;}}
.ring{{width:74px;height:74px;border-radius:50%;border:1.5px solid var(--gold);
   margin:0 auto 10px;display:flex;align-items:center;justify-content:center;
   background:radial-gradient(circle at 50% 35%, rgba(210,181,138,.12), transparent 70%);}}
.ring svg{{width:30px;height:30px;stroke:var(--navy);fill:none;stroke-width:1.6;}}
.ring-row .lbl{{font-size:.84rem;color:var(--navy);font-weight:400;line-height:1.35;}}
.pill-quote{{margin-top:20px;border:1.5px solid var(--gold);border-radius:40px;
   padding:14px 26px;text-align:center;font-family:'Mencken Std Head',serif;font-style:italic;
   color:var(--gold-deep);font-size:1.05rem;}}

/* ===== TABLES ===== */
table{{width:100%;border-collapse:collapse;font-size:.86rem;border-radius:12px;overflow:hidden;
   box-shadow:0 6px 18px rgba(42,54,73,.08);}}
thead th{{background:var(--navy);color:var(--cream);font-weight:500;padding:11px 12px;
   text-align:left;font-size:.7rem;letter-spacing:.08em;text-transform:uppercase;}}
tbody td{{padding:11px 12px;border-bottom:1px solid var(--line);vertical-align:top;}}
tbody tr:nth-child(even){{background:var(--beige);}}
tbody tr:nth-child(odd){{background:#fff;}}
td .dish{{font-weight:600;color:var(--navy);}}
.daycol{{font-weight:600;color:var(--gold-deep);font-family:'Mencken Std',serif;}}

/* ===== ZONE / FITT / DAY (deportivo) ===== */
.zone{{display:flex;align-items:center;gap:14px;padding:11px 16px;border-radius:10px;
   margin-bottom:7px;background:#fff;box-shadow:0 2px 8px rgba(42,54,73,.06);}}
.zone .zn{{width:38px;height:38px;border-radius:50%;flex-shrink:0;display:flex;
   align-items:center;justify-content:center;font-weight:600;font-size:.9rem;color:#fff;}}
.zone .zt{{font-weight:600;color:var(--navy);font-size:.9rem;}}
.zone .zd{{font-size:.8rem;color:var(--ink-soft);}}
.fitt-grid{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;}}
.fitt{{background:#fff;border-radius:14px;border-left:5px solid var(--gold);padding:18px 18px;
   box-shadow:0 6px 16px rgba(42,54,73,.08);}}
.fitt .fl{{font-size:.6rem;font-weight:600;letter-spacing:.12em;text-transform:uppercase;
   color:var(--gold-deep);}}
.fitt .ft{{font-family:'Mencken Std',serif;font-size:1.15rem;color:var(--navy);font-weight:700;margin:2px 0 6px;}}
.fitt .fv{{font-size:.82rem;color:var(--ink-soft);}}
.day{{background:#fff;border-radius:14px;padding:18px 20px;margin-bottom:14px;
   box-shadow:0 6px 16px rgba(42,54,73,.07);}}
.day.s{{border-left:5px solid var(--navy);}} .day.c{{border-left:5px solid var(--gold);}}
.day.r{{border-left:5px solid var(--cream);}} .day.f{{border-left:5px solid var(--blue-deep);}}
.day .dh{{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:10px;}}
.day .dn{{font-family:'Mencken Std',serif;font-weight:700;color:var(--navy);font-size:1.12rem;}}
.day .dtag{{font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:#fff;
   padding:3px 10px;border-radius:20px;font-weight:500;}}
.tag-s{{background:var(--navy);}} .tag-c{{background:var(--gold-deep);}}
.tag-f{{background:var(--blue-ink);}} .tag-r{{background:var(--gold);}}
.ex-tbl td{{font-size:.84rem;}} .ex-tbl .exn{{font-weight:500;color:var(--navy);}}
.prio{{display:inline-block;background:var(--gold-deep);color:#fff;font-size:.58rem;
   padding:2px 8px;border-radius:12px;letter-spacing:.04em;margin-left:6px;vertical-align:middle;}}

/* ===== TIPS / STEPS ===== */
.numlist{{counter-reset:n;}}
.numitem{{display:flex;gap:16px;margin-bottom:18px;}}
.numitem .nc{{counter-increment:n;flex-shrink:0;width:38px;height:38px;border-radius:50%;
   background:linear-gradient(145deg,var(--gold-soft),var(--gold-deep));color:#fff;
   display:flex;align-items:center;justify-content:center;font-weight:600;
   box-shadow:0 4px 10px rgba(160,128,96,.35),0 1px 0 rgba(255,255,255,.5) inset;}}
.numitem .nc::before{{content:counter(n);}}
.numitem .nt{{font-family:'Mencken Std',serif;font-weight:700;color:var(--gold-soft);font-size:1.05rem;}}
.numitem.light .nt{{color:var(--gold-deep);}}
.quote{{margin-top:26px;background:rgba(210,181,138,.16);border-radius:14px;padding:22px 28px;
   text-align:center;font-family:'Mencken Std Head',serif;font-style:italic;color:var(--gold-soft);
   font-size:1.18rem;}}
.dark-section{{background:linear-gradient(150deg,var(--navy),var(--navy-deep));color:var(--blue);
   padding:42px 54px;}}
.dark-section .sec-head .t{{color:#fff;}}
.dark-section .lead{{color:var(--blue);}}

/* ===== FOOTER PILL (estilo Paola) ===== */
.foot{{background:var(--navy-deep);padding:34px 54px 40px;text-align:center;color:#fff;}}
.foot .fname{{font-family:'Mencken Std',serif;font-size:1.25rem;font-weight:700;color:#fff;}}
.foot .ftag{{font-size:.62rem;letter-spacing:.34em;text-transform:uppercase;color:var(--gold);
   margin-top:4px;margin-bottom:22px;}}
.foot .contact{{display:inline-flex;align-items:center;gap:18px;border:1.4px solid rgba(202,211,221,.4);
   border-radius:40px;padding:12px 26px;font-size:.82rem;color:var(--blue);font-weight:300;}}
.foot .contact .sep{{width:1px;height:16px;background:rgba(202,211,221,.4);}}
.foot .contact .wa{{width:22px;height:22px;border-radius:50%;border:1.2px solid var(--blue);
   display:inline-flex;align-items:center;justify-content:center;}}
.foot .contact .wa svg{{width:13px;height:13px;fill:var(--blue);}}

/* ===== PRINT ===== */
.printbtn{{position:fixed;bottom:24px;right:24px;z-index:99;background:var(--navy);color:#fff;
   border:none;border-radius:40px;padding:13px 22px;font-family:'Poppins';font-size:.82rem;
   font-weight:500;box-shadow:0 8px 24px rgba(25,34,46,.4);cursor:pointer;display:flex;gap:8px;align-items:center;}}
.avoid-break{{page-break-inside:avoid;}}
@media print{{
  @page{{margin:0;size:letter;}}
  body{{background:#fff;font-size:12px;}}
  .no-print{{display:none!important;}}
  .section,.dark-section,.hero,.foot{{padding-left:34px;padding-right:34px;}}
  .ring-row,.fitt-grid{{gap:10px;}}
  /* Cada sección empieza en página nueva. El hero queda como portada. */
  .section,.dark-section,.band-intro{{break-before:page;page-break-before:always;}}
  .hero{{break-before:auto;page-break-before:auto;}}
  /* Una sección corta marcada así NO fuerza página nueva: fluye y llena el espacio de la
     anterior si cabe entera; si no cabe, pasa completa a la página siguiente (no se parte). */
  .keep-with-prev{{break-before:auto!important;page-break-before:auto!important;
     break-inside:avoid;page-break-inside:avoid;}}
  /* Una banda/banner introductorio arrastra a su sección: no la separa en otra página. */
  .band-intro + .section,.band-intro + .dark-section{{break-before:avoid;page-break-before:avoid;}}
  .foot{{break-before:avoid;page-break-before:avoid;}}
  /* Hero más compacto en impresión: deja entrar "enfoque" en la página 1 */
  .hero{{padding-top:30px;padding-bottom:30px;}}
  .hero h1{{font-size:2.6rem;}}
  .hero .sub{{margin-top:9px;font-size:.95rem;}}
  .hairline{{margin:15px 0;}}
  .patient-card{{margin-top:16px;}}
  .patient-card .cell{{padding:10px 18px;}}
  .section{{padding-top:30px;}}
  /* Tarjetas algo más compactas en impresión: mejor densidad sin perder aire. */
  .card{{padding:19px 22px;}}
  .note{{padding:14px 18px;}}
  .dark-card{{padding:20px 24px;}}
  *{{-webkit-print-color-adjust:exact!important;print-color-adjust:exact!important;}}
}}
@media(max-width:680px){{
  .hero,.section,.dark-section,.foot{{padding-left:22px;padding-right:22px;}}
  .hero h1{{font-size:2.2rem;}} .patient-card,.ring-row,.fitt-grid{{grid-template-columns:1fr 1fr;}}
}}
"""

# WhatsApp glyph
_WA = ('<svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 0 0-8.6 15l-1.4 5 5.1-1.3A10 10 0 1 0 12 2zm0 '
       '18a8 8 0 0 1-4.1-1.1l-.3-.2-3 .8.8-2.9-.2-.3A8 8 0 1 1 12 20zm4.5-5.9c-.2-.1-1.4-.7-1.6-.8'
       '-.2-.1-.4-.1-.5.1l-.7.9c-.1.2-.3.2-.5.1a6.5 6.5 0 0 1-3.2-2.8c-.1-.2 0-.4.1-.5l.4-.5c.1-.2.1-.3'
       '0-.5l-.7-1.7c-.2-.4-.4-.4-.5-.4h-.5c-.2 0-.5.1-.7.3a3 3 0 0 0-.9 2.2c0 1.3 1 2.6 1.1 2.8.1.2 '
       '1.9 3 4.7 4.1 1.7.6 1.9.4 2.2.4.4 0 1.3-.5 1.5-1 .2-.5.2-1 .1-1z"/></svg>')

def contact_pill():
    return (f'<div class="contact"><span class="wa">{_WA}</span>'
            f'<span>(+57) 301 512 39 91</span><span class="sep"></span>'
            f'<span>@longevityclinicalinstitute</span><span class="sep"></span>'
            f'<span>longevityclinicalinstitute.com</span></div>')

def footer():
    return (f'<footer class="foot">'
            f'<img src="{LOGO_LEFT}" style="height:58px;margin-bottom:18px;">'
            f'<div class="fname">Dra. Carolina Rodríguez Morales</div>'
            f'<div class="ftag">Longevity &amp; Functional Medicine</div>'
            f'{contact_pill()}</footer>')

def seal_svg(size=78, color="#EDE5DA"):
    """Sello circular LCI tipográfico (monograma)."""
    return f'''<svg width="{size}" height="{size}" viewBox="0 0 200 200" fill="none">
  <defs><path id="ct" d="M100,100 m-74,0 a74,74 0 1,1 148,0 a74,74 0 1,1 -148,0"/>
  <path id="cb" d="M100,100 m-74,0 a74,74 0 1,0 148,0 a74,74 0 1,0 -148,0"/></defs>
  <text fill="{color}" font-family="Poppins" font-size="11" letter-spacing="3.4">
    <textPath href="#ct" startOffset="50%" text-anchor="middle">LONGEVITY CLINICAL INSTITUTE</textPath></text>
  <text fill="{color}" font-family="Poppins" font-size="11" letter-spacing="3.4">
    <textPath href="#cb" startOffset="50%" text-anchor="middle">· LONGEVITY CLINICAL INSTITUTE ·</textPath></text>
  <text x="100" y="118" fill="{color}" font-family="Mencken Std,serif" font-size="58"
    font-weight="400" text-anchor="middle" letter-spacing="2">LCI</text>
</svg>'''

def img_strip(bg, eyebrow, head_a, head_b, h=220, pos='center'):
    """Banda de imagen tratada para CERRAR una sección y llenar espacio (no fuerza salto).
    `bg` es un data URI (usar lci_treat para tratar la foto). Parte del sistema de gestión
    inteligente del espacio: ver references/design-recipe.md."""
    return (f'<div class="avoid-break" style="margin-top:22px;position:relative;height:{h}px;'
            f'border-radius:16px;overflow:hidden;display:flex;align-items:flex-end;padding:22px 26px;'
            f'color:#fff;box-shadow:0 10px 26px rgba(42,54,73,.16);'
            f'background:linear-gradient(0deg, rgba(25,34,46,.90) 0%, rgba(25,34,46,.45) 45%, rgba(25,34,46,.06) 100%),'
            f"url('{bg}');background-size:cover;background-position:{pos};\">"
            f'<div style="position:relative;z-index:2;">'
            f'<div class="eyebrow" style="color:var(--gold);">{eyebrow}</div>'
            f'<div class="serif" style="font-size:1.4rem;margin-top:3px;line-height:1.15;">{head_a} '
            f'<span class="serif-it" style="color:var(--blue);">{head_b}</span></div></div></div>')

def html_doc(title, body):
    return (f'<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">'
            f'<meta name="viewport" content="width=device-width,initial-scale=1.0">'
            f'<title>{title}</title><style>{base_css()}</style></head><body>{body}'
            f'<button class="printbtn no-print" onclick="window.print()">'
            f'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fff" '
            f'stroke-width="2"><path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2'
            f'v5a2 2 0 0 1-2 2h-2M6 14h12v8H6z"/></svg> Imprimir / Guardar PDF</button></body></html>')

print("brand.py OK")
