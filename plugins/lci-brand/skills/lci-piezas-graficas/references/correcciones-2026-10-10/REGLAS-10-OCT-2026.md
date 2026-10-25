# Reglas de lectura, márgenes, contraste y ritmo del feed: correcciones de la Dra. Carolina (10-oct-2026)

La Dra. revisó en el celular las piezas ya publicadas en los tres perfiles (LCI, Carolina Rodríguez MD y LAI) y anotó qué falla y qué está bien. En esta carpeta están sus capturas anotadas: el número del archivo indica a qué regla corresponde. **Estas reglas valen para todas las piezas gráficas de las tres marcas**: post, carrusel, story, reel, portada, banner y highlight.

## 1. Zona segura: margen igual al 10 % del lado más corto, en los cuatro lados
Estas son las guías de márgenes de la Dra., en `margenes/`:

| Formato | Tamaño | Margen |
|---|---|---|
| Post vertical / carrusel | 1080×1350 | 108 px |
| Story / reel | 1080×1920 | 108 px |
| Post cuadrado | 1080×1080 (1200×1200) | 108 (120) px |
| Banner | 1200×630 | 63 px |
| Portada de Facebook | 851×315 | 32 px |

Logo, titulares, cuerpo, recuadros y referencias van **dentro** del marco. Lo único que puede ir en la banda del margen inferior es el pie: la cápsula de contacto o la web, centrada y dentro de los márgenes laterales. Así lo muestra la guía del post, con la web debajo del marco.

Ejemplos de piezas que fallaron: 01, 04 y 14 tenían textos pegados al borde inferior y al lateral.

## 2. Piso tipográfico: medido a 1080 px de ancho y escalado según el ancho real
| Rol | Mínimo |
|---|---|
| **Cualquier texto** | el texto de la **cápsula de contacto del pie** (teléfono · @usuario · web, el rectángulo redondeado de abajo; captura 15): **19 px** (LCI/CR) y **20 px** (LAI). Es el tamaño de fuente MÁS PEQUEÑO permitido en cualquier pieza; nada puede ir por debajo. Ojo: no es el recuadro «Reclaim the energy», que es un titular. (15) |
| Referencias [n] y aclaratorios (*) | 20 px, al pie. Los aclaratorios de LAI pueden ir de ese tamaño y en esa ubicación. (04) |
| Eyebrows, rótulos, etiquetas, «sustantivo», «ADULTEZ MEDIA · 1 DE 2» | **22 px** (LCI/CR) y **24 px** (LAI). (03, 07, 10) |
| Cuerpo de texto | **27 px**. Es el tamaño de «Nuestra academia nace de una convicción», el mínimo de cuerpo aprobado. (10) |

**El mínimo NO es el tamaño de la pieza: la jerarquía manda.** El tamaño de la cápsula de contacto es solo el piso absoluto. Lo usan únicamente el pie (cápsula y web), las referencias y los aclaratorios. Cada rol tiene su propio tamaño y una pieza **nunca** va con todos sus textos del mismo tamaño. Escala obligatoria (proporciones a 1080 px; «Reclaim» de Paola como referencia):

| Rol | Tamaño | Relación |
|---|---|---|
| Titular / palabra gancho | 70–132 px | ≥ 2.4 × cuerpo |
| Subtítulo o línea de apoyo | 36–56 px | ≈ 1.4–1.8 × cuerpo |
| Cuerpo | 27–34 px | ≥ 1.35 × piso |
| Eyebrow, rótulo o etiqueta | 22–26 px | por debajo del cuerpo y por encima del piso; se distingue con versalitas o tracking |
| Referencias, aclaratorios, pie | 19–20 px (piso) | — |

Con poco texto se sube todo un escalón y se mantienen las proporciones; nunca se iguala. El auditor marca **F8 jerarquía** cuando el titular no llega a 2.4 × el cuerpo, cuando hay menos de 3 niveles de tamaño o cuando más de la mitad de los textos están en el piso.

Si una pieza tiene poco texto, se usa el espacio. Se suben 1 o 2 tamaños manteniendo la jerarquía, o se suma un recuadro, una tarjeta u otro elemento. Nunca deben quedar textos pequeños con espacio vacío alrededor (02, 03, 07, 08).

## 3. Interlineado de bloque: aire de tinta igual arriba y abajo
Un bloque de líneas de distinto tamaño, como «Even after adjusting for BMI / up to 2× / the risk of death…», es **un solo bloque**. El aire entre la tinta de cada línea y la siguiente, de los descendentes de la de arriba a los ascendentes de la de abajo, es **el mismo** en todo el bloque. Nunca un aire enorme arriba y una línea montada abajo (11, el «ERROR gigante»).

En el motor se resuelve con `data-pila="0.30"` en el contenedor; el JS iguala los aires a 0.30 × el cuerpo más pequeño.

## 4. Recuadros: texto simétrico
En un recuadro de borde, caja o tarjeta, el aire de tinta es igual arriba y abajo, e izquierda y derecha. La referencia es «Reclaim the energy» de Paola (05, 15). Prohibido el texto corrido a un lado, como en «Y además, en la adultez.» (13).

## 5. Una sola línea de alineación
Todos los textos sin sangría arrancan en la misma vertical izquierda, **incluido el texto dentro de un recuadro**. El borde del recuadro sobresale hacia la izquierda y la tinta queda alineada con el resto, como en «Reclaim» (15).

## 6. Contraste
- El texto debe tener un contraste de **4.5:1** o más contra su fondo real.
- Los titulares de 60 px o más necesitan **7:1** o más.
- Sobre una foto o un fondo cargado, el mínimo sube un punto.
- Sobre un fondo claro se usa el **navy** de la paleta. El caso fallido fue «y en la vejez.», en gris claro sobre gris (08).
- Un titular sobre una foto usa un color que se despegue de la imagen, como «The brain ages too» de Paola. El caso fallido fue «where your fat is.», en azul grisáceo sobre una foto gris (09).

### 6b. Soportes de lectura: así se resuelve el contraste sobre una foto (indicación de la Dra., 10-oct-2026; capturas 16 y 17)
Cuando el texto o el logo caen sobre una foto cargada o clara (madera iluminada, equipos blancos, estantes), **no se oscurece toda la foto ni se mueve el texto al azar**. Se le da al texto un **soporte de diseño**:
- **Panel de vidrio opaco a media pieza:** `R.soporte('mitad')`, o `'mitad_sup'` para la mitad superior. Lleva desenfoque, tinte navy y un filo fino. El texto va centrado verticalmente en el panel y el titular sube un escalón.
- **Lámina de vidrio vertical «tipo ducha»** de alto completo, a un lado de la pieza: `R.soporte('columna_izq'|'columna_der')`, o `r_natural(..., soporte_='columna_izq')`. Ocupa el 58 % del ancho, lleva un estriado muy fino y un filo lateral. El texto va dentro de la columna, centrado en vertical, y el titular sube a ≈96 px.
- **Tarjeta de vidrio esmerilado** ajustada al bloque (`r_natural(..., soporte_='vidrio')`, `R.VIDRIO_CSS`), con texto simétrico dentro.
- **Resaltado que abraza el titular** (`M.barra`), **cápsulas** y **recuadros** (`M.caja`, pills).
- **Velo localizado** detrás del bloque (`soporte_='velo'`), solo para fotos medianamente cargadas.
- **El logo** también necesita su soporte: se ubica en una zona limpia, dentro de una lámina de vidrio de la pieza o con una caída de luz natural de la foto (viñeta amplia de esquina o borde). Nunca va dentro de una cápsula o recuadro propio ni con una mancha local alrededor. Nunca sobre madera iluminada o estantes (17).
- **El color del logo depende de la pieza** (aclaración de la Dra., 10-oct-2026): **no todos los logos van blancos**. Se elige según la foto, el color del fondo y la necesidad de la pieza: blanco sobre fondos u fotos oscuras; navy sobre fondos claros (crema, blanco, azul claro) o zonas claras limpias; beige o dorado cuando la pieza lo pide. Manda que se lea con elegancia (≥ 4.5:1). Si la zona de la foto es de tono medio o cargada y ningún color se lee bien (caso madera iluminada, capturas 18 y 19), **no se pone cápsula ni recuadro ni difuminado alrededor del logo**: se baja la luz de esa zona de la foto de forma natural (caída de luz amplia desde la esquina o el borde, que parezca de la fotografía) o se reencuadra. `_logo(kind, 'auto', pos)` hace esta elección midiendo el fondo, y el auditor F7 rechaza los logos que no se leen.
- **El panel de vidrio horizontal se AJUSTA al texto** (indicación de la Dra., 10-oct-2026): si el texto es corto, el vidrio no tapa media foto. Arranca a ≈0.6 × margen por encima del titular y baja hasta el borde, dejando la cápsula dentro. Así lo hace `r_natural(..., soporte_='mitad')`. El panel fijo de media pieza (`R.soporte('mitad')`) queda solo para bloques de texto largos.
- **Altura de la cápsula de contacto:** va a la misma altura que en «Reclaim» de Paola (arriba ≈ H − 1.2 × margen; ≈0.905 H en el post de 1080×1350), no pegada al borde inferior.
- **Logo con lámina de vidrio:** el logo blanco va dentro del vidrio, arriba.
- **El logo siempre se alinea a un margen de la pieza** (izquierdo o derecho, a 10 % del lado corto) o va centrado; nunca en una posición intermedia. Con la lámina a la derecha, va al margen derecho.

El auditor F3 propone estos soportes cuando falla el contraste.

## 7. Acentos de color
Cada pieza lleva al menos un **detalle de acento** en otro color de la paleta: nodos, puntos o una línea en dorado o azul claro. Es lo que hace destacar la pieza de Paola del cerebro (09).

## 8. Logos: tamaño estándar en todas las piezas
| Marca | Tamaño |
|---|---|
| LCI principal | 25 % del ancho |
| LCI sello | 150 px |
| LCI terciario | 118 px |
| Carolina Rodríguez, MD (wordmark) | ≈80 px de alto, como en «Y además», aprobado (13) |
| LAI horizontal | **≈34 % del ancho** (31–37 %), como en «Nuestra visión» (10). El de la pieza 14 era demasiado pequeño |

## 9. Ritmo tonal del feed
El feed de los perfiles se ve oscuro, sombrío y monótono (06, 09). Se respetan los tintes de la marca, pero:
- Al menos **1 de cada 3** portadas es **clara**: crema, blanco, azul claro o foto luminosa.
- Nunca hay 3 portadas oscuras seguidas.
- Ninguna fila de la cuadrícula tiene las tres piezas del mismo tono.
- Las piezas vecinas no comparten la misma familia de tono.
- Las piezas compartidas con la academia o la clínica ayudan a dar dinamismo, pero no reemplazan la regla.

## 10. Lo que está bien y se conserva
- Pieza «Reclaim the energy» de Paola (05, 15): tamaño y color del logo, contraste sobre la foto, tamaños y jerarquías, interlineados, palabras gancho, sangrado del texto de abajo y márgenes.
- LAI «Quiénes somos» (12): tamaños de texto y logo, y distribución.
- LAI «Presentación» (01): tamaño y jerarquización de los textos (solo falla el margen).
- CR «Y además» (13): tamaño del titular y del logo.

## 11. Resaltados que abrazan el texto: usarlos con más frecuencia (10-oct-2026)
La Dra. casi no ve piezas con el resaltado de «Exosomes» de Paola («are cellular messengers», sub-barra que abraza el texto). Regla:
- **Al menos 1 lámina por carrusel** y **al menos 1 de cada 3 piezas** del lote llevan un resaltado (`M.barra(txt, fs, M.it_css('elegante', fs, color), fondo=…)` o `M.hl`).
- Va sobre la **palabra o frase gancho**, nunca sobre un conector. Abraza el texto, sin aire vertical.
- Colores: azul gris o azul claro sobre oscuro; navy, crema o azul claro sobre claro. Dorado como acento puntual.
- También sirve como soporte de lectura sobre una foto (6b).
- Se revisa con `auditar_pieza.resaltados_ok(resultados)` al cerrar cada tanda.

## Auditoría obligatoria antes de entregar
- **LCI / CR (motor HTML):** `python3 assets/auditar_pieza.py pieza.html`, o `auditar_lote([(html, png)…])`. Bloquean F1 (piso), F2 (margen), F3 (contraste), F4 (recuadro), F5 (interlineado) y F7 (logo). F6 (aprovechamiento) es un aviso que se resuelve con criterio. Genera `*_qa.png` con la zona segura en verde y los fallos en rojo.
- **LAI (motor PIL):** `brand.guardar()` audita solo los formatos sociales. También se puede llamar `brand.auditar(im)`.
- **Feed:** `python3 assets/auditar_feed.py portadas…` en orden de publicación (reglas T1–T5). Genera `feed_qa.jpg`.

## 12. Cápsula dentro del vidrio (10-oct-2026, la Dra.)
En piezas con VIDRIO OPACO (panel a media pieza 'mitad', lámina vertical 'columna_izq/der', tarjeta 'vidrio') la cápsula de
contacto va DENTRO del vidrio y lleva SOLO la página web de la clínica (longevityclinicalinstitute.com), alineada al texto.
Así ningún elemento se sale del vidrio. Motor: `M.pill(solo_web=True)`, `R._pill_web(x)`; r_natural lo aplica solo.

## 13. Portadas con PERSONAS y variedad de sujeto (10-oct-2026, la Dra.)
«Lo que más conecta son las personas.» Al menos 1 de cada 3 portadas lleva una PERSONA (médicos del equipo, pacientes tipo
de cada público: ejecutivo/a, deportista, biohacker con wearable; rostro o cuerpo). No repetir lugares de la clínica ni
aparatos en portadas seguidas. Ampliar sujetos: alimentos (platos reales, ingredientes), microscopía (glóbulos rojos,
tejidos, células), además de clínica y ciencia. Fotos de color fuerte fuera de paleta (p. ej. fondo naranja) se tratan
con duotono de marca navy→arena→crema (ver fp/manuel-arena). Nada de antes/después ni resultados prometidos.
Equipo: Dr. Manuel Calderón — «Médico Funcional Certificado con CMFC del Kharrazian Institute · NUHS, CPD UK, experto en
Medicina Regenerativa y Terapias de Señalización Celular» (texto de la Dra.).

## 14. Retratos del equipo con el tratamiento de los de la Dra. (10-oct-2026, APROBADO)
Retratos de médicos del equipo = mismo toque que las fotos de la Dra. en el feed: recorte (rembg isnet) sobre consultorio
desenfocado. Presentación → r_retrato cálido (recorte 'calido' + F('cons','calido',…,16) + velo café), como «Meet the founder».
Portada de concepto → B/N con temperatura apenas cálida sobre sala de la clínica desenfocada, como «Why I founded LCI».
Nunca dejar un fondo ajeno (garaje, pared naranja). Ref.: fp/build2.py, PORTADAS_PERSONAS (aprobadas).
Fotos generadas con IA: personas con rasgos colombianos/paisas, Medellín, prompt maestro en lci-banco-fotos/references.

## 15. Interlineado con resaltado (10-oct-2026)
Cuando un bloque de texto lleva RESALTADO (barra), el interlineado sube un poco: la barra nunca invade la línea de arriba
ni la de abajo. Motor: aire ≈ 0.20 × tamaño antes de la barra y titular a line-height 1.08 (r_natural); 22 px en r_centrado.
Si el texto que sigue a la barra es otro bloque (sub), mantiene su margen propio.

## 16. Ajustes 10-oct-2026 (tarde)
- Resaltado: la barra se extiende 2 px más DESPUÉS del final del texto (padding derecho = 0.55 em + 2 px). Motor: M.barra.
- Cápsula y vidrio: si el vidrio cubre TODO el ancho de la pieza (panel 'mitad'), la cápsula va dentro del vidrio con TODOS
  los datos (teléfono · @usuario · web). Solo la lámina vertical ('columna') y la tarjeta ('vidrio'), que no cubren el ancho,
  llevan la cápsula SOLO con la web.
- Resaltado (barra de relleno): AL MENOS 2 px de barra arriba y abajo de la tinta; las letras nunca quedan al ras del borde.
  Motor: M.barra suma 4 px al alto y baja el texto 2 px. (Los recuadros con borde conservan su propio aire.)

## 17. Tamaños, flujo de texto y contraste del feed (10-oct-2026, tarde)
- Textos secundarios (subtítulo bajo el titular, cuerpo, definiciones, rótulos de cifras) subieron ~25 % en TODAS las recetas: cuerpo ≥ 34 px en portadas, ≥ 29 px dentro de círculos/fichas. Nada «pequeñito» bajo un titular.
- Los `<br>` manuales en textos secundarios se ignoran (`_fl`) y el corte lo hace `text-wrap:balance`: al subir tamaños nunca quedan viudas («hours.», «[1]» sueltos).
- Recuadro-acento (tipo «Functional,») conserva su aire con la línea siguiente: separación = 0.30 × titular (antes 0.10). Logo del r_poster alineado al margen de 108 px.
- Paletas claras nuevas en light blue de marca: `gradiente('cielo')` y `gradiente('cielo_crema')`. `r_centrado`, `r_dato` y `r_palabra` aceptan `light=True` (texto navy). No todo es foto: alternar con degradés.
- Distribución del feed: piezas claras nunca contiguas (ni en secuencia ni en la cuadrícula), separadas ≥ 3 publicaciones; piezas con resaltado/recuadro nunca consecutivas ni una encima de otra; cada fila de la cuadrícula con al menos una pieza clara o media.
- Bloque titular (recuadro-acento + bold + regular) = UN bloque apretado (recuadro→titular 0.08×H, titular→regular 0.04×H). Después: respiro (0.40×H) + filete fino al ancho del bloque + respiro (0.36×H) + tagline ≥ 38 px. Aplica a «Functional, with rigor», «Measured, not assumed», «Antioxidant pills».
- r_centrado: 32 px de aire entre la estrella y la línea regular de abajo (no pegada al texto destacado).
- Tríada de palabras gancho («Your history · Your biology · Your goals»): rótulo Poppins pequeño en versalitas + palabra Mencken itálica grande, en columnas con filete, debajo de un filete dorado corto.
- Foto con dato (dinamómetro): si la pieza va clara, conservar la foto y ponerle VELO CLARO (no reemplazarla por degradé).
- Cifra sobre foto cargada (testosterona): cifra + filete + texto apilados en la zona limpia, nunca el texto encima del sujeto.
- Cifras en columna (pasos diarios): columna alineada a la derecha, a ras del margen, separada del texto de la izquierda.
- Subtítulo de r_natural: 34–38 px según soporte.
- (Revisión final) Recuadro-acento PEGADO al titular: aire visible recuadro→mayúsculas del titular ≈ 0.18 × titular (13 px a 74 px), medido sobre «Reclaim» de Paola. r_poster: titular line-height .94 y margin-top −0.29×Hs. Ver SKILL.md «REGLA DE ESPACIADO».
- r_titulo_arriba: subtítulo 41 px. Foto con dato en clave clara: velo claro de ABAJO hacia ARRIBA (opaco abajo, desaparece hacia arriba), logo en light blue sobre la foto, bloque de cifra en la mitad inferior.
- Variedad de color (la Dra., 10-oct-2026, noche): el AZUL CLARO (#CAD3DD) es color PROTAGONISTA de la marca y se mantiene presente en el feed (acentos itálicos, barras de resaltado, fondos claros), pero NO todos los textos de todas las piezas pueden ir en blanco + azul claro. Variar entre piezas y dentro de una pieza: navy sobre zonas claras de la foto o fondos claros, crema (#EDE5DA) en cuerpos sobre oscuro, dorado (#D2B58A) en filetes, detalles y algún acento, azul claro como protagonista recurrente pero no único. Cuando la foto tenga pared/zona clara limpia, el titular va en NAVY sobre ella (sin vidrio) antes que un panel oscuro.


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

## 38 FONDOS — obligatorio (10-oct-2026)
- Correr assets/auditar_fondos.py antes de entregar; ninguna familia sin usar en feeds de 30+ piezas; vidrio estriado máx. 1 por carrusel.
