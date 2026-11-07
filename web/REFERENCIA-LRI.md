# Referencia: la página del Longevity Research Institute (LRI)

Fuente: el artifact "Longevity Research Institute" (versión del 7-nov-2026), hecho en Claude. Es el ejemplo de la Dra. de **cómo quiere que se vea y se sienta** una página. Este documento recoge qué hace y cómo trasladarlo al sitio de LCI **con `lci-brand`**.

## 1. Cómo está construida

| Aspecto | LRI |
|---|---|
| Motor de movimiento | GSAP 3.12 + ScrollTrigger, y Lenis 1.1 para el scroll suave. Botones magnéticos y cursor de vidrio propio |
| Escenas | Casi todas **fijadas (pin)** durante 160–440 % de scroll: el visitante no baja por la página, la recorre como una película |
| Video con el scroll | 60 fotogramas (generados con Veo) dibujados en un canvas; el scroll avanza el cuadro. El video se reproduce **al revés**: burbujas → vial. Solo el primer cuadro carga de entrada, el resto llega en segundo plano |
| WebGL propio | Malla de puntos 3D en onda (hero), ondas 3D de anillos (concepto) y una doble hélice de ADN hecha de puntos que gira con el scroll |
| Canvas 2D | Estrellas y estrellas fugaces en el hero; burbujas flotantes en la introducción |
| Carga | Pantalla de carga breve, con salida de seguridad a los 3,5 s si falla el JS |
| Accesibilidad | `prefers-reduced-motion` y versión móvil aparte (`gsap.matchMedia`) |
| Fuentes | Poppins Light (titulares), serif cursiva Instrument Serif (palabra clave), IBM Plex Mono (etiquetas en versales) |
| Paleta "Platino Glacial" | Abisal `#13202D`, noche `#0B141D`, acero `#3E5F7A`, niebla `#8FA9BC`, hielo `#D8E4EC`, papel `#F6F8FA`, con un degradé metálico para botones y logo |

## 2. El recorrido (16 secciones)

| # | Sección | Efecto principal |
|---|---|---|
| 1 | Hero | El lema aparece **gigante** y se reduce al bajar; luego entra el titular palabra por palabra. Planeta con halo, estrellas y malla WebGL |
| 2 | Zoom al vial | Pin + video escrubeado en canvas, con tres frases que cambian y una barra de progreso |
| 3 | Introducción | La pregunta "¿Qué es LRI?" aparece enorme y se reduce. Esferas de vidrio, burbujas, tarjeta de vial que se inclina, cifras que cuentan |
| 4 | "Sabemos / Nuestro objetivo / Nuestra misión" | Una sola escena fijada con tres paneles. Una cápsula rota y viaja entre ellos, y las palabras se iluminan al desplazarse |
| 5 | Banda de producto | Fotos a sangre que se cruzan, con una tarjeta de vidrio encima |
| 6 | Pilares | Escena fijada: la hélice de ADN gira mientras cambian cuatro pilares, con puntos de progreso |
| 7 | Del dato a la decisión | Ondas 3D de anillos que crecen y se expanden |
| 8 | Proceso | 4 etapas con sub-ítems numerados (1.1, 1.2…) |
| 9 | Formatos | Tarjetas que se inclinan desde abajo y descubren la foto de abajo hacia arriba |
| 10 | Moléculas | Tabla interactiva y una ruta de 6 pasos con línea que se dibuja |
| 11 | Ecosistema | Tarjetas de los tres institutos, aliados con anillos, logos y fotos |
| 12 | Equipo | Tarjetas con esferas de vidrio para los "por anunciar" |
| 13 | Journal | Rótulo gigante que se reduce, y carrusel horizontal arrastrable |
| 14 | Aliados | Esferas de vidrio con profundidad, dos marquesinas de chips en sentidos opuestos, y un panel con pestañas |
| 15 | Contacto | Eclipse con halo y titular grande |
| 16 | Pie | Planeta, logo metálico y avisos legales |

## 3. Lo que la define (el "cómo se ve")

1. **Todo es una escena, no una página.** Cada sección se fija en pantalla y avanza con el scroll.
2. **Escala dramática de la tipografía.** El rótulo aparece enorme, centrado, y se reduce hasta su sitio mientras llega el contenido.
3. **Titular ligero con una palabra serif cursiva.** Ritmo recto + cursiva.
4. **Etiquetas en versales con tracking** (mono) como segunda voz.
5. **Vidrio líquido**: botones, chips y cursor translúcidos con brillo que cruza al pasar el ratón.
6. **Un motivo propio** (aquí, el horizonte planetario) que reaparece en hero, introducción, contacto y pie.
7. **Video real como protagonista**, convertido en fotogramas que se mueven con el scroll.
8. **Oscuro y claro alternados** por sección, y la navegación cambia de color según el fondo que tiene debajo.

## 4. Cómo se traduce a LCI (con `lci-brand`)

| LRI | LCI |
|---|---|
| Poppins Light + Instrument Serif + IBM Plex Mono | **Mencken Std (titulares) + Mencken Head cursiva (acento) + Poppins (cuerpo y etiquetas).** Sin fuentes externas: solo las de la marca |
| Paleta Platino Glacial | **Navy `#2A3649`, azul acero `#94B4CC`, light blue `#CAD3DD`, cream `#EDE5DA`**, oro `#D2B58A` solo como chispa. El hielo y el platino de LRI no se copian |
| Planeta con horizonte | LCI necesita **su propio motivo**: el arco, la hélice y los anillos concéntricos que ya aparecen en el mockup. No se reutiliza el planeta de LRI, para no confundir las dos marcas |
| Vial y moléculas | Células, sangre, ADN, cerebro y laboratorio (los videos de `PROMPTS-VIDEOS-LCI`) |
| Textos | Solo datos confirmados de LCI. Nada del contenido de LRI (productos, aliados, afirmaciones) se traslada |
| Logo metálico | Logos oficiales de `brand/logos/` en blanco, beige o navy según el fondo |

## 5. Cómo se rehace el mockup de LCI

1. Sustituir mi motor casero por **GSAP + ScrollTrigger + Lenis** (las mismas versiones, desde cdnjs y jsDelivr).
2. Convertir cada sección en **escena fijada**: hero con lema gigante que se reduce, inmersión en la sangre, misión por paneles, pilares con la hélice que gira, proceso en 4 pasos, mapa de la evaluación, clínica y agenda.
3. **Video escrubeado por fotogramas**: los videos de Gemini/Veo se convierten a una secuencia de 60 cuadros (yo lo hago con ffmpeg) y se dibujan en canvas. La escena de glóbulos rojos actual en canvas se reemplaza por esa secuencia.
4. Vidrio líquido en botones, chips y cursor, con la paleta de LCI.
5. Navegación que cambia de color según la sección, y menú móvil aparte.
6. Mantener `prefers-reduced-motion`, versión móvil propia y carga diferida de los fotogramas.

## 6. A confirmar con la Dra.

1. ¿LCI mantiene **Mencken + Poppins** como marca? (LRI usa otras fuentes.)
2. ¿Qué motivo propio de LCI reemplaza al planeta: **arco, hélice, anillos** u otro?
3. ¿Los videos de Gemini llegan ya como los 3 clips (sangre, células madre, ADN) o primero el cerebro?
