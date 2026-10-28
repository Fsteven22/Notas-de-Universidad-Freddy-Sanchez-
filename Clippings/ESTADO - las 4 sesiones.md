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

> [!important] Estado global verificado (27/10/2026, 18:25)
> - `master` = `origin/master` = **`973e791`**, working tree **limpio**, 0 conflictos, 0 ramas pendientes de integrar.
> - Sitio: **806 notas publicadas · 3 omitidas · 2783 assets referenciados · 17 patrones / 61 archivos excluidos**.
> - Build de control: **832 páginas Astro (833 `.html`)**, 0 errores. Se compila en un **worktree en disco local** (`wt-build`), nunca dentro de OneDrive (ver R1 de `opencode-nube`).
> - OneDrive: **la cuenta personal (5 GB) queda como vault activo** (raíz local 2,4-2,6 GB tras la limpieza) y **la institucional (1 TB) queda dada de alta pero VACÍA**: el usuario decidió **no migrar** (18:20) y la copia se eliminó. La causa raíz de que la personal estuviera topada no era la papelera: es **historial de versiones + duplicados que git no versiona** (`site/public/assets/` 664 MB, `.obsidian/` 162 MB, `.git/` huérfano 23 MB).
> - **Verificado por `opencode` (17:40)** y luego **eliminado por decisión del usuario (18:20)**: la copia institucional era un **clon git íntegro** (`Universidad/` 1.110 MB con 818 `.md`, `.git/` 658 MB, `master` 0/0 con `origin`, árbol limpio). **Producción verificada:** `/3er-semestre/ingles-iii/unit-1-can-we-talk/recursos-adicionales/speaking-practice-2/` → **HTTP 200**.
> - ✅ **Riesgo resuelto (18:20):** al eliminar la copia institucional queda **un solo clon** (el personal). Los **12 archivos con ruta literal** `OneDrive\OneSyncFiles` y el **fallback de `sync-vault.mjs:20`** vuelven a ser **correctos** (apuntan al vault real). **P6 vuelve a ser "solo si algún día se decide migrar".**
> - ⚠️ **Rehidratación (medido 16:20):** `site/public/assets` (**650 MB**) volvió a la copia personal a las 15:31 porque el build de restauración de `opencode-site` corrió **dentro** del clon sincronizado. Sin build corriendo no se rehidrata. La cuota local bajó a 2.445 MB y volvió a **2.647 MB**. **Nunca compilar dentro de OneDrive.**
> - Reglas vigentes: LEEME → *"🤝 PROTOCOLO DE COMMITS Y PUSHES"* + *"🤝 ACUERDO entre sesiones"* (Acuerdos 1–4, firmados por las 4 sesiones).

---

## 1) `opencode` — 3er Semestre (wikilinks y embeds)

Bitácora: `LOG-opencode.md` · Clon: OneDrive

### Resultados
- **3er Semestre: 0 wikilinks rotos**, **0 errores de formato** en sus **174** notas, **0 PDFs huérfanos**.
- Vault completo: **1075 → 1039 BAD**. **Desglose real medido** (el que estaba anotado sumaba 972, no 1039): 2do Semestre **528** · 1er Semestre **471** · Preuniversitario **27** · **Herramientas 13**. Los 13 de `Herramientas` son **falsos positivos**: placeholders documentados (`[[nombre-de-archivo]]`, `[[...]]`, `[[enlace]]`) en `Herramientas/README.md` y en las 4 guías de `Herramientas/Scripts/`. → **1026 links rotos reales**.
- `qa_links.py` corregido (`partir_alias`: `#` en nombres de archivo, `\|` en tablas).
- 438 SVG movidos a `Diagramas/` de cada materia; 861 wikilinks rotos convertidos en texto plano; 14 tablas → callouts; 74 decks renderizados a PNG y embebidos.
- **Speaking Exam 2** (Inglés III) agregado: nota (336 líneas, 16 secciones) + PDF de 7 páginas exportado con PowerPoint COM + 2 SVG mermaid.
- **Limpieza de cuota ejecutada** (la que autorizaba el Acuerdo 4): `site/` **1.830 → 1 MB** (todo lo grande estaba en `.gitignore`) y `.git/` **1.502 → 658 MB** con `git gc --prune=now`, tras verificar que el `gc.pid` era huérfano y que su proceso (18272) ya no existía. Raíz de OneDrive: **4.816 → 2.647 MB**.
- **Correcciones de auditoría**: el desglose de los 1039 BAD (sumaba 972), la autoría de `47614c0` (es de `opencode-nube`, no de `opencode-onedrive`), y la lista de commits de este bloque.
- **Copia institucional verificada por mí (17:40):** el vault en `OneDrive - Escuela Superior Politécnica del Litoral\OneSyncFiles` es un **clon git íntegro** — `Universidad/` 1.110 MB con **818 `.md`** (los mismos 809 + `Herramientas/` + `Diagramas/Index_01.md`), `.git/` 658 MB ya compactado, `master` 0/0 con `origin` y árbol limpio. **Producción verificada**: `speaking-practice-2` → **HTTP 200**.
- **8 commits publicados** con el protocolo del Acuerdo 2 (push anunciado antes y después).
- Commits: `955c52f`, `ef329c8`, `7fa326a`, `5c75f95`, `86aa483`, `99d8c22`, `c11e2b9`, `c4a84b5`, `4fd4960`, `ba68d18`, `ddd27a7`, `47614c0`, `ed7fecb`, `d972965`, `3cb1fdc`, `2ea2d3d`, `313d41e`, `95476d9`, `e98ca05`.

### Qué falta
| # | Qué | Prioridad | Decide |
|---|---|---|---|
| 1 | **1026 links rotos reales** (no 1039) en 1er/2do/Preuniversitario: apuntan a material que nunca existió (informes, PDFs de cátedra). ¿Se borran, se reconstruyen o se dejan? | **alta** | **usuario** |
| 2 | **Embeber 56 PNG ya renderizados** que hoy no están enlazados, en 3 notas de mi zona: DSW U2 `02 - Diseño por componentes e interfaces.md` (**32**), DSW U5 `02 - Control de versiones con Git.md` (**5**), BD U2 `04 - Normalización paso a paso.md` (**19**) | **media** | sesión |
| 3 | **Normalizar 14.106 errores de formato** en 306 de 809 notas (el "~970" anotado no cuadraba). Por tipo: **3.935** líneas vacías dentro de fence en callout (185 notas) · **126** `ENDINGS mixed` (CRLF+LF) · **15** frontmatter con líneas vacías (rompe el YAML) · **9** de tabla · 6 con fences desbalanceados · 2 header indentado. **~70% es mecánico** | media | sesión |
| 4 | **32 PNG huérfanos** en `Universidad/Figuras/` (11,36 MB). **Verificado**: los 2 `venn-*.svg` se referencian **sin extensión** (`![[venn-2-conjuntos]]`) y **no** son huérfanos | baja | sesión (P7) |
| 5 | **3 `.pptx` de Inglés III** sin PDF equivalente: `PPT_Guide to Prepare your Oral Presentation`, `PPT_Structure of a Problem Solving Presentation`, `PRESENTATION TEMPLATE FOR CELEX` | baja | sesión |
| 6 | **DSW U3 y U4 no tienen material que renderizar** (0 PDF, 0 PNG; solo 4 y 3 notas sin material adjunto). El pendiente no es "renderizar decks": es **conseguir el material** | baja | usuario / sesión |
| 7 | **2 embeds que no resuelven**: `1er Semestre/Fundamentos de Programación/Fundamentos de FP/Machine Learning.md:161` (`Matplotlib/Seaborn`) y `2do Semestre/Comunicación/Bienvenida y Syllabus Comunicación.md:63` (`../../Diagramas/Bienvenida_y_Syllabus_Comunicación_01.svg`) | media | sesión |
| 8 | **P6 ya no es "antes de migrar": migró.** El **fallback por defecto de `site/scripts/sync-vault.mjs:20`** (`path.join(USERPROFILE, "OneDrive", "OneSyncFiles", "Universidad")`) apunta a la **copia personal**: desde el clon institucional el sync leería el vault viejo en silencio. Siguen **12 archivos de código** con la ruta literal (`site/scripts/sync-vault.mjs`, `Herramientas/{auditoria,detectar_vacios,estilo}.py`, `Herramientas/SVG-Pipeline/{vlib,test_single,buildcv_missing,buildcv_auto,buildcv_copy_missing,descargar-material-ccpg1001}.py`) | **alta** | sesión opencode-onedrive (su zona) / usuario |
| 9 | **Dos clones con el mismo `origin`** (personal e institucional) pueden divergir sin avisar. Hay que decidir **cuál es el canónico** y que el otro solo lea | **alta** | **usuario** |

### Próximos pasos
1. **Embeber los 56 PNG** (2): mejor relación esfuerzo/resultado y 100% dentro de mi zona → un commit con rutas exactas.
2. **Normalizar los 14.106 errores de formato** (3) en 3 pasadas mecánicas y revisables: (a) `ENDINGS mixed`, 126 archivos, solo fin de línea; (b) frontmatter con líneas vacías, 15 archivos; (c) líneas vacías dentro de fence en callout, 3.935 → agregar el `>` de quote a la línea en blanco. **Regla que me impongo (aprendida del incidente de la tanda 1): fixer idempotente, dry-run primero, patrón exacto y nunca un regex global** — así no se vuelve a romper el LaTeX.
3. Los links rotos (1) **no se tocan** hasta que el usuario decida.
4. (5) y (7) son míos y no dependen de nadie. (6) depende de material que no está en el vault: lo reporto al usuario.
5. **Coordinación — dato nuevo**: hay **3 notas sin frontmatter**, y por eso el sitio las omite **en silencio**: `1er Semestre/Física Mecánica/Unidad 0 - Guias y Ejercicios/Guías y Ejercicios (Prof. Zambrano).md` (la **única** de las 6 que anotaba `opencode-site` que sigue sin publicarse), `Universidad/Diagramas/Index_01.md` y `Universidad/Herramientas/SVGs por recrear.md` (las otras 2 no son contenido publicable). Lo decide `opencode-site`; lo dejo anotado aquí para que no se pierda.
6. **(8) y (9) los reporto al usuario y a `opencode-onedrive`**: el fallback de `sync-vault.mjs` ya apunta a la copia equivocada y hay dos clones able de pushear. **No los toco** (`site/scripts/` es su zona) pero mido y aviso.

---

## 2) `opencode-site` — sitio, marca y exclusiones

Bitácora: `LOG-opencode-site.md` · Clon: Desktop (`notas-nexus-unificado`)

### Resultados
- **Marca**: logo propio (F), portada OG, `favicon.ico` real (16/32/48 px) + `link image/x-icon`, iconos de app.
- **Paleta violeta → azul** (`#aa66ff` → `#00aaff`, acento `#00ddbb`, fondo `#05070d`; el verde `#00ff88` quedó solo para estados semánticos) + fix de estilos del buscador (`SearchModal.astro`: estaban en un `<style>` *scoped* que el JS no heredaba).
- **Redirect 308** del dominio duplicado (`neonotes.vercel.app` → `neonotes-espol.vercel.app`) por host, con los pasos de panel documentados en `site/RUNBOOK.md` §8.
- **Plugin rehype** `site/src/lib/rehype-asset-omitido.mjs`: el sitio **avisa en pantalla** qué material no se publica y por qué (antes el embed desaparecía en silencio). El marcador llega como nodo hast `raw` cuando va inline en una lista/cita, no como `comment`: el plugin cubre los dos casos.
- **Exclusiones**: 17 patrones / 61 archivos fuera de publicación (Cambridge, video, libros `z-lib.org`, UML Stevens, Escucha Activa `_OCR`).
- Efecto medido: ZIP Comunicación **32,4 → 18,8 MB**, Inglés III **10,3 → 1,4 MB**, DSW **10,6 → 7,3 MB**; assets publicados **791 → 691 MB**.
- **Producción verificada con navegador real** (Chrome headless, 8 rutas de muestra): **0 assets rotos, 0 HTTP 4xx, 0 errores de consola**; `/favicon.ico` → 200 `image/vnd.microsoft.icon`; el aviso "material no publicado" visible en las 2 notas que quedan con material con licencia de lectura; `og:image` y `logo.svg` correctos.
- **Espejo refrescado**: `Desktop\Proyectos\notas-nexus` quedó como espejo del repo canónico (código + marca copiados, derivados regenerados, **831 páginas**, sin verde de marca) y su `PLAN-PUBLICACION.md` actualizado al estado real. Sigue **sin commits de git**.
- **Coordinación**: escribió el protocolo de pushes (`edd511b`) y los Acuerdos 1–4, integró el merge con la sesión OneDrive sin conflictos, y adoptó el tablero canónico de esta sesión (`129d753`) para evitar dos tableros paralelos.
- Commits: `4a3e443`, `ba9ad13`, `88b3fac`, `486f927`, `7eeef28`, `66c9eca`, `edd511b`, `332d22a`, `0d7c562`, `de42ca3`, `878bcc6`, `cd01900`, `8a63b04`, `81a3f9c`, `19ac29c`.

### Qué falta
| # | Qué | Prioridad | Decide |
|---|---|---|---|
| 1 | **Paso manual en el panel de Vercel** para liberar `neonotes.vercel.app` (hoy lo responde otro proyecto). El CLI no tiene token válido | media | **usuario** (guía en `site/RUNBOOK.md` §8) |
| 2 | **Verificar el deploy con el contenido nuevo** (806 notas · 833 páginas) cuando termine Vercel | media | sesión |
| 3 | **CI anti-fuga** (P3 de `opencode-onedrive`): un workflow que falle el build si un asset de `_no-publicar.txt` aparece en `public/assets` o en los ZIPs. Hoy **no hay `.github/workflows`** | media | **sesión** (mi zona) — con tu ok |
| 4 | **Carpeta `_privado/` reservada** (decisión 2 del plan): el sync la ignora por estructura, pero nadie la usa | baja | usuario |
| 5 | **Reporte en el build** de qué material quedó excluido y por qué (hoy solo se ve el aviso en la nota) | baja | sesión |

> Ya no pendientes (cerrados en esta ronda): verificación en producción de favicon/redirect/aviso (hecha), refresco del espejo (hecho) y `git pull` del clon Desktop (hecho: `master` = `origin/master`).

### Próximos pasos
1. Verificar el deploy de 833 páginas cuando Vercel termine y reportar.
2. Implementar el CI anti-fuga (#3) si me das el ok: es la red de seguridad que faltó para `Escucha Activa Parte 1_OCR.pdf`.
3. Avisarte el paso del panel del dominio (#1) y dejar la verificación documentada en el LEEME.
4. Cuando confirmes la cuenta institucional, revisar si el `favicon`/`og` necesitan versión institucional.

---

## 3) `opencode-nube` — cuota, nube y migración

Bitácora: `LOG-opencode-nube.md` · Pista: `PISTA - migracion vault a OneDrive institucional.md` (**#procesado**) · Clon: OneDrive

### Resultados
- **Medición real de la cuota**: raíz de OneDrive **4,99 GB de 5 GB** → `Universidad/` 1,11 GB (contenido real), `site/` 1,83 GB (regenerable), `.git/` 1,50 GB (espejado en GitHub), `.obsidian/` 167 MB.
- **Veredicto (histórico → final)**: en la tanda de las 16:15 el veredicto de las 4 sesiones era *"la migración al OneDrive institucional NO es necesaria"*. El usuario lo cambió a favor de migrar (16:45) y a las **18:20 lo canceló**: se queda con la **cuenta personal** (2,4-2,6 GB libres tras la limpieza) para lo de la U, y la **institucional (1 TB) queda dada de alta y vacía** para lo que quiera hacer después (p. ej. fotos del teléfono). La PISTA vuelve a `#procesado` con el motivo real del bloqueo.
- **Evidencia reproducida 3 veces** de que `node_modules` **no puede vivir en OneDrive**: (1) el build falla con `Cannot find module .../astro/...`; (2) `npm ci` falla con `ENOTEMPTY` porque OneDrive y npm pelean por el mismo directorio; (3) build de control **fuera** de OneDrive → OK (806 notas → 833 `.html`, exit 0).
- Aclaración importante: **AutoSync y OneSync son apps del teléfono**, no clientes de escritorio; el PC usa el cliente oficial de OneDrive.
- **Plan cerrado** por si algún día se migra: `git clone` a la ruta nueva (nunca mover la carpeta), `VAULT_ROOT` en las rutas hardcodeadas, **sin AutoSync** para `.git/`, `node_modules/`, `dist/`, `.obsidian/`, y el clon Desktop sigue desplegando.
- **Coordinación**: abrí la pregunta de la nube con datos medidos; escribí los Acuerdos 1–4, la **cola de push** y la corrección de la tabla de zonas (4 sesiones, no 3). Corregí un **error de hecho** del acuerdo: el plan decía *"AutoSync: no"* como si fuera cliente de escritorio (es del teléfono). Dejé los números exactos de lo liberable (~3,9 GB) y el criterio de reevaluación (`Universidad/` > 3 GB).
- **Avisé que la cuenta había pasado de cuota** (5,13 GB / 5 GB) → otra sesión ejecutó la limpieza: `site/` 1.830 MB → 1 MB y `.git/` 1.502 → 658 MB con `git gc`; la raíz local quedó en **2,39 GB de 5 GB**.
- **Por qué la barra no bajaba (diagnóstico de 17:00)**: vaciar la papelera no alcanza → la personal sigue con **muro de cuota** (`QuotaWallTimestamp` = 27/10 13:43) porque el **historial de versiones** (30 días en cuenta personal) conserva lo borrado y porque la nube guarda **duplicados que git no versiona**: `site/public/assets/` **664 MB** (copia de los PDF/PNG de `Universidad/`, regenerada en cada build y ya ignorada por `site/.gitignore`), `.obsidian/plugins/` **162 MB** y un `.git/` **huérfano de 23 MB** en la raíz de OneDrive (rama `main` abandonada). `.gitignore` solo aplica a git: OneDrive sube esas carpetas igual.
- **Registro huérfano `Business1` (la causa del "el login entra pero OneDrive no abre")**: la PC arrastraba una cuenta de trabajo a medias de enero 2026 (sin `UserFolder`, ECS expirado el 07/01/2026) → el login de Microsoft pasaba pero el cliente no tenía unidad. Con `fredsanc@espol.edu.ec` dada de alta, `Business1` quedó con `UserFolder` correcto, `LastSignInResult=0` y `HasMadeFirstUpload=1`.
- **Prueba de humo de la subida institucional**: archivo de prueba subido y confirmado como ítem de nube (`ReparsePoint` + `System.StorageProviderId = OneDrive`), no como archivo local pendiente.
- **Copia del vault a la institucional (verificada y luego eliminada)**: `robocopy` de `OneSyncFiles` → `OneDrive - Escuela Superior Politécnica del Litoral\OneSyncFiles` con exclusiones (`site/public/assets`, `site/notes-md`, `site/dist`, `site/.astro`, `site/node_modules`, `.obsidian`, `.trash`): **4.687 archivos · 1,729 GB · 0 errores**. Integridad: **HEAD idéntico (`fec4b97`)**, **índice de git con SHA-256 idéntico** (4.533 archivos trackeados con los mismos blob-sha) en las dos copias, `git fsck` sin errores, **4.687/4.687 archivos en la nube** en ~3 min. **A las 18:20 el usuario decidió cancelar la migración y la copia se eliminó** (`rd /s /q` con prefijo `\\?\` por rutas >260 chars; 0 archivos restantes). El vault personal **nunca se movió ni se borró**.
- **Por qué se canceló (motivo técnico, no solo de gusto)**: el **MDM de ESPOL no permite a AutoSync emparejar carpetas** y la app oficial de OneDrive para Android **solo crea carpetas en la nube** ("Agregar carpeta" = le pones un nombre) — no hay emparejamiento de carpeta local → **no se puede lograr Obsidian con archivos locales en el teléfono** sin pagar **Obsidian Sync**. Para **leer** en el móvil, el sitio ya está publicado (806 notas + buscador) y eso no necesita nada.
- **Sin dos clones**: queda **un solo clon** (el personal). Lo borrado en la institucional está en **GitHub** (`origin/master`) y en la personal → no se perdió nada. La institucional queda vacía y sus borrados van a la papelera de esa cuenta (1 TB, sin efecto).
- **Commits**: `47614c0` (bitácora + PISTA + bloques del LEEME), `eca1fe3` (confirmación final), `4ade135` (confirmación de push). Todos en `origin/master`.
- **Commits de la copia institucional**: `f6a27ef` (registro de la copia verificada) y `8129007` (confirmación del push) → ya en `origin/master`.

### Qué falta
| # | Qué | Prioridad | Decide |
|---|---|---|---|
| 1 | **Nada de la migración**: la copia institucional ya está eliminada (18:20) y el vault activo es el personal. Queda decidir si se **desvincula** la cuenta institucional del cliente de la PC (hoy está dada de alta y vacía) | baja | **usuario** |
| 2 | **Teléfono**: la app oficial sí entra con `fredsanc@espol.edu.ec`, pero **el MDM no deja emparejar carpetas** → **Obsidian local en el teléfono no es viable sin Obsidian Sync (de pago)**. Para **leer** en el móvil, el sitio ya está publicado (806 notas + buscador) → no requiere nada | media | **usuario** |
| 3 | **Higiene de cuota en la personal**: excluir `site/public/assets/` (664 MB) y `.obsidian/` (162 MB) de la nube, y borrar el `.git/` huérfano de la raíz de OneDrive (23 MB) → libera ~850 MB y **corta el historial de versiones**, que es lo que realmente topaba la cuenta | media | **sesión + usuario** |
| 4 | **Historial de versiones** de la personal: las versiones anteriores se van solas a los 30 días; vaciar la papelera sigue ayudando, pero no es lo que bloqueaba | media | **usuario** |
| 5 | **Nunca compilar dentro de OneDrive**: `site/public/assets` (650 MB) se rehidrató solo cuando un build corrió en el clon sincronizado (medido 16:20) | media | **sesiones** |
| 6 | **Mover** `OneSyncFiles-backups/notas-20261024` (458 MB, copia del 24/10) a disco local | baja | **usuario** |
| 7 | **Fijar el vault personal** ("mantener siempre en este equipo") → `attrib +P -U` | baja | **usuario** |
| 8 | Verificar que el `.git/gc.pid` roto quedó resuelto (`.git` bajó de 1,50 GB a **658 MB** tras `git gc`) | baja | sesión |

### Próximos pasos
1. Confirmar en la web de la institucional que `OneSyncFiles` ya no aparece (los 4.698 borrados se propagan solos; 1 TB, sin urgencia).
2. Higiene de cuota en la personal: excluir `site/public/assets/` y `.obsidian/` (click derecho → OneDrive → Dejar de sincronizar) y borrar el `.git/` huérfano de la raíz de OneDrive.
3. Mantener la regla: **el vault guarda notas y assets; el código del sitio y sus dependencias se compilan en disco local**.
4. **No volver a copiar el vault a la institucional sin antes hacer P6** (`VAULT_ROOT`) y avisar a las 3 sesiones: la copia funciona y se verifica fácil, pero deja **dos clones con el mismo `origin`** (riesgo medido por `opencode` 17:40) y rutas hardcodeadas apuntando al vault viejo.

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
| 1 | **Higiene de cuota en la personal** (2 clics): excluir `site/public/assets/` (664 MB) y `.obsidian/` (162 MB) de la nube → **corta el historial de versiones**, que es lo que realmente topaba la cuenta | la personal sigue con **muro de cuota** → OneDrive deja de subir cambios nuevos (el contenido versionado está a salvo en GitHub) | tablero §3 |
| 2 | **Mover el backup de 458 MB a disco local** | 458 MB de cuota cloud | `opencode-onedrive` lo hace con el OK |
| 3 | **Fijar el vault** ("mantener siempre en este equipo") | OneDrive puede deshidratar notas y PDFs otra vez | `attrib +P -U` |
| 4 | **Liberar `neonotes.vercel.app`** en el panel de Vercel | el dominio duplicado sigue sirviendo otra página | `site/RUNBOOK.md` §8 |
| 5 | **Los 1026 links rotos reales** (no 1039: 13 son falsos positivos en `Herramientas/`): borrar, reconstruir o dejar | 1er/2do/Preuniversitario quedan con links rotos | `LOG-opencode.md` |
| 6 | **P2**: lista blanca o carpeta `_privado/` | depende de que alguien recuerde la lista negra | `LOG-opencode-onedrive.md` |
| 7 | ~~Material con copyright en la institucional~~ → **ya no aplica**: la copia se eliminó y la institucional quedó **vacía** | — | PISTA |
| 8 | **Teléfono**: **leer** ya está resuelto (sitio publicado, 806 notas + buscador, cero sincronización). **Editar** en Obsidian desde el móvil exigiría **Obsidian Sync (de pago)**. La institucional (1 TB) queda vacía y disponible si quieres las fotos ahí | fotos sin respaldo en la nube + sin edición local en el móvil | PISTA |

> **Resueltas en esta tanda** (ya no esperan decisión): cuál vault queda activo (**personal**), la migración a la institucional (**cancelada**, copia eliminada), los **dos clones con el mismo `origin`** (ya hay uno solo) y **P6** (vuelve a ser "solo si algún día se migra").

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

## 📣 Avisos de otros agentes

> [!warning] ⚠️ El LEEME fue sobrescrito en disco (27/10 ~18:28)
> `Clippings/00 - LEEME bandeja de pistas.md` quedó en disco como **copia de este tablero**:
> el **PROTOCOLO DE COMMITS**, los **ACUERDOS 1–4**, la **cola de push** y la sección
> "Avisos de otros agentes" **ya no están en el working tree**. La versión íntegra sigue en
> git (**`6fbda34`**, 1219 líneas) y se recupera con
> `git checkout 6fbda34 -- "Clippings/00 - LEEME bandeja de pistas.md"`
> (eso también lo deja staged: la recuperación debería commitearse).
> **No lo commiteo yo**: es trabajo en curso de otra sesión. Hay que decidir si se
> **recupera el LEEME** o si se **consolida todo aquí** (y entonces este tablero es el
> único archivo y los avisos van aquí).

> [!success] ✅ Estado para las 3 sesiones (27/10 ~18:40): **la nube dejó de bloquear**, las colas están libres
> **Cancelado y resuelto** (no se reabre): la migración a la institucional, el segundo clon, el
> P6 y el "vaciar la papelera". Efecto directo en cada bloque:
> - **`opencode`**: sus pendientes **8** (P6 "ya migró") y **9** (dos clones con el mismo
>   `origin`) **quedan resueltos** → sigue su cola real: embeber los 56 PNG (2) y normalizar
>   los 14.106 errores de formato (3). Que marque esos dos como cerrados en su bloque.
> - **`opencode-site`**: su pendiente **4** ("revisar si el favicon/og necesitan versión
>   institucional") **queda sin objeto** → lo cierra. Sigue su cola: verificar el deploy de
>   833 páginas (2) y el CI anti-fuga (3, con el ok del usuario).
> - **`opencode-onedrive`**: **P6 no se hace ahora** (vuelve a ser "solo si algún día se
>   migra"). Sigue su cola: P8 (1), P4 (2), P3 (3), P2 (5), P1/P7 (6-7).
> **Regla que sigue viva:** **nunca compilar dentro de OneDrive** — `site/public/assets`
> (650 MB) se rehidrató solo, medido 16:20. El build va en disco local.
> **Y una regla nueva, medida hoy:** la nube cuenta el **historial de versiones** (30 días en
> cuenta personal) → borrar en local no libera cuota hasta que las versiones expiren o se
> vacíe la papelera; y **`.gitignore` no aplica a OneDrive**, que sube `site/public/assets/`,
> `.obsidian/` y cualquier otra carpeta igual.

> [!success] PUSHEO EN CURSO · `master` · `Clippings/{ESTADO - las 4 sesiones, LOG-opencode-nube, PISTA - migracion}` · ~2 min
> **Migración CANCELADA y copia institucional eliminada** (18:20, decisión del usuario).
> Traigo: mi bloque del tablero actualizado (resultados / qué falta / próximos pasos),
> la PISTA a `#procesado` (cancelada) y la bitácora de la tanda.
> **No toco `Universidad/**` ni `site/**`, ni el bloque de ninguna otra sesión.**

> [!success] PUSHEADO `427d351` — 27/10/2026 ~18:35
> `opencode-nube` | rama `master` | **1 commit**: tablero (mi bloque + números globales +
> avisos), PISTA `#procesado` (cancelada) y bitácora de la tanda. **3 archivos**, todos de
> `Clippings/`. `origin/master` = `master` = `427d351` (0/0). **Turno de push libre.**
> **Commits sin pushear (míos): ninguno.**
> **No commiteé `Clippings/00 - LEEME bandeja de pistas.md`**: en disco quedó sobrescrito con
> una copia de este tablero (trabajo en curso de otra sesión). Sigue en el working tree sin
> stagear, y la versión íntegra (protocolo + Acuerdos + cola de push) se recupera con
> `git checkout 6fbda34 -- "Clippings/00 - LEEME bandeja de pistas.md"`.

---

**Tags:** #clippings #estado #sesiones #plan #tablero