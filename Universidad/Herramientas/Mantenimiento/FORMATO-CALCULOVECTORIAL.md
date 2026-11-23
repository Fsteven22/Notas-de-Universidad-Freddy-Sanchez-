---
dg-publish: false
---

# 📐 FORMATO-CALCULOVECTORIAL — contrato de formato de las notas de Cálculo Vectorial

> [!info] 📖 Estándar de la casa: la nota de SBD
>
> Este contrato **toma como plantilla real** la nota de referencia de Sistema de Bases de Datos
> (`3er Semestre/Sistema de Bases de Datos/Unidad 1 - Modelos de Datos y ER/01 - Dato, información
> y modelos de datos.md`), que es la que usaron las materias ya cerradas a 0 hallazgos
> (SBD, Cálculo 1, FESD, Diseño, MatDisc).
>
> **Corrección de calibración (19/11/2026):** la versión anterior de este contrato se calibró por
> error contra `Unidad 3 – Funciones de Varias Variables/…/01 – Límite de Funciones de Varias
> Variables.md`, que **no cumple este mismo contrato** (tiene 7 hallazgos). Por eso producía
> "0 hallazgos" en notas que no se parecían al estándar. La referencia correcta es SBD.

---

## Plantilla obligatoria de una nota de clase (perfil `clase`)

Copia esta estructura **literal** (los emojis y el orden importan):

```
---
dg-publish: true
tags: [MATG1046, unidadN, tema1, tema2, tema3]
---

# 🐍 Título de la Nota

## 🎯 Introducción

> [!info] 💡 ¿Por qué importa este tema?
>
> Párrafo de enganche (qué problema real resuelve).
>
> **¿Dónde se usa?**
>
> - aplicación 1
> - aplicación 2
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/<FIG>.svg]]
>
> **Se lee así:** qué muestra la figura, caja por caja.
>
> **Por qué importa:** qué consecuencia tiene / qué error evita.

---

## 📋 Definiciones Formales

### 1️⃣ Primer concepto — la idea

> [!note] 📋 Definición — Primer concepto
>
> Enunciado formal de la definición.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/<FIG1>.svg]]
>
> **Se lee así:** lectura de la figura.
>
> **Ejemplo:** caso concreto.

### 2️⃣ Segundo concepto — la idea

> [!note] 📋 Definición — Segundo concepto
>
> Enunciado formal.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/<FIG2>.svg]]
>
> **Se lee así:** lectura.
>
> **Ejemplo:** caso concreto.

---

## 🛠️ Sección temática (opcional, entre Definiciones y Ejercicios)

> [!note] 📋 Título
>
> Contenido: tablas, procedimientos, propiedades, diagramas…

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Título

> [!example] 📋 Planteamiento
>
> Enunciado…
>
> > [!success]- ✅ Solución
> >
> > Desarrollo y resultado.

### ✏️ Ejercicio 2 — Título

> [!example] 📋 Planteamiento
>
> Enunciado…
>
> > [!success]- ✅ Solución
> >
> > Desarrollo y resultado.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] meta 1
> - [ ] meta 2
> - [ ] meta 3

> [!note] 📋 Nivel Intermedio
>
> - [ ] meta 1
> - [ ] meta 2
> - [ ] meta 3

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - fuente 1
> - fuente 2

---

## 🔁 Repaso SR

#flashcards/calcvec-uN

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Pregunta 1?::Respuesta 1.
> - ¿Pregunta 2?::Respuesta 2.
> - ¿Pregunta 3?::Respuesta 3.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[Nota relacionada 1]] — por qué
> - [[Nota relacionada 2]] — por qué

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Cálculo Vectorial]]
> - Siguiente: [[Siguiente nota]]
> - Repaso: [[Nota previa]]

---

**Tags:** #MATG1046 #unidadN #tema1 #tema2 #tema3 #cálculo-vectorial
```

---

## Reglas (R1–R20)

### R1 · Frontmatter con tags temáticos
`tags: [MATG1046, unidadN, ...]` con **mínimo 3 temas además** del código y la unidad.
Ejemplo SBD: `[TICG1018, unidad1, datos, modelos, historia]`.

### R2 · H1 con emoji
`# 🐍 Título` — emoji visible + texto.

### R3 · Ocho secciones H2 canónicas, en este orden
`Introducción`, `Definiciones Formales`, `Ejercicios Propuestos`, `Metas de Aprendizaje`,
`Referencias`, `Repaso SR`, `Conexiones`, `Seguir estudiando`.
Las secciones temáticas van **entre** `Definiciones Formales` y `Ejercicios Propuestos`.
Cada H2 debe llevar emoji y estar precedida por `---` (salvo la primera).

### R4 · TODO el contenido dentro de callouts
Cero prosa/tabla/lista/embed fuera de un callout. Solo H1/H2/H3 y `---` van sueltos.

### R5 · Callout con título
`> [!note] 📋 Definición — X`. Nunca un callout sin título.

### R6 · Línea `>` en blanco tras el encabezado del callout
```
> [!note] 📋 Definición — X
>
> cuerpo…
```

### R7 · Separadores internos
Línea `>` vacía entre párrafos, antes de un embed `> ![[…]]` y antes de una tabla `> |…`.
Los ítems de una misma lista van pegados.

### R8 · Solución anidada y plegada en cada ejercicio
`### ✏️ Ejercicio N` → `> [!example] 📋 Planteamiento` → `> > [!success]- ✅ Solución`.

### R9 · Etiquetas en negrita
`**Se lee así:**`, `**Por qué importa:**`, `**Ejemplo:**`, `**Ejemplos:**` dentro de los callouts.

### R10 · Metas de Aprendizaje con checkboxes
Callouts `> [!note] 📋 Nivel Básico/Intermedio/Avanzado` con `- [ ]`.

### R11 · Flashcards SR dentro de la sección Repaso
`#flashcards/calcvec-uN` fuera del callout; tarjetas `- Q::A` dentro del `🧠`.

### R12 · Rutas de assets
Embeds a `Unidad 0 - Guias y Ejercicios/Diagramas/` con tantos `../` como profundidad tenga la
nota en la materia. Todo SVG lleva su `.mmd` fuente. No se embeben PDF/PPTX/DOC.

### R13 · `**Tags:**` al pie
`**Tags:** #MATG1046 #unidadN #tema…` al final.

### R14 · Todo lo visual se explica
Cada embed lleva, en las líneas siguientes dentro del callout: `**Se lee así:**`,
`**Por qué importa:**`, `**Ejemplo:**`.

### R15 · Cada definición lleva SU PROPIA figura
Todo callout `> [!note] 📋 Definición — …` contiene un embed `.svg`/`.png` **dentro**, con su
lectura R14. (Regla propia de la familia.)

### R16 · Flashcards por unidad
Mínimo **3** tarjetas `Q::A` y directiva `#flashcards/calcvec-uN`.

### R17 · Metas de Aprendizaje con checkboxes
Mínimo **3** metas `- [ ]`.

### R18 · Cada definición en su propio `### N️⃣`
Las definiciones de la sección **Definiciones Formales** van cada una en un H3 numerado
(`### 1️⃣ …`, `### 2️⃣ …`) **inmediatamente seguido** de un único callout
`> [!note] 📋 Definición — …`. No se agrupan varias definiciones en un solo callout.

### R19 · Frontmatter con al menos 3 tags temáticos
(Refuerzo de R1, lo verifica el validador como regla dura.)

### R20 · Las secciones temáticas no sustituyen a las canónicas
Entre `Definiciones Formales` y `Ejercicios Propuestos` puede haber secciones temáticas, pero
las 8 canónicas de R3 deben existir todas.

---

## Cómo se audita

```
py -X utf8 "Universidad\Herramientas\Mantenimiento\qa_formato_calcvectorial.py" --nota "<ruta>.md"
py -X utf8 "Universidad\Herramientas\Mantenimiento\qa_formato_calcvectorial.py" --calibrar
```

**Calibración obligatoria:** `--calibrar` audita la nota piloto
`Unidad 1 - Geometría Analítica en ℝ³/III – Rectas y Planos/01 - Rectas en R3.md`, que es el
molde de referencia de la materia. Debe dar **0 hallazgos**. Si no, el validador está mal.

Severidades: **H** (error duro) y **W** (desviación). `--estricto` hace fallar también los W.
