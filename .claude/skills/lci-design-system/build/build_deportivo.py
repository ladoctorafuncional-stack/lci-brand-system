# -*- coding: utf-8 -*-
import os, sys; sys.path.insert(0,'/mnt/skills/user/lci-design-system/assets')
import brand as B

MAP = {k:open(fos.path.join(os.path.dirname(__file__),'map_{k}.b64').read().strip() for k in ['lower','upper','full']}

ICO = {
 'run':'<path d="M13 4a2 2 0 1 0 0-.01M9 21l3-5 2 2 1 4M6 12l3-4 4 1 3 3M14 13l3 1"/>',
 'heart':'<path d="M12 21C7 17 3 13 3 8.5 3 6 5 4 7.5 4 9.4 4 11 5 12 6.5 13 5 14.6 4 16.5 4 19 4 21 6 21 8.5 21 13 17 17 12 21z"/>',
 'dumb':'<path d="M4 9v6M7 8v8M17 8v8M20 9v6M7 12h10"/>',
 'cal':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 9h18M8 3v4M16 3v4"/>',
 'lungs':'<path d="M12 4v8M9 9c0 4-1 8-4 8-1 0-1-1-1-2 0-4 2-9 5-9M15 9c0 4 1 8 4 8 1 0 1-1 1-2 0-4-2-9-5-9"/>',
 'chart':'<path d="M4 20V4M4 20h16M8 16l3-4 3 2 4-6"/>',
 'tools':'<path d="M14 7l3-3 3 3-3 3M7 14l-4 4 3 3 4-4M14 7L7 14M10 10l4 4"/>',
 'shield':'<path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
}
def sec_ico(n): return f'<span class="sec-ico"><svg viewBox="0 0 24 24">{ICO[n]}</svg></span>'

# ---------- HERO ----------
hero = f'''
<section class="hero avoid-break">
  <div class="hero-top">
    <img class="seal" src="{B.LOGO_SEAL}">
    <div class="hero-doc"><div class="tag">Prescripción del Ejercicio<br>Medicina de Longevidad</div></div>
  </div>
  <div class="eyebrow">Programa de Reacondicionamiento Físico</div>
  <h1 style="margin-top:12px;"><span class="accent">El movimiento</span><br>es tu medicina.</h1>
  <p class="sub">No empezamos por el rendimiento. <span class="serif-it">Empezamos por reencender tu cuerpo</span>
  —paso a paso, sin lesiones y a tu ritmo— para recuperar fuerza, energía y la ligereza de moverte con gusto otra vez.</p>
  <hr class="hairline">
  <div class="patient-card">
    <div class="cell"><div class="k">Paciente</div><div class="v">Diana María Muñoz Ospina</div></div>
    <div class="cell"><div class="k">Fecha del plan</div><div class="v">3 de junio de 2026</div></div>
    <div class="cell"><div class="k">Punto de partida</div><div class="v">Sedentarismo · 48 años · 84 kg</div></div>
    <div class="cell"><div class="k">Prioridad clínica</div><div class="v">Fuerza muscular + Zona 2 + Eje HPA</div></div>
  </div>
</section>'''

# ---------- 1. EVALUACIÓN / FC ----------
def zone(n, color, name, pct, bpm, feel):
    return f'''<div class="zone"><div class="zn" style="background:{color};">{n}</div>
      <div style="flex:1;"><div class="zt">{name}</div><div class="zd">{feel}</div></div>
      <div style="text-align:right;"><div class="zt">{bpm} <span style="font-size:.7rem;color:var(--ink-soft);">bpm</span></div>
      <div class="zd">{pct}% FCmáx</div></div></div>'''

eval_html = f'''
<section class="section">
  <div class="sec-head">{sec_ico('heart')}<div class="t">Tu corazón, <span class="it">tu brújula</span></div></div>
  <p class="lead">Diana, antes de movernos definimos tus zonas seguras. Con tu edad, tu frecuencia cardíaca máxima estimada es de
  <b>175 latidos por minuto</b>. La mayor parte de tu trabajo vivirá en la <b>Zona 2</b>: ahí quemas grasa, mejoras tu insulina
  y construyes base sin agotarte —clave porque tu cuerpo aún se recupera del COVID.</p>
  <div class="card avoid-break">
    {zone(1,'#9fb2c6','Muy ligera','50–57','87–100','Calentamiento. Respiras tranquila.')}
    {zone(2,'var(--gold-deep)','Ligera · Quema de grasa ⭐','57–63','100–110','Tu zona base. Puedes conversar sin esfuerzo.')}
    {zone(3,'var(--gold)','Moderada · Aeróbica','64–76','112–133','Hablas en frases cortas. Para más adelante.')}
    {zone(4,'var(--navy-soft)','Intensa · Umbral','77–93','135–163','Aún no. La reservamos para semanas avanzadas.')}
    {zone(5,'var(--navy)','Máxima','94–100','164–175','No aplica en esta etapa.')}
  </div>
  <div class="warn avoid-break" style="border-color:var(--gold);">
    <div class="wh" style="color:var(--gold-deep);">⚠ Señales para frenar y consultarme</div>
    <ul style="color:var(--ink-soft);">
      <li>Mientras tengas sangrado uterino abundante: evita esfuerzos intensos y cargas pesadas — quédate en caminata suave y movilidad hasta tu valoración de Ginecología.</li>
      <li>Dolor en el pecho, mareo, falta de aire desproporcionada o palpitaciones.</li>
      <li>Fatiga que no mejora con el descanso (tu cuerpo post-COVID manda: si un día pide pausa, la respetamos).</li>
    </ul>
  </div>
</section>'''

# ---------- 2. FITT ----------
fitt = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('run')}<div class="t">Tu fórmula <span class="it">F.I.T.T.</span></div></div>
  <p class="lead">Cuatro variables que hacen que el ejercicio sea medicina dosificada para ti —ni de menos, ni de más.</p>
  <div class="fitt-grid">
    <div class="fitt"><div class="fl">Frecuencia</div><div class="ft">6 días</div><div class="fv">Caminata casi diaria + 3 días de fuerza + respiración diaria. 1 día de descanso activo.</div></div>
    <div class="fitt"><div class="fl">Intensidad</div><div class="ft">Zona 2</div><div class="fv">100–110 bpm · RPE 3–4/10. La "prueba del habla": debes poder conversar mientras te mueves.</div></div>
    <div class="fitt"><div class="fl">Tiempo</div><div class="ft">15→40 min</div><div class="fv">Empezamos con 15–20 min y subimos máximo 10% por semana. La fuerza, 20–30 min por sesión.</div></div>
    <div class="fitt"><div class="fl">Tipo</div><div class="ft">Fuerza + Z2</div><div class="fv">Fuerza (tu prioridad #1), caminata aeróbica, movilidad y respiración diafragmática.</div></div>
  </div>
  <div class="dark-card avoid-break" style="margin-top:18px;">
    <h3>¿Por qué la fuerza es <span class="it">tu prioridad?</span></h3>
    <p>Tienes 48 años, estás en transición perimenopáusica y vienes de un sedentarismo total: es la tormenta perfecta para
    perder músculo. Y el músculo no es estética —es tu órgano de longevidad: regula tu azúcar, sostiene tu metabolismo y
    te protege de caídas y fragilidad. Por eso, mientras bajas de peso, <strong>construir y proteger músculo es lo primero.</strong>
    Invertir hoy en músculo es invertir en tu cuerpo del futuro.</p>
  </div>
</section>'''

# ---------- 3. CALENDARIO SEMANAL ----------
def daycard(cls, tagcls, tag, name, blocks):
    return f'''<div class="day {cls} avoid-break"><div class="dh"><div class="dn">{name}</div>
      <span class="dtag {tagcls}">{tag}</span></div>{blocks}</div>'''

def ex_table(rows, prio_note=None):
    body=''.join(f'<tr><td class="exn">{a}</td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a,b,c,d in rows)
    return f'''<table class="ex-tbl"><thead><tr><th>Ejercicio</th><th>Series × Reps</th><th>Descanso</th><th>Zona / Foco</th></tr></thead><tbody>{body}</tbody></table>'''

def mapimg(k, h=170):
    return f'<img src="{MAP[k]}" style="height:{h}px;display:block;margin:10px auto 0;">'

dayA = daycard('s','tag-s','Fuerza','Lunes — Tren inferior &amp; glúteos',
  f'''<p style="font-size:.86rem;color:var(--ink-soft);margin-bottom:10px;">Calentamiento 5 min (marcha en el sitio + movilidad de cadera y tobillo). Luego:</p>
  {ex_table([
    ('Sentadilla a la silla','2 × 10','60 s','Cuádriceps · glúteo'),
    ('Puente de glúteo en piso','2 × 12','45 s','Glúteo · isquiotibial'),
    ('Zancada estática asistida (apoyo en silla)','2 × 8 c/pierna','60 s','Cuádriceps · glúteo'),
    ('Abducción de cadera con banda elástica','2 × 12','45 s','Glúteo medio'),
    ('Elevación de talones de pie','2 × 15','40 s','Pantorrilla'),
  ])}
  <p style="font-size:.84rem;color:var(--ink-soft);margin-top:8px;">Enfriamiento 5 min: estiramiento de cuádriceps, glúteo y pantorrilla + 15 min de caminata suave en Zona 2.</p>
  {mapimg('lower')}''')

dayB = daycard('s','tag-s','Fuerza','Miércoles — Tren superior &amp; core',
  f'''<p style="font-size:.86rem;color:var(--ink-soft);margin-bottom:10px;">Calentamiento 5 min (círculos de brazos + movilidad de columna). Luego:</p>
  {ex_table([
    ('Flexión de brazos contra la pared / inclinada','2 × 10','60 s','Pecho · tríceps'),
    ('Remo con banda elástica sentada','2 × 12','45 s','Espalda · bíceps'),
    ('Press de hombro con mancuernas ligeras','2 × 10','60 s','Deltoides'),
    ('Curl de bíceps con banda','2 × 12','40 s','Bíceps'),
    ('Plancha sobre rodillas (anti-extensión)','2 × 20 s','45 s','Core'),
    ('Dead bug (anti-rotación)','2 × 8 c/lado','45 s','Core profundo'),
  ])}
  <p style="font-size:.84rem;color:var(--ink-soft);margin-top:8px;">Enfriamiento 5 min: estiramiento de pecho, espalda y cuello + 15 min de caminata suave.</p>
  {mapimg('upper')}''')

dayC = daycard('s','tag-s','Fuerza','Viernes — Cuerpo completo funcional',
  f'''<p style="font-size:.86rem;color:var(--ink-soft);margin-bottom:10px;">Calentamiento 5 min. Circuito funcional de patrones básicos de la vida diaria:</p>
  {ex_table([
    ('Peso muerto rumano con mancuernas ligeras','2 × 10','60 s','Glúteo · isquiotibial · espalda baja'),
    ('Sentadilla goblet ligera','2 × 10','60 s','Cuádriceps · glúteo'),
    ('Remo inclinado con banda','2 × 12','45 s','Espalda'),
    ('Press de hombro de pie','2 × 10','45 s','Deltoides'),
    ('Bird-dog','2 × 8 c/lado','45 s','Core · estabilidad'),
    ('Marcha en el sitio con rodillas altas','2 × 30 s','45 s','Cardio · core'),
  ])}
  <p style="font-size:.84rem;color:var(--ink-soft);margin-top:8px;">Enfriamiento 5 min de estiramiento general + 15 min de caminata.</p>
  {mapimg('full')}''')

cardio_days = f'''
  {daycard('c','tag-c','Cardio','Martes — Caminata base',
    '<p style="font-size:.88rem;color:var(--ink-soft);">20 minutos de caminata en Zona 2 (100–110 bpm), preferiblemente en la mañana para encender tu energía y regular tu reloj biológico. Termina con 5 min de movilidad articular.</p>')}
  {daycard('c','tag-c','Cardio','Jueves — Caminata + respiración',
    '<p style="font-size:.88rem;color:var(--ink-soft);">25 minutos de caminata en Zona 2. Al volver, 10 minutos de respiración diafragmática para bajar el cortisol y cerrar el día activo con calma.</p>')}
  {daycard('f','tag-f','Movilidad','Sábado — Caminata larga al aire libre',
    '<p style="font-size:.88rem;color:var(--ink-soft);">30 minutos de caminata disfrutona por San Vicente —busca una ruta con naturaleza. Cierra con 10 min de estiramiento completo. El movimiento al aire libre también es medicina para tu ánimo.</p>')}
  {daycard('r','tag-r','Descanso','Domingo — Descanso activo',
    '<p style="font-size:.88rem;color:var(--ink-soft);">Nada de entrenamiento estructurado. Movilidad muy suave, una caminata corta y placentera si te provoca, y respiración. Descansar también es parte del plan: aquí tu cuerpo se reconstruye.</p>')}
'''

calendario = f'''
<section class="section">
  <div class="sec-head">{sec_ico('cal')}<div class="t">Tu semana <span class="it">de movimiento</span></div></div>
  <p class="lead">Una estructura simple y repetible. Tres días de fuerza intercalados con caminata, y un domingo para recuperar.
  Los mapas muestran los músculos que activas cada día de fuerza.</p>
  {dayA}{cardio_days.split(chr(10))[0]}
  {daycard('c','tag-c','Cardio','Martes — Caminata base','<p style="font-size:.88rem;color:var(--ink-soft);">20 minutos de caminata en Zona 2 (100–110 bpm), preferiblemente en la mañana para encender tu energía y regular tu reloj biológico. Termina con 5 min de movilidad articular.</p>')}
  {dayB}
  {daycard('c','tag-c','Cardio','Jueves — Caminata + respiración','<p style="font-size:.88rem;color:var(--ink-soft);">25 minutos de caminata en Zona 2. Al volver, 10 minutos de respiración diafragmática para bajar el cortisol y cerrar el día activo con calma.</p>')}
  {dayC}
  {daycard('f','tag-f','Movilidad','Sábado — Caminata larga al aire libre','<p style="font-size:.88rem;color:var(--ink-soft);">30 minutos de caminata disfrutona por San Vicente —busca una ruta con naturaleza. Cierra con 10 min de estiramiento completo. El movimiento al aire libre también es medicina para tu ánimo.</p>')}
  {daycard('r','tag-r','Descanso','Domingo — Descanso activo','<p style="font-size:.88rem;color:var(--ink-soft);">Nada de entrenamiento estructurado. Movilidad muy suave, una caminata corta y placentera si te provoca, y respiración. Descansar también es parte del plan: aquí tu cuerpo se reconstruye.</p>')}
</section>'''

# ---------- 4. PROGRESIÓN 12 SEMANAS ----------
prog_rows = [
 ('1–2','Caminata 15–20 min · Zona 1–2','Fuerza 2 días · 2×10–12 · solo peso corporal','Aprender la técnica. Sin dolor, sin afán.'),
 ('3–4','Caminata 20–25 min · Zona 2','Fuerza 2–3 días · 2×12 · añadir banda elástica','Crear el hábito. Tu cuerpo empieza a pedir movimiento.'),
 ('5–6','Caminata 25–30 min · Zona 2','Fuerza 3 días · 2–3×12 · mancuernas ligeras (1–3 kg)','Notarás más energía y menos somnolencia tras el almuerzo.'),
 ('7–8','Caminata 30 min + intervalos suaves Z2–3','Fuerza 3 días · 3×12 · subir carga gradual','El músculo responde. La ropa empieza a sentirse distinta.'),
 ('9–10','Caminata 35 min · Zona 2–3','Fuerza 3 días · 3×12 · nuevos patrones','Mayor fuerza funcional para tu día a día.'),
 ('11–12','Caminata 40 min + tramos en Zona 3','Fuerza 3 días · 3×12–15 · reevaluación','Reevaluamos peso, fuerza y energía. Definimos la siguiente fase.'),
]
prog = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('chart')}<div class="t">Tu progresión a <span class="it">12 semanas</span></div></div>
  <p class="lead">Subimos de a poco —regla de oro: nunca más del 10% por semana, y nunca volumen e intensidad al tiempo.
  Esto protege tus articulaciones y respeta tu recuperación.</p>
  <table class="avoid-break"><thead><tr><th>Semana</th><th>Cardio</th><th>Fuerza</th><th>Qué vas a sentir</th></tr></thead>
  <tbody>{''.join(f'<tr><td class="daycol" style="text-align:center;">{a}</td><td>{b}</td><td>{c}</td><td style="font-style:italic;color:var(--ink-soft);">{d}</td></tr>' for a,b,c,d in prog_rows)}</tbody></table>
</section>'''

# ---------- 5. PAUSAS ACTIVAS + RESPIRACIÓN ----------
def ring(svg, lbl):
    return f'<div><div class="ring"><svg viewBox="0 0 24 24">{svg}</svg></div><div class="lbl">{lbl}</div></div>'

pausas = f'''
<section class="dark-section avoid-break">
  <div class="sec-head"><span class="sec-ico"><svg viewBox="0 0 24 24">{ICO['lungs']}</svg></span><div class="t">Rompe el <span class="it">sedentarismo</span></div></div>
  <p class="lead">Como pasas mucho tiempo en casa, tu enemigo silencioso es estar sentada horas seguidas. Cada hora, levántate
  y haz una micro-pausa de 2 minutos. Tu metabolismo y tu glucosa te lo agradecen.</p>
  <div style="background:#fff;border-radius:16px;padding:26px;">
    <div class="ring-row">
      {ring(ICO['run'],'Marcha en el sitio<br>2 minutos')}
      {ring(ICO['dumb'],'5 sentadillas<br>a la silla')}
      {ring('<path d="M12 4v16M6 8l6-4 6 4"/>','Estira brazos<br>al techo')}
      {ring(ICO['lungs'],'3 respiraciones<br>profundas')}
    </div>
    <div class="pill-quote">El movimiento es una inversión para tu salud.</div>
  </div>
  <div class="dark-card avoid-break" style="margin-top:18px;">
    <h3>Tu respiración diafragmática <span class="it">— 10 minutos</span></h3>
    <p>Tu doctora te la recetó por algo: regula tu eje del estrés (HPA), baja el cortisol que favorece la grasa abdominal y
    mejora tu sueño. Hazla 1 vez al día, idealmente en la noche:</p>
    <ol style="margin-top:10px;padding-left:18px;font-weight:300;">
      <li style="margin:5px 0;">Siéntate o acuéstate cómoda. Una mano en el pecho, otra en el abdomen.</li>
      <li style="margin:5px 0;">Inhala por la nariz 4 segundos llevando el aire al abdomen (la mano de abajo sube, la de arriba casi no).</li>
      <li style="margin:5px 0;">Retén 4 segundos. Exhala lento por la boca 6 segundos.</li>
      <li style="margin:5px 0;">Repite durante 10 minutos. Suma tu oración aquí si te conecta.</li>
    </ol>
  </div>
</section>'''

# ---------- 6. EQUIPO + TECNOLOGÍA ----------
def eq(name, desc):
    return f'''<div class="card" style="border-left:5px solid var(--gold);padding:18px 20px;">
      <div style="font-family:'Mencken Std',serif;font-weight:700;color:var(--navy);">{name}</div>
      <p style="font-size:.85rem;color:var(--ink-soft);margin-top:3px;">{desc}</p></div>'''

equipo = f'''
<section class="section">
  <div class="sec-head">{sec_ico('tools')}<div class="t">Tu equipo <span class="it">para casa</span></div></div>
  <p class="lead">No necesitas un gimnasio. Con esto entrenas completo desde tu sala:</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;">
    {eq('Banda elástica de resistencia','Tu "máquina" portátil para remo, glúteo y hombro. Económica y muy versátil.')}
    {eq('Par de mancuernas ligeras (1–3 kg)','Para progresar la fuerza de forma segura. Empieza liviano.')}
    {eq('Colchoneta','Para el trabajo de piso: puente de glúteo, plancha, dead bug, estiramientos.')}
    {eq('Silla estable','Tu asistente para sentadillas a la silla y zancadas asistidas.')}
    {eq('Banda o reloj con frecuencia cardíaca','Para vivir en tu Zona 2 sin adivinar. Un smartwatch o banda de pecho funciona perfecto.')}
    {eq('App de pasos / caminata','Meta inicial: 6.000 pasos/día, subiendo a 8.000. El celular ya cuenta tus pasos.')}
  </div>
</section>'''

# ---------- 7. CONSEJOS + CITA ----------
def tip(t, body):
    return f'<div class="numitem"><div class="nc"></div><div><div class="nt">{t}</div><p style="font-weight:300;">{body}</p></div></div>'

consejos = f'''
<section class="dark-section avoid-break">
  <div class="sec-head"><span class="sec-ico"><svg viewBox="0 0 24 24">{ICO['shield']}</svg></span><div class="t">Mis consejos <span class="it">para ti, Diana</span></div></div>
  <div class="numlist" style="max-width:760px;">
    {tip('Empieza ridículamente fácil','Tu mayor riesgo no es quedarte corta: es excederte el primer día y abandonar. Si la sesión te parece "demasiado fácil", vas perfecto. La constancia le gana a la intensidad.')}
    {tip('La mañana es tu mejor momento','Mueve tu cuerpo en la mañana: ayuda a vencer esa "pereza" y aletargamiento, ordena tu reloj biológico y mejora tu energía el resto del día.')}
    {tip('Escucha tu sangrado','En los días de flujo abundante, baja a caminata suave y movilidad. Nada de cargas pesadas ni esfuerzos máximos hasta tu valoración con Ginecología. Tu seguridad va primero.')}
    {tip('La fatiga post-COVID no es pereza','Si un día tu cuerpo pide pausa real, dásela sin culpa. Recuperación no es debilidad: es parte del entrenamiento inteligente.')}
    {tip('Celebra lo no-báscula','Vas a notar mejoras antes en la energía, el sueño, la fuerza para cargar el mercado y la ropa, que en el número del peso. Esas victorias también cuentan —mucho.')}
  </div>
  <div class="quote">"No es fitness, Diana. Es medicina de longevidad. Cada caminata y cada sentadilla son un mensaje a tu cuerpo: todavía tenemos mucha vida por delante."</div>
</section>'''

body = hero + eval_html + fitt + calendario + prog + pausas + equipo + consejos + B.footer()
html = B.html_doc("Plan Deportivo · Diana María Muñoz Ospina", body)
out = "/mnt/user-data/outputs/Plan deportivo - 2026-06-03 - MUÑOZ OSPINA DIANA MARÍA.html"
open(out,'w',encoding='utf-8').write(html)
print("WROTE", out, len(html))
