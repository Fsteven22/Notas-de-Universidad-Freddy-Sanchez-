---
dg-publish: false
---

# Office (Word, PowerPoint, Excel) a Markdown

> [!info] Qué resuelve
> Leer exámenes `.docx`, clases `.pptx` y planillas `.xlsx` sin abrirlos a mano: el texto, las tablas y las imágenes reales salen en un `.md` que puedes revisar, editar y convertir en nota del vault.

## 1. Requisitos (verificados en esta PC, 26/10/2026)

| Librería | Versión | Para qué |
| --- | --- | --- |
| mammoth | 1.11.0 | `.docx` → HTML → Markdown, con imágenes extraídas |
| python-pptx | 1.0.2 | `.pptx`: texto por slide, tablas, notas del orador, imágenes |
| openpyxl | 3.1.5 | `.xlsx`: una tabla Markdown por hoja |
| markdownify | 1.2.3 | HTML → Markdown (el que usa el camino de Word) |
| markitdown | 0.1.8 | respaldo para html, csv, json, xml, epub, msg, zip |

## 2. Comandos

```bash
py office_a_markdown.py examen.docx
py office_a_markdown.py clase.pptx -o clase.md --imagenes Figuras/clase
py office_a_markdown.py notas.xlsx
```

Opciones:

| Opción | Para qué sirve |
| --- | --- |
| `-o salida.md` | nombre del `.md` (por defecto, el mismo nombre del archivo) |
| `--imagenes CARPETA` | dónde se guardan las imágenes extraídas (por defecto `<salida>_imagenes/`) |
| `--titulo "..."` | título de la nota (por defecto, el nombre del archivo) |

## 3. Qué obtienes por formato

| Formato | Resultado |
| --- | --- |
| `.docx` | texto con encabezados, **tablas conservadas** y cada imagen del documento como archivo propio |
| `.pptx` | una sección `## Slide N: título` por diapositiva, listas con su nivel, tablas, imágenes y **notas del orador** cuando existen |
| `.xlsx` | una sección `## Hoja` por hoja, con la hoja como tabla Markdown |
| otros | markitdown como respaldo (html, csv, json, xml, epub, msg, zip) |

Las imágenes se nombran con el prefijo del archivo y quedan referenciadas en Markdown normal (`![alt](carpeta/imagen.png)`), listas para copiar a `Figuras/` y convertir en embeds `![[...]]`.

## 4. Limitaciones honestas

- `.doc` y `.odt` (formatos viejos) **no** se convierten: son binarios, no OOXML. Necesitan LibreOffice.
- En `.pptx` solo se extraen las imágenes raster; los gráficos vectoriales (SmartArt, formas) no se guardan como archivo.
- En `.xlsx` se leen los **valores** guardados, no las fórmulas; si el archivo nunca se abrió en Excel, las celdas calculadas pueden venir vacías.
- El orden de lectura de un `.docx` con tablas complexas puede no coincidir con el visual; conviene revisar el `.md`.
- El OCR de un Word escaneado no existe: si el `.docx` es solo imágenes, conviértelo a PDF primero y usa el pipeline de `GUIA-PDF-A-MARKDOWN.md`.

## 5. Flujo hasta una nota del vault

1. Convierte: `py office_a_markdown.py examen.docx -o "$TMP/examen.md"`.
2. Revisa el `.md` (tablas, orden, imágenes).
3. Crea la nota en `Universidad/<semestre>/<materia>/<Unidad>/` con frontmatter: `dg-publish: true` si va al sitio y **una sola** línea `tags:`.
4. Copia las imágenes a `Universidad/Figuras/` y cambia las referencias por embeds `![[...]]`.
5. Valida: `py verificar_nota.py "ruta/nota.md"` debe salir `0`.
6. Commit solo si lo pides.

## 6. Verificación realizada (26/10/2026)

- `2023-2PAO-1E-SBD.docx` (examen real de SBD): texto con la tabla de cabecera intacta (AÑO / PERIODO / MATERIA / PROFESORES) y 5 imágenes extraídas a disco.
- `FISG1001-Metodología PIA.pptx` (diapositivas reales): 9 slides con título, 11 imágenes extraídas y numeradas por slide.
- `.xlsx` de prueba: una tabla Markdown por hoja.

## 7. Alternativas si quieres más fidelidad

- **pandoc** (`winget install JohnMacFarlane.Pandoc`): conversor universal (docx, pptx, epub, odt, latex) con Markdown directo; mejor que markitdown para documentos largos.
- **LibreOffice** (`winget install TheDocumentFoundation.LibreOffice`): convierte `.doc`/`.odt` y exporta a PDF, y así puedes pasar el pipeline PDF/OCR a Word y PowerPoint.
- **markitdown** directo (`py -m markitdown archivo.docx`): más rápido, pero deja las imágenes como `data:` inline y pierde el detalle de slides.
