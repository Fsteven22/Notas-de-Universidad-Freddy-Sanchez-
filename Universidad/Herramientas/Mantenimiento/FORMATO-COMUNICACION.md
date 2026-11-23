---
dg-publish: false
---

# 🗣️ FORMATO-COMUNICACION — contrato de formato de las notas de Comunicación

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique.
>
> **Nota de referencia:** `3er Semestre/Sistema de Bases de Datos/Unidad 1 - Modelos de Datos y ER/01 - Dato, información y modelos de datos.md`
> (la "01" de SBD, personalmente corregida por el dueño del vault: 0 hallazgos en `qa_formato_sbd.py`).
> Cada regla cita los números de línea de esa nota como ejemplo literal. Este archivo es el contrato:
> cualquier sesión (humana o asistente) debe escribir notas de Comunicación que **pasen**
> `qa_formato_comunicacion.py`.
>
> Además del formato, el contenido debe estar **bien explicado y bien documentado para fácil lectura**:
> una nota que solo transcribe el deck es tan útil como leer el deck. Ver **R14**.

## Las 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [IDIG2012, unidadN, tema, slug]
---
```
Sin `dg-publish: true` la nota no se publica. El código de cátedra es **IDIG2012** (sílabo oficial
ESPOL). La nota de referencia lo cumple en sus líneas 1-4 (`dg-publish: true`, `tags:` con
código de cátedra y unidad).

### R2 · Título H1 con emoji
`# 👂 Escucha Activa, Empatía y Barreras` (línea 6 de la referencia de SBD:
`# 💾 Dato, Información y Modelos de Datos`). Emoji visible + texto. Un solo H1 por nota.

### R3 · Secciones H2 con emoji
Todo H2 abre con emoji. La referencia de SBD tiene todos sus H2 con emoji (L8, L27, L29…).
No hay esqueleto obligatorio: cada nota elige sus secciones por tema, pero todas llevan emoji.

### R4 · Contenido dentro de callouts
La nota de referencia de SBD tiene **0 líneas de prosa, tabla o lista fuera de callouts** (la
única excepción es un diagrama suelto en L164, que la auditoría marca con W). Todo bloque
textual, tabla, embed y fórmula va dentro de un callout.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Dato` (L27 de la referencia): tipo + emoji + texto. Nunca un
callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
La referencia lo hace en sus callouts (L10-11, L28-30, L38-40…). La excepción son los
callouts 📖 de deck de cátedra, que arrancan con prosa directo.

### R7 · Separadores internos dentro de un callout
Línea `>` en blanco antes de un embed, tabla o párrafo nuevo dentro del callout. La referencia
lo cumple en sus embeds (L21-22: header L21, `>` L22, embed L23) y en sus tablas.

### R8 · `> >` solo dentro de callout anidado
El prefijo `> >` solo es legítimo como contenido de un callout anidado con su propio `[!tipo]`.
Un `> >` suelto se renderiza como texto indentado sin estilo. **H** si aparece suelto.

### R9 · Ejemplos con etiqueta en negrita
`> **Ejemplo:**`, `> **Se lee así:**`, `> **Por qué importa:**` dentro del callout. La
referencia de SBD usa `> **Ejemplos:**`, `> **Se lee así:**` (L21, L33) — mismo patrón.

### R10 · Metas de Aprendizaje con checkboxes
Solo si la nota tiene la sección: contenido como `- [ ]`. **No aplica** si la nota no tiene la
sección; no se exige.

### R11 · Flashcards SR dentro de la sección Repaso
`#flashcards/comunicacion-uN` fuera del callout; las Q/A dentro del `> [!note] 🧠 …`. Las
flashcards del plugin SR (`Q::A` + `<!--SR:...-->`) no se tocan cuando existen.

### R12 · Rutas de assets correctas y existentes
- SVG de diagrama: `Unidad 0 - Guias y Ejercicios/Diagramas/` (única fuente). La referencia los
  embed así: `> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-01-graph.svg]]` (L19 de la
  referencia), con ruta relativa `../` según profundidad.
- **SVG ⇒ `.mmd` al lado:** cada SVG debe tener su fuente `.mmd` en `Diagramas/`.
- **Exámenes** (`.pdf`/`.docx`) viven en `Unidad 0 - Guias y Ejercicios/Exámenes/` y se **enlazan
  con alias 📎**, nunca se embeben visualmente.
- Material ajeno (`_texto/`, `site/`, `Herramientas/`) no se referencia (**H**).

### R13 · Tags al pie
`**Tags:** #…` al final de la nota, separado del último callout por línea en blanco + `---`.
La referencia lo cumple en L373:
`**Tags:** #TICG1018 #unidad1 #datos #modelos #bd`.

### R14 · Todo lo visual se explica (no se transcribe)
Cada embed (.svg/.png) y cada callout 📖 de deck lleva en las líneas siguientes su lectura:

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | Qué dice la imagen en su propia forma | 2-4 frases |
| `**Por qué importa:**` | Qué consecuencia tiene / qué error evita | 1-3 frases |
| `**Ejemplo:**` | Aplicación a un caso propio | 1 frase |

Etiquetas aceptadas (case-insensitive): `Se lee así` · `Por qué importa` · `Ejemplo(s)` ·
`Nota` · `Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Para qué sirve` · `Qué notas` ·
`Pista`.

La lectura se **fundamenta en el texto visible del propio SVG** (parseando `<foreignObject>`/
`<text>`), no se inventa. La ruta del propio embed **no cuenta** como explicación.

**Ejemplo de lectura de un SVG de la referencia (L21-23):**
```
> **Se lee así:** el diagrama es una bifurcación, y la pregunta que decide es única: *¿el dato tiene contexto y estructura?*.
> **Por qué importa:** fíjate en que los dos lados terminan con **tres** resultados.
```

### R15 · Páginas capturadas citadas con su número
Las capturas PNG de decks/syllabus van en `Unidad 0 - Guias y Ejercicios/Figuras/` y se citan con
su página. **No aplica hoy**: la materia no tiene PNG de deck.

### R16 · Deck embebido = `.mmd` al lado para todo SVG
Cada SVG recién generado trae su `.mmd` en la misma carpeta; round-trip obligatorio. **Ver R12**:
el estado actual es 0 SVG sin fuente en la materia, pendiente de generar con `svg_a_mmd.py`.

## Material que NO entra
`_texto/`, PDFs de clase crudos (se capturan sus páginas), `Contenido Extra/`, docs de
`Herramientas/`.

## Exámenes (material real de práctica)
Los exámenes de la cátedra viven en `Unidad 0 - Guias y Ejercicios/Exámenes/`. Se enlazan con
`📎` desde las secciones de ejercicios de cada tema, anotando el tema. **Nada se publica como
ejercicios resueltos sin fuente; se enlaza el PDF y se usa como autoridad.**

## Receta de producción (las 16 reglas en orden)
1. Frontmatter con `IDIG2012` + slug (R1).
2. Un solo H1 con emoji (R2).
3. `## 🎯 Introducción` y H2 con emoji (R3).
4. Callouts con título, blanco `>` tras header, separadores internos (R5-R7).
5. Diagramas: escribir el `.mmd`, renderizar, embeber, y **leerlo** (R12, R14, R16).
6. Ejemplos con etiqueta en negrita (R9); ejercicios con solución plegada si los hay (R8).
7. `**Tags:**` al pie, separado (R13).
8. Auditar y corregir hasta 0 H (`qa_formato_comunicacion.py`).

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_comunicacion.py" --solo "2do Semestre/Comunicación"
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_comunicacion.py" --calibrar
```
Severidades: **H** (bloquea: callout vacío, `> >` sin anclaje, embed roto/ajeno, ruta mal
profundizada) y **W** (desviación: prosa suelta, tags, emoji, `.mmd` faltante, lectura).
`--fix-rutas` repara embeds con profundidad incorrecta cuando la correcta existe.
`--calibrar` apunta a la nota de referencia de SBD para verificar que el validador funciona
contra una nota ya en 0 hallazgos.