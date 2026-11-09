---
dg-publish: false
---

# 📐 FORMATO-SBD — contrato de formato de las notas de Sistema de Bases de Datos

> [!info] 📖 Fuente única de verdad
> Nota de referencia: `Unidad 1 - Modelos de Datos y ER/01 - Dato, información y modelos de datos.md` (la "01"), personalmente corregida por el dueño del vault. Cada regla cita los números de línea como ejemplo literal. Este archivo es el contrato: cualquier sesión (humana o asistente) debe escribir notas SBD que **pasen** `qa_formato_sbd.py`.
>
> Además del formato, el contenido debe estar **bien explicado y bien documentado para fácil lectura**: una nota que solo transcribe el PDF del deck es tan útil como leer el PDF. Ver **R14**.

## Las 14 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [TICG1018, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta).

### R2 · Título H1 con emoji
`# 💾 Dato, Información y Modelos de Datos` (línea 6). Emoji visible + texto.

### R3 · Secciones H2, cada una con emoji y separadas por `---`
El esqueleto mínimo (líneas 8, 23, 233, 280, 296, 305, 319, 328):
```
## 🎯 Introducción
## 📋 Definiciones Formales
## 📝 Ejercicios Propuestos
## 🎯 Metas de Aprendizaje
## 📚 Referencias
## 🔁 Repaso SR (flashcards)
## 🔗 Conexiones
## 🔗 Seguir estudiando
```
Secciones temáticas extra van entre Definiciones y Ejercicios (líneas 105, 151, 168, 187, 201).

**Perfiles.** No todas las notas son una lección; el validador las distingue por nombre:

| Perfil | Se applies a | H2 requeridas |
|---|---|---|
| `clase` | `Unidad N - …/0X - …md` | Introducción · Definiciones Formales · Ejercicios Propuestos · Metas de Aprendizaje · Referencias · Repaso SR · Conexiones · Seguir estudiando (**8**) |
| `guia` | `Guía de Problemas N - ….md` | Introducción · Ejercicios Propuestos · Referencias · Conexiones · Seguir estudiando (**5**) |
| `indice` | notas raíz (`Sistema de Bases de Datos.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) | ninguna en obligatoria (**0**), pero todo H2 que exista lleva emoji |

### R4 · TODO el contenido dentro de callouts
La nota de referencia tiene **0 líneas de prosa, tabla o lista fuera de callouts** (la única excepción es 1 diagrama suelto en la línea 164, que la auditoría marca con W). Todo bloque textual, tabla, embed y fórmula va dentro de un callout.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Dato` (línea 27): tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
23 de 26 callouts de la referencia lo hacen (líneas 11, 28, 38, 48…). La excepción son los callouts 📖 de deck de cátedra, que arrancan con prosa directo (líneas 72-73, 83-84, 92-93).

### R7 · Separadores internos dentro de un callout
- Entre dos párrafos de prosa: una línea `>` vacía entre medio (líneas 29-30).
- Antes de un embed `> ![[...]]`: línea `>` vacía (el 100% de los embeds de la referencia; 0 violaciones).
- Antes de una tabla `> |...`: línea `>` vacía (líneas 60-61).
- Los items del mismo punto/lista van pegados (líneas 15-17; 284-286): solo la prosa/tablo/imagen pide separador.

### R8 · Callout anidado plegado en los ejercicios
```
> [!example] 📋 Planteamiento
>
> Enunciado...
>
> > [!success]- ✅ Solución
> >
> > Respuesta...
```
(líneas 237, 244). Prefijo `> >` en dos niveles.

### R9 · Ejemplos con etiqueta negrita
Dentro del callout, la cierre va con etiqueta en negrita: `> **Ejemplos:**`, `> **Se lee así:**`, `> **Por qué importa:**` (líneas 33, 130, 146, 170).

### R10 · Metas de Aprendizaje con checkboxes
```
> [!note] 📋 Nivel Básico
>
> - [ ] Defino dato, información y modelo sin mirar.
```
(líneas 282-286). Un callout por nivel, contenido como checkboxes.

### R11 · Flashcards SR dentro de la sección Repaso
```
#flashcards/bd-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Pregunta?::Respuesta.
```
(líneas 307-315). Con guion `- ` delante de cada flashcard. Las flashcards del plugin SR (`Q::A` + `<!--SR:...-->`) no se tocan cuando existen.

> [!tip] 🧠 Las flashcards van **dentro** del callout 🧠
> La línea `#flashcards/bd-uN` queda **fuera** del callout (es una directive del plugin), pero **todas** las líneas `- Q::A` van dentro del `> [!note] 🧠`. Una flashcard suelta en el cuerpo de la nota no la ve el plugin ni cumple R4.

### R12 · Rutas de assets correctas y existentes
`../Unidad 0 - Guias y Ejercicios/Diagramas/...` (líneas 19, 31, 41…). **Un solo nivel** porque todas las notas viven a la misma profundidad (`Sistema de Bases de Datos/Unidad N - .../`): `../../` rompe la resolución. El archivo referenciado debe existir.

Además: **no se embeben PDF/PPTX/DOC/XLS de clase** (`R12-clase-embebida`). Un taller, un deck o un enunciado se **capturan como PNG** y se citan por número de página.

### R13 · Tags al pie
`**Tags:** #TICG1018 #...` al final (línea 340).

### R14 · Todo lo visual se explica (no se transcribe)
> [!warning] 🚨 La regla que separa "leer la nota" de "leer el PDF"
> Un embed o un bloque de deck **sin lectura propia** es una transcripción: es tan difícil de entender como el material original. Cada pieza visual lleva, **en las líneas siguientes**, una interpretación propia.

**Qué exige R14 (mecanizado en `qa_formato_sbd.py`):**

1. **Cada PNG de deck** va seguido de una de estas etiquetas:
   `**Se lee así:**` · `**Por qué importa:**` · `**Ejemplos:**` / `**Ejemplo:**` · `**Nota:**`
   — o de prosa propia de **≥ 60 caracteres** que **no** sea la ruta del embed.
   La ruta del propio embed **no cuenta** como explicación (si no, la regla se cumple sola).
2. **Cada SVG (mermaid)** va seguido de la misma lectura.
3. **Cada callout 📖 de deck** (los que citan láminas del PDF del profe) lleva **al menos una** de esas etiquetas en su interior.
   Excepción: los callouts 📖 de **"Fuentes Consultadas"** son bibliografía y no necesitan lectura.

**Etiquetas aceptadas (case-insensitive):** `Se lee así` · `Por qué importa` · `Ejemplo(s)` · `Nota` · `Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Para qué sirve` · `Qué notas` · `Pista`.

**Cómo se escribe una buena lectura** (3 párrafos, en este orden):

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | ¿Qué dice la imagen **en su propia forma**? (qué cajas hay, qué flechas, qué filas, qué columnas, qué palabras del deck) | 2–4 frases |
| `**Por qué importa:**` | ¿Qué **consecuencia** tiene? ¿Qué error evita? ¿Por qué la cátedra la puso? | 1–3 frases |
| `**Ejemplo:**` | ¿Cómo se aplica a **un caso propio** de la ESPOL o de la carrera? | 1 frase con caso concreto |

> [!example] ✅ Bloque modelo (callout de deck)
> ```
> > [!info] 📖 El deck de cátedra: la 1FN en la pizarra (slides04 y BD 02.3)
> >
> > El deck del Ing. Magallanes define la 1FN como *"una tabla donde la intersección… "*
> >
> > ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p8.png]]
> >
> > **Se lee así:** la lámina (p. 8) es la definición y el ejemplo roto en la misma pantalla…
> >
> > **Por qué importa:** la raíz común de los cinco…

## Material que NO entra
`_texto/`, PDFs de clase (se capturan), `Contenido Extra/`, docs de `Herramientas/` — (carriles CLAUDE2 y existentes en qa_material_nuevo.py).

## Receta de producción

### Diagramas (SVG)
Todos los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/` y son **mermaid**, con su fuente `.mmd` **al lado** (R12-svg-sin-mmd).

**Naming:** `uX-YY-NN-tipo.mmd` / `uX-YY-NN-tipo.svg`
- `uX` unidad · `YY` nota (01, 02…) · `NN` correlativo del diagrama en esa nota.
- `tipo` ∈ catálogo:

| Sufijo | Qué es | Se dibuja como |
|---|---|---|
| `-graph` | panorama / cadena de pasos / comparación | `flowchart` |
| `-flow` | algoritmo o procedimiento con decisiones | `flowchart` |
| `-er` | esquema relacional | `erDiagram` |
| `-tree` | jerarquía | `flowchart TD` |
| `-seq` | secuencia temporal | `sequenceDiagram` |
| `-state` | máquina de estados | `stateDiagram-v2` |

**Render:**
```
py -3.12 Herramientas/SVG-Pipeline/mmdc_ligero.py -i X.mmd -o X.svg -b white
$env:PUPPETEER_EXECUTABLE_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**Reglas de sintaxis mermaid (las que fallan sin avisar):**
- En `erDiagram`, las etiquetas de relación con `,` o `:` **no parsean** → van entre comillas: `A ||--o{ B : "1:1"`.
- `<br/>` y emojis sí funcionan dentro de esas comillas.
- Un SVG **siempre** necesita su `.mmd`. Si falta, se reconstruye desde el SVG (`svg2mmd.py`) y se valida re-renderizando y comparando tokens/viewBox (`validar_mmd.py`). **Nunca** se sobrescribe un `.mmd` que ya está en git.

### Capturas de deck (PNG)
1. Se **captura la página** del PDF, no se embebe el PDF.
2. **DPI 140** → 1862×1027 px (láminas 16:9) o 1637×1158 px (láminas 4:3).
3. Carpeta por tema: `Archivos/SQL/` · `Archivos/Modelos-ER/` · `Archivos/Logico-Conversion/` · `Archivos/Talleres/`.
4. Naming:
   - `bd-sNN-pX.png` (slides01…slides06)
   - `bd-04-pX.png` (deck `BD04 DDL_dml_create_alter_drop.pdf`)
   - `bd-023-pX.png` (`BD 02.3 Normalizacion.pdf`)
   - `bd-sql-avanzado-pX.png` (`SQL Avanzado.pptx`)
   - `bd-tallerN*.png` (talleres)
5. En la nota se cita **con el número de página**: `slides04, pp. 2-4` / `BD 02.3, p. 14` / `Taller 4_20agorep.pdf, p. 1`.
6. El contenido de la lámina se extrae **por texto** del PDF (`extrae_texto_pdf.py`, PyMuPDF) o del PPTX (`pptx_texto.py`). **No se leen las imágenes a ojo**: la lectura escrita sale del texto extraído.

### Nota nueva: orden de trabajo
1. Esqueleto con los H2 del perfil y `---` entre ellos.
2. Callouts con definiciones y ejemplos (**R4**, **R5**, **R6**, **R9**).
3. Diagramas: escribir el `.mmd`, renderizar, embeber, y **leerlo** (**R14**).
4. Capturas: capturar la página correcta, embeber, y **leerla** (**R14**).
5. Ejercicios con solución plegada (**R8**).
6. Metas con checkboxes (**R10**) y flashcards dentro del callout 🧠 (**R11**).
7. `**Tags:**` al pie (**R13**).
8. Auditar y corregir hasta 0 hallazgos.

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_sbd.py" --solo "3er Semestre/Sistema de Bases de Datos"
```
Severidades: **H** (error duro, rompe lectura o el sitio) y **W** (desviación de formato). `--estricto` también hace fallar los W. `--fix-rutas` repara automáticamente los embeds con profundidad incorrecta cuando la profundidad correcta sí existe.

Complementarios (mismo directorio de trabajo):
- `scan_calidad.py` → embeds y callouts 📖 **sin lectura propia** (el detector que define el trabajo de R14).
- `scan_artefactos.py` → caracteres CJK, palabras en inglés y palabras pegadas introducidos al reescribir.

> [!success] ✅ Estado actual
> Las **20 notas** de SBD pasan `qa_formato_sbd.py` con **0 hallazgos**, y los **268 embeds visuales** + **37 callouts 📖 de deck** tienen lectura propia (R14 en 0 sin lectura).
