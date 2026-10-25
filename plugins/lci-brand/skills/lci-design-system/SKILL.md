---
name: lci-design-system
description: "Sistema de diseño gráfico maestro del Longevity Clinical Institute (Dra. Carolina Rodríguez). Motor único de marca para TODOS los documentos clínicos HTML (planes nutricionales, deportivos y de optimización del sueño, handouts, reportes). Define la paleta, tipografías embebidas (Poppins + Mencken Std), logos, el sistema de componentes visuales nivel editorial (\"estilo Paola\"), y el pipeline de tratamiento de imagen (duotono/tritono navy-gold-cream). Úsalo SIEMPRE que se construya cualquier documento visual de LCI para garantizar que el resultado sea 100% idéntico al estándar de marca. Este skill es invocado por plan-nutricional, plan-deportivo y plan-sueno.\n"
---

## 🛑 Antes de diseñar (11-oct-2026): leer y aplicar el bloque «ANTES DE DISEÑAR Y ANTES DE ENTREGAR» de lci-piezas-graficas/SKILL.md (soporte distinto por pieza, aire sobre la cabeza, logo al margen de 108 px, revisar cada PNG). Vale también para documentos.

# LCI — Sistema de Diseño Maestro (motor de marca)

Este skill es la **única fuente de verdad** del estilo gráfico de LCI. Cualquier plan o
handout se construye importando este motor. No se reinventa el diseño en cada sesión: se
ensambla con estos componentes fijos. Así todos los documentos quedan idénticos.

## REGLA INQUEBRANTABLE — interlineado con resaltado (10-oct-2026)
Cuando un bloque de texto lleva RESALTADO (barra que abraza el texto), el interlineado del bloque SUBE un poco: la barra NUNCA invade la línea de arriba ni la de abajo. Aire mínimo entre la barra y la tinta vecina: max(10 px, 12 % del alto de la barra). El auditor lo bloquea (F9). Sin excepciones.

## Regla de oro
**NUNCA recrear el CSS, los colores, las fuentes o los componentes a mano.** Siempre
importar `brand.py`. Si un documento no usa `brand.py`, está mal hecho.


## ⭐⭐ Piezas para redes y documentos visuales: reglas de lectura y márgenes (10-oct-2026)
Toda pieza gráfica (post, story, reel, banner, portada) se rige por `lci-piezas-graficas/references/correcciones-2026-10-10/REGLAS-10-OCT-2026.md`:
- Zona segura del 10 % del lado más corto en los 4 lados. Solo la cápsula o la web pueden ir en la banda inferior.
- Piso tipográfico: 19 px (cápsula), referencias 20, rótulos 22, cuerpo 27, medidos a 1080 de ancho.
- Interlineado de bloque uniforme y recuadros simétricos.
- Contraste de 4.5:1 o más (titulares de 7:1 o más). En fondo claro, navy.
- Logos a su tamaño estándar y feed con ritmo tonal (1 de cada 3 claras).
- Sobre una foto cargada se usan soportes de lectura (vidrio opaco a media pieza, tarjeta de vidrio, resaltado, cápsula o recuadro), en lugar de oscurecer toda la foto.
- Auditoría con `lci-piezas-graficas/assets/auditar_pieza.py`.

En documentos impresos sigue rigiendo el margen de 10 mm o más. Además, ningún texto de lectura va por debajo del piso de cuerpo proporcional, y las cajas mantienen la simetría y el contraste.

## ⭐ ESTÁNDAR VISUAL 2026 — piso de calidad OBLIGATORIO (oct 2026)
La Dra. aprobó el feed de Instagram de 42 publicaciones como el nivel mínimo de TODO LCI y pidió que los
documentos **dejen de salir planos**. Antes de construir cualquier documento:
1. Mirar (Read) `lci-piezas-graficas/references/estandar-visual-2026/grid_feed_EN_2026.jpg` y el ejemplo
   `references/demo-efectos-documento-2026.jpg`.
2. Leer `references/estandar-visual-documentos.md` (tabla «antes plano → ahora» y reglas).
3. Construir con `assets/efectos_lci.py` ENCIMA de `brand.py`: hero con foto tratada (`E.hero(E.foto(...))`),
   bandas separadoras con vidrio estriado / degradado de marca / ondas (`E.banda`), cifras gigantes (`E.cifras`),
   pasos con nodos (`E.pasos`), círculos de comparación (`E.circulos`), tarjetas de vidrio (`E.tarjeta`),
   cápsula en línea (`E.pildora`). CSS: `B.html_doc(...).replace('</style>', E.css()+'</style>', 1)`.
4. Verificar el render al lado del grid; si se ve más plano que el feed, rehacer. Fuentes: correr
   `lci-piezas-graficas/assets/auditar_fuentes.py` (debe salir OK).
**INTERLINEADO BLINDADO (brochures, documentos, presentaciones):** aplicar `lci-piezas-graficas/references/estandar-visual-2026/INTERLINEADO-BLINDADO.md` con `E.ritmo(fs_titular, fs_cuerpo)` — titulares line-height 1.0 sin margen entre líneas, párrafos 1.32–1.40, aire entre bloques 1.2–1.5 × cuerpo, entre secciones 2.5–3 × cuerpo. Medir antes de entregar.
**Traducciones y conectores:** la versión en español de un bloque aprobado en inglés (o viceversa) es IDÉNTICA en geometría — usar `E.documento(B, título, body)` (incluye CSS + alineación óptica `data-opt`), `E.linea` (réplica exacta de 'What is social jet lag?') y `E.marco(..., lista)` con el conector de Paola (una rama por ítem alineada a su primera línea).
**Jerarquía de titulares (brochures/documentos):** regla 15 de lci-piezas-graficas — titular = Mencken bold + acento itálico mismo tamaño, lh 1.0, sin aire entre líneas; eyebrow versal pegado y justificado al ancho de la estrella; sin marcadores gruesos. Usar `titulos_lci.hd(...)` y comparar con `TITULOS-correctos.jpg`.
**Resaltados:** toda barra/caja de resaltado abraza el texto (sin aire vertical) — `E.barra(...)`; prohibidos los resaltados «altos» (regla oct-2026).
Las referencias LOCKED fijan la ESTRUCTURA y el contenido de cada plan; la capa visual sube a este estándar.
Teléfono por idioma: `B.IDIOMA='es'` (301 512 39 91, default) · `B.IDIOMA='en'` (300 002 71 15).

**Catálogo visual de efectos:** `lci-piezas-graficas/references/estandar-visual-2026/CATALOGO-EFECTOS.jpg` (la misma foto con cada tratamiento y efecto + la llamada de código). **Fotos:** usar el banco oficial del plugin `lci-fotos` (skill `lci-banco-fotos`: todas las fotos del feed 2026, piezas de Paola, CATALOGO.md con uso y tratamiento recomendado); no pedir que se vuelvan a subir.

**Diagramaciones guardadas (oct 2026):** `lci-piezas-graficas/references/estandar-visual-2026/DIAGRAMACIONES.jpg` + `DIAGRAMACIONES.md` — 25 estilos aprobados (marco de líneas + conector, línea divisoria, recuadro-tarjeta de vidrio, recuadro-acento, barra que abraza, ficha de artículo, círculos, pasos, cifras, órbitas, red, etc.) con su receta y su función de documento (`E.marco`, `E.linea`, `E.recuadro`, `E.barra`, `E.pasos`, `E.cifras`, `E.circulos`). Mirarlos SIEMPRE antes de diagramar y combinar 2–4 estilos por serie; la Dra. no debe tener que volver a pedirlos.

**⚠️ OBLIGATORIO (la Dra., 10-oct-2026):** usar y ROTAR las 15 familias de los 38 fondos (incluidas galaxias, mallas y mesh claro/oscuro); en documentos de varias páginas, cada página con fondo usa una familia distinta. Auditor: `lci-piezas-graficas/assets/auditar_fondos.py`.

**Fondos aprobados:** catálogo de 38 fondos en el plugin `lci-fotos` → `lci-banco-fotos/FONDOS.md` + `fondos/` (+ `Catalogo-fondos-LCI.pdf`), cada uno con su función (`R.gradiente`, `R.ondas`, `R.bacterias`, `fx.galaxia`, `fx.malla`, `fx.mesh`, `R.tratar`, `R.vidrio`, `R.movimiento`). Elegir de ahí y regenerar a tamaño final; no repetir fondos (≤1–2 por documento, nunca contiguos).

## Archivos del motor (`assets/`)
- **`brand.py`** — módulo central. Expone:
  - `B.base_css()` → CSS completo (fuentes @font-face base64 + paleta + TODO el sistema de
    componentes). Va dentro de `<style>`.
  - `B.html_doc(title, body)` → envuelve el documento + botón flotante "Imprimir / Guardar PDF".
  - `B.footer()` → footer institucional con logo, nombre y pill de contacto.
  - `B.LOGO_LEFT`, `B.LOGO_SEAL` (crema transparente, para hero navy), `B.LOGO_LEFT_NAVY`,
    `B.LOGO_SEAL_NAVY` (recoloreados para fondos claros) → data URIs listos.
  - `B.contact_pill()`, `B.seal_svg()`.
- **`lci_treat.py`** — pipeline de tratamiento de imagen. Convierte cualquier foto
  licenciada en "familia LCI". Modos: `grade` (comida apetitosa + unificada — DEFAULT para
  fotos de comida), `tritone` (gradient-map firma navy·gold·cream, para texturas/heroes con
  mucho texto), `duo` (navy→cream minimalista). Más `text_overlay(side=...)` para velos de
  legibilidad. Determinista: mismos parámetros → mismo resultado.
- **`assets.json`** — fuentes (Poppins 200/400/400it/500/600/700, Mencken Std 400/700,
  Mencken Std Head 400) y logos, todo base64. `brand.py` lo lee solo.
- **`efectos_lci.py`** — capa de efectos del estándar 2026 (usa las funciones de imagen de
  `lci-piezas-graficas/assets/recetas_feed.py`: una sola implementación para redes y documentos).
- **`fonts/`** — copias .ttf/.otf decodificadas (solo si se necesita rasterizar texto sobre
  una imagen con Pillow; los planes usan @font-face de `assets.json`, no esto).

## Paleta (la única)
navy `#2A3649` · light blue `#CAD3DD` · gold `#D2B58A` · cream `#EDE5DA`.
Tipografía: **Mencken Std** (display/títulos, con su variante *Head* itálica para acentos)
+ **Poppins** (cuerpo, 300 para texto corrido). Mencken reemplaza a Playfair Display.

## Convenciones de marca 2026 (transversales — aprobadas por la Dra.)
Aplican a TODO documento LCI. (Las mismas rigen el skill `lci-piezas-graficas`; aquí van las que
corresponden a documentos clínicos.)

1. **Tipografía mixta regular + cursiva (Mencken):** en un mismo renglón, el texto regular va
   **sin negrita** (Mencken Std 400) y la palabra/frase en cursiva va **en negrita** (Mencken Std
   Head itálica **800**). En títulos display de líneas separadas, la línea de apoyo regular puede ir
   en negrita (Mencken Std 700).
2. **Versales (etiquetas/eyebrows):** tracking discreto ~`.10em`. Nunca tracking amplio (`.40em`).
3. **Jerarquía de color (oro mínimo):** el **oro `#D2B58A`** es acento de lujo MUY puntual — máx.
   1–2 elementos por página (palabra-título de sección o dato clave / sello). El resto del rol
   estructural y de acento va en **azul medio `#5D768C`** (subrayados, filetes, conectores, marcos)
   y **navy `#2A3649`** (títulos de sección, texto). **Azul claro `#CAD3DD`** para rellenos/bordes de
   recuadro y para texto sobre fondos oscuros. Sobre fondo claro no usar azul claro para texto.
4. **Fotografía — distinguir tipo:**
   - **Comida / lifestyle (planes de nutrición):** CÁLIDA y apetitosa → `treat(img, mode='grade')`.
     **No** enfriar la comida.
   - **Marca / clínica / científica (equipos, escena de consulta, células, retratos clínicos):**
     **fría con color real** → `treat_cool(img)` (balance frío suave; nunca cálida, nunca B/N, nunca
     duotono fuerte). Equipo/alta clave con defaults; escenas con personas `tint=0.0`.
5. **Respiración y saltos:** espacios amplios entre bloques (no apeñuzar); controlar saltos con
   `<br>`/`&nbsp;` para evitar palabras huérfanas y mantener juntas las frases lógicas.
6. **Consistencia entre piezas de una serie:** mismo tamaño de texto, interlineado y ritmo de
   renglón; logos, márgenes y estilo de recuadros idénticos.

7. **Piezas de redes (feed de Instagram LCI):** se rigen por el lenguaje de Paola medido en
   `lci-piezas-graficas/references/feed-instagram-lci.md` (inglés, 4:5 nativo, logo 25% W, texto a la
   izquierda desde 43% H, acento Mencken it. en caja azul acero #94B4CC, cápsula de contacto en todas
   las piezas; sin eyebrows en versalitas, sin glassmorphism, sin botones píldora). Las piezas de redes
   se producen SIEMPRE con `lci-piezas-graficas`, nunca con este motor de documentos.
   **Variación:** en redes, solo la marca se repite (tipografías, paleta, cápsula, márgenes); receta,
   tratamiento de foto, escala del titular y variante/posición de logo cambian pieza a pieza
   (§9 de feed-instagram-lci.md; fotos: brief-fotografia-lci.md).
   **Datos de LCI confirmados (oct 2026)** para cualquier texto de marca (redes, brochure, web): muestras procesadas in
   house, en Colombia y en EE. UU.; IA clínica propia con pruebas neurocognitivas propias; edad biológica con varios relojes
   biológicos; primera consulta de mínimo 2 horas; plan según lo que el caso necesita (nunca "12 puntos"); órdenes en 48 h;
   protocolos de hasta ~10 días según el protocolo; costo estimado con los primeros resultados; logística y equipo bilingüe.
   Misión y visión oficiales y reglas de revisión aprobadas: §7.1 y §9.6b de feed-instagram-lci.md.
   **Reglas de imagen aprobadas:** sin fotos repetidas entre portadas; retrato de la Dra. integrado en foto real
   desenfocada de la clínica (nunca recorte sobre fondo plano); texto claro (#E3EBF3) sobre fotos oscuras; réplicas de
   Paola con su tinte exacto.
   **Variedad de formatos (oct 2026):** no todas las piezas son foto; ideas aprobadas (degradados de marca, bokeh, órbitas,
   red de nodos, íconos, tarjetas de datos, nodo luminoso, efecto movimiento) en `lci-piezas-graficas/references/ideas-feed-lci.md`.

## Cómo construir CUALQUIER documento (recipe)
1. `import sys; sys.path.insert(0,'/mnt/skills/user/lci-design-system/assets'); import brand as B`
2. Construir el `body` ensamblando secciones con las clases del sistema (ver
   `references/design-recipe.md` para el catálogo completo de componentes).
3. `html = B.html_doc("Título", body)` → escribir a archivo.
4. Render de verificación con Chrome headless → screenshot antes de entregar.
5. Entregar con `present_files`. Indicar: abrir → Ctrl/Cmd+P → Guardar como PDF.

## Referencias BLOQUEADAS (`references/`)
- `REF_nutricional_LOCKED.html`, `REF_deportivo_LOCKED.html`, `REF_sueno_LOCKED.html` — los
  tres planes de la paciente Diana María Muñoz Ospina. Son el **estándar visual aprobado**.
  Todo plan nuevo debe verse idéntico a estos (misma estructura, mismos componentes, mismo
  ritmo). Cambia el CONTENIDO clínico; nunca el diseño.
- `design-recipe.md` — catálogo de componentes + reglas de imagen + estructura de cada plan.
- `build/` — los builders de Diana como **plantilla-ejemplo**. Para un paciente nuevo: copia
  el builder correspondiente, reemplaza SOLO el contenido clínico, conserva idénticas todas
  las llamadas de marca y la estructura.

## Tratamiento de imagen (handouts con fotos licenciadas)
- Comida apetitosa → `grade`. Texturas/abstractos/heroes con texto → `tritone`.
- Toda foto bajo texto lleva velo navy (linear-gradient rgba(25,34,46,...)) para legibilidad.
- Restricción: las fotos marcan el ritmo (hero, banda editorial, banner de sección). NO se
  pone foto en cada sección. Secciones densas (tablas, listas) van sin foto.
