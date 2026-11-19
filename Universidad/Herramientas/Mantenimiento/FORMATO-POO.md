---
dg-publish: false
---

# 📐 FORMATO-POO — contrato de formato de las notas de Programación Orientada a Objetos

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo aplica),
> **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota que el
> sitio publique. Sus hermanos son `FORMATO-SBD.md`, `FORMATO-DISENO.md` y `FORMATO-FESD.md`.
>
> Las **23 notas de clase** de la materia ya comparten un esqueleto propio —Introducción → temas
> → **Resumen Visual**— y un estilo que es del dueño del vault: código Java completo y comentado,
> tablas, callouts, emojis, diagramas SVG. Este contrato lo fija por escrito: cualquier sesión
> (humana o asistente) debe escribir notas de POO que **pasen** `qa_formato_poo.py`.
>
> Donde este contrato difiere de `FORMATO-SBD.md` (la casa común), **manda este** para POO:
> POO no usa Metas, Referencias, Conexiones ni Repaso SR obligatorias.

## Las 16 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [CCPG1044, unidadN, java...]
---
```
Sin `dg-publish: true` la nota no se publica. El código de la cátedra lo fija el plan del vault
(revisar `Bienvenida y Syllabus`); las notas raíz ya llevan `tags:`.

### R2 · Título H1 con emoji
`# 🎯 Introducción al Paradigma Orientado a Objetos`. Emoji visible + texto.

### R3 · Secciones H2 con emoji y el esqueleto de la materia
El esqueleto canónico de una nota de clase:
```
## 🎯 Introducción  (apertura habitual, ya no exigida — ver Perfiles)
## <tema con su emoji> (1..n secciones temáticas)
## 📊 Resumen Visual
```

Las secciones temáticas son variables (una o varias). Todo H2 lleva emoji.

**Perfiles.** El validador distingue las notas por su ruta:

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | `Unidad N - …/NN - ….md` | Resumen Visual (**1**) — Introducción ya no exigida (la nota 01 de U1 abre con la pregunta «¿Qué es la Programación Orientada a Objetos?»; el resto conserva su `## 🎯 Introducción` por costumbre; cambio del 18/11/2026) |
| `indice` | notas raíz (`Programación Orientada a Objetos.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) | ninguna (**0**), pero todo H2 que exista lleva emoji |

No son H2 requeridas pero son comunes y recomendadas: `📝 Ejercicios Prácticos`,
`🚀 Próximos Pasos`, `📋 Referencias` (las trae la nota de sintaxis y alguna más).

### R4 · TODO el contenido dentro de callouts
Ningún bloque de prosa, tabla, lista, embed, fórmula o fence vive fuera de un callout, en
**ningún** perfil. Si un bloque va suelto, se envuelve en un callout con título. Excepción única:
los diagramas SVG sueltos se envuelven en callout como todo lo demás (no vale dejarlos crudos).

### R5 · Callout con título siempre
`> [!note] 📋 Nombre — tema`: tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
El callout arranca con una línea `>` sola, salvo los callouts 📖 de bibliografía.

### R7 · Separadores internos dentro de un callout
- Antes de un embed `> ![[...]]`: línea `>` vacía.
- Antes de una tabla `> |...`: línea `>` vacía.
- Entre dos párrafos de prosa: una línea `>` vacía entre medio.
- Los items del mismo punto/lista van pegados.

### R8 · Callout anidado plegado en los ejercicios y ejemplos
```
> [!example] 📋 Ejemplo
>
> Enunciado...
>
> > [!success]- ✅ Solución
> >
> > Respuesta...
```
Prefijo `> >` en dos niveles. Los `[!code]` Java van también dentro de callout.

### R9 · Ejemplos con etiqueta en negrita
Dentro del callout: `> **Ejemplo:**`, `> **Se lee así:**`, `> **Por qué importa:**`.

### R10 · Metas de Aprendizaje con checkboxes (cuando existen)
POO no exige Metas, pero las notas que las llevan usan esta forma (`qa_formato_poo.py` R10, cuadro>
cuando existen callouts de **Nivel**):
```
> [!note] 📋 Nivel Básico
>
> - [ ] Entiendo X sin mirar.
```

### R11 · Flashcards SR (si se usan)
POO no tiene flashcards hoy. Si se añaden:
```
#flashcards/poo-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Pregunta?::Respuesta.
```
La directiva queda fuera; las líneas `- Q::A` van dentro del callout 🧠.

### R12 · Rutas de assets correctas y existentes

| La nota vive en | Ejemplo | Assets |
|---|---|---|
| raíz de la materia (`Docs/índice`) | `Programación Orientada a Objetos.md` | `Unidad 0 - Guias y Ejercicios/Diagramas/x.svg` |
| `Unidad N - …/` (`clase`) | `Unidad 1 - …/01 - ….md` | `../Unidad 0 - Guias y Ejercicios/Diagramas/x.svg` |

El archivo referenciado debe existir. Además:

- **No se embeben PDF/PPTX/DOC/XLS de clase** (`R12-clase-embebida`): el syllabus y las guías se
  **enlazan** con `[[ruta.pdf|alias]]`; la página transcrita se captura como PNG (DPI 140) si
  hace falta.
- **Todo SVG embebido tiene su `.mmd` fuente al lado** (`R12-svg-sin-mmd`).
- **No se referencia material ajeno** (`R12-ajeno`): `_texto/`, `Contenido Extra/`,
  `Herramientas/`, `site/`, `reportes/`, `svg-pipeline/`.

### R13 · Tags al pie
`**Tags:** #CCPG1044 #unidad1 #…` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe) — **P (pendiente)**
> [!warning] 🚨 La regla que separa "leer la nota" de "leer el PDF"
> Un embed sin lectura propia es una transcripción: es tan difícil de entender como el material
> original. Cada pieza visual lleva, **en las líneas siguientes**, una interpretación propia.

**Qué exige R14 (mecanizada en `qa_formato_poo.py`, severidad P):**
1. **Cada PNG/captura** va seguido de `**Se lee así:**` · `**Por qué importa:**` · `**Ejemplo(s):**` /
   `**Ejemplo:**` · `**Nota:**` — o de prosa propia de **≥ 60 caracteres** que no sea la ruta del embed.
2. **Cada SVG (mermaid)** va seguido de la misma lectura.
3. La ruta del propio embed **no cuenta** como explicación.

**Etiquetas aceptadas (case-insensitive):** `Se lee así` · `Por qué importa` · `Ejemplo(s)` ·
`Nota` · `Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Resumen Visual` ·
`Para qué sirve` · `Qué notas` · `Pista`.

**En esta materia R14 es severidad `P`:** las 120 lecturas quedan para la ronda de lecturas; la
ronda mecánica no las toca. Línea base 2026-11-16: de 166 SVG, solo ~46 tienen lectura (28 %).

### R15 · Los enlaces a material de clase llevan alias legible
```
📎 [[Unidad 0 - Guias y Ejercicios/Guías/SPA-Syllabus-….pdf|Syllabus POO (PDF)]]
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

**Naming:** `uX-YY-NN-tipo.mmd` / `uX-YY-NN-tipo.svg`
- `uX` unidad · `YY` nota · `NN` correlativo · `tipo` ∈ `-graph` (flowchart) · `-flow` (algoritmo) ·
  `-tree` (jerarquía) · `-seq` (secuencia) · `-state` (estados) · `-mind` (mapa mental) ·
  `-class` (diagrama de clases, como `classDiagram` simple o flowchart) · `-er` (ER).

Los diagramas antiguos USE `01_-_Seccion_NN.svg` y se respetan tal cual; el naming de arriba
aplica a diagramas nuevos.

**Nunca** se sobrescribe un `.mmd` que ya está en git.

### Capturas de material (PNG)
1. Se captura la página concreta, no se embebe el PDF.
2. **DPI 140**.
3. Carpeta: `Archivos/<tema>/`.
4. Naming: `poo-<tema>-pNN.png`.
5. En la nota se cita con el número de página.
6. El contenido se extrae por texto (PyMuPDF), no a ojo.

### Nota nueva: orden de trabajo
1. Esqueleto con los H2 del perfil y `---` entre ellos.
2. Callouts con definiciones y ejemplos (**R4**, **R5**, **R6**, **R9**).
3. Diagramas: escribir el `.mmd` (si no existe), renderizar, embeber dentro de un callout, y
   **leerlo** (**R14**).
4. PDF de clase: enlazar con alias (**R15**); capturar páginas transcritas (**R14**).
5. Ejercicios con solución plegada (**R8**).
6. `**Tags:**` al pie (**R13**).
7. Auditar y corregir hasta 0 hallazgos H y W.

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_poo.py" --solo "2do Semestre/Programación orientada a objetos"
```
Severidades: **H** (error duro), **W** (desviación de formato), **P** (pendiente de la ronda de
lecturas, solo R14). `--estricto` también hace fallar los W; `--estricto-pendientes` hace fallar
además los P. `--calibrar` audita solo `Unidad 1/01 - Introducción`.

## Nota de ubicación

Este contrato **no** vive en `2do Semestre/Programación orientada a objetos/`: es una herramienta,
y el sitio publica la carpeta de la materia. Vive en `Universidad/Herramientas/Mantenimiento/`,
junto al validador que lo aplica (`qa_formato_poo.py`) y sus hermanos.

> [!success] ✅ Estado actual (línea base 2026-11-16)
> `qa_formato_poo.py` registra **567** hallazgos en las **27** notas: **7** H (6 R4-prosa-top
> + 1 R4-lista-top), **440** W y **120** P. Se cierra por bloques: F1 contrato+QA · F2/F3 callouts
> · F4 tags/metas/secciones · F5 los 166 `.mmd` reconstruidos desde los SVG
> (`svg_a_mmd.py` + verificación re-render). Las 120 lecturas (R14) quedan para una segunda
> ronda documentada.
