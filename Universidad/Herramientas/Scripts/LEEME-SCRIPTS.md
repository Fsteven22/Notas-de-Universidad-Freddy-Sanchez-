---
dg-publish: false
---

# 🛠️ Scripts del vault (no se publican)

> [!info] ℹ️ Qué hay aquí
> Utilidades propias en Python (solo librería estándar). Los `.py` nunca se publican al Garden (solo viajan `.md` con `dg-publish: true`). Flujo antes de dar por terminada una nota: **verificar → limpiar → volver a verificar**.

## `verificar_nota.py` — auditoría pre-entrega (solo lee)

```bash
py verificar_nota.py "ruta/nota.md"
```

Revisa: frontmatter (`dg-publish`, sin blancos, tags), callouts huérfanos, líneas vacías intrusas, fences desbalanceados o con líneas vacías adentro, mermaid dentro de callouts (aviso: en Live Preview se ve como código), embeds que no resuelven, tablas con pipes disparejos, headers indentados/pegados y finales de línea (CRLF/LF/mixto). Sale `0` si está limpia.

## `limpiar_espacios.py` — limpiador seguro

```bash
py limpiar_espacios.py "ruta/nota.md"        # dry-run (solo reporta)
py limpiar_espacios.py "ruta/nota.md" --fix # aplica
```

Colapsa blancos múltiples y separadores `>` dobles, quita trailing whitespace, **preserva CRLF/LF** y nunca toca blanks entre callouts hermanos ni dentro de fences. Guard nuevo: si los fences están desbalanceados o con quoting disparejo, fuerza dry-run y no aplica (arregla con `verificar_nota.py` primero).

## `kit_recuperacion.py` — kit de recuperación FESD (dry-run por defecto)

Creado tras el incidente del 19/10/2026 (un script de tags con doble `tags:` sobrescribió 24 notas de FESD con stubs y con el contenido de otra nota). Todos los comandos que modifican archivos (`restore`, `repath`, `pipes`) son dry-run por defecto y solo escriben con `--aplicar`; `daniadas`, `sweep` y `compa` son siempre de solo lectura.

```bash
py kit_recuperacion.py daniadas 8a89bcf 6424ecf          # lista .md dañados entre refs
py kit_recuperacion.py restore 8a89bcf 6424ecf           # dry-run; --aplicar escribe
py kit_recuperacion.py repath --aplicar                  # arregla embeds '../Diagramas'/'../Anexos'
py kit_recuperacion.py pipes "Unidad 3 - Circuitos integrados" --aplicar
py kit_recuperacion.py sweep                             # verificar_nota.py en todas las notas FESD
py kit_recuperacion.py compa 5ba8f1b "Universidad/.../nota.md"   # dif cuerpo vs ref
```

La restauración reemplaza el cuerpo del archivo por el contenido en `git show <ref_ok>:<ruta>` (con guardado que preserva CRLF/LF) y garantiza UNA línea `tags:` correcta por unidad + `dg-publish: true` dentro del frontmatter.

### Regla anti doble-`tags:` (la del incidente)

Ningún script inserta una línea `tags:` si la nota ya tiene una en sus primeras 12 líneas. Invariantes: la nota tiene CERO o UNA línea `tags:`, dentro del frontmatter, nunca dos ni fuera del `---` limítrofe. Los stubs de ~500/750/980 bytes en FESD eran la firma del script roto del 19/10 — si reaparecen, `kit_recuperacion.py restore <ref_ok> <ref_dano> --aplicar`.

### Capa de prevención (añadida tras el incidente)

`verificar_nota.py` ahora falla cuando ve: más de una línea `tags:` en el frontmatter, un segundo bloque `---` en la cabecera (frontmatter duplicado), `tags:` sueltas después del frontmatter, o secuencias `\r\r` (endings corruptos por reescrituras dobles).

`auditoria.py` (barrido del vault) añadió checks: **9** múltiples `tags:` por archivo, **10** cuerpos clónicos exactos (md5), **11** cuerpos casi-iguales ≥ 0.93 de similaridad (contenido cruzado: nota A rellenada con nota B), **12** `\r\r` en bytes crudos.

`kit_recuperacion.py` añadió:
- `fix-tags [subcarpeta|nota] [--aplicar]` — repara notas con doble `tags:`/segundo `---`/`tags:` suelta: conserva UNA línea tags (la primera) y limpia el cuerpo.
- `dupez [subcarpeta]` — clones exactos + contenido cruzado (similaridad ≥ 0.93, prefiltrada por H1 y tamaño).
- `guardian [subcarpeta]` — chequeo completo (verify + clones + cruzado); sugiere el comando de reparación. Correrlo tras cualquier sesión de scripts que toquen notas.

## `referencias.py` — auditoría de referencias entre notas FESD

```bash
py referencias.py                       # dry-run completo de la materia
py referencias.py --aplicar             # agrega la sección a las sin referencias
py referencias.py --min 3               # exigir más links inline para dar OK
```

Audita cada nota: OK si tiene sección `## 📚 Referencias` (fuentes, estilo Unidad 1) o si enlaza a ≥ 2 notas de la materia; `SIN REF` si no tiene ninguna. Con `--aplicar`, a las `SIN REF` les agrega `## 🔗 Relacionadas` al final con links a las notas hermanas de su carpeta (o a la MOC de la materia si es nota única no tiene hermanas). Nunca inventa citas bibliográficas.

## Diagramas mermaid → SVG (receta)

Los bloques mermaid dentro de callouts no renderizan en Live Preview ni confiable en Garden: se convierten a SVG y se incrustan en la nota con un embed de Obsidian que apunta al archivo `.svg`. La fuente `.mmd` se guarda junto al `.svg` para reeditar.

```bash
mmdc -i diagrama.mmd -o diagrama.svg
```

Convención de nombres BD: `uX-NN-tipo.svg` (unidad-nota-posición-tipo: `er`, `flow`, `graph`) y `ejNN-tema.svg` para guías. Tras reemplazar, correr `verificar_nota.py` (chequea que cada embed resuelva).

## Figuras de dependencias (matplotlib)

`Temp/opencode/bdstrips.py` genera tiras de dependencias estilo examen (cajas + flechas arriba/abajo + corchete PK) en SVG. Es desechable por figura; si se vuelve rutina, traer la función aquí.

## PDF → Markdown con OCR (`convertir_pdf.py`)

Convierte PDFs a Markdown limpio para archivarlos en el vault y consumirlos desde OpenCode o un modelo local. Tres ejecutables que van juntos en esta carpeta:

```bash
py pdf_a_markdown.py "material.pdf" -o "material.md"        # PDF con capa de texto (markitdown, sin OCR)
py pdf_ocr_a_markdown.py "escaneado.pdf" --split            # PDF escaneado (OCR Tesseract, un .md por pagina)
py convertir_pdf.py "material.pdf"                          # decide solo; acepta --motor, --lang, --split
```

Motor OCR: Tesseract 5.4 en `C:\Program Files\Tesseract-OCR` (ya con `spa.traineddata` y agregado al PATH del usuario). **No usa Poppler**: el renderizado de páginas lo hace PyMuPDF, por eso `pdf2image` sobra. Salida: `0` ok, `1` error, `2` PDF inexistente.

Dependencias (excepción a la regla de "solo librería estándar" de este folder): `markitdown`, `pymupdf4llm==1.28.2` (la `2.0` de PyPI viene sin módulos), `pymupdf`, `pytesseract`, `pillow`, `ocrmypdf`.

Guía completa con rutas de texto/OCR, flujo PDF → nota del vault, troubleshooting y consumo con OpenCode/Qwen: **`GUIA-PDF-A-MARKDOWN.md`**.

## PDF → nota del vault (`pdf_a_nota_vault.py`)

Convierte un PDF en una nota de Obsidian lista: frontmatter (`dg-publish` + **una sola** línea `tags:`), callout de fuente, encabezados del PDF bajada un nivel (un solo H1) y las imágenes raster de cada página extraídas a `Universidad/Figuras/` con embeds `![[...]]` relativos a la nota.

```bash
py pdf_a_nota_vault.py "material.pdf" --nota "Universidad/3er Semestre/Materia/Unidad 1 - X/material.md" --tags "materia, unidad1" --aplicar
```

**Dry-run por defecto**: sin `--aplicar` solo muestra el plan. No sobrescribe notas existentes salvo `--forzar`, y al terminar corre `verificar_nota.py` sobre la nota creada (debe salir `0`).

## Office → Markdown (`office_a_markdown.py`)

Lee `.docx`, `.pptx` y `.xlsx` sin abrirlos: texto, tablas y **imágenes reales** en disco (no `data:` inline).

```bash
py office_a_markdown.py examen.docx
py office_a_markdown.py clase.pptx -o clase.md --imagenes Figuras/clase
py office_a_markdown.py notas.xlsx
```

Motores: mammoth (docx, HTML→Markdown), python-pptx (pptx: slide a slide, tablas, notas del orador, imágenes), openpyxl (xlsx: tabla por hoja), markitdown de respaldo para html/csv/json/xml/epub/msg/zip. `.doc` y `.odt` viejos no se convierten (requieren LibreOffice).

Guía completa: **`GUIA-OFFICE-A-MARKDOWN.md`**.

## Notas → flashcards (`notas_a_flashcards.py`)

Extrae los bloques de definición de tus notas (`> [!note] Definición — <término>`) y arma tarjetas con el formato del vault: `## 🔁 Repaso SR (flashcards)`, el tag `#flashcards/<materia>-<unidad>`, el callout `> [!note] 🧠 Repasa...` y líneas `- ¿<término>?::<definición>`.

```bash
py notas_a_flashcards.py --todo                                    # dry-run de todo el vault
py notas_a_flashcards.py --carpeta "Universidad/3er Semestre/Sistema de Bases de Datos"
py notas_a_flashcards.py --nota "Universidad/.../01 - Dato, informacion y modelos de datos.md" --aplicar
py notas_a_flashcards.py --carpeta "Universidad/3er Semestre" --tag flashcards/bd-u3 --aplicar --limite 5
```

Dry-run por defecto (muestra cada tarjeta antes de escribir). No borra nada: solo inserta tarjetas nuevas al final de la lista existente y crea la sección si la nota no tenía una. Filtros: término de 1-8 palabras que empiece en mayúscula, sin `**`/`$`/`?`, y respuesta de 15-320 caracteres con al menos 4 palabras de texto (descarta fórmulas sueltas, listas y encabezados). Anti-duplicado: salta el término si ya aparece en alguna tarjeta existente, si alguna tarjeta ya lo menciona en su pregunta, o si la definición coincide ≥ 60 % con una respuesta previa. Al final corre `verificar_nota.py` por nota.

Medición en el vault (26/10/2026): 813 notas revisadas → 105 notas con tarjetas propuestas y 200 tarjetas. El tag se deduce de la ruta (materia + unidad) o se reutiliza el que ya tiene la nota; `--tag` lo fuerza.

## Nota .md → PDF (`md_a_pdf.py`)

Markdown → HTML con CSS de impresión → Edge/Chrome headless. A4, márgenes de 18 mm, tablas con bordes, callouts, figuras que no se parten, KaTeX para matemáticas y mermaid para diagramas.

```bash
py md_a_pdf.py "Universidad/3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/Talleres/Tarea 2.md"
py md_a_pdf.py "ruta/nota.md" -o "salida.pdf" --html --landscape
```

Resuelve los embeds de imagen y SVG (`![[nombre-de-archivo]]`) buscando en la carpeta de la nota, luego en la raíz del vault y por último en todo el vault; convierte `> [!note]` en callout con estilos; elimina el frontmatter. KaTeX y mermaid se cargan desde CDN (requieren internet en el momento de convertir). No resuelve transclusiones de notas (`![[Otra Nota]]`).

Guía completa y receta para publicar tareas: **`GUIA-MD-A-PDF.md`**.

## Registro de patrones (error → fix → script)

- Ejercicio/example vacío (header sin cuerpo, ej. Inglés U1-01 Ej.4): completar con el drill real; detecta con `detectar_vacios.py`. Falsos positivos conocidos: `###`→`####` con contenido, callout usado como título de sección, contenido inline en la línea del header.
- `> [!example]` usado como título (`Machine Learning.md`): convertir a `###`.

- Dentro de fences en callouts: ni líneas vacías (cortan el quote) ni líneas solo con `>` (salen literales) — separar con comentarios reales.
- El `success` de solución va anidado DENTRO del `example`, nunca suelto.
- Flashcards (`Pregunta::Respuesta`): para notas nuevas, siempre a nivel superior, fuera de callouts (formato documentado). Las que ya viven en callouts con datos `<!--SR:...-->` SÍ las lee el plugin (probado) — no migrar mazos que funcionan; solo unificar secciones mezcladas moviendo tarjeta + comentario juntos.
- Rutas de embeds: relativas a la carpeta de la nota; tras mover archivos, re-verificar.
