# Estándar visual 2026 para DOCUMENTOS LCI (obligatorio desde oct 2026)

La Dra. Carolina aprobó el feed de Instagram de 42 publicaciones como **piso de calidad de TODO LCI** y pidió
explícitamente: *"que deje de estarme dando lo mismo plano de siempre en los documentos"*.
Referencia visual: `lci-piezas-graficas/references/estandar-visual-2026/` (grid + 42 posts + ESTANDAR-VISUAL-2026.md).
Ejemplo de documento al nivel: `references/demo-efectos-documento-2026.jpg` (builder: `build/demo_efectos_2026.py`).

## Qué cambia
Un documento LCI ya NO es «texto + tablas sobre fondo claro con un hero». Cada documento debe traer el lenguaje del
feed, adaptado a lectura e impresión, usando `assets/efectos_lci.py` (encima de `brand.py`, no en su lugar):

| Necesidad en el documento | Antes (plano) | Ahora (estándar 2026) |
|---|---|---|
| Portada / hero | gradiente navy + texto | `E.hero(E.foto(ruta, modo))` foto TRATADA + titular Mencken bold + acento itálico |
| Separador entre capítulos | línea o título | `E.banda(E.vidrio(...) / E.fondo(...) / E.ondas(...), titular, acento, texto)` |
| Datos clave (metas, dosis, cifras) | lista o tabla | `E.cifras([(n, unidad, texto)])` tarjetas con degradado de marca y cifra gigante |
| Proceso / cronograma / fases | lista numerada | `E.pasos([...])` línea de nodos (conector Paola) |
| Comparación (antes/después, problema/solución) | dos párrafos | `E.circulos(...)` |
| Aviso, perla clínica, recordatorio | caja beige | `E.tarjeta(html)` vidrio crema traslúcido / `oscuro=True` sobre fondo |
| Palabra clave en una frase | negrita | `E.pildora('palabra')` cápsula fina en línea |
| Referencias | lista suelta | `.fx-refs` + Vancouver [n] |
| Pregunta/concepto con explicación | título + párrafo | `E.linea(bold, acento, texto)` titular + línea divisoria fina |
| Ficha de concepto / definición | caja simple | `E.recuadro(rótulo, título, viñetas, texto)` tarjeta de vidrio sobre fondo con efecto |
| Mensaje clave + beneficios | lista | `E.marco(bold, acento, regular, lista)` recuadro de filete + conector de nodos |
| Sub-barra bajo un término | negrita | `E.barra(txt, fs)` barra que abraza el texto (nunca resaltado alto) |

## Reglas
1. **Toda foto con tratamiento** (`E.foto` modos bw/azul/frio/calido/ambar/claro; comida de planes nutricionales con
   `lci_treat` 'grade', cálida). Nunca foto cruda, nunca la misma foto en dos portadas.
2. **Ritmo de fondos**: alternar claro (contenido denso: tablas, menús, listas) ↔ banda oscura con efecto
   (vidrio, degradado, ondas, microscopía) cada 1–2 secciones. Las tablas y menús siguen limpios y legibles: el
   efecto va en portadas, separadores, cifras y avisos — no detrás de texto denso.
3. **Tipografía y paleta** idénticas a las piezas: solo Poppins + Mencken (correr `auditar_fuentes.py` de
   lci-piezas-graficas sobre el HTML), oro ≤2 veces por página, acento itálico azul acero sobre oscuro.
4. **Impresión**: márgenes ≥10 mm (superior, interior, inferior); el contenido arranca en la página 1 debajo del
   hero (no desperdiciar la portada); `break-inside:avoid` ya va en los componentes fx.
5. **Teléfono por idioma**: `B.IDIOMA='es'` (default, 301 512 39 91) / `B.IDIOMA='en'` (300 002 71 15).
6. **Estructura clínica**: el orden de secciones de cada plan (design-recipe.md, builders) se conserva; lo que sube
   es la capa visual. El contenido clínico se reproduce VERBATIM.
7. **Verificación**: render con Chrome headless → mirar la captura al lado del grid de referencia → pasar el
   checklist §3 de ESTANDAR-VISUAL-2026.md. Si se ve más plano que el feed, rehacer antes de entregar.
