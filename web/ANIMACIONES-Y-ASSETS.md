# Animaciones y assets · Sitio web LCI

Base: el video de referencia de la Dra. (Nervana y Cascaid) y la dirección inmersiva ya publicada. Principio: **la página se despliega con el scroll**. Cada tramo de scroll avanza una escena; el visitante no espera animaciones, las provoca.

## 1. Qué hacen las referencias (patrones a replicar)

| # | Patrón | Dónde se vio | Cómo se logra |
|---|---|---|---|
| P1 | Titular gigante sobre foto a pantalla completa | Nervana hero ("The Pain Free Era") | Tipografía a ancho completo sobre imagen fija o video |
| P2 | **Ventana que se expande**: un recuadro pequeño del hero crece hasta llenar la pantalla y revela la siguiente escena | Nervana (el parche pasa de tarjeta a foto completa) | `clip-path: inset()` o escala ligada al scroll, escena fijada (pin) |
| P3 | Anillos concéntricos en relieve que laten como ondas | Cascaid ("Cascaid effect") y Nervana (círculo con ondas) | Capas SVG/CSS con sombras internas, escala y opacidad por scroll |
| P4 | Frase que se ilumina palabra a palabra | Cascaid ("no te falta motivación, te falta navegación") | Scrub de opacidad por palabra (ya lo tenemos en la misión) |
| P5 | Palabra con degradado metálico sobre niebla que se aclara | Cascaid ("From complexity… to clarity") | Texto con `background-clip`, fondo desenfocado que se enfoca con el scroll |
| P6 | Video de fondo con **etiquetas de datos flotando** | Cascaid (cascada con términos de salud) | Video en loop + etiquetas mono en deriva lenta y paralaje |
| P7 | Línea de tiempo vertical con puntos que se encienden y óvalos de fondo | Cascaid (pasos 01–05) | Línea fijada, nodo activo por IntersectionObserver (ya lo tenemos) |
| P8 | Marquesina de texto gigante con símbolo | Nervana ("PAIN MANAGEMENT ✱") | Banda de texto en bucle, velocidad ligada al scroll |
| P9 | Cuadrícula de íconos lineales de órganos | Cascaid ("check engine light") | Íconos SVG que se dibujan al entrar |
| P10 | Mosaico de fotos que se abre alrededor de un marco con titular serif encima | Cascaid ("For every role you play") | Imágenes en capas con escalas distintas y titular que cruza el marco |
| P11 | Pie con wordmark gigante | Nervana ("Nervana" a ancho completo) | Texto enorme recortado por el borde, que se revela al llegar |
| P12 | Tipografía serif de alto contraste con cursiva en el acento + etiquetas en mayúscula espaciada | Cascaid | Ya es nuestro lenguaje: Mencken + Poppins |

Lo que NO copiamos: paletas (verde, marrón, naranja), logotipos, textos ni fotos. Tomamos el tipo de movimiento y lo vestimos de navy, azul acero, crema y el oro puntual de LCI.

## 2. Guion de scroll de LCI (de arriba hacia abajo)

| Acto | Qué pasa al hacer scroll | Patrón | Asset |
|---|---|---|---|
| 0. Entrada | El sello LCI se dibuja y se abre al hero | P12 | Sello en SVG animado |
| 1. Hero | Titular gigante sobre la hélice 3D. Un recuadro pequeño muestra el torrente sanguíneo | P1, P2 | Hélice en tiempo real, V1 |
| 2. **Inmersión** | El recuadro se expande a pantalla completa y **viajamos por dentro**: vaso sanguíneo con glóbulos rojos, luego un cúmulo de células madre y luego el núcleo y el ADN. Entre escenas aparecen frases cortas | P2, P4 | V2, V3, V4 |
| 3. Laboratorio | Muestra en tubo, análisis, y términos de medición flotando sobre el video | P6 | V5 |
| 4. Edad biológica | Anillos concéntricos latiendo; cada anillo es un reloj biológico | P3 | SVG/CSS, sin video |
| 5. Cómo trabajamos | Línea vertical con 4 pasos y óvalos de fondo | P7 | Ya construido; sumar anillos |
| 6. Misión | Frase que se ilumina; "LONGEVITY" en contorno | P4 | Ya construido |
| 7. Ciencia | Mapa orbital + cuadrícula de íconos de lo que medimos | P9 | Set de 12 íconos lineales |
| 8. La Dra. | Foto en ventana que se expande, nombre gigante | P2, P1 | Foto de calidad |
| 9. La clínica | Mosaico de fotos alrededor de un marco con titular encima | P10 | Fotos reales y V6 |
| 10. Viajeros | Marquesina gigante "MEDELLÍN ✱ LONGEVITY ✱ …" y paisaje nocturno | P8 | V7 |
| 11. Agenda y pie | Widget de reserva y wordmark gigante | P11 | Wordmark vectorial |

Global: scroll suave (Lenis), cursor propio, botones magnéticos, barra de progreso, transiciones entre páginas ES/EN.

## 3. Videos y animaciones a producir

| ID | Pieza | Duración | Cómo se usa | Producción recomendada |
|---|---|---|---|---|
| V1 | Hélice y partículas (ambiente del hero) | Loop 8 s | Fondo del hero | **Tiempo real** (ya existe) + video de respaldo para móviles débiles |
| V2 | Torrente sanguíneo: cámara avanzando por un vaso con glóbulos rojos bicóncavos | 12–20 s | Scroll-scrub (el scroll mueve el video) | Render propio en WebGL → MP4 |
| V3 | Células madre: cúmulo translúcido, rotación lenta y división | 12–20 s | Scroll-scrub | Render propio o video con IA, con revisión científica |
| V4 | Zoom al núcleo y al ADN (hélice con extremos) | 10 s | Scroll-scrub | Render propio |
| V5 | Laboratorio: tubos, pipeta, analizador, placas | 15 s | Fondo con etiquetas flotantes | **Video real** de la clínica (ideal) o render |
| V6 | Recorrido de la clínica: pasillo, medición, consultorio, terapias | 30–45 s | Mosaico y fondo | **Video real** con gimbal, horizontal y vertical |
| V7 | Medellín de noche desde la sala de terapias | 10 s loop | Sección viajeros | Video real |
| I1 | 12 íconos lineales de órganos y sistemas | n/a | Cuadrícula P9 | Yo los dibujo en SVG con el estilo de marca |
| I2 | Renders con transparencia: glóbulo rojo, célula madre, cúmulo | n/a | Capas con paralaje | Render propio |
| I3 | Fotos reales de alta resolución (≥ 2400 px) | n/a | Mosaico, Dra., equipo | Sesión fotográfica |

Especificaciones de entrega:
- **Scroll-scrub**: MP4 H.264 con un fotograma clave en cada cuadro (`-g 1`), 1920×1080 en escritorio y 1080×1920 en móvil. Alternativa: secuencia de 120–240 imágenes WebP. Peso objetivo: ≤ 6 MB por clip.
- **Fondo en loop**: MP4 + WebM, sin audio, ≤ 4 MB, con póster en WebP.
- **Color**: gradación a la paleta (navy #2A3649, azul acero #94B4CC, crema #EDE5DA) con el oro #D2B58A solo en puntos de luz.
- **Carga**: cada video se carga al acercarse la sección. Con "reducir movimiento" se muestra el póster.

## 4. Tres formas de producir las escenas celulares

| Opción | Calidad | Interactividad | Peso | Riesgo |
|---|---|---|---|---|
| A. Tiempo real (Three.js) | Buena, abstracta y elegante | Alta (reacciona al cursor) | Muy bajo | Móviles lentos |
| B. Render propio y exportado a video | Alta y consistente | Solo scroll | Medio | Ninguno técnico: yo lo hago con Chromium y ffmpeg |
| C. Video con IA (Veo, Runway, Kling) | Más fotorreal | Solo scroll | Medio | Inexactitudes científicas y artefactos; revisión médica obligatoria |

**Recomendación: híbrido.** A para el hero y los elementos que reaccionan al cursor. B para la inmersión V2–V4, porque controlamos paleta, ritmo y exactitud. C solo como prueba de un clip (por ejemplo V3), comparado con B antes de decidir. Yo puedo producir A y B aquí. Para C te dejo los prompts y las especificaciones.

## 5. Implementación

- **Motor de scroll**: Lenis + GSAP ScrollTrigger (escenas fijadas, escrubeo de video y de clip-path). Three.js solo en las escenas que lo usan.
- **Móvil**: escenas más cortas, video vertical, sin cursor ni magnetismo, y calidad reducida automática si el dispositivo es lento.
- **Accesibilidad**: `prefers-reduced-motion` desactiva escrubeo y bucles; el contenido siempre se lee sin JS.
- **Rendimiento**: LCP < 2,5 s, JS inicial < 150 KB, video diferido, imágenes AVIF/WebP.

## 6. Contenido científico que debe aprobar la Dra.

- Los visuales de células madre y glóbulos rojos son ilustrativos. **No afirman que LCI ofrezca un tratamiento con células madre.** Los textos de esa escena los define la Dra., con bibliografía (autores, revista, año y DOI) y distinguiendo evidencia sólida de emergente.
- Los términos flotantes del laboratorio usan solo mediciones que LCI realiza (por ejemplo ApoB, Lp(a), VO2max, composición corporal, electrocardiograma); la Dra. aprueba la lista.
- Sin cifras clínicas inventadas en etiquetas ni gráficos.

## 6b. Reglas de los skills `lci-design-system` y `lci-piezas-graficas` aplicadas al sitio

Toda pieza, escena y componente web se construye con estas reglas. Se verificó contra el mockup inmersivo.

| Regla | Cómo se aplica en la web |
|---|---|
| Solo Poppins y Mencken Std / Mencken Std Head | Prohibidos los glifos que no existen en ellas (✦ ◦ ▸ ₂ emojis): se dibujan en SVG. Auditoría de glifos antes de cada entrega |
| Titular: recta + acento en cursiva Mencken, mismo tamaño, interlineado 1.0, sin margen entre líneas | Hero y títulos de sección; el acento se distingue por cursiva y color |
| Oro mínimo (1–2 elementos por página) | Solo peldaños de la hélice y el filete de la misión. El resto en navy, azul acero y crema |
| Contraste ≥ 4,5:1 y titulares ≥ 7:1; en fondo claro, navy | Textos y acentos sobre crema y blanco van en navy; el azul medio queda para líneas y detalles. Estados atenuados con contraste suficiente |
| Eyebrows en versales con tracking ~.10em, pegados a su titular | Aplicado |
| Foto de clínica y ciencia: fría con color real (`treat_cool`); la comida, cálida | Todas las fotos de clínica pasan por `treat_cool`; el retrato con `tint=0` |
| Foto bajo texto lleva velo navy | Velos en hero, viajeros y menú |
| Rotar las 15 familias de fondos, sin repetir contiguos | Mesh oscuro (hero), malla (ciencia), galaxia (misión), noche (clínica), mesh claro (agenda). Cada escena nueva usa otra familia |
| Logo ≥ 180 px, sin cápsula propia, color según fondo | Blanco sobre oscuro, navy sobre claro |
| Teléfono e Instagram según idioma | ES (+57) 301 512 39 91 · @institutoclinicodelongevidad; EN (+57) 300 002 71 15 · @longevityclinicalinstitute |
| Personas serias, elegantes, aspiracionales; sin sonrisas ni mirada a cámara | **Pendiente:** el retrato oficial de la Dra. sonríe a cámara. Para el sitio final se necesitan tomas nuevas, serias y concentradas |
| Un soporte distinto por pieza, sin repetir el mismo recurso | En el mosaico y las escenas se rotan recuadro, vidrio, línea con nodos, resaltado y velo |
| Interlineado de párrafos 1.32–1.50 y aire entre bloques | Aplicado en cuerpos y pasos |
| Contenido: respetar el original, sin claims de mercadeo ("pionera", "100 %", "resultados inmediatos") | Todos los textos usan datos confirmados; los claims nuevos pasan por la Dra. |

## 6c. Efectos de motion ya construidos en el mockup (v3)

| Efecto | Patrón | Estado |
|---|---|---|
| Ventana que se expande y nos sumerge en un torrente sanguíneo, con tres frases que aparecen por scroll | P2 | Hecho en canvas (provisional hasta tener el video V2) |
| Anillos concéntricos en relieve que laten y crecen con el scroll, en la sección de edad biológica | P3 | Hecho |
| Marquesina gigante "LONGEVITY ✱ MEDELLÍN" cuya velocidad sube con el scroll | P8 | Hecho |
| Nombre "Longevity" gigante en el pie, recortado como en Nervana | P11 | Hecho |
| Hélice 3D, capítulos con scroll fijado, mapa orbital, misión que se ilumina, retrato que se inclina, galería arrastrable | P1, P4, P7 | Hecho (v1–v2) |
| Cuadrícula de íconos lineales de órganos que se dibujan | P9 | Pendiente (los dibujo yo) |
| Mosaico de fotos alrededor de un marco con titular encima | P10 | Pendiente (necesita fotos reales) |
| Efectos del reel de Instagram que mencionó la Dra. | por definir | Pendiente: falta ver el video |

Cuando lleguen los videos de V2–V4, la escena de glóbulos rojos en canvas se reemplaza por el video, sin cambiar la transición.

## 7. Orden de trabajo propuesto

1. **Prototipo de inmersión** (artifact): hero → ventana que se expande → vaso sanguíneo → células madre → ADN, con frases por scroll, anillos y etiquetas flotantes.
2. Aprobación de la Dra. y ajuste de ritmo y color.
3. Exportar V2–V4 a video y probar el escrubeo en móvil.
4. Íconos, mosaico, marquesina y wordmark del pie.
5. Pasar todo al repo `lci-website` (Astro) con Lenis + GSAP.
6. Sustituir fotos y video por material real de la clínica.
