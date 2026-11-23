---
dg-publish: false
---

# 📐 FORMATO-FISICA — contrato de formato de las notas de Física Mecánica

> [!info] 📖 Fuente única de verdad
>
> Nota de referencia: `01 - Cinemática/Cinemática Traslacional.md` (la "01"), corregida por el dueño del vault.
> Cada regla cita los números de línea como ejemplo literal. Este archivo es el contrato: cualquier sesión
> (humana o asistente) debe escribir notas de Física que **pasen** `qa_formato_fisica.py`.
>
> Además del formato, el contenido debe estar **bien explicado y bien documentado para fácil lectura**: una
> nota que solo transcribe el PDF del deck es tan útil como leer el PDF. Ver **R14**.

## Las 14 reglas heredadas de SBD

### R1 · Frontmatter
```
---
dg-publish: true
tags: [FISG1001, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta). `tags:` exige **≥3 tags temáticos** (R19).

### R2 · Título H1 con emoji
`# 🚗 Cinemática Traslacional` (línea 5). Emoji visible + texto.

### R3 · Secciones H2, cada una con emoji y separadas por `---`
El esqueleto mínimo (8 secciones, en este orden):
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
Secciones temáticas extra van entre Definiciones y Ejercicios. Cada H2 va precedida de `---` (salvo la primera).

### Perfiles
| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | notas dentro de `0N - …/` (N ≥ 1) | las 8 canónicas |
| `indice` | notas raíz y `Unidad 0 - Guias y Ejercicios/` | ninguna obligatoria, pero todo H2 lleva emoji |

### R4 · TODO el contenido dentro de callouts
La nota de referencia tiene **0 líneas de prosa, tabla o lista fuera de callouts**. Todo bloque textual, tabla, embed y fórmula va dentro de un callout.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Dato` (tipo + emoji + texto). Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
La mayoría de los callouts lo hacen. La excepción son los callouts 📖 de deck de cátedra, que arrancan con prosa directo.

### R7 · Separadores internos dentro de un callout
- Entre dos párrafos de prosa: una línea `>` vacía entre medio.
- Antes de un embed `> ![[...]]`: línea `>` vacía.
- Antes de una tabla `> |...`: línea `>` vacía.
- Los ítems del mismo punto/lista van pegados.

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

### R9 · Ejemplos con etiqueta negrita
Dentro del callout, la cierre va con etiqueta en negrita: `> **Ejemplos:**`, `> **Se lee así:**`, `> **Por qué importa:**`.

### R10 · Metas de Aprendizaje con checkboxes
```
> [!note] 📋 Nivel Básico
>
> - [ ] Defino dato, información y modelo sin mirar.
```
Un callout por nivel, contenido como checkboxes.

### R11 · Flashcards SR dentro de la sección Repaso
```
#flashcards/fisica-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Pregunta?::Respuesta.
```
Con guion `- ` delante de cada flashcard. La directiva `#flashcards/fisica-uN` queda **fuera** del callout, pero todas las líneas `- Q::A` van dentro del `> [!note] 🧠`.

### R12 · Rutas de assets correctas y existentes
`../Unidad 0 - Guias y Ejercicios/Diagramas/...` con el prefijo `../` apropiado a la profundidad de la nota. **Un solo nivel** porque todas las notas de física viven a la misma profundidad. El archivo referenciado debe existir.

Además: **no se embeben PDF/PPTX/DOC/XLS de clase** (`R12-clase-embebida`). Se capturan como PNG y se citan por número de página.

### R13 · Tags al pie
`**Tags:** #FISG1001 #...` al final.

### R14 · Todo lo visual se explica (no se transcribe)
Cada pieza visual (PNG de deck, SVG de diagrama, callout 📖 de deck) lleva, en las líneas siguientes, una interpretación propia con etiqueta `**Se lee así:**`, `**Por qué importa:**`, `**Ejemplo(s):**` / `**Ejemplo:**`, `**Nota:**`, o prosa propia de ≥ 60 caracteres.

## Reglas propias de Física Mecánica

### R15 · Cada definición lleva su propia figura
Cada callout de `DEFINICIÓN` en la sección `Definiciones Formales` debe contener una imagen (embebido `![[...]]` a un `.png` o `.svg`).

### R16 · Flashcards de física
Directiva `#flashcards/fisica-uN` (N = número de unidad) con **mínimo 3 tarjetas** dentro del callout `> [!note] 🧠`.

### R17 · Metas de Aprendizaje con checkboxes
La sección `Metas de Aprendizaje` debe contener **≥3 checkboxes** `- [ ]` en total.

### R18 · Cada definición en su propio H3 + callout propio
Cada definición formal va en un encabezado `### 1️⃣`, `### 2️⃣`, etc., seguido de un callout `> [!note] 📋 Definición — …`.

### R19 · Frontmatter con ≥3 tags temáticos
`tags:` en el frontmatter con al menos 3 tags temáticos (ej. `FISG1001`, `unidad1`, `cinematica`, `movimiento`).

## Material que NO entra
`_texto/`, PDFs de clase (se capturan), `Contenido Extra/`, docs de `Herramientas/`.

## Cómo se audita
```
py -X utf8 "Universidad/Herramientas/Mantenimiento/qa_formato_fisica.py" --solo "1er Semestre/Física Mecánica"
```
Severidades: **H** (error duro) y **W** (desviación de formato). `--estricto` también hace fallar los W. `--fix-rutas` repara automáticamente los embeds con profundidad incorrecta.

> [!success] ✅ Estado actual
>
> Las notas de Física Mecánica pasan `qa_formato_fisica.py` con **0 hallazgos**, y todos los embeds visuales tienen lectura propia (R14 en 0 sin lectura).
