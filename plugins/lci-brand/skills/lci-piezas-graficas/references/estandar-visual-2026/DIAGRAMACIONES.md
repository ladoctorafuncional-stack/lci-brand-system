# Diagramaciones de revista LCI (aprobadas por la Dra., oct 2026) — GUARDADAS: no volver a pedirlas

Hoja visual: `DIAGRAMACIONES.jpg` (25 estilos con su receta). Mirarla antes de diagramar cualquier pieza o documento.
Regla: rotar estilos — ninguna serie (carrusel, documento, brochure) usa un solo tipo de diagramación; se combinan
2–4 de esta lista. Piezas de redes → recetas `R.*` (recetas_feed.py). Documentos → `E.*` (efectos_lci.py).

## A. Estructuras con líneas y recuadros (lenguaje editorial de Paola)
| Estilo | Qué es (rasgos que NO se pueden perder) | Pieza | Documento |
|---|---|---|---|
| **Marco de líneas + conector** («The brain ages too») | Titular bold + acento itálico + regular DENTRO de un rectángulo de filete fino recto (1.5px, acero ~75%, sin radio), fondo apenas velado. Debajo, conector de nodos (línea vertical + horizontales finas con puntos pequeños) que lleva a 2–3 frases en Poppins itálica pequeña. Cierre en Poppins itálica acero. | `r_marco` | `E.marco(...)` |
| **Marco recto** («Medicine was built for disease») | Igual sin la columna larga: titular en recuadro + conector corto con 2 líneas. | `r_marco` | `E.marco(...)` |
| **Línea divisoria** («What is social jet lag?») | Titular bold + acento itálico acero, UNA línea horizontal fina (1px, light blue 55%) al ancho del bloque, texto Poppins itálica light debajo. Nada más: aire amplio. | `r_derecha` | `E.linea(...)` |
| **Recuadro-tarjeta de vidrio** («Gut bacteria») | Tarjeta translúcida oscura (radio ~16px, borde 1px light blue 35%, blur), rótulo en versal discreta pequeña, título Poppins medio, viñetas MÍNIMAS (punto pequeño), filete divisorio y texto de cierre + ref. Sobre fondo con efecto (microscopía, foto tratada). | `r_tarjeta_micro` | `E.recuadro(...)` |
| **Recuadro-acento** («Antioxidant pills») | Caja crema traslúcida (rgba 237,229,218,.80) con aire propio (≈0.18em vertical / 0.5em lateral), texto Mencken it navy; encima del titular bold blanco. ≠ resaltado. | `r_poster` | caja en `E.tarjeta` o mismo CSS |
| **Barra que abraza** («Exosomes / are cellular messengers», «Lp(a) / measure it once») | Barra azul-gris SIN aire vertical: de la punta de ascendentes a la base de descendentes; ~0.45/0.55em lateral. Si la palabra de arriba tiene descendentes, `M.aire_desc`. | `r_claro`, `M.barra` | `E.barra(...)` |
| **Póster caja + conector** («Reclaim the energy») | Caja de borde fino + bold + regular + tagline itálica acero + conector de nodos con lista. | `t_poster` / `r_poster` | — |
| **Ficha de artículo** («The study») | Caja-rótulo de borde + tarjeta clara tipo paper: revista, título, autores, filas tipo/evidencia/hallazgo, recomendación, DOI. | `r_articulo` | (tabla/tarjeta con mismo orden) |

## B. Estructuras de datos y conceptos
| Estilo | Rasgos | Pieza | Documento |
|---|---|---|---|
| Word of the Day | Rótulo pequeño, término Poppins grande + categoría gramatical, etiquetas en cápsulas finas, definición. | `r_palabra` | — |
| Timeline de gotas («Muscle Cells») | Eyebrow itálico + titular, gotas de nivel justificadas al ancho del titular, statement con palabra estrella. | `M.t_timeline` | `E.pasos` (versión lineal) |
| Cápsula en línea («checked with TSH alone?») | Palabra clave dentro de cápsula de contorno fino EN la línea de texto, centrada óptica. | `R.pildora` | `E.pildora` |
| Círculos problema/solución | Dos círculos superpuestos (oscuro / claro con volumen), título + texto dentro. | `r_circulos` | `E.circulos` |
| Pasos numerados | Número Mencken it gigante + título + texto sobre foto distinta por paso. | `r_paso` | `E.pasos` |
| Cifras apiladas / cifra titular | Números Poppins/Mencken gigantes con unidad pequeña y texto corto al lado. | `r_cifras`, `r_cifra_titular` | `E.cifras` |
| Tarjeta de datos | Tarjeta vidrio con marcador, valor, unidad, serie mini-gráfica — siempre «Illustrative example». | `r_tarjeta_datos` | `E.tarjeta` + gráfico |
| Órbitas / Red de nodos / Nodo luminoso | Diagramas de líneas finas con puntos pequeños sobre degradado de marca. | `r_orbitas`, `r_red`, `r_nodo_luz` | SVG en `E.banda` |
| Cita sobre vidrio, eyebrow + estrella gigante, centrado estrella, retrato integrado, foto natural | ver hoja. | `r_cita`, `r_eyebrow_gigante`, `r_centrado`, `r_retrato`, `r_natural` | `E.hero`, `E.banda` |

## Reglas transversales de estas diagramaciones
- Líneas SIEMPRE finas (1–1.5px), rectas, en acero/light blue translúcido; nodos = puntos pequeños (5–7px). Nunca líneas gruesas ni flechas pesadas.
- Viñetas DISCRETAS: punto pequeño (oro o acero) o conector de nodos; nunca viñetas grandes, emojis ni glifos de sistema.
- Recuadros: filete fino recto (marco) o vidrio translúcido con radio ~16px (tarjeta). No mezclar ambos en el mismo bloque.
- Jerarquía dentro del recuadro: rótulo pequeño → titular grande → apoyo pequeño; interlínea apretada dentro, aire amplio entre bloques.
- Justificar elementos bajo un titular ancho al ancho del titular.
