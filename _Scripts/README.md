# _Scripts — Toolkit del vault (git-synced)

Scripts de uso repetido. Se ejecutan con `py <script.py>` (Python 3.12, Windows).

## svg-pipeline/ — recreación de SVG fantasma con Mermaid

| Script | Qué hace |
|---|---|
| `vlib.py` | Resuelve rutas de la vault (`materia(semestre, key)`); constante `VAULT`. |
| `catalogo_fisica.py` | Escanea una materia y lista los SVG referenciados que no existen (fantasma) → JSON. |
| `build67.py` | Generador Física Mecánica: dict `MERMAID_SRC` por diagrama + `STD` (clases pastel compartidas) + `main()` que compila todos con `mmdc` a `.svg` (fondo blanco) y `.png` (-s 2) en `previews`. **Al importarlo corre `main()`.** |
| `descargar-material-ccpg1001.py` | Descarga PDFs/PNG del repo GitHub del profesor preservando nombres normalizados → Unidad 0. |

Pipeline estándar: `catalogo → buildNN.py (dict MMD) → mmdc → QA de previews → commit+push`.
Flujos: `QA_BY_PATH = "QA: <tramo 1>; ..."` para verificar cada flecha en los previews.
Fórmulas en vyphen: sin `<>` (rompe mmdc) — usar `∫[a→b]`, `[i=1→n]`.

## vault-maintenance/ — mantenimiento de notas

| Script | Qué hace |
|---|---|
| `fix_callouts.py` | Arregla espacios que rompen callouts (`>   ` → `>`, trailing). Default DRY. |
| `qa_links.py` | Lista TODO [[link]]/![[embed]] que no resuelve a archivo real. NFC/NFD-safe. |
| `pdf_a_texto.py` | PDF→txt + inventario (páginas, chars, encabezados) sin abrir el PDF. |

Notas del ciclo 2026-10: `build39.py` (Cálculo de una Variable) se perdió al limpiar
temp — recreable con el patrón de `build67.py`.
