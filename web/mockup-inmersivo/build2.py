#!/usr/bin/env python3
"""Immersive LCI website direction: self-contained HTML (fonts + images base64)."""
import base64, io, os, re, glob
from PIL import Image
import sys
sys.path.insert(0, '/home/user/lci-brand-system/plugins/lci-brand/skills/lci-design-system/assets')
from lci_treat import treat_cool

R = '/home/user/lci-brand-system'
FOT = f'{R}/plugins/lci-fotos/skills/lci-banco-fotos/fotos'
OUT = os.path.dirname(os.path.abspath(__file__))
b64 = lambda b: base64.b64encode(b).decode()


def img(path, w, q=72, cool=None):
    im = Image.open(path)
    if im.mode in ('RGBA', 'LA', 'P'):
        bg = Image.new('RGB', im.size, (255, 255, 255)); im = im.convert('RGBA'); bg.paste(im, mask=im.split()[3]); im = bg
    im = im.convert('RGB')
    if im.width > w: im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    if cool is not None: im = treat_cool(im, **cool)
    buf = io.BytesIO(); im.save(buf, 'JPEG', quality=q, optimize=True, progressive=True)
    return f'data:image/jpeg;base64,{b64(buf.getvalue())}'


def logo(name, w):
    im = Image.open(f'{R}/brand/logos/{name}.png').convert('RGBA')
    im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
    buf = io.BytesIO(); im.save(buf, 'PNG', optimize=True)
    return f'data:image/png;base64,{b64(buf.getvalue())}'


IMGS = {
    'dina': img(f'{FOT}/lifestyle/dinamometro.jpg', 1300, 72, cool={}),
    'medi': img(f'{FOT}/clinica-real/real-sala-medicion-inbody.jpg', 900, 74, cool={}),
    'rostro': img(f'{FOT}/lifestyle/rostro-deportista.jpg', 1700, 70, cool={}),
    'hall': img(f'{FOT}/clinica/pasillo-luces-doradas.jpg', 760, 74, cool={}),
    'adn': img(f'{FOT}/clinica/sala-medicion-adn.jpg', 760, 74, cool={}),
    'consul': img(f'{FOT}/clinica/consultorio-calido.jpg', 760, 74, cool={}),
    'sillon': img(f'{FOT}/clinica/sillon-terapia-claro.jpg', 700, 72, cool={}),
    'noche': img(f'{FOT}/clinica/sala-terapia-noche-ciudad.jpg', 700, 72, cool={}),
    'viaje': img(f'{FOT}/clinica-real/real-salas-terapia-dobles.jpg', 1500, 70, cool={}),
    'espera': img(f'{FOT}/clinica-real/real-sala-espera-amplia.jpg', 1100, 70, cool={}),
    'dra': img(f'{R}/brand/equipo/retratos/carolina-rodriguez.png', 900, 76, cool=dict(tint=0.0)),
    'bg_mesh1': img(f'{R}/brand/fondos/mesh-oscuro/19-mesh-oscuro-1.jpg', 900, 62),
    'bg_malla': img(f'{R}/brand/fondos/mallas/17-malla-2-intensidad-38.jpg', 1100, 66),
    'bg_galaxia': img(f'{R}/brand/fondos/galaxias/13-galaxia-1.jpg', 900, 60),
    'bg_noche': img(f'{R}/brand/fondos/degradados-clasicos/02-noche-espejo.jpg', 900, 60),
    'bg_claro': img(f'{R}/brand/fondos/mesh-claro/22-mesh-claro-1.jpg', 900, 60),
    'sello': logo('sello_beige', 360),
    'sello_navy': logo('sello_navy', 360),
    'logo_w': logo('principal_blanco', 640),
    'logo_n': logo('principal_navy', 640),
}

F = f'{R}/fonts'
def face(fam, file, w, style='normal', fmt='opentype'):
    mime = 'font/otf' if fmt == 'opentype' else 'font/ttf'
    return (f'@font-face{{font-family:"{fam}";src:url(data:{mime};base64,{b64(open(f"{F}/{file}", "rb").read())}) format("{fmt}");'
            f'font-weight:{w};font-style:{style};font-display:swap}}')
FONTS = '\n'.join([
    face('Mencken Std', 'mencken-std-400.otf', 400), face('Mencken Std', 'mencken-std-700.otf', 700), face('Mencken Std', 'mencken-std-800.otf', 800),
    face('Mencken Std Head', 'mencken-std-head-800-italic.otf', 800, 'italic'),
    face('Poppins', 'poppins-300.ttf', 300, 'normal', 'truetype'), face('Poppins', 'poppins-300-italic.ttf', 300, 'italic', 'truetype'),
    face('Poppins', 'poppins-400.ttf', 400, 'normal', 'truetype'), face('Poppins', 'poppins-500.ttf', 500, 'normal', 'truetype'),
])
css = open(f'{OUT}/immersive.css').read().replace('/*FONTS*/', FONTS)
css = re.sub(r'\{\{IMG:(\w+)\}\}', lambda m: f'"{IMGS[m.group(1)]}"', css)
js = open(f'{OUT}/immersive.js').read()
THREEJS = open('/tmp/claude-0/-home-user-lci-brand-system/90311451-3058-5964-b625-4f30819e3e03/scratchpad/vial/node_modules/three/build/three.min.js').read()


def A(es, en): return f'{es} / {en}'
def T(es, en): return f'<span class="es">{es}</span><span class="en">{en}</span>'

WA = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12.04 2a9.9 9.9 0 0 0-8.4 15.1L2 22l5-1.6A9.9 9.9 0 1 0 12.04 2zm0 1.8a8.1 8.1 0 1 1-4.3 15l-.3-.2-2.9.9.9-2.8-.2-.3A8.1 8.1 0 0 1 12.04 3.8zm-3 4.1c-.2 0-.5.1-.7.4-.3.3-1 1-1 2.4s1 2.8 1.2 3c.1.2 2 3.1 4.9 4.3 2.4 1 2.9.8 3.4.7.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4l-.5-.3-1.8-.9c-.3-.1-.5-.1-.7.1l-.8 1c-.1.2-.3.2-.6.1-.3-.2-1.1-.4-2.1-1.3-.8-.7-1.3-1.5-1.4-1.8-.2-.3 0-.4.1-.6l.4-.5.3-.4c.1-.2 0-.4 0-.5l-.9-2.2c-.2-.5-.5-.5-.7-.5z"/></svg>'
ARW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
ARWL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M11 6l-6 6 6 6"/></svg>'
MAIL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 7l8.5 6 8.5-6"/></svg>'
IGI = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.2" cy="6.8" r=".6" fill="currentColor"/></svg>'
TEL = T('(+57) 301 512 39 91', '(+57) 300 002 71 15')
IGH = T('@institutoclinicodelongevidad', '@longevityclinicalinstitute')
MAILA = 'carolina_md@longevityclinicalinstitute.com'

NAV = [('#metodo', 'Evaluación', 'Assessment'), ('#ciencia', 'Ciencia', 'Science'), ('#equipo', 'Equipo', 'Team'),
       ('#clinica', 'La clínica', 'The clinic'), ('#agenda', 'Contacto', 'Contact')]
nav = ''.join(f'<a href="{h}">{T(a, b)}</a>' for h, a, b in NAV)
mnav = ''.join(f'<li><a href="{h}">{T(a, b)}</a></li>' for h, a, b in NAV)

LANG = ('<div class="lang" role="group" aria-label="Idioma / Language">'
        '<button type="button" data-setlang="es" aria-pressed="true">ES</button>'
        '<button type="button" data-setlang="en" aria-pressed="false">EN</button></div>')

# ---- marquee ----
mq_items = [('2 h+', T('Primera consulta: mediciones y evaluación médica', 'First visit: measurements and medical evaluation')),
            ('48 h', T('Órdenes y fórmulas tras la consulta', 'Orders and formulations after your visit')),
            ('~10', T('Días en protocolos presenciales, según el protocolo', 'Days in in-person protocols, depending on the protocol')),
            ('ES · EN', T('Equipo y atención bilingües', 'Bilingual team and care')),
            ('In house', T('Muestras procesadas en Colombia y en laboratorios de EE. UU.', 'Samples processed in Colombia and in U.S. laboratories')),
            ('IA', T('Clínica propia, siempre revisada por el médico', 'Our own clinical AI, always reviewed by the physician'))]
mq_one = '<div>' + '<i></i>'.join(f'<span><b>{n}</b>{t}</span>' for n, t in mq_items) + '<i></i></div>'
MQ = mq_one + mq_one

# ---- chapters ----
steps = [
    (T('Medición clínica', 'Clinical measurement'),
     T('Mediciones y muestras procesadas in house, en Colombia y en laboratorios especializados de EE. UU.', 'Measurements and samples processed in house, in Colombia and in specialized U.S. laboratories.')),
    (T('Evaluación médica', 'Medical evaluation'),
     T('Una primera consulta de mínimo 2 horas reúne las mediciones y la evaluación médica. Hay modalidades más largas.', 'A first visit of at least 2 hours brings together the measurements and the medical evaluation. Longer formats are available.')),
    (T('Interpretación con IA clínica', 'Clinical AI interpretation'),
     T('IA clínica propia, siempre revisada por el médico, con pruebas neurocognitivas propias.', 'Our own clinical AI, always reviewed by the physician, with our own neurocognitive tests.')),
    (T('Plan personalizado', 'Personalized plan'),
     T('Según lo que tu caso necesita. Órdenes y fórmulas dentro de las 48 horas siguientes a la consulta.', 'Based on what your case needs. Orders and formulations within 48 hours of your visit.')),
]
STEPS = ''.join(
    f'<div class="step"><div class="k">{T("Paso", "Step")} 0{i+1} / 04</div><h3>{h}</h3><p>{p}</p><div class="mph m{i}" role="img" aria-label=""></div></div>'
    for i, (h, p) in enumerate(steps))
PH = ''.join(f'<div class="ph p{i}"></div>' for i in range(4))

# ---- orbit ----
import math
orbit = [
    (T('Edad biológica', 'Biological age'), T('Estimados preliminares calculados con varios relojes biológicos.', 'Preliminary estimates calculated with several biological clocks.')),
    (T('Salud cognitiva', 'Cognitive health'), T('Pruebas neurocognitivas propias, parte de la evaluación.', 'Our own neurocognitive tests, part of the evaluation.')),
    (T('Laboratorio', 'Laboratory'), T('Muestras procesadas in house, en Colombia y en laboratorios especializados de EE. UU.', 'Samples processed in house, in Colombia and in specialized U.S. laboratories.')),
    (T('IA clínica', 'Clinical AI'), T('IA clínica propia para interpretar resultados, siempre revisada por el médico.', 'Our own clinical AI to interpret results, always reviewed by the physician.')),
    (T('Plan personalizado', 'Personalized plan'), T('Según lo que tu caso necesita. Órdenes y fórmulas dentro de 48 horas tras la consulta.', 'Based on what your case needs. Orders and formulations within 48 hours of your visit.')),
    (T('Protocolos presenciales', 'In-person protocols'), T('Hasta ~10 días, según el protocolo. El costo estimado se da cuando hay resultados, al definir para qué terapias eres candidato.', 'Up to ~10 days, depending on the protocol. The estimated cost is given once results are in, when we define which therapies you are a candidate for.')),
]
ang = [-90, -30, 30, 90, 150, 210]
NODES = ''; PDS = ''
for i, ((t, d), a) in enumerate(zip(orbit, ang)):
    x = 50 + 36 * math.cos(math.radians(a)); y = 50 + 36 * math.sin(math.radians(a))
    NODES += f'<button type="button" class="node" data-x="{x:.1f}" data-y="{y:.1f}" style="left:{x:.1f}%;top:{y:.1f}%" aria-pressed="false"><s></s><span>{t}</span></button>'
    PDS += f'<div class="pd"><div class="n">0{i+1}</div><h3>{t}</h3><p>{d}</p></div>'

# ---- gallery ----
gal = [('s1', 't', T('Sala de terapias', 'Therapy room')), ('s2', 't', T('Sala de medición', 'Measurement room')),
       ('s4', 'wd', T('Salas de terapia', 'Therapy rooms')), ('s3', 't', T('Consultorio', 'Consulting room')),
       ('s5', 't', T('Pasillo', 'Hallway')), ('s6', 'wd', T('Sala de espera', 'Waiting room')), ('s7', 't', T('Descanso', 'Rest'))]
GAL = ''.join(f'<figure class="slide {k} {w}" style="margin:0"><div class="im"></div><figcaption><b>{c}</b><span>LCI · Medellín</span></figcaption></figure>' for k, w, c in gal)

BOOK = f'''<div class="book" data-book>
  <div class="tp"><h3>{T('Reserva en línea', 'Book online')}</h3><span class="mk">{T('Widget de ejemplo · EnfoRisk + Cognimed AI por definir', 'Sample widget · EnfoRisk + Cognimed AI to be defined')}</span></div>
  <span class="lb">{T('Tipo de consulta', 'Visit type')}</span>
  <div class="opts" data-group><button type="button" class="opt" aria-pressed="true">{T('Primera consulta', 'First visit')}</button><button type="button" class="opt" aria-pressed="false">{T('Seguimiento', 'Follow-up')}</button><button type="button" class="opt" aria-pressed="false">{T('Paciente internacional', 'International patient')}</button></div>
  <span class="lb">{T('Idioma', 'Language')}</span>
  <div class="opts" data-group><button type="button" class="opt" aria-pressed="true">Español</button><button type="button" class="opt" aria-pressed="false">English</button></div>
  <span class="lb">{T('Fecha (disponibilidad de ejemplo)', 'Date (sample availability)')}</span>
  <div class="days" data-group>
    <button type="button" class="day" aria-pressed="false"><small>{T('Lun', 'Mon')}</small>3</button>
    <button type="button" class="day" aria-pressed="true"><small>{T('Mar', 'Tue')}</small>4</button>
    <button type="button" class="day" aria-pressed="false"><small>{T('Mié', 'Wed')}</small>5</button>
    <button type="button" class="day" disabled><small>{T('Jue', 'Thu')}</small>6</button>
    <button type="button" class="day" aria-pressed="false"><small>{T('Vie', 'Fri')}</small>7</button></div>
  <button type="button" class="btn navy" data-mag>{T('Continuar', 'Continue')} {ARW}</button>
  <p class="fine">{T('La primera consulta dura mínimo 2 horas.', 'The first visit lasts at least 2 hours.')}</p></div>'''


import json as _json
_FR=[]  # sin video: escena de células madre provisional hasta recibir el clip nuevo
FRAMES=_json.dumps(['data:image/jpeg;base64,'+b64(open(f,'rb').read()) for f in _FR])

import json as _j
_TOUR_ROOMS=[
 dict(k='noche',es='Sala de terapias',en='Therapy room',ces='Un espacio de descanso con vista a Medellín.',cen='A resting space with a view of Medellín.',hs=[dict(u=.51,v=.54,to='adn')]),
 dict(k='adn',es='Sala de medición',en='Measurement room',ces='Mediciones de grado clínico.',cen='Clinical-grade measurements.',hs=[dict(u=.51,v=.54,to='consul'),dict(u=.29,v=.58,to='noche')]),
 dict(k='consul',es='Consultorio',en='Consulting room',ces='Evaluación médica en una primera consulta de mínimo 2 horas.',cen='Medical evaluation in a first visit of at least 2 hours.',hs=[dict(u=.51,v=.54,to='hall'),dict(u=.29,v=.58,to='adn')]),
 dict(k='hall',es='Pasillo',en='Hallway',ces='Cada espacio, pensado alrededor del paciente.',cen='Every space, designed around the patient.',hs=[dict(u=.47,v=.47,to='espera'),dict(u=.29,v=.58,to='consul')]),
 dict(k='espera',es='Sala de espera',en='Waiting room',ces='Atención bilingüe en español e inglés.',cen='Bilingual care in Spanish and English.',hs=[dict(u=.36,v=.52,to='hall')]),
]
_names={r['k']:r for r in _TOUR_ROOMS}
for r in _TOUR_ROOMS:
    r['src']=IMGS[r['k']]
    for h in r['hs']: h['les']=_names[h['to']]['es']; h['len']=_names[h['to']]['en']
TOURJSON=_j.dumps(dict(rooms=_TOUR_ROOMS),ensure_ascii=False)
TOUR = f"""<section class="tour" id="clinica" aria-label="{A('Recorrido por la clínica', 'Clinic walkthrough')}"><canvas id="tourgl" aria-hidden="true"></canvas><div id="hots"></div>
<div class="thead"><div class="eyebrow">{T('La clínica', 'The clinic')}</div><h2 class="mag rv">{T('<span class="mg1">Recorre la</span><span class="mg2"><em>clínica</em></span>', '<span class="mg1">Walk through the</span><span class="mg2"><em>clinic</em></span>')}</h2><p class="tip">{T('Arrastra para mirar · toca los puntos para avanzar', 'Drag to look around · tap the dots to move')}</p></div>
<ol class="tlist" id="tlist"></ol><p class="tcap" id="tcap"></p>
<script type="application/json" id="tourdata">{TOURJSON}</script></section>"""

CINE = f"""<section class="cine" id="top" aria-label="{A('Bienvenida', 'Welcome')}"><div class="cstk">
  <div class="shot s1"></div><div class="shot s2"></div><div class="shot s3"></div><div class="shot s4"></div><div class="cveil"></div>
  <div class="cinein"><div class="eyebrow">THE MEDICINE OF THE FUTURE.</div>
    <h1>{T('<span class="k1">Más años</span><span class="k2"><em>saludables</em>,</span><span class="k3">diseñados desde tu <em class="k4">biología</em>.</span>', '<span class="k1">More</span><span class="k2"><em>healthy</em></span><span class="k3">years, designed around your <em class="k4">biology</em>.</span>')}</h1>
    <p class="lead">{T('Medicina de precisión: medición de grado clínico, evidencia científica rigurosa y una atención diseñada alrededor de tu biología.', 'Precision medicine: clinical-grade measurement, rigorous scientific evidence and care designed around your biology.')}</p>
    <p class="micro">{T('Medellín, Colombia · Atención bilingüe', 'Medellín, Colombia · Bilingual care')}</p></div>
  <p class="ccap">{T('Mediciones de <em>grado clínico</em>', '<em>Clinical-grade</em> measurements')}</p>
  <p class="ccap">{T('Una primera consulta de <em>mínimo 2 horas</em>', 'A first visit of <em>at least 2 hours</em>')}</p>
  <p class="ccap">{T('IA clínica propia, <em>revisada por el médico</em>', 'Our own clinical AI, <em>reviewed by the physician</em>')}</p>
  <p class="ccap">{T('Un plan <em>hecho a tu medida</em>', 'A plan <em>built around you</em>')}</p>
  <div class="cprog" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
  <div class="cue" aria-hidden="true">{T('Desplaza', 'Scroll')}<i></i></div>
  <div class="cend"><span class="logo w cl" role="img" aria-label="Longevity Clinical Institute"></span><p>{T('Agenda tu valoración', 'Schedule your assessment')}</p>
    <a class="btn cream" href="#agenda" data-mag>{T('Agendar valoración', 'Book an assessment')} {ARW}</a><span class="ct">{TEL}</span></div>
</div></section>
"""

STAR = '<svg class="st" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 1l2.6 8.4L23 12l-8.4 2.6L12 23l-2.6-8.4L1 12l8.4-2.6z" fill="currentColor"/></svg>'
DIVE = f'''<section class="dive" id="inmersion" aria-label="{A('Inmersión', 'Immersion')}"><div class="stk"><div class="win"><canvas id="cells" aria-hidden="true"></canvas><script type="application/json" id="zframes">{FRAMES}</script><div class="vg"></div>
  <p class="beat">{T('Medición de <em>grado clínico</em>', '<em>Clinical-grade</em> measurement')}</p>
  <p class="beat">{T('Evidencia científica <em>rigurosa</em>', '<em>Rigorous</em> scientific evidence')}</p>
  <p class="beat">{T('Atención diseñada alrededor de tu <em>biología</em>', 'Care designed around your <em>biology</em>')}</p>
  <span class="ill">{T('Ilustración · células madre y exosomas', 'Illustration · stem cells and exosomes')}</span></div>
  <div class="cap"><div class="eyebrow">{T('Entra', 'Step inside')}</div><h2 class="mag">{T('<span class="mg1">Todo empieza en tu</span><span class="mg2"><em>biología</em></span>', '<span class="mg1">It all starts in your</span><span class="mg2"><em>biology</em></span>')}</h2></div>
  <div class="chip">{T('Desplaza para sumergirte', 'Scroll to dive in')}<i></i></div></div></section>
'''
RINGS = f'''<section class="rings-s" id="edad"><div class="rg" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i><div class="core"><b></b></div></div>
  <div class="in"><div class="eyebrow">{T('Edad biológica', 'Biological age')}</div>
  <h2 class="rv">{T('Estimados preliminares con <em>varios relojes biológicos</em>', 'Preliminary estimates from <em>several biological clocks</em>')}</h2>
  <p class="s">{T('Parte de la evaluación de longevidad, interpretada con IA clínica y revisada por el médico.', 'Part of the longevity assessment, interpreted with clinical AI and reviewed by the physician.')}</p></div></section>
'''
_G = f'<div class="g"><span>LONGEVITY</span>{STAR}<span class="o">MEDELLÍN</span>{STAR}</div>'
BIG = f'<section class="bigmq" aria-hidden="true"><div class="tr">{_G*4}</div></section>\n'

BODY = f'''<div class="prog" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>
<div class="intro" id="intro" aria-hidden="true"><div class="ibg"></div><div class="iw" id="iw"><span class="il" id="il"></span><span class="ish"></span></div></div>
<header class="top"><div class="in">
  <a href="#top" aria-label="Longevity Clinical Institute"><span class="logo w" role="img" aria-label="Longevity Clinical Institute"></span></a>
  <nav class="nav" aria-label="Principal">{nav}</nav>
  <div class="rt">{LANG}<a class="btn cream sm" href="#agenda" data-mag>{T('Agendar valoración', 'Book an assessment')}</a>
  <button class="burger" type="button" aria-label="Menú / Menu" aria-expanded="false"><i></i><i></i></button></div></div></header>
<div class="mnav"><div class="mt"><span class="logo w" role="img" aria-label="Longevity Clinical Institute"></span><button class="mclose" type="button" aria-label="Cerrar / Close">×</button></div><ul>{mnav}</ul><div class="ft">{LANG}<a class="btn cream" href="#agenda">{T('Agendar valoración', 'Book an assessment')}</a></div></div>

<main>
{CINE}


{DIVE}<section class="chap" id="metodo"><div class="in">
  <div class="head rv"><div class="eyebrow">{T('Cómo trabajamos', 'How we work')}</div>
  <h2 class="h2">{T('Medición, ciencia y un plan <em>hecho a tu medida</em>', 'Measurement, science and a plan <em>built around you</em>')}</h2></div>
  <div class="cgrid">
    <div class="vis" data-i="0"><svg class="rings" viewBox="-300 -300 600 600" aria-hidden="true"><g><circle class="r0" r="292"/></g><g><circle class="r1" r="262"/></g><g><circle class="r2" r="232"/></g><g><circle class="r3" r="202"/></g></svg>
      <div class="archwrap">{PH}</div><div class="vnum"><b>01</b><small>/ 04</small></div></div>
    <div class="steps">{STEPS}</div>
  </div></div></section>

{RINGS}<section class="const" id="ciencia"><div class="in">
  <div class="eyebrow">{T('Ciencia y tecnología', 'Science and technology')}</div>
  <h2 class="h2 rv" style="margin-top:20px;max-width:12em">{T('Lo que medimos y <em>cómo lo interpretamos</em>', 'What we measure and <em>how we read it</em>')}</h2>
  <div class="cwrap">
    <div class="cbox"><canvas id="orbit" aria-hidden="true"></canvas><div class="hub"><i role="img" aria-label="LCI"></i></div>{NODES}</div>
    <div class="panel" aria-live="polite">{PDS}<p class="src">{T('Explora cada punto de la evaluación.', 'Explore each point of the assessment.')}</p></div>
  </div></div></section>

<section class="mis" aria-label="{A('Misión', 'Mission')}"><div class="in">
  <p class="eyebrow" style="margin-bottom:34px">{T('Misión', 'Mission')}</p>
  <p class="scrub">{T('<span>Dar a cada paciente más años saludables mediante la medicina de precisión: medición de grado clínico, evidencia científica rigurosa y una atención diseñada alrededor de su biología.</span>', '')}{T('', '<span>To give every patient more healthy years through precision medicine: clinical-grade measurement, rigorous scientific evidence and care designed around their biology.</span>')}</p>
  <div class="by"><i></i>Longevity Clinical Institute</div></div></section>

<section class="dra" id="equipo"><div class="in dgrid">
  <div class="tilt"><div class="portrait" role="img" aria-label="Dra. Carolina Rodríguez Morales"></div></div>
  <div><div class="eyebrow">{T('Dirección médica', 'Medical direction')}</div>
  <h2 class="rv">Dra. Carolina <em>Rodríguez Morales</em></h2>
  <div class="role">Founder &amp; CEO · Medical Doctor</div>
  <p class="s">{T('Especialista en Medicina Funcional, Regenerativa y de Longevidad.', 'Specialist in Functional, Regenerative and Longevity Medicine.')}</p>
  <div class="facts">
    <div><b style="font-size:clamp(28px,2.6vw,38px)">{T('Funcional', 'Functional')}</b><span>{T('Medicina Funcional', 'Functional Medicine')}</span></div>
    <div><b style="font-size:clamp(28px,2.6vw,38px)">{T('Regenerativa', 'Regenerative')}</b><span>{T('Medicina Regenerativa', 'Regenerative Medicine')}</span></div>
    <div><b style="font-size:clamp(28px,2.6vw,38px)">{T('Longevidad', 'Longevity')}</b><span>{T('Medicina de Longevidad', 'Longevity Medicine')}</span></div>
    <div><b style="font-size:clamp(28px,2.6vw,38px)">LAI</b><span>{T('Cofundadora, Longevity Academic Institute', 'Co-founder, Longevity Academic Institute')}</span></div></div>
  <a class="btn navy" href="#agenda" data-mag>{T('Agendar con la Dra.', 'Book with the doctor')} {ARW}</a></div></div></section>

{TOUR}

<section class="trav"><div class="bg" aria-hidden="true"></div><div class="in"><div class="box">
  <div class="eyebrow">{T('Pacientes internacionales', 'International patients')}</div>
  <h2 class="h2 rv">{T('Pensado también para quien <em>viaja a Medellín</em>', 'Also designed for patients <em>who travel to Medellín</em>')}</h2>
  <p class="lead">{T('Recogida en el aeropuerto, hotel y transporte organizados por el equipo, que está pendiente de ti durante tu estadía. Atención bilingüe en inglés y español.', 'Airport pickup, hotel and transportation arranged by our team, who stay in touch with you throughout your stay. Care in English and Spanish.')}</p>
  <div class="chips"><span class="pill">{T('Aeropuerto', 'Airport')}</span><span class="pill">Hotel</span><span class="pill">{T('Transporte', 'Transportation')}</span><span class="pill">English · Español</span></div></div></div></section>

<section class="agenda" id="agenda"><div class="in agrid"><div>
  <div class="eyebrow">{T('Agenda', 'Schedule')}</div>
  <h2 class="h2 rv">{T('Agenda tu <em>valoración</em>', 'Schedule your <em>assessment</em>')}</h2>
  <p class="lead">{T('Escríbenos por WhatsApp o reserva en línea. Te confirmamos el horario y lo que necesitas para tu primera consulta.', 'Message us on WhatsApp or book online. We confirm your time slot and what you need for your first visit.')}</p>
  <div class="cinfo"><div class="tel">{WA}<span>{TEL}</span></div><div>{MAIL}<span>{MAILA}</span></div><div>{IGI}<span>{IGH}</span></div></div></div>
  {BOOK}</div></section>
</main>

<footer class="ftr"><div class="in"><div class="fg">
  <div><span class="logo w" role="img" aria-label="Longevity Clinical Institute"></span><p class="tg">THE MEDICINE OF THE FUTURE.</p></div>
  <div><h4>{T('Navegación', 'Navigate')}</h4><ul>{''.join(f'<li><a href="{h}">{T(a, b)}</a></li>' for h, a, b in NAV)}</ul></div>
  <div><h4>{T('Contacto', 'Contact')}</h4><ul><li>{TEL}</li><li>{MAILA}</li><li>{IGH}</li><li>longevityclinicalinstitute.com</li></ul></div>
  <div><h4>{T('Ubicación', 'Location')}</h4><ul><li>Medellín, Colombia</li><li>{T('Atención en español e inglés', 'Care in English and Spanish')}</li></ul></div></div>
  <div class="bot"><span>© 2026 Longevity Clinical Institute</span>
  <span>{T('Contenido informativo. No reemplaza la consulta médica.', 'Informational content. It does not replace a medical consultation.')}</span>
  <span>{T('Mockup de dirección visual: fotos del banco LCI (varias generadas con IA) y widget de reserva de ejemplo.', 'Visual direction mockup: LCI photo bank (several AI-generated) and a sample booking widget.')}</span></div><div class="wmk rv" aria-hidden="true">Longevity</div></footer>
<div class="sticky"><a class="btn cream" href="#agenda">{T('Agendar valoración', 'Book an assessment')}</a><a class="wa" href="#agenda" aria-label="WhatsApp">{WA}</a></div>'''

HTML = f'''<title>LCI Web Inmersiva</title>
<meta name="claude:viewport-fit-sides" content="cover">
<script>document.documentElement.classList.add("js-intro");setTimeout(function(){{document.documentElement.classList.remove("js-intro");var i=document.getElementById("intro");if(i)i.style.display="none"}},8000)</script>
<style>
{css}
</style>
{BODY}
<script>
{THREEJS}
</script>
<script>
{js}
</script>
'''
open(f'{OUT}/immersive.html', 'w').write(HTML)
print('ok', round(len(HTML) / 1e6, 2), 'MB')
