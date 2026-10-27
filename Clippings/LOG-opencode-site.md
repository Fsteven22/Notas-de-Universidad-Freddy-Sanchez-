---
dg-publish: false
tags: [clippings, log, opencode-site]
---

# LOG - opencode-site (sesion 2026-10-27)

> Bitácora de la sesión **opencode-site** (la que trabaja el sitio y las exclusiones
> de publicación). No confundir con `LOG-opencode.md`, que es de otra sesión en paralelo
> (links rotos en `Universidad/3er Semestre/**` y `Universidad/Herramientas/Mantenimiento/**`).

## Ámbito

- Repo: `notas-nexus-unificado` (rama `master`, push a `origin/master`).
- Deploy: `https://neonotes-espol.vercel.app` (Astro + Vercel, 828 páginas).
- Vault con dos copias que se deben mantener iguales: `notas-nexus-unificado/Universidad/` (despliega) y `OneSyncFiles/Universidad/` (trabajo).
- Flujo: `npm run sync` (`$env:VAULT_DIR="..\Universidad"`) → `npm run build` → `git add <rutas exactas>` → commit → push → esperar deploy → verificar en producción.

## Archivos que reservo (no editar sin avisar)

| Ruta | Qué hago |
|---|---|
| `site/src/styles/nexus.css`, `site/src/styles/content.css` | Paleta de marca |
| `site/src/components/SearchModal.astro` | Buscador (estilos y resaltado) |
| `site/src/pages/index.astro`, `site/src/layouts/Base.astro` | Portada y metadatos |
| `site/public/logo.svg`, `favicon.svg`, `og-neonotes.png`, `icon-*.png`, `apple-touch-icon.png` | Marca |
| `Universidad/_no-publicar.txt` (repo y OneDrive) | Qué se publica |
| `2do Semestre/Comunicación/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` | Exclusiones |
| `3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` | Exclusiones (tú dentro de 3er Semestre) |
| `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Recursos Unidad 0.md` | Exclusiones (tú dentro de 3er Semestre) |

## Commits de esta sesión

| Commit | Alcance |
|---|---|
| `4a3e443` | Site: logo propio, portada OG y favicon |
| `ba9ad13` | Site: paleta violeta→azul + fix de estilos del buscador |
| `88b3fac` | Vault: excluye Escucha Activa, UML Stevens y material Cambridge |
| `486f927` | Vault: excluye video de dinámicas y capturas Cambridge |
| `7eeef28` | Site: redirect 308 del dominio duplicado al canonical + sección de dominios en RUNBOOK |

**Efecto:** ZIP Comunicación 32,4→18,8 MB, Inglés III 10,3→1,4 MB, Diseño 10,6→7,3 MB; assets publicados 791→691 MB.

## Pendientes (requieren decisión)

1. **6 notas sin `dg-publish`** (no se publican):
   - `1er Semestre/Física Mecánica/Unidad 0 - Guias y Ejercicios/Guías y Ejercicios (Prof. Zambrano).md`
   - `3er Semestre/Fundamentos de Electricidad y Sistemas Digitales/Practico/Practicas del Laboratorio/Práctica 3 FESD/Práctica 3 — Diodos y Transistores.md`
   - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md`
   - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Capturas Empower U10-U12/Libro de ingles ultimas unidades.md`
   - `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Capturas Empower U7-U10/Libro de ingles las primeras unidades.md`
   - `3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/Talleres/Tarea 2.md`
2. **Dominio duplicado — falta un paso en el panel (no se puede hacer desde el repo).** `neonotes.vercel.app` lo responde un proyecto de Vercel aparte (la página "About" por defecto), no este sitio. Ya agregué el redirect 308 por host en `site/vercel.json` (se activa solo si el dominio pasa a apuntar a este proyecto) y los pasos en `site/RUNBOOK.md` sección 8:
   - Panel → proyecto `neonotes` (el que muestra "About") → Settings → Domains: redirigir a `https://neonotes-espol.vercel.app` o borrarlo.
   - O borrarlo y en `neonotes-espol` → Settings → Domains → Add Domain → `neonotes.vercel.app`.
   - Verificar: `curl -I https://neonotes.vercel.app/3er-semestre/` → 308 con `Location` al canonical.
   - Nota: el CLI de Vercel de esta máquina no tiene token válido (`vercel whoami` → "The specified token is not valid"), por eso no se puede hacer por terminal.
3. `favicon.ico` da 404 (solo hay `.svg`).
4. **Sandbox desactualizado:** `notas-nexus` (`C:\Users\STEVEN~1\Desktop\Proyectos`) sirve la versión verde del sitio y su `PLAN-PUBLICACION.md` dice "baseline 798".
5. **Divergencia de vault:** la copia de OneDrive de `3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` es una versión anterior (la del repo es la vigente).
6. **Colisión con la otra sesión `opencode`:** las dos creamos `Universidad/_no-publicar.txt` (la mía en `master` con 15 entradas; la de la otra en `backup-pre-fix-links` con 13). Al integrar, **unir las listas** y re-sincronizar.


## Verificaci\u00f3n de la rama OneDrive (2026-10-27 11:41)

Compil\u00e9 su rama onedrive/master (2409dfd) en un **worktree aislado** (wt-onedrive, ya eliminado) con VAULT_DIR apuntando a su vault de OneDrive:

- **Build OK**: 831 p\u00e1ginas, exit 0 (m\u00edas que mis 828: publicaron 3 notas m\u00e1s).
- **Exclusiones OK**: ninguno de los archivos con copyright/cambridge/video aparece en public/assets.
- **Marca intacta**: logo.svg, avicon.svg, og-neonotes.png e icon-192.png presentes en su build.
- **Falta mi redirect**: su site/vercel.json no tiene el bloque edirects (mi commit 7eeef28); hay que re-aplicarlo al integrar.

Diferencias de notas que quedan por unificar:

- 3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md: en su clon tiene dg-publish: true (y describe las carpetas en texto, sin embeds de Cambridge) \u2192 tras el merge **se publica**; en el m\u00edo no ten\u00eda flag.
- 3er Semestre/Sistema de Bases de Datos/.../Talleres/Tarea 2.md: no existe en su clon (lo borraron); en el m\u00edo sigue con dg-publish: false.
- 1er Semester/F\u00edsica Mec\u00e1nica/.../Gu\u00edas y Ejercicios (Prof. Zambrano).md: dg-publish: true en ambos clones, pero su sync lo cuenta como omitida. Conteos: m\u00edo 802/6, ellos 805/3 \u2014 falta que definan la lista final.

A\u00f1ad\u00ed el remoto onedrive (solo lectura) al clon Desktop para inspeccionar su rama sin tocar su working copy.
## No toco sin avisar

- Cambios de color/estilos del sitio (`nexus.css`, `content.css`, `SearchModal.astro`, `index.astro`, `Base.astro`).
- Archivos de marca en `site/public/` (logo, favicon, OG, iconos).
- `_no-publicar.txt` y las 3 notas reservadas de la tabla de arriba.
- Los ~17 `.md` con CRLF del vault: aparecen modificados en `git status` pero no son cambios míos.
- El trabajo de la otra sesión en `Universidad/3er Semestre/**` (links) y `Universidad/Herramientas/Mantenimiento/**`.

## Notas técnicas para quien siga

- `git diff --name-only` escapa los paths: usar `-c core.quotePath=false`.
- `git add -A` está prohibido: stagear rutas exactas (los `.md` con CRLF se cuelan).
- `node -e` con el signo dollar + llave se rompe en PowerShell: escribir scripts `.mjs`.
- Servidor estático para probar `dist`: `node static-server.mjs <raiz> <puerto>` (ojo: el 8099 lo tenía un servidor viejo apuntando al sandbox).
- Los nombres de archivo con á/é en la ruta rompen `Start-Process -ArgumentList`; usar `C:\Users\STEVEN~1\...`.
- El `<style>` de un componente Astro es *scoped*: lo que el JS inyecta en el DOM no lo toma, hay que moverlo a `is:global`.

## 2026-10-27 (tarde) — Merge con la sesión OneDrive + aviso de material no publicado

- **Merge limpio:** la sesión OneDrive pusheó `8fedc9f`/`b5c5669`; hice `git merge origin/master` y quedó **sin conflictos** (historial lineal, sus commits ya quedaban como ancestros).
  - Antes del merge: `git checkout -- Universidad` para descartar los 17 `.md` que aparecían modificados **solo por CRLF** (verificado con `git diff --ignore-cr-at-eol` vacío). Es el mismo ruido que bloqueaba los merges de la otra sesión.
  - Commit propio integrado: `66c9eca` (favicon.ico + plugin del aviso). `origin/master` = `f69ed87`.
- **Build integrado:** 831 páginas (antes 828), exit 0, 0 material excluido filtrado, marca y redirect intactos.
- **Nuevo: `site/src/lib/rehype-asset-omitido.mjs`** (registrado en `site/astro.config.mjs:35`).
  - El sync deja marcadores `<!-- nx:asset-omitido NOMBRE -->` / `<!-- nx:link-omitido NOMBRE -->` cuando un asset no se publica; hasta ahora **desaparecían en silencio** y el lector pensaba que la nota estaba incompleta.
  - El plugin los convierte en un aviso visible (borde dorado punteado, título en mayúsculas) + estilos en `site/src/styles/content.css`.
  - Detalle técnico: el marcador llega como nodo hast **`raw`** cuando está inline dentro de una lista/cita (`> - <!-- ... -->`), no como `comment`; el plugin cubre los dos casos.
- **Producción verificada:** el aviso se ve en las 2 notas con material no publicado (Inglés II C1-C2 e Inglés III Unidad 0); los diagramas de Cálculo que antes salían como omitidos **ahora cargan** (el refactor de `Diagramas/` de la otra sesión los arregló), así que los avisos bajaron de 6 a 2. 0 errores de consola.
- **`favicon.ico` real:** `site/public/favicon.ico` (16/32/48 px) + `<link rel="icon" type="image/x-icon" sizes="32x32">` en `Base.astro`. En producción responde **200** `image/vnd.microsoft.icon` (antes solo existía `favicon.svg`).
- **Verificado que NO se rompió nada:** redirect 308 del dominio (`site/vercel.json`), sección 8 del RUNBOOK, `og:image`, logo, exclusiones (Cambridge/Escucha Activa/UML/Empower/wmv → 0 archivos filtrados).
- **Pendiente (no bloquea):** el sandbox `C:\Users\STEVEN~1\Desktop\Proyectos\notas-nexus\` sigue con la versión verde y su `PLAN-PUBLICACION.md` dice "baseline 798"; y el dominio `neonotes.vercel.app` necesita el paso manual del panel de Vercel (CLI sin token válido, `gh` no instalado).

---

## 2026-10-27 (noche) — Acuerdo entre sesiones: commits, push y migración a OneDrive

- **Inventario verificado** (no supuesto) del estado de las 4 sesiones contra los clones:
  - `opencode-site` (yo): nada pendiente. `master` = `origin/master` = `6ffea83`, árbol limpio.
  - `opencode-onedrive`: **3 commits sin pushear** en su clon de OneDrive (`c4a84b5`, `4fd4960`, `ba68d18`) → tocan `Universidad/3er Semestre/Ingles III/**`, el LEEME y su log.
  - `opencode` (links): **nada pendiente**; sus 5 commits (`955c52f`, `ef329c8`, `7fa326a`, `5c75f95`, `86aa483`) ya están dentro de `origin/master` (verificado con `git merge-base --is-ancestor`).
  - `opencode-nube`: sin commits, pero 2 archivos sin commitear en `Clippings/` (`LOG-opencode-nube.md`, `PISTA - migracion vault a OneDrive institucional.md`) + `Recursos adicionales/Speaking Practice.md` (archivo vacío de 0 KB en la raíz de OneDrive).
- **Acuerdo escrito en el LEEME** (bloque "🤝 ACUERDO entre sesiones"): inventario de pendientes, flujo único de push con candado ("un push a la vez, siempre anunciado"), una sola copia editable por ruta (Desktop = `site/**`, OneDrive = `Universidad/**`) y el veredicto sobre la migración.
- **Veredicto sobre la migración (respuesta a la pista de `opencode-nube`):** **no es necesaria** y no es la solución de la cuota. De los 4,99 GB de la raíz de OneDrive, solo **1,11 GB** son contenido real (`Universidad/`); `site/` (1,83 GB) y `.git/` (1,50 GB) son regenerable/espejado. Limpiando ambos, la cuenta personal baja a **~1,2 GB** sin cambiar de cuenta. La migración institucional queda **opcional** (solo si el vault crece o si se quiere la misma cuenta en el teléfono) y, si se hace, el procedimiento correcto es **clon fresco**, no mover la carpeta (Files On-Demand + git = `.git` corrupto).
- **Mediciones nuevas de esta sesión** (root de `OneSyncFiles`): `Universidad/` 1.110,5 MB · `site/` 1.829,4 MB · `.git/` 1.501,2 MB (pack 566,6 MB) · `.obsidian/` 166,6 MB · `Contenido Extra/` 1,7 MB · `Recursos adicionales/` 0 MB · `.git/gc.pid` **roto** (`18272 Steven`, `git gc` se niega a correr hasta borrarlo).
- **Dato de la ruta Desktop:** el `.git` del clon canónico pesa 610 MB (fuera de OneDrive) → el de OneDrive es redundante para el mirror de GitHub.
- **No hice** (por decisión propia y por zona reservada): no pushear los commits de otra sesión, no borrar `site/` ni `.git/` de OneDrive, no tocar las 13 rutas hardcodeadas de `Herramientas/**`, no mover carpetas.
- **Firmado en el LEEME:** zona que toco = `site/src/**`, `site/public/` (marca), `site/RUNBOOK.md` §2 y §8, `Universidad/_no-publicar.txt` + las 3 notas de exclusiones ya publicadas, y el LEEME + este log. Commits sin pushear: ninguno.

---
**Tags:** #clippings #log #opencode-site
