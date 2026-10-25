# Fotos LCI con Nano Banana: fórmula maestra v3 (personas colombianas y paisas)

## Qué le agregué a la fórmula de Gemini

1. **Rasgos colombianos y paisas.** El prompt de Gemini no dice nada de origen, y por eso el modelo sale con rasgos extranjeros. Ahora se describe el origen, el tono de piel, el pelo y la edad. Se mezclan rasgos mestizos variados para no repetir siempre la misma cara.
2. **Medellín en la escena.** Montañas verdes del Valle de Aburrá vistas por la ventana, vegetación tropical (heliconias, helechos, palmas), edificios de El Poblado y luz andina de la mañana.
3. **Encuadre pensado para el diseño.** Formato vertical 4:5. El sujeto va en un tercio y queda un lado o la parte de arriba limpia para el texto, el vidrio y el logo. Sin eso, la foto no sirve como portada.
4. **Colores de la marca.** Ropa en navy, crema, arena o blanco, sin estampados ni logos. Color con saturación baja y tonos cálidos tenues, para que la foto no choque con la paleta.
5. **Edades reales por público.** Ejecutivos de 45 a 60, ejecutiva de 45 a 55 para perimenopausia, deportista de 25 a 35 y biohacker de 28 a 38. Con arrugas finas, canas y textura de piel reales cuando corresponda.
6. **Prohibiciones de marca y de salud.** Sin texto, logos, marcas de agua ni marcas comerciales. Sin escenas de antes y después, sin cuerpos «ideales» exagerados y sin procedimientos médicos mal hechos (guantes, agujas y tubos deben verse correctos).
7. **Continuidad.** Para una serie, se sube como referencia la primera foto aprobada de cada persona, para que mantenga la misma cara en el carrusel.

**Importante:**

- Las fotos hechas con IA nunca se presentan como pacientes reales ni como testimonios.
- Meta puede marcarlas como «Info de IA».
- Las fotos de los médicos del equipo (tú y el Dr. Manuel) siempre son reales, nunca generadas.

---

## Bloque fijo v3 (se pega siempre al final): realismo físico

```
Candid documentary photograph by a photojournalist, shot on Leica M10-R, 50mm Summilux at f/2.8, ISO 400, Kodak Portra 400 color palette, fine natural film grain, slightly imperfect off-center framing as if taken in the moment. Set in a real private longevity clinic in El Poblado, Medellín, Colombia: floor-to-ceiling glass with soft natural reflections of the interior and a faint daylight glare, a few fingerprints and dust specks visible on the glass; tropical garden and green Andean mountains of the Aburrá Valley softly out of focus outside. Warm walnut wood, cream walls, polished concrete with natural scuffs. Lived-in details nearby: a ceramic cup with visible coffee and faint steam, a saucer, a crumpled linen napkin, an open notebook with handwriting, a phone face-down. Hands hold objects with real grip and tension; fabric folds and creases naturally where the body bends. The person and the furniture at the same distance share the same focus; only the background blurs. Natural window light from one side, soft real shadows, muted low-saturation warm tones. Visible skin texture, pores, fine lines, stray hairs. Wardrobe in navy, cream, sand or white, no prints, no logos.
```

**Formato:** el formato vertical 4:5 se elige en el selector de Nano Banana, no en el texto, porque el prompt solo no lo garantiza (la primera foto salió horizontal).

## Por qué cambió el bloque (aprendido de la primera prueba, 10-oct-2026)

1. **Nano Banana no es un modelo de «prompt negativo».** Escribir *forbidden: perfect glass without reflection, levitating objects…* puede sembrar justamente esas ideas. Todo se pide en positivo: «el vidrio tiene reflejos», «las manos agarran con tensión real». La lista *forbidden* queda solo como respaldo corto: `Avoid: CGI look, airbrushed skin, text, logos, watermark.`
2. **f/2.8 en vez de f/1.8.** Con tanto desenfoque la IA separa a la persona del entorno de forma artificial: la silla queda nítida y el piso cambia de golpe. A f/2.8 todo lo que está a la misma distancia queda igual de nítido.
3. **Física del vidrio:** reflejos suaves, brillo de la luz, alguna huella o polvo. Un ventanal perfectamente invisible delata la IA.
4. **El «desorden natural» de un momento real:** taza con café y vapor, plato, servilleta arrugada, libreta y teléfono. El lujo silencioso no es un espacio vacío.
5. **Paleta de película (Portra 400) y saturación baja.** La primera prueba salió con verdes y naranjas muy saturados, como HDR. Además, nuestro tratamiento de marca baja la saturación y añade grano al montar la pieza, lo que disimula los restos de IA.
6. **Mejor truco: subir de referencia una foto REAL de LCI.** Si se adjunta en Nano Banana una foto real de la clínica (sala, consultorio, ventanal) con la indicación `use the attached photo as the exact location and lighting reference`, el fondo es nuestra clínica de verdad y el realismo sube mucho.
7. **Una sola persona por foto, con acciones simples.** Sostener, mirar o caminar. Cada objeto que se manipula multiplica el riesgo de manos raras.

## Foto de referencia: SIEMPRE se indica (regla de la Dra., 10-oct-2026)
Cada prompt de fotos lleva la foto de LCI que se adjunta en Nano Banana (hoja `REFERENCIAS_NanoBanana.jpg`):
**1 · Consultorio** (clinica/consultorio-calido) · **2 · Barra de café** (clinica/barra-cafe) · **3 · Terapia con vista** (clinica/sala-terapia-noche-ciudad; de día: sala-terapia-dia) · **4 · Sala de medición** (clinica-real/real-sala-medicion).
La frase va AL PRINCIPIO del prompt: `Use the attached photo as the exact location and lighting reference: keep the same room, furniture, materials and window light.`
Nunca usar de referencia la recepción con el logo (la IA deforma las letras). Escenas al aire libre: sin referencia.


## Con foto de referencia: el bloque fijo cambia (aprendido 10-oct-2026)
Cuando se adjunta una foto de LCI, el bloque fijo NO describe ventanales, montañas ni vegetación: la IA los inventa encima
de nuestra arquitectura real (en el consultorio puso una ventana donde hay muro). Se reemplaza la parte del lugar por:
```
Use the attached photo as the exact location and lighting reference: keep the same room, walls, furniture, materials and lighting exactly as they are. Do not add windows, doors, plants or views that are not in the photo; the light comes only from the sources visible in the photo.
```
Lo demás del bloque (cámara, película, piel, objetos cotidianos, expresión seria) se mantiene. Ventanal y Medellín solo
en escenas SIN referencia o con la referencia 3 (terapia con vista), que sí tiene ventana.


## Ajustes aprobados en el consultorio (10-oct-2026)
- **Luz integrada al espacio (sugerencia de Gemini):** `the lighting on her is soft and natural, matching the indoor ambient spotlighting, without any studio key light; natural subtle shadows on her face from the overhead LED cove`.
- **Lógica del consultorio (la Dra.):** el teclado y la pantalla quedan del lado del MÉDICO, de espaldas al paciente; el paciente se sienta del lado de visitante. Frase: `the keyboard and monitor face the physician's side of the desk, opposite the patient; she sits on the patient's side`.
- La foto aprobada de referencia para esta escena es `lifestyle/consultorio-cafe-IA-4x5.jpg`.

## Expresión y actitud: regla de marca (Paola, 10-oct-2026)
Las personas de LCI y de la Dra. Carolina se ven **serias, elegantes y aspiracionales**: perfiles de alto nivel y alto poder adquisitivo, **enfocadas en lo suyo** (leer, pensar, entrenar, conversar). **Nunca sonriendo a toda hora ni mirando a la cámara.** Esta frase va SIEMPRE en el prompt: `serious, composed and elegant expression, absorbed in what they are doing, not smiling, not looking at the camera`.

## Frase de persona (se cambia según el público)

```
A [EDAD]-year-old Colombian [man/woman] from Medellín (paisa), Latin American mestizo features, [warm olive / light-tan / medium-brown] skin, [dark brown / black / chestnut] hair, [brown / dark] eyes, serious, composed and elegant expression of a high-profile, affluent person, absorbed in what they are doing, not smiling, not looking at the camera, [ACCIÓN].
```

---

## Las escenas que necesitamos (el orden es el del feed)

| # | Para qué pieza | Persona y acción (va antes del bloque fijo) | Foto de referencia a adjuntar |
|---|---|---|---|
| 1 | **NA Perimenopausia** (ejecutivas) | 48-year-old Colombian woman from Medellín, executive, shoulder-length dark hair with a few grey strands, cream silk blouse, seated by the window holding a cup of coffee, calm and confident, looking slightly off-camera | 2 · Barra de café |
| 2 | NA, lámina interior | same woman doing a controlled squat with a light kettlebell in a minimalist studio, focused | 4 · Sala de medición |
| 3 | **NB Recuperación y lesiones** (deportistas) | 29-year-old Colombian male cyclist from Medellín, athletic build, medium-brown skin, sitting on a treatment bench while a physician examines his knee with both hands, recovery session | 1 · Consultorio |
| 4 | NB, portada alterna | 31-year-old Colombian female runner, ponytail, navy running gear, stretching her hamstring at sunrise on a terrace with the Aburrá Valley mountains behind | — (exterior, sin referencia) |
| 5 | **NC Wearables** (biohackers) | 33-year-old Colombian man from Medellín, short black hair, fitted cream t-shirt, looking at his smartwatch and smart ring data on his phone, seated at a walnut desk, focused serious expression | 4 · Sala de medición |
| 6 | Lp(a) / ApoB / «one measurement» (ejecutivos) | 56-year-old Colombian businessman, salt-and-pepper hair, navy blazer, no tie, reading a printed lab report in a private consultation room, thoughtful | 1 · Consultorio |
| 7 | Brainspan / cerebro (ejecutivos) | 52-year-old Colombian executive man solving a cognitive test on a tablet with a physician beside him (seen from behind, white coat) | 1 · Consultorio |
| 8 | VO₂ máx | 40-year-old Colombian man on a stationary bike wearing a cardiopulmonary exercise test mask, sweat sheen, clinician monitoring in soft focus | 4 · Sala de medición |
| 9 | Fuerza de agarre / sarcopenia | 68-year-old Colombian woman, grey hair in a low bun, gripping a hand dynamometer, focused composed expression, clinician's hand steadying the device | 4 · Sala de medición |
| 10 | Pasos diarios | Colombian couple in their 60s walking briskly under trees in a green Medellín park (Parque Lleras / Ciudad del Río feel), morning light | — (exterior, sin referencia) |
| 11 | Sueño y jet lag social | 38-year-old Colombian woman waking up naturally, morning sunlight across her face, white linen bedding, serene | 3 · Terapia con vista |
| 12 | Pacientes internacionales (EN) | 45-year-old foreign visitor arriving at a warm clinic reception in Medellín, greeted by a Colombian coordinator (30s, dark hair, navy uniform) | 2 · Barra de café |
| 13 | Toma de muestra | Colombian nurse (30s) drawing blood from a patient's arm, correct gloves, tourniquet and labeled tubes, close-up of hands, calm | 1 · Consultorio |
| 14 | Consulta larga | physician (back to camera, white coat) talking with a 50-year-old Colombian woman across a walnut desk, unhurried, coffee cups | 1 · Consultorio |

## Alimentos (sin personas, con productos de Colombia)

| # | Para qué pieza | Escena |
|---|---|---|
| 15 | Microbiota / nutrición | overhead shot of a stoneware bowl with grilled Colombian river trout, avocado, quinoa, roasted ahuyama and fresh herbs, linen napkin, walnut table |
| 16 | Antioxidantes / suplementos | still life of Colombian fruits — gulupa, uchuva, lulo, mora andina — on a cream ceramic plate, side window light |
| 17 | Insulina / metabólico | breakfast plate with eggs, avocado, arepa de chócolo small portion and tinto coffee, honest everyday portion |

Para los alimentos se cambia el inicio del bloque fijo por: `Editorial food photograph shot on Leica M10-R, 50mm at f/2.8, overhead or 45° angle`.

## Microscopía y tejidos

No las generes con IA: la IA inventa estructuras celulares y eso se nota ante un público médico. Usa las fotos reales del NCI, NIAID y Navy Medicine que dejé en tu colección de Unsplash.

---

## Cómo variar la pose sin perder la calidad

Cambia solo la frase de persona y acción, y deja intactos la cámara, el lente a f/1.8, la luz lateral de la mañana, Medellín, la paleta y las prohibiciones.
