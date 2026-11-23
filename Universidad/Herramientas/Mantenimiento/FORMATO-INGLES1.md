---
dg-publish: false
---

# 📘 FORMATO-INGLES1 — contrato de formato de las notas de Inglés I (B1-B2)

> [!info] 📖 Fuente única de verdad
> Nota de referencia: `3er Semestre/Sistema de Bases de Datos/Unidad 1 - Modelos de Datos y ER/01 - Dato, información y modelos de datos.md`
> Esta nota es el patrón que todas las notas de Inglés I deben seguir. Cada regla cita sus líneas como ejemplo literal.
>
> Las notas de Inglés I no comparten un esqueleto rígido (cada unidad mezcla Vocabulary, Grammar, Functional Language y Reading/Writing/Speaking). Este contrato fija lo que sí es común: frontmatter, emoji, callouts, embeds con lectura, ejercicios con solución plegada y tags al pie. **Copia el método, no el esqueleto de otras materias.**

## Las reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [IDIG1006, unitN, tema]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta). El código de cátedra es **IDIG1006** (sílabo oficial ESPOL).

### R2 · Título H1 con emoji
`# 🎯 Vocabulary & Use: Materials + Production & Distribution` — emoji visible + texto.

### R3 · Secciones H2 con emoji
Todo H2 abre con emoji. No hay esqueleto fijo: cada nota elige sus secciones por tema (Vocabulary, Grammar, Functional Language, Reading/Writing/Speaking).

### R4 · TODO el contenido dentro de callouts
La nota de referencia tiene **0 líneas de prosa, tabla, lista o fórmula fuera de callouts** (las únicas líneas "fuera" son el frontmatter, el H1, los H2, los `---` y los `**Tags:**` al pie, todas legítimas). Un embed suelto top-level se reporta como **H** (`R4-embed-top`).

### R5 · Callout con título siempre
`> [!info] 💡 ¿Por qué es importante este vocabulario?` — tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
```
> [!info] 💡 Título
>
> El cuerpo del callout…
```

### R7 · Separadores internos dentro de un callout
Línea `>` en blanco antes de un embed, tabla o párrafo nuevo dentro del callout.

### R8 · `> >` solo como callout anidado con su propio `[!tipo]`
```
> [!tip] 💪 Exercises
>
> **Exercise 1: …**
>
> > [!success]- ✅ Answers — Exercise 1
> >
> > 1. **cotton**
```
Prefijo `> >` en dos niveles, y el `success` **plegado** (`[!success]-`). Un `> >` suelto (sin `[!tipo]` propio) se reporta como **H** (`R8-doble-gt-sin-callout`).

### R9 · Ejemplos con título en su propio callout
Cada ejemplo va en su propio callout con título, nunca como texto suelto:
```
> [!example] 💬 Ejemplo en contexto
>
> - This shirt is made of cotton.
> - The window is made of glass.
```

### R10 · Metas de Aprendizaje con checkboxes
Solo si la nota tiene la sección: contenido como `- [ ]`. **No aplica** a Inglés I (0 notas con esta sección; no se exige).

### R11 · Flashcards SR dentro de la sección Repaso
`#flashcards/ingles1-uN` fuera del callout; las Q/A dentro del `> [!note] 🧠 …`. **No aplica** a Inglés I (0 flashcards en la materia; no se exige).

### R12 · Rutas de assets correctas y existentes
- SVG de diagrama: `Unidad 0 - Guias y Ejercicios/Diagramas/` (única fuente). La referencia los embebe así: `> ![[Diagramas/01_-_Vocabulary_&_Use_-_Materials_+_Production_&_Distribution_01.svg]]` con ruta relativa `../Unidad 0 - …` según profundidad.
- **SVG ⇒ `.mmd` al lado:** cada SVG embebido debe tener su fuente `.mmd` en `Diagramas/`.
- **PDF/PPTX/DOC de clase** no se embeben: se enlazan con alias 📎.
- Material ajeno (`_texto/`, `site/`, `Herramientas/`) no se referencia (H).

### R13 · Tags al pie
`**Tags:** #english #vocabulary #materials …` al final de la nota, separado del último callout por línea en blanco + `---`.

### R14 · Todo lo visual se explica (no se transcribe)
Cada embed (.svg/.png) lleva en las líneas siguientes su lectura:

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**How to read it:**` / `**Se lee así:**` | Qué dice la imagen en su propia forma | 2-4 frases |
| `**Why it matters:**` / `**Por qué importa:**` | Qué consecuencia tiene / qué error evita | 1-3 frases |
| `**Example:**` / `**Ejemplo:**` | Aplicación a un caso propio | 1 frase |

La referencia lo cumple en sus **8 SVG** (cada uno con las tres etiquetas). La lectura se fundamenta en el contenido del propio diagrama, no se inventa.

### R15 · Diagramas de vocabulario (regla propia de esta materia)
Los diagramas que **agrupan** vocabulario (materiales, verbos, adjetivos, collocations) pueden ser **flowchart** o **mindmap** según el tipo de información:

| Tipo de diagrama | Cuándo usar | Formato Mermaid |
|---|---|---|
| Árbol de categorías (materiales, verbos, adjetivos) | `mindmap` | `mindmap` |
| Proceso paso a paso (producción, distribución) | `flowchart` | `flowchart` |
| Relación causa-efecto (grammar) | `flowchart` | `flowchart` |

No mezclar `flowchart` con `mindmap` en el mismo diagrama. Cada diagrama debe tener su `.mmd` al lado en `Unidad 0 - Guias y Ejercicios/Diagramas/`.

### R16 · Enlaces a exámenes con alias 📎
Los exámenes viven en `Unidad 0 - Guias y Ejercicios/Exámenes/` y se **enlazan con alias** `[[…|📎 Examen …]]`, nunca se embeben visualmente. **No aplica hoy** (Inglés I no tiene exámenes en `Exámenes/`; el pendiente de enlazar 4 exámenes es de Inglés III).

## Material que NO entra
`_texto/`, PDFs de clase crudos (se capturan sus páginas), `Contenido Extra/`, docs de `Herramientas/`, `site/`.

## Receta de producción (las reglas en orden)
1. Frontmatter con `IDIG1006` + tags (R1).
2. Un solo H1 con emoji (R2).
3. H2 con emoji, sin esqueleto fijo (R3).
4. Callouts con título, blanco `>` tras header, separadores internos (R5-R7).
5. Vocabulario en tablas dentro de callouts (R16).
6. Diagramas: embeber el SVG, y **leerlo** con las tres etiquetas (R12, R14).
7. Ejercicios con solución plegada (R8).
8. `**Tags:**` al pie, separado (R13).
9. Auditar y corregir hasta 0 H (`qa_formato_ingles1.py`).

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_ingles1.py"
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_ingles1.py" --solo "1er Semestre/Ingles I (B1-B2)/Unit 10 - Why we buy"
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_ingles1.py" --calibrar
```
Severidades: **H** (error duro) y **W** (desviación de formato). `--fix-rutas` repara embeds con profundidad incorrecta cuando la correcta existe.

> [!success] ✅ Reglas heredadas de SBD, verificadas
> `qa_formato_ingles1.py` **importa** `qa_formato_algebra.py` (que a su vez importa el núcleo de SBD): no reimplementa R1..R14, las ejecuta. Si el contrato base cambia, Inglés I lo hereda sin tocar una línea. La nota de referencia es la de SBD; la de Inglés I sirve para medir el contrato contra material real de esta materia.