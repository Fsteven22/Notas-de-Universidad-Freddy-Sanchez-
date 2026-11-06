---
dg-publish: false
---

# Herramientas — toolkit del vault (git-synced)

Todo lo que mantiene el vault vive en `Universidad/Herramientas/`. Se ejecuta con `py <script.py>` (Python 3.12, Windows).

> [!tip] 🔀 Flujo de trabajo por sesión (worktree + reglas anti-mezcla)
> Trabajar cada sesión en su propio `git worktree` (fuera de OneDrive) evita que un commit captura trabajo ajeno: ver `FLUJO-WORKTREE-SESIONES.md`. Post-mortem: `Clippings/PROBLEMA - commits mezclados por el indice compartido.md`.

## Estructura

| Carpeta | Qué hay |
|---|---|
| `Scripts/` | Conversores y verificadores de uso diario: PDF→Markdown, Office→Markdown, Markdown→PDF, flashcards, `verificar_nota.py`, `limpiar_espacios.py`, `kit_recuperacion.py`. Guías `GUIA-*.md` y `LEEME-SCRIPTS.md`. |
| `Mantenimiento/` | Auditores y fixers del vault: callouts, wikilinks, PDFs huérfanos o duplicados, refs tipo checkbox, PDF→Markdown en lote. |
| `SVG-Pipeline/` | Recreación de SVG fantasma con Mermaid, con `mmd2/` (fuentes) y `previews/` (PNG de control). |
| `Reportes/` | Salidas de los auditors (markdown/txt). |
| `Figuras/` | Imágenes reutilizables embebidas en las notas. |
| `Catalogo de errores del vault.md` | Nota espejo del usuario: los 7 tipos de error del vault con ejemplo roto y solución, más el test A/B/C/D de fences. Sus examples son intencionalmente rotos, así que los fixers la excluyen por nombre (`mdlib.py`, `fix_links.py`). |

## Backups

Los respaldos **no** viven dentro del vault (así Obsidian no los indexa y git no los versiona). Van en:

```
C:\Users\Steven Sànchez\OneDrive\OneSyncFiles-backups\notas-YYYYMMDD\
```

`notas-20261024` es la copia del 3er Semestre del 2026-10-24. Si se genera un backup nuevo, se crea la carpeta `notas-<fecha>` ahí y se borra la copia del vault.

## Mantenimiento/ — los 7 tipos de error de nota

Catálogo de los 7 tipos de error (los definió el usuario en `_Test Callout Fences.md`).
**Todos los fixers corren DRY por defecto** (solo reporte con `-o`); `--apply` toca archivos.
La nota espejo `_Test Callout Fences.md` se excluye de los fixers (sus ejemplos son intencionales).

| Script | Error | Qué hace |
|---|---|---|
| `fix_callout_overlap.py` | 1. Callouts pegados | Dos callouts del mismo nivel sin línea en blanco: el 1° absorbe al 2°. Inserta el separador. |
| `fix_callout_join.py` | 2. Callout disperso | Líneas en blanco crudas cortan el callout; el contenido con `>` que queda suelto se re-agrega rellenando el hueco con el prefijo del callout. |
| `fix_callout_nested.py` | 3. Callouts anidados aplastados | Callout plegado (`[!x]-`) adyacente a contenido: lo anida (inserta `>` separador + re-prefija su bloque). |
| `qa_links.py --sugerir` | 4. Links fantasma | QA global de links/!embeds + `difflib` sugiere notas parecidas (crear / redireccionar / borrar). |
| `fix_matematica.py` | 5-6. Matemática sin `$` / `$$` | Detecta LaTeX/caret/ecuaciones peladas; reporte humano (auto-fix requiere CSV línea a línea). |
| `detect_fuera_callouts.py` | 7. Contenido fuera de callouts | Bloques huérfanos del estilo "mensaje dentro de callout" (tablas, fórmulas, datos); reporte. |
| `fix_callouts.py` | (base) | Espacios que rompen callouts (`>   ` → `>`, trailing). |
| `qa_links.py` | (base) | Verificador NFC/NFD-safe de todos los wikilinks. Saltea `Clippings/` y `site/` por defecto (ahí los dobles corchetes son ejemplos de documentación: `--incluir-docs` para incluirlos), ignora targets de Templater (`<% … %>`) y valida anclas `#Encabezado` del propio archivo (`BAD-ANCLA` solo si el encabezado no existe). |
| `pdf_a_texto.py` | (base) | PDF→txt + inventario vía PyMuPDF. |
| `mdlib.py` | (lib) | walk_notes/load/save/report/callout — utilidades compartidas. |
| `qa_all.py` | (entry) | Punto de entrada unico: ejecuta los 4 QA de arriba en orden y agrega codigos de salida. |
| `qa_assets_huerfanos.py` | (base) | Assets del vault (SVG/PNG/PDF/…) que ninguna nota publica referencia. Identifica material huerfano que ocupa cuota. |
| `qa_resolucion_diagramas.py` | (base) | Embeds de diagrama/asset (wikilink con `!` adelante, ej. `Diagramas/archivo.svg`) que no resuelve a un archivo real. |
| `qa_mojibake.py` | codec híbrido cp1252/latin-1 | Detecta y repara mojibake (doble codificación UTF-8) en notas `.md`. `--check` solo reporta; `--fix` reescribe solo los "runs" sospechosos y verifica que el esqueleto ASCII quede idéntico (no agrega ni borra texto legible). `--check --check` sobre las 832 notas del vault → 0 runs restantes. |
| `qa_material_nuevo.py` | detector carril D1 | Detecta material nuevo/modificado/eliminado en carpetas vigiladas del vault mediante baseline CSV (sha256 + tamaño). `--baseline` crea el snapshot (por defecto las 5 carpetas `Unidad 0` de 3er Semestre); `--check` compara contra el baseline; `--actualizar` reescribe el baseline tras revisar. |
| `snapshot_d1.csv` | baseline carril D1 | Snapshot de las 5 carpetas `Unidad 0 - Guias y Ejercicios` de 3er Semestre: **912 archivos** con ruta, sha256 y tamaño. Vive junto a `qa_material_nuevo.py` para que no se pierda con una poda de `<TEMP>`. |
| `qa_fugas_copyright.py` | (base) | Archivos listados en `_no-publicar.txt` (o variantes `_OCR`) que aparecen en `site/public/assets/`. Red de seguridad contra fugas de copyright. |
| `qa_svg_titulo.py` | (base) | SVGs con titulos placeholder genericos (`flowchartTitleText`) que nunca se les asigno uno real. |
| `qa_omitidas.py` | (base) | Notas que el sitio NO publica por el gate silencioso de frontmatter: sin `dg-publish: true`, sin frontmatter o con BOM UTF-8 al inicio (rompe el parseo). Agrupa por semestre/materia. `--estricto` → exit 1 si hay omitidas (CI). |

Cifras del dry-run (2026-10): pegados=204 (90 notas), dispersos=0, anidados=62 (20 notas),
links BAD=1989 (con sugerencias), matemática=893 candidatos, fuera-de-callout=229 bloques.

Entrada unica: `py Universidad/Herramientas/Mantenimiento/qa_all.py --vault <raiz_vault>` ejecuta los 4 QA en orden.

Los scripts que deducen la raíz del vault la calculan desde su propia ubicación (`Universidad/Herramientas/Mantenimiento/` → 3 niveles arriba). Si se mueven de carpeta, hay que ajustar ese cálculo.

## SVG-Pipeline/ — recreación de SVG fantasma con Mermaid

| Script | Qué hace |
|---|---|
| `vlib.py` | Resuelve rutas de la vault (`materia(semestre, key)`); constante `VAULT`. |
| `catalogo_fisica.py` | Escanea una materia y lista los SVG referenciados que no existen (fantasma) → JSON. |
| `build67.py` | Generador Física Mecánica: dict `MERMAID_SRC` por diagrama + `STD` (clases pastel compartidas) + `main()` que compila todos con `mmdc` a `.svg` (fondo blanco) y `.png` (-s 2) en `previews`. **Al importarlo corre `main()`.** |
| `descargar-material-ccpg1001.py` | Descarga PDFs/PNG del repo GitHub del profesor preservando nombres normalizados → Unidad 0. |

Pipeline estándar: `catalogo → buildNN.py (dict MMD) → mmdc → QA de previews → commit+push`.
Flujos: `QA_BY_PATH = "QA: <tramo 1>; ..."` para verificar cada flecha en los previews.
Fórmulas en vyphen: sin `<>` (rompe mmdc) — usar `∫[a→b]`, `[i=1→n]`.

## SVG-Pipeline/ — la tipografía incrustada de los SVG (leer antes de generar uno)

Mermaid CLI incrusta la tipografía **"Recursive Variable"** dentro de cada SVG que genera: 4 reglas
`@font-face` con la fuente en base64 (`data:font/woff2;base64,…`) + su licencia OFL. Son **161 KB de
base64 por archivo**, el 90% del peso de un diagrama (un SVG de 182 KB de media en el vault). Con
2.126 SVG, son **~340 MB de fuente repetida**.

La fuente va incrustada porque un SVG que se muestra con `<img src="…svg">` se dibuja en un contexto
aislado: no puede cargar el CSS de la página ni una fuente externa. Si no la lleva, las etiquetas del
diagrama salen con la tipografía del sistema.

| Script | Qué hace |
|---|---|
| `subconjuntar_fuente.py` | Recorta la fuente incrustada a **los glifos que ese diagrama usa** (texto visible + `aria-label`/`title`). El SVG se ve igual (misma variable font, mismos avances y contornos) y pasa de 182 KB a ~36 KB. Verifica que la cobertura por rangos no cambie y que **ningún glifo que la fuente original traía se pierda**; los glifos que el diagrama usa y que la fuente original NO traía (emoji, `→`, `‴`, ZWJ…) se registran en el propio SVG como `/*fuente-sin-glifo:U+2034*/` (se dibujan con la tipografía del sistema, igual que antes). Si algo no cuadra, **deja el archivo como está**. CLI: `py -3.12 subconjuntar_fuente.py <carpeta>` (con `--dry-run` solo mide). |
| `mmdc_ligero.py` | **Reemplazo directo de `mmdc`**: hace lo mismo y ademas recorta la fuente del SVG que genera. Úsalo en vez de `mmdc` al crear diagramas: `py -3.12 mmdc_ligero.py -i x.mmd -o x.svg -b white`. |
| `qa_svg_fuente.py` | QA de la fuente incrustada: (a) **cobertura** — todo carácter que el diagrama muestra y que la fuente declara en su `unicode-range` tiene que estar de verdad en la fuente (si alguien edita un SVG a mano y añade una etiqueta con un carácter que la fuente ya no trae, ese glifo saldría con la tipografía del sistema); (b) **peso** — avisa de los SVG que todavía llevan la tipografía completa. Los emoji y símbolos que nunca estuvieron en la fuente (✅ ❌ →) se dibujan con la tipografía del sistema a propósito: no cuentan como fallo. Los huecos preexistentes (los que la fuente original no traía) están documentados en el propio SVG y tampoco cuentan como fallo. |

> [!warning] Regla para quien genere diagramas
> Todo SVG nuevo que salga de `mmdc` debe pasar por `subconjuntar_fuente.py` (o generarse con
> `mmdc_ligero.py`). Si no, el SVG entra al repo con 161 KB de fuente repetida y hay que volver a
> recortarlo después — que es exactamente el trabajo que se hizo el 05/11/2026 sobre los 2.126 SVG
> existentes. `qa_svg_fuente.py` es la red de seguridad: avisa de los que se quedaron pesados.

Requisito: `py -3.12 -m pip install fonttools brotli`.

**Estado del recorte (05/11/2026):** 2.375 SVG revisados · **2.126 recortados** (421,8 MB → 124,3 MB,
−71%) · 249 sin tipografía incrustada (intactos) · **0 rechazados** · QA final: 0 pesados, 0 fallos de
cobertura, 92 SVG con huecos preexistentes documentados.
