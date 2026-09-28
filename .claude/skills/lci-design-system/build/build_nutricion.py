# -*- coding: utf-8 -*-
import os, sys; sys.path.insert(0,'/mnt/skills/user/lci-design-system/assets')
import brand as B
import json as _json
EMB = _json.load(open(os.path.join(os.path.dirname(__file__),'embeds.json')))
HERO_BG = f"data:image/jpeg;base64,{EMB['hero']}"
BAND_BG = f"data:image/jpeg;base64,{EMB['band']}"
MKT_BG  = f"data:image/jpeg;base64,{EMB['market']}"
NUTRA_BG= f"data:image/jpeg;base64,{EMB['nutra']}"
INTER_BG= f"data:image/jpeg;base64,{EMB['inter']}"

ICO = {
 'leaf':'<path d="M5 21c0-9 7-16 16-16 0 9-7 16-16 16zM5 21c4-4 7-6 11-8"/>',
 'food':'<path d="M4 3v18M4 8h4M8 3v18"/><path d="M16 3c-2 0-3 2-3 5s1 5 3 5v8"/>',
 'pill':'<rect x="3" y="9" width="18" height="6" rx="3"/><path d="M12 9v6"/>',
 'cart':'<circle cx="9" cy="20" r="1.4"/><circle cx="18" cy="20" r="1.4"/><path d="M2 3h3l2.4 12h11l2-8H6"/>',
 'heart':'<path d="M12 21C7 17 3 13 3 8.5 3 6 5 4 7.5 4 9.4 4 11 5 12 6.5 13 5 14.6 4 16.5 4 19 4 21 6 21 8.5 21 13 17 17 12 21z"/>',
 'check':'<circle cx="12" cy="12" r="9"/><path d="M8 12l3 3 5-6"/>',
 'star':'<path d="M12 3l2.5 6 6.5.5-5 4.2 1.6 6.3L12 16.8 6.4 20l1.6-6.3-5-4.2 6.5-.5z"/>',
}
def sec_ico(name): return f'<span class="sec-ico"><svg viewBox="0 0 24 24">{ICO[name]}</svg></span>'

# ---------- HERO ----------
hero = f'''
<section class="hero avoid-break" style="background:linear-gradient(118deg, rgba(25,34,46,.95) 0%, rgba(25,34,46,.86) 40%, rgba(42,54,73,.62) 72%, rgba(42,54,73,.42) 100%), url('{HERO_BG}'); background-size:cover; background-position:center;">
  <div class="hero-top">
    <img class="seal" src="{B.LOGO_SEAL}">
    <div class="hero-doc"><div class="tag">Plan de Nutrición Funcional<br>Medicina de Longevidad</div></div>
  </div>
  <div class="eyebrow">Programa de Regeneración Metabólica</div>
  <h1 style="margin-top:12px;"><span class="accent">Recupera la energía</span><br>que creías perdida.</h1>
  <p class="sub">Tu cuerpo sabe sanar. <span class="serif-it">Nosotros sabemos cómo activarlo.</span>
  Este es el primer paso para reprogramar tu metabolismo, despertar tu vitalidad y devolverle ligereza a tu día.</p>
  <hr class="hairline">
  <div class="patient-card">
    <div class="cell"><div class="k">Paciente</div><div class="v">Diana María Muñoz Ospina</div></div>
    <div class="cell"><div class="k">Fecha del plan</div><div class="v">3 de junio de 2026</div></div>
    <div class="cell"><div class="k">Edad · Ubicación</div><div class="v">48 años · San Vicente de Chucurí, Santander</div></div>
    <div class="cell"><div class="k">Meta · Enfoque</div><div class="v">84 → 70 kg · Resistencia a la insulina + Tiroides</div></div>
  </div>
</section>'''

# ---------- 1. ENFOQUE / CHECKBOXES ----------
def chk(label, on, star=False):
    box = ('<span style="display:inline-block;width:17px;height:17px;border-radius:4px;'
           'margin-right:9px;vertical-align:-3px;'
           + ('background:linear-gradient(145deg,var(--gold-soft),var(--gold-deep));'
              'box-shadow:0 1px 0 rgba(255,255,255,.5) inset;text-align:center;color:#fff;'
              'font-size:11px;line-height:17px;">✓' if on else
              'background:#fff;border:1.5px solid var(--line);">') + '</span>')
    s = ' <span style="color:var(--gold-deep);">★</span>' if star else ''
    c = 'var(--navy)' if on else 'var(--ink-soft)'
    return f'<div style="padding:5px 0;color:{c};font-size:.9rem;">{box}{label}{s}</div>'

enfoque = f'''
<section class="section keep-with-prev">
  <div class="sec-head">{sec_ico('leaf')}<div class="t">Tu plan, en <span class="it">enfoque</span></div></div>
  <p class="lead">Diana, después de analizar tu historia escogí un mapa de intervención preciso. No es una dieta más:
  es una estrategia clínica para apagar la inflamación, ordenar tu azúcar en sangre y reactivar tu tiroides desde la célula.</p>
  <div class="card" style="display:grid;grid-template-columns:1fr 1fr;gap:8px 40px;">
    <div>
      <div style="font-family:'Mencken Std',serif;color:var(--gold-deep);font-weight:700;margin-bottom:6px;">Primer paso terapéutico</div>
      {chk('Plan cardio-metabólico',True)}
      {chk('Dieta de eliminación — Fase 1 (14 días)',True,True)}
      {chk('Reintroducción progresiva de alimentos',True)}
    </div>
    <div>
      <div style="font-family:'Mencken Std',serif;color:var(--gold-deep);font-weight:700;margin-bottom:6px;">Soporte de sistemas</div>
      {chk('Soporte de barrera y ácido gástrico',True)}
      {chk('Plan mitocondrial / neuroprotección',True)}
      {chk('Equilibrio del eje hormonal',True)}
    </div>
  </div>
</section>'''

# ---------- 2. MACROS / CALORÍAS / AYUNO ----------
def macro_btn(txt, sel):
    if sel:
        return (f'<span style="display:inline-block;margin:4px;padding:8px 18px;border-radius:30px;'
                f'background:linear-gradient(145deg,var(--gold),var(--gold-deep));color:#fff;font-weight:500;'
                f'font-size:.85rem;box-shadow:0 4px 12px rgba(160,128,96,.35);">● {txt} ★</span>')
    return (f'<span style="display:inline-block;margin:4px;padding:8px 18px;border-radius:30px;'
            f'background:var(--beige);color:var(--ink-soft);font-size:.85rem;border:1px solid var(--line);">○ {txt}</span>')

macros = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('heart')}<div class="t">Recomendaciones <span class="it">a tu medida</span></div></div>

  <div class="card avoid-break">
    <div style="font-weight:600;color:var(--navy);margin-bottom:10px;">Distribución de macronutrientes</div>
    <div style="display:flex;height:30px;border-radius:8px;overflow:hidden;font-size:.74rem;color:#fff;font-weight:500;box-shadow:0 3px 8px rgba(42,54,73,.15);">
      <div style="flex:35;background:var(--navy);display:flex;align-items:center;justify-content:center;">Proteína 35%</div>
      <div style="flex:40;background:var(--gold-deep);display:flex;align-items:center;justify-content:center;">Grasa 40%</div>
      <div style="flex:25;background:var(--blue-ink);display:flex;align-items:center;justify-content:center;">Carb 25%</div>
    </div>
    <div style="margin-top:14px;">
      {macro_btn('20/30/50',False)}{macro_btn('25/30/45',False)}{macro_btn('30/30/40',False)}
      {macro_btn('30/45/25',False)}{macro_btn('35/40/25',True)}{macro_btn('20/60/20',False)}
    </div>
    <p style="margin-top:14px;font-style:italic;font-size:.9rem;color:var(--ink-soft);">
    Escogí <b style="color:var(--navy);font-style:normal;">35% proteína / 40% grasa / 25% carbohidrato</b> por una razón clara:
    tu resistencia a la insulina (categoría 13/13 en tu cuestionario) y tu LDL de 189 mg/dL me piden bajar los carbohidratos
    y subir la proteína para proteger tu músculo mientras bajas de 84 a 70 kg. La grasa saludable será tu fuente de energía
    estable —se acaban los bajones y los antojos de dulce de media tarde— y además alimenta tu cerebro, que aún se está
    recuperando del COVID.</p>
  </div>

  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:start;">
  <div class="card avoid-break">
    <div style="font-weight:600;color:var(--navy);margin-bottom:8px;">Objetivo calórico</div>
    <div>{chk('1000–1200 kcal',False)}{chk('1200–1400 kcal',True,True)}{chk('1400–1800 kcal',False)}{chk('1800–2200 kcal',False)}</div>
    <p style="font-size:.9rem;color:var(--ink-soft);margin-top:6px;">Un rango de <b>1200–1400 kcal</b> genera un déficit amable y sostenible.
    Nada de hambre extrema: comerás suficiente proteína y grasa buena para sentirte llena y con energía.</p>
  </div>

  <div class="card avoid-break">
    <div style="font-weight:600;color:var(--navy);margin-bottom:8px;">Ayuno intermitente <span style="color:var(--gold-deep);">★ Sí — 14:10</span></div>
    <p style="font-size:.9rem;color:var(--ink-soft);">Tu ventana de alimentación será de <b>8:00 a.m. a 6:00 p.m.</b> (10 horas para comer,
    14 horas de descanso digestivo nocturno). Este ritmo le da un respiro a tu páncreas, mejora la sensibilidad a la insulina y
    ordena tu reloj biológico. <b>Importante:</b> primero toma tu Thyroid Liquescence al despertar en ayunas y espera 1 hora antes
    del desayuno.</p>
  </div>
  </div>

  <div class="note avoid-break" style="margin-top:18px;">
    <b>Lo más importante que vamos a soltar:</b> azúcares y dulces, harinas de trigo, leche en polvo como calmante de ansiedad,
    gaseosa y agua saborizada comercial, aceites vegetales refinados y los ultraprocesados. Y un acuerdo de salud no negociable:
    <b>retirar la cerveza de los fines de semana</b> —es la pieza que más está frenando tu hígado y tu pérdida de peso.
  </div>
</section>'''

# ---------- 3. GUÍA DE ALIMENTOS ----------
def fcat(num, color_odd, title, obj, allow, avoid):
    bg   = 'var(--beige)' if color_odd else 'var(--cream)'
    bd   = 'var(--gold)'  if color_odd else 'var(--navy)'
    nbg  = 'linear-gradient(145deg,var(--gold-soft),var(--gold-deep))' if color_odd else 'linear-gradient(145deg,var(--navy-soft),var(--navy-2))'
    ncol = '#fff' if color_odd else 'var(--gold-soft)'
    al = ''.join(f'<li style="padding:3px 0 3px 22px;position:relative;"><span style="position:absolute;left:0;color:var(--gold-deep);">✓</span>{x}</li>' for x in allow)
    av = ''.join(f'<li style="padding:3px 0 3px 22px;position:relative;color:#9a6a60;"><span style="position:absolute;left:0;color:#b35a4e;">✕</span>{x}</li>' for x in avoid)
    return f'''<div class="avoid-break" style="background:{bg};border-left:4px solid {bd};border-radius:12px;padding:20px 22px;margin-bottom:14px;box-shadow:0 4px 12px rgba(42,54,73,.07);">
      <div style="display:flex;align-items:center;gap:12px;margin-bottom:6px;">
        <span style="width:36px;height:36px;border-radius:50%;background:{nbg};color:{ncol};display:flex;align-items:center;justify-content:center;font-weight:600;box-shadow:0 3px 8px rgba(42,54,73,.2);">{num}</span>
        <span style="font-family:'Mencken Std',serif;font-weight:700;color:var(--navy);font-size:1.12rem;">{title}</span></div>
      <p style="font-style:italic;font-size:.86rem;color:var(--ink-soft);margin-bottom:8px;">{obj}</p>
      <ul style="list-style:none;font-size:.88rem;color:var(--navy);columns:2;column-gap:30px;">{al}{av}</ul>
    </div>'''

alimentos = f'''
<section class="section">
  <div class="sec-head">{sec_ico('food')}<div class="t">Tu guía de <span class="it">alimentos</span></div></div>
  <div class="dark-card avoid-break" style="margin-bottom:20px;">
    <h3>Diana, hablemos claro <span class="it">— de tú a tú.</span></h3>
    <p>Tu cuerpo lleva años pidiéndote ayuda: el aletargamiento, la memoria que falla, los antojos de dulce después del almuerzo
    y ese peso que no cede son señales de un metabolismo inflamado y de una insulina que dejó de escucharte. La buena noticia es
    que cada plato de aquí en adelante es una dosis de medicina. Comeremos comida real, saciante y deliciosa —sin arroz ni sopas,
    como prefieres— y le daremos a tu tiroides y a tu cerebro los nutrientes exactos que necesitan.</p>
    <div class="warn">
      <div class="wh">⚠ Filtros de seguridad aplicados a TODO tu plan</div>
      <ul>
        <li>Azúcar refinada, dulces, postres y leche entera en polvo (calmante de ansiedad)</li>
        <li>Harinas de trigo y derivados (pan, galletas, pastas refinadas)</li>
        <li>Gaseosa, agua saborizada comercial y jugos azucarados</li>
        <li>Alcohol — retiro total de la cerveza de fin de semana</li>
        <li>Aceites vegetales refinados y ultraprocesados industriales</li>
        <li>Arroz y sopas (por preferencia tuya) · Crucíferas siempre <b>cocidas</b>, nunca crudas (por tu tiroides)</li>
      </ul>
    </div>
  </div>

  {fcat('1',True,'Proteínas limpias — tu prioridad','Preservan tu músculo durante la pérdida de peso, te dan saciedad y frenan los antojos. Apunta a una porción en cada comida.',
     ['Carne de res magra','Pechuga y muslo de pollo','Cerdo magro (lomo)','Huevo campesino (2–3 u)','Pescado de río y mojarra','Sardina y atún en agua','Bagre / tilapia local'],
     ['Embutidos y carnes procesadas','Carnes empanizadas o fritas'])}

  {fcat('2',False,'Grasas que sanan','Estabilizan tu energía todo el día, suben tu HDL (hoy bajo en 44.7), bajan inflamación y nutren tu cerebro post-COVID.',
     ['Aguacate (½ unidad)','Aceite de oliva extra virgen','Aceite de coco para cocinar','Almendras y nueces (puño)','Semillas de chía y linaza','Mantequilla de vaca (la toleras bien)'],
     ['Margarina y aceites vegetales refinados','Frituras de paquete'])}

  {fcat('3',True,'Vegetales de bajo índice glucémico','Fibra que alimenta tu microbiota, regula tu azúcar y apoya la detoxificación de tu hígado (categoría 8/8).',
     ['Brócoli, coliflor y repollo — COCIDOS','Calabacín y zucchini','Habichuela y espárragos','Pepino y apio','Lechuga, rúgula, espinaca cocida','Tomate, pimentón, berenjena','Ajo y cebolla'],
     ['Vegetales crucíferos crudos en exceso'])}

  {fcat('4',False,'Carbohidratos inteligentes','En porción medida, eligiendo los de digestión lenta para no disparar tu insulina. Sin arroz: hay mejores opciones para ti.',
     ['Plátano verde / patacón al horno','Yuca cocida (porción medida)','Quinua','Lenteja y fríjol (porción)','Avena en hojuelas','Batata / camote'],
     ['Arroz blanco (preferencia tuya)','Pan y harinas de trigo','Papa frita y snacks de paquete'])}

  {fcat('5',True,'Frutas y antioxidantes','Bajas en azúcar, ricas en polifenoles. Tu postre natural para el antojo dulce, sin disparar la glucosa.',
     ['Frutos rojos (mora, fresa, arándano)','Cítricos: mandarina, naranja, limón','Guayaba','Papaya (tajada pequeña)','Manzana verde con cáscara','Cacao puro >85% (local, ¡eres de tierra de cacao!)'],
     ['Frutas en almíbar','Jugos colados y azucarados','Frutas muy dulces en exceso (mango maduro, uva)'])}
</section>'''

# ---------- 4. SUPLEMENTACIÓN ----------
def supp(name, dose, desc):
    return f'''<div class="dark-card avoid-break" style="padding:20px 22px;">
      <div style="color:var(--cream);font-weight:600;font-size:1rem;">{name}</div>
      <div style="color:var(--gold-soft);font-style:italic;font-size:.86rem;margin:4px 0 8px;">{dose}</div>
      <div style="font-weight:300;font-size:.88rem;color:var(--blue);">{desc}</div></div>'''

suple = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('pill')}<div class="t">Soporte <span class="it">nutracéutico</span></div></div>
  <p class="lead">Estos tres aliados acompañan tu alimentación. No reemplazan la comida real: la potencian, atacando puntos
  específicos de tu fisiología. Tómalos exactamente así:</p>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;">
    {supp('Betaine HCl — Enzymedica','1 cápsula 1 minuto antes del almuerzo y de la cena · por 1 mes',
       'Tu acidez está alterada (saciedad temprana y agrieras): este nutracéutico restaura tu ácido gástrico para que digieras bien la proteína y absorbas hierro, zinc y B12 —claves para tu energía y tu sangrado menstrual.')}
    {supp('Chromium Picolinate 500 mcg — Pure Encapsulations / Solgar','1 cápsula al día con el almuerzo · por 3 meses',
       'El cromo mejora cómo tu célula escucha a la insulina y corta de raíz ese antojo imperativo de dulce que aparece después del almuerzo. Es tu defensa contra la glucotoxicidad.')}
    {supp('Thyroid Liquescence — Professional Formulas','Llena el gotero, diluye en poca agua y bebe al despertar en ayunas · espera 1 hora antes de comer',
       'Tu TSH (3.93) y T4 libre están en el límite: este soporte favorece la conversión hormonal periférica para reactivar el metabolismo, levantar esa "pereza" y encender tu energía matutina.')}
    <div class="card" style="border-left:5px solid var(--gold);">
      <div style="font-family:'Mencken Std',serif;color:var(--navy);font-weight:700;font-size:1.05rem;margin-bottom:6px;">Terapia médica complementaria</div>
      <p style="font-size:.86rem;color:var(--ink-soft);">En paralelo seguimos tu esquema de péptidos prescrito en consulta
      (Retatrutide y BPC-157) según las indicaciones y dosis que ya te entregué. Cualquier duda con la aplicación, me escribes.</p>
    </div>
  </div>
  {B.img_strip(NUTRA_BG,'Comida real + ciencia','Tus nutracéuticos potencian tu comida real,','nunca la reemplazan.', pos='center 60%')}
</section>'''

# ---------- 5. INTERCAMBIOS ----------
def xcard(grad, bd, title, items):
    li = ''.join(f'<div style="padding:4px 0;font-size:.85rem;color:var(--navy);">{x}</div>' for x in items)
    return f'''<div class="avoid-break" style="border-radius:14px;overflow:hidden;border:1px solid {bd};box-shadow:0 6px 16px rgba(42,54,73,.08);">
      <div style="background:{grad};color:#fff;padding:12px 16px;font-weight:600;font-size:.78rem;letter-spacing:.06em;">{title}</div>
      <div style="background:var(--beige);padding:14px 16px;">{li}</div></div>'''

inter = f'''
<section class="section keep-with-prev">
  <div class="sec-head">{sec_ico('check')}<div class="t">Guía práctica de <span class="it">intercambios</span></div></div>
  <p class="lead">Para que armes tus platos sin pesar todo. Una "porción" equivale a cualquiera de estas opciones:</p>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">
    {xcard('linear-gradient(135deg,var(--gold),var(--gold-deep))','var(--gold)','1 PORCIÓN DE PROTEÍNA',['100–120 g de carne de res','O 1 pechuga mediana de pollo','O 1 filete de pescado','O 3 huevos campesinos'])}
    {xcard('linear-gradient(135deg,var(--navy-soft),var(--navy-2))','var(--navy)','1 PORCIÓN DE GRASA',['½ aguacate','O 1 cda de aceite de oliva','O 1 puño de almendras','O 1 cda de mantequilla'])}
    {xcard('linear-gradient(135deg,var(--gold),var(--gold-deep))','var(--gold)','1 PORCIÓN DE VEGETAL',['1 taza de brócoli cocido','O 1 taza de calabacín','O 2 tazas de hojas verdes','O 1 taza de habichuela'])}
    {xcard('linear-gradient(135deg,var(--blue-mid),var(--navy-soft))','var(--blue-ink)','1 PORCIÓN DE CARB',['½ taza de yuca cocida','O 1 patacón al horno','O ½ taza de quinua','O ½ taza de lenteja'])}
  </div>
  <p class="lead" style="margin:20px 0 12px;">Y si no tienes nada para medir, tu propia mano es la guía más fiel —siempre va contigo:</p>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px;">
    {''.join(f'''<div class="avoid-break" style="text-align:center;padding:16px 12px;background:#fff;border-radius:12px;box-shadow:0 4px 12px rgba(42,54,73,.07);">
      <div style="width:38px;height:38px;margin:0 auto 8px;border-radius:50%;border:1.5px solid var(--gold);display:flex;align-items:center;justify-content:center;color:var(--gold-deep);font-weight:600;">{n}</div>
      <div style="font-family:'Mencken Std',serif;color:var(--navy);font-weight:700;font-size:.98rem;">{t}</div>
      <div style="font-size:.78rem;color:var(--ink-soft);margin-top:2px;">{d}</div></div>'''
      for n,t,d in [('1','La palma','1 porción de proteína'),('2','El puño','1 porción de vegetales'),('3','El pulgar','1 porción de grasa'),('4','La mano ahuecada','1 porción de carbohidrato')])}
  </div>
  {B.img_strip(INTER_BG,'Tu porción, a ojo','Una porción es una guía para tu ojo,','no una balanza en la mano.')}
</section>'''

# ---------- 6. MENÚ 14 DÍAS ----------
menu = [
 ("1","<span class='dish'>Huevos pericos con aguacate:</span> 2 huevos, ½ aguacate, tomate y cebolla salteados en AOVE. Café sin azúcar.",
      "<span class='dish'>Res a la plancha:</span> 120 g de res magra, brócoli y coliflor cocidos al ajillo, ½ patacón al horno.",
      "<span class='dish'>Mojarra al vapor:</span> 1 filete de pescado de río, calabacín salteado, ensalada de pepino y limón."),
 ("2","<span class='dish'>Bowl proteico:</span> 2 huevos cocidos, ½ aguacate, semillas de chía, frutos rojos (½ taza).",
      "<span class='dish'>Pollo al limón:</span> 1 pechuga, espárragos y habichuela cocida, ½ taza de quinua.",
      "<span class='dish'>Tortilla de la huerta:</span> 2 huevos con espinaca cocida y queso, ensalada verde con AOVE."),
 ("3","<span class='dish'>Revuelto andino:</span> 2 huevos, champiñones y pimentón, 1 tajada pequeña de papaya.",
      "<span class='dish'>Cerdo magro:</span> 120 g de lomo, repollo cocido salteado, ½ taza de yuca.",
      "<span class='dish'>Atún del mar:</span> atún en agua con aguacate y tomate, hojas verdes y aceite de oliva."),
 ("4","<span class='dish'>Avena salada:</span> avena con huevo pochado, aguacate y semillas de linaza. Tinto sin azúcar.",
      "<span class='dish'>Mojarra frita al horno:</span> pescado, ensalada de zucchini, ½ patacón.",
      "<span class='dish'>Pollo desmechado:</span> con cebolla y pimentón, brócoli cocido, rúgula."),
 ("5","<span class='dish'>Huevos al gusto:</span> 2 huevos, ½ aguacate, frutos rojos. Café.",
      "<span class='dish'>Bandeja ligera:</span> 120 g de res, fríjol (½ taza), ensalada de aguacate y tomate.",
      "<span class='dish'>Crema de calabacín (no sopa de paquete):</span> calabacín y caldo de hueso, 2 huevos cocidos."),
 ("6","<span class='dish'>Batido verde proteico:</span> ver receta estrella. + 1 huevo cocido.",
      "<span class='dish'>Pollo a la plancha:</span> con coliflor gratinada al horno y ensalada verde.",
      "<span class='dish'>Tilapia al ajillo:</span> con habichuela y pimentón salteados en AOVE."),
 ("7","<span class='dish'>Día libre inteligente:</span> huevos pericos + ½ aguacate + cacao puro caliente sin azúcar.",
      "<span class='dish'>Asado familiar:</span> res o cerdo magro a la parrilla, ensalada grande, patacón al horno.",
      "<span class='dish'>Ligera:</span> tortilla de huevo con vegetales cocidos, manzana verde."),
]
def menu_rows():
    rows=''
    for d,des,alm,cen in menu:
        rows+=f'<tr><td class="daycol" style="text-align:center;">Día {d}</td><td>{des}</td><td>{alm}</td><td>{cen}</td></tr>'
    # days 8-14 repeat with note
    return rows

menu_html = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('food')}<div class="t">Tu menú de <span class="it">14 días</span></div></div>
  <div class="note avoid-break" style="margin-bottom:16px;">
    <b>Nota de tu médica:</b> respeta tu ventana de 8:00 a.m. a 6:00 p.m. La <b>cena siempre antes de las 6:00 p.m.</b> para que
    duermas mejor y tu glucosa nocturna esté tranquila. Mastica lento —cuenta hasta 20 por bocado— para revertir el patrón de
    comedora rápida. Si te da antojo de dulce, tu postre es cacao puro o frutos rojos.
  </div>
  <table class="avoid-break">
    <thead><tr><th style="text-align:center;">Día</th><th>Desayuno · 8:00 a.m.</th><th>Almuerzo · 1:00 p.m.</th><th>Cena · antes 6:00 p.m.</th></tr></thead>
    <tbody>{menu_rows()}</tbody>
  </table>
  <p class="lead" style="margin-top:14px;font-style:italic;">Los días 8 al 14 repiten esta misma estructura rotando tus
  proteínas y vegetales favoritos. Mantén siempre el esquema: 1 proteína + 1–2 vegetales + ½ porción de carbohidrato inteligente + 1 grasa buena.</p>
</section>'''

# ---------- 7. RECETAS ----------
def recipe(title, time, ings, steps, benefit):
    li=''.join(f'<li style="padding:2px 0;">{i}</li>' for i in ings)
    ol=''.join(f'<li style="padding:2px 0;">{s}</li>' for s in steps)
    return f'''<div class="avoid-break" style="border-radius:16px;overflow:hidden;box-shadow:0 8px 22px rgba(42,54,73,.1);background:#fff;break-inside:avoid;page-break-inside:avoid;">
      <div style="background:linear-gradient(135deg,var(--navy-soft),var(--navy-2));padding:14px 18px;">
        <div style="font-family:'Mencken Std',serif;color:var(--gold-soft);font-weight:700;font-size:1.05rem;">{title}</div>
        <div style="color:var(--blue);font-size:.74rem;">{time}</div></div>
      <div style="display:grid;grid-template-columns:1fr 1.2fr;">
        <div style="background:var(--cream);padding:14px 16px;"><div style="font-weight:600;color:var(--navy);font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px;">Ingredientes</div><ul style="list-style:none;font-size:.82rem;color:var(--navy);">{li}</ul></div>
        <div style="background:#fff;padding:14px 16px;"><div style="font-weight:600;color:var(--navy);font-size:.78rem;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px;">Preparación</div><ol style="font-size:.82rem;color:var(--ink-soft);padding-left:16px;">{ol}</ol></div>
      </div>
      <div style="background:var(--navy);color:var(--cream);font-family:'Mencken Std Head',serif;font-style:italic;font-size:.86rem;padding:10px 18px;">{benefit}</div></div>'''

recetas = f'''
<section class="section">
  <div class="sec-head">{sec_ico('star')}<div class="t">Recetas <span class="it">para enamorarte</span></div></div>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;align-items:start;">
    {recipe('🍳 Huevos pericos del despertar','Prep 5 min · Cocción 8 min',
      ['2 huevos campesinos','½ aguacate en tajadas','1 tomate maduro picado','¼ cebolla','1 cda de aceite de oliva','Sal y cilantro'],
      ['Sofríe cebolla y tomate en el aceite.','Agrega los huevos y revuelve a fuego bajo.','Sirve con el aguacate al lado y cilantro fresco.'],
      'Proteína + grasa buena para arrancar el día con energía estable y sin antojos a media mañana.')}
    {recipe('🥩 Res al ajillo con crucíferas','Prep 10 min · Cocción 15 min',
      ['120 g de res magra','1 taza de brócoli','1 taza de coliflor','2 dientes de ajo','1 cda de AOVE','Sal, pimienta, limón'],
      ['Cocina al vapor el brócoli y la coliflor 6 min.','Sella la res 3 min por lado con el ajo.','Saltea las crucíferas cocidas en el AOVE y une todo.'],
      'Hierro y zinc para tu energía y tu sangrado; crucíferas cocidas que cuidan tu tiroides y depuran tu hígado.')}
    {recipe('🐟 Mojarra al vapor con limón','Prep 8 min · Cocción 12 min',
      ['1 filete de pescado de río','1 calabacín en rodajas','Jugo de 1 limón','1 cda de aceite de coco','Ajo, sal, perejil'],
      ['Marina el pescado con limón, ajo y sal 5 min.','Cocina al vapor 10–12 min.','Saltea el calabacín en aceite de coco y sirve.'],
      'Omega-3 ligero y antiinflamatorio que nutre tu cerebro en recuperación post-COVID.')}
    {recipe('🥤 Batido verde regenerativo','Prep 5 min',
      ['1 taza de espinaca cocida y fría','½ aguacate','½ taza de frutos rojos','1 cda de chía','1 scoop opcional de proteína','Agua y hielo'],
      ['Licúa todo hasta que quede cremoso.','Bébelo dentro de tu ventana, sin colar para conservar la fibra.'],
      'Tu desayuno antiinflamatorio: fibra, antioxidantes y grasa buena que estabilizan tu glucosa.')}
    {recipe('🥗 Bowl de quinua, pollo y aguacate','Prep 10 min · Cocción 15 min',
      ['½ taza de quinua cocida','1 pechuga de pollo','½ aguacate','1 taza de espinaca','Tomate cherry','Jugo de limón','1 cda de AOVE'],
      ['Cocina la quinua y déjala entibiar.','Sella la pechuga y córtala en tiras.','Arma el bowl con espinaca, quinua, pollo y aguacate; baña con limón y AOVE.'],
      'Tu almuerzo fórmula: proteína completa + grasa buena + carbohidrato inteligente para energía estable sin bajones.')}
    {recipe('🐟 Sardinas mediterráneas con limón','Prep 5 min · Sin cocción',
      ['1 lata de sardinas en agua','½ aguacate','Hojas verdes','Jugo de limón','1 cda de AOVE','Orégano'],
      ['Escurre las sardinas.','Sírvelas sobre hojas verdes con el aguacate.','Aliña con limón, AOVE y orégano.'],
      'Omega-3 y vitamina D para tu tiroides y tu cerebro post-COVID —lista en 5 minutos y sin encender la estufa.')}
    {recipe('🍳 Tortilla horneada de espinaca y champiñón','Prep 8 min · Cocción 18 min',
      ['3 huevos campesinos','1 taza de espinaca','½ taza de champiñones','¼ cebolla','1 cda de AOVE','Sal y pimienta'],
      ['Saltea cebolla, champiñón y espinaca en el AOVE.','Bate los huevos, mezcla y vierte en un molde.','Hornea a 180 °C por 15–18 min.'],
      'Prepárala en lote: hierro y proteína para resolver tus desayunos de media semana sin antojos.')}
    {recipe('🍌 Patacón al horno con guacamole','Prep 10 min · Cocción 20 min',
      ['1 plátano verde','½ aguacate','Jugo de limón','Cilantro','1 cda de AOVE','Sal'],
      ['Corta el plátano y hornéalo con un hilo de AOVE a 200 °C hasta dorar.','Machaca el aguacate con limón, cilantro y sal.','Sirve el patacón con el guacamole.'],
      'Tu antojo de "algo crocante" resuelto con carbohidrato resistente y grasa buena, sin freír ni disparar tu glucosa.')}
    {recipe('🥑 Snack salvador de antojos','Prep 3 min',
      ['1 puño de almendras','2 cuadros de cacao puro >85%','1 mandarina'],
      ['Cuando llegue el antojo de dulce de la tarde, ten esto a la mano.','Mastica despacio y disfruta.'],
      'Reemplaza el dulce y la leche en polvo: el cacao y el magnesio calman la ansiedad sin disparar tu insulina.')}
    {recipe('☕ Infusión digestiva de la noche','Prep 5 min',
      ['1 taza de agua caliente','1 rodaja de jengibre','Cáscara de limón','1 ramita de hierbabuena'],
      ['Infusiona 5 min y cuela.','Tómala después de la cena, antes de las 7 p.m.'],
      'Apaga la agrieras, mejora tu digestión y prepara tu cuerpo para un sueño reparador.')}
  </div>
</section>'''

# ---------- 8. LISTA DE MERCADO ----------
def shop(title, items):
    li=''.join(f'<li style="padding:3px 0 3px 20px;position:relative;font-size:.85rem;color:var(--navy);"><span style="position:absolute;left:0;color:var(--gold-deep);">✓</span>{x}</li>' for x in items)
    return f'''<div class="avoid-break" style="background:#fff;border-radius:14px;overflow:hidden;box-shadow:0 6px 16px rgba(42,54,73,.08);">
      <div style="background:linear-gradient(135deg,var(--gold),var(--gold-deep));color:#fff;padding:11px 16px;font-weight:600;font-size:.82rem;">{title}</div>
      <ul style="list-style:none;padding:12px 16px;">{li}</ul></div>'''

mercado = f'''
<section class="section alt">
  <div class="sec-head">{sec_ico('cart')}<div class="t">Lista de mercado <span class="it">— San Vicente de Chucurí</span></div></div>
  <div class="dark-card avoid-break" style="margin-bottom:18px;">
    <h3>📍 Tu ruta de compras</h3>
    <p>Empieza por la <b>Plaza de Mercado de San Vicente de Chucurí</b> para lo más fresco: aguacate, plátano, yuca, cítricos,
    verduras de la región y tu cacao local. En las <b>carnicerías del pueblo</b> consigue res magra, cerdo y pollo del día; el
    <b>pescado de río</b> con tus proveedores de confianza. En <b>tiendas D1 / Ara / Justo &amp; Bueno</b> completas huevos, atún
    en agua, avena, frutos secos, aceite de oliva y semillas. Para tus nutracéuticos (Betaine HCl, Cromo, Thyroid Liquescence)
    los pides en línea o en una droguería naturista de <b>Bucaramanga</b> —o directamente conmigo en el consultorio.</p>
  </div>
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;">
    {shop('Verduras',['Brócoli y coliflor','Repollo y col rizada','Calabacín / zucchini','Habichuela y espárragos','Espinaca y acelga','Pepino, apio, lechuga','Tomate, cebolla, ajo','Pimentón y champiñones','Zanahoria y berenjena','Cilantro y perejil'])}
    {shop('Frutas',['Frutos rojos (mora, fresa)','Arándanos','Mandarina y naranja','Limón y lima','Guayaba','Papaya','Manzana y pera verde','Kiwi','Cacao puro local >85%'])}
    {shop('Proteínas',['Res magra','Pechuga y muslo de pollo','Lomo de cerdo','Pavo','Huevos campesinos','Pescado de río / mojarra','Atún en agua','Sardina','Hígado de res (1×/sem)','Lentejas y garbanzos'])}
    {shop('Despensa y varios',['Aceite de oliva extra virgen','Aceite de coco','Aceite de aguacate','Almendras y nueces','Semillas de calabaza','Chía y linaza','Avena en hojuelas','Quinua','Yuca y plátano verde','Cúrcuma, jengibre, canela','Vinagre de manzana'])}
  </div>
  <div class="note avoid-break" style="margin-top:18px;"><b>Regla de etiqueta:</b> entre menos ingredientes, mejor. Evita lo que diga
  "azúcar", "jarabe de maíz", "harina refinada" o aceites de soya, girasol o canola. Si un empaque tiene más de cinco ingredientes
  que no reconoces, déjalo en el estante: tu cuerpo no sabe metabolizar lo que no es comida real.</div>
</section>'''

# ---------- 9. CONSEJOS + CITA ----------
def tip(t, body):
    return f'<div class="numitem"><div class="nc"></div><div><div class="nt">{t}</div><p style="font-weight:300;">{body}</p></div></div>'

consejos = f'''
<section class="dark-section avoid-break">
  <div class="sec-head"><span class="sec-ico"><svg viewBox="0 0 24 24">{ICO['heart']}</svg></span><div class="t">Mis consejos <span class="it">para ti, Diana</span></div></div>
  <div class="numlist" style="max-width:760px;">
    {tip('Mastica como una ceremonia','Tu somnolencia después de comer y tu saciedad temprana mejoran muchísimo si comes despacio. Cuenta hasta 20 por bocado y suelta los cubiertos entre uno y otro. Comer lento es comer menos, sin esfuerzo.')}
    {tip('El acuerdo de la cerveza','Sé que los fines de semana en familia son sagrados, pero la cerveza es lo que más frena tu hígado y tu pérdida de peso. Cámbiala por agua con gas y limón en una copa bonita: brindas igual, pero a favor de tu salud.')}
    {tip('Agua de verdad','Suelta la gaseosa y el agua saborizada comercial —son azúcar líquida que alimenta tu resistencia a la insulina. Apunta a 8 vasos de agua pura al día. Saborízala tú con limón, pepino o hierbabuena.')}
    {tip('Apaga las pantallas, enciende tu descanso','Tu cerebro post-COVID necesita sueño profundo para sanar la memoria. Sin televisor ni celular 2 horas antes de dormir. A las 10 p.m., cuarto oscuro y en silencio.')}
    {tip('Tu antojo de la tarde tiene respuesta','Ese deseo imperativo de dulce después del almuerzo lo vamos a desarmar con el cromo + tu snack de cacao y almendras. No es falta de voluntad: es química, y la estamos corrigiendo.')}
  </div>
  <div class="quote">"Tu cuerpo no está roto, Diana. Solo está esperando que le des las señales correctas. Empezamos hoy —y tu yo del futuro te lo va a agradecer."</div>
</section>'''

# ---------- BANDA EDITORIAL (antes de recetas) ----------
band = f'''
<section class="avoid-break band-intro" style="position:relative;min-height:280px;display:flex;align-items:center;
  padding:54px;color:#fff;background:linear-gradient(95deg, rgba(25,34,46,.93) 0%, rgba(25,34,46,.70) 42%, rgba(25,34,46,.20) 78%, rgba(25,34,46,0) 100%), url('{BAND_BG}');background-size:cover;background-position:center 38%;">
  <div style="max-width:540px;position:relative;z-index:2;">
    <div class="eyebrow" style="color:var(--gold);">Tu cocina es tu farmacia</div>
    <div class="serif" style="font-size:2.05rem;line-height:1.12;margin-top:10px;">Cada plato es <span class="serif-it" style="color:var(--blue);">una dosis</span> de información para tus células.</div>
    <hr class="hairline" style="margin:18px 0 0;max-width:200px;margin-left:0;">
  </div>
</section>'''

# ---------- BANNER LISTA DE MERCADO ----------
mkt_banner = f'''
<section class="avoid-break band-intro" style="position:relative;height:200px;display:flex;align-items:flex-end;
  padding:26px 54px;color:#fff;background:linear-gradient(0deg, rgba(25,34,46,.92) 0%, rgba(25,34,46,.45) 45%, rgba(25,34,46,.10) 100%), url('{MKT_BG}');background-size:cover;background-position:center 55%;">
  <div style="position:relative;z-index:2;">
    <div class="eyebrow" style="color:var(--gold);">Del mercado a tu mesa</div>
    <div class="serif" style="font-size:1.5rem;margin-top:4px;">Lo que llevas a casa <span class="serif-it" style="color:var(--blue);">empieza aquí.</span></div>
  </div>
</section>'''

body = (hero + enfoque + macros + alimentos + suple + inter + menu_html
        + band + recetas + mkt_banner + mercado + consejos + B.footer())
html = B.html_doc("Plan Nutricional · Diana María Muñoz Ospina", body)
out = "/mnt/user-data/outputs/Plan nutricional - 2026-06-03 - MUÑOZ OSPINA DIANA MARÍA.html"
open(out,'w',encoding='utf-8').write(html)
print("WROTE", out, len(html))
