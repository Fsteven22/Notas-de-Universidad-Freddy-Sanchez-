---
dg-publish: false
---

# 🗣️ FORMATO-COMUNICACION — contrato de formato de las notas de Comunicación

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique. Sus hermanos son `FORMATO-ALGEBRA.md`, `FORMATO-SBD.md`,
> `FORMATO-DISENO.md`, `FORMATO-CYSOC.md`, `FORMATO-POO.md`, `FORMATO-FESD.md` y
> `FORMATO-MATDISC.md`.
>
> **Nota de referencia:** `2do Semestre/Comunicación/Unidad 1 - Comunicación efectiva/01 - Escucha
> activa, empatía y barreras.md` (la "01" de la U1, la más completa de la materia: 20 H2 con
> emoji, 35 callouts de 8 tipos, 8 embeds con lectura, flashcards y metas). Cada regla cita sus
> líneas como ejemplo literal. El validador apunta a ella con `--calibrar` y da **0 hallazgos**.
>
> Las **18 notas** de la materia comparten este núcleo: H1 con emoji, `## 🎯 Introducción`, todo
> H2 con emoji, contenido dentro de callouts, embeds con lectura y `**Tags:**` al pie. **Copia el
> método, no el esqueleto de otras materias.**

## Las 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [IDIG2012, unidadN, tema, slug]
---
```
Sin `dg-publish: true` la nota no se publica. El código de cátedra es **IDIG2012** (sílabo oficial
ESPOL). La referencia lo cumple en sus líneas 1-4.

### R2 · Título H1 con emoji
`# 👂 Escucha Activa, Empatía y Barreras` (referencia L6). Emoji visible + texto. Un solo H1 por
nota.

### R3 · Secciones H2 con emoji
Todo H2 abre con emoji. La referencia tiene **20/20** (L8, L34, L67, L91, L115, L152, L169, L220,
L252, L294, L314, L333, L369, L394, L409, L462, L485, L500, L520, L532). No hay esqueleto
obligatorio: cada nota elige sus secciones por tema, pero siempre abre con `## 🎯 Introducción`.

### R4 · Contenido dentro de callouts
La referencia tiene **3 líneas fuera de callouts** y las tres son legítimas: dos embeds de
diagrama (L30 y L396, envueltos en su propio callout) y la línea `#flashcards/…` (L464), que
**debe** quedar en la raíz para que el plugin la lea. El resto de la materia es prosa dentro de
callouts: el validador reporta como **W informativo** la prosa suelta, no como error.

### R5 · Callout con título siempre
`> [!info] 💡 ¿Por Qué Escuchar Activamente?` (referencia L10). Tipo + emoji + texto. Nunca un
callout sin título.

### R6 · Línea en blanco `>` tras el encabezado del callout
La referencia lo hace en sus 35 callouts: L10-11, L30-31, L42-43, L64-65, L79-80, L103-104…
Excepción admitida: los callouts `📖` de fuentes/bibliografía pueden arrancar con prosa directo.

### R7 · Separadores internos dentro de un callout
Línea `>` en blanco antes de un embed, tabla o párrafo nuevo. La referencia lo cumple en sus
embeds (L41-43: texto L41, `>` L42, embed L43) y en sus tablas (L45-47).

### R8 · `> >` solo dentro de callout anidado
El prefijo `> >` solo es legítimo como contenido de un callout anidado con su propio `[!tipo]`.
La referencia lo usa correctamente en L93 (`> > [!quote] 📖 Efectiva vs asertiva`), L158
(`> > [!warning] ⚠️ Auto-test`) y L489 (`> > [!success]- ✅ Solución guiada`). Un `> >` suelto se
reporta como **H**.

### R9 · Ejemplos con etiqueta en negrita
`> **Ejemplo:**`, `> **Se lee así:**`, `> **Por qué importa:**` dentro del callout. La referencia
usa `> **Analogía del mundo real:**` (L14), `> **Actividad sugerida:**` (L305) y
`> **Implicación práctica:**` (L251) — mismo patrón.

### R10 · Metas de Aprendizaje con checkboxes
La referencia tiene la sección `## ✅ Metas de Aprendizaje` (L485) con tres niveles y checkboxes
`- [ ]`. Cuando la nota la tenga, el formato es obligatorio.

### R11 · Flashcards SR dentro de la sección Repaso
`#flashcards/comunicacion-uN` **en la raíz** (referencia L464), fuera de todo callout, y las Q/A
dentro del `> [!note] 🧠 …` con formato `- pregunta::respuesta` (L468-478). El plugin Spaced
Repetition necesita la etiqueta en la raíz para indexar la nota.

### R12 · Rutas de assets correctas y existentes
- SVG de diagrama: `Unidad 0 - Guias y Ejercicios/Diagramas/` (única fuente), con ruta relativa
  según profundidad: `../Unidad 0 - …` para las notas de unidad (referencia L42).
- **SVG ⇒ `.mmd` al lado:** cada SVG debe tener su fuente `.mmd` en `Diagramas/`. Estado actual:
  **0 SVG sin `.mmd`** en la materia.
- **Exámenes** (`.pdf`/`.docx`) viven en `Unidad 0 - Guias y Ejercicios/Exámenes/` y se **enlazan
  con alias 📎**, nunca se embeben.
- Material ajeno (`_texto/`, `site/`, `Herramientas/`) no se referencia (**H**).

### R13 · Tags al pie
`**Tags:** #…` al final de la nota, separado del último callout por línea en blanco + `---`.
La referencia lo cumple en L557:
`**Tags:** #IDIG2012 #unidad1 #escucha-activa #empatia #comunicacion #neuronas-espejo`.
**1 nota** aún no lo lleva: `Recursos Visuales.md` (W: `R13-tags-final`).

### R14 · Todo lo visual se explica (no se transcribe)
Cada embed (.svg/.png) lleva en las líneas siguientes su lectura:

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | Qué dice la imagen en su propia forma | 2-4 frases |
| `**Por qué importa:**` | Qué consecuencia tiene / qué error evita | 1-3 frases |
| `**Ejemplo:**` | Aplicación a un caso propio | 1 frase |

Etiquetas aceptadas (case-insensitive): `Se lee así` · `Por qué importa` · `Ejemplo(s)` · `Nota` ·
`Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Para qué sirve` · `Qué notas` · `Pista`.
La lectura se **fundamenta en el texto visible del propio SVG** (parseando `<foreignObject>`/
`<text>`), no se inventa. La referencia cumple en sus 8 embeds.

### R15 · Páginas capturadas citadas con su número
Las capturas PNG de decks/syllabus van en `Unidad 0 - Guias y Ejercicios/Figuras/` y se citan con
su página. **No aplica hoy**: la materia no tiene PNG de deck.

### R16 · Deck embebido = `.mmd` al lado para todo SVG
Cada SVG recién generado trae su `.mmd` en la misma carpeta; round-trip obligatorio. **Ver R12**:
el estado actual es 0 SVG sin fuente, así que la regla se cumple.

## Material que NO entra
`_texto/`, PDFs de clase crudos (se capturan sus páginas), `Contenido Extra/`, docs de
`Herramientas/`.

## Exámenes (material real de práctica)
Los **19 exámenes** de la cátedra (2017-1S, 2017-2S y 2018-1S; 1Par/2Par/Mejora) viven en
`Unidad 0 - Guias y Ejercicios/Exámenes/`. Se enlazan con `📎` desde las secciones de ejercicios de
cada tema, anotando el tema. **Nada se publica como ejercicios resueltos sin fuente.**

## Receta de producción (las 16 reglas en orden)
1. Frontmatter con `IDIG2012` + slug (R1).
2. Un solo H1 con emoji (R2).
3. `## 🎯 Introducción` y H2 con emoji (R3).
4. Callouts con título, blanco `>` tras header, separadores internos (R5-R7).
5. Diagramas: escribir el `.mmd`, renderizar, embeber, y **leerlo** (R12, R14, R16).
6. Ejemplos con etiqueta en negrita (R9); soluciones plegadas con `> > [!success]-` (R8).
7. Ejercicios, flashcards SR y metas (R10, R11).
8. `**Tags:**` al pie, separado (R13).
9. Auditar y corregir hasta 0 H (`qa_formato_comunicacion.py`).

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_comunicacion.py" --solo "2do Semestre/Comunicación"
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_comunicacion.py" --calibrar
```
Severidades: **H** (bloquea: callout vacío, `> >` sin anclaje, embed roto/ajeno) y **W**
(desviación: prosa suelta, tags, emoji, `.mmd` faltante, lectura).
`--fix-rutas` repara embeds con profundidad incorrecta cuando la correcta existe.
Estado al cierre de esta edición: **18 notas, 153 hallazgos, 0 H** (37 `R4-embed-top`,
30 `R14-embed-sin-explicacion`, 29 `R6-sin-blanco-header`, 27 `R4-prosa-top`, 8 `R12-clase-embebida`,
8 `R3-h2-emoji`, 5 `R4-lista-top`, 5 `R7-separador-antes`, 3 `R11-flashcards-guion`,
1 `R13-tags-final`). La nota de referencia da **0 hallazgos**.

## Nota de proceso (23/11/2026)
El contrato se creó a partir del motor de Álgebra (mismas reglas R1-R16, ya calibradas contra el
material real), adaptando la raíz por defecto, el `--calibrar` y el docstring. Antes de escribir
una sola línea del contrato se midió la materia (167 → 158 hallazgos tras cerrar 4 H reales: 3
callouts vacíos y 1 `> >` suelto) y se eligió la nota de referencia **midiendo las 18 notas**, no
por intuición: la "01" de U1 ganó por tener 8 embeds, 20 H2 con emoji, flashcards y metas.