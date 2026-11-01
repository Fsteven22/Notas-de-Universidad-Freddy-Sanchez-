---
dg-publish: false
tags: [clippings, protocolo, colaboracion, estado]
---

# LEEME — bandeja única (protocolo, estado y acuerdos)

> [!important] Única fuente de verdad — 01/11/2026
>
> Por decisión del dueño del vault, **este archivo es el único** de `Clippings/`. Se borraron los 15 restantes
> (PROPUESTAS ×2, REPORTE, CRUCE, PROBLEMA, PISTA ×3, LOG-* ×4, ESTADO, INTAKE ×2): su contenido vigente está
> volcado acá y **el historial completo sigue en git** (`git log -- Clippings/`).
>
> **Regla nueva:** nada de archivos auxiliares nuevos. Todo reporte, pedido o decisión se escribe **acá**, en un
> bloque con el nombre de la sesión y la fecha. Si algo se reporta en otro lado, se pierde.

---

## 🧭 CÓMO SE TRABAJA (resumen ejecutable)

> [!tip] Las 8 reglas que evitan todos los incidentes anteriores
>
> 1. **Worktree propio por sesión** (las 4 activas): `git worktree add ../wt-<sesion> -b sesion/<nombre> master`.
>    Tu commit ya no puede capturar trabajo de otra sesión: cada worktree tiene su propio índice.
> 2. **`git add` de rutas exactas propias**, nunca `-A` ni `commit -a`.
> 3. **Antes de commitear**: `git diff --cached --name-status` y confirmar que solo aparece lo tuyo (el hook
>    `pre-commit` del clon lo lista; si ves ruta ajena, `git restore --staged <ruta>`).
> 4. **Commit atómico**: escribir + `add` + commit en el mismo ciclo (OneDrive revierte en segundos lo no commiteado).
> 5. **Antes de pushear**: `git show --stat HEAD` (archivos y mensaje propios) y `git log origin/master..HEAD`.
> 6. **Nunca** `--force` sobre `master` ni historia compartida, nunca `amend` de lo publicado, nunca `reset --hard`
>    ajeno. Si algo quedó mal: commit nuevo que lo corrija y se documenta.
> 7. **Un push a la vez, anunciado**: bloque `PUSHEO EN CURSO` acá → push → bloque `PUSHEADO <hash>`.
> 8. **Integración**: cada sesión commitea en su rama; **una sola integra a `master`** con
>    `git merge --ff-only sesion/<nombre>` desde el worktree de OneDrive (el que lee Obsidian). CRLF: si un `.md`
>    aparece modificado y no lo tocaste, `git diff --ignore-cr-at-eol` vacío → `git checkout -- "<ruta>"`.

---

## 🗺️ ZONAS (quién toca qué)

| Sesión | Worktree | Zona propia | No toca sin avisar |
|---|---|---|---|
| `opencode` (3er Semestre) | `Documents/wt-opencode` | `Universidad/3er Semestre/**`, `Universidad/Herramientas/Mantenimiento/**` | `site/**`, `Universidad/2do Semestre/Cálculo Vectorial/**`, `_no-publicar.txt` |
| `opencode-onedrive` | ruta propia (hoy en TEMP) | `Universidad/2do Semestre/Cálculo Vectorial/**`, `site/scripts/sync-vault.mjs`, `site/RUNBOOK.md`, `Universidad/Herramientas/**` (scripts) | `site/src/**`, `site/public/**`, `Universidad/3er Semestre/**` |
| `opencode-site` | `Desktop/wt-opencode-site` | `site/src/**`, `site/public/**`, marca | `site/scripts/sync-vault.mjs`, `Universidad/**` |
| `opencode-nube` | `TEMP/opencode/wt-nube` | `Clippings/**` (solo este archivo) | todo lo demás |
| **Dueño del vault** | — | decisiones, material nuevo (carpetas `Unidad 0 - Guías y Ejercicios` de 3er Sem) | — |

---

## 📊 ESTADO VERIFICADO — 01/11/2026

> [!success] Lo que está HECHO (verificado, con hash en git)

| Tema | Estado | Desde |
|---|---|---|
| **Taxonomía `Unidad 0 - Guias y Ejercicios/`** | 8 subcarpetas + índice en las **17 materias** (16 + Cálculo Vectorial), raíces vacías | `opencode` + `opencode-onedrive` |
| **`Diagramas/` y `Figuras/` de raíz → `U0/`** | ~4.000 SVG/MMD + 122 figuras unificados; `Universidad/Diagramas/` y `Figuras/` globales eliminados; mapa PAO en `00 - Mapa PAO 2-2026.md` (raíz) enlazado desde `Index.md` | `opencode` |
| **Links rotos de `Universidad/**`** | **`qa_links.py` bad=0** (raíz `Universidad`): de 852 a 0 con redirección por contenido + eliminación de los sin destino equivalente (decisión del dueño) | `opencode` |
| **láminas/PNG** | 56 PNG huérfanos embebidos (DSW U2/U5, SBD U2) | `opencode` |
| **Inglés III** | 3 PPTX exportados a PDF | `opencode` |
| **`qa_links.py` / placeholders** | 7 BADs de documentación corregidos; `norm_name` sin `basename()` (2617 falsos positivos) arreglado | `opencode-onedrive` |
| **Sitio** | dominio real `neonotes-espol.vercel.app`, marca, aviso "material no publicado", 821/824 publican (2 omitidas deliberadas, 1 = mapa PAO, omisión decidida) | `opencode-site` |
| **Normalización** | Pasada 1 (111 notas CRLF→LF) y 2 (15 frontmatter) cerradas; pasada 3 sin objeto | `opencode-nube` |
| **Clon compartido** | **P1: las 4 sesiones firmaron A/B/C y trabajaran en worktree propio**; dueño autorizó A (vía `opencode`, 31/10). Un commit mezclado quedó como hecho puntual y documentado | las 4 |

> [!warning] Lo que FALTA (con dueño)

| # | Qué | Dueño | Estado |
|---|---|---|---|
| 1 | **90 assets huérfanos** (70 de `Universidad/3er Semestre/**`): embebido o descarte documentado, uno por uno | `opencode` | aceptado 01/11, en curso |
| 2 | **Rebuild del sitio** con el vault en `bad=0` + verificar 0 assets rotos en producción | `opencode-site` | pendiente de su turno |
| 3 | **Regenerar el SVG del mapa PAO** (el `.md` es la fuente; el SVG quedó desactualizado) | `opencode-site` (carril C) | pendiente |
| 4 | **50 links reales en `Contenido Extra/**`** (zona sin dueño): aplicar la misma regla de links | a asignar — `opencode` ofrecido | espera OK |
| 5 | **`qa_links.py` con raíz=repo completo marca 160**: 58 `[[#Encabezado]]` intra-doc (falsos positivos: el heading existe en el mismo archivo) + 49 placeholders de `Clippings/**` + 50 de `Contenido Extra/**` + 2 de `site/docs` | carril A: `opencode-onedrive` (excluir/clasificar) | pedido hecho |
| 6 | **Ruta permanente del worktree** de `opencode-onedrive` (hoy en `<TEMP>`: el sistema puede limpiarlo) | dueño del vault | propuesta: `Desktop/wt-onedrive` |
| 7 | **DSW U3 y U4 sin material** (0 PDF, 0 PNG): conseguir el material | dueño del vault | reportado |
| 8 | Firma formal del dueño en la fila A del post-mortem (la autorización ya está tomada vía `opencode`) | dueño del vault | opcional |

---

## ✅ DECISIONES DEL DUEÑO (vigentes)

1. **Links**: si existe contenido que hable del tema (cualquier semestre) → **redirigir**; si no existe → **eliminar** el link. No crear notas para rellenar links.
2. **Copyright**: se ignora al publicar. Manda la lista negra `Universidad/_no-publicar.txt`; **no** hay lista blanca ni carpeta `_privado/`.
3. **Mapa PAO**: la nota no se publica (`dg-publish` sin frontmatter a propósito); solo se publica el SVG vía la portada `Index.md`.
4. **Material nuevo** de 3er Sem.: se deja exactamente en las carpetas `Unidad 0 - Guías y Ejercicios` de cada materia.
5. **Un solo archivo de coordinación**: este LEEME. Los LOGs/PROPUESTAS/ESTADO/etc. fueron borrados; el historial vive en git.
6. **Nunca compilar dentro de OneDrive** (`node_modules` se corrompe y `site/public/assets` se rehidrata): build y sync en disco local.
7. **Migración a OneDrive institucional**: cancelada; no se reabre. Para leer en el móvil: el sitio publicado.
8. **Worktree por sesión (P1)**: aprobado.

---

## 🧯 LECCIONES DURAS (una línea cada una — sin narrativa)

- Clon compartido = índice compartido: un `commit` se come todo lo staged. Se cura con **worktree propio** (P1) + verificar `git diff --cached` antes de commitear.
- OneDrive revierte en segundos lo no commiteado → **escritura atómica**.
- `git pull --no-rebase`, nunca rebase de lo ya publicado; conflictos de este archivo se resuelven **conservando ambos bloques**.
- `_texto/**` (salidas de scripts) y `site/public/assets` **nunca** se commitean.
- El hook `pre-commit` (regla C) vive en el `.git` del clon: los worktrees del mismo clon lo heredan; desde otro clon hay que copiarlo.
- Medir el estado **desde el directorio correcto**: `qa_links.py` con raíz `Universidad` (bad=0) NO es lo mismo que con raíz del repo completo (160, casi todos placeholders de documentación).

---

## 📝 CÓMO REPORTAR (formato obligatorio)

> [!example] Bloque de reporte — copiar y completar
>
> ```markdown
> ### `<sesión>` — <tema> — <fecha>
>
> > [!success|warning|question] <titulo>
> >
> > - **Hecho:** <qué + hash>
> > - **Pendiente:** <qué + de quién>
> > - **Necesito:** <de otro agente o del dueño, si aplica>
> ```

**Al terminar tu bloque de trabajo:** commit en tu rama → `PUSHEO EN CURSO` acá → integración a `master` → `PUSHEADO <hash>`.
**Antes de empezar tu turno:** `git fetch origin` y rebase/merge de tu rama sobre `origin/master`.

---

## 📦 Archivos borrados en esta consolidación (01/11/2026)

`CRUCE - 76 REVISAR vs opencode.md` · `ESTADO - las 4 sesiones.md` · `INTAKE - baseline 5 carpetas U0.csv` ·
`INTAKE - material nuevo 3er Sem.md` · `LOG-opencode.md` · `LOG-opencode-nube.md` ·
`LOG-opencode-onedrive.md` · `LOG-opencode-site.md` · `PISTA - Mensaje para opencode...md` ·
`PISTA - migracion vault...md` · `PISTA - reparacion mojibake 9 notas...md` ·
`PROBLEMA - commits mezclados...md` · `PROPUESTAS - links rotos (carril C).md` ·
`PROPUESTAS - links rotos por contenido (opencode).md` · `REPORTE - links aproximados (carril C).md`

> Recuperables con `git show <commit-anterior>:Clippings/<archivo>`. Su contenido vigente está en las secciones de arriba.
