---
dg-publish: false
tags: [clippings, log, opencode-onedrive, publicacion, calidad, vault]
---

# LOG - opencode-onedrive (sesiÃ³n 2026-10-27)

> [!info] ðŸ“Œ Alcance de esta sesiÃ³n
> SesiÃ³n de **higiene de publicaciÃ³n del vault**. No es la sesiÃ³n de links
> rotos (`LOG-opencode.md`), ni la del sitio/marca (`LOG-opencode-site.md`), ni
> la de nube (`LOG-opencode-nube.md`).
> **Zona que reservÃ©:** `Universidad/2do Semestre/CÃ¡lculo Vectorial/**`,
> `site/scripts/sync-vault.mjs`, `site/RUNBOOK.md`,
> `site/docs/HISTORIAL-LANZAMIENTO.md`, `Universidad/Herramientas/SVGs por recrear.md`.
> **Commits:** todos en `master` y **pusheados** a `origin/master` (ver tabla abajo).

> [!info] ðŸ“‘ Ãndice
>
> - [[#1. QuÃ© hice, en orden]]
> - [[#2. Commits de esta sesiÃ³n]]
> - [[#3. Propuestas]]
> - [[#4. Lo que necesito]]
> - [[#5. Acuerdo entre las 4 sesiones (cierre del 27/10/2026)]]
> - [[#5-bis. QuÃ© me falta a mÃ­ (resumen corto; el detalle en el tablero)]]
> - [[#6. Estado al cierre]]
> - [[#1.1 Sistema de publicaciÃ³n (lo que sostiene todo lo demÃ¡s)]]
> - [[#1.2 CÃ¡lculo Vectorial (mi zona)]]
> - [[#1.3 Copyright]]
> - [[#1.4 DocumentaciÃ³n]]
> - [[#1.5 IntegraciÃ³n entre sesiones (lo que mÃ¡s tiempo consumiÃ³)]]
> - [[#P1 â€” Un `git worktree` por sesiÃ³n (arregla la carrera entre agentes)]]
> - [[#P2 â€” Lista blanca para el material con copyright (decisiÃ³n del usuario)]]
> - [[#P3 â€” VerificaciÃ³n de publications en CI (que no se repita la fuga)]]
> - [[#P4 â€” Que el embed roto se detecte antes de publicar]]
> - [[#P5 â€” Sacar `site/` del vault (resuelve la cuota sin migrar nada)]]
> - [[#P6 â€” Parametrizar las rutas absolutas antes de migrar]]
> - [[#P7 â€” Limpiar los 32 PNG huÃ©rfanos de `Universidad/Figuras/`]]
> - [[#P8 â€” Arreglar los `verificar_nota.py` que fallan en CÃ¡lculo Vectorial]]

## 1. QuÃ© hice, en orden

### 1.1 Sistema de publicaciÃ³n (lo que sostiene todo lo demÃ¡s)

> [!tip] ðŸ”§ Regla final implementada en `sync-vault.mjs`
>
> Regla final implementada en `site/scripts/sync-vault.mjs`:

> [!info] ðŸ“‹ Reglas del sistema de publicaciÃ³n
>
> | Regla | QuÃ© hace | Por quÃ© |
> |---|---|---|
> | Gate `dg-publish` | Solo se publica una nota con `dg-publish: true` | El vault tiene material de clase y libros que no van al sitio |
> | `Universidad/_no-publicar.txt` | Lista con comodines `*` y `?`, coincidencia por **nombre o ruta** | Material con copyright que sÃ­ vive en el vault pero no se distribuye |
> | Solo assets referenciados | Un archivo se copia a `public/` **solo si** alguna nota publicada lo referencia | Evita subir capturas y PDFs huÃ©rfanos |
> | Fix de embeds | `![[Nota]]` sin extensiÃ³n de media â†’ `[[Nota]]` | Evita que un enlace a nota se convierta en asset roto |
> | Marcador `<!-- nx:asset-omitido -->` | Se deja constancia en la nota de quÃ© se excluyÃ³ y por quÃ© | Para que nadie piense que el archivo se perdiÃ³ |

> [!success] âœ… NÃºmeros verificados tras el merge
>
> **NÃºmeros verificados tras el merge** (`npm run sync`): 805 notas publicadas Â·
> 3 omitidas Â· 2777 assets referenciados Â· 17 patrones / 61 archivos excluidos Â·
> 831 pÃ¡ginas en `npm run build`.

### 1.2 CÃ¡lculo Vectorial (mi zona)

> [!success] âœ… QuÃ© hice, en orden
>
> - 16 diagramas que eran *placeholders* ("Concepto clave / DefiniciÃ³n formal")
> sustituidos por las versiones con contenido real, con los embeds actualizados.
> - 2 diagramas "Teorema Fundamental de LÃ­nea" corregidos: tenÃ­an contenido de
> "Distancias en RÂ³" (copia de otro diagrama).
> - 37 diagramas maestros huÃ©rfanos integrados en sus 32 notas (insertados tras
> el primer callout de intro) â†’ **0 embeds de diagramas rotos** en todo el vault.
> - Borrados: `test.svg` del pipeline, 9 SVG superados, 2 duplicados exactos de
> `Figuras/`, `Tarea 2.md` + su PNG, `04_-_Propiedades_de_las_Operaciones_01_temp.svg`.
> - 332 previews de `SVG-Pipeline/previews/` borrados (12,7 MB) + regla `previews/`
> en `.gitignore`.
> - `Universidad/Herramientas/SVGs por recrear.md` regenerada: 474 entradas
> obsoletas â†’ **0**.

### 1.3 Copyright

> [!success] âœ… Fuga real cerrada
>
> - **Fuga real cerrada:** `Escucha Activa Parte 1/2_OCR.pdf` **se estaban
> publicando** (el patrÃ³n no cubrÃ­a el sufijo `_OCR`). Ahora estÃ¡n en
> `_no-publicar.txt`.
> - `Universidad/_no-publicar.txt` quedÃ³ como **uniÃ³n** de las listas de dos
> sesiones (17 patrones): libros `z-lib.org`, Cambridge (`Empower*.pdf`,
> `CAMBRIDGE ONE_GUIDE...`), UML Stevens, Refactoring, Pressman, Clean
> Architecture, Johnsonbaugh, Rosen, el `.wmv` de dinÃ¡micas y los derivados
> `_OCR` de Escucha Activa.

### 1.4 DocumentaciÃ³n

> [!success] âœ… DocumentaciÃ³n y reglas
>
> - `site/RUNBOOK.md`: nueva secciÃ³n "QuÃ© se publica (notas y archivos)" +
> renumerado + "Notas omitidas" con el marcador `nx:asset-omitido`.
> - `site/docs/HISTORIAL-LANZAMIENTO.md`: estadÃ­sticas reales (805 / 3 / 831 /
> 2745 assets) y decisiones 1-9.
> - `Clippings/00 - LEEME bandeja de pistas.md`: protocolo multi-agente (claim por
> rename `PISTA - <tema> [EN-PROCESO <agente>].md`, bitÃ¡cora por agente, stage por
> rutas exactas, nunca `git add -A`) y secciÃ³n "Progreso de los agentes" con la
> entrada de cada sesiÃ³n.

### 1.5 IntegraciÃ³n entre sesiones (lo que mÃ¡s tiempo consumiÃ³)

> [!note] ðŸ§­ Hubo tres sesiones en el mismo vault
>
> Hubo **tres sesiones** trabajando en el mismo vault y el mismo remoto:

> [!note] ðŸ§­ QuiÃ©n trabaja en quÃ©
>
> | SesiÃ³n | Zona | BitÃ¡cora |
> |---|---|---|
> | `opencode` (3er Semestre) | links rotos, `Herramientas/Mantenimiento/**` | `LOG-opencode.md` |
> | `opencode-site` (clon Desktop) | estilos, marca, visor PDF, exclusiones | `LOG-opencode-site.md` |
> | `opencode-nube` | decisiÃ³n de migraciÃ³n de nube | `LOG-opencode-nube.md` |
> | `opencode-onedrive` (esta) | reglas de publicaciÃ³n + CÃ¡lculo Vectorial | este archivo |

> [!note] ðŸ“‹ Lo que hubo que resolver
>
> Lo que hubo que resolver:

> [!info] ðŸ“‹ Conflictos resueltos
>
> 1. **El remoto (`origin/master`) y el local tenÃ­an dos implementaciones
> distintas de `_no-publicar.txt`.** Se integraron en **una sola** en
> `sync-vault.mjs`: la de la otra sesiÃ³n (`leerNoPublicar`/`coincideNoPublicar`,
> exportadas) + la mÃ­a (`globToRegex` con comodines, coincidencia por ruta y
> la pre-pasada de assets referenciados).
> 2. **Los PDFs de FESD y MatemÃ¡ticas Discretas**: ganÃ³ la layout **local** con
> subcarpetas (`Diapositivas/`, `GuÃ­as/`, `Talleres/`, `Lecciones/`,
> `ExÃ¡menes/`) y se borraron las copias planas duplicadas del remoto.
> 3. **Causa raÃ­z del ruido CRLF (la encontrÃ© midiendo, no adivinando):** 82 `.md`
> de `Preuniversitario/MatemÃ¡ticas` tenÃ­an **CRLF dentro del blob commiteado**.
> Como `.gitattributes` dice `*.md text eol=lf`, git los marcaba como
> modificados aunque el contenido fuera idÃ©ntico â†’ **todos los merges fallaban**
> con `Your local changes would be overwritten by merge`. Se normalizÃ³ solo el
> fin de lÃ­nea (`a05dfa4`) y los merges volvieron a funcionar.
> 4. **Un merge sobrescribiÃ³ trabajo sin commitear de otra sesiÃ³n** (nota de
> InglÃ©s III, nota de BD y `qa_links.py`). Se recuperÃ³ desde el commit del
> stash descartado (`ea525f6`) y se confirmÃ³ que el merge final traÃ­a esa
> misma versiÃ³n.

## 2. Commits de esta sesiÃ³n

> [!success] âœ… Commits de esta sesiÃ³n
>
> | Commit | QuÃ© |
> |---|---|
> | `374e833` | `site/scripts/sync-vault.mjs`: publicar solo assets referenciados + `_no-publicar.txt` + `.gitignore` + borrados |
> | `5aded86` | `Clippings/00 - LEEME bandeja de pistas.md`: protocolo multi-agente |
> | `67ed5ac` | `Universidad/Herramientas/SVGs por recrear.md` regenerada |
> | `462191b` | `2do Semestre/CÃ¡lculo Vectorial`: 37 diagramas maestros integrados |
> | `6a41cf9` | `site/RUNBOOK.md` + `site/docs/HISTORIAL-LANZAMIENTO.md` |
> | `d45c240` | `_no-publicar.txt`: derivados `_OCR` de Escucha Activa |
> | `ca4ab56`, `99d8c22`, `17df803`, `ef26d75`, `8fedc9f` | merges con el clon Desktop |
> | `a05dfa4` | normalizar fin de lÃ­nea de 82 `.md` (desbloquea los merges) |
> | `544ba11` | responder en el LEEME las preguntas de `opencode-site` |

## 3. Propuestas

### P1 â€” Un `git worktree` por sesiÃ³n (arregla la carrera entre agentes)

> [!tip] ðŸ—‚ï¸ Un solo directorio de trabajo
>
> Hoy las tres sesiones comparten **el mismo directorio de trabajo y el mismo
> remoto**. Consecuencia medida: un merge sobrescribiÃ³ cambios sin commitear de
> otro agente. Propuesta: cada sesiÃ³n trabaja en su propio
> `git worktree` (rama propia) y **solo una** integra a `master`.

> [!example] ðŸ’» Crear el worktree por sesiÃ³n
>
> ```bash
> git -C "C:/Users/Steven SÃ nchez/OneDrive/OneSyncFiles" worktree add ../wt-links -b sesion/links master
> ```

> [!success] âœ… Ventajas
>
> Ventajas: nadie pisa a nadie, los merges se hacen una vez al final, y el
> `git status` de cada sesiÃ³n es limpio.

### P2 â€” Lista blanca para el material con copyright (decisiÃ³n del usuario)

> [!warning] âš ï¸ `_no-publicar.txt` es una lista negra
>
> `_no-publicar.txt` es una **lista negra**: si se olvida un archivo, se publica.
> Propuesta: invertirla â€” un `Universidad/_publicar.txt` explÃ­cito, o mover el
> material con copyright a `Universidad/_privado/` (carpeta que el sync ignora por
> estructura, no por nombre). Es mÃ¡s difÃ­cil que se escape algo.

> [!success] âœ… Lo que ya estÃ¡ protegido
>
> Mientras tanto, lo que **ya estÃ¡ protegido**: 17 patrones, 61 archivos.

### P3 — Verificación de publications en CI (que no se repita la fuga) ✅ IMPLEMENTADO

> [!success] 🚀 Implementado y pusheado (commit `1233551`, master = origin/master)
>
> Se crearon tres piezas que en conjunto forman la red de seguridad contra
> fugas de copyright (material de `Escucha Activa Parte 1_OCR.pdf` y similares):
>
> | Pieza | Archivo | Qué hace |
> |---|---|---|
> | Verificación en el sync | `site/scripts/sync-vault.mjs` | `verificarNoPublicados()` al final de `main()` recorre `public/assets/` y lanza error si encuentra un archivo excluido por `_no-publicar.txt`. |
> | Script standalone de CI | `site/scripts/ci-check-privado.mjs` | Verifica `public/assets/` y `public/downloads/*.zip` contra los patrones de `_no-publicar.txt`. Sale con código != 0 si hay fuga. |
> | Workflow de GitHub Actions | `.github/workflows/ci-privacy.yml` | Corre en push y PR a `master`: `npm ci` + `sync` (`VAULT_DIR=../Universidad`) + `build` + `ci-check-privado.mjs`. Falla si hay fuga. |
>
> Convenciones: `globToRegex` igual que `sync-vault.mjs` (`*` y `?`), match por
> nombre y ruta relativa, case-insensitive. Los scripts ya existentes
> (`qa_fugas_copyright.py`, `qa_all.py`) siguen disponibles para uso local.
>
> **Nota:** `opencode-site` es dueña de `site/src/**` y `site/public/**`; este cambio toca solo `site/scripts/` (zona de `opencode-onedrive`, acordada en el tablero). Se avisó antes de tocar.


### P4 â€” Que el embed roto se detecte antes de publicar

> [!tip] ðŸ›¡ï¸ Scripts de auditorÃ­a que ya existen
>
> Existen ya `qa_links.py` y `verificar_nota.py` en `Universidad/Herramientas/`.
> Propuesta: mover ahÃ­ mis scripts de auditorÃ­a (estÃ¡n en
> `C:\Users\STEVEN~1\AppData\Local\Temp\opencode\`) y dejar **una sola** entrada
> que corra todo:

> [!tip] ðŸ” Scripts de auditorÃ­a propuestos
>
> | Script | QuÃ© detecta |
> |---|---|
> | `qa_resolucion_diagramas.py` | embeds de diagramas cuyo archivo no existe |
> | `qa_assets_huerfanos.py` | assets en el vault que ninguna nota referencia |
> | `qa_fugas_copyright.py` | archivos con copyright que sÃ­ se publicarÃ­an |
> | `qa_svg_titulo.py` | SVG placeholder ("Concepto clave") que quedÃ³ sin sustituir |

### P5 â€” Sacar `site/` del vault (resuelve la cuota sin migrar nada)

> [!info] ðŸ“Š `site/` pesa 1,83 GB
>
> `site/` pesa **1,83 GB** dentro del vault y es **todo regenerable**
> (`node_modules` 211 MB, `dist` 874 MB, `public/assets` 649 MB,
> `public/downloads` 74 MB). El RUNBOOK ya dice que no deberÃ­a vivir ahÃ­.
> Sacarlo **libera 1,83 GB de la cuota personal sin tocar la nube institucional**
> y elimina de raÃ­z la ambigÃ¼edad de "dos clones".

> [!info] ðŸ“Š `.git/` pesa 1,50 GB
>
> Relacionado: `.git/` pesa 1,50 GB con un pack de 546 MB y hay un
> `.git/gc.pid` de un `git gc` interrumpido â†’ un `git gc --aggressive` local
> compactarÃ­a bastante.

### P6 â€” Parametrizar las rutas absolutas antes de migrar

> [!warning] âš ï¸ 15+ archivos con rutas hardcodeadas
>
> Hay **15+ archivos** con rutas hardcodeadas a
> `C:\Users\Steven SÃ nchez\OneDrive\OneSyncFiles` (lista completa en
> `PISTA - migracion vault a OneDrive institucional.md`). Si el vault se mueve a
> `OneDrive - <OrganizaciÃ³n>`, todos se rompen. Propuesta: una sola variable de
> entorno (`VAULT_ROOT`) con fallback a la ruta actual, leÃ­da por los ~12
> scripts Python de `Universidad/Herramientas/` y por `sync-vault.mjs`.

### P7 â€” Limpiar los 32 PNG huÃ©rfanos de `Universidad/Figuras/`

> [!info] ðŸ—‚ï¸ Material en curso de MatemÃ¡ticas Discretas
>
> Son material en curso de **MatemÃ¡ticas Discretas** (`01-cardinalidad.png`,
> `05-de-morgan.png`, `09-hasse.png`, `U3-*`, `U5-cubo.png`â€¦). Con la regla "solo assets referenciados" **no llegan
> al sitio**, pero siguen ocupando sitio en el vault. Propuesta: moverlos a la
> carpeta de la unidad que los usa cuando se integren en las notas, o borrarlos
> si ya no sirven.

### P8 â€” Arreglar los `verificar_nota.py` que fallan en CÃ¡lculo Vectorial

> [!warning] âš ï¸ Fences vacÃ­os en las notas de CV
>
> Quedaron vacÃ­as dentro de fences en callouts de las notas de CV (las reporta
> `Universidad/Herramientas/Reportes/qa_refs_checkbox_2026-10-26.md`). Son de mi
> zona; los arreglo en una pasada propia si me das luz verde.

## 4. Lo que necesito

> [!question] â“ Lo que necesito (del usuario y de las sesiones)
>
> - **Del usuario:** decidir P2 (lista negra vs lista blanca), P5 (sacar `site/`
> del vault) y responder si el material con copyright puede vivir en la cuenta
> institucional.
> - **De `opencode-site`:** ya estÃ¡ resuelto (no tocar `sync-vault.mjs` sin
> avisar; `_no-publicar.txt` no se vuelve a tocar sin avisar).
> - **De `opencode` (3er Semestre):** nada pendiente de mi parte; su trabajo
> (nota de BD + `qa_links.py`) quedÃ³ commiteado.
> - **De `opencode-nube`:** P5 y P6 tocan su pista; lo dejo decidir a esa sesiÃ³n
> y al usuario, y por eso no muevo nada.

## 5. Acuerdo entre las 4 sesiones (cierre del 27/10/2026)

> [!success] âœ… Las 4 sesiones firman el mismo acuerdo
>
> Las 4 sesiones que.conviven en este vault **firmaron el mismo acuerdo** en
> `Clippings/00 - LEEME bandeja de pistas.md`:

> [!success] ðŸ¤ Las 4 sesiones y su zona
>
> | SesiÃ³n | Zona | Firma |
> |---|---|---|
> | `opencode-site` (Desktop) | `site/src/**`, `site/public/**` (marca), `site/RUNBOOK.md` Â§2/Â§8, `_no-publicar.txt` + 3 notas | âœ… |
> | `opencode-onedrive` (esta) | `2do Semestre/CÃ¡lculo Vectorial/**`, `site/scripts/sync-vault.mjs`, `site/RUNBOOK.md`, `site/docs/**`, `SVGs por recrear.md` | âœ… |
> | `opencode` (3er Semestre) | `3er Semestre/**`, `Herramientas/Mantenimiento/**` | âœ… |
> | `opencode-nube` | solo `Clippings/` (bitÃ¡cora + PISTA) | âœ… |

> [!note] ðŸ“‹ Acuerdos 1â€“4 (resumen)
>
> **Acuerdos 1â€“4 (resumen):**

> [!success] âœ… Los 4 acuerdos en detalle
>
> 1. **Inventario de commits pendientes** con dueÃ±o y orden (cola de push).
> 2. **Candado de push:** un push a la vez, **anunciado** en la bandeja
> (`PUSHEO EN CURSO Â· <rama> Â· <quÃ©> Â· ~3 min` â†’ `PUSHEADO <hash>`); si el
> push falla, se vuelve al paso 2 en vez de reintentar a ciegas; prohibido
> `--force`, `commit --amend` de algo publicado, `reset --hard` ajeno y
> `git add -A`.
> 3. **Una sola copia editable por ruta:** `site/**` en Desktop, `Universidad/**`
> en OneDrive, y el que necesita la ruta del otro **avisa y no edita**.
> 4. **MigraciÃ³n a OneDrive institucional: no es necesaria.** Solo 1,11 GB de
> los 4,99 GB son contenido real; lo demÃ¡s es regenerable o ya estÃ¡ en
> GitHub. El deploy no depende de la nube local (Vercel compila desde GitHub).

> [!note] ðŸ“‹ Correcciones que aportÃ© al acuerdo
>
> **Correcciones que aportÃ© al acuerdo:**

> [!warning] âš ï¸ CorrecciÃ³n de la tabla de zonas
>
> - La tabla de zonas atribuÃ­a a `opencode-onedrive` la zona de `3er Semestre`
> (que es de la sesiÃ³n `opencode`) y faltaba la cuarta sesiÃ³n.
> - Reglas 8 y 9: **commitear antes de que otra sesiÃ³n mergee** (un merge pisa
> lo que estÃ© sin commitear: pasÃ³ 3 veces) y **un `git worktree` por sesiÃ³n**.
> - **Cola de push** con dueÃ±o, orden y quÃ© archivo es de quiÃ©n.
> - **Refinamiento de la limpieza de cuota**: en el clon OneDrive se borra **solo
> lo generado** (`node_modules`, `dist`, `public/assets`, `public/downloads`);
> el cÃ³digo versionado de `site/` se queda, y `.git/` no se toca sin aviso.

> [!warning] âš ï¸ Hallazgo nuevo: `node_modules` se vaciÃ³ solo
>
> **Hallazgo nuevo (importante):** el `node_modules` del clon OneDrive **se vaciÃ³
> solo** durante la sesiÃ³n (211 MB â†’ 25 MB, sin `astro` ni `.bin`) y un `npm ci`
> de reposiciÃ³n quedÃ³ a medias (faltaba `yargs-parser/index.js`). No lo rompiÃ³
> nadie: **OneDrive escribe/deshidrata sobre los archivos mientras npm los
> escribe**. Consecuencia directa:

> [!tip] ðŸ’¡ Verificar el build en un worktree local
>
> - La verificaciÃ³n del build se tuvo que hacer en un **worktree en disco local**
> (`wt-build`), no en el clon de OneDrive.
> - **`node_modules` no debe vivir nunca dentro de una carpeta sincronizada**, y
> el cÃ³digo del sitio tampoco.

> [!success] âœ… VerificaciÃ³n del estado integrado
>
> **VerificaciÃ³n del estado integrado** (worktree local `wt-build`):
> `npm run sync` â†’ 806 publicadas Â· 3 omitidas Â· 2783 assets referenciados Â·
> 17 patrones / 61 archivos excluidos; `npm run build` â†’ 832 pÃ¡ginas, 0 errores.

## 5-bis. QuÃ© me falta a mÃ­ (resumen corto; el detalle en el tablero)

> [!warning] â³ QuÃ© me falta a mÃ­
>
> | # | QuÃ© | Prioridad | Depende de |
> |---|---|---|---|
> | 1 | **P8**: arreglar `verificar_nota.py` en CÃ¡lculo Vectorial (lÃ­neas vacÃ­as en fences dentro de callouts) | media | nada (mi zona) |
> | 2 | **P4**: mover mis 4 scripts de auditorÃ­a a `Universidad/Herramientas/Mantenimiento/` + una entrada Ãºnica | media | nada |
> | 3 | **P3**: CI que falle si algo de `_no-publicar.txt` llega a `public/` o a un ZIP | media | usuario (Â¿CI?) |
> | 4 | **P6**: `VAULT_ROOT` en los 15+ archivos con ruta absoluta | media | nada (antes de migrar) |
> | 5 | **P2**: lista blanca o `Universidad/_privado/` en vez de lista negra | media | **usuario** |
> | 6 | **P1**: `git worktree` por sesiÃ³n como estÃ¡ndar | baja | sesiones |
> | 7 | **P7**: 32 PNG huÃ©rfanos de `Universidad/Figuras/` | baja | sesiÃ³n del 3er Semestre |
> | 8 | **Cuota**: vaciar la papelera, mover el backup de 458 MB y fijar el vault | alta | **usuario** |

> [!note] ðŸ§­ Tablero completo (las 4 sesiones)
>
> **Tablero completo (las 4 sesiones):** `Clippings/ESTADO - las 4 sesiones.md`.

## 6. Estado al cierre

> [!success] âœ… Estado al cierre
>
> - `master` = `origin/master` (0/0), sin conflictos pendientes.
> - `npm run sync` â†’ 805 publicadas Â· 3 omitidas Â· 2777 assets Â· 17 patrones.
> - `npm run build` â†’ 831 pÃ¡ginas, sin errores.
> - Working tree limpio, salvo lo que pertenece a otras sesiones.

---
---

## 7. Taxonomía Unidad 0 en Cálculo Vectorial — 30/10/2026 (tarea del LEEME)

> [!success] ✅ Tarea asignada por `opencode` y cerrada (hash `b9de5b7`)
>
> `opencode` aplicó la taxonomía Unidad 0 a 16 materias y me dejó a mi **Cálculo Vectorial** en el LEEME: crear `Unidad 0 - Guias y Ejercicios/` con las 8 subcarpetas estándar, mover los 3 archivos de raíz y unir `Diagramas/` a `U0/Diagramas/`.

### Lo ejecutado

> [!info] 📦 Cambios (todo en `Universidad/2do Semestre/Cálculo Vectorial/**`)
>
> - `Unidad 0 - Guias y Ejercicios/` con `Diagramas/`, `Diapositivas/`, `Exámenes/`, `Figuras/`, `Guías/`, `Lecciones/`, `Material de clase/`, `Talleres/` + `00 - Leeme Unidad 0.md` (`dg-publish: true`, tags `MATG1046`).
> - `Diagramas/` de raíz (563 SVG) → `U0/Diagramas/`.
> - `Bienvenida y Syllabus Calculo Vectorial.md` y `SPA-SyllabusEUR_ACE-MATG1046.pdf` → `Guías/`; `Cálculo Vectorial.md` → `Material de clase/`.
> - Links sin reescribir: los 563 `[[Diagramas/…]]` resuelven por basename (mismo criterio que las 15 materias de `opencode`).

### Verificación

> [!tip] 🔍 Números medidos
>
> - `qa_links.py` (root=`Universidad`): `targets=8056 bad=852` — **0 regresiones** vs el verdict de `opencode` (854 → 852 por sus 2 fixes) y **0 BADs a media** en todo el vault.
> - Regla P8 sobre las 92 notas de mi zona: **0 líneas vacías dentro de fences, 0 fences sin cierre**.
> - Las 12 notas de CV que tocó la Pasada 1 de `opencode-nube` (`a2be225`): diff con `--ignore-all-space` **vacío** → solo fines de línea, contenido intacto.

### Incidente: mi trabajo quedó dentro del commit de otra sesión (`b9de5b7`)

> [!warning] ⚠️ Cómo pasó y cómo quedó
>
> En el clon compartido de OneDrive, mis 566 renombres quedaron **staged** mientras `opencode` commiteaba su PUSHEADO: su commit `b9de5b7` arrastró **568 archivos** (567 de mi zona + su LEEME) bajo su mensaje. Contenido **byte-idéntico**, 0 pérdidas, sin `--force`. `opencode` lo avisó y corrigió en `4c78ae9`. **Decisión:** acepto `b9de5b7` como el commit de mi taxonomía (autoría documentada acá y en el LEEME; no hago commit vacío). **Lección para P1:** en un clon compartido, el trabajo propio debe commitearse en cuanto se termina — un worktree por sesión lo evita.

### Pendientes míos tras el cierre

> [!question] ❓ Lo que sigue
>
> - Rebuild del sitio con `opencode-site` (assets por basename → sin cambios de rutas).
> - P1 (worktree por sesión) gana prioridad tras el incidente de staging.
> - P2, P7 siguen esperando decisión/coordinación.

---
**Tags:** #clippings #log #opencode-onedrive #publicacion #calidad #vault
