---
dg-publish: false
---

# 📘 FORMATO-INGLES1 — contrato de formato de las notas de Inglés I (B1-B2)

> [!info] 📖 Fuente única de verdad
> Nota de referencia: `Universidad/1er Semestre/Ingles I (B1-B2)/Unit 10 - Why we buy/01 - Vocabulary & Use - Materials + Production & Distribution.md`
> Esta nota es el patrón que todas las notas de Inglés I deben seguir. Cualquier sesión (humana o asistente) debe escribir notas de Inglés I que **pasen** `qa_formato_ingles1.py`.
>
> Además del formato, el contenido debe estar **bien explicado y bien documentado para fácil lectura**: una nota que solo transcribe el libro de texto es tan útil como leer el libro. Ver **R14**.

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
`> [!info] 💡 ¿Por qué es importante este vocabulario?` (línea 10). Tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
```
> [!info] 💡 ¿Por qué es importante este vocabulario?
>
> El vocabulario de materiales, producción y distribución es fundamental para:
```
La referencia lo hace en todos sus callouts.

### R7 · Separadores internos dentro de un callout
Línea `>` en blanco antes de un embed, tabla o párrafo nuevo dentro del callout.

### R8 · `> >` solo como callout anidado con su propio `[!tipo]`
```
> [!tip] 💪 Exercises
>
> **Exercise 1: Complete with the correct material**
>
> > [!success]- ✅ Answers — Exercise 1
> >
> > 1. **cotton**
> > 2. **glass**
```
Prefijo `> >` en dos niveles, y el `success` **plegado** (`[!success]-`): el enunciado se ve, la solución se abre cuando la quieres. **Un `> >` suelto (sin `[!tipo]` propio) se renderiza como texto indentado sin estilo y se reporta como `R8-doble-gt-sin-callout`.**

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
- SVG de diagrama: `Unidad 0 - Guias y Ejercicios/Diagramas/` (única fuente). La referencia los embebe así: `> ![[Diagramas/01_-_Vocabulary_&_Use_-_Materials_+_Production_&_Distribution_01.svg]]` (línea 32), con ruta relativa `../Unidad 0 - …` según profundidad.
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

La referencia lo cumple en sus **8 SVG** (cada uno con las tres etiquetas). La lectura se fundamenta en el contenido del propio diagrama (parseando `<foreignObject>`/`<text>`), no se inventa.

### R15 · Diagramas de vocabulario en `mindmap` (regla propia de esta materia)
> [!important] 🎯 La regla que diferencia esta materia
> Los diagramas que **agrupan** vocabulario (materiales, verbos, adjetivos, collocations) van en **mermaid `mindmap`**, no en `flowchart`. Un `mindmap` tiene nodo raíz y ramas jerárquicas — es lo que espera un mapa de vocabulario.
>
> ```
> mindmap
> root((Materials))
>     Natural
>         Cotton
>         Leather
>     Synthetic
>         Plastic
> ```
>
> Los `flowchart` se reservan para **procesos** (production chain, distribution chain, passive voice transformation) donde el orden de los pasos importa.
>
> **Por qué:** un `flowchart` de vocabulario (cajas conectadas con flechas) sugiere secuencia — *primero esto, luego aquello* — cuando el vocabulario no tiene orden: es un conjunto jerárquico. El `mindmap` comunica "esto es un árbol de categorías", no "esto es un camino".

### R16 · Vocabulario en tablas dentro de callouts (regla propia de esta materia)
> [!important] 🎯 La regla que diferencia esta materia
> El vocabulario (materiales, verbos, adjetivos, collocations) va en **tablas markdown dentro de callouts** `[!example]` o `[!success]`, con columnas fijas: `English | Spanish | Pronunciation | Common products`.
>
> ```
> > [!example] 📦 Basic materials
> >
> > | Material | Spanish | Pronunciation | Common products |
> > |---|---|---|---|
> > | **Cotton** | Algodón | /ˈkɒt.ən/ ("cotón") | T-shirts, jeans |
> ```
>
> **Por qué:** en Inglés la tabla es el formato canónico de vocabulario (el del libro *Evolve*), y el callout la mantiene dentro de la estructura del sitio. Una lista suelta fuera de callout rompe R4.

### R17 · Pronunciación legible (regla propia de esta materia)
> [!important] 🎯 La regla que diferencia esta materia
> La pronunciación se escribe con símbolos fonéticos **reconocibles** y, cuando sea posible, con una aproximación fonética en español entre paréntesis. **Nunca símbolos fonéticos sueltos sin contexto.**
>
> ```
> /kɒt.ən/ → "cotón" (algodón)
> /ˈleð.ər/ → "ledor" (cuero)
> ```
>
> **Por qué:** un símbolo como `/wʊl/` sin más no se lee; el estudiante no sabe si es "ul", "ool" o "uol". La aproximación entre paréntesis hace que el símbolo sea accesible desde el primer día.

### R18 · Enlaces a exámenes con alias 📎
Los exámenes viven en `Unidad 0 - Guias y Ejercicios/Exámenes/` y se **enlazan con alias** `[[…|📎 Examen …]]`, nunca se embeben visualmente. **No aplica hoy** (Inglés I no tiene exámenes en `Exámenes/`; el pendiente de enlazar 4 exámenes es de Inglés III).

## Material que NO entra
`_texto/`, PDFs de clase crudos (se capturan sus páginas), `Contenido Extra/`, docs de `Herramientas/`, `site/`.

## Receta de producción (las reglas en orden)
1. Frontmatter con `IDIG1006` + tags (R1).
2. Un solo H1 con emoji (R2).
3. H2 con emoji, sin esqueleto fijo (R3).
4. Callouts con título, blanco `>` tras header, separadores internos (R5-R7).
5. Vocabulario en tablas dentro de callouts (R16).
6. Diagramas de vocabulario en `mindmap`, procesos en `flowchart` (R15).
7. Embeber el SVG, y **leerlo** con las tres etiquetas (R12, R14).
8. Ejercicios con solución plegada (R8).
9. `**Tags:**` al pie, separado (R13).
10. Auditar y corregir hasta 0 H (`qa_formato_ingles1.py`).

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_ingles1.py"
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_ingles1.py" --solo "1er Semestre/Ingles I (B1-B2)/Unit 10 - Why we buy/01 - Vocabulary & Use - Materials + Production & Distribution.md"
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_ingles1.py" --calibrar
```
Severidades: **H** (error duro) y **W** (desviación de formato). `--fix-rutas` repara embeds con profundidad incorrecta cuando la correcta existe.

> [!success] ✅ Reglas heredadas de SBD, verificadas
> `qa_formato_ingles1.py` **importa** `qa_formato_algebra.py` (que a su vez importa el núcleo de SBD): no reimplementa R1..R14, las ejecuta. Si el contrato base cambia, Inglés I lo hereda sin tocar una línea. La nota de referencia es la de SBD; la de Inglés I sirve para medir el contrato contra material real de esta materia.