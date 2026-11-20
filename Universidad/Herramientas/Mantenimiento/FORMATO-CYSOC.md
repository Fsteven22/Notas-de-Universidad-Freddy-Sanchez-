---
dg-publish: false
---

# 💻 FORMATO-CYSOC — contrato de formato de las notas de Computación y Sociedad

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique. Sus hermanos son `FORMATO-SBD.md` y `FORMATO-DISENO.md`.
>
> Las **39 notas de clase** de la materia comparten una estructura mínima real, que el validador
> mide: todas llevan `## 🎯 Introducción`, y el resto de secciones aparecen de forma desigual
> (Metas 19, Ejercicios 19, Referencias 17+10+2, Conexiones 10+9, Resumen 8+7+2). Este contrato fija
> ese mínimo por escrito: cualquier sesión (humana o asistente) debe escribir notas de
> Computación y Sociedad que **pasen** `qa_formato_cysoc.py`.
>
> El esqueleto real es **propio de la materia** (mnemotecnias, Analogías → Analogía, tablas IEEE,
> línea de tiempo general, comparaciones, fórmulas). **No copies el de SBD ni el de Diseño** — copia
> el método, no el esqueleto.

## Los 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [CYSOC/CFSGNN, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta). **El código de cátedra de
la materia es el que fijes en el sitio/nota raíz; no hay uno estándar documentado todavía — pendiente
 de confirmar con la cátedra/dueño.**

### R2 · Título H1 con emoji
`# 💻 Orígenes e Instrumentos de Cálculo`. Emoji visible + texto.

### R3 · Secciones H2: `Introducción` obligatoria + emoji en todo H2
El mínimo real medido en las 39 notas de clase: **`## 🎯 Introducción` en el 100%**.
Todo H2, de cualquier sección, abre con emoji (regla del validador `R3-h2-emoji`).

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | `Unidad N - …/0X - …md` (y nietos de U3/I-II) | **`Introducción`** (obligatoria, W) + emoji en todo H2 |
| `material` | `Unidad 0 - Guias y Ejercicios/Material de clase/…` | ninguna (**0**), pero todo H2 que exista lleva emoji |
| `indice` | notas raíz (`Computación y Sociedad.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) | ninguna (**0**), pero todo H2 que exista lleva emoji |

> [!note] Cierre recomendado (desviación W, no error)
> Se recomienda —confirmado por cobertura real— cerrar con alguna sección de cierre: `## 🎯 Metas
> de Aprendizaje` (19 notas), `## 📝 Ejercicios Progresivos` (19), `## 📚 Referencias` (17), `## 🔗
> Conexiones` (10) o `## 📚 Referencias y Conexiones` (9). La ausencia es una **desviación W**, no un
> error duro: no hay una sola sección de cierre obligatoria en la materia. El validador reporta su
> ausencia como `R3-cierre-falta`.

### R4 · TODO el contenido dentro de callouts
Ningún bloque de prosa, tabla, lista, embed o fórmula vive fuera de un callout. Si un diagrama va
suelto, se envuelve en un callout con título.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Mnemónico del IEEE`: tipo + emoji + texto. Nunca un callout sin título.
Los tipos de callout son minúscula e idénticos a los de Obsidian (`note`, `tip`, `warning`, `info`,
`success`, `question`, `example`, `quote`, `important`, `summary`, `danger`, `todo`).

### R6 · Línea en blanco `>` después del encabezado del callout
El callout arranca con una línea `>` sola, salvo los callouts 📖 de deck/syllabus, que pueden arrancar con prosa directo.

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
Un callout por nivel, contenido como checkboxes `- [ ]`. (Solo dentro de la sección de Metas.)

### R11 · Flashcards SR dentro de la sección Repaso
La línea `#flashcards/cysoc-uN` queda fuera del callout (es una directiva del plugin), pero **todas**
las líneas `- Q::A` van dentro del `> [!note] 🧠…`.

### R12 · Rutas de assets correctas y existentes
- SVG de diagrama: `Unidad 0 - Guias y Ejercicios/Diagramas/` (**única fuente**, con su `.mmd` al lado — regla de los validadores SBD/Diseño/Calculo 1).
- `../Unidad 0 - Guias y Ejercicios/Diagramas/…` para notas a profundidad 1; `../../Unidad 0 - …` para notas a profundidad 2 (U3/I-II). **Un solo nivel de `../` por nivel de profundidad.**
- Las rutas se verifican **locales a la nota**, **locales a la materia**, o por **basename en cualquier parte de `Universidad/`** (el sitio resuelve wikilinks globalmente; antes de reportar rota se comprueba la ausencia en todo el vault — misma lección que el manual).
- Material de clase **no se embebe** (PDF/PPTX/DOC): se capturan sus páginas como PNG en `Archivos/<Tema>/` y se citan con su número de página (R15).

### R13 · Tags al pie
`**Tags:** #CYSOC #...` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe)
**La regla que separa "leer la nota" de "leer el deck".** Cada embed visual (.png de deck/syllabus o
.svg) lleva, en las líneas siguientes, una lectura propia con etiquetas fijas:

| Etiqueta | Qué responde | Mínmo |
|---|---|---|
| `**Se lee así:**` | Qué dice la imagen en su propia forma (cajas, flechas, filas, palabras) | 2-4 frases |
| `**Por qué importa:**` | Qué consecuencia tiene; qué error evita; por qué la cátedra la puso | 1-3 frases |
| `**Ejemplo:**` | Cómo se aplica a un caso propio de la ESPOL o de la carrera | 1 frase con caso concreto |

> [!warning] Etiquetas aceptadas (case-insensitive)
> `Se lee así` · `Por qué importa` · `Ejemplo(s)` · `Nota` · `Cómo se lee` · `Verificación` ·
> `Analogía` · `Resumen` · `Para qué sirve` · `Qué notas` · `Pista`

**Cómo se escribe una buena lectura** (rutina operativa): del PDF saco el texto con PyMuPDF
(`doc[i].get_text("text")`) y del SVG saco el texto visible parseando el XML
(`<foreignObject>` / `<text>`). Con eso se escribe una lectura fundamentada, no inventada.

### R15 · Las páginas capturadas se citan con su número
Toda captura PNG va en `Archivos/<Tema>/` con naming `cysoc-uX-YY-NN-slug.png` (o `cysoc-syllabus-pNN.png`
para el syllabus) y se cita en la nota con su número de página (`slides01, p. 8` / `Syllabus, p. 2`).

### R16 · Deck embebido = `.mmd` al lado para todo SVG
Cada SVG recién generado debe traer su fuente `.mmd` en la misma carpeta (reconstruida parseando el
XML del SVG; si no se puede reconstruir con fidelidad, se rehace el diagrama desde cero en mermaid y
se re-renderiza). **Round-trip obligatorio:** re-renderizar el `.mmd` con `mmdc_ligero.py` y comparar
contra el SVG original (texto visible + viewBox). Texto igual pero viewBox distinto = dirección u
orden de aristas mal detectado.

## Material que NO entra
`_texto/`, PDFs de clase (se capturan), `Contenido Extra/`, docs de `Herramientas/`.

## Receta de producción (las 16 reglas en orden)
1. Esqueleto con `## 🎯 Introducción` y `---` entre secciones.
2. Callouts con definiciones y ejemplos (R4, R5, R6, R9).
3. Diagramas: escribir el `.mmd`, renderizar, embeber, y **leerlo** (R14, R16).
4. Capturas: capturar la página correcta, embeber, y **leerla** (R14, R15).
5. Ejercicios con solución plegada (R8).
6. Metas con checkboxes (R10) y flashcards dentro del callout 🧠 (R11).
7. `**Tags:**` al pie (R13).
8. Auditar y corregir hasta 0 hallazgos (`qa_formato_cysoc.py`).

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_cysoc.py" --solo "2do Semestre/Computación y Sociedad"
```
Severidades: **H** (error duro, rompe lectura o el sitio) y **W** (desviación de formato).
`--estricto` también hace fallar los W. `--fix-rutas` repara automáticamente los embeds con profundidad
incorrecta cuando la profundidad correcta sí existe. `--calibrar` audita la nota candidata de
referencia (`Unidad 1 - Historia de la computación/01 - Orígenes e Instrumentos de Cálculo.md`).

## Nota de referencia (candidata, pendiente de aprobación del dueño)
`2do Semestre/Computación y Sociedad/Unidad 1 - Historia de la computación/01 - Orígenes e Instrumentos de Cálculo.md`
— 8 H2 con emoji, callouts `info`/`success`/`question`, mnemotecnias y analogías. Cuando el dueño la
confirme, `--calibrar` apuntará a ella y este contrato citará sus líneas.
