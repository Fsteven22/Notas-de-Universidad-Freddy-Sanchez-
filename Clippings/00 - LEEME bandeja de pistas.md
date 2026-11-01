---
dg-publish: false
tags: [clippings, protocolo, coordinacion, fuente-unica]
---

# LEEME — bandeja única de las 4 sesiones

> [!important] Regla del dueño del vault (01/11/2026)
> Este archivo es la **única fuente de verdad**. Los demás documentos de `Clippings/`
> (PISTAs, PROPUESTAS, REPORTE, CRUCE, INTAKE, ESTADO, PROBLEMA) **se borraron** el
> 01/11/2026: con tantos archivos las sesiones quedaban con **mentes dispersas** y
> reportaban como pendientes cosas ya hechas. Cada sesión mantiene **su**
> `LOG-<agente>.md` con lo vivo; el detalle histórico queda en git.
> **Antes de decir que algo falta, medirlo**: los BADs y las notas se miden, no se recuerdan.

## Protocolo (lo vigente, corto)

> [!tip] 8 reglas
>
> 1. **Un push a la vez**: avisar `PUSHEO EN CURSO · master · <qué> · ~N min` aquí, y
>    `PUSHEADO <hash>` al terminar, con `origin/master = master` y turno libre.
> 2. **`git add --` de rutas exactas propias**; nunca `git add -A` ni `commit -a`.
>    Antes de commitear: `git diff --cached --stat` y confirmar que solo hay rutas propias.
> 3. **Push**: `git show --stat HEAD` · `git push origin HEAD:master`.
> 4. **Prohibido**: `--force` sobre `master` o historia compartida, `amend` de lo ya
>    publicado, `reset --hard` ajeno. Un force sobre la **rama propia** se permite y se avisa.
> 5. **Worktree por sesión (P1, firmado por las 4)**: cada una en su branch
>    `sesion/<agente>`, **fuera de OneDrive** (OneDrive rehidrata CRLF y revierte lo no commiteado).
> 6. **Hook `pre-commit`**: **no se hereda entre clones distintos** (vive en `.git/hooks/`).
>    Copiarlo una vez por clon y probarlo con un commit descartable.
> 7. **Zona ajena**: avisar aquí primero y esperar confirmación.
> 8. **EOL**: el sitio lee **del disco**, no del commit. Si OneDrive rehidrató CRLF,
>    verificar antes de `sync`/build, o compilar desde el clon Desktop.

## Zonas

| Sesión | Zona que puede tocar |
|---|---|
| `opencode-site` (esta) | `site/**`, `Universidad/**/Diagramas/`, `Herramientas/SVG-Pipeline/`, y **calidad de lo publicado** (sync, build, deploy) |
| `opencode` | `Universidad/3er Semestre/**` (notas, figuras, embeds, wikilinks) |
| `opencode-onedrive` | `Universidad/Herramientas/**` (qa, scripts), `2do Semestre/Cálculo Vectorial/**`, reglas de publicación |
| `opencode-nube` | infraestructura y nube, formato (EOL/frontmatter), carril D1 (ingesta de material nuevo) |

## Estado real medido (01/11/2026)

> [!info] Cifras verificadas por `opencode-site` (no recuerdos: mediciones)
>
> | Qué | Valor |
> |---|---|
> | Sitio | **821 notas publicadas · 3 omitidas · 2849 assets · 17 patrones / 59 archivos excluidos** |
> | Build | **847 páginas**, 0 errores |
> | Deploy | HTTP 200 (`neonotes-espol.vercel.app`) |
> | Links, root `Universidad/**` | **BAD 0** |
> | Links, root repo completo | **160** (ninguno en `Universidad/**`): ver pendiente 2 |
> | EOL / BOM | **0 `.md`** con BOM · `*.md text eol=lf` vigente |
>
> **Las 3 omitidas** (deliberadas): los 2 libros de inglés III con copyright y
> `raiz/General/00 - Mapa PAO 2-2026.md`.

## Qué hizo cada sesión (cerrado, verificado)

> [!success] Resumen — nada de esto es pendiente
>
> | Sesión | Cerrado |
> |---|---|
> | `opencode-site` | **Carril C**: de 1039 a **0 BAD** en `Universidad/**` (180 redirigidos, 522 neutralizados, 20 notas republicadas por BOM/frontmatter, Leeme de BD reescrito) · **P1** firmado con worktree + hook probado · build 847 + deploy verificado |
> | `opencode` | **Carril B**: figuras y `Diagramas/` unidos a `U0/` de cada materia · 95 redirecciones por contenido verificado · 56 láminas embebidas · firma P1 con worktree |
> | `opencode-onedrive` | **Carril A**: `qa_links.py` y scripts · taxonomía de Cálculo Vectorial · fix de `norm_name` (2617 falsos positivos) · hook + `FLUJO-WORKTREE-SESIONES.md` · CI anti-fuga |
> | `opencode-nube` | Normalización de formato (Pasadas 1 y 2) · `dg-publish` a las 5 `Recursos visuales` · **reparador de mojibake probado** (0 palabras cambiadas) · firma P1 |

## Pendientes reales (lo único que falta)

> [!warning] 5 cosas, ni una más
>
> 1. **Mojibake: 16 notas publicadas con texto roto.** Medido por mí: **2541 marcas**
>    visibles en el sitio — 8 de BD U1/U2 (2503 marcas) + 8 chicas de 1–12 (MOOC inglés ×4,
>    inglés I ×2, Física ×1, Syllabus BD ×1). El reparador de `opencode-nube` está probado;
>    **falta el OK de `opencode`** para aplicarlo. `opencode-site` verifica sync/build/deploy después.
> 2. **160 BADs fuera de `Universidad/**`** (root repo): 50 links reales en `Contenido Extra/**`
>    (`opencode` propone tomarlos con la regla ya aprobada), 58 **falsos positivos** de
>    `[[#Encabezado]]` intra-documento en `Clippings/**` (patch para `opencode-onedrive`, carril A),
>    49 placeholders de documentación y 2 en `site/docs/**`.
> 3. **DSW U3/U4**: solo 4 y 3 archivos — **falta conseguir el material** (dueño del vault).
> 4. **69 targets aproximados del carril C** (links cuyo destino sugerido es de otra materia):
>    criterio del dueño — redirigir por contenido verificado (tabla de `opencode`) o neutralizar.
>    **Decisión pendiente del dueño; sin ella no se tocan.**
> 5. **Nada más**: CI anti-fuga implementado, `_privado/` descartado, dominio cerrado
>    (`neonotes.vercel.app` no es de este proyecto), migración OneDrive cancelada.

## Lo que necesita `opencode-site` de los demás

> [!question] 4 pedidos concretos
>
> 1. **`opencode`**: **OK para reparar el mojibake** de las 16 notas (o autorizarme a aplicar el
>    reparador probado de `opencode-nube`). Es el único defecto de contenido visible en
>    producción y viene de mi propia republicación de esas notas.
> 2. **`opencode-nube`**: correr el reparador en **modo lectura** sobre las 8 notas chicas
>    (MOOC inglés, inglés I, Física, Syllabus BD) y confirmar 0 palabras cambiadas — con eso
>    `opencode` autoriza de una.
> 3. **`opencode-onedrive`**: sumar al `FLUJO-WORKTREE-SESIONES.md` que **el hook no se hereda
>    entre clones distintos** (copiarlo y probarlo por clon). Es tu documento, no lo edito sin tu OK.
> 4. **Las 4 sesiones**: verificar su hook `pre-commit` con un commit descartable. Con B/C
>    vigente, es lo único que puede fallar en silencio.
>
> **Mi turno de push queda libre. Commits sin pushear (míos): ninguno.**

---

**Tags:** #clippings #protocolo #coordinacion #fuente-unica
