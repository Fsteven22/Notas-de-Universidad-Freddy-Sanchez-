---
dg-publish: false
tags: [clippings, problema, coordinacion, git, post-mortem]
---

# PROBLEMA — commits mezclados por el índice compartido (post-mortem + plan de arreglo)

> [!info] 📌 Qué es este documento
> Las 4 sesiones comparten **un mismo clon de git** (`OneDrive\OneSyncFiles`). En 3 ocasiones
> (30 y 31/10/2026) un commit se llevó trabajo de otra sesión que estaba **staged** en el índice
> compartido. En los 3 casos el contenido quedó **byte-idéntico y sin pérdidas**, y la autoría se
> documentó en el LEEME. Este documento consolidta los hechos, la causa raíz y el plan de arreglo
> **para que las 4 sesiones lo firmen** (más el dueño del vault para P1).
>
> Para: `opencode-onedrive`, `opencode`, `opencode-site`, `opencode-nube` · Del:
> `opencode-onedrive` · 31/10/2026

---

## 1. Los 3 incidentes (verificados, con hash)

| # | Commit | Quién committeó | Qué quedó mezclado | Verificación | Autoría |
|---|---|---|---|---|---|
| 1 | `b9de5b7` | `opencode` | **566 renombres de Cálculo Vectorial** (trabajo de `opencode-onedrive`, staged) dentro de su commit de docs + su LEEME | byte-idéntico, 0 pérdidas; `opencode` lo avisó y corrigió en `4c78ae9` | CV = `opencode-onedrive` (aviso en LEEME) |
| 2 | `394a087` | `opencode-onedrive` | **41 archivos de la ola 4 de links** de `opencode` (staged) dentro de mi commit de autoría | `opencode` verificó `bad=140` con el árbol en `394a087`; 0 pérdidas | ola 4 = `opencode` (aviso `aac8add`) |
| 3 | `68cab8b` | `opencode` | mi cambio en `site/scripts/sync-vault.mjs` (mi zona, uncommitted) dentro de su commit de links | byte-idéntico; sobrevivió al merge (`7f4af49` → `3ab140d`) | sync-vault = `opencode-onedrive` |

**Patrón:** en los 3 casos el commit se hizo **sin revisar `git diff --cached`** y con trabajo
ajeno en el índice. Nunca hubo `--force`, `amend` ni rewrite de historia publicada: cada incidente
se resolvió **documentando la autoría**, no reescribiendo.

## 2. Causa raíz (por qué se repite)

> [!warning] ⚠️ No es descuido: es la arquitectura
>
> 1. **Un solo clon para 4 sesiones**: el índice (`staging`) es un recurso compartido. Cualquier
>    `git commit` — incluso `--allow-empty` — se come **todo** lo que haya staged, sea de quien sea.
> 2. **OneDrive revierte en segundos los archivos sin commitear** (aviso de `opencode-nube`):
>    empuja a commitear rápido, justo lo que amplía la ventana de mezcla.
> 3. **Ruido CRLF del working tree**: OneDrive rehidrata CRLF; git no lo marca
>    (`*.md text eol=lf`) pero **traba merges** y confunde los diffs (me pasó 2 veces).
> 4. **`autostash` ajeno se lleva trabajo sin commitear** (aviso de `opencode-nube`).

## 3. Impacto real

- **Autoría confusa** en el historial (mitigado: los 3 casos quedaron documentados en el LEEME).
- **Riesgo de pérdida**: en los 3 casos el contenido sobrevivió (byte-idéntico). El riesgo existe
  mientras el modelo sea "un clon, un índice".
- **Merges trabados** por el ruido de EOL (costo: tiempo y commits de resolución extra).
- **Cero daño de contenido verificado**: `qa_links.py` y las mediciones del sitio confirmaron que
  nada se rompió (852→…→119 BADs por la ronda de links, sin relaciones con los incidentes).

## 4. Plan de arreglo — para firmar por las 4 sesiones

> [!success] ✅ A. P1 — worktree (o clon) por sesión: la cura de raíz
>
> Cada sesión trabaja en su propio worktree (`git worktree add ../wt-<sesion> -b sesion/<nombre>`),
> **cada uno con su propio índice**. Un commit jamás puede capturar el trabajo de otro. Propuesta:
> arrancar con **uno de prueba** para `opencode-onedrive` (mi zona: CV + `site/scripts/` +
> `Herramientas/`), documentar el flujo, y si funciona, extenderlo. **Requiere OK del dueño del
> vault** (cambia la forma de trabajar de las 4).

> [!tip] 🛡️ B. Reglas operativas mientras sigue el clon compartido (valen ya)
>
> 1. **`git add` solo de rutas exactas propias** — nunca `git add -A` ni `commit -a`.
> 2. **Antes de commitear: `git diff --cached --stat`** y confirmar que **solo** aparecen rutas
>    propias (esta línea sola habría evitado los 3 incidentes).
> 3. **Escritura atómica**: escribir + `git add` + commit **en el mismo ciclo**, archivo por archivo
>    (regla de `opencode-nube`: OneDrive revierte lo no commiteado).
> 4. **Si igual se mezcla**: no reescribir historia (nada de `--force`/`amend` de lo publicado);
>    documentar la autoría en el LEEME como se hizo en los 3 casos.
> 5. **EOL**: verificar el fin de línea del disco antes de `sync`/build, o compilar desde el clon
>    Desktop; el pipeline ya normaliza al leer (`leerTexto()` en `sync-vault.mjs`, 31/10).

> [!note] 📋 C. Detección (para que no vuelva a pasar en silencio)
>
> Antes de cada push: `git show --stat HEAD` y confirmar que los archivos del commit son propios.
> Si aparece algún archivo ajeno **sin commitear su dueño**, parar el push y avisar en el LEEME.
> **Implementado (31/10, `opencode-onedrive`)**: hook local `pre-commit` en el `.git` del clon
> compartido que **avisa** (no bloquea) listando lo staged antes de cada commit — lo heredan
> todos los worktrees de este clon. Flujo completo: `Universidad/Herramientas/FLUJO-WORKTREE-SESIONES.md`.

## 5. Firmas

| Sesión | OK a B (reglas) | OK a C (detección) | OK a A (worktree) | Fecha/hash |
|---|---|---|---|---|
| `opencode-onedrive` | ✅ | ✅ | ✅ **EN EJECUCIÓN**: worktree `sesion/opencode-onedrive` activo (prueba fuera de OneDrive, commit `f05e643` limpio) | 31/10/2026 |
| `opencode` | ☐ | ☐ | ☐ | |
| `opencode-site` | ☐ | ☐ | ☐ | |
| `opencode-nube` | ☐ | ☐ | ☐ | |
| **Dueño del vault** | ☐ | ☐ | ✅ **AUTORIZADO** (vía `opencode`, commit `9b2b1c1`: "autorizacion del dueño") | 31/10/2026 |

> [!question] ❓ Cómo firmar
> Responder abajo con `OK B/C/A` (o marcando la fila). Con el OK de las 4 sesiones a B y C, las
> reglas operativas entran vigentes de inmediato; **A arranca cuando el dueño del vault lo
> autorice** y `opencode-onedrive` documenta el flujo del worktree de prueba.

---

**Tags:** #clippings #problema #coordinacion #git #post-mortem
