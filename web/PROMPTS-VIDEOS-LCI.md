# Prompts de video para el sitio LCI (Gemini / Veo y ChatGPT / Sora)

Los prompts van en **inglés** porque estos modelos responden mejor así. Cada uno trae una línea en español con lo que hace.
Siguen las lecciones del documento de fotos de LCI (`PROMPTS_FOTOS_LCI_NanoBanana.md`): todo en positivo, sin listas largas de prohibiciones y con una referencia visual adjunta cuando existe.

> Los límites (duración del clip, resolución, número de generaciones) dependen de tu plan. Verifícalos antes de empezar. Desde aquí no puedo usar Gemini ni ChatGPT: tú generas y me pasas los archivos, y yo los integro.

---

## 1. Flujo recomendado (cada escena)

1. **Imagen clave primero.** En Gemini (imagen / Nano Banana) o ChatGPT (imágenes) genera el primer fotograma con el prompt de imagen de cada escena. Elige la mejor entre 4 variantes.
2. **De imagen a video.** En Gemini (Veo, por ejemplo desde Flow) o ChatGPT (Sora), sube esa imagen como fotograma inicial y pega el prompt de video. Si tu plan permite fotograma inicial y final, sube también la imagen final.
3. **Encadenar escenas.** El último fotograma de un clip es la imagen inicial del siguiente. Así el viaje (sangre → células madre → ADN) se siente continuo.
4. **Formato.** Genera en **16:9** para escritorio. Si el modelo lo permite, repite el clip en **9:16** para móvil. Pide la resolución más alta disponible y descarga sin comprimir.
5. **Variantes.** Genera 3–4 por escena. Descarta las que tengan formas que se deforman, texto, caras o logos.
6. **Entrega.** Pásame los MP4 con estos nombres: `B1-cerebro`, `V2-sangre`, `V3-celulas-madre`, `V4-nucleo-adn`, `V5-laboratorio`, `V6-clinica`, `V7-medellin`. Yo les ajusto el color a la paleta, quito el audio, los codifico para que se muevan con el scroll y creo la versión móvil.

## 2. Bloque de estilo fijo (se pega SIEMPRE al final de cada prompt)

```
Cinematic scientific visualization with a high-end documentary look. Color world: deep navy blue shadows (#2A3649), steel-blue (#94B4CC) and pale ice-blue highlights, soft cream light (#EDE5DA), and only tiny champagne-gold sparks (#D2B58A) as a rare accent. Low saturation, elegant, calm and precise. Shallow depth of field with soft bokeh particles, gentle volumetric light, subtle film grain. Photoreal translucent and glassy materials with soft subsurface scattering. One slow, smooth, continuous camera move with no cuts. Pure imagery with no text, no letters, no logos, no people, silent. Avoid: cartoon look, neon colors, purple, watermark.
```

ES: mundo de color navy, azul acero, crema, con chispas doradas mínimas; elegante, calmado, cámara lenta y continua, sin texto ni personas.

---

## 3. Escenas

### B1 · Cerebro principal (hero, loop de 8 s)
**Imagen clave:**
```
Ultra-detailed scientific render of a translucent human brain floating in a dark navy void, placed on the right 60% of a 16:9 frame, left third darker and empty. Inside the glassy brain, fine neurons and synaptic connections glow in pale steel-blue and cream light, a few tiny champagne-gold sparks at the synapses. Crisp, anatomically accurate cortical folds, soft rim light from behind, volumetric haze, drifting luminous dust. [BLOQUE DE ESTILO]
```
**Video:**
```
Use the attached image as the first frame. A slow cinematic push-in with a gentle 20-degree orbit to the right around the translucent brain. Electrical impulses travel along the neural fibers in slow waves of steel-blue and cream light; a few tiny gold sparks flash at the synapses. The brain gently breathes with light, rim light shifts softly, luminous dust drifts in the foreground. The left third of the frame stays dark and calm. [BLOQUE DE ESTILO]
```
ES: cerebro translúcido con neuronas que se encienden, cámara que avanza y rodea lentamente; el tercio izquierdo queda oscuro para el texto.

### V2 · Torrente sanguíneo con glóbulos rojos (12–16 s, se mueve con el scroll)
**Imagen clave:**
```
First-person view inside a large blood vessel, a luminous tunnel ahead. Hundreds of biconcave red blood cells with accurate disc shape and soft concave centers drift at different depths, some close to the camera and softly out of focus. The red is a deep muted crimson that sits within the navy and steel-blue environment. Translucent vessel walls, tiny particles in the plasma, soft cream backlight from the far end. [BLOQUE DE ESTILO]
```
**Video:**
```
Use the attached image as the first frame. The camera glides forward slowly through the vessel, passing red blood cells that drift and gently rotate at different depths, some brushing past the lens in soft focus. The luminous opening ahead grows gradually brighter as we approach. Continuous forward motion, no cuts. [BLOQUE DE ESTILO]
```
ES: viaje en primera persona por un vaso con glóbulos rojos bicóncavos; avanza hacia una luz.

### V3 · Células madre (12–16 s, se mueve con el scroll)
**Imagen clave:**
```
A cluster of about a dozen round, translucent, pearl-like stem cells floating in a clear nutrient fluid, each with a faintly visible nucleus and a delicate shimmering membrane. Soft out-of-focus cells in the distance, dark navy background, steel-blue and cream light, subtle champagne-gold glints on the membranes. [BLOQUE DE ESTILO]
```
**Video:**
```
Use the attached image as the first frame. The camera orbits slowly around the cluster. One cell gently elongates and divides into two in a smooth, realistic mitosis while the others drift with a soft breathing motion. Delicate light ripples across the membranes. [BLOQUE DE ESTILO]
```
ES: cúmulo de células madre translúcidas; una se divide con suavidad mientras la cámara las rodea.

> Estas imágenes son ilustrativas. No indican que LCI ofrezca un tratamiento con células madre. Los textos de esta escena los define la Dra.

### V4 · Del núcleo al ADN (10 s, se mueve con el scroll)
**Imagen clave:**
```
Extreme close-up of the surface of a translucent cell, the nucleus faintly visible behind the membrane, steel-blue and cream light, dark navy surroundings. [BLOQUE DE ESTILO]
```
**Imagen final (si tu plan permite fotograma final):**
```
A luminous DNA double helix filling the frame diagonally, centered to the right, fine base-pair rungs glowing steel-blue and cream, a few rungs in champagne gold, dark navy void with soft bokeh. [BLOQUE DE ESTILO]
```
**Video:**
```
Use the attached image as the first frame. The camera glides through the cell membrane into the nucleus; chromatin fibers gather and resolve into a luminous double helix that rotates slowly and fills the frame diagonally. One continuous forward move, no cuts. [BLOQUE DE ESTILO]
```
ES: la cámara atraviesa la célula, entra al núcleo y termina en la hélice de ADN.

### V5 · Laboratorio (15 s, de preferencia grabar real)
**Video (texto a video):**
```
Macro cinematic shot of an empty modern laboratory bench in cream and navy tones. A rack of clear glass blood-collection tubes with deep red plasma and a few with pale straw-colored serum, softly backlit. A precise automated analyzer in the background with a faint blue indicator light. Slow lateral dolly from left to right with a gentle rack focus from the tubes to the analyzer, tiny dust particles floating in the light. No readable text on any label. [BLOQUE DE ESTILO]
```
ES: tubos de muestra y analizador; cámara lateral lenta con cambio de foco. Mejor aún: grabar la sala real de la clínica.

### V6 · Recorrido de la clínica (30–45 s, **grabar real**)
Si se genera con IA, **adjunta una foto real** y usa esta frase al inicio, igual que en las fotos (`PROMPTS_FOTOS_LCI_NanoBanana.md`):
```
Use the attached photo as the exact location and lighting reference: keep the same room, walls, furniture, materials and lighting exactly as they are. Do not add windows, doors, plants or views that are not in the photo. A slow smooth dolly forward along the space, warm LED cove lighting, no people, no readable text. [BLOQUE DE ESTILO]
```
Fotos de referencia sugeridas: pasillo (`clinica/pasillo-luces-doradas.jpg`), sala de medición (`clinica-real/real-sala-medicion.jpg`), consultorio (`clinica/consultorio-calido.jpg`). No usar la recepción con el logo: la IA deforma las letras.

### V7 · Medellín de noche desde la sala de terapias (10 s, loop)
```
Use the attached photo as the exact location and lighting reference: keep the same room, furniture and window exactly as they are. A very slow push-in toward the window while the city lights of Medellín twinkle softly and a few clouds drift; the room light stays warm and still. No people, no readable text. [BLOQUE DE ESTILO]
```
Foto de referencia: `clinica/sala-terapia-noche-ciudad.jpg`.

---

## 3b. Qué fotos adjuntar en cada video

Rutas dentro de `plugins/lci-fotos/skills/lci-banco-fotos/fotos/`. Se adjunta como **fotograma inicial** o como **referencia de lugar**, siempre con la frase "use the attached photo as the exact location and lighting reference".

| Video | Fotos recomendadas | Notas |
|---|---|---|
| B1 Cerebro | **Ninguna del banco.** Se genera la imagen clave con el prompt | La del cerebro de cristal azul queda descartada. Si tienes un cerebro que te encante, adjunta ESA como referencia de estilo |
| V2 Glóbulos rojos | Ninguna como fotograma. Opcional, solo como referencia de forma: `cientificas/ia-globulos-rojos-fondo-blanco.jpg` | Decir "use the attached image only as reference for the biconcave cell shape". Su color rojo vivo y fondo blanco no son de marca: se grada |
| V3 Células madre | Ninguna | Se genera la imagen clave |
| V4 Núcleo y ADN | Opcional, solo forma: `cientificas/ia-adn-calido.jpg` | Es cálida y fuera de paleta; se usa para la forma de la hélice, no para el color |
| V5 Laboratorio | Referencia de equipo: `clinica-real/real-sala-medicion-inbody.jpg` y `clinica-real/real-electrocardiografo-edan.jpg`. Referencia de mesa: `cientificas/laboratorio-moderno.jpg` | No hay foto real del laboratorio de procesamiento. **Hay que grabarlo** para que sea fiel. No usar `ia-tubos-sangre-guante.jpg` (lleva mano y guante) |
| V6 Recorrido de la clínica | `clinica/pasillo-luces-doradas.jpg`, `clinica-real/real-sala-medicion.jpg`, `clinica-real/real-consultorio-camilla.jpg`, `clinica-real/real-sala-terapia-dia.jpg` | Un clip por foto y luego se unen. Lo ideal es grabarlo real con gimbal |
| V7 Medellín de noche | `clinica-real/real-sala-terapia-noche-ciudad.jpg`. Alterna sin cartel: `clinica/sala-terapia-noche-variante.jpg` | El cartel de la mesita tiene texto y el video lo puede deformar |

**No usar como referencia**
- Recepción con el logo: la IA deforma las letras.
- Pasillos con señalética o nombres de médicos, y la zona de lavado.
- Cualquier foto de la Dra. o del equipo para generar una persona: las fotos y videos de los médicos son siempre reales, nunca generados.

Las fotos del banco `clinica/…` son de la serie generada con IA. Para el sitio final lo ideal es reemplazarlas por fotos y video reales de la clínica.

## 3c. Imágenes fijas para el sitio

Se generan en Gemini (imagen / Nano Banana) o ChatGPT (imágenes). Las de células y ADN se piden **sobre fondo negro puro**: así se mezclan con el fondo navy de la página en modo "screen" y no necesitan recorte. Las escenas de clínica llevan una **foto real adjunta** (ver 3b). Las de personas usan la fórmula v3 del documento de fotos de LCI.

### F1 · Glóbulos rojos aislados (formato 16:9)
```
Hyper-realistic 3D render of five biconcave red blood cells floating at different depths, isolated on a pure black background for compositing, accurate disc shape with soft concave centers, muted deep crimson with a subtle steel-blue rim light, glossy translucent membrane, shallow depth of field with the nearest cell softly out of focus, left third of the frame empty. [BLOQUE DE ESTILO]
```
ES: glóbulos rojos 3D sobre fondo negro, para mezclar con la página.

### F2 · Células madre aisladas (16:9)
```
Hyper-realistic 3D render of a cluster of about ten round, translucent, pearl-like stem cells with faintly visible nuclei and delicate shimmering membranes, isolated on a pure black background for compositing, steel-blue and cream light with subtle champagne-gold glints, shallow depth of field. [BLOQUE DE ESTILO]
```

### F3 · Doble hélice de ADN (16:9)
```
A luminous DNA double helix running diagonally across the frame, isolated on a pure black background for compositing, fine base-pair rungs glowing steel-blue and cream, a few rungs in champagne gold, soft bokeh particles, razor-sharp center and gently blurred ends. [BLOQUE DE ESTILO]
```

### F4 · Red de neuronas en macro (16:9)
```
Macro scientific render of a network of neurons with glowing dendrites and synapses, pale steel-blue and cream light, a few tiny champagne-gold sparks at the synapses, dark navy background, shallow depth of field, drifting luminous dust. [BLOQUE DE ESTILO]
```

### F5 · Tubos de muestra en el laboratorio (16:9)
```
Macro photograph of a rack of clear glass blood-collection tubes with deep red plasma and a few with pale straw-colored serum, softly backlit on a cream and navy laboratory bench, a precise automated analyzer softly out of focus behind with a faint blue indicator light. No readable text on any label. [BLOQUE DE ESTILO]
```

### F6 · Sala de medición con ángulo de cine (16:9 o 4:5)
Adjunta `clinica-real/real-sala-medicion-inbody.jpg`.
```
Use the attached photo as the exact location and lighting reference: keep the same room, walls, furniture, equipment, materials and lighting exactly as they are. Do not add windows, doors, plants or views that are not in the photo. A cinematic, slightly low camera angle with the warm LED cove light glowing along the wood slats, no people, no readable text on screens. Candid documentary photograph, Leica M10-R 50mm f/2.8, Kodak Portra 400 palette, fine film grain. Avoid: CGI look, text, logos, watermark.
```

### F7 · Medellín al atardecer (16:9)
Adjunta `clinica-real/real-sala-terapia-noche-ciudad.jpg`.
```
Use the attached photo as the exact location and lighting reference: keep the same room, furniture and window exactly as they are. Dusk over Medellín seen through the window, the first city lights turning on, a deep blue sky, the room light warm and still. No people, no readable text. Candid documentary photograph, Leica M10-R 50mm f/2.8, Kodak Portra 400 palette, fine film grain. Avoid: CGI look, text, logos, watermark.
```

### F8 · Paciente ejecutivo en el consultorio (4:5 vertical)
Adjunta `lifestyle/consultorio-cafe-IA-4x5.jpg` o `clinica/consultorio-calido.jpg`. Sigue la fórmula v3 de `PROMPTS_FOTOS_LCI_NanoBanana.md`.
```
Use the attached photo as the exact location and lighting reference: keep the same room, walls, furniture, materials and lighting exactly as they are. Do not add windows, doors, plants or views that are not in the photo. A 52-year-old Colombian man from Medellín (paisa), Latin American mestizo features, medium-brown skin, dark brown hair with grey at the temples, dark eyes, serious, composed and elegant expression of a high-profile, affluent person, absorbed in what he is doing, not smiling, not looking at the camera, reviewing a printed lab report seated on the patient side of the desk. The keyboard and monitor face the physician's side of the desk, opposite the patient. Navy sweater, no prints, no logos. The lighting on him is soft and natural, matching the indoor ambient spotlighting, with subtle shadows from the overhead LED cove. Candid documentary photograph, Leica M10-R 50mm f/2.8, Kodak Portra 400 palette, fine natural film grain, visible skin texture and fine lines. Avoid: CGI look, airbrushed skin, text, logos, watermark.
```
ES: el mismo molde sirve para otras escenas: cambia edad, acción y ropa, y mantén la frase de expresión seria.

### F9 · Paciente en la sala de terapias (4:5 vertical)
Adjunta `clinica-real/real-sala-terapia-noche-ciudad.jpg`.
```
Use the attached photo as the exact location and lighting reference: keep the same room, furniture and window exactly as they are. A 47-year-old Colombian woman from Medellín (paisa), Latin American mestizo features, light-tan skin, chestnut hair pulled back, dark eyes, serious, composed and elegant expression of a high-profile, affluent person, absorbed in what she is doing, not smiling, not looking at the camera, resting in the reclining chair with her eyes closed, hands relaxed. Cream linen top, no prints, no logos. Soft natural light matching the room, subtle shadows, city lights glowing outside. Candid documentary photograph, Leica M10-R 50mm f/2.8, Kodak Portra 400 palette, fine natural film grain, visible skin texture. Avoid: CGI look, airbrushed skin, text, logos, watermark.
```

### Fotos que NO se generan: se hacen reales
- Retratos de la Dra. y del equipo: serios, concentrados, de perfil o de tres cuartos, en el consultorio con luz natural. Las fotos de los médicos son siempre reales.
- La Dra. en consulta con una paciente real, con su autorización por escrito.
- Detalle de manos y equipos de la sala de medición, y del laboratorio de procesamiento.
- Recorrido de la clínica en video (ver V6).
- Íconos de órganos: los dibujo yo en SVG con el estilo de la marca.

## 4. Revisión de calidad antes de enviármelos

- Glóbulos rojos con forma de disco bicóncavo, sin deformarse ni fundirse entre sí.
- Cerebro con circunvoluciones nítidas, sin zonas borrosas o repetidas.
- Sin texto, letras, logos, manos ni caras.
- Movimiento lento y continuo, sin saltos ni cortes.
- Zona libre para el texto (tercio izquierdo oscuro) en las escenas de hero.
- Fotos y videos generados con IA **no se presentan como pacientes reales ni como testimonios**. Meta puede marcarlos como "Info de IA" si se usan en redes.

## 5. Lo que hago yo con tus archivos

1. Gradúo el color a la paleta de LCI (navy, azul acero, crema y oro mínimo) con el mismo tratamiento frío de las fotos.
2. Quito el audio y estabilizo el recorte para texto.
3. Codifico para el scroll (fotograma clave en cada cuadro) y creo la versión móvil y el póster.
4. Integro cada escena en la página con la transición que corresponda (ventana que se expande, anillos, frases que se iluminan).
