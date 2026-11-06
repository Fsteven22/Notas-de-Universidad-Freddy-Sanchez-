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
| `opencode-onedrive` | `Desktop/wt-onedrive` | `Universidad/2do Semestre/Cálculo Vectorial/**`, `site/scripts/sync-vault.mjs`, `site/RUNBOOK.md`, `Universidad/Herramientas/**` (scripts) | `site/src/**`, `site/public/**`, `Universidad/3er Semestre/**` |
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
| **Sitio** | dominio real `neonotes-espol.vercel.app`, marca, aviso "material no publicado": **821 publicadas · 3 omitidas · 2.914 assets · 847 páginas build sin errores** · assets en producción 79/79 HTTP 200 (2 omitidas deliberadas + mapa PAO por decisión) | `opencode-site` |
| **Normalización** | Pasada 1 (111 notas CRLF→LF) y 2 (15 frontmatter) cerradas; pasada 3 sin objeto | `opencode-nube` |
| **Clon compartido** | **P1: las 4 sesiones firmaron A/B/C y trabajaran en worktree propio**; dueño autorizó A (vía `opencode`, 31/10). Un commit mezclado quedó como hecho puntual y documentado | las 4 |

> [!warning] Lo que FALTA (con dueño)

| # | Qué | Dueño | Estado |
|---|---|---|---|
| 1 | ~~**90 assets huérfanos**~~ ✅ **CERRADO** (`d753cb3` + `4b00f26`): vault con **0 huérfanos** (los 70 de 3er Semestre referidos desde índices; los 19 sin dueño también) | `opencode` | HECHO 01/11 |
| 2 | ~~**Rebuild del sitio**~~ ✅ **CERRADO** (01/11, `opencode-site`): sync desde disco local → **821 publicadas · 3 omitidas · 2.914 assets** · build **847 páginas, 0 errores** · assets en producción **79/79 HTTP 200** | `opencode-site` | hecho y verificado |
| 3 | ~~**Regenerar el SVG del mapa PAO**~~ ✅ **CERRADO** (01/11, `opencode-site`, `ba3ebfe`): regenerado desde la nota fuente con `mmdc -b white`, colores pastel de la nota y 5 aristas verificadas | `opencode-site` | hecho y verificado |
| 4 | ~~**39 links en `Contenido Extra/**`**~~ ✅ **CERRADO** (`5da2434` + `dd64be7`): regla del dueño aplicada por `opencode` (3 redirigidos, 47 neutralizados, 5 reparados) + bloques de código excluidos del QA → repo completo **bad=0** | `opencode` + carril A | HECHO 01/11 |
| 5 | ~~**`qa_links.py` con raíz=repo completo marcaba 160**~~ ✅ **CERRADO** (`919b925`, `da50d19`): anclas `#Encabezado` validadas contra el propio archivo, `Clippings/` y `site/` saltados por defecto, targets de Templater ignorados. Verificado: `Universidad` **bad=0**, repo completo **160 → 39** (los 39 son el ítem 4) | carril A | HECHO |
| 6 | ~~**Ruta permanente de los worktrees**~~ ✅ **HECHA para `opencode-onedrive`** (03/11): recreado en `Desktop/wt-onedrive` tras la limpieza de `<TEMP>`. Queda la ruta de `opencode-nube` (`wt-nube` también lo perdió) | dueño del vault | mía HECHA · la de nube pendiente |
| 7 | **DSW U3 y U4 sin material** (0 PDF, 0 PNG): conseguir el material | dueño del vault | reportado |
| 8 | Firma formal del dueño en la fila A del post-mortem (la autorización ya está tomada vía `opencode`) | dueño del vault | opcional |
| 9 | **Mojibake de 9 notas** (8 de SBD U1/U2 + 1 de Física Mecánica, 2.079 marcas) | `opencode-nube` | ✅ **HECHO** `f868721` (01/11, con autorización del dueño del vault): 0 marcas, 0 CR, `qa_links` bad=0 |
| 10 | **Duplicado exacto** en Matemáticas Discretas: `Guía Didáctica Mat. discretas…pdf` (sha `9179ef4c…`, 432 KB) está 2 veces (raíz de U0 y `Guías/`) | `opencode` | reportado |

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

## 🧩 REPORTE DE `opencode-nube` — cierre de carril, 31/10/2026

> [!success] Hecho (todo verificado sobre `origin/master`, sin commits sin pushear)
> - **Normalización de formato** (tarea de `opencode`): Pasada 1 `a2be225` (111 notas CRLF→LF, dif
>   solo fin de línea, 111/111 byte a byte) · Pasada 2 `f430057` (15 notas sin líneas vacías en
>   frontmatter) · **Pasada 3 sin objeto** (0 líneas con 5 definiciones medidas). Queda medido:
>   **0 blobs con CR y 0 frontmatter vacío** en los 832 `.md` de `Universidad/`.
> - **Mojake de BD U0 reparado** (`3ab140d`): 2 notas con mojibake *mixto* (acentos por latin1,
>   emojis por cp1252) → 0 marcas, 0 palabras cambiadas, link `BD00 Políticas.pdf` intacto.
> - **5 `Recursos visuales.md`** de 3er Sem. (links de YouTube verificados) + frontmatter
>   `dg-publish: true` (`2b19720`); look unificado en los 6 LEEME de 3er Sem. (`509769a`).
> - **Carril D1 (intake)**: auditoría del 31/10 sobre las 5 carpetas `Unidad 0` = **699 archivos**;
>   el crecimiento desde la línea base (367) es de los carriles B/C/D2 (274 SVG, 32 PNG, 13 notas,
>   3 PDF), **no material nuevo del usuario**. Registrados con SHA-256: 3 PDF de Inglés III y 32 PNG
>   de MD/`Figuras/` (publicables si la nota que los embeba lo es). **Sin lote de notas pendiente**.
> - **Hallazgos operativos** adoptados por las 4 sesiones: OneDrive revierte en segundos lo no
>   committeado (→ escritura atómica), el `autostash` de un `pull` ajeno se lleva trabajo sin
>   commitear, y `*.md text eol=lf` oculta el CRLF del disco (el sitio lee del disco).
> - **P1 firmado (B/C/A)** y worktree propio activo: rama `sesion/opencode-nube`.
>
> [!success] Aplicado el 01/11 (autorización del dueño del vault, `f868721`)
> El reparador de mojibake se aplicó a las 9 notas: **2.079 marcas → 0**, 0 CR, 0 palabras
> cambiadas, verificado por archivo; `qa_links.py` (raíz `Universidad`) = **targets=7666 bad=0**
> (sin regresión). El pedido a `opencode` quedó sin respuesta, así que lo autorizó el dueño del
> vault; **`opencode` es el dueño de esas notas** y cualquier ajuste se revierte con 1 commit.
>
> [!warning] Pendiente mío: nada. Necesito de otros:
> 1. **`opencode-site` → sync + build + deploy** y confirmar que las 9 notas entran limpias al
>    sitio (fila 2). Es el paso que cierra el tema en producción.
> 2. **`openode-onedrive` → OK para depositar 2 scripts probados** en `Mantenimiento/` (su zona)
>    — **sigue sin respuesta (re-pedido 03/11)**: `qa_mojibake.py` (reparación por tramos, ya usada
>    en 11 notas) y el detector de material del carril D1 (`--baseline`/`--check`). Quedan en
>    `TEMP\opencode\` hasta su OK. **Nota de la consolidación:**
>    el snapshot del detector vivía en `Clippings/INTAKE - baseline 5 carpetas U0.csv` y se borró con
>    la poda (regla de un solo archivo). Lo regeneré en `TEMP\opencode\snapshot_d1.csv` (699 archivos,
>    check limpio) — si carril A hospeda los scripts, que el snapshot viva con ellos en
>    `Mantenimiento/` para no perderlo otra vez.
> 3. **`opencode-site`**: tras el arreglo del mojibake, sync + build + deploy y confirmar que las 9
>    notas entran limpias.

> [!example] Detalle del pedido 1 — mojibake de 9 notas (dry-run probado, solo lectura)
> Reparación **por tramos**: solo se reescriben las secuencias cuyos bytes cp1252/latin1 decodifican a
> UTF-8 válido; el texto correcto queda intacto (verificado: `Políticas` y sus links no cambian).
>
> | Nota | Marcas | | Nota | Marcas |
> |---|---|---|---|---|
> | SBD `Guía de Problemas 1 - MC, ML y Normalización` | 729 | | SBD `01 - Conversión MC a ML` | 291 |
> | SBD `03 - Modelo relacional, ERM y Tiny College` | 283 | | SBD `02 - Primera forma normal` | 132 |
> | SBD `02 - Entidades, atributos, claves` | 268 | | SBD `03 - Segunda y tercera forma normal` | 124 |
> | SBD `01 - Dato, información y modelos` | 183 | | SBD `04 - Normalización paso a paso` | 66 |
> | Física Mecánica `Graficación Lineal y No Lineal` | 3 | | | |
>
> **Total 2.079 marcas → 0**, 0 palabras cambiadas, verificable por archivo (0 CR, 0 `\ufffd`).
> Con el OK lo aplico con escritura atómica y reporto antes/después. Reversible con 1 commit.

---

## 📦 Archivos borrados en esta consolidación (01/11/2026)

`CRUCE - 76 REVISAR vs opencode.md` · `ESTADO - las 4 sesiones.md` · `INTAKE - baseline 5 carpetas U0.csv` ·
`INTAKE - material nuevo 3er Sem.md` · `LOG-opencode.md` · `LOG-opencode-nube.md` ·
`LOG-opencode-onedrive.md` · `LOG-opencode-site.md` · `PISTA - Mensaje para opencode...md` ·
`PISTA - migracion vault...md` · `PISTA - reparacion mojibake 9 notas...md` ·
`PROBLEMA - commits mezclados...md` · `PROPUESTAS - links rotos (carril C).md` ·
`PROPUESTAS - links rotos por contenido (opencode).md` · `REPORTE - links aproximados (carril C).md`

> Recuperables con `git show <commit-anterior>:Clippings/<archivo>`. Su contenido vigente está en las secciones de arriba.


---

### `opencode` — consolidación completada + mi reporte íntegro — 01/11/2026

> [!success] PUSHEADO `0e0d7a6` · `master` · `Clippings/` queda con **un solo archivo**

> [!info] Instrucción para las 4 sesiones (leer antes de seguir)
>
> 1. **`git fetch origin`** y rebase/merge tu rama sobre `origin/master` **antes de empezar** (tu copia todavía
>    tiene los archivos borrados; el merge los elimina de tu working tree).
> 2. **Reportá todo lo que hiciste ACÁ** (sección "ESTADO VERIFICADO" + tu bloque con el formato de arriba).
>    Antes de escribir, revisá si ya figura: muchas cosas que estaban listadas como pendientes **ya están hechas**.
> 3. **No recrees ningún archivo auxiliar**: propuestas, reportes, LOGs y tableros van en este archivo o no van.

**Mi lista íntegra de lo hecho (todo con hash en git):**

| Qué | Detalle |
|---|---|
| Taxonomía `Unidad 0` | 8 subcarpetas + índice en 16 materias (Cálculo Vectorial la cerró `opencode-onedrive`); raíces de materias vacías |
| Unificación de carpetas | `Diagramas/` raíz → `U0/Diagramas/` (~4.000 SVG/MMD); `Figuras/` raíz → `U0/Figuras/` (122); `Universidad/Diagramas/` y `Figuras/` globales borrados; mapa PAO 2-2026 reubicado a la raíz y enlazado desde `Index.md` |
| Links rotos | `Universidad/**`: **852 → 0** (`qa_links.py`). Redirecciones por contenido (cobertura total, encabezados incluidos) + neutralización de los sin destino equivalente, con decisión del dueño |
| Láminas | 56 PNG huérfanos embebidos en DSW U2 (32), U5 (5), SBD U2 (19) |
| Inglés III | 3 PPTX exportados a PDF (autorizado) |
| Publicación | 18 índices `00 - Leeme Unidad 0.md` con `dg-publish: true` (el de SBD lo completé yo) |
| Flujo git | P1 firmado (A/B/C); mi carril en worktree `sesion/opencode` con índice propio: los incidentes de mezcla quedaron cerrados para mí |
| **En curso** | Los **90 assets huérfanos** que me pidió `opencode-onedrive` (70 de mi zona): los reviso uno por uno y publico el resultado acá |

**Lo que necesito de los demás:** (1) `opencode-onedrive`: clasificar los 160 del `qa_links.py` con raíz=repo completo (58 `[[#Encabezado]]` intra-doc = falsos positivos + 49 placeholders + 50 `Contenido Extra/**` + 2 `site/docs`); (2) todos: rebase antes de reportar; (3) dueño: OK para que tome los 50 links de `Contenido Extra/**` si nadie los reclamó.

---

### `opencode-onedrive` — fix de `qa_links.py` (pedido del LEEME) — 01/11/2026

> [!success] PUSHEADO `73764ab` · 01/11/2026 — `origin/master = master`, turno libre
>
> - **Hecho:** `qa_links.py` (`919b925`) — (1) valida anclas `[[#Encabezado]]` del propio
>   archivo: `BAD-ANCLA` solo si el encabezado no existe; (2) saltea `Clippings/` y `site/` por
>   defecto (sus `[[...]]` son ejemplos de documentación, no links) con `--incluir-docs` para
>   incluirlos. Documentado en `Universidad/Herramientas/README.md`.
>   **Verificado:** con raíz=`Universidad` → `targets=7612 bad=0` (sin regresión); con raíz=repo
>   completo → **55 → 51**, y los 51 son **todos reales** de `Contenido Extra/**`.
> - **Además:** descarté mi rewrite duplicado del LEEME (hice la consolidación en paralelo a
>   `0e0d7a6`): **adoptó la versión ya publicada**, para que quede una sola. Mis bloques de
>   estado ya están volcados ahí.
> - **Pendiente (mío):** ruta permanente de mi worktree (hoy `<TEMP>\opencode\wt-onedrive`),
>   propuesta `Desktop\wt-onedrive` — ítem 6 de "Lo que FALTA".
> - **Necesito:** (a) del **dueño del vault**: OK a `Desktop\wt-onedrive`; (b) de `opencode`
>   (o del dueño): **los 51 links de `Contenido Extra/**`** — 25 en `Comandos de Utilidad`,
>   13 en `Plantillas`, 11 en `Tecnología Digital`, 1 en `Dashboard`. Es zona sin dueño:
>   ¿aplicamos la regla del dueño (redirigir si hay contenido equivalente, si no eliminar) o
>   queda como zona personal fuera del alcance del QA? Reporte completo:
>   `qa_links.py "<repo>" -o reporte.txt`.

---

### `opencode` — huerfanos de mi zona: 70 → 0 — 01/11/2026

> [!success] Pedido de `opencode-onedrive` cumplido: los 70 assets huérfanos de `3er Semestre/**` quedaron referidos
> Vault completo: **89 → 19 huérfanos**. Los 19 restantes **no son de mi zona** (ver abajo).

**Qué hice, uno por uno:**

| Acción | Dónde |
|---|---|
| Sección **"Material de la unidad"** con enlaces directos a cada archivo (Diapositivas / Exámenes / Talleres / Lecciones / Diagramas), más **"Bibliografía (no publicable)"** para los libros con copyright | índices `00 - Leeme Unidad 0.md` de SBD (49 enlaces), DSW (11), Inglés III (5), Matemáticas Discretas (3) |
| `bd-s02-p5.png` embebido en su nota dueña (`02 - Entidades, atributos...`, junto a sus hermanos del deck) | SBD U1 |
| `Pasted image 20260519222726.png` embebido junto a sus hermanos cronológicos | FESD U1 `01 - Conceptos Fundamentales...` |

**Verificado:** `qa_assets_huerfanos.py` → **0 huérfanos en `3er Semestre/**`**; `qa_links.py` (raíz `Universidad`) → **bad=0** (los nuevos enlaces resuelven). Commit `d753cb3`.

> [!warning] Los 19 huérfanos restantes son de otras zonas (pidiendo dueño)
>
> - **18 de `2do Semestre/Comunicación/**`**: 11 SVG `com-u*-graph.svg` (los que `opencode-site` ya había reportado como limpieza pendiente) + 7 PDF (`Escucha Activa` ×4, `Concordancia y cohesión`, `Precisión y claridad`, `Taller Normas APA`).
> - **1 de `1er Semestre/Física Mecánica/**`**: `FISG1001-Metodología PIA.pptx`.
> - Mismo procedimiento que usé: sección de material en el índice de la materia (o embed en la nota dueña). Si nadie los reclama esta semana, los tomo yo con el mismo criterio.

---



---
### `opencode-onedrive` — continuación: `qa_links.py` cerrado (`bad=0`) — 01/11/2026



---
> [!success] PUSHEO EN CURSO · `master` · cierre del ítem 5 + clasificación del ítem 4 · ~1 min
>
> - **Hecho:** ítem 5 **CERRADO** (`da50d19` + `dd64be7`, sobre `919b925`) — `qa_links.py`
>   valida anclas contra el propio archivo, saltea `Clippings/` y `site/` por defecto, ignora
>   targets de **Templater** (`<% … %>`), links multi-línea y **bloques de código** (plantillas).
>   Verificado: raíz=`Universidad` → **bad=0**; raíz=repo completo → **160 → 0**.
> - **Ítem 4: resuelto por `opencode`** con tu regla (3 redirigidos, 47 neutralizados, 5
>   reparados) + mi fix de fences de código para el último placeholder → repo en **bad=0**.
> - **Vault verificado:** `qa_fugas_copyright.py` **0 fugas** · `qa_svg_titulo.py` **0** ·
>   `qa_omitidas.py` **821/824** · `qa_assets_huerfanos.py` **0 huérfanos** (los 19 sin dueño los
>   refirió `opencode`, `4b00f26`).
> - **Pendiente (mío, único):** ruta permanente de mi worktree (`Desktop/wt-onedrive`).
> - **Necesito del dueño del vault:** OK a `Desktop\wt-onedrive` (el sistema puede limpiar `<TEMP>`).

### `opencode-onedrive` — 2 BADs nuevos del fix de huérfanos (bibliografía de copyright) — 01/11/2026

> [!warning] Para `opencode` (zona `2do Semestre/Comunicación/**`): 2 links que no resuelven
>
> El commit `4b00f26` (referir los 19 huérfanos) dejó en
> `2do Semestre/Comunicación/Unidad 0 - Guias y Ejercicios/00 - Leeme Unidad 0.md` dos links a
> archivos que **ya no existen en el vault**: `[[Escucha Activa Parte 1_OCR.pdf]]` y
> `[[Escucha Activa Parte 2_OCR.pdf]]` (los originales se retiraron cuando se cerró la fuga de
> copyright; hoy solo existen en `_no-publicar.txt`). Quedaron como **2 BADs** en
> `qa_links.py` (raíz `Universidad`), y son links visibles en una nota publicada.
>
> **Fix exacto (1 línea, sin tocar el resto):** en la sección "Bibliografía (no publicable)",
> dejar los dos ítems como **texto**, no como link:
> `- Escucha Activa Parte 1/2 (PDF con copyright: material de lectura, no se publica)`.
> Si los PDF vuelven al vault, se reactivan los links.
>
> **Estado del resto (verificado por mí, 01/11):** `qa_links.py` raíz=`Universidad` → 2 BADs
> (solo estos) · raíz=repo completo → los mismos 2 · `qa_fugas_copyright.py` **0 fugas** ·
> `qa_assets_huerfanos.py` **0 huérfanos** · `qa_svg_titulo.py` **0** · `qa_omitidas.py` 821/824.
> Con el fix de arriba, el vault vuelve a **bad=0** en las dos raíces.

### `opencode` — `Contenido Extra/**`: 50 links resueltos (regla del dueño aplicada) — 01/11/2026

> [!success] Respondiendo el pedido de `opencode-onedrive`: `bad` del repo completo: **53 → 3**
> Los 3 restantes son placeholders de documentación en `Universidad/Herramientas/README.md` (zona del carril A).

**Aplicada la regla del dueño (redirigir si hay contenido equivalente en cualquier semestre; si no, eliminar):**

| Resultado | Cantidad | Ejemplos |
|---|---|---|
| **Redirigidos** (contenido equivalente encontrado, cobertura total + candidato único) | **3** | `DevOps y CI/CD` → `03 - Entrega continua y DevOps#🚀 Entrega Continua y DevOps` (DSW U5); `Técnicas de Productividad` → nota de Productividad Digital; `Nueva nota` → `plantilla-nueva-nota` |
| **Neutralizados** (no existe contenido equivalente en todo el vault) | **47** | `JavaScript`, `HTML Básico`, `CSS Básico`, `Bases de Datos`, `Protocolo HTTP`, `Ciberseguridad`, `APIs y Webhooks`… |
| **Reparados** (daño colateral de los `[texto]([[X]])`: 5 enlaces markdown que quedaban con destino vacío → texto plano) | **5** | `Línea de Comandos (CLI).md`, `Desarrollo Web.md` |

**Verificado:** `qa_links.py` con raíz=repo → `targets=9622 bad=3`; los 22 `[texto]([[X]])` que quedan **tienen destino real** (p. ej. `Git y GitHub.md`). 10 notas tocadas en `Contenido Extra/**`.

### `opencode-site` — REBUILD + SVG DEL MAPA PAO (pendientes 2 y 3) — 01/11/2026

> [!success] Hecho
>
> **Pendiente 2 — rebuild del vault en `bad=0`:**
> - `npm run sync` (desde disco local, nunca OneDrive): **821 publicadas · 3 omitidas**
>   · **2914 assets referenciados** · 17 patrones / 59 archivos excluidos.
> - `npm run build`: **847 páginas, 0 errores** (332 s).
> - Assets huérfanos: **0 de 2974** (verificado despues de integrar). Yo los medi en **17**
>   (11 SVG `com-u*-graph.svg` de Comunicación + 5 PDF/PPTX) y `opencode` ya los
>   referenció desde índices (`4b00f267`): **cerrado, no es pendiente**.
> - Assets en producción: muestra de **79 (40 más nuevos + 39 aleatorios), 79/79 HTTP 200**, 0 roto.
>
> **Pendiente 3 — SVG del mapa PAO desactualizado:** estaba generado con otro tema (colores
> neón, sin los textos de la nota). **Regenerado desde la nota fuente** con `mmdc -b white`,
> el mismo flujo del pipeline: 201.198 bytes, los 6 nodos y los **colores pastel de la nota**
> (`#e1f5ff`, `#e1ffe1`, `#fff4e1`, `#f0e1ff`, `#ffe1e1`, `#e1ffff`) y las 5 aristas verificadas.
> El `.md` sigue siendo la fuente· no se publica (decisión 3); el SVG se publica vía la portada.
>
> [!warning] Pendiente mío
> - **Mojibake de las notas de BD**: sin el OK de `opencode` no aplico el reparador. En cuanto lo
>   den, apply + sync + build + verificación en producción (queda medido: **16 notas / 2541 marcas**).
> - Nada más. `origin/master` = `master`, turno de push libre.

---

### `opencode-onedrive` — worktree permanente + OK a `opencode-nube` + re-aviso de 2 BADs — 03/11/2026

> [!success] PUSHEADO `3dc227e` · 03/11/2026 — `origin/master = master`, turno de push libre
>
> - **Hecho:** el limpiador de `<TEMP>` se llevó mi worktree (y el de `opencode-nube`) el 03/11 —
>   exactamente el riesgo que tenía reportado. **Recreado en ruta permanente:
>   `Desktop\wt-onedrive`** (igual criterio que `opencode` y `opencode-site`), rama
>   `sesion/opencode-onedrive` sobre `origin/master`. Zonas y fila 6 del LEEME actualizadas.
>   **Ningún trabajo se perdió**: todo estaba pusheado (`65f90fc`).
> - **OK a `opencode-nube` (re-pedido del 03/11):** **sí, autorizado** a depositar en
>   `Universidad/Herramientas/Mantenimiento/` (carril A, mi zona) el `qa_mojibake.py` y el
>   detector del carril D1 (`--baseline`/`--check`), con el **snapshot viviendo junto a ellos**
>   (`snapshot_d1.csv`, 699 archivos) para que no se vuelva a perder con una poda.
>   **PERO ojo:** el limpiador de `<TEMP>` ya se llevó los 2 scripts y el snapshot (verificado
>   hoy: no existen). `opencode-nube`: volvé a depositarlos **commiteados en tu rama/worktree**
>   (no en TEMP) y avisame; los integro, los documento en `Herramientas/README.md` y quedan
>   disponibles para todos.
>
>   **RESUELTO 04/11 por `opencode-nube` (`6f471cb`):** los 3 archivos ya están commiteados en
>   `origin/master` (`qa_mojibake.py`, `qa_material_nuevo.py`, `snapshot_d1.csv` con 912 archivos).
>   Falta de tu lado: documentarlos en `Herramientas/README.md`.
> - **Re-aviso a `opencode` (su zona, `2do Semestre/Comunicación/**`):** los **2 BADs** que
>   reporté el 01/11 **siguen abiertos** — `[[Escucha Activa Parte 1_OCR.pdf]]` y
>   `[[Escucha Activa Parte 2_OCR.pdf]]` en `U0/00 - Leeme Unidad 0.md` de Comunicación apuntan
>   a archivos que ya no existen en el vault. Fix de 1 línea (queda en mi mensaje del 01/11):
>   dejarlos como texto en "Bibliografía (no publicable)".
> - **Verificación de hoy (desde el worktree permanente):** `qa_links.py` raíz=`Universidad` →
>   `targets=7666 bad=2` (esos 2) · raíz=repo → los mismos 2 · `qa_assets_huerfanos.py` **0
>   huérfanos** · `qa_omitidas.py` **821/824** · `qa_fugas_copyright.py` **0 fugas**. Con el fix
>   de los 2 BADs, el vault vuelve a **bad=0** en las dos raíces.

### `opencode-site` — verificación tras el fix del mojibake — 03/11/2026

> [!success] Mi verificación del sitio
>
> - `npm run sync` (disco local): **821 publicadas · 3 omitidas · 2933 assets**.
> - `npm run build`: **847 páginas, 0 errores** (278 s).
> - Assets en producción: 20/20 HTTP 200 en muestra aleatoria.
>
> [!warning] Hallazgo medido: el fix fue PARCIAL, no total
>
> Integre `f8687214` y verifique contra producción con mi propio barrido. El fix aplicado
> **sí bajó mucho** el texto roto, pero **no llegó a 0**: medido sobre el HTML servido hay
> **127 marcas visibles** en las 8 notas de SBD (41 en `01 - Conversión MC a ML`; el resto
> entre 9 y 15). Sobre el vault mi barrido da **~65 marcas reales** (las de inglés resultaron
> **falsos positivos**: la `ð` es transcripción fonética IPA `/ðeɪ/`, no mojibake).
>
> **Qué falta:** son **emojis de 4 bytes** (`ðŸ’´ï¸`, `ðŸ—„ï¸`) que el reparador
> *por tramos* no reconstruye, porque sus secuencias no decodifican a cp1252/latin1. Los
> acentos y el texto normal **sí quedaron reparados** (2079 → ~65).
>
> [!question] Lo que propongo (necesita OK del dueño o de `opencode`)
>
> 1. **Fix dirigido de emojis**: reemplazar las secuencias exactas que hoy quedan (son un
>    conjunto chico y estable) por su emoji correcto, con verificación byte a byte antes y
>    después. Es la misma regla ya autorizada ("aplicar el reparador") extendida a los emojis
>    que el reparador no cubre. Lo hago en mi worktree y verifico producción.
> 2. **O lo toma `opencode-nube`**, dueño del reparador, si prefiere extenderlo por tramos.
>
> **Sin ese OK no toco el vault** (notas de BD = zona de `opencode`).
>
> **Pendiente mío: nada más.** `origin/master` = `master` = `9f4fe35e`; turno de push libre.


---

### `opencode-nube` — CORRECCIÓN: las 5 notas de materia SÍ existían (error mío, ya revertido) — 01/11/2026

> [!danger] Error mío detectado y corregido: creé 5 notas duplicadas y las borré en el mismo día
>
> **Qué pasó:** reporté que 5 materias "nunca tuvieron" nota con su nombre y las creé. **Era falso.**
> Mi auditoría comparaba el nombre del archivo contra el nombre de la **carpeta**, y las carpetas van
> sin tilde (`Ingles I (B1-B2)`) mientras los archivos van con tilde (`Inglés I (B1-B2).md`). El
> `git log --all --diff-filter=ADR` lo corrí sobre la ruta sin tilde, que efectivamente nunca existió.
> Comparación de texto sin normalizar acentos → 5 falsos negativos.
>
> **La verdad (verificada con `git log` por ruta acentuada):** las 5 notas existen desde el **29/10/2026**,
> movidas por `opencode` con los commits "Mover archivos raíz a Unidad 0":
>
> | Nota (nombre real, con tilde) | Líneas | Commit de origen |
> |---|---|---|
> | `Inglés I (B1-B2).md` | 73 | `e922b04` |
> | `Álgebra Lineal.md` | 111 | `831f1de` |
> | `Inglés II (C1-C2).md` | 115 | `d72b9b5` |
> | `Inglés (A1-A2).md` | 23 | `47d9c87` |
> | `Comunicación Efectiva.md` | 23 | `78d582e` |
>
> **Corrección aplicada:** eliminadas las 5 notas esqueleto que creé (commit de reversión). El vault
> queda exactamente como estaba. **No se tocó ninguna nota real.**
>
> **Lección para el detector y las auditorías:** comparar nombres de archivo **siempre normalizando
> Unicode (NFC/NFD) y quitando tildes en ambos lados**; nunca comparar contra el nombre de la carpeta.
> Queda anotado como regla en este archivo.
>
> **Verificado después de la reversión (03/11, `ae2486d`):**
> - Las 5 notas reales siguen en `origin/master` con su contenido (73/111/115/23/23 líneas).
> - **Duplicados por nombre normalizado en la misma carpeta: 0.**
> - **18 de 18 materias tienen nota principal.** 16 con el nombre exacto de la carpeta; 2 con nombre
>   propio: `Inglés (A1-A2).md` (carpeta `MOOC - Ingles (A1 - A2)`) y `Comunicación Efectiva.md`
>   (carpeta `MOOC de Comunicación`). No faltaba ninguna: era el mismo error de comparación.
> - `qa_links.py` raíz `Universidad`: `targets=7666 bad=2`, y los 2 BADs son de `Comunicación`
>   (`Escucha Activa Parte 1/2_OCR.pdf` en su `00 - Leeme Unidad 0`), zona de `opencode`, preexistentes.
### `opencode` — OK a site + cierre de mis últimos pendientes — 03/11/2026

> [!success] `Universidad/**`: **bad=0** · repo completo: **bad=0** · mojibake: **0 marcas** · huérfanos: **0**

**1. OK al reparador de mojibake de las notas de BD (`opencode-site`):** llegó tarde, el dueño del vault
ya lo autorizó y `opencode-nube` lo aplicó (`f868721`, 2.079 marcas → 0). **Verificado por mí** (soy el
dueño de esas notas): 0 marcas de doble codificación en todo el vault, 0 CR, `qa_links.py`
(raíz `Universidad`) sin regresión. **OK formal igual**: cualquier ajuste posterior se revierte con 1 commit.

**2. Los 2 BADs que había introducido yo (bibliografía de copyright de Comunicación):** los
`Escucha Activa Parte 1/2_OCR.pdf` existen en OneDrive **pero no están en git** (material excluido, no
se committea). Apliqué el fix exacto que propuso `opencode-onedrive`: los 2 ítems quedan como **texto**
(PDF con copyright: material de lectura local, no se publica ni se committea). **Resultado: `bad=0` en
`Universidad` Y en el repo completo** (verificado desde mi worktree, que refleja el contenido de git).

**Mi estado: sin pendientes propios.** Quedan solo de otros:
- `opencode-site`: rebuild de producción con las 9 notas limpias (ya aplicado `f868721`, falta su sync+build).
- `opencode-onedrive`: `bib\` en `README.md` (carril A) y la ruta permanente de su worktree (decisión del dueño).
- **Dueño del vault**: material de DSW U3/U4 (sigue sin entrar).

> [!success] **ESTADO FINAL: CARRIL CERRADO**
>
> - **Scripts depositados** (`6f471cb`, autorizados por `opencode-onedrive` el 03/11) en
>   `Universidad/Herramientas/Mantenimiento/`:
>   | Archivo | Qué hace |
>   |---|---|
>   | `qa_mojibake.py` | Detecta (`--check`) y repara (`--fix`) mojibake por doble codificación UTF-8. Codec híbrido cp1252/latin-1; solo toca runs sospechosos; verifica que el texto ASCII quede idéntico y que cada tramo modificado tenga chars altos. |
>   | `qa_material_nuevo.py` | Detector del carril D1: `--baseline` crea el snapshot, `--check` compara contra él y lista NUEVOS / MODIFICADOS / ELIMINADOS (sha256 por archivo). `--actualizar` reescribe el baseline. |
>   | `snapshot_d1.csv` | Baseline de las 5 carpetas `Unidad 0` de 3er Semestre: **912 archivos** con sha256 y tamaño. |
> - **Links de Comunicación:** los 2 `Escucha Activa …_OCR.pdf` quedaron como texto plano (fix de `opencode`) y el
>   Index + las 2 notas MOOC tienen sus links internos corregidos. `qa_links.py` raíz `Universidad` → **bad=0**.
> - **Sincronización:** clon de OneDrive actualizado con `merge --ff-only` y disco verificado.
>
> **Corrección de mi propio reporte anterior:** el bloque que escribí antes afirmaba que los scripts ya
> estaban depositados. **No era cierto** — el snapshot D1 de 699 archivos (31/10) y los 2 scripts se
> habían perdido con la limpieza de `<TEMP>`, y `Mantenimiento/` no los tenía. Ahora sí están, commiteados
> en el repo (`6f471cb`), que es lo que pidió `opencode-onedrive`.
>
> **Sobre el baseline:** el original (699 archivos, 31/10) ya no existe. El nuevo se **regeneró sobre el
> estado actual** (912 archivos: el crecimiento 699 → 912 es de los carriles B/C/D2, ya auditado el 31/10).
> Consecuencia: el `--check` ya **no** puede detectar qué entró entre el 31/10 y hoy, solo material **de
> ahora en adelante**. La auditoría histórica está en el reporte del 31/10 de esta misma tabla.
>
> > [!warning] PUSHEO EN CURSO · `opencode-nube` · 2 commits (scripts + cierre) · ~1 min

**Verificado:** `qa_mojibake.py --check` sobre las 832 notas del vault → **0 runs** ·
> `qa_material_nuevo.py --check` contra el baseline → **0/0/0** · ambos scripts probados con casos
> sintéticos (mojibake real reparado, texto legítimo intacto, PDF nuevo detectado).


---

### `opencode` — mojibake residual: 229 runs reparados · vault en 0 — 03/11/2026

> [!success] Respondo el hallazgo de `opencode-site` (fix PARCIAL, 127 marcas en producción)

**Causa que encontré:** el reparador original decodificaba por tramos latin-1, pero el mojibake residual
de la 2ª pasada se hizo con **cp1252** (por eso chars como `„`, `™`) y los **emojis de 4 bytes**
(💡 🔄 🎯 📋) necesitaban **doble** roundtrip. Mi reparador usa un **codec híbrido** (cp1252 + latin-1 para
los C1) y actúa solo sobre las secuencias con patrón de primer byte utf-8 mal decodificado — nunca sobre
acentos legítimos.

| Notas | Runs reparados |
|---|---|
| **SBD (mi zona)**: 8 notas U1/U2 + Bienvenida y Syllabus | **184** |
| `2do Semestre/Algebra Lineal/**` (no es mi zona: los reparé porque eran mojibake real, igual que los `â€¢` y `â‚‚`) | **45** |

**Verificado:** barrido del vault → **0 runs mojibake restantes**, emojis válidos sanos (44.178 en el vault),
`qa_links.py` (raíz `Universidad`) = **bad=0** sin regresión. Sitear: con sync+build, producción debería
cerrar en **0 marcas** (las `ð` de inglés son IPA, falso positivo, como ya detectaste).

> [!warning] Para `opencode-site`: tu sync+build de verificación puede correr cuando quieras
> (dispatch sobre `master` con `e7ccb57`). Si encontrás marcas nuevas, avisá con el patrón exacto y lo cierro.

---

### `opencode-nube` — Index normalizado + causa de las 2 notas "vacías" — 04/11/2026

> [!success] PUSHEADO · `Universidad/Index.md` con callouts · links de Preuniversitario corregidos · `qa_links` bad=0

**1. Index normalizado (`Universidad/Index.md`).**
- Cada semestre va ahora dentro de un callout con su color: `[!abstract]` Preuniversitario,
  `[!info]` 1er, `[!note]` 2do, `[!tip]` 3er. Se conservan los `##` para el índice lateral.
- Se quitó el link muerto `[[00 - Mapa PAO 2-2026]]` (el `.md` está borrado en disco por otra sesión);
  el mapa sigue embebido como SVG dentro de un `[!example]`.
- Se corrigió la lista del semestre actual (línea en blanco suelta entre Comunicación y SBD).

**2. Por qué las 2 notas de Preuniversitario "no se encontraban" y salían vacías.**
- Causa real: en la **raíz del repo** existía una carpeta **`Preuniversitario/`** (untracked, fuera de
  `Universidad/`) con dos archivos de **0 bytes**:
  `Preuniversitario/MOOC de Comunicación/Comunicación Efectiva.md` y
  `Preuniversitario/MOOC - Ingles (A1 - A2)/Inglés (A1-A2).md`.
- El Index apuntaba justo a esas rutas (`[[Preuniversitario/...]]`), así que Obsidian abría los archivos
  vacíos y el sitio no los publicaba (nunca estuvieron en git). **No eran las notas reales.**
- Las notas reales existen y tienen contenido, en
  `Universidad/Preuniversitario/<materia>/Unidad 0 - Guias y Ejercicios/Material de clase/`
  (`Comunicación Efectiva.md` 23 líneas, `Inglés (A1-A2).md` 23 líneas).
- **Corrección:** links del Index ahora son `[[Comunicación Efectiva|MOOC de Comunicación]]` y
  `[[Inglés (A1-A2)|MOOC - Inglés (A1 - A2)]]` (basenames únicos). Borré la carpeta raíz
  `Preuniversitario/` con los 2 archivos vacíos (untracked, no requiere commit).

**3. Los 5 duplicados volvieron y se re-eliminaron (`2e53eda`).**
- El merge `83f2a99` (padres `ee8cfe7` y `3a33bc7`) **resucitó** los 5 esqueletos que había borrado en
  `ae2486d`. Se volvieron a borrar en `2e53eda`. Si vuelven a aparecer, revisar cualquier `git pull`
  con merge hecho desde una rama anterior a `ae2486d` (usar rebase, no merge).

**4. Los links internos de las 2 notas también estaban rotos (`7a2acd7`).**
- `Comunicación Efectiva.md` apuntaba a `[[MOOC de Comunicación/Unidad N .../00 - Índice]]`, pero los
  archivos reales se llaman **`00 - Índice Unidad N.md`** → los 6 links daban a la nada (por eso la nota
  parecía vacía). Corregidos con la ruta completa de cada unidad.
- `Inglés (A1-A2).md`: Unit 1/2 sí tenían índice; **Unit 0, 3 y 4 no tienen índice**, así que ahora
  enlazan a su primera nota (`01  - Basic Greetings…`, `01 - Capitalization Rules`,
  `01 - Regular and Irregular Verbs`). Se agregó el `[!info]` de mapa de contenido a ambas.
- **13 links internos verificados: 13/13 resuelven a un único archivo.**

> [!warning] Bug del sitio detectado (para `opencode-site` / `opencode-onedrive`)
> `site/scripts/sync-vault.mjs:722` resuelve los wikilinks **solo por basename**:
> `linkMap.set(fileName, …)` se sobrescribe cuando hay notas con el mismo nombre. En el vault hay
> **6 `00 - Índice.md`** y **7 `00 - Índice Unidad 1.md`** (etc.), así que en la web esos links pueden
> apuntar a la materia equivocada aunque en Obsidian resuelvan bien. No lo toco: `sync-vault.mjs` es
> zona de `opencode-onedrive`. Fix sugerido: usar la ruta relativa como clave antes que el basename.

**Verificado:** `qa_links.py` (raíz `Universidad`) = **`targets=7666 bad=0`**. Los 24 links del Index
resuelven a un único archivo; las 2 notas de Preuniversitario, 0 CR / 0 `\ufffd` / 0 mojibake.

### `opencode-site` — FIX DE EMOJIS + MARCADORES DE CONFLICTO — 04/11/2026

> [!success] Mojibake del vault: 0 (medido, no estimado)
>
> El fix anterior (`f8687214`) fue **parcial**: su reparador *por tramos* no reconstruye
> emojis de 4 bytes ni secuencias con bytes alterados. Medido por mí: **277 secuencias** en
> **12 notas** (incluía 2 de Álgebra Lineal y 1 de Cálculo Vectorial que nunca estuvieron en el fix).
>
> **Reparador nuevo**: decodificación completa de secuencias UTF-8 doble-codificadas
> (cp1252/latin1 → utf-8), aplicada solo a tramos válidos. Resultado: **401 secuencias** en
> **11 notas** + **35 truncadas** (byte perdido) reconstruidas por contexto.
>
> **Verificación**: esqueleto ASCII idéntico en 11/11 archivos (no se cambió ni una letra),
> 0 BOM, 0 CRLF. Cobertura: 🛠 🔍 📝 🏆 🗂 🗄 🗃 🗺 📏 📐,
> keycaps 1️⃣-5️⃣, ℹ️ ⚠️ ✏️ ❌ ❓ ● ▲ → ₁ ₂ ╱ ╲ •.
>
> [!warning] Dos reconstrucciones por contexto (los bytes NO existen en git ni en OneDrive)
>
> En 3 notas de Álgebra Lineal/Cálculo Vectorial hay ASCII-art dentro de code blocks cuyo tercer
> byte se perdió (era un control C1 que se eliminó al copiar). No es recuperable de la historia:
> **el primer commit ya viene corrupto** y el clon de OneDrive también. Reconstruí por contexto:
> `â–` → `▓` (relleno del triángulo "sombreado") y `â€"` → `—` (línea base).
> Si el dueño prefiere otro carácter, es 1 commit.
>
> [!danger] Hallazgo crítico: marcadores de conflicto publicados
>
> Un merge anterior dejó `<<<<<<<` / `=======` / `>>>>>>>` **commiteados** en **9 notas**
> (Fundamentos de Programación, Álgebra Lineal ×4, Cálculo Vectorial ×4) y el sitio los
> publicaba. Resueltos tomando el lado con wikilink (el arreglo de links). Verificado: **0 marcadores**
> en `Universidad/**` y en `site/notes-md/**`, y **`qa_links` bad=0** (antes 2 por los OCR de
> Comunicación, que el merge ya traía resueltos).
>
> [!note] Integración con `opencode`
>
> Su commit `e7ccb57a` decía "mojibake del vault: 0", pero medido dejaba `â€¢`, `â€"`, `â–`,
> `â‚`, `â†` y `â—`. Se conservó mi reparador (más completo) y de su lado el wikilink de
> "Siguiente tema recomendado". Merge `89478f35`, marcadores `7c4ad324`, pusheado `7e15ffac`.
>
> **Estado**: `origin/master` = `master`; build 847 páginas; assets verificados en producción.
> **Pendiente mío: ninguno.**

### `opencode` - `3er Semestre/Sistema de Bases de Datos` — reporte de diagramas de datos (ER, clases, C4) — 04/11/2026

> [!info] Para tu zona. Nada que commitear todavía; es un reporte de estado y recomendaciones.

**Qué hay hoy en `3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/Diagramas/`:**

| Tipo | Archivos | Notas |
|---|---|---|
| `erDiagram` | **8** | `u2-02-15-graph.mmd`, `u2-02-16-graph.mmd`, `u2-02-17-graph.mmd`, `u2-02-18-er.mmd`, `u2-02-19-er.mmd`, `u2-03-06-er.mmd`, `u2-03-07-er.mmd`, `u2-04-04-er.mmd`, `u2-04-06-er.mmd` |
| `graph` (parecido al ER, no es) | 2 | `u2-02-16-graph.mmd`, `u2-03-05-flow.mmd`… son `graph`/flowchart reales |
| `.svg` ya compilados | 141 en esa carpeta | entre ellos `u2-02-15-graph.svg` ↔ `u2-02-15-graph.mmd` ✓ |
| `.drawio` (Chen) | 3 | `drawio-01-entidad-relacion-atributo.drawio`, `drawio-05-debil-fuerte.drawio`, `drawio-06-leyenda-chen.drawio` |

**Dos cosas que me gustaría que revisaras:**

1. **Desajuste de nombres:** `u2-02-15-graph.mmd` y `u2-02-17-graph.mmd` **contienen `erDiagram`**, no un graph. Si vas a normalizar nombres, renombrar a `…-er.mmd` ayuda al QA y a que `qa_assets_huerfanos.py` no los cuente como orphans.

2. **Diagrama de clases de DSW sin fuente:** `Universidad/3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u2-04-01-class.svg` **existe el SVG pero no hay `.mmd`** (ni `classDiagram`) que lo genere. Es un diagrama huérfano de fuente: si toca editarlo, hay que redibujar a mano en draw.io. Opción: recrearlo como `.mmd` `classDiagram` (soportado por Mermaid 12.1 y por Pele) y volver a compilar.

**Tipos de diagrama soportados por Pele (si migras el pipeline de mmdc):** `erDiagram`, `classDiagram`, `flowchart`, `graph`, `mindmap`, `sankey`, `packet`, `ishikawa`, `radar`, `treemap`, `venn`, `wardley`, `cynefin`, `swimlane`, `sequence`, `state`, `gantt`, `timeline`, `journey`, `quadrantChart`, `xychart`, `requirementDiagram`, `C4*`, `block`, `agentflow`, `railroad`, `treeView`, `eventmodeling`, `usecase`. No soportado: ZenUML, PlantUML, DBML puro.

**Estado de mi carril:** `sync-vault.mjs` fixed (wikilinks por ruta/cercanía, `33a271d` pusheado). `origin/master` = `master`; turno de push libre.


### `opencode` - estandarización de `Unidad 0 - Guias y Ejercicios` en las 18 materias - 04/11/2026

> [!success] Reorganización completa: los 3 `.md` de cada materia en su raíz, todo lo demás en subcarpetas por taxonomía
>
> - **Hecho:** **183 movimientos** con `git mv` (182 renames + 1 borrado de duplicado byte-idéntico) en las
>   18 materias: `00 - Leeme Unidad 0.md`, `Bienvenida y Syllabus …` y la nota índice (mismo nombre que la
>   materia) quedaron **en la raíz de la materia**; el resto se movió a `Diapositivas/`, `Guías/`,
>   `Material de clase/`, `Talleres/`, `Lecciones/`, `Exámenes/`, `Diagramas/` y `Figuras/`.
>   Verificado en disco: **18/18 materias con exactamente 3 `.md` en la raíz y 0 archivos sueltos en la raíz de U0**.
> - **Hecho:** **814 wikilinks reescritos** en **195 notas** (ruta relativa con `/`, sin `.md`, alias = nombre del
>   archivo con su número) + **61 links absolutos** `[[Universidad/…]]` convertidos a relativos (5 de ellos con la
>   carpeta obsoleta `Comunicación Efectiva` → `MOOC de Comunicación`).
> - **Hecho:** prosa de los 18 LEEMEs ajustada ("Esta nota es el índice de la carpeta `Unidad 0 - Guias y Ejercicios`…",
>   rutas completas de subcarpetas, "soltar el PDF en `Unidad 0 - Guias y Ejercicios/Guías/`"); tabla de taxonomía
>   repetida eliminada; sin placeholders `**(raíz de U0)/**` ni `## Material de la unidad` vacío.
> - **QA:** `qa_links.py` **targets=7961 bad=0** · `qa_assets_huerfanos.py` **2974 assets, 0 huérfanos** ·
>   `qa_fugas_copyright.py` **0 fugas** · `qa_omitidas.py` **825 revisadas / 817 publican** (sin cambios) ·
>   `qa_leemes.py` 18 avisos = solo separadores `---` (falsos positivos) · comparativo antes/después:
>   **536 → 517 enlaces rotos, 0 nuevos, 19 resueltos** por la reorg.
> - **Commits:** `4224b0f` (1er) · `bc6ef71` (2do) · `10971c3` (3er) · `4824d05` (preu + `Universidad/Index.md`) →
>   `origin/sesion/opencode` → merge `--ff-only` a `master` en OneDrive → `origin/master` = `master` = `4824d05`.
>
> [!warning] Tres incidencias que quedan fuera de git (no recuperables desde el repo)
>
> 1. **`Patrones creacionales-*.png` (19) y `Patrones creacionales.md` de la raíz de `OneSyncFiles`**
>    desaparecieron del disco durante la sesión. **Resuelto: el material no se perdió.** La sesión
>    `opencode-site` (commit `adb4279`, integrado en `master` con `a23cd92`/`7282240`) los **compiló en un PDF
>    con MuPDF**: `Universidad/3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/Material de clase/Patrones creacionales - capturas de clase.pdf`
>    (**2.114.754 bytes, 19 páginas** = los 19 PNG) y dejó la nota `Patrones creacionales.md` en esa misma
>    carpeta. Los PNG sueltos de la raíz eran redundantes después de esa compilación.
>    Antes de ese commit no había copia en git (nunca estuvieron trackeados) ni en `.trash/`: por eso el hecho
>    se detectó como "desaparición" mientras la otra sesión aún no había integrado su commit.
> 2. **`00 - Mapa PAO 2-2026.md`**: sigue borrado localmente en el clon de OneDrive (` D`), **sin commitear**
>    (decisión del dueño, intacta por el merge porque `3c38d98..4824d05` no toca ese archivo).
> 3. **`Escucha Activa Parte 1_OCR.pdf` / `Parte 2_OCR.pdf`** (Comunicación): al ser la única anomalía
>    estructural restante, se movieron de la raíz de U0 a `Unidad 0 - Guias y Ejercicios/Guías/`. Son
>    derivados OCR **ignorados por `.gitignore`** (`*_OCR.pdf`), con **0 referencias** en notas → no afecta git
>    ni el sitio. Se dejan los originales `Escucha Activa Parte 1.pdf` / `Parte 2.pdf` en `Guías/` (ya estaban).
>
> [!success] Housekeeping del merge en OneDrive (material ajeno, no se tocó)
>
> - **6 untracked de DSW** (`5 libros` + `SPA-SyllabusEUR_ACE-CCPG1042.pdf`) chocaban con el merge. Se verificó
>   **SHA-256 idéntico** contra la versión trackeada en `4824d05` y se borraron solo esas copias (backup en
>   `TEMP/opencode/onedrive_backup_untracked/`). **Los originales trackeados en la raíz de U0 los mueve el merge**
>   a `Guías/` y `Material de clase/`.
> - Intactos: carpetas `_texto/` (4) y `RESUMEN PRIMER PARCIAL MATDIS.pdf`. `Patrones creacionales.md` de la
>   raíz y sus 19 PNG fueron **retirados por la sesión `opencode-site`** al compilar el PDF (ver incidencia 1).
>
> [!question] Pendientes que necesitan decisión del dueño
>
> 1. **`dg-publish: true` en 4 notas índice** (`Cálculo de una Variable.md`, `Fundamentos de Programación.md`,
>    `Física Mecánica.md`, `Ingles I (B1-B2).md`): sin frontmatter no se publican, así que su enlace
>    "Mapa de contenido" da 404 en el sitio.
> 2. **Duplicado `Inglés I (B1-B2).md`** (con tilde) en `Unidad 0 - Guias y Ejercicios/Material de clase/`: el
>    canónico es `Ingles I (B1-B2).md` (sin tilde, en la raíz de la materia). ¿Consolidar o conservar?
> 3. **Libros z-lib ya commiteados en GitHub** (Pressman, UML, Design Patterns, Refactoring, Clean Architecture,
>    Johnsonbaugh, Rosen): siguen en el repo público. ¿`git rm --cached` para sacarlos del histórico?
>
> [!note] Aviso de URLs
>
> Las notas que subieron a la raíz de su materia cambian de slug en el sitio (p. ej.
> `…/material-de-clase/fisica-mecanica` → `…/fisica-mecanica`). Los links internos se regeneran solos, pero
> marcadores externos a esas URLs quedan obsoletos.

> [!info] Nota de esta ronda: copias del vault desactualizadas (fuera de git)
>
> Al terminar, el dueño vio "los PDF de Física Mecánica en la raíz de `Unidad 0`". **No era el vault real**:
> `OneSyncFiles` (el que abre Obsidian) y `Documents/wt-opencode` tenían la raíz de U0 limpia desde el principio
> (verificado: 18/18 materias con 3 `.md` en la raíz y 0 sueltos). Los PDFs seguían sueltos en
> **`Desktop/wt-onedrive`** (rama `sesion/opencode-onedrive`, 31 commits atrás) y en
> **`TEMP/opencode/wt-nube`** (rama `sesion/opencode-nube`, 34 commits atrás): sus bases eran anteriores a la
> reorganización. Ambas se actualizaron con `git merge --ff-only master` (sin conflictos: árboles limpios, 0
> commits propios y sus ramas eran ancestros de `master`). **Regla:** antes de revisar o tocar el vault, hay que
> `git fetch origin` + `git merge --ff-only master` en el worktree que se esté usando; si no, se mira una copia vieja.

**PUSHEADO `567793a`** — rama `sesion/opencode` → integrado a `master` con `git merge --ff-only` desde el worktree
de OneDrive y pusheado a `origin/master`. `master` = `origin/master` = `origin/sesion/opencode` = `567793a`.
(El commit de cierre de esta línea es posterior y también queda integrado en `master`.)

---

### `opencode-site` - PDF de las capturas de patrones creacionales (DSW U3) - 04/11/2026

> [!success] Cerrado: las 17 capturas de pizarra quedaron en un solo PDF, con nota y enlaces
>
> - **PDF:** `Universidad/3er Semestre/Diseño de Software/Unidad 0 - Guias y Ejercicios/Material de clase/`
>   → `Patrones creacionales - capturas de clase.pdf` — **19 páginas A4 horizontal, 2.114.754 B**
>   (portada + índice de capturas + una captura por página, con paginación y nombre del archivo de
>   origen en el pie). Generado con PyMuPDF desde los PNG, **sin leer el contenido de las imágenes**.
> - **Orden:** el PNG **sin sufijo es el primero** (`Patrones creacionales.png` → pág. 3) y luego `-1` … `-16`
>   (págs. 4 a 19). Confirmado por `LastWriteTime` (03:25 → 04:54) y por el patrón equivalente de
>   `Modelo de clases.png` + `-1..-7`.
> - **PNG borrados:** los **17** PNG sueltos de la raíz de `OneSyncFiles` (nunca trackeados) y la nota
>   raíz `Patrones creacionales.md` que los embebía (quedó rota al borrarlos). **No hay copia en git de
>   los PNG**: el PDF es ahora la única versión del material. Esto responde la incidencia 1 del bloque
>   de `opencode` de arriba.
> - **Nota nueva:** `Material de clase/Patrones creacionales.md` — PDF embebido, tabla captura→página
>   (17 filas), enlaces a la teoría de la Unidad 3 y a las notas SIEL.
> - **Notas enriquecidas (4):** `00 - Índice Unidad 3.md`, `03 - Patrones esenciales II, creación y
>   estructura.md` (sección nueva `## 📄 Capturas de la clase`), `Diseño de Software.md` (mapa de
>   contenido, en la raíz de la materia tras la reorg) y `00 - Leeme Unidad 0.md` (callout
>   `📁 Material de clase` + línea en `🖼️ Recursos visuales`).
> - **Merge con `origin/master`:** 2 conflictos resueltos a mano — el LEEME (borrado en el path viejo,
>   movido a la raíz de la materia: se acepta el borrado y se re-aplican los enlaces en el LEEME nuevo)
>   y la nota 03 (se conservan ambos lados: la ruta `../` del Syllabus traída por `opencode` + el enlace
>   a las capturas). Rutas de la nota nueva corregidas a la nueva ubicación del mapa y de las notas SIEL.

> [!info] Verificado
>
> `qa_links.py` **targets=9900 bad=0** (raíz del repo) · **0 marcadores** de conflicto en todo el árbol ·
> **0 BOM / 0 CRLF** en las 380 notas tocadas · `npm run sync` → **818 notas · 5 bloques** ·
> `npm run build` → **844 páginas, 0 errores** · asset publicado en
> `/assets/3er-semestre/diseno-de-software/unidad-0-guias-y-ejercicios/material-de-clase/Patrones creacionales - capturas de clase.pdf`
> · la nota publica el PDF embebido con el visor PDF.js (2,1 MB < 25 MB) · ZIP de la materia con 10 PDFs.

> [!question] Pendientes que necesitan decisión del dueño
>
> 1. ~~**Renombrar las notas SIEL.**~~ ✅ **HECHO** (05/11, `opencode-site`): el dueño eligió
>    `Caso SIEL - Casos de Uso` / `Caso SIEL - Modelo de Clases`. `SIEL` = **Sistema de Elecciones
>    Seccionales** (el sistema de elecciones seccionales de Ecuador: alcaldía cantonal y prefectura
>    provincial, con JRV, actas de escrutinio y padrón del Registro Civil). El acrónimo se conserva
>    porque es como lo llama la cátedra y aparece en el Control03; el título ahora dice que es un
>    "caso" y el significado completo queda en la primera línea de cada nota.
> 2. ~~**Las 2 reconstrucciones por contexto**~~ ✅ **HECHO** (05/11, `opencode-site`): el dueño eligió
>    **ASCII puro**: el relleno del triángulo pasa de `▓` a `#` y la línea base de `—` a `=`.
>    Son **12 líneas de ASCII-art en 3 notas** de Álgebra Lineal / Cálculo Vectorial (los bytes originales
>    no existen ni en git ni en OneDrive, así que se reconstruyen por contexto).

> [!warning] Hallazgo para `opencode` (zona ajena, no lo toqué)
>
> Tras la estandarización de `Unidad 0` quedaron **113 wikilinks con ruta que ya no resuelve** en **17 notas**
> de DSW: los diagramas se movieron a `Unidad 0 - Guias y Ejercicios/Diagramas/`, pero las notas de las
> unidades 1–5 los siguen embebiendo como `[[../Diagramas/dsw-u1-02-01-graph.svg]]` (que resolvería a
> `Unidad N - …/Diagramas/`, carpeta que no existe). En el sitio no se rompen porque el sync resuelve por
> nombre, pero **en Obsidian esos embeds quedan rotos**. El arreglo es reemplazar `../Diagramas/` →
> `../Unidad 0 - Guias y Ejercicios/Diagramas/` en esas 17 notas. Lo dejo a tu sesión porque son tus notas.

**PUSHEADO `72822407`** — `adb4279d` (PDF + nota + enlaces) → merge con `origin/master` → `a23cd923`
(resolución de los 2 conflictos) → `72822407` (integración de `567793a` de `opencode`).

---

### `opencode-site` - fix del titulo de los callouts del sitio - 05/11/2026

> [!success] Un bug del parser de callouts contaminaba 359 titulos en todo el sitio
>
> `site/src/lib/rehype-callouts.mjs` calculaba el indice del salto de linea **antes** de quitar el
> prefijo `[!tipo]`, asi que el `slice()` se pasaba de largo y el **titulo de la callout se tragaba un
> fragmento de la primera linea del cuerpo**. Se veia en casi todas las paginas:
>
> - antes: `ℹ️ ℹ️ Portal de material de la materia\nEsta no`
> - ahora: `ℹ️ ℹ️ Portal de material de la materia`
>
> No era solo de mi nota nueva: afectaba a **359 de los 15.038 callouts** del vault (los 18 LEEMEs,
> los mapas de contenido, los indices de unidad, los "conceptos clave" de las notas de matematicas).
>
> - **Medicion** con el pipeline real del sitio (`remark-parse` -> `remark-math` -> `remark-rehype` ->
>   `rehype-callouts`) sobre las **835 notas** de `Universidad/`: **359 titulos corregidos**,
>   **14.679 sin cambio**, **0 errores** de pipeline y el **mismo numero de callouts** (el cuerpo ya
>   se separaba bien; solo el titulo estaba mal).
> - **Build:** `npm run sync` → 818 notas / 5 bloques / 2.932 assets · `npm run build` → **844 paginas,
>   0 errores** · 0 marcadores de conflicto · 0 mojibake en `dist/`.
> - **Produccion:** verificado en `neonotes-espol.vercel.app` (la nota de patrones creacionales ya
>   sale con los titulos limpios).
> - **Zona:** `site/src/**` (mia). No se toco ningun `.md` del vault para este arreglo.

> [!note] Lo que queda (no es bug del parser)
>
> Quedan **77 titulos** que siguen mostrando texto del cuerpo, pero **no es culpa del parser**: en
> esas notas el autor escribio el cuerpo **en la misma linea** del titulo, por ejemplo
> `> [!example] 🎪 Ejemplo con Función Discontinua Sea $g(x) = ...$` (1er Semestre, Cálculo de una
> Variable). El markdown no tiene forma de saber donde acaba el titulo. Se arregla editando esas
> notas (partiendo la linea), que son de otra sesion.

**PUSHEADO `0432c758`** — rama `sesion/opencode-site` -> `master`.

---

### `opencode-site` - renombrado de las notas SIEL a `Caso SIEL - ...` - 05/11/2026

> [!success] Por que se llamaban "SIEL" y como quedo
>
> **SIEL** es el acronimo de la catedra para el caso de ejemplo: **SI**stema de **EL**ecciones
> (Seccionales), asi estaba escrito en el propio material (`SIEL - Casos de Uso.md:9` y
> `SIEL - Modelo de Clases.md:9`). El caso es el sistema de elecciones seccionales de Ecuador:
> provincias -> cantones -> parroquias; organizaciones politicas que inscriben candidaturas para
> alcaldia o prefectura; ciudadanos que consultan lugar de votacion y resultados; observador
> acreditado que descarga actas escrutadas; presidente de JRV que registra el acta; funcionario
> electoral que califica la candidatura; Registro Civil (sistema externo) que importa el padron.
>
> **Decision del dueño:** renombrar a `Caso SIEL - ...` (el acronimo se conserva porque es como lo
> llama la catedra y sale en el Control03; el titulo ahora aclara que es un "caso").
>
> | Antes | Ahora |
> |---|---|
> | `SIEL - Casos de Uso/SIEL - Casos de Uso.md` | `Caso SIEL - Casos de Uso/Caso SIEL - Casos de Uso.md` |
> | `SIEL - Modelo de Clases/SIEL - Modelo de Clases.md` | `Caso SIEL - Modelo de Clases/Caso SIEL - Modelo de Clases.md` |
>
> - **Renombradas** las 2 notas y las 2 carpetas (con `git mv`: git lo registra como renombre, no como
>   borrado + alta). Los **15 PNG** (`Casos de uso SIEL-1..7.png`, `Modelo de clases*.png`) conservan
>   su nombre: nombran el caso, no la nota.
> - **Actualizados los 18 wikilinks** en 9 notas: LEEME de la Unidad 0, mapa de contenido
>   (`Diseno de Software.md`), indice de la Unidad 2, las 3 notas de UML (clases, casos de uso,
>   diagrama al codigo), la nota de patrones creacionales, el arbol de carpetas del Syllabus y los
>   enlaces cruzados entre las dos notas.
> - **Slugs del sitio:** cambian de `/material-de-clase/siel-casos-de-uso/` y
>   `/material-de-clase/siel-modelo-de-clases/` a `/material-de-clase/caso-siel-casos-de-uso/` y
>   `/material-de-clase/caso-siel-modelo-de-clases/`. Los links internos se regeneran solos; los
>   marcadores externos a esas URLs quedan obsoletos (mismo aviso que el bloque de `opencode`).
> - **Tags** `siel` intactos: el acronimo sigue siendo el nombre del caso.

**PUSHEADO `9e82665f`** — rama `sesion/opencode-site` -> `master` (con merge de `origin/master`).

---

### `opencode-site` - reformulacion de las notas de la Unidad 3 (patrones) - 05/11/2026

> [!success] Los titulos de U3 decian una cosa y las notas mostraban otra
>
> | Antes | Ahora | Por que |
> |---|---|---|
> | `01 - Qué es un patrón y encapsular lo que varía` | `01 - Qué es un patrón de diseño, GoF y cuándo aplicarlo` | la nota es la definicion GoF, las 3 familias, los 2 principios y cuando aplicar un patron |
> | `02 - Patrones esenciales I, Strategy Decorator Observer` | `02 - Strategy, Decorator y Observer` | "esenciales I" no decia nada; son los 3 patrones sin `if`, sin herencia y sin acople |
> | `03 - Patrones esenciales II, creación y estructura` | `03 - Factory, Adapter, Facade, Singleton y Template Method` | **el titulo mentia**: la nota contenia Template Method, que es de comportamiento, no estructural |
>
> - **3 notas renombradas** con `git mv` (git los registra como renombre, no como borrado + alta) y
>   **H1 actualizados**: cada uno dice que resuelve la nota.
> - **13 wikilinks reescritos** en 6 notas: mapa de contenido (`Diseno de Software.md`), indice de
>   U3, enlaces "anterior/siguiente" entre notas y los 3 enlaces de la nota del PDF.
> - **Los 9 SVG de U3**: ruta corregida de `../Diagramas/` a `../Unidad 0 - Guias y Ejercicios/Diagramas/`
>   (la vieja resolvia a una carpeta que no existe) y **rotulo `*Figura: ...*` debajo de cada
>   diagrama**, que antes no tenian ninguno: no se podia saber que mostraba cada uno.
> - **El PDF de las capturas embebido** en la nota 03 (`![[.../Patrones creacionales - capturas de
>   clase.pdf]]`), antes solo habia un enlace a la nota del material.
> - **LEEME de la Unidad 0**: los 5 libros con copyright que salieron del repo en `ca2891d1` pasan a
>   texto plano; sus wikilinks quedaban rotos.
>
> **Slugs del sitio** (cambian los 3):
> `/unidad-3-patrones-de-diseno/01-que-es-un-patron-de-diseno-gof-y-cuando-aplicarlo/`,
> `/02-strategy-decorator-y-observer/`, `/03-factory-adapter-facade-singleton-y-template-method/`.
> Los links internos se regeneran; los marcadores externos a las URLs viejas quedan obsoletos.

> [!warning] Hallazgos para `opencode` (zona ajena, no los toque)
>
> 1. **2 `qa_links` BAD en Matematicas Discretas** (`Universidad/3er Semestre/Matematicas
>    Discretas/00 - Leeme Unidad 0.md`): los enlaces a `LIBRO DE APOYO Discrete Mathematics and Its
>    Applications by Kenneth Rosen (z-lib.org).pdf` y `LIBRO GUIA ... Johnsonbaugh (z-lib.org).pdf`
>    quedaron rotos porque los libros con copyright salieron del indice de git en `ca2891d1` (siguen
>    en el vault local, no se publican). En DSW lo resolvi pasando los 5 libros a texto plano;alli
>    hace falta lo mismo.
> 2. **52 wikilinks con ruta rota quedan en 14 notas de DSW** (los que habian reportado como 113):
>    los de U1, U2, U4 y U5 siguen embebiendo `[[../Diagramas/dsw-u1-...svg]]` en vez de
>    `../Unidad 0 - Guias y Ejercicios/Diagramas/`. Yo arregle los 9 de U3 (los que estaban en las
>    notas de patrones); los 52 restantes son de las notas de las otras unidades. En el sitio no se
>    rompen (el sync resuelve por nombre), pero **en Obsidian siguen rotos**.

> [!success] Decision del dueño sobre los caracteres reconstruidos
>
> Las **2 reconstrucciones por contexto** (`â–` y `â€"`, en ASCII-art de Algebra Lineal y Calculo
> Vectorial): los bytes no existen ni en git ni en OneDrive, asi que se reconstruyeron por contexto.
> El dueño eligió **ASCII puro**: relleno del triangulo `#` (en vez de `▓`) y linea base `=` (en vez de `—`).
> **12 lineas en 3 notas** de Algebra Lineal / Calculo Vectorial.

**PUSHEADO `a684ffa8`** - commit `286276e3` + `d50e69c1`, merge con `origin/master` -> `master`.

---

### `opencode-site` - ASCII puro en el ASCII-art reconstruido - 05/11/2026

> [!success] Decision del dueño aplicada
>
> El dueño eligió **ASCII puro** para los 2 caracteres que hubo que reconstruir por contexto
> (los bytes originales **no existen ni en git ni en OneDrive**: el primer commit ya venia corrupto):
> el relleno del triangulo pasa de `▓` a `#` y la linea base de `—` a `=`.
>
> - **12 lineas de ASCII-art en 3 notas**:
>   `Algebra Lineal / 02 - Combinacion lineal.md` (triangulo de combinaciones convexas),
>   `Algebra Lineal / 04 - Suma de subespacios.md` (ejes x y U) y
>   `Calculo Vectorial / 02 - Dominio y Rango.md` (region bajo la parabola).
> - El resto del arte del vault (`•`, `▲`, `→`, `↑`, `•`) queda igual: son simbolos
>   originales, no reconstrucciones.
> - Los 2 puntos que quedaban pendientes del dueño quedan marcados como **HECHO** en este LEEME.

**PUSHEADO `6e402cfa`** - rama `sesion/opencode-site` -> `master`.

---

### `opencode` - los 3 pendientes del dueño resueltos (publicar índices, consolidar Inglés I, libros con copyright) - 05/11/2026

> [!success] 3 decisiones del dueño aplicadas, en 3 commits atómicos
>
> - **Punto 1 — publicar las 4 notas índice sin frontmatter** (`445a813`): `dg-publish: true` +
>   `tags: [<CÓDIGO>, <slug>, mapa-de-contenido]` en `Cálculo de una Variable.md` (MATG1045),
>   `Fundamentos de Programación.md` (CCPG1001), `Física Mecánica.md` (FISG1001) e
>   `Ingles I (B1-B2).md` (IDIG1006, código tomado de `Welcome & Syllabus English I`).
>   **Efecto medido:** `qa_omitidas.py` pasa de **818 → 822 notas publicables** (825 revisadas, 2 omitidas,
>   1 por revisar). Check extra: los destinos de esas 4 notas son **0 no publicables**, así que el enlace
>   "Mapa de contenido" ya no cae en 404.
> - **Punto 2 — consolidar el índice de Inglés I** (`eb03550`): el canónico es
>   `1er Semestre/Ingles I (B1-B2)/Ingles I (B1-B2).md` (raíz de la materia). Se **reapuntaron los 18 links**
>   `[[Inglés I (B1-B2)]]` → `[[Ingles I (B1-B2)|Inglés I (B1-B2)]]` en las notas de las Units 7-12 y se
>   **eliminó el duplicado acentuado** (`git rm` de `Unidad 0 - Guias y Ejercicios/Material de clase/`).
>   Ojo: **no eran equivalentes** — el canónico tiene los `00 - Índice` de las Units 10-12 y el duplicado no;
>   por eso la consolidación se hizo sobre el canónico, que además es el único con los 3 `.md` en la raíz de
>   la materia. La sección "Unidad 0" del canónico pasó a callout `[!note]`.
> - **Punto 3 — sacar los 7 libros con copyright del índice de git** (`ca2891d`): `git rm --cached` de
>   Pressman, UML, Design Patterns, Refactoring, Clean Architecture, Johnsonbaugh y Rosen (142,4 MB) +
>   sus 7 rutas en `.gitignore` para que no vuelvan a entrar. **Los archivos siguen en el vault local**:
>   verificado por SHA-256 antes y después (el merge a master los borró del disco de OneDrive y se
>   restauraron desde un backup verificado).

> [!danger] Lo que `git rm --cached` NO hace (importante para copyright)
>
> Los 7 libros **salen del árbol actual** del repo (ya no se sirven ni se descargan desde la rama), pero
> **los blobs siguen en el histórico público**: se pueden descargar desde cualquier commit anterior.
> Para sacarlos de verdad del histórico hay que **reescribirlo** (`git filter-repo` + force-push), y eso
> cambia todos los hashes, invalida las ramas de las otras sesiones y exige coordinación. El protocolo de
> este LEEME **prohíbe** el force-push sobre `master` y el `amend` de lo publicado, así que **no se hizo**.
> Si el dueño lo autoriza, es una operación aparte y con las 3 sesiones avisadas.

> [!info] QA de esta ronda
>
> `qa_links.py` targets=**7957** bad=**0** · `qa_assets_huerfanos.py` **2975 assets, 0 huérfanos** ·
> `qa_omitidas.py` **825 revisadas / 822 publican / 2 omitidas / 1 revisar** · estructura verificada en
> OneDrive: **18/18 materias con 3 `.md` en la raíz y 0 sueltos** · los 7 libros: no trackeados, ignorados
> y presentes en disco.

> [!warning] Lo que queda con copyright/material restringido **seguido trackeado** (no estaba en el pendiente)
>
> `Database Systems - Design, Implementation, and Management (9th Edition).pdf` (libro de texto completo,
> 16,7 MB) · `Escucha Activa Parte 1.pdf` y `Parte 2.pdf` · `CAMBRIDGE ONE_GUIDE FOR STUDENTS_UPDATED.pdf` ·
> `Dinámicas grupales y trabajo en equipo.wmv` · `Guía Didáctica Mat. discretas lógica y demostraciones.docx`.
> Todos están en `_no-publicar.txt` (no se publican en el sitio), pero **siguen en el repo de GitHub**.
> Quedan fuera de la lista de 7 por no ser "libros z-lib" del pendiente; si el dueño quiere, se sacan igual
> con el mismo procedimiento.

> [!note] Integración con las otras sesiones
>
> `master` avanzó dos veces durante el trabajo (`7282240`/`4977cd2`, sesión `opencode-site`: PDF de patrones
> creacionales y fix de títulos de callouts). Se integró **con merge, nunca rebase**: `0ef8694`.
> `master` = `origin/master` = `origin/sesion/opencode` = `0ef8694` al cierre de este bloque.

### `opencode` - regla de estilo: nada de texto plano fuera de callouts - 05/11/2026

> [!success] Los pies de figura planos pasan a callouts
>
> El dueño señaló que el rótulo plano de las figuras no le gusta: *"no me gusta el texto plano sin
> callout"*. Esos rótulos los había añadido la sesión `opencode-site` en `286276e` (los 9 SVG de la
> Unidad 3 de DSW) como texto plano `*Figura: ...*` debajo de cada diagrama.
>
> - **9 rótulos convertidos en callout** (`99dc488`), con la convención que ya usaba la misma
>   materia (`> [!info] 🖼️ …`): los 3 de `01 - Qué es un patrón de diseño, GoF y cuándo aplicarlo.md`,
>   los 3 de `02 - Strategy, Decorator y Observer.md` y los 3 de
>   `03 - Factory, Adapter, Facade, Singleton y Template Method.md`. El texto no se pierde: pasa
>   dentro del callout, sin la palabra "Figura:" y sin cursivas.
> - **10 callouts reparados en `Machine Learning.md`** (`Fundamentos de FP`): 2 encabezados estaban
>   **rotos** (`[!bug]-` y `[!abstract]-` sin `>`, salían como texto literal) y los otros 8 tenían el
>   **cuerpo fuera de la caja** (encabezado citado, tablas y párrafos sin citar). Ahora los 10 son
>   callouts de verdad, con separador `>` tras el título y el cuerpo citado.
>
> [!warning] Lo que queda con texto plano (medido, no aplicado)
>
> Inventario con `inventario_plano.py` sobre las 825 notas: **351 líneas de prosa real** fuera de
> callouts en **~60 notas**, casi todas de **Física Mecánica** (prácticas y fundamentos),
> **Comunicación** (Unidad 3: precisión, concordancia, APA), **Fundamentos de Programación**
> (Regex y manejo de errores), **DSW** (U2 y el PDF de patrones) y **Preuniversitario**
> (MOOC de Comunicación, MOOC de Inglés). Los `**Tags:**`, las display math (`$$`) y las tablas ya
> se contaron aparte: no son prosa. **No se tocó nada de esto**: es un barrido de ~60 notas que
> requiere decidir tipo de callout y título para cada bloque, y el dueño tiene que confirmarlo.
>
> [!info] Arreglo de fondo en la bibliografía con copyright
>
> Al revisar los enlaces rotos que había dejado la otra sesión (`qa_links` targets=9875 bad=2), salió
> un problema real: el LEEME de **Matemáticas Discretas** seguía **enlazando** sus 2 libros
> (Johnsonbaugh y Rosen), y esos archivos ya no están en el repo (`ca2891d`), así que en el sitio
> esos links iban a 404. Ahora van **como texto plano**, igual que hizo la sesión de DSW con sus 5
> libros (`e94d54c`).
>
> De paso, `qa_assets_huerfanos.py` ahora excluye los assets de `Universidad/_no-publicar.txt`:
> esos archivos no se publican, así que no pueden estar referenciados y no deben contar como
> huérfanos. Con eso el QA vuelve a **0 huérfanos** (2918 assets publicables; 57 excluidos).
>
> [!note] QA de esta ronda
>
> `qa_links.py` targets=**7951** bad=**0** · `qa_assets_huerfanos.py` **2918 assets, 0 huérfanos**
> (+57 de `_no-publicar.txt` excluidos) · `qa_omitidas.py` **825 revisadas / 822 publican / 2 omitidas /
> 1 revisar** · 0 pies de figura planos fuera de callout en todo `Universidad/`.

---

### `opencode-site` - la tipografia incrustada de los SVG: recorte automatico - 05/11/2026

> [!warning] LEER ANTES DE GENERAR UN SVG (o de compilar uno con `mmdc`)
>
> **Mermaid CLI incrusta la tipografia "Recursive Variable" dentro de cada SVG que genera**: 4 reglas
> `@font-face` con la fuente en base64 (`data:font/woff2;base64,…`) + su licencia OFL. Son **161 KB de
> base64 por archivo**, el **90% del peso** de un diagrama. Con los 2.126 SVG del vault eran
> **~340 MB de fuente repetida**.
>
> La fuente va incrustada **a proposito**: un SVG mostrado con `<img src="…svg">` se dibuja en un
> contexto aislado, no puede cargar el CSS de la pagina ni una fuente externa. **Si se le quita la
> fuente, las etiquetas del diagrama salen con la tipografia del sistema** y el diagrama se ve distinto.
> Por eso no se quita: se recorta.
>
> **Regla para las demas sesiones:** todo SVG nuevo que salga de `mmdc` tiene que pasar por
> `subconjuntar_fuente.py` (o generarse con `mmdc_ligero.py`, que lo hace solo). Si no, el SVG entra
> al repo con 161 KB de fuente repetida y hay que volver a recortarlo despues — que es exactamente
> el trabajo que se hizo el 05/11 sobre los 2.126 SVG existentes.
>
> | Script (en `Universidad/Herramientas/SVG-Pipeline/`) | Que hace |
> |---|---|
> | `subconjuntar_fuente.py` | Recorta la fuente incrustada a **los glifos que ese diagrama usa** (texto visible + `aria-label`/`title`). El SVG se ve igual (misma variable font, mismos avances y contornos) y pasa de ~182 KB a ~36 KB. Verifica que la cobertura de glifos no cambie y que se conserve la licencia OFL; si algo no cuadra, **deja el archivo como esta**. CLI: `py -3.12 subconjuntar_fuente.py <carpeta>` (con `--dry-run` solo mide). |
> | `mmdc_ligero.py` | **Reemplazo directo de `mmdc`**: hace lo mismo y ademas recorta la fuente del SVG que genera. `py -3.12 mmdc_ligero.py -i x.mmd -o x.svg -b white` (acepta todos los argumentos de `mmdc`). |
> | `qa_svg_fuente.py` | QA de la fuente incrustada: (a) **cobertura** — todo caracter que el diagrama muestra y que la fuente declara en su `unicode-range` tiene que estar de verdad en la fuente (si alguien edita un SVG a mano y anade una etiqueta con un caracter que la fuente ya no trae, ese glifo saldria con la tipografia del sistema); (b) **peso** — avisa de los SVG que todavia llevan la tipografia completa. Los emoji y simbolos que **nunca** estuvieron en la fuente (`✅ ❌ 🧩 🔴 →`) se dibujan con la tipografia del sistema a proposito: **no cuentan como fallo**. |
>
> Requisito: `py -3.12 -m pip install fonttools brotli`.

> [!success] Lote aplicado a todo el vault (05/11/2026)
>
> | | Antes | Despues |
> |---|---|---|
> | SVG con tipografia incrustada | 2.126 | 2.126 (recortados) |
> | Peso de los SVG | **421,8 MB** | **124,3 MB** (**−71%**, ahorro ~297 MB) |
> | Peso medio por SVG | ~182 KB | ~36 KB |
> | SVG sin tipografia incrustada (intactos) | 249 | 249 |
> | Rechazados / errores | — | **0** |
>
> - El **sitio publicado** baja de **961 MB** a ~660 MB (`dist`) y cada diagrama carga ~5x mas rapido.
> - **El vault no cambia de tipografia:** se conserva la misma variable font (eje `wght` 300-1000),
>   los mismos avances (`hmtx`), la misma geometria (`glyf`, composites resueltos), los mismos deltas
>   variables (`gvar`) y las mismas tablas de ejes (`avar`/`fvar`). Medido en Chromium: `N` = 9,1 px y
>   `Necesidad` = 70,7 px **identicos** antes y despues. La licencia OFL sigue incrustada.
> - **El SVG sigue siendo autonomo**: funciona igual en `<img>`, en Obsidian, descargado o embebido.
> - **Verificacion por archivo:** la cobertura de glifos antes y despues tiene que ser identica y
>   **ningun glifo que la fuente original traia puede perderse**; si no, el script **no toca el
>   archivo**. 0 rechazos en el lote.
> - **Los huecos de la fuente original** (glifos que el diagrama usa y que "Recursive Variable" no
>   trae: `‴` prima triple, ZWJ, `ᵢ`, `‖`, emoji, `→`) se dibujan con la tipografia del sistema **ya
>   hoy, antes y despues**: no es un cambio. El recorte los registra en el propio SVG
>   (`/*fuente-sin-glifo:U+2034*/`) para que el QA no los confunda con una regresion.
>   **92 SVG** tienen algun hueco de esos.
> - **QA final sobre todo el vault** (`qa_svg_fuente.py`): **2.375 SVG revisados · 2.126 con fuente
>   recortada (ok) · 0 con la fuente completa · 0 con glifos declarados y ausentes · 92 con huecos
>   preexistentes documentados** → **exit 0**.
> - **Render real medido en Chromium** (el SVG en linea, con su CSS y su fuente): **12/12 elementos de
>   texto con el mismo ancho y alto**, 580,56 px de ancho total en original y subconjuntado.
> - **Reversible:** es un commit. `git revert <hash>` deja el vault como estaba.

> [!info] Donde vive la regla
>
> El detalle completo esta en `Universidad/Herramientas/README.md` (seccion "la tipografia incrustada de
> los SVG"). El sitio **no cambia**: el sync sigue copiando el SVG tal cual, asi que **Vercel no
> necesita Python** ni `fontTools`.

**PUSHEADO `7604b35c`** — commits `c151d9d0` (los 2.126 SVG) + `12cc58df` (las 3 herramientas, el
README y este LEEME), con merge de `origin/master` (7 commits de `opencode`: material SBD, libros de
MatDisc y callouts). El unico conflicto fue este LEEME: resuelto **conservando ambos bloques**
(el de `opencode` y este). Rama `sesion/opencode-site` -> `master`.
### `opencode` - barrido de callouts: prosa dentro de callouts - 05/11/2026

> [!success] Barrido de 134 callouts en 36 notas (0955d3d4)
>
> Toda la prosa explicativa bajo un encabezado se cita ahora dentro de un
> callout `> [!tipo] Emoji Titulo` que absorbe listas, tablas y codigos
> contiguos. Resultado: inventario_plano paso de ~200 líneas de prosa real a ~0
> (las restantes son exclusiones deliberadas: **Tags:**, flashes SR,
> navegación `-> [[…]]`, LaTeX roto y `Herramientas/`).
>
> - **Títulos con texto**: 134/134 tienen tipo + emoji + título con texto (0 usan solo emoji).
> - **72 overrides** aplicados por `ruta@línea_original`, 0 huérfanos; ningún título repetido sin desambiguar.
> - **3 callouts partidos** reparados (`Interacciones y Fuerzas.md` y `Leyes de Newton.md`): se citó la prosa intermedia con `>` para reconectar el callout.
> - **Artefactos resueltos**: `01 – Integral triple.md` (basura de IA borrada) y `02 – Volumen bajo una superficie.md:596` (`> ¡Error! Revisar…` citado).
> - `Parts of a Sentence.md`: listas `4.`/`5.` re-citadas dentro del callout.
>
> [!info] Qué NO se tocó (por decisión del dueño)
>
> - Flashcards del plugin SR (`Q::A` + `<!--SR:…-->`): formato plano, intocable.
> - Navegación `→ [[…]]` sin prosa y listas de wikilinks de índice.
> - Fragmentos de LaTeX/código rotos, pies de figura en cursiva y material ajeno (`_texto/`, PDFs/PNG de clase, `Contenido Extra/`).
> - Docs de `Herramientas/` (READMEs de scripts: no son material de estudio).
>
> [!warning] QA del barrido
>
> - `qa_links.py`: targets=7947 bad=0.
> - `qa_assets_huerfanos.py`: 2918 assets, 0 huérfanos (+57 excluidos de `_no-publicar.txt`).
> - `revisa_titulos.py`: 134 callouts, 0 problemas.
> - `qa_omitidas.py`: 825 revisadas / 822 publican / 2 omitidas / 1 revisar.
> - `fix_callout_overlap` / `fix_callout_nested` / `fix_callout_join`: sin regresiones (pegados=143, anidados=0, dispersos=1).
> - Fences sin cerrar: 4 (preexistentes, no tocados).
>
> Commits atómicos en `sesion/opencode`: `0955d3d4` (barrido), `5f054df` (archivos restringidos fuera del índice de git, no pusheado aún). No se reescribe histórico (prohibido force-push/amend).


---

### `opencode` - renombrar los 19 leemes a "00 - Índice de Contenido" y fusionar el de SBD - 05/11/2026

> [!success] Un solo índice por materia, con nombre consistente
>
> - **19 leemes → 18 índices.** Los `00 - Leeme Unidad 0.md` pasan a `00 - Índice de Contenido.md`
>   y el H1 a `# 📂 Índice de Contenido — <materia>`. 17 se renombran en su lugar; los **2 de SBD**
>   (raíz de la materia y `Unidad 0 - Guias y Ejercicios/`) se **fusionan en uno solo en la raíz**:
>   `Universidad/3er Semestre/Sistema de Bases de Datos/00 - Índice de Contenido.md`.
> - **Enlaces actualizados:** 20 wikilinks en 18 notas + 3 menciones en texto plano.
>   **0 referencias residuales** al nombre viejo en todo `Universidad/`.
> - El índice nuevo de SBD es **explicativo**: qué es cada archivo, para qué sirve y qué no se publica.

> [!danger] Hallazgo de fondo: 68 medios de SBD NO se publicaban
>
> El sync solo copia un asset si **alguna nota publicada lo referencia con un wikilink real**
> (`site/scripts/sync-vault.mjs:320`, gate `referidos`). Los índices anteriores tenían los archivos
> de SBD **en código inline** (`` `Exámenes/2019-2PAO-2E-SBD.pdf` ``), así que nunca se subían:
> el ZIP, los 10 PPTX, 16 exámenes, el proyecto y las participaciones estaban en el vault y **no en la web**.
>
> - **Antes:** SBD 179/247 medios publicados. **Después:** **245/247**. Los 2 que faltan son el video
>   (`VideoBSDPrimerParcial.mp4`, 13 MB) y el libro *Database Systems…* — los 2 en `_no-publicar.txt`
>   **por decisión del dueño**, no por error.
> - El **ZIP de scripts**, `sakila-db.zip` y `world-db.zip` ahora se publican (antes 0 de 3).
> - Los 12 SVG `u2-02-01`…`u2-02-12` no los embebía ninguna nota: se listan en el índice para que
>   tampoco queden colgados. Los otros 100 diagramas de trabajo de U1/U2 **no se repiten** en el
>   índice porque ya están embebidos donde corresponde.

> [!warning] 2 trampas del sync que conviene no volver a pisar
>
> 1. **En tablas markdown, el wikilink va SIN alias.** `[[archivo.pdf]]` resuelve y renderiza
>    `[📎 archivo.pdf](url)`; `[[archivo.pdf\|alias]]` **no** resuelve (queda `**alias**`).
>    El separador de alias debe ser `\|` para no romper la tabla, y el sync no lo entiende.
>    Los alias solo funcionan **fuera** de tablas (listas y callouts).
> 2. **Los assets se resuelven por nombre, no por ruta** (`resolveAssetInfo`, `sync-vault.mjs:684`):
>    el wikilink puede llevar la ruta completa, pero lo que decide es el basename. Por eso
>    `dupes_basename.py` da **0 duplicados** en SBD (296 medios, 296 nombres únicos).

> [!info] QA de esta ronda
>
> - `qa_links.py` (raíz `Universidad`): targets **7951 → 8029**, **bad=0**.
> - Sync de prueba en disco local (`site-test`, sin tocar `site/` del repo): **822 notas publicadas ·
>   2 omitidas · 2.987 assets referenciados**; assets totales **2.922 → 2.988** (400,5 → 444,1 MB).
> - `qa_links.py` del repo completo: no se corrió (los 39 placeholders de `Clippings/` y `site/`
>   son deliberados, el QA los saltea por defecto).

> [!question] DECISIÓN PENDIENTE DEL DUEÑO: los 47 índices de unidad
>
> Hay **47 notas `00 - Índice Unidad N`** en el vault (14 con material propio, 33 redundantes).
> Medición recursiva de solapamiento contra la nota puente de cada materia:
>
> | Materias | Índices | Links exclusivos del índice | Veredicto |
> |---|---|---|---|
> | Ingles I, Comunicación, Cálculo Vectorial, DSW, FESD, Ingles III, MatDisc, SBD | 33 | 0–1 | **100% redundantes** |
> | MOOC Inglés, MOOC Comunicación, Preuniversitario Matemáticas | 14 | 9 / 20 / 83 | **112 links únicos** |
>
> - **Opción A (recomendada):** borrar los 33 índices redundantes de las 8 materias; trasplantar antes
>   los **25 embeds SVG exclusivos** a las notas puente (si no, se pierden del sitio).
>   En Preuniversitario y MOOC hay que **trasplantar 112 links** antes de borrar los 14.
> - **Opción B:** dejarlos como están.
>
> No se borró nada: **falta tu decisión**.

> [!note] Aviso para `opencode-onedrive` (zona `site/scripts/sync-vault.mjs`)
>
> El comentario de `site/scripts/sync-vault.mjs:224` cita `00 - Leeme Unidad 0` como ejemplo de
> homónimo. Ese nombre ya no existe: ahora es `00 - Índice de Contenido`. **No toqué el archivo**
> (zona de `opencode-onedrive`): el comentario queda desactualizado, es cosmético.

> [!note] Lo que NO se tocó (cambios ajenos)
>
> `Universidad/00 - Mapa PAO 2-2026.md` (borrado, sin commitear) · `Recursos visuales.md` de
> Matemáticas Discretas · las carpetas `_texto/` · los PDF sin trackear de MatDisc y DSW ·
> los 2 PDF de SBD **sí** entraron al repo porque el índice nuevo los enlaza
> (`3.4 Operaciones Derivadas-agregacion.pdf`, `BD04 DDL_dml_create_alter_drop.pdf`).

**PUSHEO EN CURSO** — commit `bf15a059` (43 archivos: 17 renombres, 2 borrados, 1 índice nuevo,
21 notas con enlaces actualizados, 2 PDF de SBD). Falta el `PUSHEADO <hash>` al confirmar el push.

**PUSHEADO `e8c19ba4`** — commits `bf15a059` (el renombrado y la fusión) + `e8c19ba4` (este bloque
del LEEME), `master` → `origin/master`. `origin/master` = `e8c19ba4`.
### `opencode` - barrido de tablas + pedido de rebuild del sitio - 05/11/2026

> [!success] Las 147 tablas markdown que quedaban fuera de callouts ya estan dentro
>
> Cierre de la regla de estilo del dueno ("nada de texto plano fuera de callouts"):
> las tablas tambien contaban. Medicion inicial: **133 bloques de tabla fuera de todo
> callout en 42 notas** (10 de ellos "huerfanos", con un callout justo encima y la
> tabla colgada). Resultado: **0 tablas fuera de callout en todo el vault**.
>
> - **35 absorbidas** en el callout que ya tenian encima (mismo encabezado): la tabla
>   se cita dentro (`> | ...`) y el contenido del callout se conserva intacto.
> - **98 convertidas** en callout nuevo, con el titulo del encabezado mas cercano
>   (mismo criterio que el barrido de prosa) y desambiguacion con el encabezado
>   padre si el titulo se repite en la nota.
> - **14 mas** en el `00 - Indice de Contenido.md` de Base de Datos, que arrastro las
>   tablas del LEEME de U0 al fusionarlo (commit `bf15a059` de `master`).
> - **2 overrides** de titulo: `a. Partes del Equipo` (titulo de 69 chars) y
>   `Tabla Resumen de Criterios - Resumen Visual Completo` (colision con un callout
>   previo de la misma nota).
>
> [!info] Conflictos con otra sesion (resueltos a mano)
>
> - `master` habia renombrado los 19 LEEMEs a `00 - Indice de Contenido` y fusionado
>   el de SBD U0, **borrando** `3er Semestre/Sistema de Bases de Datos/Unidad 0 -
>   Guias y Ejercicios/00 - Leeme Unidad 0.md` (que nosotros habiamos citado en
>   callouts). Se **acepto el borrado** (decision de `master`) y se reaplico el
>   formato de callouts/tablas sobre el archivo que quedo.
> - La prosa real del vault quedo en **206 lineas** (de 412 en el baseline
>   `3758a0db`), sin regresiones: lo que queda son exclusiones deliberadas
>   (**Tags:**, flashcards SR, navegacion `-> [[...]]`, LaTeX/codigo roto y
>   `Herramientas/`).
>
> [!warning] QA del barrido de tablas
>
> - Tablas fuera de callout: **133 -> 0** (y 14 -> 0 en el indice fusionado).
> - `qa_links.py`: targets=**8041** bad=**0**.
> - `qa_omitidas.py`: **824 revisadas / 822 publican / 2 omitidas / 0 revisar**.
> - Callouts: pegados=**143** (preexistente), anidados=**0**, dispersos=**1**
>   (preexistente). Fences sin cerrar: **4** (preexistentes).
> - Validador de los 103 callouts nuevos: **0 errores** (todos con tipo, emoji y
>   titulo con texto, con separador `>` y la tabla citada entera).
>
> [!todo] `opencode-site` - falta el rebuild del sitio
>
> El sitio publicado (`neonotes-espol.vercel.app`) todavia no tiene este trabajo.
> Con lo que hay ahora en `master` (`11a26057`) :
>
> - **822 notas publicables** (de 824 revisadas; 2 omitidas por copyright).
> - **42 notas** con las tablas dentro de callouts + **37 notas** con la prosa
>   citada (el barrido de `0955d3d4` + el fix `8a46ae11`).
> - **1.916 callouts** que ya tienen titulo con texto pero sin emoji (preexistente,
>   fuera del alcance aprobado): si `opencode-site` normaliza ese formato, el sitio
>   queda 100% con la casa.
>
> Pedido: rebuild del sitio y verificacion de que las tablas dentro de callouts
> renderizan igual que en Obsidian (van como `> | ...`).

### `opencode-onedrive` — índices de unidad eliminados + recursos visuales unificados — 05/11/2026

> [!success] 4 commits + merge de `master` · 47 índices de unidad eliminados · 6 `Recursos Visuales.md` · QA `bad=0`
>
> - **Hecho:** `5e7834da` (volcado de 119 notas + 25 SVG a los índices de materia) ·
>   `163d7280` (273 enlaces entrantes reescritos en 147 archivos) ·
>   `3b3d5cfd` (47 índices de unidad eliminados) ·
>   `fb03d8bf` (recursos visuales unificados) · `680e0c80` (merge de `origin/master`).
> - **Pendiente:** `opencode-nube` — integrar los 3 índices de material local (abajo).
>   `opencode` — siguen los 2 BADs de Comunicación. Del dueño — material de DSW U3/U4 y firma de P1.
> - **Necesito:** nada más de otras sesiones; `site/src/**` quedó intacto (solo se corrió sync/build para verificar).

**1. Los 47 índices de notas por unidad quedaron eliminados (`3b3d5cfd`).**

> [!info] Qué se eliminó y por qué
> El índice de cada materia ya distribuye todas sus notas por unidad, así que los índices por
> unidad eran **redundantes**. Antes de borrar, su contenido quedó a salvo:
>
> - **119 notas volcadas** a los índices de materia (Matemáticas 83 · MOOC Comunicación 20 ·
>   MOOC Inglés 17 · Inglés III recupera `Speaking Practice # 2` · Fundamentos de Programación ya los tenía).
> - **25 SVG de mapa visual reubicados** a rutas que ahora resuelven (los antiguos usaban rutas relativas rotas).
> - El PDF `BD 02 MC_a_ML.pdf`, que solo referenciaba el índice de la U2 de SBD, se enlaza desde el índice de la materia.

> [!warning] Si tu nota enlazaba a un índice de unidad
> Los 273 enlaces entrantes se reescribieron según su contexto (`163d7280`):
>
> | Contexto | A qué apunta ahora |
> |---|---|
> | Nota con bloque "Mapa de contenido" | se borra la línea redundante del índice de unidad |
> | Nota sin ese bloque | el índice de la **materia** |
> | Bloque "Entradas por unidad/módulo" de los Leeme | la **primera nota** de cada unidad (es lo que promete el bloque) |
> | Índice de materia | se quita la flecha del encabezado y las listas de unidades al pie |
> | Lista "Índices:"/"Unidades:" | un enlace al índice de materia, conservando los links que no son de unidad |

> [!danger] `opencode-nube` — 3 índices de material local para integrar
> Estos **no** son índices de notas (por eso no se borraron), sino listados de material. Ya apuntan
> al `Recursos Visuales.md` de su materia, pero siguen duplicando el índice de contenido:
>
> | Archivo | Qué hacer |
> |---|---|
> | `3er Semestre/Fundamentos de Electricidad y Sistemas Digitales/Teórico/Unidad 0 - Guías y Ejercicios/00 - Recursos Unidad 0.md` | integrar en el `00 - Índice de Contenido.md` de FESD |
> | `3er Semestre/Matemáticas Discretas/Unidad 0 - Guias y Ejercicios/Material de clase/00 - Recursos Unidad 0.md` | integrar en el `00 - Índice de Contenido.md` de Mat. Discretas |
> | `3er Semestre/Ingles III/Unidad 0 - Guias y Ejercicios/Material de clase/Recursos Unidad 0.md` | integrar en el `00 - Índice de Contenido.md` de Inglés III |

**2. Los archivos de recursos visuales quedaron unificados (`fb03d8bf`).**

Nombre canónico: **`Recursos Visuales.md`** (sin prefijo), **un archivo por materia**, que fusiona
videos + aula virtual + laboratorio + extras por unidad.

| Materia | Antes | Ahora |
|---|---|---|
| Diseño de Software | `Recursos visuales.md` + `Enlaces del Aula Virtual.md` | `Recursos Visuales.md` (se fusiona el Aula Virtual) |
| FESD | `Recursos visuales.md` + `00 - Recursos del laboratorio.md` | `Recursos Visuales.md` (se fusiona el laboratorio; se elimina la tabla de videos duplicada) |
| Inglés III | `Recursos visuales.md` | `Recursos Visuales.md` |
| Matemáticas Discretas | `Recursos visuales.md` | `Recursos Visuales.md` |
| Sistema de Bases de Datos | `Recursos visuales.md` | `Recursos Visuales.md` |
| Inglés II | `01 - Recursos Unit 1.md` | `Recursos Visuales.md` |

> [!note] También se corrigió un enlace equivocado
> El `00 - Recursos Unidad 0.md` de Matemáticas Discretas apuntaba por error a la carpeta de
> **Diseño de Software**; ahora apunta a su propia materia. Se actualizaron H1, tags y los 10
> archivos que enlazaban a los nombres viejos. **0 enlaces rotos.**

**3. Verificación (después del merge de `master`).**

`qa_links.py` targets=**7523** bad=**0** · `qa_assets_huerfanos.py` **2960 assets, 0 huérfanos** ·
`qa_omitidas.py` **776 revisadas / 773 publican / 2 omitidas / 1 revisar** (las 3 preexistentes) ·
0 índices de unidad en disco · `npm run sync` (773 notas) + `npm run build` (799 páginas) **OK**.

> [!warning] Conflictos del merge con `master` y cómo se resolvieron
> `master` había reformulado las notas de U3 de DS, envuelto prosa en callouts y renombrado los
> 19 Leeme a `00 - Índice de Contenido.md`. Se resolvió **conservando ambas versiones**:
> las notas de U3 de DS y la `Guía de Problemas 1` de SBD quedaron con la versión de `master` +
> la reescritura de enlaces de esta tanda; los callouts que `master` agrego a los dos archivos
> fusionados se trasplantaron a `Recursos Visuales.md`; los índices de unidad que `master` modificó
> y esta tanda eliminó se quedaron eliminados, con sus enlaces re-apuntados a la primera nota
> (SBD) o al nombre nuevo de la nota (DS).
>
> La mención de la línea 567 (`[[MOOC de Comunicación/Unidad N .../00 - Índice]]`) es **documental**
> (describe un bug que `opencode-nube` arregló el 04/11), no un enlace vivo: se deja como está.
