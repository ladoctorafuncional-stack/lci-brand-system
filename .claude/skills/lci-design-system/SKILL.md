---
name: lci-design-system
description: "Sistema de diseño gráfico maestro del Longevity Clinical Institute (Dra. Carolina Rodríguez). Motor único de marca para TODOS los documentos clínicos HTML (planes nutricionales, deportivos y de optimización del sueño, handouts, reportes). Define la paleta, tipografías embebidas (Poppins + Mencken Std), logos, el sistema de componentes visuales nivel editorial (\"estilo Paola\"), el pipeline de tratamiento de imagen (duotono/tritono navy-gold-cream), y el flujo continuo de paginación al imprimir/exportar PDF. Úsalo SIEMPRE que se construya cualquier documento visual de LCI para garantizar que el resultado sea 100% idéntico al estándar de marca y que la impresión no deje páginas con espacio en blanco. Este skill es invocado por plan-nutricional, plan-deportivo y plan-sueno."
---

---
name: "lci-design-system"
description: "Sistema de diseño gráfico maestro del Longevity Clinical Institute (Dra. Carolina Rodríguez). Motor único de marca para TODOS los documentos clínicos HTML (planes nutricionales, deportivos y de optimización del sueño, handouts, reportes). Define la paleta, tipografías embebidas (Poppins + Mencken Std), logos, el sistema de componentes visuales nivel editorial (\"estilo Paola\"), el pipeline de tratamiento de imagen (duotono/tritono navy-gold-cream), y el flujo continuo de paginación al imprimir/exportar PDF. Úsalo SIEMPRE que se construya cualquier documento visual de LCI para garantizar que el resultado sea 100% idéntico al estándar de marca y que la impresión no deje páginas con espacio en blanco. Este skill es invocado por plan-nutricional, plan-deportivo y plan-sueno."
---


# LCI — Sistema de Diseño Maestro (motor de marca)

Este skill es la **única fuente de verdad** del estilo gráfico de LCI. Cualquier plan o
handout se construye importando este motor. No se reinventa el diseño en cada sesión: se
ensambla con estos componentes fijos. Así todos los documentos quedan idénticos.

## Regla de oro
**NUNCA recrear el CSS, los colores, las fuentes o los componentes a mano.** Siempre
importar `brand.py`. Si un documento no usa `brand.py`, está mal hecho.

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

## Cómo construir CUALQUIER documento (recipe)
1. `import sys; sys.path.insert(0,'/mnt/skills/user/lci-design-system/assets'); import brand as B`
2. Construir el `body` ensamblando secciones con las clases del sistema (ver
   `references/design-recipe.md` para el catálogo completo de componentes).
3. `html = B.html_doc("Título", body)` → **luego aplicar el flujo continuo de impresión**
   (sección siguiente, OBLIGATORIO) → escribir a archivo.
4. Render de verificación con Chrome headless o `--print-to-pdf` antes de entregar. Revisar
   que ninguna página quede con más de ~25% de espacio en blanco al final (ver benchmark abajo),
   que ninguna tarjeta salga seccionada y que las franjas de 10 mm arriba/abajo salgan en crema.
5. Entregar con `present_files`. Indicar: abrir → Ctrl/Cmd+P → Guardar como PDF.

## ⚠️ Paginación de impresión — flujo continuo (OBLIGATORIO, en TODAS las secciones)

**Causa de fondo (diagnosticada y corregida):** `brand.py` trae en su bloque `@media print`
dos reglas que, combinadas, generan páginas con la mitad en blanco:
1. `break-before:page` en **toda** `.section` / `.dark-section` → cada sección abre hoja
   nueva sin importar cuánto contenido tenga.
2. La clase `.avoid-break` (`page-break-inside:avoid`) puesta sobre **contenedores grandes**
   (tarjetas con varias zonas, `.bracket`, grids de 2-4 columnas, tablas largas) → si ese
   bloque grande no cabe entero en lo que queda de página, salta completo a la siguiente y
   deja el encabezado solo arriba con el resto de la hoja vacía.

Además `.bracket` es `display:grid`, y los navegadores **no fragmentan contenedores grid**
al imprimir: saltan enteros sí o sí, sin importar el CSS de paginación.

**La corrección probada (WeasyPrint, medido sobre 3 planes reales — Nutrición/Ejercicio/Sueño):
44 → 35 páginas, cola de página vacía promedio 28% → 9%, páginas con >25% de hueco interior
19 → 1.** Filosofía: *todo fluye de forma continua por defecto; solo son indivisibles los
títulos, encabezados e imágenes.*

**Aplicación — obligatoria en cada build, para TODAS las secciones sin excepción:**

Al final de cada script builder, definir (o copiar) este helper y envolver siempre el
`html_doc()` con él antes de escribir el archivo:

```python
PRINT_FIX = """
/* ===== LCI · FLUJO CONTINUO DE IMPRESIÓN (obligatorio, aplica a TODAS las secciones) ===== */
@media print{
  /* 1. NADA fuerza hoja nueva: el documento fluye de principio a fin. */
  .section,.section.alt,.dark-section,.band-intro,.keep-with-prev,.avoid-break{
     break-before:auto!important;page-break-before:auto!important;}

  /* 2. TODO es fragmentable por defecto (anula el avoid-break del motor sobre
        contenedores grandes, que era la causa de fondo de las páginas vacías). */
  *{break-inside:auto!important;page-break-inside:auto!important;}

  /* 3. ÚNICAS excepciones: títulos, encabezados, imágenes y TARJETAS INDIVIDUALES.
        Regla de equilibrio: la PIEZA pequeña es indivisible; el CONTENEDOR grande que
        la agrupa NO. Así una tarjeta nunca sale seccionada por la mitad y, a la vez,
        no reaparecen las páginas medio vacías. */
  img,svg,.sec-ico,.ring,.zn,.nc,tr,.hero,.band-intro,.patient-card,
  .sec-head,h1,h2,h3,.dn,.nt,.ft,.wh,.pill-quote,
  .fitt,.zone,.numitem,.warn,.note,.patient-card .cell,
  /* TARJETAS: ninguna tarjeta puede salir seccionada por la mitad —incluidas las
     oscuras de suplementos (.dark-card: «Vitamina D3/K2», «Complejo B metilado») y
     las celdas del grid de categorías de alimentos. NO QUITAR de esta lista. */
  .card,.dark-card,.recipe-card,.suppl-card,
  .ring-row>*,.fitt-grid>*,
  .avoid-break:not(section):not(.dark-section):not(.day):not(table){
     break-inside:avoid!important;page-break-inside:avoid!important;}

  /* 4. Un título nunca queda solo al pie: se pega a lo que sigue. */
  .sec-head,h1,h2,h3,.dark-card h3,.dn,.nt,.wh,thead{
     break-after:avoid!important;page-break-after:avoid!important;}
  .sec-head + .lead,.sec-head + .card,.sec-head + .dark-card,.sec-head + .bracket{
     break-before:avoid!important;page-break-before:avoid!important;}
  thead{display:table-header-group!important;}

  /* 5. Grid no fragmenta al imprimir -> .bracket pasa a bloque, filete conservado. */
  .bracket{display:block!important;}
  .bracket .line{display:none!important;}
  .bracket .items{border-left:1.5px solid var(--blue-mid);padding-left:20px!important;}

  /* 6. Aire recortado: mismo ritmo visual, menos hoja desperdiciada. */
  .section,.section.alt{padding-top:22px!important;padding-bottom:22px!important;}
  .dark-section{padding-top:26px!important;padding-bottom:26px!important;}
  .sec-head{margin-bottom:15px!important;}
  .lead{margin-bottom:13px!important;}
  .quote{margin-top:18px!important;}

  /* 7. Footer compacto y pegado: nunca se va solo a una hoja final. */
  .foot{break-before:avoid!important;page-break-before:avoid!important;
     break-inside:avoid!important;padding:20px 34px 22px!important;}
  .foot img{height:40px!important;margin-bottom:10px!important;}

  /* 8. Sin viudas ni huérfanas. */
  p,li,.lbl{orphans:3;widows:3;}

  /* 9. MARGEN FÍSICO DE 10 mm ARRIBA Y ABAJO (obligatorio).
        Toda impresora tiene un área no imprimible en los bordes; con `margin:0`
        el texto y las tarjetas llegaban al filo del papel y la impresora los
        recortaba. 10 mm arriba/abajo dejan ese margen de seguridad.
        Los laterales quedan en 0 a propósito: heros, bandas y secciones siguen
        sangrando de borde a borde en horizontal (el aire lateral del texto ya lo
        da el padding de 34px de `.section`/`.hero`/`.foot` en impresión).
        Este @page va DESPUÉS del `@page{margin:0}` de brand.py, así que gana en
        la cascada; no hay que tocar brand.py. */
  /* La `background` del @page pinta TODA la hoja, franjas incluidas (WeasyPrint). */
  @page{margin:10mm 0;size:letter;background:#EDE5DA;}

  /* 10. Las franjas de 10 mm NO pueden salir blancas: van en crema de marca.
         Dos mecanismos a propósito, porque cada motor implementa uno:
         · `@page{background}`  -> pinta la hoja completa en WeasyPrint.
         · `html{background}`   -> se propaga al lienzo de impresión en Chrome.
         El que no aplique se ignora sin efectos secundarios. NO quitar ninguno. */
  html{background:#EDE5DA!important;}

  /* 11. ESCAPE POR TAMAÑO — `.frag-ok` (excepción a la regla 3).
         La regla 3 blinda TODAS las tarjetas, y eso está bien para las normales.
         Pero una tarjeta que por sí sola ocupa más del ~60% del alto útil de la
         hoja no cabe casi nunca en lo que queda de página: si es indivisible,
         salta entera a la siguiente y deja el encabezado solo con media hoja en
         blanco. A ESAS —y solo a esas— se les devuelve el permiso de partirse.
         Cómo se usa: el builder mide la tarjeta y, si supera el umbral, le añade
         la clase `frag-ok` en el HTML (p. ej. `<div class="dark-card frag-ok">`).
         Nunca se aplica «por si acaso»: una tarjeta pequeña con `.frag-ok` vuelve
         a producir el defecto de la foto de la doctora.
         Umbral: alto útil de carta con margen 10 mm ≈ 259 mm → fragmentable si la
         tarjeta mide más de ~155 mm (≈ 585 px CSS a 96 dpi).
         La clase se escribe repetida a propósito: sube la especificidad por encima
         del selector con `:not(...)` de la regla 3, sin tener que reordenar nada. */
  .frag-ok.frag-ok.frag-ok.frag-ok{
     break-inside:auto!important;page-break-inside:auto!important;}
}
"""

def finish(html, lang='es', print_label='Imprimir / Guardar PDF'):
    """Envolver SIEMPRE el resultado de B.html_doc(...) con esto antes de escribir el archivo."""
    html = html.replace('</style>', PRINT_FIX + '</style>', 1)
    html = html.replace('<html lang="es">', f'<html lang="{lang}">')
    html = html.replace('Imprimir / Guardar PDF', print_label)
    return html

# Uso al final del builder:
# html = finish(B.html_doc("Título", body))
# open(out,'w',encoding='utf-8').write(html)
```

### Tarjetas que nunca se parten (regla nacida de una foto real — NO SE PUEDE PERDER)

La Dra. Carolina Rodríguez mandó una foto de un plan impreso con la tarjeta oscura de
suplementos **«Complejo B (metilado)»** cortada por el borde inferior de la hoja, con la palabra
«vegetal)» huérfana arriba de la página siguiente, y el mensaje: **«que es esto tannnn feo»**.
La causa era que el `PRINT_FIX` excluía `.card` y `.dark-card` del `break-inside:avoid`. Esta es
la regla que lo corrige, y **no se puede volver a perder**:

1. **Las tarjetas y las piezas pequeñas NUNCA se fragmentan.** `.card`, `.dark-card`,
   `.recipe-card`, `.suppl-card`, `.fitt`, `.zone`, `.numitem`, `.warn`, `.note`, las celdas
   del grid de categorías de alimentos, las filas de tabla, los títulos y las imágenes llevan
   `break-inside:avoid`. Prohibido sacar `.dark-card` de esa lista: es exactamente el error
   que produjo la foto.
2. **Los contenedores grandes SÍ se fragmentan.** `section`, `.dark-section`, `.day` y las
   tablas siguen partiéndose entre páginas. Blindarlos es lo que generaba las páginas medio
   vacías; el equilibrio es *pieza pequeña indivisible / contenedor grande divisible*.
3. **Excepción por tamaño — la tarjeta gigante se marca como fragmentable.** Si una tarjeta
   por sí sola pasa del **~60 % del alto de la hoja**, blindarla deja el encabezado solo con
   media página en blanco. En ese caso el builder le añade la clase **`.frag-ok`** en el HTML
   (`<div class="dark-card frag-ok">…`) y la regla 11 del `PRINT_FIX` le devuelve
   `break-inside:auto`. Es una regla **general y reutilizable del CSS**, no un parche medido
   documento por documento: se decide midiendo la tarjeta al construirla (umbral ≈ 155 mm /
   585 px CSS sobre carta con margen de 10 mm). Ejemplo típico: la línea de tiempo del ritual
   nocturno del plan de sueño, que ocupa el 73 % de la hoja.
4. **`.frag-ok` no se pone «por si acaso».** Aplicarla a una tarjeta normal reintroduce el
   defecto original.

**Verificado sobre 511 planes reales** (2026-07-31): tarjetas de suplementos completas, el grid
«Verduras / Frutas / Proteínas / Despensa y varios» entero en una página, franjas de 10 mm en
crema exacto `#EDE5DA`, ningún texto al filo del papel y **menos** páginas que antes
(16→14, 14→11, 14→11), con el hueco medio al pie del documento bajando de 34-41 % a 14-19 %.

### Margen de impresión de 10 mm (regla de la Dra., obligatoria)
Los planes se imprimen **en papel**. Con `@page{margin:0}` el contenido llegaba al borde
físico y la impresora lo recortaba (texto al filo, tarjetas seccionadas). Por eso el
`PRINT_FIX` fija **`@page{margin:10mm 0}`**: 10 mm de aire arriba y abajo, 0 a los lados.
- **Los colores del fondo se mantienen:** `html{background:#EDE5DA}` propaga el crema de
  marca al lienzo de impresión, así que las dos franjas de 10 mm salen del color papel de
  LCI, nunca blancas; y como los laterales siguen en 0, heros, bandas y `.dark-section`
  siguen sangrando de borde a borde horizontalmente.
- **No se pierde papel:** el texto sigue corrido, sin saltos forzados ni bloques en blanco;
  solo se recorta la caja útil 10 mm arriba y 10 mm abajo.
- **Nada de tarjetas partidas:** las tarjetas (`.card`, `.dark-card`, `.recipe-card`,
  `.suppl-card`) y las piezas pequeñas (celdas del grid de categorías de alimentos
  —Verduras / Frutas / Proteínas / Despensa—, `.fitt`, `.zone`, `.numitem`, `.warn`,
  `.note`, tarjetas sueltas con `.avoid-break`) llevan `break-inside:avoid`. Los
  **contenedores grandes** que las agrupan (`section`, `.dark-section`, `.day`, tablas)
  **siguen siendo fragmentables**: ponerles `break-inside:avoid` es justo lo que generaba
  páginas medio vacías. Única excepción: una tarjeta que sola pase del ~60% del alto de
  la hoja se marca con `.frag-ok` (ver «Tarjetas que nunca se parten», arriba).
- Vale automáticamente para `plan-nutricional`, `plan-deportivo` y `plan-sueno`: los tres
  pasan por `finish()`, y `finish()` inyecta este `@page`.

**Reglas de uso:**
- Se aplica siempre, sin excepción, a los tres tipos de plan (nutricional, deportivo, sueño)
  y a cualquier handout nuevo. No es opcional ni depende del tamaño del documento.
- No cambia paleta, tipografía, componentes ni el layout de columnas — solo corrige cómo se
  reparte el contenido entre páginas al imprimir.
- Si un documento usa `lang="en"` (paciente internacional), pasar `lang='en'` y
  `print_label='Print / Save as PDF'` a `finish()`.
- Verificación antes de entregar: renderizar a PDF y confirmar que ninguna página interior
  (todas menos la última, que naturalmente cierra a media hoja) tenga más de ~25% de espacio
  en blanco al final. Si algo así aparece, casi siempre es una imagen o banda con foto que no
  se puede partir — aceptable — o un bloque al que se le volvió a poner `avoid-break` a mano.
- **Nunca revertir a `break-before:page` por sección** ni volver a envolver contenedores
  grandes en `avoid-break`: esa es exactamente la causa de fondo ya diagnosticada.
- **Nunca volver a `@page{margin:0}`** ni quitar `html{background:#EDE5DA}`: lo primero
  hace que la impresora recorte el texto en el borde del papel; lo segundo deja dos
  franjas blancas que rompen el fondo de color de la página.
- **Nunca sacar `.card` / `.dark-card` / `.recipe-card` / `.suppl-card`** de la lista de
  `break-inside:avoid` de la regla 3, ni devolverlos al `:not(...)`: eso es exactamente lo
  que partía por la mitad las tarjetas de suplementos en la foto que mandó la doctora. La
  única salida permitida es la clase `.frag-ok`, y solo en tarjetas que por sí solas pasen
  del ~60 % del alto de la hoja.

## Referencias BLOQUEADAS (`references/`)
- `REF_nutricional_LOCKED.html`, `REF_deportivo_LOCKED.html`, `REF_sueno_LOCKED.html` — los
  tres planes de la paciente Diana María Muñoz Ospina. Son el **estándar visual aprobado**.
  Todo plan nuevo debe verse idéntico a estos (misma estructura, mismos componentes, mismo
  ritmo). Cambia el CONTENIDO clínico; nunca el diseño.
- `design-recipe.md` — catálogo de componentes + reglas de imagen + estructura de cada plan.
- `build/` — los builders de Diana como **plantilla-ejemplo**. Para un paciente nuevo: copia
  el builder correspondiente, reemplaza SOLO el contenido clínico, conserva idénticas todas
  las llamadas de marca y la estructura, y aplica `finish()` como se indica arriba.

## Tratamiento de imagen (handouts con fotos licenciadas)
- Comida apetitosa → `grade`. Texturas/abstractos/heroes con texto → `tritone`.
- Toda foto bajo texto lleva velo navy (linear-gradient rgba(25,34,46,...)) para legibilidad.
- Restricción: las fotos marcan el ritmo (hero, banda editorial, banner de sección). NO se
  pone foto en cada sección. Secciones densas (tablas, listas) van sin foto.

