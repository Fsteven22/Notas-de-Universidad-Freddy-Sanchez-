---
dg-publish: false
---

# PDF a Markdown: guía de uso (texto y OCR)

> [!info] Qué resuelve
> Convertir PDFs (con texto real o escaneados) a Markdown limpio, listo para archivarse en el vault, editarse a mano y consumirse desde OpenCode o un modelo local. El pipeline **no usa Poppler**: el OCR se hace con Tesseract + PyMuPDF, que ya están en esta PC.

## 1. Decisión en 5 segundos

| Cómo se ve el PDF | Tipo | Qué correr |
| --- | --- | --- |
| Puedes seleccionar y copiar texto | Con capa de texto | `py pdf_a_markdown.py archivo.pdf` |
| Es una foto, una diapositiva escaneada | Escaneado | `py pdf_ocr_a_markdown.py archivo.pdf` |
| No sabes | Automático | `py convertir_pdf.py archivo.pdf` |
| Documento largo (100+ páginas) | Cualquiera | añade `--split` |

`convertir_pdf.py` decide solo: si alguna página tiene capa de texto usa MarkItDown; si el PDF es puro escaneo hace OCR. Si el motor elegido falla, prueba el siguiente y al final te dice qué falló en cada intento.

## 2. Requisitos (verificados en esta PC, 26/10/2026)

| Pieza | Estado | Detalle |
| --- | --- | --- |
| Python | 3.12.3 | `C:\Users\Steven Sànchez\AppData\Local\Programs\Python\Python312` |
| markitdown | 0.1.8 | extrae capa de texto (pdfminer) |
| pymupdf | 1.28.2 | renderiza páginas a imagen sin Poppler |
| pymupdf4llm | 1.28.2 | Markdown con layout + OCR automático |
| pytesseract + Pillow | 0.3.13 | OCR manual página por página |
| ocrmypdf | 17.13.0 | genera PDF con capa de texto (Ruta C) |
| Tesseract | 5.4.0 | `C:\Program Files\Tesseract-OCR`, con `eng`, `osd` y `spa` |

Tesseract ya tenía `spa.traineddata`, así que el OCR en español funciona sin descargas extra. Se agregó `C:\Program Files\Tesseract-OCR` al PATH del usuario, por eso `tesseract` responde en cualquier terminal nueva.

**Poppler no está instalado y no hace falta.** Los tutoriales que usan `pdf2image` fallan aquí con `PDFInfoNotInstalledError`; este pipeline no usa `pdf2image`.

## 3. Los tres ejecutables

| Archivo | Qué hace | Motor |
| --- | --- | --- |
| `convertir_pdf.py` | CLI completo: decide, hace fallback, y expone todas las opciones | auto |
| `pdf_a_markdown.py` | Atajo para PDF con texto real | markitdown |
| `pdf_ocr_a_markdown.py` | Atajo para PDF escaneado | pymupdf4llm + Tesseract |

Opciones disponibles:

| Opción | Para qué sirve |
| --- | --- |
| `-o salida.md` | nombre del `.md` de salida (por defecto, el mismo nombre del PDF) |
| `--split` | además del `.md` único, deja una carpeta con un `.md` por página |
| `--lang spa+eng` | idiomas de Tesseract (por defecto `spa+eng`) |
| `--motor {auto,markitdown,pymupdf4llm,manual}` | fuerza un motor; `manual` es OCR página por página con PyMuPDF + pytesseract |

Códigos de salida: `0` todo bien, `1` error (el detalle sale en stderr), `2` el PDF no existe. Sirve para encadenar con otro script sin adivinar.

Los tres archivos van juntos en la misma carpeta: los dos atajos son wrappers que llaman a `convertir_pdf.py`.

## 4. Ruta A: PDF con texto real (rápido, sin OCR)

```bash
py pdf_a_markdown.py "Universidad/2do Semestre/.../material.pdf" -o "material.md"
```

Los comandos se corren desde esta carpeta (`Scripts`); las rutas de los PDFs pueden ser absolutas o relativas a la raíz del vault (`C:\Users\Steven Sànchez\OneDrive\OneSyncFiles`).

Qué esperar: texto plano en Markdown, sin paginación forzada. Deja el `.md` junto al material de apoyo dentro de la carpeta de la unidad. MarkItDown respeta los acentos **si el PDF los codifica bien**; algunos PDFs exportados con Helvetica/WinAnsi traen los acentos rotos en la capa de texto y eso ya es defecto del archivo original, no del conversor. En ese caso el script avisa con un `Aviso:` y conviene regenerar el PDF o usar OCR sobre la imagen.

## 5. Ruta B: PDF escaneado (OCR)

```bash
py pdf_ocr_a_markdown.py "apuntes-escaneados.pdf" -o "apuntes.md"
```

Qué esperar: Tesseract reconoce el texto de la imagen y PyMuPDF4LLM arma el Markdown respetando el layout. Limitaciones honestas del OCR: no inventa tablas (quedan como texto corrido), puede partir palabras y los títulos dependen de la calidad del escaneo.

Para documentos largos, divide:

```bash
py pdf_ocr_a_markdown.py "libro.pdf" --split --lang spa+eng
```

Sale `libro.md` y una carpeta `libro/` con `pagina-0001.md`, `pagina-0002.md`, etc. Esa carpeta es la que conviene alimentar al modelo, porque una sola nota de 400 páginas no entra en contexto.

## 6. Ruta C: OCR de mejor calidad (OCRmyPDF)

Cuando el escaneo está torcido, con ruido de fondo o quieres conservar el PDF buscable:

```bash
py -m ocrmypdf -l spa --force-ocr "entrada.pdf" "entrada_ocr.pdf"
py pdf_a_markdown.py "entrada_ocr.pdf" -o "entrada.md"
```

Ventaja: `entrada_ocr.pdf` queda con capa de texto real (buscable, imprimible) y el Markdown sale mucho más limpio porque ya no hay OCR en tiempo real. Requiere Tesseract en el PATH, que ya está.

## 7. De PDF a nota del vault: el flujo completo

1. **Convertir** con la ruta que corresponda (sección 1).
2. **Revisar** el `.md` a ojo: acentos, tablas, títulos, orden de columnas. El OCR nunca es perfecto.
3. **Limpiar** formato: `py limpiar_espacios.py "ruta/nota.md" --fix` (script del vault, ver `LEEME-SCRIPTS.md`).
4. **Convertir en nota**: copia el `.md` a `Universidad/<semestre>/<materia>/`, con frontmatter (`dg-publish: true` si va al Garden, `dg-publish: false` si es material interno) y **una sola** línea `tags:`.
5. **Auditar**: `py verificar_nota.py "ruta/nota.md"` debe salir con `0`.
6. **Diagramas**: si el PDF traía gráficos, genera los SVG y embébelos con la sintaxis de embed de Obsidian (receta en `LEEME-SCRIPTS.md`).
7. **Commit** solo si lo pides.

Criterio de "listo": `verificar_nota.py` sale `0`, los acentos se leen bien, y la nota responde preguntas concretas (no "resume todo", sino "¿qué dice la unidad 3 sobre el teorema X y dónde está escrito?").

## 8. Usarlo con OpenCode o un modelo local

- `@archivo.md` en el chat adjunta el archivo; OpenCode lo lee por partes, no vuelca el documento entero de golpe. Pide secciones concretas ("resume la sección 3") en vez de "léete todo".
- Para documentos largos, usa `--split` y apunta a la página concreta: `@carpeta/pagina-0042.md`.
- Tus modelos locales (`ollama list`: `qwen2.5-coder:1.5b`, `3b`, `7b`) son de código, **no de visión**: no pueden "ver" un PDF escaneado. El OCR ya resolvió esa parte y el modelo solo lee el `.md`.
- Prompt que funciona: "Con @nota.md responde: ¿qué condiciones debe cumplir X? Cita la sección y no inventes lo que no está".

## 9. Problemas frecuentes

| Síntoma | Causa real | Solución |
| --- | --- | --- |
| `TesseractNotFoundError` | Tesseract no está en el PATH de esa terminal | el script ya busca en `C:\Program Files\Tesseract-OCR`; si aun así falla, abre una terminal nueva |
| `ModuleNotFoundError: pymupdf4llm` | la versión `2.0` de PyPI viene sin módulos | `py -m pip install --force-reinstall "pymupdf4llm==1.28.2"` |
| `PDFInfoNotInstalledError` | falta Poppler (solo si usas `pdf2image`) | `winget install oschwartz10612.Poppler`, o no usar `pdf2image` |
| El `.md` sale vacío | el PDF es escaneo y usaste la ruta de texto | usa `pdf_ocr_a_markdown.py` |
| Acentos raros en la consola | la consola de PowerShell usa cp437/cp850 | el `.md` está bien en UTF-8; ábrelo con editor o `chcp 65001` |
| `context exceeds model limit` | nota demasiado larga para el modelo | `--split` y pide páginas concretas |
| OCR con palabras pegadas | escaneo de baja calidad | Ruta C con OCRmyPDF, que deskewa y rota páginas |

## 10. Verificación realizada (26/10/2026)

- `mi_documento.pdf` (con capa de texto) → motor markitdown → acentos correctos (`á é í ó ú ñ` verificado por codepoint).
- `mi_documento_imagen.pdf` (solo imagen) → OCR con Tesseract en español → texto recuperado.
- PDF escaneado de 2 páginas con `--split` → `pagina-0001.md` y `pagina-0002.md` con el contenido correcto de cada página.
- Códigos de salida `0`, `1` y `2` comprobados.

## 11. Instalarlo en otra PC

```bash
py -m pip install markitdown "pymupdf4llm==1.28.2" pymupdf pytesseract pillow ocrmypdf
winget install UB-Mannheim.TesseractOCR
```

Después: copia `spa.traineddata` a `C:\Program Files\Tesseract-OCR\tessdata\` (la instalación por winget trae solo `eng` y `osd`) y agrega `C:\Program Files\Tesseract-OCR` al PATH.

Alternativas si Tesseract no convence: Poppler por winget (`oschwartz10612.Poppler`) solo si quieres `pdf2image`; OCR en la nube (Azure AI Document Intelligence u OpenAI vision vía el plugin OCR de MarkItDown) para máxima calidad, con API key y costo por página; o un modelo de visión local en Ollama (requiere descargar uno tipo `qwen2.5vl` o `minicpm-v`, los `qwen2.5-coder` que tienes no son de visión).
