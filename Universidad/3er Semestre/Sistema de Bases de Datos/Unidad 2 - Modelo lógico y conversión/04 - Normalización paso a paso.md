---
dg-publish: true
tags: [TICG1018, unidad2, normalizacion, paso-a-paso, bd]
---

# 🛠️ Normalización Paso a Paso

## 🎯 Introducción

> [!info] 💡 Normalizar es un Protocolo, No un Salto
>
> Las formas normales se aplican **en orden**: 1FN es el piso, 2FN cura las parciales, 3FN cura las transitivas y BCNF es el chequeo final. Cada curación sigue siempre el mismo gesto: **partir la tabla y dejar el determinante en la original como FK**.
>
> **Analogía:** es una limpieza por capas — desarmas el mueble pieza por pieza; nunca arrancas la pata si aún hay tornillos sueltos.

---

## 🧰 Lo que Necesitas Antes de Empezar

> [!info] 🧰 Los 4 pre-requisitos
>
> 1. **La tabla ya en 1FN** — un valor por celda, sin grupos repetitivos. Sin piso no se normaliza: [[02 - Primera forma normal y diccionario de datos]].
> 2. **La PK identificada** — si es compuesta, hay 2FN por hacer; si es simple, saltas directo a la 3FN.
> 3. **La lista completa de DFs** — no se inventan: salen de mirar qué datos se repiten juntos. El repaso está en [[03 - Segunda y tercera forma normal]].
> 4. **El orden fijo** — 2FN antes que 3FN: una parcial sin curar se disfraza de transitiva.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-04-05-graph.svg]]
>
> **Analogía:** antes de operar, plan leído y radiografía hecha. Sin los 4 ítems, partes a ciegas.

---

## 🛠️ Método: el protocolo paso a paso

> [!note] 📋 Protocolo
>
> 1. **¿Está en 1FN?** Un valor por celda, sin grupos repetitivos. Si no, corrige primero.
> 2. **¿2FN?** Si la PK es compuesta, busca DFs cuyo determinante sea *solo parte de la PK*. Por cada parcial: tabla nueva con él como PK, mueve sus dependientes y **déjalo en la original como FK**. Si la PK es simple, la 2FN es automática y pasas directo al paso 3.
> 3. **¿3FN?** Busca transitivas: un **no-primo** determinando a otro no-primo (`no-primo → no-primo`). Por cada transitiva: tabla nueva con el determinante como PK, mueve sus dependientes y déjalo como FK.
> 4. **¿BCNF?** Chequea si **todo determinante es clave candidata**. Si algún determinante no-clave sobrevive, parte una vez más.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-04-01-flow.svg]]
> ![[Figuras/bd-s04-p12.png]]

> [!tip] 🎯 Regla de Oro: el Determinante Nunca Abandona
>
> Al partir una tabla, el determinante **se copia en la original como FK** (mudar nunca). Las tablas nuevas necesitan ese puente para reunir los datos con un JOIN; sin FK quedan huérfanas.
>
> **Ejemplo:** de `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)` la transitiva `JOB_CLASS → CHG_HOUR` saca la tabla `JOB`, pero `JOB_CLASS` vive en ambas:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-04-03-graph.svg]]

> [!note] 📋 Herramienta: el Diagrama de Dependencias
>
> Antes de partir, dibuja las DFs: **PK en negrita**; sus flechas (sanas) **arriba**; las sospechosas (parciales y transitivas) **abajo**. Ese dibujo te dice de un vistazo qué tabla nace y qué deja detrás.
>
> Las DFs no se inventan: salen de las filas. Pregúntate por cada columna: ¿con qué valor aparece siempre acompañada? `cod_estud` siempre llega con el mismo `nomb_estud` ⇒ `cod_estud → nomb_estud`.
>
> Filas reales de MATRICULA:
>
> | cod_estud | cod_curso | nomb_estud | nomb_curso | creditos | cod_instructor | nomb_instructor | nota_final |
> |---|---|---|---|---|---|---|---|
> | 101 | BD01 | Ana | BD | 3 | 10 | Dra. Ruíz | 9.5 |
> | 101 | SO01 | Ana | SO | 4 | 20 | Ing. Ponce | 8.0 |
> | 102 | BD01 | Luis | BD | 3 | 10 | Dra. Ruíz | 7.5 |
>
> Mira: `nomb_estud` se repite con cada matrícula del estudiante (parcial), los datos del curso con cada matrícula del curso (parcial), y el instructor está escondido tras el curso (transitiva).
>
> **Caso `MATRICULA(cod_estud, cod_curso, nomb_estud, nomb_curso, creditos, cod_instructor, nomb_instructor, nota_final)`:**
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-04-02-graph.svg]]
> ![[Figuras/bd-023-p15.png]]

---

## 🎨 Ejemplo Trabajado Completo

> [!example] 🟢 De 1NF a BCNF sin perder datos
>
> Entrada: `MATRICULA(cod_estud, cod_curso, nomb_estud, nomb_curso, creditos, cod_instructor, nomb_instructor, nota_final)` — PK = `(cod_estud, cod_curso)`.
>
> > > [!success]- ✅ Pasos
> >
> > 1. **1FN:** cada celda un valor. ✔
> > 2. **2FN (parciales):** `cod_estud → nomb_estud` y `cod_curso → nomb_curso, creditos, cod_instructor` nacen de *parte* de la PK.
> >    - → `ESTUDIANTE(cod_estud, nomb_estud)` + `CURSO(cod_curso, nomb_curso, creditos, cod_instructor)` + original ahora `MATRICULA(cod_estud FK, cod_curso FK, nota_final)`.
> >
> >    ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-04-06-er.svg]]
> >
> > 3. **3FN (transitiva):** dentro de CURSO sobrevive `cod_instructor → nomb_instructor` (no-primo → no-primo).
> >    - → `INSTRUCTOR(cod_instructor, nomb_instructor)` + `CURSO(cod_curso, nomb_curso, creditos, cod_instructor FK)`.
> > 4. **Chequeo BCNF:** los determinantes son `cod_estud`, `cod_curso`, `cod_instructor` — todos claves candidatas. ✔
> >
> > Resultado: 4 tablas, 0 duplicados. Cambiar el nombre de un instructor toca **una** fila.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-04-04-er.svg]]

---

## ⚠️ Errores Comunes

### ❌ Error 1: Buscar parciales con PK simple

> [!danger] ❌ Viola: sin PK compuesta no hay parciales
>
> Con PK de un solo atributo la 2FN es automática — no hay "parte" de la PK. El trabajo ahí es detectar la transitiva (paso 3). En la pizarra: dibuja la PK antes de decidir.

### ❌ Error 2: Mudar el determinante fuera

> [!danger] ❌ Viola: el determinante se queda como FK
>
> Al extraer `JOB`, borrar `JOB_CLASS` de EMPLOYEE rompe el puente: ya no puedes saber qué clase tiene cada empleado. **Copia, no mudes.**

### ❌ Error 3: No revisar la tabla nueva

> [!danger] ❌ Viola: re-evaluar tras cada partición
>
> Cada tabla nueva puede esconder su propia transitiva. Tras cada partición: re-dibuja el diagrama de dependencias de la tabla nueva y vuelve al paso 3. Termina con el chequeo BCNF global.

### ❌ Error 4: Inventar PK nueva en las particiones

> [!danger] ❌ Viola: la PK de la tabla nueva es el determinante
>
> La tabla nueva nace con el **determinante como PK**. Si después inventas un `id` surrrogado, pierdes el chequeo de unicidad que detectaba las anomalías.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Repito el protocolo de 4 pasos sin mirar.
> - [ ] Distingo flecha sana (nace de la PK) de sospechosa (parcial o trans) en un diagrama.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Parto una tabla a 2FN y a 3FN dejando los FKs correctos.
> - [ ] Dibujo el diagrama de dependencias antes de tocar schemas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Decido BCNF mirando si todo determinante es clave candidata.
> - [ ] Encuentro transitivas escondidas en las tablas nuevas tras cada partición.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition

- ¿Protocolo completo en 1 línea?::1FN piso → 2FN (parciales fuera) → 3FN (transitivas fuera) → BCNF (determinantes = claves).
- ¿PK simple, necesario 2FN?::No, es automática; voy directo a buscar transitivas.
- ¿Qué hago con cada determinante parcial?::Tabla nueva con él como PK, muevo dependientes y lo dejo como FK en la original.
- ¿Cómo detecto una transitiva?::Un no-primo determinando a otro no-primo.
- ¿Dónde queda el determinante al partir?::En la tabla original como FK (copiar, no mudar).
- ¿Chequeo BCNF?::Todo determinante debe ser clave candidata.

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
> - ✅ El protocolo de normalización en orden
> - ✅ El diagrama de dependencias como herramienta
> - ✅ La regla del determinante como FK
>
> **Próxima clase:** denormalización y dudas del proyecto.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Anterior: [[03 - Segunda y tercera forma normal]]

---

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (proceso de normalización, §6.3-6.6).
> - Diapositivas BD 02 MC_a_ML: métodos de conversión y formas normales.

---

**Tags:** #TICG1018 #unidad2 #normalizacion #paso-a-paso #bd
