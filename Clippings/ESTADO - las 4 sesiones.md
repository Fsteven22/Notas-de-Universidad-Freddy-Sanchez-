---
dg-publish: false
tags: [clippings, estado, coordinacion]
---

# ESTADO - las 4 sesiones (cierre del 27/10/2026)

> [!info] Qué es este archivo
> Inventario de **lo que cada sesión ya dejó hecho** (resultados) y **lo que le falta** (pendientes + próximos pasos), con dueño. Es la respuesta a la pregunta "qué nos falta por hacer a cada uno".
>
> **Quién puede tocar qué:** las secciones de `opencode-onedrive`, `opencode` y `opencode-nube` están **transcritas de su propio log** (`LOG-<agente>.md`): si algo no coincide con lo que esa sesión piensa, lo corrige en su log y avisa acá. La sección de `opencode-site` es la mía.

## Resumen ejecutivo

| Sesión | Zona | Resultado (verificado) | Qué le falta | Siguiente paso |
|---|---|---|---|---|
| `opencode-site` | `site/src/**`, `site/public/` (marca), `site/RUNBOOK.md` §2 y §8, `_no-publicar.txt` | Marca (logo F, favicons, OG, paleta violeta→azul) + 17 patrones de exclusión + aviso visible de material omitido + redirect 308 + deploy sano (0 assets rotos) | **1 cosa depende de vos**: el dominio. Y 2 mejoras que puedo hacer sin permiso (CI anti-fuga, carpeta `_privado/`) | Verificar el deploy de 833 páginas cuando termine Vercel; esperar tu "dale" al dominio |
| `opencode-onedrive` | `2do Semestre/Cálculo Vectorial/**`, `site/scripts/sync-vault.mjs`, `site/RUNBOOK.md`, `site/docs/**`, `Herramientas/SVGs por recrear.md` | Cálculo Vectorial saneado (16 diagramas placeholder → reales, 37 maestros integrados → **0 embeds rotos**), `SVGs por recrear.md` 474 → **0**, fuga `_OCR` de Escucha Activa cerrada, `_no-publicar.txt` unificado, RUNBOOK reescrito | **8 propuestas (P1–P8)**: 3 necesitan tu luz verde (P2 lista blanca, P5 sacar `site/`, P8), 1 es mía (P3 CI), 1 es suya (P4 versionar los QA) | P1 (worktree por sesión) **ya acordada**; P3 y P4 son las de mayor valor |
| `opencode` (3er Semestre) | `3er Semestre/**`, `Herramientas/Mantenimiento/**` | 3er Semestre con **0 wikilinks rotos, 0 errores de formato, 0 PDFs huérfanos**; Speaking Exam 2 completo (nota 336 líneas + 2 SVG mermaid + PDF 7 pág. + PPTX editable); `qa_links.py` / `verificar_nota.py` en verde; push de 8 commits anunciado | **5 pendientes** (§9 de su log): 2 de contenido (embeber PNG, renderizar decks) y 3 de volumen (1039 BAD del 1er/2do/Preuniversitario, ~970 errores de formato, 32 PNG huérfanos) | El #3 (1039 BAD) **lo tenés que decidir vos**: ¿se arreglan o se aceptan? |
| `opencode-nube` | solo `Clippings/**` | PISTA de migración + **corrección de alcance** (AutoSync/OneSync son del teléfono, no de la PC) + mediciones de cuota + hallazgo de que `node_modules`/`dist` no pueden vivir en OneDrive + **criterio de reevaluación** (migrar solo si `Universidad/` > 3 GB) | La PISTA sigue `#pendiente`: faltan **5 datos que solo tenés vos** (cuota real institucional, límite por archivo, retención al terminar la carrera, MDM/OAuth de AutoSync, copyright en cuenta institucional) | Esperar tus respuestas; si confirmás, se actualiza la PISTA a `#procesado` con el plan cerrado |

## 1. `opencode-site` (este repo: marca, exclusiones, deploy)

### Resultados

- **Marca**: logo F (`logo.svg`), `favicon.svg` + `favicon.ico` real (16/32/48 px), `icon-192/512.png`, `apple-touch-icon.png`, `og-neonotes.png` (1200×630). Paleta violeta `#aa66ff` → azul `#00aaff`, acento cian `#00ddbb`, fondo `#05070d`; el verde `#00ff88` quedó **solo para estados semánticos** ("En curso", callout de éxito).
- **Fix del buscador**: sus estilos estaban en un `<style>` *scoped* de Astro y el JS no los heredaba → movidos a `is:global` (resaltado cian, hover violeta).
- **Metadatos**: `og:image` + `twitter:card=summary_large_image` + `theme-color` + canonical.
- **Exclusiones de publicación**: `_no-publicar.txt` con **17 patrones / 61 archivos** (Cambridge, Escucha Activa + derivados `_OCR`, UML Stevens, Empower, `.wmv`, 43 capturas `empower-*.png`) y **3 notas** convertidas a texto plano. Efecto medido: `public/assets` 791,5 → **690,9 MB**; ZIPs de Comunicación 32,4 → 18,8 MB, Inglés III 10,3 → 1,4 MB, Diseño 10,6 → 7,3 MB.
- **Aviso visible de material no publicado** (nuevo): plugin rehype `site/src/lib/rehype-asset-omitido.mjs` + estilos en `content.css`. Antes el embed **desaparecía en silencio**; ahora es un aviso con borde dorado. En producción quedan **2 notas** con aviso (Inglés II C1-C2 e Inglés III U0): lo demás se resolvió (los diagramas de Cálculo que salían como omitidos ya cargan).
- **Redirect 308** de `neonotes.vercel.app` → canonical, en `site/vercel.json` + pasos de panel en `site/RUNBOOK.md` §8.
- **Coordinación**: merge limpio con la sesión OneDrive, protocolo de pushes, acuerdo de las 4 sesiones y veredicto de migración (no migrar ahora).
- **Producción verificada con navegador real**: 0 assets rotos, 0 HTTP 4xx, 0 errores de consola en 8 rutas de muestra.

### Qué me falta

| # | Qué | Depende de |
|---|---|---|
| 1 | **Verificar el deploy con el contenido nuevo** (806 notas · 833 páginas) cuando termine Vercel | nada (lo hago yo) |
| 2 | **Dominio `neonotes.vercel.app`**: paso manual en el panel de Vercel (hoy responde la página "About" de otro proyecto) | **vos** |
| 3 | **CI anti-fuga** (propuesta P3 de `opencode-onedrive`): un workflow que falle el build si un asset de `_no-publicar.txt` aparece en `public/assets` o en los ZIPs. Hoy no hay `.github/workflows` | tu ok (es barato y evita que se repita la fuga de `Escucha Activa`) |
| 4 | **`_privado/` reservado** (decisión 2 del plan): el sync lo ignora por estructura, pero nadie lo usa todavía | tu ok |
| 5 | **Reporte de material omitido en el build**: el aviso nuevo cubre la nota; falta un resumen en la consola/listado de qué se excluyó y por qué | nada (prioridad baja) |

> Lo que **ya está hecho** y no hace falta repetir: `404.astro` propia, `sitemap.xml` (171 KB), `robots.txt`, ZIPs por materia (13), buscador Ctrl+K, flashcards, callouts, KaTeX.

## 2. `opencode-onedrive` (higiene de publicación) — transcrito de su log

### Resultados

- **Cálculo Vectorial**: 16 diagramas que eran *placeholders* sustituidos por los reales; 2 "Teorema Fundamental de Línea" corregidos (tenían contenido de otro diagrama); **37 diagramas maestros integrados en sus 32 notas → 0 embeds de diagramas rotos en todo el vault**.
- **Limpieza**: borrados `test.svg`, 9 SVG superados, 2 duplicados exactos de `Figuras/`, `Tarea 2.md` + su PNG, y **332 previews** de `SVG-Pipeline/previews/` (12,7 MB) + regla `previews/` en `.gitignore`.
- **`Universidad/Herramientas/SVGs por recrear.md`: 474 entradas → 0.**
- **Copyright**: se escapaba `Escucha Activa Parte 1/2_OCR.pdf` (el patrón no cubría el sufijo `_OCR`) → cerrado. `_no-publicar.txt` quedó como **unión** de las dos listas (17 patrones).
- **Publicación**: 805 → **806 notas publicadas · 3 omitidas · 2783 assets referenciados · 833 páginas** sin errores.
- **Documentación**: reescribió `site/RUNBOOK.md` (8 secciones) y dejó `site/docs/HISTORIAL-LANZAMIENTO.md`.
- **Merge final**: resolvió los 2 conflictos del LEEME conservando las dos versiones, con `qa_links.py` y `verificar_nota.py` en verde.

### Qué le falta (sus propuestas P1–P8)

| # | Propuesta | Estado / dueño |
|---|---|---|
| P1 | **Un worktree por sesión** (que nadie comparta working tree) | **Acordada** por las 4 sesiones |
| P2 | **Lista blanca** para el material con copyright (invertir `_no-publicar.txt` a `_publicar.txt`, o mover el material a `Universidad/_privado/`) | **decisión tuya** |
| P3 | **CI que verifique las publicaciones** (que falle si se filtra un asset excluido) | **mi zona** → te la puedo hacer |
| P4 | **Una sola entrada de QA**: mover sus 9 scripts de auditoría (están en `C:\Users\STEVEN~1\AppData\Local\Temp\opencode\`: `qa_fugas_copyright.py`, `qa_resolucion_diagramas.py`, `qa_assets_huerfanos.py`, `qa_svg_titulo.py`…) a `Universidad/Herramientas/` y versionarlos | **su zona** (yo no los muevo) |
| P5 | **Sacar `site/` del vault** (1,83 GB) | **decisión tuya** + forma corregida: **mover**, no borrar dentro de la nube, y **vaciar la papelera de OneDrive** |
| P6 | **Parametrizar rutas absolutas** con una variable `VAULT_ROOT` (~15 archivos) | **su zona**; solo si algún día se migra |
| P7 | **Limpiar los 32 PNG huérfanos** de `Universidad/Figuras/` (material en curso de Discretas) | baja |
| P8 | **Arreglar los `verificar_nota.py` que fallan en Cálculo Vectorial** (vacíos dentro de fences en callouts) | **su zona**; pide luz verde |

## 3. `opencode` (3er Semestre) — transcrito de su log

### Resultados

- **3er Semestre: 0 wikilinks rotos, 0 errores de formato, 0 PDFs huérfanos.** 5 commits (`955c52f`, `ef329c8`, `7fa326a`, `5c75f95`, `86aa483`) + merges, ya dentro de `origin/master`.
- **Speaking Exam 2** (Inglés III, `Unit 1 - Can We Talk`): nota `Speaking Practice # 2.md` (336 líneas, misma estructura que la # 1), 2 diagramas mermaid (`en3-u1-12-01-graph.svg`, `en3-u1-12-02-mind.svg`), PDF de la presentación (7 páginas, 415 KB) y **PPTX editable que queda local, no se publica**; actualizó los 2 índices (Unidad 0 y Unidad 1).
- **Auditoría**: `qa_links.py` y `verificar_nota.py` en verde (0 BAD en 3er Semestre; vault en 1039).
- **Push correcto**: anunciando el turno (`3cb1fdc`) y verificando antes de pushear (806/3, 833 páginas).
- **Aportó al acuerdo**: el patrón de resolución de conflictos del LEEME (conservar HEAD **y** origin, en orden cronológico) y la propuesta de worktree por sesión.

### Qué le falta (§9 de su log)

| # | Qué | Dónde | Prioridad | Dueño |
|---|---|---|---|---|
| 1 | **Embeber los PNG ya renderizados**: Git, componentes, normalización | `3er Semestre/Diseño de Software/Unidad 2 y 5/Archivos/` | media | la sesión |
| 2 | **Renderizar lo que falta**: DSW U3/U4/U5-01 y decks de BD | decks oficiales | baja | la sesión |
| 3 | **Decidir los 1039 BAD de 1er/2do/Preuniversitario** | todo el vault | **requiere tu decisión** | **vos** |
| 4 | **Normalizar ~970 errores de formato** del 1er/2do/Preuniversitario | todo el vault | baja | la sesión |
| 5 | **Revisar los 32 PNG huérfanos de `Figuras/`** (mismo tema que P7) | `Universidad/Figuras/` | baja | la sesión |

## 4. `opencode-nube` (infraestructura / nube) — transcrito de su log

### Resultados

- **PISTA** `PISTA - migracion vault a OneDrive institucional.md` + **corrección de alcance**: AutoSync y OneSync son clientes del **teléfono**, no de la PC → si el teléfono va a la institucional y la PC no, se ven **copias distintas**.
- **Mediciones**: raíz de OneDrive 4,99 GB / 5 GB → `Universidad/` 1,11 GB (contenido real) · `site/` 1,83 GB · `.git/` 1,50 GB · `.obsidian/` 167 MB · backups 0,45 GB. **~3,9 GB liberables** sin migrar.
- **Veredicto**: **no migrar ahora**; criterio de reevaluación: **migrar solo si `Universidad/` supera 3 GB**.
- **Hallazgo compartido con las otras sesiones**: `node_modules` y `dist` **no pueden vivir** dentro de la carpeta sincronizada (OneDrive los deshidrató/borró mientras npm y Astro escribían encima).
- **Cola de push con dueño** por cada pendiente y **regla de zona** corregida (son 4 sesiones, no 3).

### Qué le falta

- La PISTA sigue en **`#pendiente`** porque faltan **5 datos que solo tenés vos**: (1) cuota real por usuario de la institucional, (2) límite por archivo, (3) retención/borrado al terminar la carrera, (4) si el MDM institucional bloquea el OAuth de AutoSync (plan B: app oficial de OneDrive para Android), (5) si el material con copyright puede vivir en una cuenta institucional.
- **No mueve ninguna carpeta** hasta que confirmes esos 5 puntos.
- **No commitea** `Notas de hoy.md` (tuyo) ni `Recursos adicionales/` (scratch).

## 5. Lo que te corresponde decidir (nadie más lo puede hacer)

| # | Decisión | Consecuencia | Estado |
|---|---|---|---|
| 1 | **Vaciar la papelera de OneDrive** | Las 1,8 GB de `site/` ya no están en el clon, pero hasta vaciar la papelera siguen contando en la cuota | pendiente |
| 2 | **Dominio `neonotes.vercel.app`** (panel de Vercel → Settings → Domains; pasos en `site/RUNBOOK.md` §8) | El canonical ya es `neonotes-espol.vercel.app`; el duplicado hoy muestra la página "About" de otro proyecto | pendiente |
| 3 | **P2: lista negra o lista blanca** para el copyright | Hoy: lista negra con 17 patrones / 61 archivos, y funciona. La lista blanca es más difícil que se escape algo | tu decisión |
| 4 | **P5: sacar `site/` del vault** (mover + vaciar papelera) y **`.git/`** (1,50 GB) | Libera ~3,3 GB sin migrar de cuenta; requiere que nadie compile dentro de OneDrive | tu decisión |
| 5 | **1039 BAD del 1er/2do/Preuniversitario** | Se arreglan o se aceptan (los "BAD" son referencias que no resuelven) | tu decisión |
| 6 | **Material con copyright en la cuenta institucional** | Si no se puede, la migración institucional se cae sola | tu decisión (+ consultar a TI/biblioteca) |
| 7 | **`OneSyncFiles-backups/`** (0,45 GB) | Mover a la institucional o borrar | tu decisión |
| 8 | **Tus 2 archivos** en el clon de OneDrive: `Notas de hoy.md` (modificado) y `Recursos adicionales/Speaking Practice.md` (0 KB, scratch) | No los tocó ninguna sesión | tu decisión |
| 9 | **Teléfono**: AutoSync → institucional emparejando solo `DCIM/Camera` (el vault no se empareja) | Reemplaza OneSync (Samsung), que hoy sube las fotos a la cuenta personal | tu decisión |

## 6. Reglas vigentes (resumen del acuerdo, en `00 - LEEME bandeja de pistas.md`)

1. **Un push a la vez**, anunciado antes y después: `PUSHEO EN CURSO …` / `PUSHEADO <hash>`.
2. Antes de pushear: `git fetch origin` → `git log origin/master..HEAD` (lo mío) → `git log HEAD..origin/master` (lo ajeno) → si hay algo ajeno: `git pull --no-rebase`, resolver **conservando las dos versiones**, **build de control** si tocó `site/**` o `Universidad/**`.
3. **Nunca** `--force`, `amend` de un commit publicado, `reset --hard` sobre trabajo ajeno, ni `git add -A` / `commit -a`.
4. **Ruido de CRLF**: `git diff --ignore-cr-at-eol --stat` para confirmar que un `.md` no cambió de verdad, y `git checkout -- <ruta>` para descartarlo.
5. **Commiteá antes de que otra sesión mergee** (un merge pisa lo sin commitear) y usá **un worktree por sesión**.
6. **Zonas reservadas** por sesión; una nota destino = un agente responsable; cada `LOG-<agente>.md` tiene un solo dueño.
7. **En el clon de OneDrive solo viven `Universidad/`, `Clippings/` y el código versionado**: `node_modules/`, `dist/`, `public/assets/`, `public/downloads/` y `notes-md/` **nunca** (OneDrive los pelea con npm y Astro). Para compilar desde ahí: worktree en disco local.

---
**Tags:** #clippings #estado #coordinacion #onedrive
