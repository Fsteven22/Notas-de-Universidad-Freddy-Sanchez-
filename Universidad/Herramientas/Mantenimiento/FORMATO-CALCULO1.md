---
dg-publish: false
---

# 📐 FORMATO-CALCULO1 — contrato de formato de las notas de Cálculo de una Variable

> [!info] 📖 Fuente única de verdad
> Este contrato **adopta el de Sistema de Bases de Datos** (`FORMATO-SBD.md`, reglas R1..R14) sin
> rebajarlo: la nota de referencia es `Universidad/3er Semestre/Sistema de Bases de Datos/Unidad 1 - Modelos de Datos y ER/01 - Dato, información y modelos de datos.md`, corregida por el dueño.
> El validador `qa_formato_calculo1.py` **importa** `qa_formato_sbd.py` y ejecuta su mismo núcleo
> (R1..R14) más las reglas propias de esta materia (**R15**, figura por definición).
>
> Encargo del dueño (13/11/2026): *"quiero que el formato que tienen sbd lo muevas a calculo de una
> variable, con los svg y las explicaciones y todo eso"*. Lo que sigue es ese formato.
>
> Además del formato, el contenido debe estar **bien explicado**: una nota que solo transcribe el PDF
> es tan útil como leer el PDF. Ver **R14**.

## Las 14 reglas de SBD (adoptadas) + R15

### R1 · Frontmatter
```
---
dg-publish: true
tags: [MATG1045, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta).

### R2 · Título H1 con emoji
`# 🤔 Concepto Intuitivo de Límite`. Emoji visible + texto.

### R3 · Secciones H2, cada una con emoji y separadas por `---`
El esqueleto mínimo de una nota de clase:
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
**8 secciones.** Las secciones temáticas de la materia (teoremas, técnicas, errores comunes,
fórmulas) van **entre `Definiciones Formales` y `Ejercicios Propuestos`**.

**Perfiles.** El validador resuelve el perfil solo, por la ruta de la nota:

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | notas dentro de `Unidad N - …/` (N ≥ 1), cualquier subnivel | las **8** de arriba |
| `indice` | raíz de la materia (`Cálculo de una Variable.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) y `Unidad 0 - …/` | ninguna obligatoria (**0**), pero todo H2 que exista lleva emoji |

> [!warning] ⚠️ C1 tiene unidades anidadas
> La carpeta de una nota puede ser `Unidad 4 - Derivadas/IV - Técnicas Avanzadas/` (tres niveles
> dentro de la materia). El perfil se decide **buscando un ancestro `Unidad N` con N ≥ 1**, no por
> el nombre de la carpeta inmediata: si no, la mitad de las notas se clasificaría como `indice` y no
> se les exigiría el esqueleto.

### R4 · TODO el contenido dentro de callouts
Cero líneas de prosa, tabla o lista fuera de callouts. Todo bloque textual, tabla, embed y fórmula
va dentro de un callout. (Los encabezados H2/H3 y los `---` sí van sueltos: son estructura.)

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Límite`. Tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
```
> [!note] 📋 Definición — Límite
>
> El cuerpo del callout…
```

### R7 · Separadores internos dentro de un callout
- Entre dos párrafos de prosa: una línea `>` vacía entre medio.
- Antes de un embed `> ![[…]]`: línea `>` vacía.
- Antes de una tabla `> |…`: línea `>` vacía.
- Los items del mismo punto/lista van pegados.

### R8 · Solución anidada y plegada en los ejercicios
```
> [!example] 📋 Planteamiento
>
> Enunciado…
>
> > [!success]- ✅ Solución
> >
> > Respuesta…
```
Prefijo `> >` en dos niveles, y el `success` **plegado** (`[!success]-`): el enunciado se ve, la
solución se abre cuando la quieres. Aplica a los ejemplos de la sección **Ejercicios Propuestos**.

### R9 · Ejemplos con etiqueta en negrita
Dentro del callout: `> **Ejemplos:**`, `> **Se lee así:**`, `> **Por qué importa:**`, `> **Ejemplo:**`.

### R10 · Metas de Aprendizaje con checkboxes
```
> [!note] 📋 Nivel Básico
>
> - [ ] Defino el límite sin mirar.
```
Un callout por nivel, contenido como checkboxes. La sección **Metas de Aprendizaje** tiene que
contener al menos un callout así.

### R11 · Flashcards SR dentro de la sección Repaso
```
#flashcards/cal1-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice el teorema de Lagrange?::Respuesta.
```
La línea `#flashcards/cal1-uN` queda **fuera** del callout (es la directive del plugin), pero todas
las líneas `- Q::A` van **dentro** del `> [!note] 🧠`. El identificador sigue `cal1-uN`, con N el
número de unidad.

### R12 · Rutas de assets correctas y existentes
Los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/` y las capturas en
`Unidad 0 - Guias y Ejercicios/Archivos/<Tema>/`. Desde una nota, el prefijo relativo tiene que
tener **tantos `../` como la profundidad de la nota dentro de la materia**:

| Nota | Prefijo |
|---|---|
| `Cálculo de una Variable/Índice de Contenido.md` (0 niveles) | `Unidad 0 - Guias y Ejercicios/…` |
| `Cálculo de una Variable/Unidad 2 - Límites/01 - …md` (1 nivel) | `../Unidad 0 - Guias y Ejercicios/…` |
| `Cálculo de una Variable/Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - …md` (2 niveles) | `../../Unidad 0 - Guias y Ejercicios/…` |

Además: **no se embeben PDF/PPTX/DOC/XLS de clase** (`R12-clase-embebida`). Un examen, un taller o
un deck se **capturan como PNG** y se citan por número de página. Y **todo SVG embebido lleva su
`.mmd` fuente al lado**.

### R13 · Tags al pie
`**Tags:** #MATG1045 #…` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe)
Un embed o un bloque de deck **sin lectura propia** es una transcripción. Cada pieza visual lleva,
en las líneas siguientes, una interpretación propia.

**Etiquetas fijas** (se aceptan en cualquiera de estos tres órdenes, pero las tres en la lectura):
`**Se lee así:**` · `**Por qué importa:**` · `**Ejemplo:**`

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | ¿Qué dice la imagen **en su propia forma**? (qué cajas hay, qué flechas, qué filas) | 2–4 frases |
| `**Por qué importa:**` | ¿Qué **consecuencia** tiene? ¿Qué error evita? | 1–3 frases |
| `**Ejemplo:**` | ¿Cómo se aplica a **un caso propio** de la ESPOL o de la carrera? | 1 frase con caso concreto |

La lectura se escribe **desde la fuente** (el `.mmd` del SVG o el texto extraído del PDF), nunca
transcribiendo la imagen a ojo.

### R15 · Cada definición lleva su figura (regla propia de esta materia)
> [!important] 🎯 La regla que diferencia esta materia
> Un callout de definición (`> [!note] 📋 Definición — …`) **contiene su propia figura**: un embed
> `.svg` o `.png` **dentro** del mismo callout, con su lectura R14.
>
> ```
> > [!note] 📋 Definición — Límite
> >
> > Texto de la definición.
> >
> > ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/…svg]]
> >
> > **Se lee así:** …
> >
> > **Por qué importa:** …
> >
> > **Ejemplo:** …
> ```
>
> **Por qué:** en SBD la nota de referencia tiene una figura por definición (el diagrama es lo que
> hace que la definición se entienda de un vistazo). En Cálculo 1, la figura de una definición es
> la que dibuja la curva, el intervalo o la geometría: sin ella, el lector tiene que imaginarse lo
> que la definición describe.

## Receta de producción

### Diagramas (SVG)
Todos los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/`, son **mermaid** y llevan su
fuente `.mmd` **al lado**. La nota se llama igual que el diagrama y se numera:
`01_-_Concepto_y_Definición_Formal_del_Límite_01.mmd` / `.svg`.

**Render:**
```
py -X utf8 "Universidad/Herramientas/SVG-Pipeline/mmdc_ligero.py" -i X.mmd -o X.svg -b white
$env:PUPPETEER_EXECUTABLE_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**Round-trip obligatorio:** re-render del `.mmd` y comparación contra el SVG original de **texto
visible + viewBox**. Texto igual pero viewBox distinto = la dirección o el orden de las aristas
está mal.

**Reglas de sintaxis mermaid (las que fallan sin avisar):**
- En `erDiagram`, las etiquetas de relación con `,` o `:` **no parsean** → van entre comillas.
- `<br/>` y emojis sí funcionan dentro de esas comillas.
- Un SVG **siempre** necesita su `.mmd`. Si falta, se reconstruye desde el SVG (`svg_a_mmd.py`) y se
  valida re-renderizando. **Nunca** se sobrescribe un `.mmd` que ya está en git.

### Capturas de PDF (PNG)
1. Se **captura la página** del PDF, no se embebe el PDF.
2. **DPI 140** (`Universidad/Herramientas/Mantenimiento/pdf_a_png.py`).
3. Carpeta por tema: `Archivos/Examenes/`, `Archivos/Figuras/`, …
4. Naming: `cal1-<examen>-p<NN>.png`.
5. En la nota se cita **con el número de página**: `EXA-2023-0S-1Par, p. 6`.
6. El contenido se extrae **por texto** del PDF (`pdf_a_markdown_lote.py`, PyMuPDF). **No se leen las
   imágenes a ojo**: la lectura escrita sale del texto extraído.

### Nota nueva: orden de trabajo
1. Esqueleto con los H2 del perfil y `---` entre ellos.
2. Callouts con definiciones y ejemplos (**R4**, **R5**, **R6**, **R9**).
3. Diagramas: escribir el `.mmd`, renderizar, embeber **dentro del callout de la definición** y
   **leerlo** (**R14**, **R15**).
4. Capturas: capturar la página correcta, embeber, y **leerla** (**R14**).
5. Ejercicios con solución plegada (**R8**).
6. Metas con checkboxes (**R10**) y flashcards dentro del callout 🧠 (**R11**).
7. `**Tags:**` al pie (**R13**).
8. Auditar y corregir hasta 0 hallazgos.

## Cómo se audita
```
py -X utf8 "Universidad/Herramientas/Mantenimiento/qa_formato_calculo1.py"
```
Severidades: **H** (error duro) y **W** (desviación de formato). `--estricto` también hace fallar
los W. `--solo <ruta>` audita una parte y `--calibrar` audita la nota de referencia.

> [!success] ✅ Reglas heredadas de SBD, verificadas
> `qa_formato_calculo1.py` **importa** `qa_formato_sbd.py`: no reimplementa R1..R14, las ejecuta.
> Si el contrato de SBD cambia, Cálculo 1 lo hereda sin tocar una línea.
