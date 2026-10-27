---
dg-publish: false
tags: [clippings, estado, sesiones, plan, tablero]
---

# ESTADO - las 4 sesiones (27/10/2026)

> [!info] 📌 Qué es este archivo
> Es el **tablero vivo** del vault. Cada sesión mantiene **su propio bloque**
> (Resultados / Qué falta / Próximos pasos) y **no toca el de los demás**.
> Al cerrar una tanda: actualizá tu bloque → stageá rutas exactas → **anunciá el
> push** en el LEEME ("Avisos de otros agentes") → pusheá.
> Los **números globales** de abajo los actualiza quien haga el push.

> [!important] Estado global verificado (27/10/2026, 15:45)
> - `master` = `origin/master` = **`bb1bc19`**, working tree **limpio**, 0 conflictos, 0 ramas pendientes de integrar.
> - Sitio: **806 notas publicadas · 3 omitidas · 2783 assets referenciados · 17 patrones / 61 archivos excluidos**.
> - Build de control: **832 páginas Astro (833 `.html`)**, 0 errores. Se compila en un **worktree en disco local** (`wt-build`), nunca dentro de OneDrive (ver R1 de `opencode-nube`).
> - Cuota OneDrive: **2,39 GB de 5 GB** en la raíz local. En la **nube** sigue pendiente vaciar la papelera (~1,8 GB) → depende del usuario.
> - Reglas vigentes: LEEME → *"🤝 PROTOCOLO DE COMMITS Y PUSHES"* + *"🤝 ACUERDO entre sesiones"* (Acuerdos 1–4, firmados por las 4 sesiones).

---

## 1) `opencode` — 3er Semestre (wikilinks y embeds)

Bitácora: `LOG-opencode.md` · Clon: OneDrive

### Resultados
- **3er Semestre: 0 wikilinks rotos**, **0 errores de formato** en sus 173 notas, **0 PDFs huérfanos**.
- Vault completo: **1075 → 1039 BAD** (ningún semestre subió).
- `qa_links.py` corregido (`partir_alias`: `#` en nombres de archivo, `\|` en tablas).
- 438 SVG movidos a `Diagramas/` de cada materia; 861 wikilinks rotos convertidos en texto plano; 14 tablas → callouts; 74 decks renderizados a PNG y embebidos.
- **Speaking Exam 2** (Inglés III) agregado: nota + PDF de 7 páginas exportado con PowerPoint COM + 2 SVG mermaid.
- Commits: `955c52f`, `ef329c8`, `7fa326a`, `5c75f95`, `86aa483`, `99d8c22`, `c11e2b9`, `4fd4960`, `ba68d18`, `c4a84b5`.

### Qué falta
| # | Qué | Prioridad | Decide |
|---|---|---|---|
| 1 | Los **1039 BAD** de 1er/2do/Preuniversitario: son links a material que nunca existió (informes, PDFs de cátedra). ¿Se borran, se reconstruyen o se dejan? | **alta** | **usuario** |
| 2 | Embebir los PNG ya renderizados (Git, componentes, normalización) en `DSW/Unidad 2 y 5/Archivos/` | media | sesión |
| 3 | Renderizar los decks que faltan: DSW U3/U4/U5-01 y BD | baja | sesión |
| 4 | Normalizar ~970 errores de formato del 1er/2do/Preuniversitario (`ENDINGS mixed`, líneas vacías dentro de fences en callout) | baja | sesión |
| 5 | Revisar los **32 PNG huérfanos** de `Universidad/Figuras/` (material en curso de Matemáticas Discretas) | baja | sesión (P7) |

### Próximos pasos
1. Esperar la decisión del usuario sobre los 1039 BAD (no tocar antes: son links a material que no existe).
2. Embebir los PNG ya renderizados (2) y dejar los decks pendientes en cola.
3. Cuando `opencode-onedrive` mueva los scripts de auditoría a `Herramientas/Mantenimiento/`, sumar ahí un chequeo de PDFs huérfanos.

---

## 2) `opencode-site` — sitio, marca y exclusiones

Bitácora: `LOG-opencode-site.md` · Clon: Desktop (`notas-nexus-unificado`)

### Resultados
- **Marca**: logo propio, portada OG, `favicon.ico` real (16/32/48 px) + `link image/x-icon`, iconos de app.
- **Paleta violeta → azul** + fix de estilos del buscador (`SearchModal.astro`).
- **Redirect 308** del dominio duplicado (`neonotes.vercel.app` → `neonotes-espol.vercel.app`) por host, con los pasos de panel documentados en `site/RUNBOOK.md` §8.
- **Plugin rehype** `site/src/lib/rehype-asset-omitido.mjs`: el sitio **avisa en pantalla** qué material no se publica y por qué.
- **Exclusiones**: 17 patrones / 61 archivos fuera de publicación (Cambridge, video, libros `z-lib.org`, UML Stevens, Escucha Activa `_OCR`).
- Efecto medido: ZIP Comunicación **32,4 → 18,8 MB**, Inglés III **10,3 → 1,4 MB**, DSW **10,6 → 7,3 MB**; assets publicados **791 → 691 MB**.
- **Coordinación**: escribió el protocolo de pushes (`edd511b`) y los Acuerdos 1–4, y avisó antes de tocar rutas ajenas.
- Commits: `4a3e443`, `ba9ad13`, `88b3fac`, `486f927`, `7eeef28`, `66c9eca`, `edd511b`, `332d22a`, `0d7c562`.

### Qué falta
| # | Qué | Prioridad | Decide |
|---|---|---|---|
| 1 | **Paso manual en el panel de Vercel** para liberar `neonotes.vercel.app` (hoy lo responde otro proyecto). El CLI no tiene token válido | media | **usuario** (guía en `site/RUNBOOK.md` §8) |
| 2 | Verificar en producción, ya desplegado: favicon, redirect y el aviso "material no publicado" | media | sesión |
| 3 | Refrescar el **espejo** `Desktop\Proyectos\notas-nexus` (sirve la versión verde; es espejo, **sin commits**) | baja | sesión |
| 4 | `git pull` en el clon Desktop para traer el último merge (`bb1bc19`) | baja | sesión |

### Próximos pasos
1. Avisar al usuario el paso del panel (o pedirle que lo ejecute) y dejar la verificación documentada.
2. `git pull` del clon Desktop y verificar que marca + redirect + exclusiones siguen íntegros.
3. Cuando el usuario confirme la cuenta institucional, revisar si el `favicon`/`og` necesitan versión institucional.

---

## 3) `opencode-nube` — cuota, nube y migración

Bitácora: `LOG-opencode-nube.md` · Pista: `PISTA - migracion vault a OneDrive institucional.md` (**#procesado**) · Clon: OneDrive

### Resultados
- **Medición real de la cuota**: raíz de OneDrive **4,99 GB de 5 GB** → `Universidad/` 1,11 GB (contenido real), `site/` 1,83 GB (regenerable), `.git/` 1,50 GB (espejado en GitHub), `.obsidian/` 167 MB.
- **Veredicto**: **la migración al OneDrive institucional NO es necesaria**; la cuota se resuelve limpiando lo generado y compactando `.git`. Pista cerrada en `#procesado`.
- **Evidencia reproducida 3 veces** de que `node_modules` **no puede vivir en OneDrive**: (1) el build falla con `Cannot find module .../astro/...`; (2) `npm ci` falla con `ENOTEMPTY` porque OneDrive y npm pelean por el mismo directorio; (3) build de control **fuera** de OneDrive → OK (806 notas → 833 `.html`, exit 0).
- Aclaración importante: **AutoSync y OneSync son apps del teléfono**, no clientes de escritorio; el PC usa el cliente oficial de OneDrive.
- **Plan cerrado** por si algún día se migra: `git clone` a la ruta nueva (nunca mover la carpeta), `VAULT_ROOT` en las rutas hardcodeadas, **sin AutoSync** para `.git/`, `node_modules/`, `dist/`, `.obsidian/`, y el clon Desktop sigue desplegando.

### Qué falta
| # | Qué | Prioridad | Decide |
|---|---|---|---|
| 1 | **Vaciar la papelera de OneDrive** → libera ~1,8 GB en la nube (lo borrado de `site/` sigue contado como eliminado) | **alta** | **usuario** (1 clic) |
| 2 | **Mover** `OneSyncFiles-backups/notas-20261024` (458 MB, copia del 24/10) a disco local → libera 458 MB en la nube sin perder el respaldo | alta | **usuario** (ya ofrecida por `opencode-onedrive`) |
| 3 | **Fijar el vault** ("mantener siempre en este equipo") para que OneDrive no lo deshidrate | alta | **usuario** |
| 4 | Cuenta institucional: cuota real por usuario, límite por archivo (el `.wmv` pesa 58 MB), **retención** al terminar la carrera y si el material con copyright es aceptable ahí | media | **usuario / TI** |
| 5 | Teléfono: AutoSync → cuenta institucional, **solo `DCIM/Camera`**; el vault no se empareja; PC y teléfono a la misma cuenta | baja | **usuario** |
| 6 | Verificar que el `.git/gc.pid` roto quedó resuelto (`.git` bajó de 1,50 GB a **658 MB** tras `git gc`) | baja | sesión |

### Próximos pasos
1. Cerrar 1–3 con el usuario (los tres son reversible y no tocan contenido).
2. Con la respuesta a 4, dejar por escrito si la migración queda descartada o solo aplazada, y actualizar la PISTA.
3. Mantener la regla: **el vault guarda notas y assets; el código del sitio y sus dependencias se compilan en disco local**.

---

## 4) `opencode-onedrive` — reglas de publicación y Cálculo Vectorial

Bitácora: `LOG-opencode-onedrive.md` · Clon: OneDrive

### Resultados
- **Sistema de publicación** en `site/scripts/sync-vault.mjs`: gate `dg-publish`, `_no-publicar.txt` con comodines `*`/`?` (match por nombre **o** ruta), **solo se publica un asset si una nota publicada lo referencia**, fix de embeds `![[Nota]]` → `[[Nota]]`, y marcador `<!-- nx:asset-omitido -->`.
- **Cálculo Vectorial**: 16 diagramas placeholder sustituidos por los reales, 2 "Teorema Fundamental" corregidos, **37 diagramas maestros integrados en 32 notas** → **0 embeds de diagramas rotos** en todo el vault; 332 previews borrados (12,7 MB); lista maestra regenerada (474 → **0**).
- **Copyright**: cerrada la fuga de `Escucha Activa Parte 1/2_OCR.pdf` (se publicaban) y unificada la lista con la otra sesión (17 patrones / 61 archivos).
- **Diagnóstico del ruido CRLF**: 82 `.md` con CRLF en el blob commiteado hacían fallar **todos** los merges (`Your local changes would be overwritten`) → normalizados solo en fin de línea (`a05dfa4`).
- **Coordinación**: protocolo de pushes, Acuerdos 1–4, cola de push con dueño, corrección de la tabla de zonas (4 sesiones), reglas de *commitear antes de que otro mergee* y de *worktree por sesión*.
- Commits: `374e833`, `5aded86`, `67ed5ac`, `462191b`, `6a41cf9`, `d45c240`, `a05dfa4`, `7013acf`, `9fbc2e8`, `bb1bc19` + merges.

### Qué falta
| # | Qué | Prioridad | Decide |
|---|---|---|---|
| 1 | **P8**: arreglar `verificar_nota.py` en Cálculo Vectorial (líneas vacías dentro de fences en callouts). Es mi zona | media | sesión |
| 2 | **P4**: mover mis scripts de auditoría (`qa_resolucion_diagramas.py`, `qa_assets_huerfanos.py`, `qa_fugas_copyright.py`, `qa_svg_titulo.py`) a `Universidad/Herramientas/Mantenimiento/` con **una sola entrada** | media | sesión |
| 3 | **P3**: CI (GitHub Actions) que falle si algo de `_no-publicar.txt` llega a `public/` o a un ZIP | media | sesión + usuario (¿CI?) |
| 4 | **P6**: `VAULT_ROOT` en los 15+ archivos con ruta absoluta (8 en `SVG-Pipeline/`, 3 en `Herramientas/`, `sync-vault.mjs:19-20`, 3 `.md`) | media | sesión (antes de cualquier migración) |
| 5 | **P2**: lista negra (`_no-publicar.txt`) → **lista blanca** (`_publicar.txt`) o carpeta `Universidad/_privado/` | media | **usuario** |
| 6 | **P1**: un `git worktree` por sesión como forma estándar de trabajar | baja | sesiones |
| 7 | **P7**: 32 PNG huérfanos de `Universidad/Figuras/` (coordinado con la sesión del 3er Semestre) | baja | sesiones |

### Próximos pasos
1. P8 (mi zona, sin dependencias de nadie) → commit con rutas exactas.
2. P4: dejar los 4 scripts en `Herramientas/Mantenimiento/` + documentarlos en `Herramientas/README.md`.
3. P5 ya está hecho (limpieza de `site/`); queda solo **esperar el OK del usuario** para los 3 puntos de cuota de `opencode-nube` (vaciar papelera, mover backup, fijar carpeta).
4. P6 antes de cualquier migración; P3 y P2 esperando decisión del usuario.

---

## ✅ Decisiones que esperan al usuario

| # | Decisión | Impacto si no se decide | Detalle |
|---|---|---|---|
| 1 | **Vaciar la papelera de OneDrive** | la nube sigue "llena" (~1,8 GB de borrados) | bandeja del sistema → OneDrive → Papelera → Vaciar |
| 2 | **Mover el backup de 458 MB a disco local** | 458 MB de cuota cloud | `opencode-onedrive` lo hace con el OK |
| 3 | **Fijar el vault** ("mantener siempre en este equipo") | OneDrive puede deshidratar notas y PDFs otra vez | `attrib +P -U` |
| 4 | **Liberar `neonotes.vercel.app`** en el panel de Vercel | el dominio duplicado sigue sirviendo otra página | `site/RUNBOOK.md` §8 |
| 5 | **Los 1039 BAD**: borrar, reconstruir o dejar | 1er/2do/Preuniversitario quedan con links rotos | `LOG-opencode.md` |
| 6 | **P2**: lista blanca o carpeta `_privado/` | depende de que alguien recuerde la lista negra | `LOG-opencode-onedrive.md` |
| 7 | **Material con copyright** en la cuenta institucional | define si la migración es posible | PISTA |
| 8 | **Teléfono**: AutoSync con `DCIM/Camera` a la institucional | fotos siguen en el celular | PISTA |

---

## 🔒 Reglas de operación (resumen — el detalle está en el LEEME)

1. **Un push a la vez, siempre anunciado**: `PUSHEO EN CURSO · <rama> · <qué> · ~3 min` → `PUSHEADO <hash>`.
2. **Stagear rutas exactas**: nunca `git add -A` ni `git commit -a`.
3. **Ruido de CRLF**: si un `.md` aparece modificado y no lo tocaste, `git diff --ignore-cr-at-eol --stat` y `git checkout -- "<ruta>"`.
4. **Antes de pushear**: `git fetch origin` → comparar `origin/master..HEAD` con `HEAD..origin/master` → si hay commits ajenos, `git pull --no-rebase` y **re-verificar con build**.
5. **Prohibido**: `--force`, `amend` de algo publicado, `reset --hard` ajeno.
6. **Si vas a tocar la ruta de otra sesión**: avisá en "Avisos de otros agentes" y esperá confirmación.
7. **Zonas**: `site/src/**`+`site/public/**` → `opencode-site` · `Universidad/3er Semestre/**` → `opencode` · `2do Semestre/Cálculo Vectorial/**`+`site/scripts/sync-vault.mjs`+`site/RUNBOOK.md` → `opencode-onedrive` · `Clippings/` (su bitácora) → cada uno.

---
**Tags:** #clippings #estado #sesiones #plan #tablero
