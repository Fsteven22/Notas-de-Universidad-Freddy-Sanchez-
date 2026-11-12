---
dg-publish: false
---

# 📐 FORMATO-CALCULO1 — contrato de formato de las notas de Cálculo de una Variable

> [!info] 📖 Fuente única de verdad
> Este contrato vive en `Universidad/Herramientas/Mantenimiento/` (junto al validador que lo
> aplica), **no** dentro de la carpeta de la materia: es una herramienta de auditoría, no una nota
> que el sitio publique. Sus hermanos son `FORMATO-SBD.md` y `FORMATO-DISENO.md`, en la misma
> carpeta.
>
> Cálculo de una Variable (MATG1045) tiene **65 notas**: 61 de clase (7 unidades, con subniveles
> `I - …`, `II - …`) y 4 de raíz. El método es el de la casa (SBD, Diseño); lo **propio** de esta
> materia es el esqueleto de secciones, que **no es fijo**: cada nota tiene sus secciones
> temáticas y las de cierre.

## Las 14 reglas

### R1 · Frontmatter
```
---
dg-publish: true
tags: [MATG1045, calculo-de-una-variable, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica. El código de la cátedra es **MATG1045**.

### R2 · Título H1 con emoji
`# 🎯 Métricas en Matemáticas`. El emoji va **al inicio** (41 de 65 lo hacen; 14 lo llevan al
final y 10 no llevan ninguno: se normalizan al inicio).

### R3 · Secciones H2 con emoji, y una sección de cierre
Cada H2 lleva un emoji visible. En las notas de clase, además, la nota **cierra** con al menos una
sección de cierre —`Referencias`, `Notas Recomendadas` o `Conexiones`— (55 de 61 la tienen hoy).

**No hay esqueleto fijo de H2.** A diferencia de SBD (14 secciones) y Diseño (12 secciones), aquí
cada nota tiene su propio recorrido temático; lo que se exige es:

- todo H2 con emoji;
- el cierre con bibliografía o notas relacionadas;
- las secciones características de la materia —`Técnica de Estudio: …`, `Tabla Resumen`,
  `Algoritmo de Decisión`, `Ejemplos Trabajados Completos`, `Conexiones y Aplicaciones`,
  `Ejercicios Progresivos`— **cuando apliquen**, con ese nombre.

**Perfiles.** El validador distingue las notas por su ruta:

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | `Unidad N - …/[subnivel/]0X - …md` | cierre (Referencias \| Notas Recomendadas \| Conexiones) |
| `material` | `Unidad 0 - Guias y Ejercicios/Material de clase/…` | ninguna; todo H2 que exista lleva emoji |
| `indice` | notas raíz (`Cálculo de una Variable.md`, `Índice de Contenido.md`, `Recursos Visuales.md`, `Bienvenida y Syllabus….md`) | ninguna; todo H2 que exista lleva emoji |

### R4 · TODO el contenido dentro de callouts
Ningún bloque de prosa, tabla, lista, embed o fórmula vive fuera de un callout. Si un diagrama
va suelto, se envuelve en un callout con título.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Acoplamiento`: tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
El callout arranca con una línea `>` sola.

### R7 · Separadores internos dentro de un callout
- Antes de un embed `> ![[...]]`: línea `>` vacía.
- Antes de una tabla `> |...`: línea `>` vacía.
- Entre dos párrafos de prosa: una línea `>` vacía entre medio.
- Los items del mismo punto/lista van pegados.

### R8 · Callout anidado plegado en las soluciones
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

### R10 · Tipo de callout válido y en minúscula
Tipos admitidos: `info`, `note`, `tip`, `success`, `example`, `warning`, `caution`, `danger`,
`error`, `bug`, `quote`, `brain`, `todo`, `question`, `abstract`, `summary`.
`> [!NOTE]` y `> [!info-]` no son tipos válidos: el sitio no los reconoce y caen a `Nota` genérica.

### R11 · Enlaces que resuelven
Todo `[[wikilink]]` a una nota apunta a una nota que **existe en el vault** (se comprueba en
todo el vault, no solo en la materia) y todo `![[embed]]` a un asset apunta a un archivo real.

### R12 · Rutas de assets correctas, canónicas y existentes
Los diagramas viven **todos** en `Unidad 0 - Guias y Ejercicios/Diagramas/`; las capturas, en
`Unidad 0 - Guias y Ejercicios/Figuras/`. El prefijo relativo depende de la profundidad de la nota
respecto a la raíz de la materia:

| Profundidad de la nota | Prefijo a `Unidad 0 - Guias y Ejercicios/` |
|---|---|
| `Unidad N - …/0X - …md` | `../Unidad 0 - Guias y Ejercicios/…` |
| `Unidad N - …/I - …/0X - …md` | `../../Unidad 0 - Guias y Ejercicios/…` |

Además:
- **Todo SVG embebido tiene su `.mmd` fuente al lado** (`R12-svg-sin-mmd`): sin fuente, el
  diagrama no se puede re-editar ni volver a compilar.
- **Ningún SVG fuera de la carpeta canónica** (`R12-diagrama-fuera`).
- **Ningún PDF/PPTX/DOC embebido** (`R12-clase-embebida`).
- **Nada de material ajeno** (`R12-ajeno`): `_texto/`, `site/`, `Herramientas/`, `Reportes/`.

### R13 · Tags al pie
`**Tags:** #MATG1045 #unidad1 #...` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe)
> [!warning] 🚨 La regla que separa "leer la nota" de "leer el PDF"
> Un embed sin lectura propia es una transcripción: es tan difícil de entender como el material
> original. Cada pieza visual lleva, **en las líneas siguientes**, una interpretación propia.

**Qué exige R14:**
1. **Cada SVG embebido** va seguido de una de estas etiquetas:
   `**Se lee así:**` · `**Por qué importa:**` · `**Ejemplo(s):**` · `**Nota:**`
   — o de prosa propia de **≥ 60 caracteres** que no sea la ruta del embed.
   La ruta del propio embed **no cuenta** como explicación.
2. **Cada PNG/JPG de figura** va seguido de la misma lectura.

**Etiquetas aceptadas (case-insensitive):** `Se lee así` · `Por qué importa` · `Ejemplo(s)` ·
`Nota` · `Cómo se lee` · `Verificación` · `Analogía` · `Resumen` · `Para qué sirve` ·
`Qué notas` · `Pista`.

**Cómo se escribe una buena lectura** (3 párrafos, en este orden):

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | ¿Qué dice la imagen **en su propia forma**? (qué cajas hay, qué flechas, qué filas) | 2–4 frases |
| `**Por qué importa:**` | ¿Qué **consecuencia** tiene? ¿Qué error evita? | 1–3 frases |
| `**Ejemplo:**` | ¿Cómo se aplica a **un caso propio** de la ESPOL o de la carrera? | 1 frase con caso concreto |

## Material que NO entra
`_texto/` (extracciones de texto, solo local), documentos de `Herramientas/`, PDFs de clase.
La `Unidad 0 - Guias y Ejercicios/` de esta materia **está vacía de material**: no hay PDF ni
láminas, así que **no hay de dónde sacar lecturas de deck y no se inventan citas**.

## Receta de producción

### Diagramas (SVG)
Todos los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/` y son **mermaid**, con su
fuente `.mmd` **al lado** (R12-svg-sin-mmd).

**Naming (convención ya vigente en la materia y en Cálculo Vectorial — no se renombra):**
`NN_-_Titulo_de_la_Nota_NN.svg` · `01_-_Continuidad_y_Límites_01.svg`

**Render:**
```
py -3.12 Herramientas/SVG-Pipeline/mmdc_ligero.py -i X.mmd -o X.svg -b white
$env:PUPPETEER_EXECUTABLE_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
```

**Reglas de sintaxis mermaid (las que fallan sin avisar):**
- En `erDiagram`, las etiquetas de relación con `,` o `:` **no parsean** → van entre comillas.
- `<br/>` y emojis sí funcionan dentro de esas comillas.
- Un SVG **siempre** necesita su `.mmd`. Si falta, se reconstruye desde el SVG y se valida
  re-renderizando y comparando texto visible + viewBox. **Nunca** se sobrescribe un `.mmd` que ya
  está en git.

**Sintaxis verificada en esta materia (183/183 diagramas con round-trip exacto):**
- **Todo label va entre comillas dobles** (`A["texto"]`, `B{"decision"}`, `C("redondeado")`).
  Sin comillas, una `{`, un `|`, un `;` o un `>` dentro del texto rompe el lexer.
- La comilla doble del texto se escapa como `#quot;`.
- En `mindmap`, los paréntesis del texto se escapan como entidades: `F#40;b#41; - F#40;a#41;`.
  Con `F(b) - F(a)` a secas el diagrama **no parsea**.
- En `mindmap`, para que el nodo conserve su forma hay que declararla:
  `x1(F#40;…#41;)` (redondeada) o `x1[F#40;…#41;]` (cuadrada). Sin forma, el layout cambia.
- El **título** que pinta mermaid (`<text class="flowchartTitleText">`) sale del frontmatter YAML:
  ```
  ---
  title: "02 - Propiedades de la Integral: integral indefinida"
  ---
  ```
  Sin ese bloque, el viewBox sale 54 px más corto.
- Un diagrama con **subgrafos** necesita `flowchart LR` + `direction TB` dentro de cada `subgraph`
  para reproducir el layout original (ver `Bienvenida_y_Syllabus_Cálculo_de_una_Variable_01.mmd`).

**Herramientas del pipeline para esta materia:**
- `Universidad/Herramientas/SVG-Pipeline/svg_a_mmd.py` — reconstruye el `.mmd` desde el SVG
  (lee los ids de nodo `my-svg-flowchart-<ID>-<n>` y de arista `my-svg-L_<ORIG>_<DEST>_<n>`,
  la forma de cada caja, sus estilos y el título). `--lote` reconstruye una carpeta; `--sincronizar`
  alinea el frontmatter de título de los `.mmd` existentes. No cubre los diagramas con subgrafos.
- `Universidad/Herramientas/SVG-Pipeline/verifica_mmd.py` — round-trip: re-renderiza cada `.mmd` y
  compara **texto visible** (nodos, etiquetas de arista y título) y **viewBox** contra su SVG.
  Es el que deja la materia en 0 hallazgos de R12.

**Si el `.mmd` se borró del repo**, se recupera del historial (no se reescribe a mano):
```
git ls-tree -r --name-only <commit>^ -- "Universidad/1er Semestre/Cálculo de una Variable/Diagramas/"
git show <commit>^:"Universidad/1er Semestre/Cálculo de una Variable/Diagramas/X.mmd"
```

### Figuras (PNG/JPG)
Viven en `Unidad 0 - Guias y Ejercicios/Figuras/` con **nombre temático**:
`cal1-<tema>-<slug>.png`. Un archivo `Pasted image 2025….png` o con UUID **no** es publicable:
se renombra y se reescribe el embed.

### Nota nueva: orden de trabajo
1. Frontmatter con `dg-publish` y `tags` (R1).
2. H1 y H2 con emoji (R2, R3).
3. Callouts con definiciones y ejemplos (**R4**, **R5**, **R6**, **R9**).
4. Diagramas: escribir el `.mmd`, renderizar, embeber dentro de un callout, y **leerlo** (**R14**).
5. Cierre con `Referencias` / `Notas Recomendadas` (**R3**).
6. `**Tags:**` al pie (**R13**).
7. Auditar y corregir hasta 0 hallazgos.

## Cómo se audita
```
py -3.12 "Universidad/Herramientas/Mantenimiento/qa_formato_calculo1.py" --solo "1er Semestre/Cálculo de una Variable"
```
Severidades: **H** (error duro, rompe lectura o el sitio) y **W** (desviación de formato).
`--estricto` también hace fallar los W. `--fix-rutas` repara automáticamente los embeds cuando la
ruta canónica existe de verdad.

## Nota de ubicación
Este contrato **no** vive en `1er Semestre/Cálculo de una Variable/`: es una herramienta, y el sitio
publica la carpeta de la materia. Vive en `Universidad/Herramientas/Mantenimiento/`, junto al
validador que lo aplica (`qa_formato_calculo1.py`) y a sus hermanos (`FORMATO-SBD.md`,
`FORMATO-DISENO.md`).
