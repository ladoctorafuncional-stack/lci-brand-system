---
name: lci-banco-fotos
description: "Banco de fotos oficial del Longevity Clinical Institute (LCI) de la Dra. Carolina Rodríguez: TODAS las fotos usadas en el feed de Instagram 2026 (clínica, fotos reales, retratos de la Dra., científicas, lifestyle), las piezas originales de la diseñadora Paola y el catálogo visual de efectos de marca (tratamientos, vidrio estriado, movimiento, degradados, ondas, microscopía). Úsalo SIEMPRE que una pieza, documento, plan, brochure o presentación de LCI necesite una foto o un fondo, o cuando se pregunte qué fotos o efectos hay disponibles. Las fotos se tratan con el motor de lci-piezas-graficas (recetas_feed.py) o con efectos_lci.py de lci-design-system — nunca se usan crudas."
---

# LCI — Banco de fotos y efectos

Fuente única de las fotos de LCI. No pedir a la Dra. que vuelva a subir estas fotos.

## Contenido
- `fotos/clinica/` — renders de la clínica (consultorio, recepción, salas de medición y terapias, pasillo, barra de café).
- `fotos/clinica-real/` — fotos REALES tomadas con celular en la clínica (sep 2026).
- `fotos/dra-carolina/` — retratos de la Dra. (`dra-de-pie-sin-fondo.png` = recorte; integrarlo SIEMPRE sobre foto real desenfocada de la clínica, nunca sobre fondo plano).
- `fotos/cientificas/` — resonancia, cerebros, laboratorios, músculo, rostros (edad biológica).
- `fotos/lifestyle/` — deporte, dinamómetro, jugos verdes, gafas de masaje, oxímetro, médicos.
- `paola/feed/` — piezas ORIGINALES de Paola usadas en el feed (Reclaim ×3, Brain ages too, Thousand supplements, Muscle Cells, Exosomes, Your body knows, Schedule).
- `paola/muestras/` — las 34 piezas maestras de Paola (estándar visual a igualar).
- `fondos/` + `FONDOS.md` — catálogo aprobado de 38 fondos de marca (degradados, ondas, microscopía, bokeh, galaxias, mallas, mesh oscuro/claro, fotos tratadas, vidrio, movimiento) con su función generadora y reglas de no repetición; `fondos/Catalogo-fondos-LCI.pdf` es el catálogo original.
- `CATALOGO-EFECTOS.jpg` — la misma foto con cada tratamiento y efecto disponible, con la llamada de código exacta.
- `CATALOGO.md` — cada foto con descripción, dónde se usó y tratamiento recomendado.

## Reglas
1. **Nunca foto cruda.** Toda foto lleva tratamiento de marca (ver CATALOGO-EFECTOS.jpg):
   `R.tratar(p, 'bw'|'azul'|'frio'|'calido'|'ambar'|'claro')` · `'natural'` solo en el tour real de la clínica.
   Efectos de superficie: `R.vidrio(p, tinte)` (vidrio estriado) · `R.movimiento(p, tinte)` · fondos sin foto
   `R.gradiente('noche'|'acero'|'aurora'|'niebla')`, `R.ondas()`, `R.bacterias()`; `R.bokeh()` nunca en portadas.
   (`R` = `lci-piezas-graficas/assets/recetas_feed.py`; en documentos usar `lci-design-system/assets/efectos_lci.py`.)
2. **Sin fotos repetidas** entre portadas; una foto ya usada en portada puede reciclarse en interiores con otro efecto (vidrio, movimiento, blur).
3. Revisar CATALOGO.md antes de elegir: las marcadas «sin usar aún» son las primeras candidatas para piezas nuevas.
4. Comida en planes nutricionales: tratamiento cálido apetitoso (`lci_treat 'grade'` de lci-design-system).
5. Fotos de stock/terceros: confirmar derechos con la Dra.; logos de terceros se retocan (inpaint) antes de usar.

## Cómo usar una foto
```python
import glob, sys
BANCO = glob.glob('/mnt/skills/**/lci-banco-fotos', recursive=True)[0]   # o la ruta del plugin instalado
p = BANCO + '/fotos/clinica/pasillo-luces-doradas.jpg'
uri = R.tratar(p, 'calido')            # pieza de redes
# documento: E.hero(E.foto(p, 'calido'), 'Titular', 'acento.')
```

## Fotos generadas con Nano Banana (10-oct-2026)
Usar `references/PROMPTS_FOTOS_LCI_NanoBanana.md` (fórmula maestra v2): personas con rasgos colombianos/paisas, Medellín,
4:5 con espacio para texto, paleta de marca. Nunca generar a los médicos del equipo ni presentar fotos IA como pacientes reales.

## Expresión de las personas (regla de marca, Paola · 10-oct-2026)
En fotos de LCI y de la Dra. Carolina las personas se ven SERIAS, ELEGANTES y ASPIRACIONALES (alto perfil, alto poder adquisitivo), enfocadas en lo suyo. Nunca gente sonriendo a toda hora ni mirando a la cámara. Al elegir fotos del banco o de stock, descartar las que no cumplan; al generar con IA, la frase va en el prompt.

## Prompts de fotos: SIEMPRE decir qué foto de referencia de LCI adjuntar en Nano Banana (ver references/PROMPTS_FOTOS_LCI_NanoBanana.md y REFERENCIAS_NanoBanana.jpg).
