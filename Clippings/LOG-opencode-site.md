---
dg-publish: false
tags: [clippings, log, opencode-site]
---

# LOG - opencode-site (sesion 2026-10-27)

> [!info] 📌 Alcance de esta sesión
> Bitácora de la sesión **opencode-site** (la que trabaja el sitio y las exclusiones
> de publicación). No confundir con `LOG-opencode.md`, que es de otra sesión en paralelo
> (links rotos en `Universidad/3er Semestre/**` y `Universidad/Herramientas/Mantenimiento/**`).

> [!info] 📑 Índice
>
> - [[#Ámbito]]
> - [[#Archivos que reservo (no editar sin avisar)]]
> - [[#Commits de esta sesión]]
> - [[#Pendientes (requieren decisión)]]
> - [[#Verificación de la rama OneDrive (2026-10-27 11:41)]]
> - [[#No toco sin avisar]]
> - [[#Notas técnicas para quien siga]]
> - [[#2026-10-27 (tarde) — Merge con la sesión OneDrive + aviso de material no publicado]]
> - [[#2026-10-27 (noche) — Acuerdo entre sesiones: commits, push y migración a OneDrive]]
> - [[#Incidente que causé y como lo arreglé (27/10/2026, noche)]]
> - [[#Cierre de la ronda de coordinación (27/10/2026, noche)]]
> - [[#Tablero de estado (27/10/2026, tarde)]]

## Ámbito

> [!info] 🗂️ Ámbito
>
> - Repo: `notas-nexus-unificado` (rama `master`, push a `origin/master`).
> - Deploy: `https://neonotes-espol.vercel.app` (Astro + Vercel, 828 páginas).
> - Vault con dos copias que se deben mantener iguales: `notas-nexus-unificado/Universidad/` (despliega) y `OneSyncFiles/Universidad/` (trabajo).
> - Flujo: `npm run sync` (`$env:VAULT_DIR="..\Universidad"`) → `npm run build` → `git add <rutas exactas>` → commit → push → esperar deploy → verificar en producción.

## Archivos que reservo (no editar sin avisar)

> [!tip] 📋 Archivos que reservo
>
> | Ruta | Qué hago |
> |---|---|
> | `site/src/styles/nexus.css`, `site/src/styles/content.css` | Paleta de marca |
> | `site/src/components/SearchModal.astro` | Buscador (estilos y resaltado) |
> | `site/src/pages/index.astro`, `site/src/layouts/Base.astro` | Portada y metadatos |
> | `site/public/logo.svg`, `favicon.svg`, `og-neonotes.png`, `icon-*.png`, `apple-touch-icon.png` | Marca |
> | `Universidad/_no-publicar.txt` (repo y OneDrive) | Qué se publica |
> | `2do Semestre/Comunicación/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` | Exclusiones |
> | `3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` | Exclusiones (tú dentro de 3er Semestre) |
> | `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Recursos Unidad 0.md` | Exclusiones (tú dentro de 3er Semestre) |

## Commits de esta sesión

> [!success] ✅ Commits de esta sesión
>
> | Commit | Alcance |
> |---|---|
> | `4a3e443` | Site: logo propio, portada OG y favicon |
> | `ba9ad13` | Site: paleta violeta→azul + fix de estilos del buscador |
> | `88b3fac` | Vault: excluye Escucha Activa, UML Stevens y material Cambridge |
> | `486f927` | Vault: excluye video de dinámicas y capturas Cambridge |
> | `7eeef28` | Site: redirect 308 del dominio duplicado al canonical + sección de dominios en RUNBOOK |

> [!success] ✅ Efecto medido
>
> **Efecto:** ZIP Comunicación 32,4→18,8 MB, Inglés III 10,3→1,4 MB, Diseño 10,6→7,3 MB; assets publicados 791→691 MB.

## Pendientes (requieren decisión)

> [!warning] ⏳ Pendientes (requieren decisión)
>
> 1. **6 notas sin `dg-publish`** (no se publican):
> - `1er Semestre/Física Mecánica/Unidad 0 - Guias y Ejercicios/Guías y Ejercicios (Prof. Zambrano).md`
> - `3er Semestre/Fundamentos de Electricidad y Sistemas Digitales/Practico/Practicas del Laboratorio/Práctica 3 FESD/Práctica 3 — Diodos y Transistores.md`
> - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md`
> - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Capturas Empower U10-U12/Libro de ingles ultimas unidades.md`
> - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Capturas Empower U7-U10/Libro de ingles las primeras unidades.md`
> - `3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/Talleres/Tarea 2.md`
> 2. **Dominio duplicado — falta un paso en el panel (no se puede hacer desde el repo).** `neonotes.vercel.app` lo responde un proyecto de Vercel aparte (la página "About" por defecto), no este sitio. Ya agregué el redirect 308 por host en `site/vercel.json` (se activa solo si el dominio pasa a apuntar a este proyecto) y los pasos en `site/RUNBOOK.md` sección 8:
> - Panel → proyecto `neonotes` (el que muestra "About") → Settings → Domains: redirigir a `https://neonotes-espol.vercel.app` o borrarlo.
> - O borrarlo y en `neonotes-espol` → Settings → Domains → Add Domain → `neonotes.vercel.app`.
> - Verificar: `curl -I https://neonotes.vercel.app/3er-semestre/` → 308 con `Location` al canonical.
> - Nota: el CLI de Vercel de esta máquina no tiene token válido (`vercel whoami` → "The specified token is not valid"), por eso no se puede hacer por terminal.
> 3. `favicon.ico` da 404 (solo hay `.svg`).
> 4. **Sandbox desactualizado:** `notas-nexus` (`C:\Users\STEVEN~1\Desktop\Proyectos`) sirve la versión verde del sitio y su `PLAN-PUBLICACION.md` dice "baseline 798".
> 5. **Divergencia de vault:** la copia de OneDrive de `3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` es una versión anterior (la del repo es la vigente).
> 6. **Colisión con la otra sesión `opencode`:** las dos creamos `Universidad/_no-publicar.txt` (la mía en `master` con 15 entradas; la de la otra en `backup-pre-fix-links` con 13). Al integrar, **unir las listas** y re-sincronizar.


## Verificación de la rama OneDrive (2026-10-27 11:41)

> [!info] 💻 Verificación de la rama OneDrive
>
> Compilé su rama onedrive/master (2409dfd) en un **worktree aislado** (wt-onedrive, ya eliminado) con VAULT_DIR apuntando a su vault de OneDrive:

> [!success] ✅ Resultado del build
>
> - **Build OK**: 831 páginas, exit 0 (mías que mis 828: publicaron 3 notas más).
> - **Exclusiones OK**: ninguno de los archivos con copyright/cambridge/video aparece en public/assets.
> - **Marca intacta**: logo.svg, avicon.svg, og-neonotes.png e icon-192.png presentes en su build.
> - **Falta mi redirect**: su site/vercel.json no tiene el bloque
> edirects (mi commit 7eeef28); hay que re-aplicarlo al integrar.

> [!note] 📋 Diferencias de notas por unificar
>
> Diferencias de notas que quedan por unificar:

> [!tip] 🗂️ Las 3 diferencias
>
> - 3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md: en su clon tiene dg-publish: true (y describe las carpetas en texto, sin embeds de Cambridge) → tras el merge **se publica**; en el mío no tenía flag.
> - 3er Semestre/Sistema de Bases de Datos/.../Talleres/Tarea 2.md: no existe en su clon (lo borraron); en el mío sigue con dg-publish: false.
> - 1er Semester/Física Mecánica/.../Guías y Ejercicios (Prof. Zambrano).md: dg-publish: true en ambos clones, pero su sync lo cuenta como omitida. Conteos: mío 802/6, ellos 805/3 — falta que definan la lista final.

> [!info] 🔗 Remoto `onedrive` añadido (solo lectura)
>
> Añadí el remoto onedrive (solo lectura) al clon Desktop para inspeccionar su rama sin tocar su working copy.

## No toco sin avisar

> [!warning] ⚠️ No toco sin avisar (estilos)
>
> - Cambios de color/estilos del sitio (`nexus.css`, `content.css`, `SearchModal.astro`, `index.astro`, `Base.astro`).
> - Archivos de marca en `site/public/` (logo, favicon, OG, iconos).
> - `_no-publicar.txt` y las 3 notas reservadas de la tabla de arriba.
> - Los ~17 `.md` con CRLF del vault: aparecen modificados en `git status` pero no son cambios míos.
> - El trabajo de la otra sesión en `Universidad/3er Semestre/**` (links) y `Universidad/Herramientas/Mantenimiento/**`.

## Notas técnicas para quien siga

> [!tip] 💡 Notas técnicas para quien siga
>
> - `git diff --name-only` escapa los paths: usar `-c core.quotePath=false`.
> - `git add -A` está prohibido: stagear rutas exactas (los `.md` con CRLF se cuelan).
> - `node -e` con el signo dollar + llave se rompe en PowerShell: escribir scripts `.mjs`.
> - Servidor estático para probar `dist`: `node static-server.mjs <raiz> <puerto>` (ojo: el 8099 lo tenía un servidor viejo apuntando al sandbox).
> - Los nombres de archivo con á/é en la ruta rompen `Start-Process -ArgumentList`; usar `C:\Users\STEVEN~1\...`.
> - El `<style>` de un componente Astro es *scoped*: lo que el JS inyecta en el DOM no lo toma, hay que moverlo a `is:global`.

## 2026-10-27 (tarde) — Merge con la sesión OneDrive + aviso de material no publicado

> [!success] ✅ Merge con la sesión OneDrive + aviso de material no publicado
>
> - **Merge limpio:** la sesión OneDrive pusheó `8fedc9f`/`b5c5669`; hice `git merge origin/master` y quedó **sin conflictos** (historial lineal, sus commits ya quedaban como ancestros).
> - Antes del merge: `git checkout -- Universidad` para descartar los 17 `.md` que aparecían modificados **solo por CRLF** (verificado con `git diff --ignore-cr-at-eol` vacío). Es el mismo ruido que bloqueaba los merges de la otra sesión.
> - Commit propio integrado: `66c9eca` (favicon.ico + plugin del aviso). `origin/master` = `f69ed87`.
> - **Build integrado:** 831 páginas (antes 828), exit 0, 0 material excluido filtrado, marca y redirect intactos.
> - **Nuevo: `site/src/lib/rehype-asset-omitido.mjs`** (registrado en `site/astro.config.mjs:35`).
> - El sync deja marcadores `<!-- nx:asset-omitido NOMBRE -->` / `<!-- nx:link-omitido NOMBRE -->` cuando un asset no se publica; hasta ahora **desaparecían en silencio** y el lector pensaba que la nota estaba incompleta.
> - El plugin los convierte en un aviso visible (borde dorado punteado, título en mayúsculas) + estilos en `site/src/styles/content.css`.
> - Detalle técnico: el marcador llega como nodo hast **`raw`** cuando está inline dentro de una lista/cita (`> - <!-- ... -->`), no como `comment`; el plugin cubre los dos casos.
> - **Producción verificada:** el aviso se ve en las 2 notas con material no publicado (Inglés II C1-C2 e Inglés III Unidad 0); los diagramas de Cálculo que antes salían como omitidos **ahora cargan** (el refactor de `Diagramas/` de la otra sesión los arregló), así que los avisos bajaron de 6 a 2. 0 errores de consola.
> - **`favicon.ico` real:** `site/public/favicon.ico` (16/32/48 px) + `<link rel="icon" type="image/x-icon" sizes="32x32">` en `Base.astro`. En producción responde **200** `image/vnd.microsoft.icon` (antes solo existía `favicon.svg`).
> - **Verificado que NO se rompió nada:** redirect 308 del dominio (`site/vercel.json`), sección 8 del RUNBOOK, `og:image`, logo, exclusiones (Cambridge/Escucha Activa/UML/Empower/wmv → 0 archivos filtrados).
> - **Pendiente (no bloquea):** el sandbox `C:\Users\STEVEN~1\Desktop\Proyectos\notas-nexus\` sigue con la versión verde y su `PLAN-PUBLICACION.md` dice "baseline 798"; y el dominio `neonotes.vercel.app` necesita el paso manual del panel de Vercel (CLI sin token válido, `gh` no instalado).

---

## 2026-10-27 (noche) — Acuerdo entre sesiones: commits, push y migración a OneDrive

> [!info] 📋 Inventario verificado de las 4 sesiones
>
> - **Inventario verificado** (no supuesto) del estado de las 4 sesiones contra los clones:
> - `opencode-site` (yo): nada pendiente. `master` = `origin/master` = `6ffea83`, árbol limpio.
> - `opencode-onedrive`: **3 commits sin pushear** en su clon de OneDrive (`c4a84b5`, `4fd4960`, `ba68d18`) → tocan `Universidad/3er Semestre/Ingles III/**`, el LEEME y su log.
> - `opencode` (links): **nada pendiente**; sus 5 commits (`955c52f`, `ef329c8`, `7fa326a`, `5c75f95`, `86aa483`) ya están dentro de `origin/master` (verificado con `git merge-base --is-ancestor`).
> - `opencode-nube`: sin commits, pero 2 archivos sin commitear en `Clippings/` (`LOG-opencode-nube.md`, `PISTA - migracion vault a OneDrive institucional.md`) + `Recursos adicionales/Speaking Practice.md` (archivo vacío de 0 KB en la raíz de OneDrive).
> - **Acuerdo escrito en el LEEME** (bloque "🤝 ACUERDO entre sesiones"): inventario de pendientes, flujo único de push con candado ("un push a la vez, siempre anunciado"), una sola copia editable por ruta (Desktop = `site/**`, OneDrive = `Universidad/**`) y el veredicto sobre la migración.
> - **Veredicto sobre la migración (respuesta a la pista de `opencode-nube`):** **no es necesaria** y no es la solución de la cuota. De los 4,99 GB de la raíz de OneDrive, solo **1,11 GB** son contenido real (`Universidad/`); `site/` (1,83 GB) y `.git/` (1,50 GB) son regenerable/espejado. Limpiando ambos, la cuenta personal baja a **~1,2 GB** sin cambiar de cuenta. La migración institucional queda **opcional** (solo si el vault crece o si se quiere la misma cuenta en el teléfono) y, si se hace, el procedimiento correcto es **clon fresco**, no mover la carpeta (Files On-Demand + git = `.git` corrupto).
> - **Mediciones nuevas de esta sesión** (root de `OneSyncFiles`): `Universidad/` 1.110,5 MB · `site/` 1.829,4 MB · `.git/` 1.501,2 MB (pack 566,6 MB) · `.obsidian/` 166,6 MB · `Contenido Extra/` 1,7 MB · `Recursos adicionales/` 0 MB · `.git/gc.pid` **roto** (`18272 Steven`, `git gc` se niega a correr hasta borrarlo).
> - **Dato de la ruta Desktop:** el `.git` del clon canónico pesa 610 MB (fuera de OneDrive) → el de OneDrive es redundante para el mirror de GitHub.
> - **No hice** (por decisión propia y por zona reservada): no pushear los commits de otra sesión, no borrar `site/` ni `.git/` de OneDrive, no tocar las 13 rutas hardcodeadas de `Herramientas/**`, no mover carpetas.
> - **Firmado en el LEEME:** zona que toco = `site/src/**`, `site/public/` (marca), `site/RUNBOOK.md` §2 y §8, `Universidad/_no-publicar.txt` + las 3 notas de exclusiones ya publicadas, y el LEEME + este log. Commits sin pushear: ninguno.

### Incidente que causé y como lo arreglé (27/10/2026, noche)

> [!warning] ⚠️ Incidente que causé y cómo lo arreglé
>
> - **Qué hice mal:** borré los derivados de `OneDrive\OneSyncFiles\site` (`node_modules`, `dist`, `public/assets`, `public/downloads`, `notes-md`, `public/pdfjs/build` — 1,83 GB) **mientras había 2 builds de Astro corriendo en ese clon** → el build de la sesión `opencode-onedrive` murió. No verifiqué los procesos antes de borrar. Es error mío y quedó asumido en el LEEME.
> - **Cómo lo arreglo:** dejé corriendo la restauración completa de su clon (`npm ci` → `npm run sync` → `npm run build`, log en `C:\Users\STEVEN~1\AppData\Local\Temp\opencode\work\restore-onedrive.log`). Verificado: `node_modules` 210,7 MB, `public/assets` 649,8 MB y `notes-md` 13 MB de vuelta; el build regenerated `dist`. **No toqué** `.git/`, `.obsidian/`, `Notas de hoy.md`, la PISTA de `opencode-nube`, `Recursos adicionales/` ni ningún archivo versionado (`git status` de su clon no muestra versionados tocados).
> - **Hallazgo técnico que corrige el plan de limpieza:** **borrar dentro de la carpeta sincronizada no libera cuota de forma confiable**: OneDrive **re-hidrata** lo que está en la nube (`node_modules` volvió solo: 59 MB → 100 MB en un minuto mientras lo miraba). La forma correcta es **mover** la carpeta fuera del árbol de OneDrive (el clon canónico `Desktop\Proyectos\notas-nexus-unificado\site` ya existe) y **vaciar la papelera de OneDrive**. Y nunca con un build corriendo.
> - **Adopto el acuerdo de `opencode-onedrive`** (`47614c0`): su cola de push, su tabla de 4 sesiones con la corrección de zonas (`3er Semestre/**` es de `opencode`, no de `opencode-onedrive`), la rama `backup-pre-fix-links` como respaldo que no se mergea ni se borra, y el veredicto de migración (no necesaria; primero limpiar). Retiro mi petición de pushear sus commits: los pushea la sesión dueña.
> - **Cambio de rumbo:** el "Acuerdo 4" que escribí decía "borrar `site/` y `.git/`"; queda corregido por lo de arriba (mover, no borrar dentro de la nube).

### Cierre de la ronda de coordinación (27/10/2026, noche)

> [!success] ✅ Las 4 sesiones responden y firman
>
> - **Las 4 sesiones respondieron y firman el mismo acuerdo**: `opencode-site` (yo), `opencode-onedrive`, `opencode` (3er Semestre) y `opencode-nube`. Todo está en el LEEME, con la respuesta de cada una.
> - **Los commits pendientes de la otra sesión los pusheó su dueña** (`3cb1fdc`, luego `2ea2d3d`), anunciando el turno antes y después, tal como marca el protocolo. Yo solo pusheo commits de documentación: `cd01900` (merge con las dos versiones del LEEME conservadas) y `8a63b04` (estado final consolidado). `origin/master` = `8a63b04`.
> - **Verificado que no queda nada pendiente:** los 5 commits de `opencode-onedrive` y los 3 de `opencode` están dentro de `origin/master` (con `git merge-base --is-ancestor` sobre los 3 clones).
> - **Contenido verificado por la sesión OneDrive en un worktree local:** 806 notas publicadas · 3 omitidas · 17 patrones / 61 archivos excluidos · 2783 assets referenciados · **833 páginas** sin errores.
> - **Evidencia consolidada sobre OneDrive:** `node_modules` y `dist` **no pueden vivir** dentro de la carpeta sincronizada. Lo vieron las dos sesiones: (a) la OneDrive seeing `node_modules` vaciarse solo y un `npm ci` a medias, y (b) mi restauración en su clon (`npm ci` → sync → build, 832 páginas OK) que **minutos después OneDrive volvió a borrar `node_modules` y `dist`**. Regla final: en el clon de OneDrive solo `Universidad/`, `Clippings/` y el código versionado; para compilar desde ahí, **worktree en disco local**.
> - **Cuota:** las 1,8 GB de `site/` generadas ya no están en el clon de OneDrive (las borró OneDrive o yo, sin diferencia). La nube las libera cuando el usuario **vacía la papelera de OneDrive**. `.git/` (1,50 GB) **no se tocó**, como pidió la sesión dueña.
> - **Lo que queda para el usuario:** vaciar la papelera de OneDrive · el paso de panel del dominio `neonotes.vercel.app` · si quiere la cuenta institucional (opcional) · sus 2 archivos sueltos (`Notas de hoy.md`, `Recursos adicionales/Speaking Practice.md`).
> - **Mi clon Desktop quedó intacto y es el que compila de verdad:** `site/node_modules` presente, `site/dist` con 832 HTML, `site/public/assets` 649,4 MB.

### Tablero de estado (27/10/2026, tarde)

> [!note] 📋 Tablero de estado
>
> - La sesión `opencode-onedrive` creó el **tablero canónico** `Clippings/ESTADO - las 4 sesiones.md` (`129d753`) con un bloque por sesión (Resultados / Qué falta / Próximos pasos) y pidió que cada una confirme su bloque.
> - Yo había escrito un inventario propio con el **mismo nombre** → conflicto `add/add` al integrar. **Resolución: adopted su tablero como canónico** (no tener dos tableros con el mismo propósito) y **actualicé solo mi bloque** con lo verificado en esta ronda: producción con 0 assets rotos / 0 errores de consola, `/favicon.ico` 200 `image/vnd.microsoft.icon`, aviso "material no publicado" visible, espejo refrescado (831 páginas, sin verde de marca) y `master` = `origin/master`.
> - **Lo que me queda** (ya en mi bloque del tablero): (1) el **paso manual del panel de Vercel** para `neonotes.vercel.app` → **vos**; (2) verificar el deploy de 833 páginas cuando termine Vercel → yo; (3) **CI anti-fuga** (P3 de `opencode-onedrive`: que el build falle si un asset de `_no-publicar.txt` aparece en `public/assets` o en los ZIPs) → mi zona, falta tu ok; (4) carpeta `_privado/` reservada → tu ok; (5) reporte en consola de material excluido → bajo.
> - Los 2 pushes de esta ronda: `19ac29c` (tablero) y `1b0bb6c` (merge del tablero + mi bloque actualizado). Hubo que reintentar el push 2 veces porque la otra sesión pusheó en medio: es exactamente el caso que cubre el "candado de push" del LEEME (yo avisé, pero no bloqueé).

### Cierre de carril C (2026-10-29)

> [!success] ✅ Carril C cerrado — `opencode-site`

> - **39 SVG NaN regenerados** desde cero con `mmdc` a partir de 39 specs nuevos en `Universidad/Herramientas/SVG-Pipeline/mmd2/fix_nan/` (OK=39/39). Copiados al vault fuera de OneDrive.
> - **214 links rotos fijos** en 98 notas (`[[Base|Texto]]` / `[[Base#Encabezado|Texto]]`), byte-level preservando finales de línea originales. Verificado con `qa_links.py`: BAD 1039 → 825.
> - **19 `.mmd` obsoletos borrados** (16 duplicados en-dash de `cv_auto`, 2 artefactos de prueba, 1 fuente genérica de `cv_lote4`).
> - **`Universidad/Herramientas/SVGs por recrear.md` en 0** (0 embeds de imagen rotos).
> - **554 targets restantes** (825 ocurrencias) → `Clippings/PROPUESTAS - links rotos (carril C).md` (180 aproximado, 374 sin-destino).
> - **8 mindmaps `com-u*-graph.svg`** de Comunicación reportados como limpieza pendiente (rotos, no embebidos en ninguna nota).
> - **554 targets** (825 ocurrencias) → `Clippings/PROPUESTAS - links rotos (carril C).md`; los **180 aproximados** → `Clippings/REPORTE - links aproximados (carril C).md` (acción propuesta `REDIRIGIR` / `REVISAR`), esperando revisión del usuario.
> - **CI anti-fuga (P3):** lo implementó `opencode-onedrive` (`ci-privacy.yml` + `ci-check-privado.mjs`). Mi workflow duplicado quedó **revertido** (`44bdf1d`).
> - **`_privado/` (P4): descartado** — la lista negra `_no-publicar.txt` (17 patrones) ya excluye el material con copyright al publicar.
>
> ### Fix CRCRLF — nota que había dejado de publicarse (29/10/2026)
>
> - **Síntoma:** el sync bajó de **806 a 805 notas publicadas** y `02 - Representación gráfica.md` apareció en la lista de omitidas, aunque su frontmatter sí declara `dg-publish: true`.
> - **Causa:** el archivo tenía **160 líneas con `

`** (CR duplicado). El regex de frontmatter de `site/scripts/sync-vault.mjs:68` (`/^---\r?\n([\s\S]*?)\r?\n---/`) no matcheaba → la nota se trata como "sin dg-publish" → **omitida del sitio**. Consecuencia extra: el archivo se leía como **327 líneas** en vez de 167 (160 líneas vacías espurias).
> - **Fix:** solo los bytes de fin de línea (`

` → `
`). **0 palabras cambiadas**, verificado con `HEAD` sin los `
` extra == archivo corregido. Blob resultante: 100% LF (167 líneas), coherente con `.gitattributes` (`*.md text eol=lf`).
> - **Barrido del vault:** **1 solo `.md` afectado**. Los 42 archivos no-texto con `

` son **PDF/WMV** (binario, falsos positivos).
> - **Resultado del fix aislado:** 806 publicadas / 2820 assets (la nota vuelve al sitio).
> - **POST-merge (medicion final, `origin/master` reestructurado por el carril B):** **795 publicadas · 28 omitidas · 2624 assets (la Pasada 2 del carril B arregló un frontmatter mas) · 17 patrones / 59 archivos excluidos**. La baja no es mia ni un bug del gate: son los **`00 - Leeme Unidad 0.md` nuevos** de la taxonomia universal (+ materiales que quedaron dentro de `Material de clase/`) que nacieron sin `dg-publish: true`. Reportado en ESTADO, item 8 del bloque 2.
> - **Zona:** el archivo es de Preuniversitario (zona compartida / carril B) → **avisado en el LEEME** para `opencode`. No toco el bloque de otra sesión.
>
> ### Estado del sitio tras el merge (medido 29/10/2026)
>
> - **8 notas omitidas:** 1 de Física Mecánica (`Guías y Ejercicios (Prof. Zambrano).md`) · 2 libros de Inglés III · **5 `Recursos visuales.md` de 3er Semestre que nacieron sin `dg-publish: true`** (zona `opencode` / `opencode-nube` → decisión del usuario).
> - Las 5 son las nuevas del carril D1 (`opencode-nube`, commit `509769a`): son índice de recursos con links verificados, probablemente publicables, pero **no las toco** (no son mi zona).
> - **Deploy:** falta verificar en `neonotes-espol.vercel.app` cuando Vercel termine con este contenido.
> - **Dominio `neonotes.vercel.app`:** confirmado con el usuario que **no existe en su panel de Vercel** (solo `neonotes-espol.vercel.app` y `notas-de-universidad-freddy-sanchez.vercel.app` → 307). El 308 por host de `site/vercel.json` queda como **protección pasiva**; **no requiere ninguna acción del usuario**. El paso de panel queda **cerrado**.

---
**Tags:** #clippings #log #opencode-site

> ### Ronda de links autorizada por el usuario (30/10/2026)
>
> | Commits | Que | Verificado |
> |---|---|---|
> | `2cec9b0` | 180 wikilinks redirigidos (104 targets REDIRIGIR del reporte) | 190 ocurrencias detectadas, 180 aplicadas (10 autorreferencias) |
> | `cc2dfae` | 522 wikilinks neutralizados (sin-destino) | 532 detectadas, 522 aplicadas en 167 notas |
> | `83b755b` | 20 notas republicadas | 10 con BOM + 10 Leemes sin frontmatter |
>
> - **Medición:** `qa_links.py` **BAD 852 · 150** (1039 al abrir el carril C). Sync: **815 publicadas · 9 omitidas · 2850 assets**.
> - **BOM:** 11 `.md` del vault tenían BOM UTF-8; rompe el regex `^---` del frontmatter de
>   `sync-vault.mjs`. Al quitarlo, **0 palabras cambiadas** (verificado byte a byte). El de
>   Física Mecánica también estaba oculto por eso.
> - **Hallazgo para el carril B/D1:** `00 - Leeme Unidad 0.md` de BD tiene **mojibake**
>   (no es doble-codificación pura) · reportado, **no tocado**.
> - **Pendiente del usuario:** los **76 targets `REVISAR`** del reporte (destino sugerido en otra
>   materia; aplicarlos crearía links engañosos). Neutralizo a medida que me lo indique.
