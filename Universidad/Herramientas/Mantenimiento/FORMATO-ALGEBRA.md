---
dg-publish: false
---

# 🧮 FORMATO-ALGEBRA — contrato de formato de las notas de Álgebra Lineal

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique. Sus hermanos son `FORMATO-SBD.md`, `FORMATO-DISENO.md`, `FORMATO-CYSOC.md`,
> `FORMATO-POO.md`, `FORMATO-FESD.md` y `FORMATO-MATDISC.md`.
>
> **Nota de referencia:** `2do Semestre/Algebra Lineal/Unidad 1 – Sistemas Lineales y Matrices/I –
> Sistemas de ecuaciones y representación/01 - Sistema de ecuaciones lineales en R2 y R3.md`
> (la "01" de la I, la más estructurada de la materia: 26 H2 con emoji, 57 callouts de 9 tipos,
> 3 embeds con lectura, tags al pie). Cada regla cita sus líneas como ejemplo literal. El
> validador apunta a ella con `--calibrar`.
>
> Las **51 notas** de la materia no comparten esqueleto fijo (son documentos largos y multi-tema,
> a diferencia de SBD). Este contrato fija lo que sí es común: frontmatter, emoji, callouts,
> embeds con lectura y tags al pie. **Copia el método, no el esqueleto de otras materias.**

## Las 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [MATG1049, algebra-lineal, unidadN, tema]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta). El código de cátedra
es **MATG1049** (sílabo oficial ESPOL, 5.8 ECTS). Las 4 notas raíz ya lo llevan; las 47 notas de
clase se taggearon en el primer pase (19/11/2026). La referencia lo cumple en sus líneas 1-4.

### R2 · Título H1 con emoji
`# 📐 Sistemas de Ecuaciones Lineales (S.E.L.)` — emoji visible + texto. La referencia lo cumple
en su línea 6. **Anomalía documentada de la materia:** 6 notas tienen **dos H1** (documentos
fusionados del dueño; p. ej. la referencia lleva un segundo H1 en su línea 614
`# 📐 Ecuaciones de Grado 1 en ℝ² y ℝ³`). Es material del dueño, no un defecto de formato: el
validador no lo reporta. Al escribir notas **nuevas** va un solo H1.

### R3 · Secciones H2 con emoji
Todo H2 abre con emoji. La referencia tiene 26/26 (líneas 8, 25, 120, 166, 301, 472, 510, 569,
592, 616, 651, 766, 888, 1014, 1068, 1180, 1356, 1523, 1534, 1576, 1668, 1740, 1761, 1772, 1806,
1851). No hay esqueleto obligatorio: cada nota elige sus secciones por tema.

### R4 · Contenido dentro de callouts
La referencia tiene **0 líneas de prosa, tabla, lista o fórmula fuera de callouts** (sus únicas
líneas "fuera" son el frontmatter, los dos `**Tags:**` al pie y el segundo H1, todas legítimas).
El resto de la materia es prosa densa fuera de callouts por diseño del dueño (~780 líneas en 51
notas): el validador lo reporta como **W informativo**, no como error. Lo que sí es **H** es un
embed suelto top-level (ver R12).

### R5 · Callout con título siempre
`> [!note] 📋 Estructura Matemática Un sistema de **m ecuaciones**…` (referencia L29). Tipo +
emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` tras el encabezado del callout
La referencia lo hace en sus 57 callouts (p. ej. L10-11, L29-30). Excepción admitida por la
materia: callouts de deck 📖 que arrancan con prosa directo (no hay en la referencia; el
validador los exime como en CYSOC).

### R7 · Separadores internos dentro de un callout
Línea `>` en blanco antes de un embed, tabla o párrafo nuevo dentro del callout. La referencia lo
cumple en sus embeds (L282-284: header L282, `>` L283, embed L284).

### R8 · `> >` solo dentro de callout anidado
El prefijo `> >` solo es legítimo como contenido de un callout anidado con su propio `[!tipo]`.
Un `> >` suelto se renderiza como texto indentado sin estilo: se baja un nivel conservando el
emoji. Reportado como **H** (igual que CYSOC/POO).

### R9 · Ejemplos con etiqueta en negrita
`> **Ejemplo:**`, `> **Se lee así:**`, `> **Por qué importa:**` dentro del callout. La referencia
usa `> **Analogías útiles:**`, `> **Importancia histórica:**` (L11-17) — mismo patrón.

### R10 · Metas de Aprendizaje con checkboxes
Solo si la nota tiene la sección: contenido como `- [ ]`. **No aplica** a Álgebra (0 notas con
esta sección; no se exige).

### R11 · Flashcards SR dentro de la sección Repaso
`#flashcards/algebra-lineal-uN` fuera del callout; las Q/A dentro del `> [!note] 🧠 …`. **No
aplica** a Álgebra (0 flashcards en la materia; no se exige).

### R12 · Rutas de assets correctas y existentes
- SVG de diagrama: `Unidad 0 - Guias y Ejercicios/Diagramas/` (única fuente). La referencia los
  embed así: `> ![[01_-_Sistema_de_ecuaciones_lineales_en_R2_y_R3_01.svg]]` (L284), con ruta
  relativa `../../Unidad 0 - …` según profundidad.
- **SVG ⇒ `.mmd` al lado:** cada SVG debe tener su fuente `.mmd` en `Diagramas/`. Estado actual
  (19/11/2026): **248 SVG sin `.mmd`** en la materia — es el déficit real, pendiente de generar
  con `svg_a_mmd.py` (misma herramienta que CYSOC). Mientras dure, se reporta como **W**
  (`R12-svg-sin-mmd`), no como H.
- **Exámenes** (`.pdf`/`.docx`) viven en `Unidad 0 - Guias y Ejercicios/Exámenes/` y se **enlazan
  con alias 📎**, nunca se embeben visualmente.
- Material ajeno (`_texto/`, `site/`, `Herramientas/`) no se referenncia (H).

### R13 · Tags al pie
`**Tags:** #…` al final de la nota, en la raíz, separado del último callout por línea en blanco +
`---`. La referencia lo cumple dos veces (L612 y L1891, por ser dos documentos fusionados; ver R2).
**4 notas** de la materia aún no lo llevan: `Recursos Visuales.md`, `02 - Teorema de Rouché-
Frobenius.md`, `04 – Suma de subespacios.md`, `04 – Matriz de cambio de base.md` (W: `R13-tags-final`).

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
`<text>`), no se inventa. Fase 2 (19/11/2026): 246 lecturas insertadas; quedan 1 por pulir.

### R15 · Páginas capturadas citadas con su número
Las capturas PNG de decks/syllabus van en `Archivos/<Tema>/` con naming `algebra-uX-YY-NN-slug.png`
y se citan con su página (`syllabus, p. 2`). **No aplica hoy**: Álgebra no tiene PNG de deck
(0 en `Archivos/`, que está vacía salvo `.gitkeep`).

### R16 · Deck embebido = `.mmd` al lado para todo SVG
Cada SVG recién generado trae su `.mmd` en la misma carpeta; round-trip obligatorio. **Ver R12**:
el estado actual es 248 sin generar; la regla es de producción (para notas nuevas), no de
auditoría retroactiva.

## Material que NO entra
`_texto/`, PDFs de clase crudos (se capturan sus páginas), `Contenido Extra/`, docs de
`Herramientas/`.

## Exámenes (material real de práctica)
Los 42 exámenes de la cátedra (14 Parcial I · 14 Parcial II · 14 Mejoramiento, 2009–2026) viven en
`Unidad 0 - Guias y Ejercicios/Exámenes/`. Las secciones de ejercicios de cada tema son el lugar
natural para enlazarlos con 📎; al citar un examen conviene anotar su tema (Gauss → algoritmos,
autovalores → valores y vectores propios, etc.). **Nada se publica como ejercicios resueltos sin
fuente; se enlaza el PDF y se usa como autoridad.**

## Receta de producción (las 16 reglas en orden)
1. Frontmatter con `MATG1049` + slug (R1).
2. Un solo H1 con emoji (R2).
3. H2 con emoji, sin esqueleto fijo (R3).
4. Callouts con título, blanco `>` tras header, separadores internos (R5-R7).
5. Diagramas: escribir el `.mmd`, renderizar, embeber, y **leerlo** (R12, R14, R16).
6. Ejemplos con etiqueta en negrita (R9); ejercicios con solución plegada si los hay (R8).
7. `**Tags:**` al pie, separado (R13).
8. Auditar y corregir hasta 0 H (`qa_formato_algebra.py`).

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_algebra.py" --solo "2do Semestre/Algebra Lineal"
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_algebra.py" --calibrar
```
Severidades: **H** (bloquea: callout vacío, `> >` sin anclaje, embed roto/ajeno, ruta mal
profundizada) y **W** (desviación: prosa suelta, tags, emoji, `.mmd` faltante, lectura).
`--fix-rutas` repara embeds con profundidad incorrecta cuando la correcta existe.
Estado al cierre de esta edición (21/11/2026): **51 notas, 781 hallazgos, 0 H**. Los 781 son
únicamente `R4-prosa-top`, **W informativo por diseño**: el estilo de la materia es prosa densa
fuera de callouts y el contrato lo acepta. La nota de referencia da **0 hallazgos**.

## Nota de proceso (19/11/2026)
El contrato se reescribió sobre la nota de referencia real después de que el dueño lo pidiera
("usar la nota de refereencia de SBD como todos los contratos y recorrerlo"). La primera versión
(clon de CYSOC) tenía tres huecos: sin nota de referencia, `--calibrar` roto, y reglas heredadas
(R10/R11/R15) sin medir en la materia. Este documento los cierra.

## Nota de proceso (21/11/2026) — el validador aprendió de los datos
Al recorrer las 1367 desviaciones que quedaban se vio que **tres reglas heredadas producían
falsos positivos** con el material real de esta materia. Se corrigieron en el validador, no en
las notas (mismo criterio que ya se aplicó con keycaps y ©️/™️):

| Regla | Antes | Ahora | Por qué |
|---|---|---|---|
| `R14-deck-sin-explicacion` | 7 | **0** | Marcaba *todo* callout 📖 sin etiqueta de lectura. En Álgebra la mayoría son prosa pura (definiciones, taxonomías, bibliografía) y **no embeben nada**. Ahora solo dispara si el callout trae un `![[…]]` con `.png`/`.svg` dentro. Mismo criterio que **R14.4 de Física**. |
| `R7-separador-antes` | 220 | **0** | El clasificador trataba como tabla cualquier línea que abriera con `\|`, así que el **arte ASCII** (rectas, planos, matrices dibujadas) y los **bloques ```** generaban cientos de avisos. Ahora exige una **separadora markdown real** (`\| --- \| ---: \|`) en la línea siguiente, y no interpreta el interior de un fence. |
| `R6-sin-blanco-header` | 99 | **0** | Era un hallazgo **real**: 99 callouts con contenido pegado al header. Corregido insertando la línea `>` en blanco (23 en las 4 notas raíz + 76 en 11 notas de clase). |
| `R12-svg-sin-mmd` | 248 | **0** | No era un déficit: los 247 SVG de `Unidad 0/Diagramas/` **ya tenían** su `.mmd` (los generó otra sesión en `c4088779`). Verificado par a par que el `.mmd` corresponde al contenido del SVG. |

Los 19 hallazgos quirúrgicos (6 H2 sin emoji, 4 notas sin `**Tags:**`, 2 PDF embebidos en vez de
enlazados, 7 falsos R14) se cerraron a mano. Verificación posterior: 51 notas, **0 problemas
estructurales** (fences balanceados, tags al pie, H2 con emoji).
