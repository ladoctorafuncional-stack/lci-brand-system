# Brief de fotografía LCI (oct 2026)

Objetivo: que cada pieza del feed tenga una foto con **temperatura, luz y escala distintas** (ver
`feed-instagram-lci.md` §9). Las fotos actuales de la clínica (mejoradas con IA) son todas cálidas,
de plano general y con la misma luz: sirven, pero solo como 1 de 4 familias.

## 1. Cuatro familias de imagen (repartir ≈25% cada una en el feed)
| Familia | Qué | Tratamiento | Recetas |
|---|---|---|---|
| A. Ciencia sobre oscuro | microscopía (células, mitocondria, neuronas, tejido), moléculas/vidrio 3D sobre negro, tubos de muestra contra fondo oscuro | `azul` / `frio` | R2, R3, R4 |
| B. Cuerpo y movimiento | adultos 45–65 entrenando, corriendo, respirando; espalda, manos, torso; NUNCA fitness juvenil de gimnasio | `bw` | R6, R1 |
| C. Medellín | ciudad al atardecer, montañas con niebla, vegetación, El Poblado/Las Palmas; turismo médico | `ambar` / `frio` | R5, R2 |
| D. Serie clara | laboratorio/consulta high-key, guantes, tubos, superficies blancas, recepción | `claro` | R7 |

## 2. Sesión propia en la clínica (prioridad — lo que más diferencia la marca)
Lista de tomas (vertical 4:5, dejar 40% superior o inferior limpio para texto):
1. Manos de la Dra. tomando muestra / manipulando tubo (detalle, f/2).
2. Tubos de sangre en gradilla, contraluz.
3. Pantalla de bioimpedancia/estudio SIN datos de paciente, desenfocada.
4. Paciente 50+ en prueba de fuerza de agarre o VO2 (perfil, B/N).
5. Pasillo con luz lineal, sin personas, simétrico.
6. Escritorio de consulta: madera + luz lateral, objetos mínimos.
7. Retrato de la Dra.: medio cuerpo, monocromo frío, expresión neutra, fondo oscuro.
8. Retrato de la Dra. de espaldas/perfil mirando hacia la ciudad (ventana).
9. Detalle de suplemento/cápsula sobre superficie oscura (sin marcas comerciales).
10. Recepción high-key, luz de mañana.
11. Exteriores: fachada/entorno con vegetación al atardecer.
12. Medellín desde la clínica o un mirador, hora azul.

Especificaciones para el fotógrafo:
- Óptica 50–85 mm, f/1.8–2.8 (profundidad corta), ISO bajo.
- **Una sola fuente de luz** dominante por toma (ventana o softbox lateral); sombras profundas, sin flash frontal.
- Vertical, RAW, mínimo 4000 px de alto. Dos versiones por toma: con espacio negativo arriba y abajo.
- Sin objetos cotidianos legibles (cartas, cables, logos de terceros, pantallas con datos).
- Consentimiento firmado de toda persona identificable (pacientes y equipo).

## 3. Stock (complemento)
- Pago, recomendado: Adobe Stock, Stocksy (estética editorial, adultos reales), Getty "Creative".
- Gratuito: Unsplash (verificar licencia y crédito opcional), Canva (licencia según plan).
- Búsquedas útiles: "mitochondria microscopy dark", "fluorescence cells black background",
  "mature athlete black and white", "older runner monochrome", "Medellin sunset", "Medellin fog
  mountains", "blood sample tube gloved hand", "glass molecule dark".
- Evitar: personas sonriendo a cámara con bata, stock de "doctor con estetoscopio", gradientes
  genéricos, ADN en 3D azul brillante de catálogo, cualquier imagen ya vista en clínicas competidoras.

## 4. Banco de fotos en Canva
- Carpeta de candidatas: **"LCI · Fotos feed · Selección 1"** (https://www.canva.com/folder/FAHW6ELz2oU),
  16 fotos de Unsplash nombradas por familia (`LCI-A1…D4`). Aprobadas → usar; descartadas → borrar.
- Flujo: buscar en Unsplash/Canva → importar a la carpeta con nombre `LCI-<familia><n> <descripción>` →
  aprobación de la Dra. → descargar original → `tratar()` en `recetas_feed.py`.
