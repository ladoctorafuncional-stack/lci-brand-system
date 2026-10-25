# Catálogo de fondos LCI (aprobado por la Dra., oct 2026)

38 fondos de marca con su función generadora. `HOJA-FONDOS.jpg` = vista de todos; `Catalogo-fondos-LCI.pdf` = catálogo
original (a tamaño A4). Las imágenes aquí son de REFERENCIA (900 px de ancho): para producir, **regenerar a tamaño final
con el código** (`lci-piezas-graficas/assets/recetas_feed.py` = R, `assets/fx.py` = fx; documentos: `efectos_lci.py`).

## Reglas
- Ningún fondo se repite más de 1–2 veces por documento ni en páginas/slides contiguas; alternar oscuro/claro y familia.
- Bajo texto: mallas con `inten` 0.4–0.7; galaxias con el centro en una esquina (texto en zona limpia).
- Páginas claras: solo blanco, azul claro y azul acero — NUNCA beige/cream→azul. Oro solo como toque mínimo.
- `bokeh()` nunca en portadas. Fotos siempre con tratamiento (nunca crudas); ≥1 de cada 3 páginas sin foto.
- Antes de entregar un documento multipágina: hoja de contactos para detectar fondos repetidos.

| Archivo | Cómo se genera |
|---|---|
| `fondos/01-degrades-clasicos-noche.jpg` | R.gradiente('noche') |
| `fondos/02-degrades-clasicos-noche-espejo.jpg` | R.gradiente('noche') espejado |
| `fondos/03-degrades-clasicos-acero.jpg` | R.gradiente('acero') |
| `fondos/04-degrades-clasicos-aurora.jpg` | R.gradiente('aurora') |
| `fondos/05-degrades-clasicos-aurora-invertida.jpg` | R.gradiente('aurora') invertido |
| `fondos/06-degrades-clasicos-niebla-clara.jpg` | R.gradiente('niebla') |
| `fondos/07-degrades-clasicos-niebla-clara-espejo.jpg` | R.gradiente('niebla') espejado |
| `fondos/08-efectos-de-marca-ondas-nivel-1-0.jpg` | R.ondas(nivel=…) |
| `fondos/09-efectos-de-marca-ondas-nivel-66.jpg` | R.ondas(nivel=…) |
| `fondos/10-efectos-de-marca-ondas-nivel-5.jpg` | R.ondas(nivel=…) |
| `fondos/11-efectos-de-marca-microscopia-bacterias.jpg` | R.bacterias() |
| `fondos/12-efectos-de-marca-bokeh-nunca-en-portadas.jpg` | R.bokeh() — NUNCA en portadas |
| `fondos/13-galaxias-fx-py-galaxia-1.jpg` | fx.galaxia(W,H,seed,tono,giro,centro) |
| `fondos/14-galaxias-fx-py-galaxia-2-toque-dorado.jpg` | fx.galaxia(W,H,seed,tono,giro,centro) |
| `fondos/15-galaxias-fx-py-galaxia-3.jpg` | fx.galaxia(W,H,seed,tono,giro,centro) |
| `fondos/16-mallas-fx-py-malla-1-intensidad-7.jpg` | fx.malla(W,H,seed,focal,inten=…) |
| `fondos/17-mallas-fx-py-malla-2-intensidad-38.jpg` | fx.malla(W,H,seed,focal,inten=…) |
| `fondos/18-mallas-fx-py-malla-3-intensidad-4.jpg` | fx.malla(W,H,seed,focal,inten=…) |
| `fondos/19-mesh-gradient-oscuro-fx-py-mesh-oscuro-1.jpg` | fx.mesh(W,H,grid,seed,…) |
| `fondos/20-mesh-gradient-oscuro-fx-py-mesh-oscuro-2.jpg` | fx.mesh(W,H,grid,seed,…) |
| `fondos/21-mesh-gradient-oscuro-fx-py-mesh-oscuro-3-toque-dorado.jpg` | fx.mesh(W,H,grid,seed,…) |
| `fondos/22-mesh-gradient-claro-fx-py-mesh-claro-1.jpg` | fx.mesh(W,H,grid,seed,…) |
| `fondos/23-mesh-gradient-claro-fx-py-mesh-claro-2.jpg` | fx.mesh(W,H,grid,seed,…) |
| `fondos/24-mesh-gradient-claro-fx-py-mesh-claro-3.jpg` | fx.mesh(W,H,grid,seed,…) |
| `fondos/25-mesh-gradient-claro-fx-py-mesh-claro-4.jpg` | fx.mesh(W,H,grid,seed,…) |
| `fondos/26-mesh-gradient-claro-fx-py-mesh-claro-5.jpg` | fx.mesh(W,H,grid,seed,…) |
| `fondos/27-foto-con-tratamiento-de-marca-foto-azul.jpg` | R.tratar(foto,'azul') |
| `fondos/28-foto-con-tratamiento-de-marca-foto-bw.jpg` | R.tratar(foto,'bw') |
| `fondos/29-foto-con-tratamiento-de-marca-foto-frio.jpg` | R.tratar(foto,'frio') |
| `fondos/30-foto-con-tratamiento-de-marca-foto-calido.jpg` | R.tratar(foto,'calido') |
| `fondos/31-foto-con-tratamiento-de-marca-foto-ambar.jpg` | R.tratar(foto,'ambar') |
| `fondos/32-foto-con-tratamiento-de-marca-foto-claro.jpg` | R.tratar(foto,'claro') |
| `fondos/33-foto-con-tratamiento-de-marca-foto-natural.jpg` | R.tratar(foto,'natural') |
| `fondos/34-vidrio-estriado-vidrio-azul.jpg` | R.vidrio(foto,tinte=…) |
| `fondos/35-vidrio-estriado-vidrio-calido.jpg` | R.vidrio(foto,tinte=…) |
| `fondos/36-vidrio-estriado-vidrio-color-real.jpg` | R.vidrio(foto,tinte=…) |
| `fondos/37-movimiento-movimiento-calido.jpg` | R.movimiento(foto,'calido') |
| `fondos/38-movimiento-movimiento-azul.jpg` | R.movimiento(foto,'azul') |
