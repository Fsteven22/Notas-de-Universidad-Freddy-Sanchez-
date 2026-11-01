---
dg-publish: false
---

# Nota .md a PDF (impresión limpia)

> [!info] Qué resuelve
> Convierte cualquier nota del vault en un PDF presentable: A4, márgenes de 18 mm, tablas con bordes, callouts, figuras que no se parten entre páginas, matemáticas con KaTeX y diagramas SVG. La ruta es Markdown → HTML con CSS de impresión → Edge/Chrome headless.

## 1. Uso

```bash
py md_a_pdf.py "Universidad/3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/Talleres/Tarea 2.md"
py md_a_pdf.py "ruta/nota.md" -o "salida.pdf"
py md_a_pdf.py "ruta/nota.md" --html          # deja el HTML intermedio para depurar
py md_a_pdf.py "ruta/nota.md" --landscape     # pagina horizontal (tablas anchas)
py md_a_pdf.py "ruta/nota.md" --sin-katex --sin-mermaid
```

El PDF sale junto a la nota (`nota.md` → `nota.pdf`). Rutas relativas al vault o absolutas.

## 2. Qué entiende de la sintaxis de Obsidian

| Sintaxis | Resultado en el PDF |
| --- | --- |
| `!nombre-de-archivo` (imagen o SVG) | imagen embebida, resuelta en la carpeta de la nota, luego en la raíz del vault y por último en todo el vault |
| `enlace` | texto plano (no se hipervincula) |
| `> [!note] Título` | callout con barra de color y título en negrita |
| `$...$` y `$$...$$` | renderizado con KaTeX |
| ```` ```mermaid ```` | diagrama renderizado con mermaid; si el bloque trae `%% nombre %%` y existe el SVG en el vault, se usa ese SVG |
| Frontmatter `---` | se elimina del PDF |
| Tablas, listas, código, citas | con estilos de impresión |

## 3. Límites que conviene saber

- **KaTeX y mermaid se cargan desde CDN**: requieren internet en el momento de convertir. Sin internet, la matemática queda como texto plano y los bloques mermaid sin renderizar (los SVG ya convertidos del vault sí funcionan siempre).
- El motor es Edge o Chrome en modo headless. Si no hay ninguno instalado, el script lo dice y termina.
- No resuelve **transclusiones de notas** (`!Otra Nota`): solo imágenes y SVG.
- Las rutas de imagen se resuelven por nombre en todo el vault: si hay dos archivos con el mismo nombre, gana el primero en orden alfabético. Conviene mover las imágenes a la carpeta de su nota.
- El PDF no lleva portada ni índice automático; si la nota es larga, añade un `## Índice` manual o usa la nota que ya hace de índice (`00 - Índice.md`).

## 4. Receta para publicar una tarea o taller

1. Guarda el enunciado como nota en la carpeta del taller (por ejemplo `Unidad 0 - Guias y Ejercicios/Talleres/Tarea 2.md`).
2. Deja las imágenes junto a la nota, no en la raíz del vault.
3. Convierte: `py md_a_pdf.py "Universidad/.../Talleres/Tarea 2.md"`.
4. Revisa el PDF: el enunciado debe leerse completo y las figuras nítidas.
5. Si el enunciado llegó como captura (imagen dentro de la nota), el PDF sale como imagen. Para que sea **buscable**, transcribe el enunciado a Markdown (o usa OCR) y vuelve a convertir.
6. Commit del `.md` y del `.pdf` juntos.

## 5. Verificación realizada (26/10/2026)

- `Tarea 2.md` (SBD, Talleres): nota con una sola imagen embebida → PDF de 1 página con la imagen incluida (179 KB).
- `01 - Dato, información y modelos de datos.md` (SBD, 15 páginas de nota): PDF de 16 páginas con tabla con bordes, callouts, 60 imágenes y diagramas SVG bien escalados.
- `01 - Derivada y Definición Formal.md` (Cálculo, 20 páginas): las fórmulas salen renderizadas con KaTeX, no como código.

## 6. Alternativas

- **Pandoc** (`winget install JohnMacFarlane.Pandoc`): md → docx/PDF con LaTeX, mejor para documentos con bibliografía o estilos academicos; pero exige motor LaTeX (pesado en Windows).
- **Imprimir desde Obsidian**: sirve para una nota puntual, pero pierde callouts, KaTeX y el control de márgenes.
- **El sitio del vault** (Astro + `remark-obsidian` + `rehype-katex`): publica el Markdown con la misma sintaxis; sirve para el sitio, no para un PDF descargable.
