---
dg-publish: false
tags: [clippings, log, opencode-nube, onedrive, infraestructura]
---

# LOG - opencode-nube (sesiones 27-29/10/2026, condensado)

> [!info] 📌 Alcance de esta sesión
> Sesión de **infraestructura / nube**. Solo escribe en `Clippings/**`, salvo la tarea de
> **normalización de formato** que `opencode` me asignó el 29/10 (ahí sí toqué `Universidad/**`).
> **Las tandas cerradas viven en el historial de git** (`git log -- "Clippings/LOG-opencode-nube.md"`)
> y en el tablero `ESTADO - las 4 sesiones.md`; acá queda solo lo vivo y lo que no se debe repetir.

> [!info] 📑 Índice
>
> - [[#Vivo - lo que sigue abierto]]
> - [[#Reglas y hallazgos que no se repiten]]
> - [[#Historial cerrado (condensado)]]

## Vivo - lo que sigue abierto

> [!warning] ⏳ Pendientes míos
> - **Carril D1 (mío):** vigilar las **5 carpetas `Unidad 0 - Guías y Ejercicios`** de 3er Sem. y
>   dejar **una pista por lote** (checksum, duplicados, unidad, copyright → se ignora al publicar,
>   publicable sí/no). Tracker: `INTAKE - material nuevo 3er Sem.md` (línea base de 367 archivos).
>   Falta el **script de detección automática** (pedido al carril A) y el **primer lote** que llegue.
> - **Avisos**: publicar el `PUSHEADO f430057` (Pasada 2) en mis zonas del LEEME/tablero.
> - **Deuda del usuario (no la resuelve ningún agente)**: borrar los despliegues viejos de
>   **Vercel** (~70 GB), decidir si `.obsidian/` (162 MB) sale de la nube ("Dejar de sincronizar")
>   y mover `OneSyncFiles-backups/notas-20261024` (458 MB) a disco local.

## Reglas y hallazgos que no se repiten

> [!note] 🧠 Operativa dura ganada (no volver a aprenderla)
> - **OneDrive revierte en segundos los archivos sin commitear**: los 15/16 escritos de la
>   Pasada 2 volvieron a su estado anterior antes del `git add`. → **escritura atómica**
>   (escribir + `git add` + commit en el mismo ciclo, archivo por archivo).
> - **`*.md text eol=lf` (clean filter)**: `git status` **no marca** CRLF en el working tree, pero
>   el sitio (`site/scripts/sync-vault.mjs`) **sí lee del disco** → avisado a `opencode-site`.
> - **Nunca compilar dentro de OneDrive**: `node_modules` se corrompe y `site/public/assets`
>   (650 MB) se rehidrata solo con cada build.
> - **Mecanismos de OneDrive medidos**: *"Dejar de sincronizar"* y *"mover fuera"* sacan de la
>   nube; *"Liberar espacio"* y *"Seleccionar carpetas"* solo sacan la copia de la PC.
> - **Con el árbol ajeno en vuelo**: commit **pathspec-explícito** o **worktree limpio con
>   cherry-pick**; nunca merge con árbol sucio; nunca capturar el staging de otra sesión.
> - **Un carril = un dueño = una zona = un commit**; un solo push a la vez, anunciado.

## Historial cerrado (condensado)

> [!success] 📜 Tandas cerradas (el detalle está en el historial de git)
>
> | Fecha | Tanda | Cierre |
> |---|---|---|
> | 27/10 | Sesión inicial: diagnóstico de cuota y migración | veredicto: migración NO necesaria; luego el usuario la pidió y a las 18:20 la canceló |
> | 27/10 18:20 | Migración probada y cancelada | copia institucional verificada (4.687 archivos, 0 errores) y **eliminada**; institucional queda vacía; vault personal intacto |
> | 27/10-28/10 | Limpieza de la nube | `site/public/assets` (650 MB) y el `.git/` huérfano de la raíz (23 MB, con respaldo) borrados; 4 mecanismos de OneDrive medidos |
> | 28/10 01:20 | Plan de carriles | §0 en `ESTADO - las 4 sesiones.md` (la cola real que todos leen) |
> | 28/10 02:30 | Correcciones del usuario | copyright: NO P2; links rotos → carril C; dominio real `neonotes-espol.vercel.app`; 4 sesiones, no 3 |
> | 28/10 03:00 | Links de contenido recomendado | 5 páginas `Recursos visuales.md` + look unificado en los 6 LEEME de 3er Sem. (`509769a`) |
> | 29/10 | Normalización Pasada 1 | `a2be225`: 111 notas CRLF→LF, dif solo fin de línea, 111/111 byte a byte, `qa_links` sin regresiones |
> | 29/10 | Normalización Pasada 2 | `f430057`: 15 notas sin líneas vacías en frontmatter (25 líneas); residual CRCA ya limpio en remoto. **Pasada 3 = sin objeto** (0 líneas, 5 definiciones medidas) |
> | 30/10 | Poda de `Clippings/` | LOG y mis 2 PISTAs condensadas; regla de poda escrita en el LEEME |
>
> **Aprendizaje que salió de la Pasada 2**: la medida "33 archivos de frontmatter" era falsa
> (18 eran finales `\r\r\n` que parten el renglón); y el `autostash` de un `git pull` ajeno se
> lleva trabajo sin commitear → de ahí la escritura atómica.

---

**Tags:** #clippings #log #opencode-nube #onedrive
