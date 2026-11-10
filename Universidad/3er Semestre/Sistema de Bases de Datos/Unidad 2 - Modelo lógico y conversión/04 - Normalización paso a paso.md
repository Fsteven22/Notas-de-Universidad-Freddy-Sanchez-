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

## 📋 Definiciones Formales

### 1️⃣ Dependencia Funcional (DF)

> [!note] 📋 Definición — Dependencia Funcional
>
> Escribimos `X → Y` cuando **conocer X basta para saber Y**: no hay dos filas con el mismo X y distinto Y. X es el **determinante** y Y el **dependiente**.
>
> **Se lee así:** `cod_estud → nomb_estud` quiere decir *"si sé el código del estudiante, ya sé su nombre"*. Por eso el nombre se repite: depende de algo que no es su clave.
>
> **Ejemplo:** en la tabla de repeatable, todas las filas con `cod_estud = 101` traen `nomb_estud = Ana`. Eso es una DF, y se lee mirando los datos, no inventándola.

### 2️⃣ Dependencia Parcial

> [!note] 📋 Definición — Dependencia Parcial
>
> Es una DF cuyo determinante es **parte** de la clave primaria (y no la clave completa). Rompe la 2FN.
>
> **Se lee así:** si la PK es `(cod_estud, cod_curso)` y `cod_estud → nomb_estud`, el nombre depende de *media* clave. Es como dejar una nota pegada solo a la mitad izquierda del composite.
>
> **Por qué importa:** al cambiar el nombre del estudiante tendrías que actualizar todas sus filas de matrícula; por eso la `nomb_estud` sale a su propia tabla.

### 3️⃣ Dependencia Transitiva

> [!note] 📋 Definición — Dependencia Transitiva
>
> Es una DF entre dos atributos que **no son parte de la clave**: `no-primo → no-primo`. Rompe la 3FN.
>
> **Se lee así:** `cod_curso → cod_instructor` y `cod_instructor → nomb_instructor` encadenadas. El nombre del instructor no depende del curso, depende del instructor: está "escondido" detrás.
>
> **Ejemplo:** en `CURSO(cod_curso, nomb_curso, creditos, cod_instructor, nomb_instructor)`, `nomb_instructor` repite por cada curso del mismo instructor. Sale a `INSTRUCTOR`.

### 4️⃣ Forma Normal (FN)

> [!note] 📋 Definición — Forma Normal
>
> Una relación está en una FN cuando cumple una restricción concreta sobre sus DFs. Cada FN **elimina una familia de anomalías** (de inserción, de actualización y de borrado).
>
> | Forma | Qué exige | Qué elimina |
> |---|---|---|
> | **1FN** | Una celda, un valor (sin listas ni grupos) | Datos multivaluados escondidos |
> | **2FN** | Nada depende de *parte* de la PK | Redundancia por clave compuesta |
> | **3FN** | Ningún no-primo depende de otro no-primo | Redundancia por cadenas de DFs |
> | **BCNF** | Todo determinante es clave candidata | Determinantes no-clave que sobreviven |
>
> **Se lee así:** son capas. 1FN es el suelo (si no cumples eso, las otras no tienen sentido), 2FN se apoya en la 1FN, 3FN en la 2FN y BCNF es el chequeo final. Por eso el orden importa: una parcial sin curar se disfraza de transitiva.

### 5️⃣ Diagrama de Dependencias

> [!note] 📋 Definición — Diagrama de Dependencias
>
> Es el dibujo de las DFs como flechas: cada atributo es una caja y cada DF es una flecha del determinante al dependiente. Sirve para **ver** qué tablas van a nacer antes de crear ninguna.
>
> **Se lee así:** flechas que salen de la PK (en negrita) son **sanas**: la tabla ya está bien. Flechas que salen de una parte de la PK o de un no-primo son **sospechosas**: cada una anuncia una tabla nueva.
>
> **Por qué importa:** es el mapa de la partición. Si dibujas el diagrama antes de partir, cada paso del protocolo se ve mecánicamente: "esta flecha sospechosa se va con su dependiente, y el determinante se queda como FK".

---

## 🧰 Lo que Necesitas Antes de Empezar

> [!info] 🧰 Los 4 pre-requisitos
>
> 1. **La tabla ya en 1FN** — un valor por celda, sin grupos repetitivos. Sin piso no se normaliza: [[02 - Primera forma normal y diccionario de datos]].
> 2. **La PK identificada** — si es compuesta, hay 2FN por hacer; si es simple, saltas directo a la 3FN.
> 3. **La lista completa de DFs** — no se inventan: salen de mirar qué datos se repiten juntos. El repaso está en [[03 - Segunda y tercera forma normal]].
> 4. **El orden fijo** — 2FN antes que 3FN: una parcial sin curar se disfraza de transitiva.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-05-graph.svg]]
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-01-flow.svg]]
>
> **Se lee así:** el diagrama del protocolo completo, de arriba abajo. Primero la pregunta de la 1FN (si no, corrige antes de seguir); luego *"¿la PK es compuesta?"* — si **no** lo es, la 2FN es automática y saltas directo a buscar transitivas; si **sí**, la siguiente pregunta es *"¿hay alguna flecha que nazca de solo parte de la PK?"*. Cada flecha sospechosa produce una tabla nueva con ese determinante como PK, y el determinante **se queda como FK** en la original. De ahí se pasa a la 3FN (*"¿no-primo → no-primo?"*), y de la 3FN al chequeo BCNF (*"¿todo determinante es clave candidata?"*), que puede obligarte a volver a partir una vez más.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p12.png]]
>
> **Se lee así:** la lámina del deck (p. 12 de *slides04*) trae el **ejemplo clásico** de la 2FN con la tabla `Staff`, que tiene PK compuesta `(staffNo, branchNo)`. Fíjate en las flechas: `branchNo → branchAddress` y `staffNo → name, position` **nacen de una sola mitad de la clave**, mientras que `staffNo, branchNo → hoursPerWeek` nace de la clave **completa**. La lámina marca las dos primeras con *"No 2FN: dependencia parcial"*. Es decir: `hoursPerWeek` (las horas que trabaja un empleado *en una sucursal*) sí depende de todo el par; pero la dirección de la sucursal depende solo de la sucursal, y el nombre y el puesto del empleado solo del empleado.
>
> **Por qué importa:** este ejemplo muestra por qué la 2FN **solo** existe cuando la PK es compuesta. Si tu PK es un solo atributo, no hay "mitades" de la clave y la 2FN se cumple sola — como dice la propia lámina, *"la segunda forma normal aplica a tablas con clave primaria compuesta"*. Y el reparto que deja la tabla es el que se aplica: `branchNo` con su dirección en una tabla, `staffNo` con nombre y puesto en otra, y el HoursPerWeek se queda con la tabla puente porque necesita las dos mitades.
>
> **Ejemplo:** traducido a tu caso, la tabla `MATRICULA(cod_estud, cod_curso, nomb_estud, nomb_curso, ...)` tiene exactamente la misma forma: `cod_estud → nomb_estud` es la "dependencia parcial" de la lámina, y por eso el nombre del estudiante sale a `ESTUDIANTE`.

> [!tip] 🎯 Regla de Oro: el Determinante Nunca Abandona
>
> Al partir una tabla, el determinante **se copia en la original como FK** (mudar nunca). Las tablas nuevas necesitan ese puente para reunir los datos con un JOIN; sin FK quedan huérfanas.
>
> **Ejemplo:** de `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)` la transitiva `JOB_CLASS → CHG_HOUR` saca la tabla `JOB`, pero `JOB_CLASS` vive en ambas:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-03-graph.svg]]

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-02-graph.svg]]
>
> **Se lee así:** el diagrama de dependencias del caso, codificado por color para que la partición sea evidente. En **verde** la flecha sana: `(cod_estud, cod_curso) → nota_final`, la PK completa hacia su único dependiente, esa no se toca. En **ámbar** las flechas que nacen de *media* PK: `cod_estud → nomb_estud` y `cod_curso → nomb_curso, creditos, cod_instructor` — son las **parciales** que anuncian dos tablas nuevas. En **rojo** la cadena `cod_instructor → nomb_instructor`, la **transitiva**: el nombre del instructor no depende del curso, depende del instructor, así que sale a su propia tabla.
>
> **Por qué importa:** el diagrama es el *plan de partición*. Cada flecha ámbar o roja es una tabla que todavía no existe; la verde se queda como está. Si lo dibujas antes de partir, después cada paso del protocolo es literalmente "recoger esta flecha y crear su tabla", sin sorpresas.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-023-p15.png]]
>
> **Se lee así:** esta lámina del deck (p. 15 de *BD 02.3 Normalización*) es el **molde** del método: cinco atributos sin nombre (A, B, C, D, E) unidos por flechas, y debajo la pregunta que se repite en cada ejercicio — *«¿está en 1FN? ¿qué dependencias funcionales tiene?»*. Fíjate en que la lámina **no** trae los nombres de tus columnas: trae el esqueleto. Flecha significa *"si conozco el origen, ya sé el destino"*; los rótulos A…E son los huecos que tú llenas con `cod_estud`, `cod_curso`, etc.
>
> **Por qué importa:** el orden de la lámina (primero verificar 1FN, *después* buscar DFs) es exactamente el orden del protocolo. No tiene sentido buscar dependencias funcionales sobre una tabla que todavía tiene grupos repetitivos: sobre una tabla mal formada las DFs que ves son falsas, y partirías por la dependencia equivocada.
>
> **Ejemplo:** la lámina del deck y el caso de arriba son el mismo ejercicio en dos formatos — la primera te da el esqueleto (`A → B`, `C → D`), la segunda te da los datos reales (`cod_estud → nomb_estud`). Cuando resuelvas un ejercicio de examen, dibuja el esqueleto primero y luego rellénalo.

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
> >    ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-06-er.svg]]
> >
> > 3. **3FN (transitiva):** dentro de CURSO sobrevive `cod_instructor → nomb_instructor` (no-primo → no-primo).
> >    - → `INSTRUCTOR(cod_instructor, nomb_instructor)` + `CURSO(cod_curso, nomb_curso, creditos, cod_instructor FK)`.
> > 4. **Chequeo BCNF:** los determinantes son `cod_estud`, `cod_curso`, `cod_instructor` — todos claves candidatas. ✔
> >
> > Resultado: 4 tablas, 0 duplicados. Cambiar el nombre de un instructor toca **una** fila.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-04-er.svg]]
>
> **Se lee así:** el diagrama es **el modelo final del ejercicio**, con las cuatro tablas ya separadas: `ESTUDIANTE(cod_estud PK, nomb_estud)`, `CURSO(cod_curso PK, nomb_curso, creditos, cod_instructor FK)`, `INSTRUCTOR(cod_instructor PK, nomb_instructor)` y `MATRICULA(cod_estud PK FK, cod_curso PK FK, nota_final)`. Las tres relaciones llevan etiqueta en singular: `ESTUDIANTE ||--o{ MATRICULA : "matricula"`, `CURSO ||--o{ MATRICULA : "recibe"` y `INSTRUCTOR ||--o{ CURSO : "dicta"`.
>
> **Por qué importa:** fíjate en que `MATRICULA` es **la única tabla con PK compuesta** (dos columnas marcadas `PK, FK`) y también la única con un atributo propio, `nota_final`. Esa es la señal de que era una relación N:N: la PK compuesta es la huella de la tabla intermedia. Y fíjate en que `CURSO` **conserva** `cod_instructor` como FK: el curso sigue sabiendo quién lo dicta, pero ya no repite el nombre del instructor.
>
> **Ejemplo:** la prueba de que el modelo está bien es que **cada dato vive en un solo lugar**. El nombre del instructor está en `INSTRUCTOR` y en ninguna otra tabla. Si el instructor cambia de nombre, hay un solo `UPDATE` que lo cambia, y no importa cuántos cursos dicta ni cuántos alumnos lo tienen matriculado.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Identifica la PK y las DFs

> [!example] 📋 Planteamiento
>
> Tabla `NOTAS(cod_alumno, cod_asignatura, nota, nombre_alumno, nombre_asignatura)`.
>
> - a) ¿Cuál es la PK?
> - b) Enumera las DFs que ves en los datos.
> - c) ¿Alguna es parcial? ¿Alguna transitiva?
>
> > [!success]- ✅ Solución
> > >
> > - **a)** PK = `(cod_alumno, cod_asignatura)`: la nota de un alumno en una asignatura. Ni uno solo identifica: el mismo alumno tiene varias notas y la misma asignatura la tienen muchos.
> > - **b)** `(cod_alumno, cod_asignatura) → nota`; `cod_alumno → nombre_alumno`; `cod_asignatura → nombre_asignatura`.
> > - **c)** **Parcial:** `cod_alumno → nombre_alumno` (depende de media PK). No hay transitiva: `nombre_alumno` y `nombre_asignatura` no determinan a nada más.
> > >
> > > **Por qué:** si solo miraras las columnas y no los datos, pensarías que `nota` es el PK (¡es lo único que cambia!). La PK no es "el dato más único", es "el dato que identifica la fila completa".

### ✏️ Ejercicio 2 — Normaliza hasta 3FN

> [!example] 📋 Planteamiento
>
> Con la tabla del ejercicio 1 y las DFs que encontraste:
>
> - a) Pasa a 2FN.
> - b) Pasa a 3FN (si hace falta).
> - c) Nombra una anomalía de cada tipo que se eliminó.
>
> > [!success]- ✅ Solución
> > >
> > - **a) 2FN:** sale `ALUMNO(cod_alumno PK, nombre_alumno)` y queda `NOTAS(cod_alumno PK/FK, cod_asignatura PK/FK, nota)`. El nombre sale porque dependía de media PK.
> > - **b) 3FN:** no hace falta partir más — no queda ninguna transitiva. `NOTAS` y `ALUMNO` están en 3FN.
> > - **c) Anomalías eliminadas:**
> >   - *De inserción:* antes no podías crear un alumno sin nota (su `nombre_alumno` viajaba en la fila de `NOTAS`); ahora sí, con `ALUMNO`.
> >   - *De actualización:* antes corregir el nombre de un alumno obligaba a tocar todas sus filas; ahora, una.
> >   - *De borrado:* antes borrar la última nota de un alumno borraba también su nombre; ahora el nombre sobrevive en `ALUMNO`.
> > >
> > > **Se lee así:** esas tres anomalías son el *motivo* de normalizar. Si no puedes nombrar cuál se eliminó, no terminaste el ejercicio.

### ✏️ Ejercicio 3 — Detecta la transitiva escondida

> [!example] 📋 Planteamiento
>
> `EMPLEADO(emp_num PK, emp_name, job_class, chg_hour)`, con las DFs:
>
> - `emp_num → emp_name, job_class, chg_hour`
> - `job_class → chg_hour`
>
> - a) ¿En qué FN está?
> - b) Normaliza.
> - c) ¿Dónde queda `job_class`?
>
> > [!success]- ✅ Solución
> > >
> > - **a)** Está en **2FN**: la PK es simple, así que no hay parciales, pero la transitiva `job_class → chg_hour` impide la 3FN.
> > - **b)** Sale `JOB(job_class PK, chg_hour)` y queda `EMPLEADO(emp_num PK, emp_name, job_class FK)`.
> > - **c)** `job_class` queda **en las dos**: como PK en `JOB` y como FK en `EMPLEADO`. Esa es la regla de oro — el determinante se **copia**, nunca se muda.
> > >
> > > **Por qué importa:** si quitas `job_class` de `EMPLEADO`, dejaste a los empleados sin saber cuánto gana su clase. El FK es el puente, no un adorno.

### ✏️ Ejercicio 4 — El chequeo BCNF

> [!example] 📋 Planteamiento
>
> `PROVEEDOR(prov_id PK, nombre, ciudad_id FK, ciudad, provincia)`, con:
>
> - `prov_id → nombre, ciudad_id`
> - `ciudad_id → ciudad, provincia`
>
> - a) ¿Está en 3FN?
> - b) ¿Está en BCNF?
> - c) ¿Qué hay que hacer?
>
> > [!success]- ✅ Solución
> > >
> > - **a)** **Sí**, está en 3FN: `ciudad_id → ciudad, provincia` es transitiva (no-primo → no-primo) y se cura con `CIUDAD(ciudad_id PK, ciudad, provincia)`, dejando `ciudad_id` como FK en `PROVEEDOR`.
> > - **b)** **No.** En BCNF todo determinante debe ser clave candidata. Después de la partición, `ciudad_id` sigue determinando a `ciudad` y `provincia`… salvo que `ciudad_id` sea ahora la PK de `CIUDAD`, en cuyo caso **sí** es clave candidata y la relación queda en BCNF.
> > - **c)** Si al curarla sigue quedando algún determinante no-clave, se parte una vez más con la misma regla: tabla nueva con el determinante como PK + el determinante como FK en la original.
> > >
> > > **Se lee así:** BCNF es el mismo gesto que 3FN pero sin la excepción de los primos. Si te sale una DF cuyo determinante no es clave, aplica el mismo parting otra vez.

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
>
> - ¿Protocolo completo en 1 línea?::1FN piso → 2FN (parciales fuera) → 3FN (transitivas fuera) → BCNF (determinantes = claves).
> - ¿PK simple, necesario 2FN?::No, es automática; voy directo a buscar transitivas.
> - ¿Qué hago con cada determinante parcial?::Tabla nueva con él como PK, muevo dependientes y lo dejo como FK en la original.
> - ¿Cómo detecto una transitiva?::Un no-primo determinando a otro no-primo.
> - ¿Dónde queda el determinante al partir?::En la tabla original como FK (copiar, no mudar).
> - ¿Chequeo BCNF?::Todo determinante debe ser clave candidata.

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
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Anterior: [[03 - Segunda y tercera forma normal]]

---

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (proceso de normalización, §6.3-6.6).
> - Diapositivas `BD 02 MC_a_ML.pdf` — métodos de conversión y formas normales (Unidad 0 — Diapositivas).
> - Diapositivas `2026_1PAO_slides3_final_1_TICG1018.pdf` — la normalización paso a paso (Unidad 0 — Diapositivas).
> - Diapositivas `2026_1PAO_slides4_1_TICG1018.pdf` — el diagrama de dependencias y la regla del determinante (Unidad 0 — Diapositivas).

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u2-paso

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Protocolo completo en 1 línea?::1FN piso → 2FN (parciales fuera) → 3FN (transitivas fuera) → BCNF (determinantes = claves).
> - ¿PK simple, necesario 2FN?::No, es automática; voy directo a buscar transitivas.
> - ¿Qué hago con cada determinante parcial?::Tabla nueva con él como PK, muevo dependientes y lo dejo como FK en la original.
> - ¿Cómo detecto una transitiva?::Un no-primo determinando a otro no-primo.
> - ¿Dónde queda el determinante al partir?::En la tabla original como FK (copiar, no mudar).
> - ¿Chequeo BCNF?::Todo determinante debe ser clave candidata.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[02 - Primera forma normal y diccionario de datos]] — el piso: una celda, un valor.
> - [[03 - Segunda y tercera forma normal]] — las formas con sus anomalías y el diagrama de dependencias.
> - [[01 - Conversión MC a ML por cardinalidad]] — del conceptual a las tablas, antes de normalizar.
> - [[../Unidad 1 - Modelos de Datos y ER/03 - Modelo relacional, ERM y casos Tiny College|03 - Modelo relacional, ERM y casos Tiny College]] — el modelo relacional donde se aplica el protocolo.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización|Guía de Problemas 2]] — el caso del hotel resuelto con este mismo protocolo.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Anterior: [[03 - Segunda y tercera forma normal]]
> - Siguiente: [[../Unidad 3 - Álgebra Relacional/01 - Operadores Básicos|Álgebra Relacional — Operadores Básicos]]

---

**Tags:** #TICG1018 #unidad2 #normalizacion #paso-a-paso #bd
