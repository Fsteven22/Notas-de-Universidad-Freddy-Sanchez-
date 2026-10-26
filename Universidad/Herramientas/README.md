---
dg-publish: false
---

# Herramientas — toolkit del vault (git-synced)

Todo lo que mantiene el vault vive en `Universidad/Herramientas/`. Se ejecuta con `py <script.py>` (Python 3.12, Windows).

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
| `qa_links.py --sugerir` | 4. Links fantasma | QA global de [[links]]/![[embeds]] + `difflib` sugiere notas parecidas (crear / redireccionar / borrar). |
| `fix_matematica.py` | 5-6. Matemática sin `$` / `$$` | Detecta LaTeX/caret/ecuaciones peladas; reporte humano (auto-fix requiere CSV línea a línea). |
| `detect_fuera_callouts.py` | 7. Contenido fuera de callouts | Bloques huérfanos del estilo "mensaje dentro de callout" (tablas, fórmulas, datos); reporte. |
| `fix_callouts.py` | (base) | Espacios que rompen callouts (`>   ` → `>`, trailing). |
| `qa_links.py` | (base) | Verificador NFC/NFD-safe de todos los wikilinks. |
| `pdf_a_texto.py` | (base) | PDF→txt + inventario vía PyMuPDF. |
| `mdlib.py` | (lib) | walk_notes/load/save/report/callout — utilidades compartidas. |

Cifras del dry-run (2026-10): pegados=204 (90 notas), dispersos=0, anidados=62 (20 notas),
links BAD=1989 (con sugerencias), matemática=893 candidatos, fuera-de-callout=229 bloques.

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
