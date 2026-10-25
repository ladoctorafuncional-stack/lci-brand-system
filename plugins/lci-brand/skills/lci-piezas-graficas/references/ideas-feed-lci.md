# Banco de ideas para el feed de LCI (guardado oct 2026 a pedido de la Dra.)

Referencias que la Dra. Carolina aprobó como inspiración para las próximas publicaciones. Las imágenes están en
`references/ideas-feed/`. Regla madre: **tomar la idea, nunca copiar la pieza**. Todo se adapta a la paleta de LCI
(navy #2A3649, azul acero #94B4CC, light blue #CAD3DD, cream #EDE5DA, gold #D2B58A), a Mencken + Poppins, a los logos
oficiales y a la cápsula de contacto. Los textos de la marca siguen en inglés y con datos verificados (§7.1 de
feed-instagram-lci.md).

## Principio: no todo es foto
- **No todas las portadas ni todas las publicaciones llevan foto.** Alternar con fondos de color con degradé, bokeh,
  iconografía y diagramas lineales.
- Ritmo sugerido para la cuadrícula: de cada 3 publicaciones, al menos 1 sin foto. Nunca 2 piezas sin foto del mismo
  tipo seguidas.

## Ideas y cómo se hacen en el motor (`assets/recetas_feed.py`)

| # | Idea (referencia) | Qué tomar | Cómo en LCI | Estado |
|---|---|---|---|---|
| 1 | Feed de degradados y diagramas (`ref_feed_degradados_diagramas.jpg`) | Fondos de malla difusa con grano, diagramas de línea fina con nodos, órbitas concéntricas, ícono grande centrado | `gradiente('noche'/'acero'/'aurora'/'niebla')` + R14 `r_orbitas`, R15 `r_red`, R16 `r_icono` | Listo (muestras NF2–NF4) |
| 2 | Word of the Day (`ref_word_of_the_day_bokeh.jpg`) | Término grande + clase gramatical + píldoras de categoría + definición, sobre bokeh cálido | `bokeh()` + R13 `r_palabra` | Listo (muestra NF1) |
| 3 | Movimiento + cifra (`ref_movimiento_cifra.jpg`) | Barrido y doble exposición sobre retrato deportivo, cifra enorme fina | `movimiento()` + R12 `r_dato` | Listo |
| 4 | Tarjeta de datos sobre foto (`ref_tarjeta_datos_story.jpg`, `ref_tarjetas_biomarcadores.jpg`) | Titular serif + tarjeta translúcida con un biomarcador, su valor, unidad y una minigráfica de tendencia; columnas de tarjetas por sistema (metabólico, vitamina D, plan de acción) | R23 `r_tarjeta_datos`. Tarjeta navy translúcida sutil con filete fino (NO vidrio esmerilado fuerte: la regla §5 de no-glassmorphism se mantiene para todo lo demás). Valores SIEMPRE marcados como "Illustrative example" o datos agregados reales; nunca datos de un paciente | Listo (post 36) |
| 5 | Dedo con nodo luminoso (`ref_dedo_nodo_luminoso.jpg`) | Foto muy desenfocada en tonos fríos, un anillo/nodo luminoso con una línea vertical fina que baja al titular centrado en Poppins Light | R22 `r_nodo_luz` sobre foto con `blur` alto (≈30) y tratamiento `frio`; anillo blanco + gold | Listo (post 37) |

| 6 | Vidrio estriado + cifras (`ref_vidrio_estriado_cifras.jpg`) | Foto difusa vista a través de vidrio acanalado; columna de cifras enormes finas a la derecha | `vidrio(path, crop, tinte)` + R19 `r_cifras` | Listo (post 27) |
| 7 | Ondas 3D + píldora (`ref_ondas_3d_pildora.jpg`) | Fondo oscuro con ondas estriadas en relieve y un destello cálido; palabra clave encerrada en cápsula delineada dentro del titular serif | `ondas(seed, calor)` (navy/acero, destello gold) + R24 `r_ondas` con `pildora()` | Listo (post 32) |
| 8 | Tarjeta de microscopía (`ref_tarjeta_microscopia.jpg`) | Imagen macro/microscopía con tarjeta translúcida: rótulo pequeño, término, viñetas y definición | `bacterias(seed)` (microscopía generada, sin licencias de terceros) + R21 `r_tarjeta_micro`; tarjeta navy translúcida sutil | Listo (post 35) |
| 9 | Círculos problema/solución (`ref_circulos_problema_solucion.jpg`) | Fondo claro, dos círculos superpuestos (uno sólido, uno degradé), barra de progreso y rótulo de sección | R20 `r_circulos` | Listo (posts 24, 28) |
| 10 | Ritmo de feed qura.health (`ref_feed_qura_ritmo.jpg`) | Portadas con foto a sangre y tipografía gigante, intercaladas con portadas limpias y citas | Reglas de ritmo abajo + R17 `r_portada_limpia`, R18 `r_cita` | Aplicado (posts 24–31) |

## Reglas de ritmo del feed (oct 2026, aprobadas)
- **Portadas: maximizar fotos** (clínica real, fotos de celular con `exif_transpose`, imágenes generadas aprobadas). Tipografía gigante (R17) sobre foto natural o tratada.
- **Interiores: fondos o fotos recicladas con otro efecto** — `gradiente`, `bokeh`, `vidrio`, `movimiento`. Una foto ya usada en portada puede volver en interior SOLO con efecto distinto.
- **Portadas limpias** para que el feed respire: al menos 1 por fila de 3 (fondo claro, foto clara o pieza sin foto).
- Nunca dos degradés del mismo nombre/semilla seguidos en un carrusel; alternar noche/acero/aurora/niebla y cambiar `seed`.
- Cifras, datos y citas: solo los confirmados por la Dra. (§7.1) o con referencia Vancouver verificada en PubMed.

## Muestras ya producidas (oct 2026, en `references/ideas-feed/`)
- NF1 Word of the Day — *Healthspan* (bokeh)
- NF2 Your longevity journey — órbitas (Measure · Interpret · Personalize · Re-measure)
- NF3 Measured, not assumed — red de nodos (Metabolic, Hormonal, Inflammatory, Neurocognitive, Epigenetic, Body composition)
- NF4 You are not "just tired." — ícono lineal + degradé aurora
- `muestra_P24-2` vidrio estriado · `muestra_P24-4` R20 círculos · `muestra_P27-3` R19 cifras sobre vidrio · `muestra_P25-1` Word of the Day
- `muestra_P32-1` ondas+píldora · `muestra_P35-1` microscopía · `muestra_P36-1` tarjeta de datos · `muestra_P37-1` nodo luminoso
- Posts 32–40 (16 dic 2026–8 ene 2027): TSH, Sarcopenia, Grip strength, Microbiota, ApoB, One measurement, Inflammaging, Daily steps, Welcome to LCI
- Posts 24–31 del feed (27 nov–14 dic 2026): Lp(a), Healthspan, Journey, Measured, Just tired, 4P medicine, Social jet lag, cita de la fundadora

## Temas sugeridos para estas plantillas
- Word of the Day: Healthspan, Biological age, VO₂max, Sarcopenia, Insulin resistance, Inflammaging, Circadian rhythm,
  Neuroplasticity (definición verificada con fuente).
- Órbitas / red: el journey del paciente, los sistemas que medimos, los pilares del plan (nutrición, movimiento, sueño,
  terapias, seguimiento).
- Tarjeta de datos: "Don't lose sight of what's changing inside" con ApoB, HbA1c o vitamina D como ejemplo ilustrativo.
- Nodo luminoso: "Precision starts with one measurement" / "Your biology, in exact numbers".
