---
dg-publish: false
---

# 📐 FORMATO-SBD — contrato de formato de las notas de Sistema de Bases de Datos

> [!info] 📖 Fuente única de verdad
> Nota de referencia: `Unidad 1 - Modelos de Datos y ER/01 - Dato, información y modelos de datos.md` (la "01"), personalmente corregida por el dueño del vault. Cada regla cita los números de línea como ejemplo literal. Este archivo es el contrato: cualquier sesión (humana o asistente) debe escribir notas SBD que **pasen** `qa_formato_sbd.py`.

## Las 13 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [TICG1018, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta).

### R2 · Título H1 con emoji
`# 💾 Dato, Información y Modelos de Datos` (línea 6). Emoji visible + texto.

### R3 · Secciones H2, cada una con emoji y separadas por `---`
El esqueleto mínimo (líneas 8, 23, 233, 280, 296, 305, 319, 328):
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
Secciones temáticas extra van entre Definiciones y Ejercicios (líneas 105, 151, 168, 187, 201).

### R4 · TODO el contenido dentro de callouts
La nota de referencia tiene **0 líneas de prosa, tabla o lista fuera de callouts** (la única excepción es 1 diagrama suelto en la línea 164, que la auditoría marca con W). Todo bloque textual, tabla, embed y fórmula va dentro de un callout.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Dato` (línea 27): tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
23 de 26 callouts de la referencia lo hacen (líneas 11, 28, 38, 48…). La excepción son los callouts 📖 de deck de cátedra, que arrancan con prosa directo (líneas 72-73, 83-84, 92-93).

### R7 · Separadores internos dentro de un callout
- Entre dos párrafos de prosa: una línea `>` vacía entre medio (líneas 29-30).
- Antes de un embed `> ![[...]]`: línea `>` vacía (el 100% de los embeds de la referencia; 0 violaciones).
- Antes de una tabla `> |...`: línea `>` vacía (líneas 60-61).
- Los items del mismo punto/lista van pegados (líneas 15-17; 284-286): solo la prosa/tablo/imagen pide separador.

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
(líneas 237, 244). Prefijo `> >` en dos niveles.

### R9 · Ejemplos con etiqueta negrita
Dentro del callout, la cierre va con etiqueta en negrita: `> **Ejemplos:**`, `> **Se lee así:**`, `> **Por qué importa:**` (líneas 33, 130, 146, 170).

### R10 · Metas de Aprendizaje con checkboxes
```
> [!note] 📋 Nivel Básico
>
> - [ ] Defino dato, información y modelo sin mirar.
```
(líneas 282-286). Un callout por nivel, contenido como checkboxes.

### R11 · Flashcards SR dentro de la sección Repaso
```
#flashcards/bd-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Pregunta?::Respuesta.
```
(líneas 307-315). Con guion `- ` delante de cada flashcard. Las flashcards del plugin SR (`Q::A` + `<!--SR:...-->`) no se tocan cuando existen.

### R12 · Rutas de assets correctas y existentes
`../Unidad 0 - Guias y Ejercicios/Diagramas/...` (líneas 19, 31, 41…). **Un solo nivel** porque todas las notas viven a la misma profundidad (`Sistema de Bases de Datos/Unidad N - .../`): `../../` rompe la resolución. El archivo referenciado debe existir.

### R13 · Tags al pie
`**Tags:** #TICG1018 #...` al final (línea 340).

## Material que NO entra
`_texto/`, PDFs de clase, `Contenido Extra/`, docs de `Herramientas/` — (carriles CLAUDE2 y existentes en qa_material_nuevo.py).

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_sbd.py" --solo "3er Semestre/Sistema de Bases de Datos"
```
Severidades: **H** (error duro, rompe lectura o el sitio) y **W** (desviación de formato). `--estricto` también hace fallar los W. `--fix-rutas` repara automáticamente los embeds con profundidad incorrecta cuando la profundidad correcta sí existe.