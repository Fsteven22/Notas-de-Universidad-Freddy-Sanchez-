---
dg-publish: false
---

# 📐 FORMATO-DISENO — contrato de formato de las notas de Diseño de Software

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique. Su hermano es `FORMATO-SBD.md`, en la misma carpeta.
>
> Las **17 notas de clase** de la materia ya comparten un esqueleto de 12 secciones H2 y un
> estilo de prosa propio, que es el dueño del vault. Este contrato lo fija por escrito: cualquier
> sesión (humana o asistente) debe escribir notas de Diseño de Software que **pasen**
> `qa_formato_diseno.py`.
>
> El hermano de este contrato es `FORMATO-SBD.md`; las reglas son las mismas (R1–R14) con dos
> diferencias: el esqueleto de secciones es el de Diseño, y hay dos reglas extra (**R15** y
> **R16**) por los decks y las capturas de esta materia.

## Las 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [CCPG1042, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta). El código de la
cátedra es **CCPG1042** (en SBD es TICG1018).

### R2 · Título H1 con emoji
`# 🏗️ Naturaleza del Software y el Diseño`. Emoji visible + texto.

### R3 · Secciones H2 con emoji y el esqueleto de la materia
Las 17 notas de clase comparten este esqueleto (**12 secciones**):

```
## 🎯 Introducción
## 🧵 <Tema> (1..n secciones temáticas)
## 🗺️ Diagrama de Decisión: ¿<pregunta>?
## ⚠️ Problemas Comunes y Soluciones
## 🎯 Mejores Prácticas
## 📝 Ejercicios Propuestos
## 📋 Resumen Ejecutivo
## ✅ Metas de Aprendizaje
## 📊 Resumen Visual
## 🚀 Próximos Pasos
## 🔁 Repaso SR (flashcards)
## 🔗 Seguir estudiando
## 📚 Referencias
```

Las secciones temáticas (`🧵`) son variables: puede haber una o varias.

**Perfiles.** El validador distingue las notas por su ruta:

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | `Unidad N - …/0X - …md` | las **12** del esqueleto |
| `material` | `Unidad 0 - Guias y Ejercicios/Material de clase/…` | ninguna (**0**), pero todo H2 que exista lleva emoji |
| `indice` | notas raíz (`Diseño de Software.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) | ninguna (**0**), pero todo H2 que exista lleva emoji |

### R4 · TODO el contenido dentro de callouts
Ningún bloque de prosa, tabla, lista, embed o fórmula vive fuera de un callout. Si un diagrama
va suelto, se envuelve en un callout con título.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Acoplamiento`: tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
El callout arranca con una línea `>` sola, salvo los callouts 📖 de deck, que pueden arrancar
con prosa directo.

### R7 · Separadores internos dentro de un callout
- Antes de un embed `> ![[...]]`: línea `>` vacía.
- Antes de una tabla `> |...`: línea `>` vacía.
- Entre dos párrafos de prosa: una línea `>` vacía entre medio.
- Los items del mismo punto/lista van pegados.

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
Prefijo `> >` en dos niveles.

### R9 · Ejemplos con etiqueta en negrita
Dentro del callout: `> **Ejemplo:**`, `> **Se lee así:**`, `> **Por qué importa:**`.

### R10 · Metas de Aprendizaje con checkboxes
```
> [!note] 📋 Nivel Básico
>
> - [ ] Distingo acoplamiento de cohesión sin mirar.
```
Un callout por nivel, contenido como checkboxes.

### R11 · Flashcards SR dentro de la sección Repaso
```
#flashcards/dsw-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Pregunta?::Respuesta.
```
La línea `#flashcards/dsw-uN` queda **fuera** del callout (es una directive del plugin), pero
**todas** las líneas `- Q::A` van dentro del `> [!note] 🧠`.

### R12 · Rutas de assets correctas y existentes
`../Unidad 0 - Guias y Ejercicios/Diagramas/…` para diagramas y
`../Unidad 0 - Guias y Ejercicios/Archivos/<Tema>/…` para capturas. **Un solo nivel** de `../`
porque todas las notas de clase viven a la misma profundidad. El archivo referenciado debe existir.

Además:
- **No se embeben PDF/PPTX/DOC/XLS de clase** (`R12-clase-embebida`). Un deck se **captura como
  PNG** y se cita por número de página.
- **Todo SVG embebido tiene su `.mmd` fuente al lado** (`R12-svg-sin-mmd`).
- **Todo SVG vive en `Unidad 0 - Guias y Ejercicios/Diagramas/`** (`R12-diagrama-fuera`).

### R13 · Tags al pie
`**Tags:** #CCPG1042 #unidad1 #...` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe)
> [!warning] 🚨 La regla que separa "leer la nota" de "leer el PDF"
> Un embed sin lectura propia es una transcripción: es tan difícil de entender como el material
> original. Cada pieza visual lleva, **en las líneas siguientes**, una interpretación propia.

**Qué exige R14:**
1. **Cada PNG de captura** va seguido de una de estas etiquetas:
   `**Se lee así:**` · `**Por qué importa:**` · `**Ejemplos:**` / `**Ejemplo:**` · `**Nota:**`
   — o de prosa propia de **≥ 60 caracteres** que no sea la ruta del embed.
   La ruta del propio embed **no cuenta** como explicación.
2. **Cada SVG (mermaid)** va seguido de la misma lectura.
3. **Cada callout 📖 de deck** lleva **al menos una** de esas etiquetas en su interior.
   Excepción: los callouts 📖 de "Fuentes Consultadas" son bibliografía y no necesitan lectura.

**Etiquetas aceptadas (case-insensitive):** `Se lee así` · `Por qué importa` · `Ejemplo(s)` ·
`Nota` · `Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Para qué sirve` ·
`Qué notas` · `Pista`.

**Cómo se escribe una buena lectura** (3 párrafos, en este orden):

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | ¿Qué dice la imagen **en su propia forma**? (qué cajas hay, qué flechas, qué filas, qué palabras del deck) | 2–4 frases |
| `**Por qué importa:**` | ¿Qué **consecuencia** tiene? ¿Qué error evita? ¿Por qué la cátedra la puso? | 1–3 frases |
| `**Ejemplo:**` | ¿Cómo se aplica a **un caso propio** de la ESPOL o de la carrera? | 1 frase con caso concreto |

### R15 · Toda captura cita su deck y su página
Cada PNG de `Archivos/` tiene el nombre `<deck>-p<NN>[-<slug>].png`. En la nota, el texto
cercano al embed **cita el deck y la página**: `01b, p. 5` · `deck 04a, pp. 11-19`. Una captura
sin página citada es una imagen sin procedencia.

### R16 · Nada de material ajeno
`_texto/`, PDFs de clase (se capturan), `Contenido Extra/`, docs de `Herramientas/` — no se
referencian ni se embeben (`R12-ajeno`).

## Material que NO entra
`_texto/` (extracciones de texto de los libros, solo local), `Contenido Extra/`,
docs de `Herramientas/`.

## Receta de producción

### Diagramas (SVG)
Todos los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/` y son **mermaid**, con su
fuente `.mmd` **al lado** (R12-svg-sin-mmd).

**Naming:** `dsw-uX-YY-NN-tipo.mmd` / `dsw-uX-YY-NN-tipo.svg`
- `dsw` Diseño de Software · `uX` unidad · `YY` nota · `NN` correlativo del diagrama en esa nota.
- `tipo` ∈ catálogo:

| Sufijo | Qué es | Se dibuja como |
|---|---|---|
| `-graph` | panorama / cadena de pasos / comparación | `flowchart` |
| `-flow` | algoritmo o procedimiento con decisiones | `flowchart` |
| `-class` | diagrama de clases | `flowchart` (mermaid `classDiagram` no cubre UML completo) |
| `-use` | casos de uso | `flowchart` |
| `-seq` | secuencia temporal | `sequenceDiagram` |
| `-mind` | mapa mental / panorama de un tema | `flowchart` |

**Render:**
```
py -3.12 Herramientas/SVG-Pipeline/mmdc_ligero.py -i X.mmd -o X.svg -b white
$env:PUPPETEER_EXECUTABLE_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**Reglas de sintaxis mermaid (las que fallan sin avisar):**
- En `erDiagram`, las etiquetas de relación con `,` o `:` **no parsean** → van entre comillas.
- `<br/>` y emojis sí funcionan dentro de esas comillas.
- Un SVG **siempre** necesita su `.mmd`. Si falta, se reconstruye desde el SVG y se valida
  re-renderizando y comparando texto visible + viewBox. **Nunca** se sobrescribe un `.mmd` que ya
  está en git.

### Capturas de deck (PNG)
1. Se **captura la página** del PDF, no se embebe el PDF.
2. **DPI 140** → 1862×1027 px (láminas 16:9) o 1637×1158 px (láminas 4:3).
3. Carpeta por tema: `Archivos/Diseno-Basico/` · `Archivos/UML/` · `Archivos/Patrones/` ·
   `Archivos/Refactorizacion/` · `Archivos/Pruebas/`.
4. Naming: `dsw-<deck>-p<NN>[-<slug>].png` — `dsw-01b-p5.png`, `dsw-04a-p18-notacion-relaciones.png`.
5. En la nota se cita **con el número de página**: `01b, pp. 4-13` / `04a, p. 18`.
6. El contenido de la lámina se extrae **por texto** del PDF (`extrae_texto_pdf.py`, PyMuPDF).
   **No se leen las imágenes a ojo**: la lectura escrita sale del texto extraído.

### Nota nueva: orden de trabajo
1. Esqueleto con los 12 H2 del perfil y `---` entre ellos.
2. Callouts con definiciones y ejemplos (**R4**, **R5**, **R6**, **R9**).
3. Diagramas: escribir el `.mmd`, renderizar, embeber dentro de un callout, y **leerlo** (**R14**).
4. Capturas: capturar la página correcta, embeber, y **leerla** (**R14**, **R15**).
5. Ejercicios con solución plegada (**R8**).
6. Metas con checkboxes (**R10**) y flashcards dentro del callout 🧠 (**R11**).
7. `**Tags:**` al pie (**R13**).
8. Auditar y corregir hasta 0 hallazgos.

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_diseno.py" --solo "3er Semestre/Diseño de Software"
```
Severidades: **H** (error duro, rompe lectura o el sitio) y **W** (desviación de formato).
`--estricto` también hace fallar los W. `--fix-rutas` repara automáticamente los embeds con
profundidad incorrecta cuando la profundidad correcta sí existe.

> [!success] ✅ Estado actual
> _Pendiente de completar: la auditoría de arranque registró 684 hallazgos en las 24 notas
> (línea base 2026-11-09). Se cierra por bloques: assets → `.mmd` → formato mecánico → lecturas._

## Nota de ubicación

Este contrato **no** vive en `3er Semestre/Diseño de Software/`: es una herramienta, y el sitio
publica la carpeta de la materia. Vive en `Universidad/Herramientas/Mantenimiento/`, junto al
validador que lo aplica (`qa_formato_diseno.py`) y a su hermano (`FORMATO-SBD.md`).
