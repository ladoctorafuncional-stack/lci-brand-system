---
name: lci-piezas-graficas
description: "Motor de DISEÑO GRÁFICO y diagramación del Longevity Clinical Institute (Dra. Carolina Rodríguez), estilo de la diseñadora Paola Londoño (Ikigai). Úsalo SIEMPRE que se pida crear, diseñar, diagramar o adaptar cualquier pieza gráfica de LCI: post o carrusel de Instagram, story, infografía, flyer, afiche, banner, portada, brochure, revista o documento multipágina, cita, dato, invitación, aviso a pacientes, pieza del curso de péptidos, firma de correo o carnet. Dispara con \"diseña\", \"hazme una pieza\", \"story\", \"post\", \"carrusel\", \"brochure\", \"diagrama esto con mi marca\" o cuando se suba contenido para convertir en pieza visual. Todo el material de marca está embebido (Mencken Std + Poppins, logos, paleta, piezas maestras de Paola, estándar visual 2026, diagramaciones, interlineado blindado): nunca pedir que se vuelvan a subir. Resultado: PNG pixel-exacto. Documentos clínicos: skill lci-design-system."
---

# LCI — Piezas Gráficas (clon de Diana Paola Londoño)

## 🛑 ANTES DE DISEÑAR Y ANTES DE ENTREGAR — OBLIGATORIO EN CADA TANDA (la Dra., 11-oct-2026)
Este bloque manda sobre todo lo demás. Se relee COMPLETO al empezar cada tanda, aunque sea en la misma conversación.
1. **Un soporte distinto por pieza — y el panel de vidrio a media pieza (`mitad`) es la EXCEPCIÓN (la Dra., 25-oct-2026: «se está repitiendo mucho»).**
   Antes de diseñar, correr `R.plan_variedad(n)` (propone la tabla «pieza → soporte → acento») y ajustarla a cada foto.
   Los soportes de Paola, por orden de preferencia — **son la norma**:
   | Soporte (`soporte_=`) | Qué es | Referencia de Paola |
   |---|---|---|
   | `None` (directo) | titular directo sobre la foto con caída de luz natural, sin panel | «Your body knows how to heal» |
   | `linea` | texto directo + línea vertical con nodos y viñetas cortas (`vinetas=[…]`, usa `M.conector`) | «Reclaim the energy» |
   | `tarjeta` | tarjeta redondeada de vidrio con filo, titular + filete dorado + viñetas (`vinetas=[…]`) | «Somos expertos en…» |
   | `resaltar=True` | resaltado que abraza la palabra gancho (`M.barra`) | «are cellular messengers» |
   | `recuadro` | recuadro de filo fino alrededor del titular | «The brain ages too» |
   | `blur` | desenfoque del fondo solo detrás del titular (ajustado al bloque, sin llenar media pieza) | fondos desenfocados de Paola |
   | `vidrio`, `panel_claro`, `velo` | tarjeta de vidrio · panel crema · velo localizado | |
   | `columna_izq/der` | lámina «ducha» (máx. 1 por tanda) | |
   | `mitad` | panel a media pieza — **solo si ningún otro sirve para esa foto; justificarlo por escrito en la tabla** (máx. 1 de cada 4 piezas) | |
   Ejemplo visual verificado con los auditores: `references/estandar-visual-2026/variedad-soportes-2026-10-25.jpg`.
   Nunca el mismo soporte en dos piezas seguidas del mismo perfil ni más de 2 veces en la tanda. `R.auditar_soportes({perfil:[(nombre, html)…]})`
   (es una FUNCIÓN, no un script) lo verifica y DETIENE el render; ES y EN de un mismo par son perfiles distintos, así que **además hay que
   mirar el feed ya publicado**: si las últimas piezas usaron `mitad`, no repetirlo.
1b. **El acento NO es siempre azul claro.** Rotar en la tanda: crema · azul Paola `#AFCAE4` · dorado · azul acero · blanco · azul claro
   (`R.ACENTOS`, parámetro `acc_col=`). Máx. la mitad de las piezas con el mismo color, nunca 3 seguidas: `R.auditar_acentos(...)`.
   Sobre foto clara, un acento claro no pasa el contraste (F3): usar crema/blanco con soporte `blur`/`tarjeta`, o navy sobre claro.
2. **El soporte se elige por la foto, no por costumbre:** primero se mira dónde están la cara, la cabeza y el objeto
   protagonista; el texto va en la zona libre. Si la persona está a un lado → lámina o tarjeta al lado contrario; si la
   zona libre es arriba → panel crema arriba; si es abajo → panel o tarjeta abajo.
3. **Aire sobre la cabeza:** la cabeza nunca toca el borde superior ni la zona del logo; si la foto viene justa, se
   prolonga el fondo arriba (cielo, pared, niebla) antes de montar la pieza.
4. **Logo y sello CR al margen de 108 px** (posts e historias), alineados a un margen, solos en su esquina, sobre zona limpia.
5. **Cápsula en historias:** top = H − 190; referencias justo encima.
6. **Mirar cada PNG** (no solo el auditor) y revisar: caras libres, logo, aire entre bloques, que EN y ES sean idénticas.

Motor para producir piezas de redes/marketing idénticas al estándar de marca de LCI. **No se
reinventa el diseño**: se ensambla con `marca.py`, que ya trae fuentes, logos, paleta y los
motivos firma de Paola. La doctrina de marca completa está en
`references/marca-oficial/MANUAL-LCI.md` — **léela primero** ante cualquier duda de color,
tipografía, logo o foto.

## REGLA INQUEBRANTABLE — interlineado con resaltado (10-oct-2026)
Cuando un bloque de texto lleva RESALTADO (barra que abraza el texto), el interlineado del bloque SUBE un poco: la barra NUNCA invade la línea de arriba ni la de abajo. Aire mínimo entre la barra y la tinta vecina: max(10 px, 12 % del alto de la barra). El auditor lo bloquea (F9). Sin excepciones.

## Regla 10-oct-2026: con vidrio opaco la cápsula va DENTRO del vidrio: completa si el vidrio cubre todo el ancho (panel), solo con la web en lámina vertical o tarjeta. Resaltado: +2 px de barra después del texto y al menos 2 px arriba y abajo de las letras. Portadas: ≥1 de cada 3 con PERSONAS; variar sujetos (alimentos, glóbulos rojos, tejidos); no repetir lugares/aparatos.

## REGLA DE ESPACIADO — recuadro-acento + titular (10-oct-2026, ajustada con la Dra.)
El recuadro-acento («Measured,», «Antioxidant pills», «Functional,», «Welcome to») va CERCA del titular, con el MISMO aire óptico en todas las piezas: aire VISIBLE entre el borde inferior del recuadro y la TINTA más alta de la primera línea del titular = 0.24 × tamaño del titular (≈ 18 px con titular de 74 px; tope: titular de 90 px). No se usa un margen fijo: `r_poster` mide la tinta real con JS (canvas `actualBoundingBoxAscent`), porque las ascendentes de «with», «the», «h» suben más que una mayúscula y un margen fijo pegaba unas piezas y separaba otras. Titular → línea regular: 0.04×Hs. Después del bloque: respiro 0.40×Hs + filete fino al ancho del bloque + respiro 0.36×Hs + tagline ≥ 38 px. En `r_centrado`, 44 px entre la estrella y la línea regular. Subtítulos bajo titulares: 34–41 px, nunca menores.

## REGLA DE COLOR DE TEXTOS (10-oct-2026)
El azul claro #CAD3DD es protagonista de la marca, pero los textos no pueden ser siempre blanco + azul claro. Rotar en el lote: navy sobre claro, crema en cuerpos sobre oscuro, dorado en filetes/detalles, azul claro como acento recurrente. Revisar el lote completo antes de entregar: si más de la mitad de las piezas repite blanco + azul claro, cambiar combinaciones.

## Regla de oro
Nunca recrear CSS, colores, fuentes ni logos a mano. Siempre `import marca as B`. Si una pieza
no usa `marca.py`, está mal hecha.


## ⭐⭐ REGLAS DE LECTURA, MÁRGENES, CONTRASTE Y RITMO DEL FEED (10-oct-2026). Regla dura que va por encima de todo lo anterior
La Dra. revisó en el celular las piezas publicadas. Está todo en `references/correcciones-2026-10-10/REGLAS-10-OCT-2026.md` y en sus capturas anotadas (01–15). Hay que **leerlo antes de diseñar**. Resumen:
1. **Zona segura = 10 % del lado más corto en los 4 lados** (guías en `correcciones-2026-10-10/margenes/`): 1080×1350 → 108 px, 1080×1920 → 108, 1200×1200 → 120, 1200×630 → 63, 851×315 → 32. Logo, textos, recuadros y referencias van dentro. Solo la cápsula o la web pueden ir en la banda inferior, centradas y dentro de los márgenes laterales. Usar `M.margen(W,H)`. `_logo`, `_pill` y `_refs` ya lo aplican.
2. **Piso tipográfico (a 1080 px):** el tamaño más pequeño permitido es el del texto de la **cápsula de contacto del pie** (teléfono · @usuario · web; 19 px). Nada puede ir por debajo. No confundir con el recuadro «Reclaim the energy», que es un titular. **El piso NO es el tamaño de la pieza:** la jerarquía manda (titular ≥ 2.4 × cuerpo; subtítulo 1.4–1.8 ×; cuerpo 27–34; rótulos 22–26; solo pie, referencias y aclaratorios en el piso). Nunca todos los textos del mismo tamaño; el auditor lo marca como F8. Referencias: 20 px. Eyebrows, rótulos y etiquetas: 22 px. Cuerpo: 27 px. `marca.lienzo` inyecta `REGLAS_JS` (`assets/reglas_lectura.py`), que sube lo que esté por debajo. Los grupos en em llevan `data-escala`.
3. **Aprovechar el espacio:** con poco texto, subir 1–2 tamaños manteniendo la jerarquía, o sumar un recuadro o tarjeta. Prohibido el texto chico con espacio vacío alrededor.
4. **Interlineado de bloque uniforme:** en un bloque de líneas de distinto tamaño, el aire de tinta es igual entre todas las líneas. Usar `data-pila="0.30"` en el contenedor. El caso «up to 2×» fue un error gigante.
5. **Recuadros simétricos** (arriba = abajo, izquierda = derecha), como «Reclaim the energy». **Una sola línea de alineación izquierda**, incluido el texto dentro de un recuadro (el borde sobresale).
6. **Contraste:** 4.5:1 o más. Titulares de 60 px o más: 7:1 o más, y un punto más sobre foto cargada. En fondo claro, navy. Prohibido el gris sobre gris («y en la vejez.») y el azul grisáceo sobre foto gris («where your fat is.»).
6b. **Soportes de lectura sobre foto:** el contraste no se resuelve oscureciendo toda la foto, sino con un panel de vidrio opaco a media pieza (`R.soporte('mitad')`), una lámina de vidrio vertical «tipo ducha» de alto completo (`soporte_='columna_izq'|'columna_der'`), una tarjeta de vidrio (`soporte_='vidrio'`), un resaltado que abrace el texto (`M.barra`), cápsulas o recuadros. Con lámina de vidrio, el logo blanco va dentro del vidrio. El color del logo depende de la pieza (blanco, navy, beige o dorado según el fondo y la foto) y, si ningún color se lee, se oscurece esa zona con una caída de luz natural de la foto: viñeta amplia de esquina o borde que parece de la fotografía, nunca una mancha local alrededor del logo. Nunca va dentro de una cápsula o recuadro propio, porque le quita elegancia a la marca. El logo siempre se alinea a un margen (izquierdo o derecho); con la lámina a la derecha, al margen derecho. El color del logo depende de la pieza: blanco sobre oscuro y navy sobre claro. Si la zona es de tono medio, se baja la luz de la foto de forma natural. El motor lo resuelve con `theme='auto'` y el auditor F7 rechaza los logos que no se ven. El logo también va en zona limpia o sobre un soporte, nunca sobre madera iluminada o estantes (capturas 16 y 17).
6c. **Resaltados más frecuentes:** al menos 1 lámina por carrusel y 1 de cada 3 piezas llevan el resaltado que abraza el texto de «Exosomes» de Paola (`M.barra`) sobre la palabra gancho. Se revisa con `auditar_pieza.resaltados_ok(...)` al cerrar la tanda.
7. **Acento de color** en cada pieza: nodos, puntos o línea en dorado o azul claro, como en el cerebro de Paola.
8. **Logos estándar:** LCI principal 22 % W (la Dra., 10-oct-2026: un poquito más pequeño que el 25 % original para que no choque con los textos) · sello 150 px · terciario 118 px · wordmark CR ≈80 px de alto.
9. **Feed con contraste tonal:** al menos 1 de cada 3 portadas clara, nunca 3 oscuras seguidas, ninguna fila monótona. Revisar con `assets/auditar_feed.py`.
10. **Auditoría obligatoria:** `assets/auditar_pieza.py`. Una pieza con fallos F1–F5 o F7 no se entrega; F6 es un aviso. Revisar el `*_qa.png`. En los scripts de render, esperar `window.__lci_listo===true` antes de la captura.

## ⭐ ESTÁNDAR VISUAL 2026 — piso de calidad OBLIGATORIO (oct 2026)
El feed de Instagram de 42 publicaciones (137 piezas) aprobado por la Dra. es el NIVEL MÍNIMO a igualar o superar
en TODA pieza de LCI. Antes de diseñar: abrir (Read) `references/estandar-visual-2026/grid_feed_EN_2026.jpg` y
3–4 `references/estandar-visual-2026/posts/NN-*.jpg` del tipo más parecido, y leer
`references/estandar-visual-2026/ESTANDAR-VISUAL-2026.md` (ADN: foto siempre tratada, efectos de superficie
vidrio/movimiento/gradiente/ondas/microscopía, jerarquía recta/cursiva Mencken, objetos con volumen, variación y
ritmo; catálogo de las 42 con receta y efectos; checklist «¿está al nivel?»). Nada plano: si al ponerla junto al
grid se ve de menor nivel, se rehace antes de entregar.

**Catálogo visual de efectos:** `references/estandar-visual-2026/CATALOGO-EFECTOS.jpg` (la misma foto con cada tratamiento y efecto + la llamada de código). **Fotos:** usar el banco oficial del plugin `lci-fotos` (skill `lci-banco-fotos`: todas las fotos del feed 2026, piezas de Paola, CATALOGO.md con uso y tratamiento recomendado); no pedir que se vuelvan a subir.

**Diagramaciones guardadas (oct 2026):** `references/estandar-visual-2026/DIAGRAMACIONES.jpg` + `DIAGRAMACIONES.md` — 25 estilos aprobados (marco de líneas + conector, línea divisoria, recuadro-tarjeta de vidrio, recuadro-acento, barra que abraza, ficha de artículo, círculos, pasos, cifras, órbitas, red, etc.) con su receta. Mirarlos SIEMPRE antes de diagramar y combinar 2–4 estilos por serie; la Dra. no debe tener que volver a pedirlos.


## ⚠️ REGLA OBLIGATORIA — LOS 38 FONDOS (la Dra., 10-oct-2026: «es una regla que TIENES QUE CUMPLIR»)
Hay 38 fondos aprobados (lci-fotos → `fondos/`, `FONDOS.md`, `Catalogo-fondos-LCI.pdf`) en 15 familias:
degradés noche / acero / aurora / niebla clara (01–07) · ondas (08–10) · bacterias (11) · bokeh (12, nunca en portadas) ·
**galaxias (13–15)** · **mallas (16–18)** · **mesh oscuro (19–21)** · **mesh claro (22–26)** · foto tratada azul/bw/frío/cálido/ámbar/claro/natural (27–33) ·
vidrio estriado azul/cálido/color real (34–36) · movimiento cálido/azul (37–38).
1. ANTES de entregar cualquier tanda, feed o documento: `python3 assets/auditar_fondos.py <builds…>`. Ninguna familia puede quedar SIN USAR en un feed de 30+ piezas, y ninguna puede superar ≈12 % del total (la foto tratada es la excepción).
2. El vidrio estriado NO es el comodín: máximo 1 por carrusel y nunca en piezas contiguas del feed.
3. Para galaxia/malla/mesh usar `FXB('galaxia'|'galaxia_oro'|'malla'|'mesh_oscuro'|'mesh_claro')` (en feed_lanzamiento_build.py) o las recetas de fx.py documentadas abajo.
4. Si el auditor marca una familia sin usar, cambiar piezas de texto (r_centrado, r_cifras, r_palabra) a esa familia antes de entregar.

**Fondos aprobados:** catálogo de 38 fondos en el plugin `lci-fotos` → `lci-banco-fotos/FONDOS.md` + `fondos/` (+ `Catalogo-fondos-LCI.pdf`), cada uno con su función (`R.gradiente`, `R.ondas`, `R.bacterias`, `fx.galaxia`, `fx.malla`, `fx.mesh`, `R.tratar`, `R.vidrio`, `R.movimiento`). Elegir de ahí y regenerar a tamaño final; no repetir fondos (≤1–2 por documento, nunca contiguos).

## Flujo de trabajo
1. `import sys; sys.path.insert(0,'/mnt/skills/user/lci-piezas-graficas/assets'); import marca as M`
2. Elegir formato (`M.PRESETS`: story, post, post_v, carrusel, infografia, flyer, banner, email_sig, carnet…).
3. Construir con un **template** de alto nivel (`M.t_poster`, `M.t_concepto`, `M.t_concepto_hero`,
   `M.t_story`, `M.t_seal_hero`, `M.t_timeline`, `M.t_curso`, `M.t_cita`) o ensamblar a mano con los **helpers**
   (eyebrow, titular, hl, caja, conector, bullets, checklist, chips, goldbox, bloque_fecha,
   bloque_ubicacion, pill, logo…).
   - `t_poster`, `t_seal_hero` y `t_timeline` traen su **sistema tipográfico MEDIDO** del original de
     Paola escrito en ratios (ver docstring). `t_seal_hero` y `t_timeline` posicionan cada elemento en
     `position:absolute` por su ratio exacto — no dependen de flex — así el ritmo vertical cae idéntico.
   - `t_timeline` (afiche 'Creatine timeline / Muscle Cells', preset `poster_v` 1080×1620): eyebrow
     itálico + titular Mencken Head itálico + **timeline de gotas paramétrico** (`marks`=[(label,
     nivel 0..1)], líquido CLARO que baja con el nivel) + statement con palabra estrella + body Poppins.
     El eyebrow, las gotas, la línea punteada y la unidad quedan **justificados al ancho del titular**
     (columna = `inline-block` que se ajusta al titular; la tracking del eyebrow se calibra en el
     render para que sea UNIFORME, nunca `justify` por palabras que deja huecos desiguales).
   - `t_concepto_hero` (concepto 'Exosomes', preset `poster_v`, `theme` claro/oscuro): logo arriba +
     término estrella Mencken itálico + **sub-barra azul-gris que abraza el texto** (delicada) + cuerpo
     Poppins itálico. Elige el master itálico correcto según el tema (regla del criterio 10).
4. Escribir el HTML a archivo y renderizar a PNG exacto:
   `python3 scripts/render.py salida.html salida.png <formato> 2`  (2 = densidad retina).
5. **Verificar visualmente** el PNG contra las muestras de `references/muestras-paola/` antes de
   entregar, aplicando los **Criterios de diseño** de abajo (no solo comparar: ejercer criterio).
6. Entregar con `present_files` (PNG para publicar + HTML editable).

## Criterios de diseño (checklist de calidad — aplicar SIEMPRE, con criterio propio)
Estos criterios los exigió la Dra. y son mandatorios; no basta ejecutar, hay que juzgarlos en cada pieza:
1. **Contraste de colocación:** el logo y todo elemento claro van donde el fondo esté LIMPIO/OSCURO,
   nunca sobre el área cargada de partículas/luz. En `t_poster` se controla con `logo_pos`
   ('right' por defecto porque `bg_particulas` carga arriba-izquierda). Mirar el fondo real y decidir.
2. **Medir antes de reproducir:** al clonar una muestra, MEDIR el original en píxeles (cuerpos,
   interlínea, padding, aire entre bloques) y codificar en ratios; nunca adivinar tamaños.
3. **Ritmo:** interlínea APRETADA dentro de un bloque, aire AMPLIO entre bloques distintos (punto medio,
   ni pegado ni disperso).
4. **Jerarquía del titular:** línea recta en **Mencken bold** + acento en **cursiva** (Mencken Head
   italic), misma tipografía y mismo tamaño; la jerarquía es recta/cursiva, no peso ni tamaño.
5. **Centrado en cajas:** el texto debe quedar centrado PERFECTO en ambos ejes (el bearing itálico
   descentra; corregir con nudge en em). Verificar arriba≈abajo e izquierda≈derecha.
6. **Cápsula de contacto:** rectángulo con bordes redondeados (radio ~16px) en piezas tipo story;
   píldora (radio 60px) en el póster. Una sola línea, legible, sin cortar el teléfono.
7. **Sin contradicciones:** al editar el motor, revisar que docstrings, CSS y este SKILL queden
   consistentes con el código (no dejar reglas viejas que contradigan las nuevas).
8. **Columna justificada al titular:** cuando hay un titular ancho con elementos debajo (eyebrow,
   timeline, línea, unidad), TODOS se justifican al mismo ancho del titular (medido: Paola encolumna
   todo dentro del ancho de la palabra grande). El eyebrow se rellena con tracking UNIFORME, no con
   `justify` por palabras. Las series (gotas, íconos) usan `space-between`: primera al borde izq,
   última al derecho. Lo hace `t_timeline` automáticamente.
9. **Nivel que se LEE:** en indicadores de nivel (gotas, barras) sobre fondo oscuro, el relleno debe
   ser CLARO (no oscuro que se pierde sobre el navy); el nivel se mide del original (líquido claro,
   aire oscuro) y baja/sube según el dato.
10. **Master del itálico Mencken (regla medida en 11 piezas de Paola):** Mencken Std Head itálico trae
    solo DOS dibujos: **400** (abierto, contraste suave) y **800** (contraste extremo). **Nunca pedir
    700** (no existe; el navegador salta al 800 y sale grueso). Se elige por ROL, con `M.it_css(rol,…)`
    / `M.menc_it(…)`:
    - **`hero_oscuro` → 800**: la palabra ESTRELLA de la pieza cuando es CLARA sobre OSCURO (light-blue/
      crema/blanco sobre foto o navy). El contraste extremo brilla y le da presencia frente a la foto.
      Casos: 'Muscle Cells', 'longevidad.', 'Péptidos', 'ages too.', 'We know how to activate it.',
      'Thousand supplements', 'Some people in their 40s'.
    - **`hero_claro` → 400 + trazo 2.2%**: la palabra estrella cuando es NAVY sobre CLARO ('Exosomes',
      'Your lab results…', 'Acompañándote'). El 800 quedaría como mancha negra; el 400 engrosado da
      presencia con elegancia y conserva las letras abiertas del original.
    - **`acento` → 400 + trazo 2.5%**: acentos en CAJA ('Reclaim the energy', 'Los nuevos comienzos',
      'something important'). Medido: pesan casi como un protagonista, NO son delicados.
    - **`elegante` → 400 + trazo 1%**: sub-barras y líneas secundarias ('are cellular messengers',
      'Schedule your longevity assessment', 'Beneficios físicos', 'Pronto…', 'Soon…'). Voz de apoyo:
      nunca compite con la estrella. `.serif-it` y `.dh .it` del CSS son el 400 puro (base de este rol).
    Al clonar una pieza nueva, verificar el master **glifo a glifo** (forma de E/x/o/s y contraste),
    no solo el grosor: el 800 se distingue por su contraste grueso/fino extremo.

11. **Resaltados que ABRAZAN el texto (regla oct-2026, medida en Paola):** toda BARRA de resaltado
    (sub-barra bajo una palabra estrella: 'are cellular messengers', 'measure it once') va de la punta de los
    ascendentes a la base de los descendentes — sin aire vertical — y
    ~0.45em/0.55em de aire lateral. **Prohibido el resaltado "alto"** (padding vertical + line-height 1): la Dra. lo
    rechazó. OJO: el RECUADRO (caja-acento crema 'Antioxidant pills', caja de borde 'The study' / 'Reclaim') es otro
    elemento y conserva su aire propio aprobado. Barras siempre con `M.barra(txt, fs, M.it_css(rol, fs, color), fondo=… | borde=…)`, nunca a mano. Si la palabra
    de arriba tiene descendentes (p, g, y, paréntesis…), separar con `M.aire_desc(palabra, fs)` para que no toque la
    barra (caso 'Lp(a)').

12. **INTERLINEADO BLINDADO (regla dura oct-2026):** leer `references/estandar-visual-2026/INTERLINEADO-BLINDADO.md` y
    ver `INTERLINEADO-ejemplos-aprobados.jpg`. Titular display: line-height 1.0 y 0 de margen entre sus líneas;
    eyebrow/estrella/sub-barra PEGADOS a su titular (0.06–0.25 × fs titular); párrafos Poppins 1.32 (itálica) – 1.40
    (recta); aire ENTRE bloques 1.2–1.5 × cuerpo (con filete: 1.2 arriba / 0.9 abajo). Siempre con `M.ritmo(fs_tit, fs_cuerpo)`,
    nunca a ojo; medir en píxeles antes de entregar. Ni muy separados ni muy cerca.

13. **Conector de nodos = el de Paola ('The brain ages too'):** cada ítem tiene SU rama con punto en la unión,
    a la altura del centro de la x-height de la PRIMERA línea del ítem; texto a 0.68em del final de la rama en
    columna angosta (2–3 líneas, interlínea 1.28); la vertical baja del bloque superior hasta la última rama.
    Siempre `M.conector(items, fs)` (documentos: `E.marco(..., lista)`); verificado ±1px contra Paola. Prohibido:
    ítems en una sola línea larga separados de sus ramas.
14. **Versión en otro idioma = geometría IDÉNTICA a la aprobada:** al traducir una pieza o bloque (p. ej. «What is
    social jet lag?» → «¿Qué es el jet lag social?»), se conservan exactamente ancho del bloque, alineación, filetes,
    aires e interlineados; solo cambia el texto (cortes de línea equivalentes). La tinta de la primera letra de
    cada línea cae en el mismo borde: atributo `data-opt` + `M.OPTICA_JS` (alineación óptica que corrige la «j»
    itálica colgada y el «¿»). Verificar midiendo en píxeles las dos versiones lado a lado.

15. **JERARQUÍA DE TITULARES (regla dura oct-2026, tras el brochure):** un titular partido en líneas es UN bloque:
    Mencken bold + acento Mencken Head itálico al MISMO tamaño, line-height 1.0, cero margen entre líneas. Nunca
    cambiar de familia o peso a mitad de frase (prohibido «Medellín, tu destino» en Poppins bold + «de salud» en Poppins
    light). Eyebrow en versalitas = Poppins itálica light ~0.40× la estrella, PEGADO a ella (aire de tinta ≈0.20× estrella,
    medido en «Muscle Cells» de Paola) y justificado a su ancho — prohibido el eyebrow separado de su titular («UN EQUIPO,
    ··· un solo criterio.»). Prohibidos los marcadores/subrayados gruesos bajo el acento y las cajas altas: el acento se
    distingue por cursiva + color, o va en barra que abraza (`M.barra`). Usar SIEMPRE `titulos_lci.hd(...)` (estilos
    corregidos: plain, caps, block, panel, pills, tagbox, vrule, glass, rulesub, bar) y comparar contra
    `references/estandar-visual-2026/TITULOS-correctos.jpg`.

## Feed de Instagram de LCI (estándar oct 2026 — OBLIGATORIO para piezas de feed)
Antes de producir cualquier post o carrusel para @longevityclinicalinstitute, leer
`references/feed-instagram-lci.md`: idioma inglés, formato nativo 4:5 (`post_v`/`carrusel`, nunca
2:3 recortado), medidas de Paola (logo 25% W a 13%/9%, texto a la izquierda desde 43% H, cápsula de
contacto 7.5–92.5% W en todas las slides), dirección de foto, lista de PROHIBIDOS (eyebrows en
versalitas, glassmorphism, bandas claras con texto oscuro, botones píldora, párrafos largos) y qué
plantilla verificada usar por tipo de pieza.

**Fuentes — regla dura (oct 2026):** solo Poppins y Mencken Std / Mencken Std Head. No basta con declararlas: un glifo que no existe en ellas (✦ ◂ ▸ ₂ ‑ flechas, emojis) cae en una fuente del sistema. Antes de entregar, correr `assets/auditar_fuentes.py` sobre todas las piezas; debe salir 'OK'. Viñetas, flechas y adornos se dibujan en SVG; subíndices con <span> reducido en la misma fuente.

**Variación obligatoria (§9):** cada pieza/slide usa una receta de `assets/recetas_feed.py` (R1–R12: incluye R8 foto natural, R9 retrato, R10 pasos, R11 ficha de artículo para carruseles de evidencia, R12 dato con efecto `movimiento()`, R13 Word of the Day con `bokeh()`, R14 órbitas, R15 red de nodos, R16 ícono, sobre `gradiente()` sin foto; R17 portada limpia de tipografía gigante, R18 cita real, R19 cifras apiladas, R20 círculos problema/solución, R21 tarjeta de microscopía sobre `bacterias()`, R22 nodo luminoso, R23 tarjeta de datos (siempre 'Illustrative example'), R24 ondas 3D + píldora sobre `ondas()`; efectos `vidrio()` estriado y `pildora()` en línea). Portadas con foto, interiores con fondos o fotos recicladas con otro efecto, ≥1 portada limpia por fila — ver `references/ideas-feed-lci.md`,
un tratamiento de foto (`bw|ambar|calido|frio|azul|claro|natural`, recorte de detalle) y una variante/posición de logo
distinta a la anterior. Nunca repetir seguidas receta, tratamiento ni logo. Solo la marca es constante.

**Fondos dinámicos — regla dura de la Dra. (oct 2026):** en una tanda de carruseles, cada EFECTO de fondo aparece como máximo UNA vez (el vidrio estriado no es el comodín). Rotar entre: foto tratada (azul/bw/frío/cálido), foto desenfocada fuerte detrás de `r_tarjeta_micro`, `fx.galaxia`, `fx.malla` (intensidad ≤0.5, foco lejos del texto), `ondas()`, `bokeh()`, `movimiento()`, `gradiente()` (noche/aurora/acero/niebla, sin repetir nombre), `vidrio()` y retrato de la Dra. Lo mismo con las recetas: no tres `r_marco` en un mismo carrusel; alternar marco, red, órbitas, tarjeta, cifras, círculos. Revisar la hoja de contacto de la tanda antes de entregar.

**Perfil personal de la Dra. (marca «Carolina Rodríguez, MD», oct 2026):** mismo sistema LCI pero SIN logo de la clínica y SIN firmas tipográficas inventadas: se usa SIEMPRE su logo oficial `M.logo_cr()` — wordmark «CAROLINA / RODRÍGUEZ, MD / LONGEVITY MEDICINE» donde iría el logo principal (≈80 px de alto, recortado a su tinta, alineado al borde izquierdo del titular) y sello circular «CR · LONGEVITY MEDICINE» donde iría el sello o el terciario; recolorear con `mark_recolor` (blanco, beige, gold o navy según fondo). Cápsula `M.pill(institucional=False)`. Español. Línea editorial: brainspan con evidencia (copys profundos de 150–300 palabras, nivel de evidencia explícito, Vancouver).

## ⭐ BROCHURES, REVISTAS Y DOCUMENTOS MULTIPÁGINA (oct 2026) — reglas de la Dra. tras el brochure ES 2026
Aplican a brochure, revista, handout y cualquier documento de varias páginas (A4 = 1240×1754 px a 150 dpi; `M.PRESETS['brochure']=(1240,1754)`). Estándar «revista científica de lujo»: nunca plano.

### A. Fondos — NO repetir el mismo degradé
La Dra. reclamó que el degradé azul con foco dorado (`gradiente('aurora'/'noche')`) se repetía en demasiadas páginas. **Ningún fondo se usa más de 1–2 veces por documento ni en páginas contiguas**; alternar oscuras/claras y variar la familia. `assets/fx.py` (numpy/scipy/PIL; solo colores de marca):
- `galaxia(W,H,seed,tono,giro,centro,estr)` — nebulosa en espiral con estrellas (`tono='oro'` = toque dorado mínimo). Poner el centro en una esquina para que el texto quede en zona limpia.
- `malla(W,H,seed,focal,nx,ny,inten=)` — malla triangulada (Delaunay) con nodos luminosos. `inten` 1.0 solo con poco texto; **0.4–0.7 bajo texto** (si líneas/nodos cruzan el texto, bajar `inten` o mover `focal`).
- `mesh(W,H,grid,seed,warp,g)` — mesh gradient: cuadrícula de colores de marca interpolada y deformada. Oscuro: INK/NAVY/STEEL/SLATE/DEEP. Claro: WHITE/ICE/BLUE/SLATE. **En páginas claras NUNCA beige/cream→azul**; gold solo como toque mínimo en una página.
- Existentes: `gradiente('niebla'|'acero'|'noche'|'aurora')`, `ondas()`, `bacterias()`, `bokeh()` (nunca en portadas), `vidrio()`/`movimiento()` sobre fotos del banco. ≥1 de cada 3 páginas sin foto.
- Recetas probadas (1240×1754): `galaxia(W,H,2,'azul',3.2,(.74,.2))`, `galaxia(W,H,7,'oro',2.4,(.28,.12),1.4)`, `malla(W,H,4,(.72,.25),inten=.7)`, `malla(W,H,9,(.2,.75),10,14,inten=.38)`, mesh oscuro `[[DEEP,INK,NAVY],[INK,STEEL,SLATE],[NAVY,DEEP,INK],[STEEL*.8,NAVY,DEEP]]` (warp 70), mesh claro `[[WHITE,ICE,BLUE],[ICE,SLATE*1.12,WHITE],[WHITE,BLUE,ICE],[BLUE,WHITE,SLATE*1.1]]` (warp 60, g .012).
- Antes de entregar generar una **hoja de contactos** (miniaturas de todas las páginas) para detectar repetición de fondo, foto o diagramación.

### B. Biblioteca de diagramaciones de título (aportadas por la Dra.) — `assets/titulos_lci.py`
No repetir el mismo estilo en todo el documento: **≤2 usos por estilo y nunca en páginas consecutivas**. `T.hd(bold,acc,light,size,v=…)`; los estilos con filete/etiqueta propios eliminan el filete/kicker genérico (`T.consumir(inner)`):
1. `panel` (ref. «The brain ages too»): titular bold + acento italic dentro de recuadro de borde fino 1.6px translúcido + conector vertical; el cuadro abraza el texto (`fit-content`, `align-self:flex-start`).
2. `pills` (ref. «Healthspan»): título Poppins 700 grande (acento Poppins 300) + 2–3 píldoras de borde fino en versalitas + filete a todo el ancho.
3. `tagbox` (ref. «Antioxidant pills»): caja rellena gris-azul con texto itálico + titular Mencken bold + subtítulo Mencken regular (0.74×).
4. `caps` (ref. «Muscle Cells»): línea corta en versalitas con tracking + acento itálico a 1.5× el cuerpo.
5. `vrule` (ref. «It's not fitness»): borde izquierdo 3px, línea regular 0.9× y acento itálico debajo.
6. `glass` (ref. «Gut bacteria»): tarjeta redondeada 22px, borde fino, fondo translúcido + `backdrop-filter:blur`, sombra; título Poppins 600 + subtítulo Poppins italic 300.
7. `rulesub` (ref. «social jet lag»): titular Mencken bold + filete + subtítulo Poppins italic 300.
8. `bar` (ref. «Exosomes»): palabra Mencken itálica 1.18× + banda resaltada que abraza el texto (Poppins 600).
Extras: `plain`/`marker` (titular limpio: acento en cursiva + color, SIN marcador), `block` (acento en barra sólida que abraza el texto), `gold` (acento dorado, solo en fondo oscuro). Ver regla 15. Cuando la Dra. aporte nuevas referencias de título, agregarlas aquí y en `titulos_lci.py`.

### C. Maquetación editorial
- **TODO el texto corrido va JUSTIFICADO** (párrafos y descripciones de listas; `text-align:justify`, `lang="es"` en `<html>`), a una o dos columnas, con **guiones suaves** de `pyphen` (`Pyphen(lang='es').inserted(palabra,'\u00ad')`, solo palabras ≥7 letras y fuera de etiquetas): Chromium headless no silabea y sin esto salen «ríos» de espacios. Columnas angostas: cuerpo ≥28 px. No se justifican titulares, kickers, citas centradas ni la contraportada.
- **Citas destacadas:** recuadro de borde fino, texto itálico **centrado**, caja AJUSTADA al texto (`width:fit-content`, padding ~26/44 px), pestaña dorada centrada arriba, y la caja centrada en el espacio libre (márgenes `auto`).
- Letra capital, fotos de distintos tamaños (a sangre, en banda, asimétricas), cabecera corrida (oculta en páginas con foto a sangre arriba) y folios; márgenes ≥10 mm; fondo claro de marca para impresión.
- Una foto no se repite en el mismo documento: usar el banco `lci-fotos` con tratamiento (`tratar(...,'azul'|'natural'|'frio'|'bw')`), nunca cruda. Recortar para que se vea completo el equipo clave (p. ej. tensiómetro InBody); el pie de foto no va encima de texto de la foto.
- Portada con `t_poster` (eyebrow corto, p. ej. «Medicina de longevidad»; verificar centrado: aire arriba ≈ abajo medido en píxeles). La cápsula de contacto de `marca.py` trae @longevityclinicalinstitute: en español sustituir por **@institutoclinicodelongevidad** y (+57) 301 512 39 91; en inglés: @longevityclinicalinstitute, longevityclinicalinstitute.com y (+57) 300 002 71 15.
- Nombre de la doctora: «Dra. Carolina Rodríguez Morales» sin «, MD» (redundante con «Dra.»).
- **Contenido:** respetar el original; no reutilizar afirmaciones fuertes de mercadeo de terceros (p. ej. «absorción del 100% y resultados inmediatos», «rejuveneciendo desde la raíz», «pionera»): la Dra. las considera falsas/mercadeo barato. Redactar en lenguaje clínico sobrio y marcar para su revisión todo claim sin respaldo.
- Versión interactiva (flipbook): renderizar cada página a JPEG ~1000×1415 y montarlas en un motor de pasar página CSS-3D (doble ≥820 px, simple en móvil); sonido de papel suave con perfiles seleccionables.

## Estado de verificación de plantillas (estándar: "como si Paola lo hiciera")
Solo cuentan como ADN blindado las plantillas **verificadas 100% idénticas** a una pieza maestra
de Paola (medidas en píxeles, comparadas lado a lado y aprobadas por la Dra.):
- ✅ `t_poster` — afiche 'Reclaim the energy' (poster_brain_reprogram / banner_reclaim).
- ✅ `t_seal_hero` — story 'Your body knows how to heal' (post_exosomes_light = DNA).
- ✅ `t_timeline` — afiche 'Timeline of creatine / Muscle Cells' (poster_reclaim_blur).
- ✅ `t_concepto_hero` — concepto 'Exosomes' (poster_reclaim_face).
- ⚠️ `t_concepto`, `t_story`, `t_curso`, `t_cita` — aproximaciones anteriores al método de medición;
  NO están verificadas contra Paola. Antes de usarlas para una pieza real, medir la muestra
  correspondiente y promoverlas (o preferir la plantilla verificada más cercana).
Si una versión aprobada difiere del original de Paola, **gana Paola**: se corrige, no se conserva.

## Identidad de marca (resumen — detalle en MANUAL-LCI.md)
- **Paleta (5):** navy `#2A3649` (principal) · azul medio `#5D768C` (resaltar) · light blue
  `#CAD3DD` (sobre oscuro) · gold `#D2B58A` (apoyo, junto al medio) · cream `#EDE5DA` (fondos livianos).
- **Tipografía:** Mencken Std (display + textos largos "Text" + botón) · Poppins (títulos,
  subtítulos, cuerpo, itálicas de acento). Patrón firma: palabra-acento Mencken itálico
  (azul/crema/oro) + resto Mencken bold (blanco/navy). Todo embebido base64 (`fonts_brand.json`).
- **Logos (`logos_brand.json`):** `logo('principal'|'sello'|'terciario', tema)` con tema
  blanco/beige/gold/navy/claro. `principal` = wordmark apilado (default). Marca personal:
  `logo_cr('wordmark'|'sello', color=hex)` — solo cuando la Dra. lo pida.
- **Foto:** expresiones neutras (sin sonrisas fuertes), luz bioluminiscente, close-ups de
  células/ADN/neuronas; tratar con `lci_treat` (tritone/duo navy) + velo navy bajo texto.
- **Contacto (pill obligado al cierre):** institucional `M.pill()` o personal `M.pill(False)`.
- **Sub-paletas de fondo:** `M.GRAD_NAVY/_DEEP` (institucional) · `M.GRAD_CURSO` (azul eléctrico,
  curso de péptidos) · `M.GRAD_CREAM/_BLUE/_GRIS` (temas claros, usar `theme="light"`).

## Motivos firma disponibles (helpers en marca.py)
barra de resaltado `hl(txt,'blue'|'gold'|'mid'|'grey')` · caja de borde `caja()` · caja dorada
`goldbox()` · conector con nodos `conector([...])` · viñetas diamante `bullets([...])` · lista
check dorada `checklist([...])` · chips `chips([...])` · dato grande `stat()` · fecha
`bloque_fecha()` · ubicación `bloque_ubicacion()` · pill `pill()`.

## Catálogo y referencias
- `references/estandar-visual-2026/` — ⭐ grid + 42 posts aprobados (piso de calidad) + ESTANDAR-VISUAL-2026.md.
- `references/marca-oficial/MANUAL-LCI.md` — biblia de marca (paleta, tipografía, logo, foto, contactos).
- `references/marca-oficial/BRANDBOOK_*.pdf` — manual oficial fuente.
- `references/muestras-paola/` — 34 piezas maestras aprobadas = estándar visual a igualar.
- `references/catalogo-piezas.md` — recetas por tipo de pieza.
- `references/feed-instagram-lci.md` — estándar del feed de Instagram de LCI (medidas, prohibidos, foto, cuadrícula, §9 sistema de variación).
- `references/brief-fotografia-lci.md` — qué fotos comprar/producir (4 familias, sesión en clínica, stock).
- `references/ideas-feed-lci.md` — BANCO DE IDEAS aprobado para próximas publicaciones (fondos sin foto: degradados, bokeh, órbitas, red de nodos, ícono; tarjetas de datos; nodo luminoso; movimiento). Leer antes de planear un nuevo lote del feed. Regla: no todo es foto (≥1 de cada 3 sin foto).
- `assets/recetas_feed.py` — motor de variación: recetas R1–R7 + tratamientos de foto (`tratar`) + logos por variante/posición.
- `assets/papeleria/membrete_lci.png` — cabezote navy / textura de partículas.

## Expresión de las personas (regla de marca, Paola · 10-oct-2026)
En fotos de LCI y de la Dra. Carolina las personas se ven SERIAS, ELEGANTES y ASPIRACIONALES (alto perfil, alto poder adquisitivo), enfocadas en lo suyo. Nunca gente sonriendo a toda hora ni mirando a la cámara. Al elegir fotos del banco o de stock, descartar las que no cumplan; al generar con IA, la frase va en el prompt.


## REGLA DE ALINEACIÓN DE RESALTADOS (la Dra., 10-oct-2026) — TODOS los resaltados
- Texto a la IZQUIERDA: la primera letra del resaltado arranca en la misma vertical que la primera letra del titular de arriba (y del filete y el texto de abajo); poco azul al comienzo (0.16 em) que sobresale apenas a la izquierda; cola 0.30 em + 2 px a la derecha.
- Texto a la DERECHA (espejo): la última letra y el punto cierran en la vertical de la última letra del titular («medimos.» bajo la «e» de «Donde»); la barra sobresale un poco a la DERECHA (0.16 em + 2 px); 0.30 em de azul al comienzo.
- Bloque centrado: 0.40 em a cada lado.
- MISMO aire arriba y abajo de la tinta (round(0.09·fs)+2 px): la barra se ajusta a la tinta REAL de la palabra (sin reservar descendentes que no tiene, p. ej. «measure it once»).
- Motor: M.barra mide la tinta en el navegador (_BARRA_JS, canvas actualBoundingBox) y alinea con la primera/última letra del bloque anterior. alinear=True (izq, defecto) · "der" · False (centrado). Los recuadros con borde no cambian.
- Cuerpo en Poppins itálica bajo un titular: corregir el bearing de la itálica (≈ -4 px a 36 px).
- Versión en otro idioma: mismo tamaño y mismos cortes de línea que la aprobada; si el texto no cabe, ajustar la redacción (no achicar ni pasar a más líneas).


## REGLA DE VARIEDAD DE SOPORTES (la Dra., 10-oct-2026)
- La lámina de vidrio vertical «tipo ducha» le gusta mucho, pero NO se repite: máximo ~1 de cada 12 publicaciones y nunca en dos publicaciones seguidas ni dos veces en un mismo carrusel.
- Rotar entre TODOS los recursos del sistema: panel de vidrio a media pieza (mitad / mitad_sup), tarjeta de vidrio esmerilado ajustada al texto (vidrio), velo localizado (velo), panel crema claro con texto navy (PANEL_CLARO), velo claro de abajo hacia arriba (r_dato light), degradados de marca (cielo, cielo_crema, noche), vidrio estriado de fondo, duotono/tritono, ondas, microscopía, malla y galaxia (fx.py), resaltados y recuadros.
- Antes de entregar una tanda, contar qué soporte lleva cada pieza y cambiar los que se repitan.

## RECETAS NUEVAS (10-oct-2026)
- `R.r_panel_claro(bold, acc, cuerpo, fondo, lado="der")` — panel de vidrio crema con texto navy sobre foto clara (aprobado: «Del frasco / al plato»). Acento del feed, nunca dos seguidas.
- `r_natural(..., acc_col="#CAD3DD")` — color del acento en cursiva (variar colores; aprobado: «es parte de ti.» en azul claro).
- `r_natural(..., luz_sup=True)` — caída de luz amplia arriba para que el logo blanco se lea sobre fotos cargadas.
- Tarjeta `soporte_="vidrio"`: ancho mínimo fijo para que EN y ES queden idénticas.
- Cortes de línea forzados en subtítulos: usar `<br/>` (el `<br>` simple lo quita el texto fluido).

## AZUL DE PAOLA Y RECUADRO (la Dra., 10-oct-2026)
- `R.AZUL_PAOLA = "#AFCAE4"`: azul claro medido en «The brain ages too» de Paola (175,202,228), más vivo que #CAD3DD. Usarlo en ALGUNAS piezas (acento en cursiva sobre fondo oscuro, p. ej. `acc_col=R.AZUL_PAOLA`), alternando con el azul claro de paleta.
- `soporte_="recuadro"` en r_natural: el recuadro de Paola — filo claro fino (1.2 px, rgba(202,211,221,.42)) + relleno navy translúcido (rgba(12,20,34,.46)), sin desenfoque, abrazando el bloque con ≈34 px de aire. Alternativa elegante al vidrio (aprobado para «Inside LCI»).
- Antes de armar un feed, verificar qué piezas YA se publicaron en el perfil (p. ej. «The brain ages too» de Paola) y sacarlas.
- No repetir la misma foto de persona en dos portadas del mismo feed.

## ⚠️ REGLA DE COMPOSICIÓN CON PERSONAS (la Dra., 10-oct-2026)
- El texto NUNCA pasa por encima de la cara, la cabeza ni el pelo de la persona protagonista. Antes de ubicar el bloque, mirar dónde está la cara y poner el texto en la zona libre (regazo, fondo, lado contrario) con su soporte.
- El logo nunca va pegado ni al lado de un bloque de texto: va solo en su esquina, con aire alrededor.
- Si la comida, el objeto o la persona es la protagonista, el texto va donde no la tape (p. ej. panel arriba y el plato abajo, completo).
- Historias (1080×1920): logo y sello CR al MARGEN de 108 px arriba (11-oct-2026; antes 210, «demasiado abajo»); cápsula con top = H − 190. Recetas y fotos de los posts también sirven de fondo.

- **Historias: aire entre bloques** (Dra., 10-oct-2026, «los textos demasiado pegados»): en story (H>1500) `r_centrado` usa pila 0.95 × cuerpo menor, interlineado 1.16 en la línea serif y 1.5 en la nota. Si una foto tiene un elemento importante (ala, plato, cara), se desplaza la foto (extender cielo/mesa arriba) antes que montar texto encima.
- **Cápsula de contacto en historias** (Dra., 11-oct-2026): 1 cm más abajo → top = H − 190 (antes H − 310); referencias a 210 px del borde. Mismo criterio en LAI (handle a H − 165).
