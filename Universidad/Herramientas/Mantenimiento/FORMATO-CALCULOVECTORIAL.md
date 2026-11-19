---
dg-publish: false
---

# 📐 FORMATO-CALCULOVECTORIAL — contrato de formato de las notas de Cálculo Vectorial

> [!info] 📖 Fuente única de verdad
> Este contrato **adopta el de Sistema de Bases de Datos** (`FORMATO-SBD.md`, reglas R1..R14)
> sin rebajarlo. El validador `qa_formato_calcvectorial.py` **importa** `qa_formato_sbd.py` y
> ejecuta su mismo núcleo (R1..R14) **más las reglas propias de esta materia** (R15, R16, R17),
> igual que hicieron `FORMATO-CALCULO1.md` (MATG1045) y `FORMATO-MATDISC.md` (MATG1051).
>
> Encargo del dueño (18/11/2026): *"Me parece bien, pero si tienes que crear un contrato como
> los demas, para ponerse a trabajar en esto lo mas que puedas"* — Cálculo Vectorial
> (MATG1046, prerrequisito MATG1045) es la siguiente materia a auditar/cerrar.
>
> Además del formato, el contenido debe estar **bien explicado**: una nota que solo transcribe
> apuntes o imágenes es tan útil como no leerlos. Ver **R14**.

## Las 14 reglas de SBD (adoptadas) + R15 · R16 · R17

### R1 · Frontmatter
```
---
dg-publish: true
tags: [MATG1046, unidadN, temas...]
---
```
Sin `dg-publish: true` la nota no se publica (`qa_omitidas.py` la detecta).

### R2 · Título H1 con emoji
`# 📐 Definición y Clasificación de Funciones de Varias Variables`. Emoji visible + texto.

### R3 · Secciones H2, cada una con emoji y separadas por `---`
El esqueleto mínimo de una nota de clase (8 secciones):
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
Las secciones temáticas de la materia (teoremas, superficies, coordenadas,
campos vectoriales, integrales, jacobiana, Hessiana…) van **entre `Definiciones
Formales` y `Ejercicios Propuestos`**.

**Perfiles.** El validador resuelve el perfil solo por la ruta de la nota:

| Perfil | Se aplica a | H2 requeridas |
|---|---|---|
| `clase` | notas dentro de `Unidad N - …/` (N ≥ 1), incluso anidadas varios niveles | las **8** de arriba |
| `indice` | raíz de la materia y `Unidad 0 - …/` | ninguna (**0**), pero todo H2 que exista lleva emoji |

> [!warning] ⚠️ Cálculo Vectorial tiene unidades anidadas
> La carpeta de una nota puede ser `Unidad 5 - Línea e Integrales Dobles/II - Integrales de Línea/`.
> El perfil se decide **buscando un ancestro `Unidad N` con N ≥ 1** (no por la carpeta
> inmediata), igual que en Cálculo 1.

### R4 · TODO el contenido dentro de callouts
Cero líneas de prosa, tabla, lista, embed fuera de callouts. Los encabezados H2/H3 y los
`---` son estructura y van sueltos.

### R5 · Callout con título siempre
`> [!note] 📋 Definición — Gradiente`. Tipo + emoji + texto. Nunca un callout sin título.

### R6 · Línea en blanco `>` después del encabezado del callout
```
> [!note] 📋 Definición — Gradiente
>
> El cuerpo del callout…
```

### R7 · Separadores internos dentro de un callout
- Entre dos párrafos de prosa: una línea `>` vacía entre medio.
- Antes de un embed `> ![[…]]`: línea `>` vacía.
- Antes de una tabla `> |…`: línea `>` vacía.
- Los items de la misma lista van pegados.

### R8 · Solución anidada y plegada en los ejercicios
```
> [!example] 📋 Planteamiento
>
> Enunciado…
>
> > [!success]- ✅ Solución
> >
> > Respuesta…
```
Prefijo `> >` y el `success` **plegado** (`[!success]-`). Aplica a los ejemplos de
`Ejercicios Propuestos`.

### R9 · Etiquetas en negrita
Dentro del callout: `> **Ejemplos:**`, `> **Se lee así:**`, `> **Por qué importa:**`,
`> **Ejemplo:**`.

### R10 · Metas de Aprendizaje con checkboxes
Un callout por nivel, con checkboxes. La sección **Metas de Aprendizaje** debe contener
al menos un callout con el patrón `- [ ]`.

### R11 · Flashcards SR dentro de la sección Repaso
```
#flashcards/calcvec-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es el gradiente?::El vector de derivadas parciales…
```
La directiva queda **fuera** del callout; las líneas `- Q::A`, **dentro** del 🧠.
Identificador `calcvec-uN`, con N el número de unidad.

### R12 · Rutas de assets y fuentes mermaid
- Los diagramas viven en `Unidad 0 - Guias y Ejercicios/Diagramas/`, en mermaid, y
  **todo SVG lleva su `.mmd` fuente al lado**.
- Los embeds de assets usan tantos `../` como la **profundidad de la nota dentro de la materia**:

| Nota | Prefijo |
|---|---|
| raíz de la materia | `Unidad 0 - Guias y Ejercicios/…` |
| nota a 1 nivel (`Unidad 5 - …/01 - …md`) | `../Unidad 0 - …` |
| nota a 2 niveles (`Unidad 5 - …/II - …/01 - …md`) | `../../Unidad 0 - …` |

- **No se embeben PDF/PPTX/DOC/XLS de clase** (`R12-clase-embebida`): se citan como 📎
  wikilink. El syllabus oficial `SPA-SyllabusEUR_ACE-MATG1046.pdf` se enlaza, no se embebe.

### R13 · Tags al pie
`**Tags:** #MATG1046 #unidadN #…` al final de la nota.

### R14 · Todo lo visual se explica (no se transcribe)
Un embed **sin lectura propia** es una transcripción. Cada pieza visual lleva, en las líneas
siguientes, una interpretación propia:

| Etiqueta | Qué responde | Mínimo |
|---|---|---|
| `**Se lee así:**` | ¿Qué dice la imagen en su propia forma? (cajas, flechas, filas, flechas) | 2–4 frases |
| `**Por qué importa:**` | ¿Qué consecuencia tiene? ¿Qué error evita? | 1–3 frases |
| `**Ejemplo:**` | ¿Cómo se aplica a un caso propio de la ESPOL o de la carrera? | 1 frase con caso concreto |

La lectura se escribe **desde la fuente** (el `.mmd` del SVG o el texto extraído del PDF),
nunca transcribiendo la imagen a ojo.

### R15 · Cada definición lleva su figura (regla propia heredada de Cálculo 1)
Un callout de definición (`> [!note] 📋 Definición — …`) **contiene su propia figura**
(embed `.svg`/`.png`) **dentro** del mismo callout, con su lectura R14. En Cálculo Vectorial
la figura de la definición es la que dibuja el plano, la superficie, los vectores — sin ella
el lector tiene que imaginarse la geometría que la definición describe.

### R16 · Flashcards por unidad (regla propia de la familia)
Mínimo **3 tarjetas** `Q::A` dentro del callout 🧠, con directiva `#flashcards/calcvec-uN`
eco de la unidad de la nota.

### R17 · Metas de Aprendizaje con checkboxes
Mínimo **3 metas** con checkbox `- [ ]` en la sección `Metas de Aprendizaje`.

## Receta de producción

### Diagramas (SVG)
Todo diagrama vive en `Unidad 0 - Guias y Ejercicios/Diagramas/`, es **mermaid** y lleva su
fuente `.mmd` al lado. Render:
```
$env:PUPPETEER_EXECUTABLE_PATH="C:\Program Files\Google\Chrome\Application\chrome.exe"
py -X utf8 "Universidad\Herramientas\SVG-Pipeline\mmdc_ligero.py" -i X.mmd -o X.svg -b white
```
**Round-trip obligatorio**: re-render del `.mmd` y comparación contra el SVG de texto
visible + viewBox. `verifica_mmd.py` lo hace automáticamente.

**Reglas de sintaxis mermaid:**
- En `erDiagram`, las etiquetas con `,` o `:` van entre comillas.
- `<br/>` y emojis sí funcionan.
- Un SVG **siempre** necesita su `.mmd`. Si falta, se reconstruye desde el SVG
  (`svg_a_mmd.py --lote <carpeta>`) y se valida re-renderizando. **Nunca** se sobrescribe
  un `.mmd` que ya está en git.

### Notas nuevas: orden de trabajo
1. Esqueleto con los H2 del perfil y `---` entre ellos.
2. Callouts con definiciones y ejemplos (**R4**, **R5**, **R6**, **R9**).
3. Diagramas: `.mmd` → render → embed **dentro del callout de la definición** → leerlo
   (**R14**, **R15**).
4. Ejercicios con solución plegada (**R8**).
5. Metas con checkboxes (**R10**, **R17**) y flashcards dentro del callout 🧠 (**R11**, **R16**).
6. `**Tags:**` al pie (**R13**).
7. Auditar y corregir hasta 0 hallazgos.

## Cómo se audita
```
py -X utf8 "Universidad\Herramientas\Mantenimiento\qa_formato_calcvectorial.py"
```
Severidades: **H** (error duro) y **W** (desviación de formato). `--estricto` también hace
fallar los W. `--solo <ruta>` audita una parte y `--calibrar` audita la nota de referencia.

> [!success] ✅ Reglas heredadas de SBD
> `qa_formato_calcvectorial.py` **importa** `qa_formato_sbd.py`: no reimplementa R1..R14, las
> ejecuta; cambia solo el perfil de anidamiento y añade R15..R17.
