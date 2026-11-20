---
dg-publish: false
---

# 📐 FORMATO-FISICA — contrato de formato de las notas de Física Mecánica

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo aplica),
> **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota que el
> sitio publique. Sus hermanos son `FORMATO-SBD.md`, `FORMATO-POO.md` y `FORMATO-FESD.md`.
>
> Las **108 notas** de Física Mecánica ya tienen contenido didáctico (definiciones, fórmulas,
> ejemplos, ejercicios, prácticas de laboratorio). Este contrato fija el formato por escrito:
> cualquier sesión (humana o asistente) debe escribir notas de Física Mecánica que **pasen**
> `qa_formato_fisica.py`.

## Las 16 reglas

### R1 · Frontmatter

```
---
dg-publish: true
tags: [FISG1001, unidadN, tema]
---
```

Sin `dg-publish: true` la nota no se publica. El código de la cátedra es `FISG1001`.
Las notas de clase llevan `unidad1`..`unidad6` o `fundamentos`; las de práctica llevan `laboratorio`.

### R2 · Título H1 con emoji

`# 🚗 Cinemática Traslacional`. Emoji visible + texto.

### R3 · Secciones H2 con emoji y el esqueleto de la materia

El esqueleto canónico de una nota de clase de Física Mecánica:

```
## 📋 Conceptos Fundamentales
## 🔢 Variables ...
## 📊 Ecuaciones / Fórmulas / Resumen
## 🧮 Ejemplos / Problemas Resueltos (opcional)
```

Las secciones temáticas son variables (una o varias). Todo H2 lleva emoji.

**Perfiles.** El validador distingue las notas por su ruta:

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | `01 - Cinemática/`, `02 - Dinámica/`, `03 - Trabajo y Energía/`, `04 - Impulso y Colisiones (Lineal)/`, `05 - Equilibrio y Elasticidad/`, `06 - Hidrostática e Hidrodinámica/`, `Fundamentos de Física Mecánica/` | ninguna por nombre fijo, pero todo H2 lleva emoji |
| `practica` | `Practicas De Laboratorio/` | ninguna por nombre fijo, pero todo H2 lleva emoji |
| `indice` | notas raíz (`Física Mecánica.md`, `Bienvenida y Syllabus….md`, `Recursos Visuales.md`, `Índice de Contenido.md`) | ninguna (**0**), pero todo H2 que exista lleva emoji |

### R4 · TODO el contenido dentro de callouts

Ningún bloque de prosa, tabla, lista, embed, fórmula o fence vive fuera de un callout, en
**ningún** perfil. Si un bloque va suelto, se envuelve en un callout con título.

### R5 · Callout con título siempre

`> [!tip] 📍 Posición (x, r) **Definición:** ...`: tipo + emoji + texto. Nunca un callout sin título.

> [!note] 📌 El texto de introducción puede vivir en el propio header
> En esta materia es habitual que la frase de apertura vaya en la primera línea del callout
> (`> [!info] Las gráficas angulares son herramientas…`) y no en líneas internas. El validador
> lo acepta: solo cuenta como *callout vacío* si tampoco hay texto en el título.

### R6 · Línea en blanco `>` después del encabezado del callout

El callout arranca con una línea `>` sola.

### R7 · Separadores internos dentro de un callout

- Antes de un embed `> ![[...]]`: línea `>` vacía.
- Antes de una tabla `> |...`: línea `>` vacía.
- Entre dos párrafos de prosa: una línea `>` vacía entre medio.
- Los ítems del mismo punto/lista van pegados.

### R8 · Ejemplos con solución plegada (cuando existan)

```
> [!example] 🧮 Ejemplo
>
> Enunciado...
>
> > [!success]- ✅ Solución
> >
> > Respuesta...
```

Prefijo `> >` en dos niveles.

### R9 · Etiquetas en negrita dentro del callout

Dentro del callout: `> **Definición:**`, `> **Ejemplo:**`, `> **Nota:**`.

### R10 · Metas de Aprendizaje con checkboxes (cuando existen)

Física no exige Metas, pero las notas que las llevan usan:

```
> [!note] 📋 Objetivo
>
> - [ ] Sé aplicar la segunda ley de Newton sin ayuda.
```

### R11 · Flashcards SR (si se usan)

Física no tiene flashcards hoy. Si se añaden, las líneas `- Q::A` van dentro del callout 🧠.

### R12 · Rutas de assets correctas y existentes

| La nota vive en | Ejemplo | Assets |
|---|---|---|
| raíz de la materia | `Física Mecánica.md` | `Unidad 0 - Guias y Ejercicios/Diagramas/x.svg` |
| `Unidad N - …/` (`clase`) | `02 - Dinámica/Leyes de Newton.md` | `../Unidad 0 - Guias y Ejercicios/Diagramas/x.svg` |
| `Practicas De Laboratorio/` (`practica`) | `Práctica de Caída Libre.md` | `../Unidad 0 - Guias y Ejercicios/Diagramas/x.svg` |

El archivo referenciado debe existir. Además:

- **No se embeben PDF/PPTX/DOC/XLS de clase** (`R12-clase-embebida`): el syllabus y las guías se
  **enlazan** con `📎 [[ruta.pdf|alias]]`; la página transcrita se captura como PNG (DPI 140) si
  hace falta.
- **Todo SVG embebido tiene su `.mmd` fuente al lado** (`R12-svg-sin-mmd`).
- **No se referencia material ajeno** (`R12-ajeno`): `_texto/`, `Contenido Extra/`,
  `Herramientas/`, `site/`, `reportes/`, `svg-pipeline/`.

### R13 · Tags al pie

`**Tags:** #FISG1001 #unidad1 #cinematica #…` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe) — **P (pendiente)**

> [!warning] 🚨 La regla que separa "leer la nota" de "leer el PDF"
> Un embed sin lectura propia es una transcripción: es tan difícil de entender como el material
> original. Cada pieza visual lleva, **en las líneas siguientes**, una interpretación propia.

**Qué exige R14 (mecanizada en `qa_formato_fisica.py`, severidad P):**

1. **Cada PNG/captura** va seguido de `**Se lee así:**` · `**Por qué importa:**` · `**Ejemplo(s):**`
   o de prosa propia de **≥ 60 caracteres** que no sea la ruta del embed.
2. **Cada SVG (mermaid)** va seguido de la misma lectura.
3. La ruta del propio embed **no cuenta** como explicación.

**En esta materia R14 es severidad `P`:** las lecturas quedan para una segunda ronda.

### R15 · Los enlaces a material de clase llevan alias legible

```
📎 [[Unidad 0 - Guias y Ejercicios/Diapositivas/FISG1001-Slides-S01 Sesión 1.pdf|Slides Sesión 1]]
```

El alias es lo que se ve en el sitio: no puede estar vacío, ni repetir la ruta, ni llevar `/`
(`R15-enlace-clase-sin-alias`).

### R16 · Nada de material ajeno

`_texto/`, `Contenido Extra/`, docs de `Herramientas/`, `site/`, `reportes/`, `svg-pipeline/` —
no se referencian ni se embeben (`R12-ajeno`).

## Material que NO entra

`_texto/`, `Contenido Extra/`, docs de `Herramientas/`. El material de clase (syllabus, guías)
**vive en la materia y se enlaza** (R15); no se embebe (R12).

## Receta de producción

### Diagramas (SVG)

Todos los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/` y son **mermaid**, con su
fuente `.mmd` **al lado** (R12-svg-sin-mmd).

Si falta la fuente:

- `flowchart-v2` → `py -X utf8 SVG-Pipeline/svg_a_mmd.py --lote <carpeta>`
- `mindmap` → reconstructor de mindmap (árbol desde aristas `edge_A_B`, `root((…))` y `id("texto")`)
- `sequence` / `pie` / `classDiagram` → reconstrucción manual; `note over` de mermaid admite solo
  **dos** participantes y los alias con paréntesis van entre comillas.

### Capturas de material (PNG)

1. Se captura la página concreta, no se embebe el PDF.
2. **DPI 140**.
3. Carpeta: `Archivos/<tema>/`.
4. Naming: `fisica-<tema>-pNN.png`.
5. En la nota se cita con el número de página.

### Nota nueva: orden de trabajo

1. Esqueleto con los H2 del perfil y `---` entre ellos.
2. Callouts con definiciones y fórmulas (**R4**, **R5**, **R6**, **R9**).
3. Diagramas: escribir el `.mmd` (si no existe), renderizar, embeber dentro de un callout, y
   **leerlo** (**R14**).
4. PDF de clase: enlazar con alias (**R15**); capturar páginas transcritas (**R14**).
5. Ejercicios con solución plegada (**R8**).
6. `**Tags:**` al pie (**R13**).
7. Auditar y corregir hasta 0 hallazgos H y W.

## Cómo se audita

```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_fisica.py" --solo "1er Semestre/Física Mecánica"
```

Severidades: **H** (error duro), **W** (desviación de formato), **P** (pendiente de la ronda de
lecturas: R14). `--estricto` también hace fallar los W; `--estricto-pendientes` hace fallar
además los P. `--calibrar` audita solo `01 - Cinemática/Cinemática Traslacional`.

## Nota de ubicación

Este contrato **no** vive en `1er Semestre/Física Mecánica/`: es una herramienta, y el sitio
publica la carpeta de la materia. Vive en `Universidad/Herramientas/Mantenimiento/`, junto al
validador que lo aplica (`qa_formato_fisica.py`) y sus hermanos.

> [!success] ✅ Estado actual (2026-11-19)
> `qa_formato_fisica.py` registra **230** hallazgos en las **108** notas: **0 H**, **1 W**
> (`R2-h1` en la única nota vacía) y **229 P** (lecturas R14). Línea base al empezar la ronda:
> 1 530 hallazgos con 851 H.
>
> Pendientes:
> - **R14 (229)**: la ronda de lecturas, nota por nota.
> - `03 - Trabajo y Energía/Aplicaciones de Trabajo y Energía/Problemas de Potencia y Gradiente de
>   Potencial.md` estaba **vacía**; debe llevar contenido propio.
