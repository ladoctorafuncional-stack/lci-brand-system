# INTERLINEADO BLINDADO LCI (regla dura, oct 2026) — piezas, brochures, documentos, presentaciones

La Dra. lo pidió explícitamente: los textos no pueden quedar "ni muy separados ni muy cerca". Estas son las
medidas de las piezas APROBADAS (`INTERLINEADO-ejemplos-aprobados.jpg`: Exosomes, What is social jet lag?,
Word of the day / Inflammaging, Timeline of creatine, Dr. Carolina Rodríguez Morales, Thousand supplements),
medidas en píxeles sobre el original de Paola y sobre nuestras recetas aprobadas. **Se aplican siempre, en
ratios del tamaño de letra (em), a cualquier tamaño de formato.** Desviarse = entrega rechazada.

Calcularlas SIEMPRE con `M.ritmo(fs_titular, fs_cuerpo)` (piezas) o `E.ritmo(...)` (documentos); nunca a ojo.

## 1. DENTRO de un bloque (apretado)
| Elemento | line-height | Margen entre sus líneas |
|---|---|---|
| Titular display Mencken (bold + línea itálica de acento, p. ej. «What is / social jet lag?», «Dr. Carolina / Rodríguez / Morales») | **1.00** (rango 0.98–1.04) | **0** — las líneas del titular son UN bloque |
| Estrella gigante + línea regular de apoyo («Thousand / supplements / to improve») | 0.98 / 1.05 | **0.10–0.12 × fs estrella** |
| Eyebrow pequeño pegado a su titular («Timeline of creatine in» → «Muscle Cells», «You don't need a» → «Thousand») | 1.0 | **0.06–0.10 × fs titular** (eyebrow casi toca el titular) |
| Sub-barra bajo palabra estrella («Exosomes» → barra) | — | **0.15–0.25 × fs estrella** desde la línea base (+ `M.aire_desc` si hay descendentes) |
| Párrafo Poppins light recto | **1.40** (1.35–1.45) | — |
| Párrafo Poppins itálica | **1.32** (1.28–1.38) | — |
| Rótulo / etiqueta de 1 línea | 1.0 | — |

## 2. ENTRE bloques distintos (aire amplio, nunca disperso)
`c` = tamaño de letra del cuerpo que viene después.
| Transición | Aire |
|---|---|
| Titular → párrafo (sin filete) | **1.2–1.5 × c** (Paola Exosomes: barra → texto = 1.4 c) |
| Titular → filete fino → párrafo | **arriba 1.1–1.3 × c · abajo 0.85–1.0 × c** (social jet lag, Founder) |
| Rótulo «Word of the day» → término | **1.0 × fs rótulo** |
| Término → etiquetas (cápsulas) | **0.22 × fs término** |
| Etiquetas → filete → definición | **arriba 1.5 × c · abajo 1.0 × c** |
| Párrafo → párrafo (mismo grupo) | **0.75–0.85 × c** |
| Sección → sección (documentos/brochure) | **2.5–3 × c** y nunca menos que el aire entre bloques internos |

## 3. Prohibido
- line-height ≥ 1.15 en titulares display o margen entre sus líneas (se "despegan").
- line-height < 1.25 o > 1.5 en párrafos.
- Aire entre bloques < 0.7 × c (pegado) o > 2 × c dentro de un mismo grupo (disperso).
- Usar `<br>`+`margin` arbitrarios; todo sale de `ritmo()`.
- Mismo aire dentro y entre bloques (sin jerarquía de ritmo): dentro SIEMPRE más apretado que entre.

## 4. Verificación obligatoria
Renderizar y MEDIR en píxeles (filas de tinta) las distancias base-a-base y entre bloques; comparar contra esta
tabla y contra `INTERLINEADO-ejemplos-aprobados.jpg` antes de entregar.
