---
dg-publish: false
---

# 📐 FORMATO-MATDISC — contrato de formato de las notas de Matemáticas Discretas

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique. Sus hermanos son `FORMATO-SBD.md` y `FORMATO-DISENO.md`, en la misma
> carpeta.
>
> Las **34 notas de clase** de la materia ya comparten cuatro secciones núcleo y un estilo de
> prosa propio (callouts, emojis, tabla resumen, metas por nivel). Este contrato lo fija por
> escrito: cualquier sesión (humana o asistente) debe escribir notas de Matemáticas Discretas que
> **pasen** `qa_formato_matdisc.py`.
>
> La diferencia con los otros contratos: aquí **no hay decks de clase**. El material son guías de
> problemas, lecciones, talleres y exámenes (43 PDF). Por eso **R15 no aplica** y las capturas son
> figuras propias, no láminas.

## Las 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [MATG1051, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta). El código de la
cátedra es **MATG1051** (en SBD es TICG1018, en Diseño CCPG1042). Los `tags:` del frontmatter son
los mismos hashtags que van al pie de la nota (R13), en forma de lista.

### R2 · Título H1 con emoji
`# 🧮 Divisibilidad y Números Primos`. Emoji visible + texto.

### R3 · Secciones H2 con emoji, separadas por `---`
Cada nota de clase arranca con `## 🎯 Introducción` y cierra con sus secciones de cierre. Las
**cuatro secciones núcleo** que comparten las 34 notas de clase son:

```
## 🎯 Introducción
## <secciones temáticas del tema>
## 📊 Resumen Visual
## 📚 Referencias
## ✅ Metas de Aprendizaje
```

> [!info] 📖 Qué cuenta como emoji
> El validador acepta los bloques de emoji de Unicode: *Miscellaneous Symbols* (2600-27BF),
> *Dingbats* (2B00-2BFF), *Supplemental Symbols* (1F000-1FAFF), flechas (2190-21FF) y
> **Técnico (2300-23FF)** — este último cubre los emoji de reloj y cronómetro
> (⏱️ U+23F1, ⌛ U+231B, ⏳ U+23F3), que antes se rechazaban por un hueco en el rango.
> La misma regla se aplica en `qa_formato_diseno.py` y `qa_formato_sbd.py`.

Las secciones temáticas son variables (cada unidad tiene las suyas). Las secciones opcionales que
ya usa parte de la materia y que **deben** llevar emoji si existen: `🔁 Repaso SR (flashcards)`,
`🔗 Seguir estudiando`, `⚠️ Errores Comunes y Principios`, `📝 Ejercicios Propuestos`.

**Separador:** cada H2 va precedido de una línea `---` (salvo el primero de la nota).

**Perfiles.** El validador distingue las notas por su ruta:

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | `Unidad N - …/0X - …md` | las **4** núcleo |
| `guia` | `Unidad N - …/Guía de Problemas N - Ejercicios Resueltos.md` | ninguna (**0**), pero todo H2 que exista lleva emoji |
| `indice` | notas raíz (`Matemáticas Discretas.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) | ninguna (**0**), pero todo H2 que exista lleva emoji |

> [!tip] 💡 Por qué solo cuatro secciones y no doce
> La materia **no** tiene un esqueleto único: las unidades 1 y 2 (lógica) son más extensas
> (Repaso SR, Seguir estudiando, Errores Comunes) y las unidades 3–6 son más compactas. El
> contrato fija el mínimo común —Introducción, Resumen Visual, Referencias, Metas— y deja las
> secciones extra a criterio del tema. Copiar el esqueleto de otra materia sería inventar
> secciones que nadie pidió.

### R4 · TODO el contenido dentro de callouts
Ningún bloque de prosa, tabla, lista, embed o fórmula vive fuera de un callout. Si un diagrama
va suelto, se envuelve en un callout con título.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Divisibilidad`: tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
El callout arranca con una línea `>` sola, salvo los callouts 📖 de bibliografía, que pueden
arrancar con prosa directo.

### R7 · Separadores internos dentro de un callout
- Antes de un embed `> ![[...]]`: línea `>` vacía.
- Antes de una tabla `> |...`: línea `>` vacía.
- Entre dos párrafos de prosa: una línea `>` vacía entre medio.
- Los items del mismo punto/lista van pegados.

### R8 · Callout anidado plegado en las guías de ejercicios
```
> [!example] 📋 Ejercicio 3
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
> - [ ] Distingo divisibilidad de divisibilidad exacta.
```
Un callout por nivel, contenido como checkboxes.

### R11 · Flashcards SR dentro de la sección Repaso
```
#flashcards/matdisc-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Pregunta?::Respuesta.
```
La línea `#flashcards/matdisc-uN` queda **fuera** del callout (es una directive del plugin), pero
**todas** las líneas `- Q::A` van dentro del `> [!note] 🧠`.

### R12 · Rutas de assets correctas y existentes
- Diagramas: `../Unidad 0 - Guias y Ejercicios/Diagramas/…` (o `../../…` si la nota vive un nivel
  más hondo, como las subcarpetas `I - …`, `II - …`).
- Figuras raster: `../Unidad 0 - Guias y Ejercicios/Figuras/…`.
- El archivo referenciado **debe existir**: un embed con nombre suelto (`![[Pasted image….png]]`)
  no resuelve aunque el archivo esté en otra carpeta.
- **Todo SVG embebido tiene su `.mmd` fuente al lado** (`R12-svg-sin-mmd`).
- **Todo SVG de diagrama vive en `Unidad 0 - Guias y Ejercicios/Diagramas/`** (`R12-diagrama-fuera`).
- **Un PDF solo se embebe en el índice de la materia y en las guías de problemas** (son el material
  que el estudiante abre). En una nota de clase el PDF se **cita**, no se embebe
  (`R12-clase-embebida`).

### R13 · Tags al pie
`**Tags:** #MATG1051 #unidad3 #...` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe)
> [!warning] 🚨 La regla que separa "leer la nota" de "leer la guía"
> Un embed sin lectura propia es una transcripción: es tan difícil de entender como el material
> original. Cada pieza visual lleva, **en las líneas siguientes**, una interpretación propia.

**Qué exige R14:**
1. **Cada PNG de figura** va seguido de una de estas etiquetas:
   `**Se lee así:**` · `**Por qué importa:**` · `**Ejemplos:**` / `**Ejemplo:**` · `**Nota:**`
   — o de prosa propia de **≥ 60 caracteres** que no sea la ruta del embed.
   La ruta del propio embed **no cuenta** como explicación.
2. **Cada SVG (mermaid)** va seguido de la misma lectura.
3. **Cada callout 📖** lleva **al menos una** de esas etiquetas en su interior.
   Excepción: los callouts 📖 de "Fuentes consultadas" son bibliografía y no necesitan lectura.

**Etiquetas aceptadas (case-insensitive):** `Se lee así` · `Por qué importa` · `Ejemplo(s)` ·
`Nota` · `Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Para qué sirve` ·
`Qué notas` · `Pista` · `Cómo se aplica` · `Truco`.

**Cómo se escribe una buena lectura** (3 párrafos, en este orden):

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | ¿Qué dice la imagen **en su propia forma**? (qué cajas hay, qué flechas, qué filas) | 2–4 frases |
| `**Por qué importa:**` | ¿Qué **consecuencia** tiene? ¿Qué error evita? | 1–3 frases |
| `**Ejemplo:**` | ¿Cómo se aplica a **un caso propio** del curso? | 1 frase con caso concreto |

### R15 · No aplica en esta materia
No hay decks de clase: el material son guías de problemas, lecciones, talleres y exámenes. No
hay láminas que capturar ni "deck + página" que citar. Si algún día la cátedra sube diapositivas,
esta regla se reactiva como en `FORMATO-DISENO.md`.

### R16 · Nada de material ajeno
`_texto/`, `Contenido Extra/`, docs de `Herramientas/` — no se referencian ni se embeben
(`R12-ajeno`).

## Material que NO entra
`_texto/` (extracciones de texto de los libros, solo local), `Contenido Extra/`,
docs de `Herramientas/`.

## Receta de producción

### Diagramas (SVG)
Todos los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/` y son **mermaid**, con su
fuente `.mmd` **al lado** (R12-svg-sin-mmd). En esta materia son **flowcharts** (nada de mindmap,
classDiagram ni sequenceDiagram).

**Naming:** `dis-uX-YY-NN-tipo.svg` / `dis-uX-YY-NN-tipo.mmd`
- `dis` Discretas · `uX` unidad · `YY` nota · `NN` correlativo del diagrama en esa nota.
- `tipo` ∈ {-graph (panorama/comparación), -flow (procedimiento con decisiones)}.

**Render:**
```
py -3.12 Herramientas/SVG-Pipeline/mmdc_ligero.py -i X.mmd -o X.svg -b white
$env:PUPPETEER_EXECUTABLE_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**Reglas de sintaxis mermaid (las que fallan sin avisar):**
- Un SVG **siempre** necesita su `.mmd`. Si falta, se reconstruye desde el SVG y se valida
  re-renderizando y comparando texto visible + viewBox. **Nunca** se sobrescribe un `.mmd` que ya
  está en git.
- La dirección del flowchart se deduce del **eje por el que todas las aristas avanzan** (abajo =
  TB, derecha = LR); sumar desplazamientos se anula con las aristas de retroceso.
- El rombo de mermaid no está centrado en el origen: se reconoce por la forma del polígono, no
  por su centro.

### Figuras raster (PNG)
1. Viven en `Unidad 0 - Guias y Ejercicios/Figuras/`.
2. Nombre **temático**: `venn-2-conjuntos.png`, `demo-grafo-euler.png` — nunca `Pasted image
   20260613145551.png`.
3. El contenido se extrae **por herramienta** (OCR del PNG o texto del PDF de origen), no a ojo.
4. En la nota se embeben y se **leen** (R14).

### Nota nueva: orden de trabajo
1. Esqueleto con los H2 del perfil y `---` entre ellos.
2. Callouts con definiciones y ejemplos (**R4**, **R5**, **R6**, **R9**).
3. Diagramas: escribir el `.mmd`, renderizar, embeber dentro de un callout, y **leerlo** (**R14**).
4. Metas con checkboxes (**R10**) y flashcards dentro del callout 🧠 (**R11**).
5. `**Tags:**` al pie (**R13**) y los mismos tags en el frontmatter (**R1**).
6. Auditar y corregir hasta 0 hallazgos.

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_matdisc.py" --solo "3er Semestre/Matemáticas Discretas"
```
Severidades: **H** (error duro, rompe lectura o el sitio) y **W** (desviación de formato).
`--estricto` también hace fallar los W. `--fix-rutas` repara automáticamente los embeds con
profundidad incorrecta cuando la profundidad correcta sí existe.

> [!success] ✅ Estado actual
> _Línea base de la auditoría de arranque (2026-11-10): **670 hallazgos** en las 44 notas_
> (150 SVG sin `.mmd`, 100 callouts sin línea en blanco, 90 embeds sin lectura, 69 embeds fuera de
> callout, 51 prosa fuera de callout, 40 frontmatters sin `tags:`, 32 embeds rotos, 32 H2 sin
> emoji, 25 callouts 📖 sin lectura, 18 secciones núcleo faltantes).
> Se cierra por bloques: assets → `.mmd` → formato mecánico → lecturas.

## Nota de ubicación
Este contrato **no** vive en `3er Semestre/Matemáticas Discretas/`: es una herramienta, y el sitio
publica la carpeta de la materia. Vive en `Universidad/Herramientas/Mantenimiento/`, junto al
validador que lo aplica (`qa_formato_matdisc.py`) y a sus hermanos (`FORMATO-SBD.md`,
`FORMATO-DISENO.md`).
