---
dg-publish: false
---

# 📐 FORMATO-FESD — contrato de formato de las notas de Fundamentos de Electricidad y Sistemas Digitales

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique. Su hermano es `FORMATO-SBD.md`, en la misma carpeta.
>
> Las **20 notas de clase** de la materia ya comparten un esqueleto propio (Introducción → secciones
> temáticas → Resumen Visual → Metas de Aprendizaje → Referencias) y un estilo que es del dueño del
> vault. Este contrato lo fija por escrito y le añade las dos secciones de cierre que la casa usa en
> todas las materias publicadas (**Conexiones** y **Seguir estudiando**). Cualquier sesión (humana o
> asistente) debe escribir notas de FESD que **pasen** `qa_formato_fesd.py`.
>
> Donde este contrato y `FORMATO-SBD.md` difieren, **manda este** para FESD (FESD tiene más perfiles,
> más profundidad de carpetas y material en PDF que no se embebe).

## Las 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [EYAG1037, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica. El código de la cátedra es **EYAG1037**.

### R2 · Título H1 con emoji
`# ⚡ Conceptos Fundamentales de la Electricidad`. Emoji visible + texto.

### R3 · Secciones H2 con emoji y el esqueleto de la materia
El esqueleto canónico de una nota de clase (**Ver ejemplos vivos en `Unidad 1/01` y en `Unidad 4/01`**):
```
## 🎯 Introducción
## <tema con su emoji> (1..n secciones temáticas)
## 📊 Resumen Visual
## ✅ Metas de Aprendizaje
## 📚 Referencias
## 🔗 Conexiones
## 🔗 Seguir estudiando
```

Las secciones temáticas son variables (una o varias). Todo H2 lleva emoji.

**Perfiles.** El validador distingue las notas por su ruta:

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | `Teórico/Unidad N - …/NN - ….md` | Introducción · Resumen Visual · Metas de Aprendizaje · Referencias · Conexiones · Seguir estudiando (**6**) |
| `guia` | `Teórico/Unidad N - …/Ejercicios Recopilados - EYAG1037.md` | Metas de Aprendizaje · Conexiones · Seguir estudiando (**3**) |
| `practica` | `Practico/Practicas del Laboratorio/Práctica N FESD/….md` | Seguridad · Materiales · Notas personales · Informe · Guía oficial · Metas de Aprendizaje (**6**; además: Introducción y procedimiento libre) |
| `referencia` | `Practico/Fundamentos del Laboratorio/Equipos del Laboratorio - FESD.md` | ninguna (**0**), pero todo H2 que exista lleva emoji |
| `indice` | notas raíz (`Fundamentos de Electricidad y Sistemas Digitales.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) | ninguna (**0**), pero todo H2 que exista lleva emoji |

Notas de clase: `Referencias` apunta al PDF/deck **exacto** que cubre la nota (ver R15). `Conexiones`
enlaza las notas relacionadas de la materia; `Seguir estudiando` enlaza el material para profundizar
(videos, simuladores, datasets, libros).

### R4 · TODO el contenido dentro de callouts
Ningún bloque de prosa, tabla, lista, embed o fórmula vive fuera de un callout, en **ningún** perfil
(incluido `indice`): si un diagrama o una tabla van sueltos, se envuelven en un callout con título.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Campo Eléctrico`: tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
El callout arranca con una línea `>` sola. Excepción: los callouts 📖 de bibliografía/fuentes pueden
arrancar con prosa directo.

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
```
> [!note] 🎯 Nivel Básico
>
> - [ ] Explico la notación $(N)_r$ y qué representa la base de un sistema de numeración.
```
Un callout por nivel, contenido como checkboxes. La regla **solo aplica dentro de la sección
`Metas de Aprendizaje`**: los callouts `📋 Nivel 1…` de los cuestionarios de las secciones
temáticas son agrupación de preguntas, no metas, y no piden checkbox.

### R11 · Flashcards SR (si se usan)
FESD no tiene flashcards hoy (0 `#flashcards`, 0 `Q::A`). Si se añaden:
```
#flashcards/fesd-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Pregunta?::Respuesta.
```
La directiva queda **fuera** del callout; todas las líneas `- Q::A` van **dentro** del callout 🧠.

### R12 · Rutas de assets correctas y existentes
La **profundidad `../` depende de dónde vive la nota**. Cuenta los niveles desde la nota hasta la
raíz de la materia y usa los `../` que toquen. Tabla de la casa:

| La nota vive en | Ejemplo | Assets (`Unidad 0 - Guias y Ejercicios/…`) |
|---|---|---|
| raíz de la materia (`indice`) | `Índice de Contenido.md` | `Unidad 0 - Guias y Ejercicios/Diagramas/x.svg` (sin `../`) |
| `Teórico/Unidad N - …/` (`clase`, `guia`) | `Teórico/Unidad 1 - Electricidad y Circuitos/01 - ….md` | `../../Unidad 0 - Guias y Ejercicios/Diagramas/x.svg` |
| `Practico/Fundamentos del Laboratorio/` (`referencia`) | `Equipos del Laboratorio - FESD.md` | `../../Unidad 0 - Guias y Ejercicios/…` |
| `Practico/Practicas del Laboratorio/Práctica N FESD/` (`practica`) | `Práctica 2 — ….md` | `../../../Unidad 0 - Guias y Ejercicios/Diagramas/x.svg` |

El archivo referenciado **debe existir** (el validador comprueba; en Windows las rutas crudas de
más de 260 caracteres se recortan, por eso el QA normaliza antes de comprobar — Obsidian las
resuelve igual).

Además:
- **No se embeben PDF/PPTX/DOC/XLS de clase** (`R12-clase-embebida`). El material de clase se
  **enlaza** con `[[ruta.pdf|alias]]` (R15); si la nota transcribe una página concreta, esa página
  se **captura como PNG** (DPI 140) en `Archivos/` y se cita por su número de página.
- **Todo SVG embebido tiene su `.mmd` fuente al lado** (`R12-svg-sin-mmd`).
- **No se referencia material ajeno** (`R12-ajeno`): `_texto/`, `Contenido Extra/`,
  `Herramientas/`, `site/`, `reportes/`, `svg-pipeline/`.

### R13 · Tags al pie
`**Tags:** #EYAG1037 #unidad1 #…` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe) — **P (pendiente)**
> [!warning] 🚨 La regla que separa "leer la nota" de "leer el PDF"
> Un embed sin lectura propia es una transcripción: es tan difícil de entender como el material
> original. Cada pieza visual lleva, **en las líneas siguientes**, una interpretación propia.

**Qué exige R14 (mecanizado en `qa_formato_fesd.py`, severidad P):**
1. **Cada PNG de captura** va seguido de una de estas etiquetas — o de prosa propia de
   **≥ 60 caracteres** que no sea la ruta del embed:
   `**Se lee así:**` · `**Por qué importa:**` · `**Ejemplos:**` / `**Ejemplo:**` · `**Nota:**`
2. **Cada SVG (mermaid)** va seguido de la misma lectura.
3. La ruta del propio embed **no cuenta** como explicación.

**Etiquetas aceptadas (case-insensitive):** `Se lee así` · `Por qué importa` · `Ejemplo(s)` ·
`Nota` · `Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Para qué sirve` ·
`Qué notas` · `Pista`.

**Cómo se escribe una buena lectura** (3 bloques, en este orden):

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | ¿Qué dice la imagen **en su propia forma**? | 2–4 frases |
| `**Por qué importa:**` | ¿Qué **consecuencia** tiene? ¿Por qué la cátedra la puso? | 1–3 frases |
| `**Ejemplo:**` | ¿Cómo se aplica a **un caso propio**? | 1 frase con caso concreto |

**En esta materia R14 es severidad `P` (pendiente), no H ni W**: los **118** embeds que hoy no
tienen lectura son el trabajo de la ronda de lecturas. La ronda mecánica (este contrato, rutas,
callouts, secciones) **no** los toca; el validador los cuenta aparte y no bloquea el
cierre mecánico. Línea base 2026-11-16: de 219 embeds solo 7 tienen lectura (3 %).

### R15 · Los enlaces a material de clase llevan alias legible
En FESD el material de clase se **enlaza**, no se embebe. El enlace se escribe con alias:
```
📎 [[Practico/Practicas del Laboratorio/Práctica 2 FESD/Práctica 2 Ley de Ohm.pdf|Práctica 2 Ley de Ohm y Kirchhoff.pdf]]
```
El alias es lo que se ve en el sitio: no puede quedar vacío, ni repetir la ruta, ni ser más corto
de 3 caracteres (`R15-enlace-clase-sin-alias`). El patrón 📎 de la casa para bibliografía es un
enlace con este emoji visible.

### R16 · Nada de material ajeno
`_texto/`, `Contenido Extra/`, docs de `Herramientas/`, `site/`, `reportes/`, `svg-pipeline/` — no
se referencian ni se embeben (`R12-ajeno`).

## Material que NO entra
`_texto/`, `Contenido Extra/`, docs de `Herramientas/`. El material de clase (PDF de diapositivas y
guías) **vive en la materia y se enlaza** (R15); lo que no entra es volcarlo como embed (R12).

## Receta de producción

### Diagramas (SVG)
Todos los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/` y son **mermaid**, con su
fuente `.mmd` **al lado** (R12-svg-sin-mmd).

**Naming:** `uX-YY-NN-tipo.mmd` / `uX-YY-NN-tipo.svg`
- `uX` unidad · `YY` nota · `NN` correlativo del diagrama en esa nota · `tipo` ∈ catálogo:

| Sufijo | Qué es | Se dibuja como |
|---|---|---|
| `-graph` | panorama / cadena de pasos / comparación | `flowchart` |
| `-flow` | algoritmo o procedimiento con decisiones | `flowchart` |
| `-tree` | jerarquía | `flowchart TD` |
| `-seq` | secuencia temporal | `sequenceDiagram` |
| `-state` | máquina de estados | `stateDiagram-v2` |
| `-mind` | mapa mental / panorama de un tema | `flowchart` |

Los diagramas antiguos de FESD (`01_-_Tema_01.svg`, con `.mmd` al lado) preestrenan el catálogo: se
respetan tal cual; el naming de arriba aplica a diagramas nuevos.

**Render:**
```
py -3.12 Herramientas/SVG-Pipeline/mmdc_ligero.py -i X.mmd -o X.svg -b white
$env:PUPPETEER_EXECUTABLE_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**Nunca** se sobrescribe un `.mmd` que ya está en git.

### Capturas de deck y de PDF (PNG)
1. Se **captura la página** del PDF, no se embebe el PDF.
2. **DPI 140** → 1862×1027 px (láminas 16:9) o 1637×1158 px (láminas 4:3).
3. Carpeta por tema: `Archivos/<tema>/` (por ejemplo `Archivos/Electricidad/`).
4. Naming: `fesd-<deck>-pNN[-<slug>].png`.
5. En la nota se cita **con el número de página**: `SESIÓN 3, p. 12` / `Guía Práctica 1, pp. 2-4`.
6. El contenido de la lámina se extrae **por texto** del PDF (PyMuPDF, `pdf_a_png.py` para la
   captura). **No se leen las imágenes a ojo**: la lectura escrita sale del texto extraído.

### Nota nueva: orden de trabajo
1. Esqueleto con los H2 del perfil y `---` entre ellos.
2. Callouts con definiciones y ejemplos (**R4**, **R5**, **R6**, **R9**).
3. Diagramas: escribir el `.mmd`, renderizar, embeber dentro de un callout, y **leerlo** (**R14**).
4. PDF de clase: enlazar con alias (**R15**); capturar como PNG solo las páginas transcritas
   (**R14**).
5. Ejercicios con solución plegada (**R8**).
6. Metas con checkboxes (**R10**).
7. `**Tags:**` al pie (**R13**).
8. Auditar y corregir hasta 0 hallazgos H y W.

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_fesd.py" --solo "3er Semestre/Fundamentos de Electricidad y Sistemas Digitales"
```
Severidades: **H** (error duro), **W** (desviación de formato), **P** (pendiente de la ronda de
lecturas, solo R14). `--estricto` también hace fallar los W; `--estricto-pendientes` hace fallar
también los P. `--fix-rutas` repara automáticamente los embeds con profundidad incorrecta cuando
la profundidad correcta sí existe. `--calibrar` audita solo `Unidad 1/01 - Conceptos`.

## Nota de ubicación

Este contrato **no** vive en `3er Semestre/Fundamentos de Electricidad y Sistemas Digitales/`: es
una herramienta, y el sitio publica la carpeta de la materia. Vive en
`Universidad/Herramientas/Mantenimiento/`, junto al validador que lo aplica (`qa_formato_fesd.py`) y
a su hermano (`FORMATO-SBD.md`).

> [!success] ✅ Estado actual (línea base 2026-11-16)
> `qa_formato_fesd.py` registra **482** hallazgos en las **33** notas: **82** errores (H),
> **282** avisos (W) y **118** pendientes de lectura (P). Se cierra por bloques:
> F2 rutas · F3 embeds fuera de callout y formatos · F4 secciones faltantes + metas ·
> F5 los 6 `.mmd` ausentes · F6 commit. Las 118 lecturas (R14) y los PDF de clase quedan
> documentados para una segunda ronda.
