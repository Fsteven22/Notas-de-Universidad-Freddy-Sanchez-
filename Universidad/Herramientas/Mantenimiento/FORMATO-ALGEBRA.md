---
dg-publish: false
---

# 🧮 FORMATO-ALGEBRA — contrato de formato de las notas de Álgebra Lineal

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique. Sus hermanos son `FORMATO-CYSOC.md`, `FORMATO-DISENO.md`, `FORMATO-SBD.md`,
> `FORMATO-POO.md` y `FORMATO-MATDISC.md`.
>
> Las **51 notas** de la materia (común a ESPOL) no comparten esqueleto fijo: son documentos de
> clase densos, por tema, con muchos H2 (definiciones, teoremas, ejemplos, aplicaciones). A
> diferencia de CYSOC, **no se exige un `Introducción` obligatorio**: se exige portada con H1 y
> todos los H2 con emoji. Este contrato documenta lo que la materia ya hace y bloquea lo que la
> rompe. **Copia el método, no el esqueleto de otras materias.**
>
> El validador que lo aplica es `qa_formato_algebra.py` (mismas severidades y flags que
> `qa_formato_cysoc.py`). Baseline a la fecha del contrato: **51 notas · 1345 hallazgos · 0 H**
> tras la primera pasada (tags, emoji, embeds sueltos y errores de render reales).

## Los 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [MATG1049, algebra-lineal, unidadN, tema]
---
```
El código de cátedra es **MATG1049** (sílabo oficial ESPOL, 5.8 ECTS). Las 4 notas raíz llevan
`unidad0`; las de unidad 1/2 llevan `unidad1`/`unidad2` + slug. Sin `dg-publish: true` la nota no se
publica.

### R2 · Título H1 con emoji
`# 📐 Sistemas de Ecuaciones Lineales (S.E.L.)`. Emoji visible + texto.

### R3 · Secciones H2: emoji en todo H2
Las notas son multi-tema (p. ej. Sistema Binario tiene 15+ H2). **No** se exige ninguna sección
concreta (no hay "Introducción obligatoria": la portada ya ubica al lector). El validador solo exige:
todo H2 abre con emoji.

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | `Unidad N - …/** 0N - ….md` | ninguna (**0**); emoji en todo H2 |
| `material` | `Unidad 0 - Guias y Ejercicios/Material de clase/…` | ninguna (**0**), pero todo H2 lleva emoji |
| `indice` | notas raíz (`Álgebra Lineal.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) | ninguna (**0**), pero todo H2 lleva emoji |

> [!note] Cierre recomendado (desviación W, no error)
> Se recomienda un cierre — `## 📚 Referencias`, `## 🎯 Metas de Aprendizaje`, `## 🔗 Conexiones`,
> `## 📝 Ejercicios`, etc. — pero su ausencia es **W**, no error. Ver `R3-cierre-falta` en el
> validador.

### R4 · Contenido suelto vs embeds
La prosa de estas notas vive mayoritariamente **fuera** de callouts por diseño (estilo-materia, no
un defecto). El validador la reporta como **R4-\*** en severidad informativa (W, no H). Lo que sí
rompe la lectura es un **embed suelto**: todo `![[...]]` va dentro de un callout o, si está
top-level, se envuelve en uno con su lectura (ver R14).

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Dimensión`: tipo + emoji + texto.

### R6 · Línea en blanco `>` tras el encabezado del callout
Entre `> [!tipo] emoji …` y el contenido, una línea con solo `>`. Excepción: callouts 📖 de deck
pueden ir pegados al encabezado si su primer párrafo sigue en la misma línea lógica del encabezado.

### R7 · Separador `>` en blanco ante embeds/tablas/párrafos
Antes de un `![[...]]`, una tabla o un párrafo dentro de un callout, va una línea `>` en blanco.

### R8 · `> >` solo dentro de callout anidado
`> >` sólo es legítimo como contenido de un callout anidado que abre con su propio `[!tipo]`.
Un `> >` suelto es texto indentado sin estilo: se baja un nivel (`> `). El dato extra va en el
callout padre con su emoji (`> 💡 …`, `> 📌 …`, `> ⚠️ …`), o en un callout anidado con título.
El validador lo reporta como `R8-doble-gt-sin-callout` (H).

### R9 · Ejemplos con etiqueta en negrita
Dentro del callout: `> **Ejemplo:**`, `> **Se lee así:**`, `> **Por qué importa:**`.

### R10 · Metas de Aprendizaje con checkboxes
`- [ ]` en la sección de metas, si la nota la tiene.

### R11 · Flashcards SR dentro de la sección Repaso
`#flashcards/algebra-lineal-uN` fuera del callout; las Q/A dentro del `> [!note] 🧠 …`.

### R12 · Rutas de assets correctas y existentes
- SVG de diagrama: `Unidad 0 - Guias y Ejercicios/Diagramas/` (única fuente, con su `.mmd` al lado).
- Profundidad correcta de `../` según la profundidad real de la nota.
- Exámenes (`.pdf`/`.docx`) viven en `Unidad 0 - Guias y Ejercicios/Exámenes/`; se enlazan con
  wikilink + alias 📎 (p. ej. `[[123456789-…__EXA-2024-1S-…-2Par.pdf|📎 Examen 2024-1S …]]`),
  nunca embebidos visualmente.

### R13 · Tags al pie
`**Tags:** #MATG1049 …` en la raíz al final de la nota, separado del último callout por línea en
blanco + `---`. El validador reporta `R13-tags-final` (falta) y `R13-tags-pegado` (pegado).

### R14 · Todo lo visual se explica (no se transcribe)
Cada embed (.svg de diagrama o .png) lleva en las líneas siguientes su lectura:

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | Qué dice la imagen en su propia forma | 2-4 frases |
| `**Por qué importa:**` | Qué consecuencia tiene / qué error evita | 1-3 frases |
| `**Ejemplo:**` | Aplicación a un caso propio | 1 frase |

Etiquetas aceptadas (case-insensitive): `Se lee así` · `Por qué importa` · `Ejemplo(s)` · `Nota` ·
`Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Para qué sirve` · `Qué notas` · `Pista`.
La lectura se **fundamenta en el texto visible del propio SVG** (parseando `<foreignObject>`/`<text>`),
no se inventa.

### R15 · Páginas capturadas citadas con su número
Las capturas de decks/syllabus van en `Archivos/<Tema>/` con naming `algebra-uX-YY-NN-slug.png` y se
citan con su página (`syllabus, p. 2`).

### R16 · SVG ⇒ `.mmd` al lado
Cada SVG nuevo trae su fuente `.mmd` en la misma carpeta; round-trip obligatorio (`.mmd` → PNG →
comparar con el SVG original).

## Material que NO entra
`_texto/`, PDFs de clase crudos (se capturan sus páginas), `Contenido Extra/`, docs de `Herramientas/`.

## Exámenes (material real de práctica)
Los 42 exámenes de la cátedra (14 Parcial I · 14 Parcial II · 14 Mejoramiento, 2009–2026) viven en
`Unidad 0 - Guias y Ejercicios/Exámenes/`. Las secciones de ejercicios de cada tema son el lugar
natural para enlazarlos con 📎; al citar un examen conviene anotar su tema (Gauss → algoritmos,
autovalores → valores y vectores propios, etc.). **Nada de esto se publica como ejercicios resueltos
sin fuente; se enlaza el PDF y se usa como autoridad.**

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_algebra.py" --solo "2do Semestre/Algebra Lineal"
```
Severidades: **H** (bloquea) y **W** (desviación de formato, no bloquea salvo `--estricto`).
`--fix-rutas` repara embeds con la profundidad incorrecta cuando la correcta existe.
Estado al cierre de esta edición: **0 H**.
