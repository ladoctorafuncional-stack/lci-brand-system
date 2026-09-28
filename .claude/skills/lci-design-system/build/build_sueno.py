# -*- coding: utf-8 -*-
import os, sys; sys.path.insert(0,'/mnt/skills/user/lci-design-system/assets')
import brand as B

ICO = {
 'moon':'<path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/>',
 'sun':'<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 'coffee':'<path d="M4 8h13v5a4 4 0 0 1-4 4H8a4 4 0 0 1-4-4zM17 9h2a2.5 2.5 0 0 1 0 5h-2M7 4.5V6M10 4.5V6M13 4.5V6"/>',
 'lungs':'<path d="M12 4v8M9 9c0 4-1 8-4 8-1 0-1-1-1-2 0-4 2-9 5-9M15 9c0 4 1 8 4 8 1 0 1-1 1-2 0-4-2-9-5-9"/>',
 'brain':'<path d="M12 5a3 3 0 0 0-5.6-1.5A2.8 2.8 0 0 0 4 8a2.8 2.8 0 0 0 .5 5A2.8 2.8 0 0 0 9 16a3 3 0 0 0 3 1 3 3 0 0 0 3-1 2.8 2.8 0 0 0 4.5-3 2.8 2.8 0 0 0 .5-5 2.8 2.8 0 0 0-2.4-4.5A3 3 0 0 0 12 5zM12 5v12"/>',
 'spark':'<path d="M12 3l1.7 5.1L19 10l-5.3 1.9L12 17l-1.7-5.1L5 10l5.3-1.9z"/>',
 'bed':'<path d="M3 19v-7h18v7M3 19v2M21 19v2M3 12V8a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v4M11 11h10v1"/>',
 'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7.5V12l3 2"/>',
 'shield':'<path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
}
def sec_ico(n): return f'<span class="sec-ico"><svg viewBox="0 0 24 24">{ICO[n]}</svg></span>'

# ---------- HERO ----------
hero = f'''
<section class="hero avoid-break">
  <div class="hero-top">
    <img class="seal" src="{B.LOGO_SEAL}">
    <div class="hero-doc"><div class="tag">Higiene del Sueño &amp; Ritmo Circadiano<br>Medicina de Longevidad</div></div>
  </div>
  <div class="eyebrow">Programa de Regulación del Eje HPA</div>
  <h1 style="margin-top:12px;"><span class="accent">Dormir bien</span><br>es regenerarte.</h1>
  <p class="sub">Diana, mientras duermes tu cuerpo <span class="serif-it">repara tu memoria, ordena tus hormonas y limpia tu cerebro.</span>
  No es tiempo perdido —es tu terapia más poderosa, y la tienes gratis cada noche.</p>
  <hr class="hairline">
  <div class="patient-card">
    <div class="cell"><div class="k">Paciente</div><div class="v">Diana María Muñoz Ospina</div></div>
    <div class="cell"><div class="k">Fecha del plan</div><div class="v">3 de junio de 2026</div></div>
    <div class="cell"><div class="k">Punto de partida</div><div class="v">7 h de sueño · buena base de horario</div></div>
    <div class="cell"><div class="k">Objetivo</div><div class="v">Sueño profundo, reparador y protegido</div></div>
  </div>
</section>'''

# ---------- 1. POR QUÉ TU SUEÑO ES MEDICINA ----------
porque = f'''
<section class="section">
  <div class="sec-head">{sec_ico('moon')}<div class="t">Por qué tu sueño <span class="it">es medicina</span></div></div>
  <p class="lead">Tu sueño no es un interruptor de "apagado". Es un turno de noche activísimo donde tu cuerpo hace reparaciones
  que ningún suplemento puede igualar. Y en tu caso particular, cada una de esas reparaciones apunta directo a lo que
  estamos tratando:</p>
  <div class="bracket">
    <div class="line"></div>
    <div class="items">
      <div class="it"><span class="lead-w">Repara tu memoria y tu olfato.</span> El sueño profundo es cuando el cerebro consolida lo aprendido y activa el sistema que "lava" sus desechos. Es tu mejor aliado contra las fallas de memoria y la anosmia que te dejó el COVID.</div>
      <div class="it"><span class="lead-w">Ordena tus hormonas.</span> De noche se regulan el cortisol, la melatonina y la conversión tiroidea. Dormir bien apoya tu tiroides y suaviza el vaivén hormonal de esta etapa perimenopáusica.</div>
      <div class="it"><span class="lead-w">Controla tu azúcar y tus antojos.</span> Una sola noche mala dispara la resistencia a la insulina y multiplica el antojo de dulce del día siguiente. Dormir bien es, literalmente, parte de tu plan para bajar de peso.</div>
      <div class="it"><span class="lead-w">Recarga tu energía de verdad.</span> Esa "pereza" y aletargamiento diurno se atacan desde la raíz con noches profundas, no con más café.</div>
    </div>
  </div>
</section>'''

# ---------- 2. TU SUEÑO HOY ----------
diag = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('clock')}<div class="t">Tu sueño hoy: <span class="it">el punto de partida</span></div></div>
  <p class="lead">La buena noticia, Diana: partes de una base sólida. Ya tienes varias cosas a favor. Nuestro trabajo es proteger
  esa base y corregir un solo hábito que, en silencio, te está robando la mejor parte de tu descanso.</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;">
    <div class="card avoid-break">
      <div style="font-family:'Mencken Std',serif;font-weight:700;color:var(--gold-deep);font-size:1.15rem;margin-bottom:14px;">Lo que ya haces bien</div>
      <ul style="list-style:none;font-size:.9rem;color:var(--ink-soft);">
        <li style="padding:6px 0 6px 26px;position:relative;"><span style="position:absolute;left:0;color:var(--gold-deep);font-weight:700;">✓</span> Te acuestas a una hora estable: <b>22:00</b>.</li>
        <li style="padding:6px 0 6px 26px;position:relative;"><span style="position:absolute;left:0;color:var(--gold-deep);font-weight:700;">✓</span> Te duermes rápido: <b>15 minutos</b> de latencia.</li>
        <li style="padding:6px 0 6px 26px;position:relative;"><span style="position:absolute;left:0;color:var(--gold-deep);font-weight:700;">✓</span> Duermes <b>7 horas</b> y casi no te despiertas.</li>
        <li style="padding:6px 0 6px 26px;position:relative;"><span style="position:absolute;left:0;color:var(--gold-deep);font-weight:700;">✓</span> Sientes el sueño <b>reparador</b> al despertar.</li>
        <li style="padding:6px 0 6px 26px;position:relative;"><span style="position:absolute;left:0;color:var(--gold-deep);font-weight:700;">✓</span> Tienes un ancla preciosa: tu <b>oración</b> diaria.</li>
      </ul>
    </div>
    <div class="card avoid-break" style="border-top:4px solid var(--gold);">
      <div style="font-family:'Mencken Std',serif;font-weight:700;color:var(--navy);font-size:1.15rem;margin-bottom:14px;">Lo que vamos a corregir</div>
      <ul style="list-style:none;font-size:.9rem;color:var(--ink-soft);">
        <li style="padding:6px 0 6px 26px;position:relative;"><span style="position:absolute;left:0;color:#b35a4e;font-weight:700;">!</span> <b>Pantallas y TV encendidas hasta el momento de dormir.</b> Este es el saboteador silencioso de tu sueño profundo —lo explicamos abajo.</li>
        <li style="padding:6px 0 6px 26px;position:relative;"><span style="position:absolute;left:0;color:#b35a4e;font-weight:700;">!</span> <b>Café hasta las 19:00</b> (2 a 6 tazas al día). Aunque sientas que no te afecta, puede estarte robando profundidad sin que lo notes.</li>
        <li style="padding:6px 0 6px 26px;position:relative;"><span style="position:absolute;left:0;color:#b35a4e;font-weight:700;">!</span> <b>Somnolencia después del almuerzo:</b> señal de tu azúcar y tu energía, que también mejora con buen sueño.</li>
      </ul>
    </div>
  </div>
</section>'''

# ---------- 3. LA REGLA DE ORO ----------
regla = f'''
<section class="section">
  <div class="sec-head">{sec_ico('spark')}<div class="t">La regla de oro: <span class="it">luz fuera, melatonina dentro</span></div></div>
  <p class="lead">Si solo cambiaras una cosa de toda esta guía, que sea esta. Es la indicación central de tu prescripción y
  la de mayor impacto sobre la calidad real de tu descanso.</p>
  <div class="dark-card avoid-break">
    <h3>¿Qué pasa con la luz <span class="it">de las pantallas?</span></h3>
    <p>Tu cerebro tiene un reloj que decide cuándo liberar <strong>melatonina</strong>, la hormona que te da sueño profundo y reparador.
    Ese reloj se guía por la luz. La luz azul del televisor y el celular le grita a tu cerebro <em>"¡todavía es de día!"</em> y
    frena la melatonina justo cuando más la necesitas. Resultado: te duermes, sí —pero el sueño es más superficial y menos restaurador.</p>
  </div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:18px;">
    <div class="card avoid-break" style="border-left:5px solid var(--gold);">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <span style="width:40px;height:40px;border-radius:12px;background:linear-gradient(145deg,var(--gold-soft),var(--gold-deep));display:flex;align-items:center;justify-content:center;"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#fff" stroke-width="1.7"><path d="M2 2l20 20M9 5a9 9 0 0 1 11 8M6.5 8A9 9 0 0 0 4 13M12 17h.01"/></svg></span>
        <div style="font-family:'Mencken Std',serif;font-weight:700;color:var(--navy);font-size:1.1rem;">Pantallas fuera, 2 horas antes</div>
      </div>
      <p style="font-size:.9rem;color:var(--ink-soft);">Apaga el televisor y guarda el celular a las <b>20:00</b>. Sé que es el cambio más retador —por eso abajo te dejo
      con qué reemplazar ese rato. Tu sueño profundo lo agradecerá desde la primera semana.</p>
    </div>
    <div class="card avoid-break" style="border-left:5px solid var(--navy);">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:8px;">
        <span style="width:40px;height:40px;border-radius:12px;background:linear-gradient(145deg,var(--navy-soft),var(--navy-deep));display:flex;align-items:center;justify-content:center;"><svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="#fff" stroke-width="1.7">{ICO['moon']}</svg></span>
        <div style="font-family:'Mencken Std',serif;font-weight:700;color:var(--navy);font-size:1.1rem;">Oscuridad absoluta al dormir</div>
      </div>
      <p style="font-size:.9rem;color:var(--ink-soft);">A las <b>22:00</b>, cuarto totalmente oscuro: sin lucecitas de aparatos, sin pantallas, cortinas cerradas.
      La oscuridad total es lo que dispara los <b>pulsos de melatonina</b> que reparan tu cuerpo de noche.</p>
    </div>
  </div>
</section>'''

# ---------- 4. RITUAL NOCTURNO ----------
def step(time, title, body):
    return f'''<div style="display:grid;grid-template-columns:74px 1fr;gap:0 18px;align-items:start;margin-bottom:4px;">
      <div style="text-align:right;font-family:'Mencken Std',serif;font-weight:700;color:var(--gold-deep);font-size:1.05rem;padding-top:1px;">{time}</div>
      <div style="border-left:2px solid var(--line);padding:0 0 22px 20px;position:relative;">
        <span style="position:absolute;left:-7px;top:4px;width:12px;height:12px;border-radius:50%;background:var(--gold);box-shadow:0 0 0 3px var(--beige);"></span>
        <div style="font-weight:600;color:var(--navy);margin-bottom:2px;">{title}</div>
        <div style="font-size:.89rem;color:var(--ink-soft);">{body}</div>
      </div></div>'''

ritual = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('bed')}<div class="t">Tu ritual <span class="it">para aterrizar la noche</span></div></div>
  <p class="lead">Tu cuerpo ama la repetición. Una secuencia simple y siempre igual le avisa que se acerca la hora de soltar el día.
  Esto es lo que reemplaza la TV de la noche:</p>
  <div class="card avoid-break" style="padding-top:30px;">
    {step('20:00','Apaga las pantallas','Televisor y celular fuera. Baja las luces de la casa a algo cálido y tenue: tu cerebro empieza a fabricar melatonina.')}
    {step('20:30','Cierra el día sin pantallas','Lectura en papel, una ducha tibia, dejar lista la ropa del otro día, una conversación tranquila con tu esposo. Nada estimulante.')}
    {step('21:30','Tu ancla espiritual','Tu oración diaria —que ya practicas— es el cierre perfecto: calma la mente y le da paz al sistema nervioso antes de dormir.')}
    {step('21:45','Respiración para soltar','10 minutos de respiración diafragmática (te la explico en la siguiente sección) para bajar el tono de estrés del día.')}
    {step('22:00','A dormir, en oscuridad total','Cuarto oscuro, fresco y silencioso. Si la mente sigue activa, vuelve a la respiración: inhala, exhala, suelta.')}
  </div>
</section>'''

# ---------- 5. RESPIRACIÓN ----------
resp = f'''
<section class="section">
  <div class="sec-head">{sec_ico('lungs')}<div class="t">Respiración <span class="it">4 · 4 · 6</span></div></div>
  <p class="lead">Esta es tu herramienta para apagar el "modo alerta" y encender el "modo descanso". Al alargar la exhalación,
  activas el nervio que le dice a tu cuerpo que ya está a salvo y puede repararse. Diez minutos, prescritos en tu plan.</p>
  <div class="ring-row avoid-break">
    <div><div class="ring"><svg viewBox="0 0 24 24"><path d="M12 20V8M12 8c-2-3-6-3-6 1M12 8c2-3 6-3 6 1"/></svg></div><div class="lbl"><b>Inhala 4 seg</b><br>por la nariz, llevando el aire al abdomen</div></div>
    <div><div class="ring"><svg viewBox="0 0 24 24"><path d="M5 12h14M12 5v14"/></svg></div><div class="lbl"><b>Sostén 4 seg</b><br>suave, sin tensión</div></div>
    <div><div class="ring"><svg viewBox="0 0 24 24"><path d="M19 12H5M9 8l-4 4 4 4"/></svg></div><div class="lbl"><b>Exhala 6 seg</b><br>lento, por la boca, soltando el día</div></div>
    <div><div class="ring"><svg viewBox="0 0 24 24">{ICO['clock']}</svg></div><div class="lbl"><b>Repite 10 min</b><br>cada noche, antes de dormir</div></div>
  </div>
  <div class="pill-quote avoid-break">Mano en el pecho, mano en el abdomen: solo debe moverse la de abajo.</div>
</section>'''

# ---------- 6. CAFÉ ----------
cafe = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('coffee')}<div class="t">El café <span class="it">y tu reloj interno</span></div></div>
  <p class="lead">Tú sientes que el café de la tarde no te afecta —y es muy posible que te duermas sin problema. Pero la cafeína tiene
  un efecto silencioso: aunque te duermas, puede recortar tu sueño <b>profundo</b>, justo la fase que repara tu cerebro y tu energía.</p>
  <div class="card avoid-break">
    <p style="font-size:.93rem;color:var(--ink-soft);margin-bottom:14px;">La cafeína tarda muchas horas en irse de tu cuerpo: <b>la mitad sigue activa unas 5 a 6 horas después</b> de tomarla.
    Si tu última taza es a las 19:00, todavía hay café circulando cuando te acuestas a las 22:00.</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
      <div style="background:var(--beige);border-radius:10px;padding:16px 18px;">
        <div style="font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft);font-weight:600;">Hoy</div>
        <div style="font-family:'Mencken Std',serif;font-weight:700;color:var(--navy);font-size:1.15rem;margin:3px 0;">Hasta las 19:00</div>
        <div style="font-size:.85rem;color:var(--ink-soft);">2 a 6 tazas al día, la última en la noche.</div>
      </div>
      <div style="background:rgba(210,181,138,.18);border:1px solid var(--gold);border-radius:10px;padding:16px 18px;">
        <div style="font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--gold-deep);font-weight:600;">Hacia dónde vamos</div>
        <div style="font-family:'Mencken Std',serif;font-weight:700;color:var(--navy);font-size:1.15rem;margin:3px 0;">Última taza a las 14:00</div>
        <div style="font-size:.85rem;color:var(--ink-soft);">Disfruta tu café en la mañana y temprano en la tarde; en la noche, una aromática sin cafeína.</div>
      </div>
    </div>
    <div class="note" style="margin-top:16px;"><b>Sin drama:</b> no te pido renunciar al café que amas, solo correrlo más temprano. Tu mañana es su mejor momento
    —ahí te ayuda con la energía y no le quita nada a tu noche.</div>
  </div>
</section>'''

# ---------- 7. CIRCADIANO DÍA ----------
# Cinta circadiana 24h (SVG firma)
def circ_marker(x, label, sub, up=True):
    if up:
        return (f'<line x1="{x}" y1="70" x2="{x}" y2="46" stroke="#9fb2c6" stroke-width="1.2"/>'
                f'<circle cx="{x}" cy="46" r="3.4" fill="#D2B58A"/>'
                f'<text x="{x}" y="34" fill="#2A3649" font-family="Poppins" font-size="11" font-weight="600" text-anchor="middle">{label}</text>'
                f'<text x="{x}" y="22" fill="#55617a" font-family="Poppins" font-size="9" text-anchor="middle">{sub}</text>')
    else:
        return (f'<line x1="{x}" y1="70" x2="{x}" y2="94" stroke="#9fb2c6" stroke-width="1.2"/>'
                f'<circle cx="{x}" cy="94" r="3.4" fill="#2A3649"/>'
                f'<text x="{x}" y="110" fill="#2A3649" font-family="Poppins" font-size="11" font-weight="600" text-anchor="middle">{label}</text>'
                f'<text x="{x}" y="122" fill="#55617a" font-family="Poppins" font-size="9" text-anchor="middle">{sub}</text>')

# x para 24h sobre ancho útil 60..820 ; hora->x
def hx(h): return 60 + (h/24)*760
circ = f'''<svg viewBox="0 0 880 150" style="width:100%;height:auto;">
  <defs>
    <linearGradient id="rib" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#19222e"/><stop offset="22%" stop-color="#36445a"/>
      <stop offset="46%" stop-color="#EDE5DA"/><stop offset="62%" stop-color="#f7f1e9"/>
      <stop offset="82%" stop-color="#36445a"/><stop offset="100%" stop-color="#19222e"/>
    </linearGradient>
  </defs>
  <rect x="60" y="64" width="760" height="12" rx="6" fill="url(#rib)"/>
  <text x="60" y="142" fill="#55617a" font-family="Poppins" font-size="9" text-anchor="middle">00:00</text>
  <text x="440" y="142" fill="#55617a" font-family="Poppins" font-size="9" text-anchor="middle">12:00</text>
  <text x="820" y="142" fill="#55617a" font-family="Poppins" font-size="9" text-anchor="middle">24:00</text>
  {circ_marker(hx(6),'06:00','Despertar', True)}
  {circ_marker(hx(7),'07:00','Luz + tiroides', False)}
  {circ_marker(hx(12),'Mediodía','Movimiento', True)}
  {circ_marker(hx(14),'14:00','Último café', False)}
  {circ_marker(hx(20),'20:00','Pantallas off', True)}
  {circ_marker(hx(22),'22:00','Dormir · oscuro', False)}
</svg>'''

dia = f'''
<section class="section">
  <div class="sec-head">{sec_ico('sun')}<div class="t">Tu día también <span class="it">construye tu noche</span></div></div>
  <p class="lead">El sueño no empieza a las 22:00: empieza al amanecer. Estos gestos de día le ponen orden a tu reloj biológico
  para que la melatonina llegue puntual en la noche.</p>
  <div class="card avoid-break" style="margin-bottom:18px;">{circ}</div>
  <div class="ring-row avoid-break">
    <div><div class="ring"><svg viewBox="0 0 24 24">{ICO['sun']}</svg></div><div class="lbl"><b>Luz al despertar</b><br>10–15 min de luz natural en la mañana ancla tu reloj</div></div>
    <div><div class="ring"><svg viewBox="0 0 24 24"><path d="M13 4a2 2 0 1 0 0-.01M9 21l3-5 2 2 1 4M6 12l3-4 4 1 3 3"/></svg></div><div class="lbl"><b>Muévete temprano</b><br>tu caminata matutina mejora la noche</div></div>
    <div><div class="ring"><svg viewBox="0 0 24 24"><path d="M5 12h14M5 12a7 7 0 0 1 14 0M9 5l1-2M14 5l1-2"/></svg></div><div class="lbl"><b>Cena ligera y temprano</b><br>así la digestión no compite con tu descanso</div></div>
    <div><div class="ring"><svg viewBox="0 0 24 24"><path d="M3 12h4l2-7 4 14 2-7h6"/></svg></div><div class="lbl"><b>Cuida el bajón de la 1pm</b><br>almuerzo sin dulce + caminar 5 min lo suavizan</div></div>
  </div>
</section>'''

# ---------- 8. CONSEJOS + CITA ----------
def tip(t, body):
    return f'<div class="numitem"><div class="nc"></div><div><div class="nt">{t}</div><p style="font-weight:300;">{body}</p></div></div>'

consejos = f'''
<section class="dark-section avoid-break">
  <div class="sec-head"><span class="sec-ico"><svg viewBox="0 0 24 24">{ICO['shield']}</svg></span><div class="t">Mis consejos <span class="it">para ti, Diana</span></div></div>
  <div class="numlist" style="max-width:760px;">
    {tip('La constancia le gana a la perfección','No necesitas una noche perfecta: necesitas repetir el ritual casi todas las noches. Tu cuerpo aprende por repetición, no por intensidad.')}
    {tip('El cuarto: fresco, oscuro y silencioso','Estos tres son los pilares físicos del sueño profundo. Una temperatura algo fresca y la oscuridad total valen más que cualquier suplemento.')}
    {tip('Si te desvelas, no pelees con la cama','Si llevas mucho rato despierta y con ansiedad, levántate, haz algo calmado con luz tenue y vuelve cuando sientas sueño. La cama es solo para dormir.')}
    {tip('Tu sueño y tu peso van de la mano','Cada noche profunda baja tus antojos de dulce y mejora tu insulina al día siguiente. Dormir bien no es un lujo: es parte central de tu tratamiento.')}
    {tip('Dale tiempo a tu cerebro post-COVID','La reparación de la memoria y el olfato sucede de noche, en silencio. Proteger tu sueño profundo es proteger tu recuperación.')}
  </div>
  <div class="quote">"El descanso no es lo que haces cuando terminas tu día, Diana. Es lo que hace posible tu día. Cuídalo como cuidas lo que más amas."</div>
</section>'''

body = hero + porque + diag + regla + ritual + resp + cafe + dia + consejos + B.footer()
html = B.html_doc("Plan de Sueño · Diana María Muñoz Ospina", body)
out = "/mnt/user-data/outputs/Plan de sueño - 2026-06-03 - MUÑOZ OSPINA DIANA MARÍA.html"
open(out,'w',encoding='utf-8').write(html)
print("WROTE", out, len(html))
