---
dg-publish: false
tags: [clippings, log, opencode-onedrive, publicacion, calidad, vault]
---

# LOG - opencode-onedrive (sesión OneDrive, oct-2026)

> [!info] ℹ️ Alcance y cómo leer este LOG
> Sesión `opencode-onedrive`, clon **OneDrive** (`OneSyncFiles/`). Zona: `Universidad/2do Semestre/
> Cálculo Vectorial/**`, `site/scripts/sync-vault.mjs`, `site/RUNBOOK.md`, `site/docs/**`,
> `Universidad/Herramientas/**` (carril A), `Clippings/LOG-opencode-onedrive.md`.
> **Versión condensada (31/10/2026, regla de poda de `opencode-nube`)**: el detalle histórico
> completo está en git (`git log -- Clippings/LOG-opencode-onedrive.md`) y en el LEEME.

## 1. Lo hecho, con hash

| Tema | Qué | Hash |
|---|---|---|
| **Sistema de publicación** | Gate `dg-publish` + `_no-publicar.txt` con comodines `*`/`?` (match por nombre o ruta), solo se publica un asset si una nota publicada lo referencia, fix de embeds `![[Nota]]`→`[[Nota]]`, marcador `<!-- nx:asset-omitido -->` | `374e833`, `5aded86`, … |
| **P3 — CI de privacidad** | `verificarNoPublicados()` en el sync + `ci-check-privado.mjs` + `.github/workflows/ci-privacy.yml` (falla si algo de `_no-publicar.txt` se publica) | `1233551` |
| **P4 — Scripts QA** | 4 auditores + `qa_all.py` + `qa_omitidas.py` (31/10) en `Herramientas/Mantenimiento/`, documentados en `README.md` | `847a33a` |
| **P6 — `VAULT_ROOT`** | Rutas parametrizadas (env var + fallback desde `__file__`) en 7 scripts; 0 rutas hardcodeadas | `21cbe0c` |
| **P8 — Fences en CV** | 88 líneas vacías reales → `"> "`; 5 fences sobrantes eliminados; 91 notas, 0 errores | `2b2dda7`, `68960b5` |
| **Taxonomía Unidad 0 en CV** | `U0/` con 8 subcarpetas + `00 - Leeme Unidad 0.md`; 566 renombres R100 (563 SVG + 3 archivos de raíz); verificado sin regresiones | `b9de5b7` |
| **Fix EOL al leer** | `leerTexto()` en `sync-vault.mjs` (colapsa `\r\n`/`\r`): el sitio ya no filtra `\r` al HTML aunque OneDrive rehidrate CRLF | `4acb8d5`, `68cab8b` |
| **Arreglo anti-mezcla** | Worktree `sesion/opencode-onedrive` (fuera de OneDrive) + hook `pre-commit` de aviso + `FLUJO-WORKTREE-SESIONES.md` | `f05e643`, `71d32d0`, `8e9e707` |
| **Bug propio corregido** | `qa_assets_huerfanos.py`: `norm_name()` no quitaba la carpeta → 2617 falsos positivos; ahora 90 huérfanos reales (0 de mi zona) | este LOG |
| **Cierre de links del carril C** | Verificado tras la ronda masiva: **852 → 7 BADs**; copyright **0 fugas**; SVGs placeholder **0** | — (verificación) |

## 2. Propuestas P1–P8 — estado final

| # | Propuesta | Estado |
|---|---|---|
| P1 | Worktree por sesión | ✅ **EN EJECUCIÓN** (worktube + hook); falta OK del dueño del vault para la ruta permanente |
| P2 | Lista blanca vs lista negra | ✅ **CERRADO por decisión del usuario**: se mantiene la lista negra (`_no-publicar.txt`); sin lista blanca ni `_privado/` |
| P3 | CI que falle si se publica material excluido | ✅ IMPLEMENTADO (`1233551`) |
| P4 | Scripts de auditoría con entrada única | ✅ IMPLEMENTADO (`847a33a`) |
| P5 | Sacar `site/` del vault | ✅ Resuelto por limpieza (1,8 GB de derivados); deploy no depende del clon local |
| P6 | Parametrizar rutas absolutas | ✅ IMPLEMENTADO (`21cbe0c`) |
| P7 | 32 PNG huérfanos de `Universidad/Figuras/` | ✅ CERRADO por `opencode` (56 láminas embebidas, `Figuras/` global vacío) |
| P8 | `verificar_nota.py` en CV | ✅ IMPLEMENTADO (`2b2dda7`, `68960b5`) |

## 3. Incidentes del clon compartido (resumen)

> [!warning] ⚠️ 3 commits mezclados por el índice compartido — sin pérdidas
> `b9de5b7` (capturó mis 566 renombres de CV), `394a087` (capturó 41 archivos de la ola 4 de
> `opencode`), `68cab8b` (capturó mi cambio de `sync-vault.mjs`). En los 3: contenido byte-idéntico,
> 0 pérdidas, autoría documentada. Post-mortem + plan de arreglo firmable:
> `Clippings/PROBLEMA - commits mezclados por el indice compartido.md`.

## 4. Estado al cierre (31/10/2026)

> [!success] ✅ Verificado
>
> - `origin/master` = `master` = `8e9e707`; trabajo desde el worktree `sesion/opencode-onedrive`.
> - `qa_links.py`: **7 BADs** (852 al abrir el carril C) · `qa_fugas_copyright.py`: **0 fugas** ·
> `qa_svg_titulo.py`: **0 placeholders** · `qa_omitidas.py`: **821/824 publican** (2 omitidas
> deliberadas + 1 a revisar: el Mapa PAO, zona ajena) · huérfanos reales: **90 (0 de mi zona;
> 70 de 3er Semestre, reportados a `opencode`)**.
> - Regla P8 en mis 92 notas de CV: 0 líneas vacías en fences, 0 fences sin cierre.

## 5. Pendientes míos

> [!question] ❓ Lo que queda de mi lado
>
> 1. **P1**: cuando el dueño del vault autorice, proponer la ruta permanente del worktree
>    (fuera de OneDrive) para que monten la suya las otras 3 sesiones.
> 2. **Rebuild del sitio** (`opencode-site`): ejercita mi fix de EOL al leer; verificar 0 broken assets.
> 3. Mantener el flujo del §`FLUJO-WORKTREE-SESIONES.md` (reglas B/C) en cada commit.

---
**Tags:** #clippings #log #opencode-onedrive #publicacion #calidad #vault
