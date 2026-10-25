# Catálogo de piezas — recetas rápidas

Cada receta = template de `marca.py` + la muestra maestra que debe igualar. Verifica siempre
contra el archivo en `muestras-paola/`.

## Póster / story con foto (familia "Reclaim")  → `t_poster`
Caja-acento (Mencken it azul) + titular bold + línea reg + tagline itálico + conector·lista + pill.
Fondo: `M.foto(uri,'navy'|'navy-side')`. Muestras: `poster_reclaim_*`, `poster_brain_reprogram`,
`post_thousand_supplements`, `story_biologically40s`, `story_lab_normal` (theme="light").

## Concepto educativo  → `t_concepto`
Término Mencken display + barra-resaltado (`hl(...,'mid')`) + cuerpo itálico. Claro u oscuro.
Muestras: `post_exosomes_light` (theme="light", logo navy), `poster_creatine_timeline` (oscuro).

## Story editorial  → `t_story`
Sello/wordmark arriba + titular display abajo + hairline + pill. Muestras: `story_dna_heal`,
`story_assessment_clinica`, `story_soon_welcome_*` (usa `vpanel` + `bloque_ubicacion`).

## Curso de péptidos (sub-marca azul eléctrico)  → `t_curso`
`GRAD_CURSO` + término crema italic + barra + `goldbox` oferta + precio en caja navy/oro +
"By LCI". Muestras: `curso_pep_*`, `post_peptidos_retatrutide`.

## Cita / frase  → `t_cita`
Comilla Mencken gigante + frase serif centrada + autor + wordmark. Muestra: `post_carolina_presentacion` (variación).

## Dato / estadística
`stat(numero,label)` sobre fondo navy o foto tratada + contexto + pill. (Ensamblar con helpers.)

## Invitación / evento
Caja-acento + body centrado + `goldbox` (motivo del evento) + `bloque_fecha("RESERVA LA FECHA","SÁB. 6 <span>|</span> JUNIO <span>|</span> 26")`. Muestra: `story_invitacion_eucaristia`.

## Aviso a pacientes (formal)
Eyebrow "Dear Patients," + body Poppins con `<strong>` + `framebox` (quote) + cierre Mencken it +
banda de credenciales (Kharrazian/CFMC/AFMC — logos NO embebidos aún, pedirlos si se requiere).
Muestras: `story_aviso_pacientes_es/en`.

## Infografía con íconos / ring-row / timeline
Ensamblar con helpers; íconos SVG inline stroke. Muestras: `infografia_beneficios_ring`,
`poster_creatine_timeline` (fila de gotas con eje).

## Firma de email (`email_sig`) / Carnet (`carnet`)
Split navy/blanco con foto circular + datos. Pendiente: templates `t_firma`, `t_carnet`
(ver muestras `firma_email_equipo`, `carnets_id_equipo`). Usar membrete navy como fondo.

## Chips de síntomas
`chips(["Fatigue","Inflammation","Brain fog","Hormonal changes"])`. Muestra: `*_lab_normal`.
