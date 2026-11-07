# Brief de arranque · Sitio web LCI

Documento para iniciar el trabajo en Claude Code. Fuente de verdad del sitio: arquitectura, contenido, integraciones, despliegue y plan.
Marca: usar siempre `tokens/`, `fonts/`, `brand/` y los skills `lci-design-system` y `lci-piezas-graficas` de este repo.

---

## 1. Decisiones ya tomadas

| Tema | Decisión |
|---|---|
| Dónde se construye | Claude Code (código en repo, versionado, con capturas de verificación) |
| Diseño | Primero dirección visual (home + interna + móvil), aprobada por la Dra., y luego código |
| Idiomas | Español e inglés, con la misma estructura y geometría en ambos |
| Dominio | GoDaddy |
| Hosting | Hostinger |
| Agendamiento | EnfoRisk y Cognimed AI |
| Prioridad | Diseño de marca al nivel del feed 2026 aprobado |

## 2. Qué debe lograr el sitio

1. Que un paciente local o internacional entienda en 30 segundos qué es LCI y cómo es la primera consulta.
2. Que agende su valoración sin fricción (WhatsApp o reserva en línea).
3. Que transmita rigor científico: medición de grado clínico, IA clínica revisada por el médico, evidencia.
4. Que posicione a la Dra. Carolina Rodríguez Morales y al equipo.
5. Que sea rápido, accesible y encontrable (SEO ES/EN).

Público: (a) pacientes en Colombia, (b) pacientes internacionales, principalmente de EE. UU., que viajan a Medellín.

## 3. Stack recomendado

- **Astro** (sitio estático) con TypeScript opcional y CSS propio basado en `tokens/`. Genera HTML puro: rápido, sin servidor, fácil de subir a Hostinger.
- **i18n por rutas**: `/es/…` y `/en/…`, con slugs traducidos y `hreflang`. La raíz `/` redirige según idioma del navegador y recuerda la elección.
- **Contenido** en archivos Markdown/JSON por idioma (`src/content/es`, `src/content/en`). La Dra. puede editar texto sin tocar código.
- **Fuentes** autoalojadas (sin Google Fonts), en WOFF2. **Imágenes** en AVIF/WebP con tamaños responsivos.
- **Formularios y correo**: endpoint PHP pequeño en Hostinger o servicio externo. Ningún dato clínico pasa por el sitio.
- **Despliegue**: build local o en GitHub Actions y subida a `public_html` por Git deploy de Hostinger o SFTP. Verificar qué admite el plan contratado.
- **Repositorio**: crear `lci-website` aparte de este repo, que sigue siendo el kit de marca. Copiar `tokens/`, `fonts/` y los logos necesarios, o enlazarlos como submódulo.

## 4. Arquitectura del sitio (sitemap)

| # | Página | URL ES | URL EN | Función |
|---|---|---|---|---|
| 1 | Home | `/es/` | `/en/` | Tesis, método, datos, Dra., agenda |
| 2 | Evaluación de longevidad | `/es/evaluacion/` | `/en/assessment/` | Primera consulta: qué incluye, después, FAQ |
| 3 | Protocolos | `/es/protocolos/` | `/en/protocols/` | Índice de protocolos presenciales |
| 3a | Protocolo (plantilla) | `/es/protocolos/[slug]/` | `/en/protocols/[slug]/` | Una página por protocolo, ver sección 5 |
| 4 | Ciencia | `/es/ciencia/` | `/en/science/` | Edad biológica, IA clínica, pruebas neurocognitivas, laboratorio |
| 5 | Equipo | `/es/equipo/` | `/en/team/` | Dra. y equipo, con retratos |
| 6 | Pacientes internacionales | `/es/pacientes-internacionales/` | `/en/international-patients/` | Logística, bilingüe, cómo viajar |
| 7 | Agenda | `/es/agenda/` | `/en/schedule/` | Widget de reserva + WhatsApp |
| 8 | Contacto | `/es/contacto/` | `/en/contact/` | Datos, mapa (enlace), formulario breve |
| 9 | Preguntas frecuentes | `/es/preguntas/` | `/en/faq/` | Consolida las FAQ |
| 10 | Conocimiento (fase 2) | `/es/conocimiento/` | `/en/insights/` | Artículos con bibliografía, para SEO |
| 11 | Legales | `/es/privacidad/`, `/es/terminos/`, `/es/aviso-medico/` | `/en/privacy/`, `/en/terms/`, `/en/medical-disclaimer/` | Habeas data, términos, aviso médico |

Navegación principal: Evaluación · Protocolos · Equipo · Ciencia · Contacto, más selector ES/EN y botón "Agendar valoración".
Pie de página: navegación, contacto por idioma, ubicación, aviso médico, redes.
Móvil: menú a pantalla completa y barra fija inferior con "Agendar" + WhatsApp.

## 5. Programas y protocolos (por completar con la Dra.)

El repo confirma solo dos ofertas: la **Evaluación de longevidad** (primera consulta) y los **protocolos presenciales** (hasta ~10 días, según el protocolo). La lista de protocolos o programas que se lanzarán la define la Dra.

Para cada uno se necesita esta ficha, y con ella se genera su página:

| Campo | Ejemplo de qué escribir |
|---|---|
| Nombre ES / EN | |
| Para quién es | Perfil de paciente |
| Qué incluye | Lista |
| Duración | Dato confirmado, nunca estimado |
| Evidencia | Referencias con autores, revista, año y DOI. Se distingue evidencia sólida de emergente |
| Cómo se decide la candidatura | Según resultados de la evaluación |
| Costo | Por política: "se define cuando hay resultados". No publicar precios |
| Imagen | Foto del banco `lci-fotos` o foto real |

Mientras llega la lista, la página `/protocolos/` se maqueta con 3 tarjetas de ejemplo, claramente marcadas como provisionales.

## 6. Bloques de contenido por página

**Home**: hero (tesis + CTA) · datos (2 h+, 48 h, ~10 días, ES·EN) · cómo trabajamos (4 pasos) · lo que medimos (3 tarjetas) · Dra. con misión · pacientes que viajan · agenda · pie.
**Evaluación**: hero · qué incluye (lista) · después de la consulta (línea de tiempo) · FAQ · tarjeta de reserva.
**Ciencia**: cada capacidad con explicación técnica y referencias. Lenguaje médico avanzado, sin simplificar mecanismos.
**Equipo**: retratos en escala de grises del repo (`brand/equipo/retratos/`), nombre, cargo, bio. Confirmar cargos antes de publicar.
**Pacientes internacionales**: recogida en aeropuerto, hotel y transporte organizados por el equipo, que está pendiente del paciente. Atención en inglés y español.

### Datos de LCI confirmados (usar tal cual)
- Muestras procesadas in house, en Colombia y en laboratorios especializados de EE. UU.
- IA clínica propia, siempre revisada por el médico, con pruebas neurocognitivas propias.
- Edad biológica: estimados preliminares con varios relojes biológicos.
- Primera consulta de mínimo 2 horas (nunca "2 horas" exactas). Hay modalidades más largas.
- Plan personalizado según lo que el caso necesita (nunca "12 puntos").
- Órdenes y fórmulas dentro de 48 horas tras la consulta.
- Protocolos presenciales de hasta ~10 días según el protocolo. Costo estimado cuando hay resultados.
- Sin superlativos tipo "pioneros en el mundo" sin documento que los respalde.
- Teléfono: ES (+57) 301 512 39 91 · EN (+57) 300 002 71 15. Instagram ES `@institutoclinicodelongevidad` · EN `@longevityclinicalinstitute`. Correo `carolina_md@longevityclinicalinstitute.com`.

## 7. Integraciones

### Agendamiento: EnfoRisk y Cognimed AI
Antes de diseñar el flujo definitivo hay que responder, con la documentación de cada plataforma:
1. ¿Ofrece enlace público de reserva, widget incrustable (iframe o script) o API?
2. ¿Qué datos pide al paciente y dónde se almacenan?
3. ¿Soporta inglés y español?
4. ¿Cuál se usa para qué? Propuesta de partida: EnfoRisk para la agenda médica y Cognimed AI para las pruebas neurocognitivas. **Confirmar con la Dra.**

Plan por niveles, del más simple al más integrado:
- **Nivel 1**: botón que abre el enlace de reserva de la plataforma, más WhatsApp. Se puede lanzar ya.
- **Nivel 2**: widget incrustado dentro de `/agenda/`, con estilo de marca alrededor.
- **Nivel 3**: reserva propia con API (solo si la plataforma la ofrece y es segura).

**Regla dura**: el sitio público nunca se conecta a historias clínicas ni lee datos de pacientes. Solo reserva de citas y formularios con datos mínimos. Las herramientas internas de EnfoRisk quedan fuera del sitio.

### Otras integraciones
- WhatsApp con enlace directo y número según el idioma.
- Analítica respetuosa (Plausible o GA4) con aviso de cookies.
- Google Search Console y Google Business Profile. Datos estructurados `MedicalClinic` y `Physician` (JSON-LD).
- Metricool ya conectado para redes. Enlaces a Instagram ES/EN.

## 8. Dominio y despliegue (GoDaddy + Hostinger)

1. Confirmar el dominio definitivo (el manual de marca usa `longevityclinicalinstitute.com`) y el plan de Hostinger.
2. **No cambiar los nameservers sin revisar el correo.** Si hay correo en GoDaddy o Microsoft/Google, un cambio de nameservers puede cortarlo. Opción más segura: mantener DNS en GoDaddy y apuntar registros A y `www` a la IP de Hostinger, conservando los MX.
3. Activar SSL, redirigir `www` ↔ raíz y HTTP → HTTPS.
4. Probar primero en un subdominio (`staging.`) antes de apuntar el dominio principal.
5. Redirecciones 301 si el dominio ya tiene una web.

## 9. Requisitos de diseño

- Paleta y tipografía de `tokens/colors.css` y `tokens/typography.css`. Oro máximo 1–2 elementos por página; el resto en navy y azul medio.
- Logo con área de reserva 2X y mínimo 180 px digital. Fondo oscuro: logo blanco o beige. Fondo claro: logo navy.
- Fotografía: expresiones neutras y fría con color real; comida cálida. Arco para hero y retratos.
- Fondos de la familia de 38, rotando familias. No repetir el mismo fondo en secciones contiguas.
- Conector con nodos (motivo de Paola) para pasos y misión.
- Piso tipográfico web: cuerpo ≥ 16 px (17–18 px en escritorio), contraste ≥ 4.5:1 (titulares ≥ 7:1).
- Móvil primero: probar a 375, 768 y 1440 px con capturas antes de cada entrega.
- **Licencia de Mencken Std**: confirmar que incluye uso web (webfont) antes de publicar. Poppins es de licencia abierta (OFL).

## 9b. Experiencia inmersiva (requisito de la Dra.)

El sitio debe verse espectacular, académico, técnico y de lujo, y ser interactivo. La referencia ya construida está en `web/mockup-inmersivo/` (artifact publicado; fuentes `immersive.css`, `immersive.js`, `build2.py`).

| Momento | Efecto | Notas técnicas |
|---|---|---|
| Hero | Hélice de ADN 3D en canvas, reactiva al cursor y al scroll; titular que aparece palabra a palabra; etiquetas flotantes | Canvas 2D propio, pausa fuera de pantalla, DPR máx. 2, menos partículas en móvil |
| Cómo trabajamos | Capítulos con scroll fijado: foto en arco que cambia, anillos y contador por paso | `position: sticky` + IntersectionObserver |
| Ciencia | Mapa orbital interactivo de la evaluación (6 nodos, partículas por las líneas, panel que cambia) | Canvas + botones accesibles |
| Misión | Texto que se ilumina palabra a palabra con el scroll, y marca de agua "LONGEVITY" en paralaje | Scroll ligado a progreso |
| Dra. | Retrato en arco con inclinación 3D al mover el cursor | Solo con puntero fino |
| Clínica | Galería arrastrable con paralaje y flechas | Scroll nativo + drag |
| Global | Cursor propio, botones magnéticos, barra de progreso, cabecera que se vuelve cristal, grano sutil | Cursor y magnetismo solo en escritorio |

Reglas:
- **Rendimiento**: sin librerías pesadas por defecto (vanilla + Astro). Si se necesita más (Three.js, GSAP), cargarlas solo en la sección que las usa. Presupuesto: LCP < 2,5 s en 4G, JS inicial < 150 KB, canvas a 60 fps en un portátil medio.
- **Accesibilidad**: `prefers-reduced-motion` apaga animaciones, la hélice queda estática y la misión se ve completa. Todo el contenido es legible sin JS. Foco visible, navegación por teclado y contraste ≥ 4,5:1.
- **Móvil**: sin cursor ni magnetismo, capítulos apilados con su foto, barra inferior fija con "Agendar" y WhatsApp, menú a pantalla completa.
- **Contenido**: la espectacularidad es visual; los textos usan solo datos confirmados. Las etiquetas y gráficos decorativos no muestran cifras clínicas inventadas.
- **Fase 2 posible**: hélice en WebGL con Three.js, recorrido 3D de la clínica y línea de tiempo animada de la evaluación.

Referencia de estilo y de movimiento aprobada por la Dra.: la página del Longevity Research Institute. Análisis y traducción a LCI en `web/REFERENCIA-LRI.md`.

### Regla de la Dra.: imágenes a todo el ancho
Las imágenes y los videos ocupan **todo el ancho de la página, de borde a borde**, para que el sitio se vea imponente. Nada de recuadros pequeños, arcos, esquinas redondeadas ni fotos en una columna. El texto va encima, sobre un degradado de lectura. Las excepciones son los retratos de personas, que ocupan la mitad de la pantalla también de borde a borde. Para que no se pixelen, las imágenes de sección se entregan en **16:9 de 2560×1440 como mínimo (ideal 3840×2160)** y los videos en 1920×1080 como mínimo.

## 10. Calidad

- Accesibilidad WCAG 2.1 AA: teclado, foco visible, alt en imágenes, `lang` correcto por página.
- Rendimiento: Lighthouse ≥ 90 en móvil, imágenes optimizadas, sin librerías innecesarias.
- SEO: títulos y descripciones únicos por idioma, `hreflang`, sitemap, `robots.txt`, Open Graph.
- Contenido clínico: bibliografía con autores, revista, año y DOI; se distingue evidencia sólida de emergente; sin promesas de curación.
- Legal: política de datos conforme a la Ley 1581 de 2012 (Colombia), consentimiento para datos de salud, aviso médico. Revisar con asesor legal, también por pacientes de EE. UU.

## 11. Plan por fases

| Fase | Entregable | Aprobación |
|---|---|---|
| 0 | Esta lista de pendientes resuelta (sección 12) | Dra. |
| 1 | Dirección visual: home, interna y móvil (mockup HTML) | Dra. |
| 2 | Sistema de componentes + Home en código, ES/EN | Dra. |
| 3 | Evaluación, Equipo, Pacientes internacionales, Agenda, Contacto | Dra. |
| 4 | Protocolos (con las fichas), Ciencia, FAQ, legales | Dra. |
| 5 | Integración de agendamiento (nivel 1 y 2), analítica, SEO | Dra. |
| 6 | Staging en Hostinger, pruebas, corrección | Dra. |
| 7 | Publicación (DNS), redirecciones, Search Console | Dra. |
| 8 | Fase 2: sección Conocimiento | |

## 12. Pendientes que necesita la Dra.

1. Lista de programas y protocolos con la ficha de la sección 5.
2. Dominio definitivo, plan de Hostinger y acceso a GoDaddy (DNS).
3. Documentación o enlaces de EnfoRisk y Cognimed AI para agendamiento.
4. Dirección física de la clínica y horarios.
5. Bios y cargos del equipo, y autorización para publicar sus retratos.
6. Fotos reales de la clínica y del equipo. Varias del banco son generadas con IA.
7. Traducción al español de la misión, para aprobarla.
8. Licencia web de Mencken Std.
9. Textos legales o asesor legal.

---

## Cómo arrancar en Claude Code

1. Crear el repo `lci-website` en GitHub y abrirlo en Claude Code. Agregar este brief como `docs/BRIEF.md`.
2. Crear un `CLAUDE.md` en la raíz con este contenido:

```md
# lci-website
Sitio web del Longevity Clinical Institute. Lee docs/BRIEF.md antes de cualquier tarea.
- Stack: Astro estático, i18n por rutas /es y /en. Despliegue a Hostinger.
- Marca: tokens y fuentes de lci-brand-system. Skills lci-design-system y lci-piezas-graficas.
- Contenido: usa solo los datos confirmados del brief. Nunca inventes cifras, precios ni claims.
- Contenido fuente de la Dra.: reproducirlo al 100%, sin omitir ni resumir.
- Idiomas: ES y EN con la misma geometría. Teléfono e Instagram según idioma.
- Antes de entregar: capturas con Playwright a 375, 768 y 1440 px, y revisar que se vea al nivel del feed 2026.
- El sitio nunca se conecta a historias clínicas ni a datos de pacientes.
```

3. Instalar los plugins de marca (`lci-brand`, `lci-fotos`) en ese repo, según `MIGRACION.md`.
4. Primer mensaje para pegar en Claude Code:

> Lee docs/BRIEF.md y CLAUDE.md. Haz la Fase 2: inicializa Astro con i18n (/es y /en), importa tokens y fuentes de marca, construye el sistema de componentes (header, hero, datos, pasos con conector, tarjetas, retrato en arco, banda de viaje, tarjeta de reserva, footer) y la Home completa en ES y EN. Toma capturas a 375, 768 y 1440 px, corrige y muéstrame el resultado antes de seguir.
