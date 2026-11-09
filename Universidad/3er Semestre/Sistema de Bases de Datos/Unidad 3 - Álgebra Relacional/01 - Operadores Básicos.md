---
dg-publish: true
tags: [TICG1018, unidad3, algebra-relacional, operadores-basicos, bd]
---

# 🧮 Álgebra Relacional — Operadores Básicos

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Álgebra Relacional?
>
> SQL esconde las operaciones matemáticas que hacen posible cada consulta. Entender el álgebra relacional es lo que separa escribir consultas que "funcionan" de escribir consultas que se ejecutan de forma eficiente. Es el lenguaje formal que subyace a todo motor de bases de datos relacionales.
>
> **Aplicaciones:**
> - Diseño de consultas: entender qué hace cada cláusula SQL bajo el capó.
> - Optimización: reescribir consultas para que corran más rápido.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-01-graph.svg]]
>
> **Se lee así:** el diagrama es la **misma tabla `PRODUCTO` que se usa como ejemplo en toda la unidad**, con sus dos filas (`101 · Pasta · 3.50` y `104 · Gel · 4.00`) y sus tres columnas (`CODIGO`, `DESCRIPCION`, `PRECIO`). Desde esa tabla salen dos flechas: *"tiene"* hacia una **tupla** concreta — `(104, Gel, 4.00)` — y otra hacia un **atributo** concreto — `PRECIO`.
>
> **Por qué importa:** ese diagrama es la respuesta visual a *"¿por qué el álgebra relacional?"*. Cada operador de los que verás es una **operación sobre relaciones**, y una relación es exactamente esta caja de filas y columnas. Cuando el motor ejecuta tu `SELECT`, internamente está aplicando estos mismos operadores: por eso el álgebra relacional es el lenguaje en el que se razona sobre el costo de una consulta.
>
> **Ejemplo:** tu `SELECT * FROM PRODUCTO WHERE CODIGO = 104` es, en álgebra, `σ CODIGO = 104 (PRODUCTO)`. Y tu `SELECT DESCRIPCION FROM PRODUCTO` es `π DESCRIPCION (PRODUCTO)`. Todo el SQL de la Unidad 4 se puede escribir así; la diferencia es que el motor además sabe **optimizar** el plan.

---

## 📋 Definiciones Formales

### 1️⃣ Relación, tupla y atributo

> [!note] 📋 Definición — Vocabulario de tabla
>
> | Elemento | Definición | Ejemplo |
> |---|---|---|
> | Relación (tabla) | Intersección de filas y columnas | Tabla completa |
> | Tupla / fila | Una ocurrencia | Un estudiante concreto |
> | Atributo / columna | Una casilla | nombre, código |
>
> Ejemplo: la tabla es la relación; cada fila una tupla; cada columna un atributo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-01-graph.svg]]
>
> **Se lee así:** ahora el diagrama se lee como una **definición visual**: la caja grande es la **relación** (la tabla completa, con el nombre de sus columnas en la primera fila y sus valores debajo), la flecha *"tiene"* baja a la **tupla** (una fila completa: `104, Gel, 4.00` — los tres valores, no uno suelto), y la flecha sin etiqueta baja al **atributo** (una sola columna: `PRECIO`).
>
> **Por qué importa:** la diferencia entre tupla y atributo es la que genera la mitad de los errores de examen. **Una tupla es una fila completa**; un atributo es **una columna completa**. Cuando escribes `σ CÓDIGO = 104 (PRODUCTO)`, la condición `CÓDIGO = 104` se evalúa **tupla por tupla** y devuelve tuplas enteras; no devuelve el valor `104` suelto.
>
> **Ejemplo:** la tupla `(104, Gel, 4.00)` es la unidad de información que se mueve de tabla en tabla cuando aplicas un operador. Por eso el resultado de `σ` y de `π` **sigue siendo una relación**: si seleccionas, la tupla conserva sus tres valores; si proyectas, la tupla se recorta a las columnas que pediste.

### 2️⃣ Selección σ

> [!note] 📋 Definición — Selección σ
>
> La selección filtra filas (tuplas) que satisfacen una condición.
>
> Se representa con σ y la condición va entre paréntesis antes del nombre de la relación.
>
> Sintaxis: σ condición (relación)
>
> Resultado: una relación con las mismas columnas, pero solo las filas que cumplen la condición.
>
> Ejemplo: σ CÓDIGO = 104 (PRODUCTO)
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-02-graph.svg]]
>
> **Se lee así:** el diagrama muestra la **selección como un filtro de filas**: la tabla `PRODUCTO` completa (cuatro filas) entra por la izquierda y sale por la derecha una tabla con **una sola fila**, `104 · Gel · 4.00`. La flecha lleva el rótulo `σ CÓDIGO = 104`, que es literalmente la operación. Fíjate en que la salida conserva **las tres columnas**: la selección quita filas, nunca columnas.
>
> **Por qué importa:** esa es la propiedad que distingue `σ` de `π` y la que se pregunta en examen: **`σ` cambia el número de filas, `π` cambia el número de columnas**. Y las dos propiedades juntas explican por qué la salida de `σ` **sigue siendo una relación**: mismo nombre de columnas, mismos dominios, sin filas repetidas.
>
> **Ejemplo:** si el filtro fuera `PRECIO > 4`, la salida serían las filas `102`, `103` y `104` — tres filas, tres columnas. Cambiar de filtro cambia cuántas filas salen, nunca cuáles columnas.

> [!example] 🧪 Ejemplo de selección
>
> | CODIGO | DESCRIPCION | PRECIO |
> |---|---|---|
> | 101 | Pasta | 3.50 |
> | 102 | Cepillo | 4.50 |
> | 103 | Papel higiénico | 7.00 |
> | 104 | Gel | 4.00 |
>
> σ CÓDIGO = 104 (PRODUCTO) devuelve:
>
> | CODIGO | DESCRIPCION | PRECIO |
> |---|---|---|
> | 104 | Gel | 4.00 |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-02-graph.svg]]
>
> **Se lee así:** el diagrama repite el ejemplo numérico de la tabla de arriba: de cuatro productos (`Pasta`, `Cepillo`, `Papel higiénico`, `Gel`) solo sobrevive el **`104 · Gel · 4.00`**. La flecha rotulada `σ CÓDIGO = 104` es el filtro, y la caja de la derecha es **la tabla resultado**, no un valor suelto.
>
> **Por qué importa:** la lectura que hay que hacer aquí es la de **subconjunto**: el resultado de una selección es un *subconjunto* de las filas de la tabla original. Eso significa que el resultado **hereda la clave primaria** y que toda regla de negocio que aplicaba a `PRODUCTO` sigue valiendo para el resultado. La selección no crea datos nuevos.
>
> **Ejemplo:** si `PRODUCTO` exige que `CODIGO` sea único, el resultado `σ CODIGO = 104 (PRODUCTO)` también lo cumple. Por eso puedes seguir usando `π CODIGO` sobre él sin miedo a duplicados: la clave ya venía garantizada.

### 3️⃣ Proyección π

> [!note] 📋 Definición — Proyección π
>
> La proyección elige columnas y elimina duplicadas.
>
> Se representa con π y las columnas van listadas después del símbolo.
>
> Resultado: una relación con solo las columnas solicitadas, sin filas duplicadas.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-03-graph.svg]]
>
> **Se lee así:** la flecha va de la tabla `PRODUCTO` (dos filas, tres columnas) a una caja de resultado que tiene **una sola columna, `DESCRIPCION`**, con dos valores (`Pasta` y `Gel`). El rótulo `π DESCRIPCION` dice la operación: *qué columna(s) te quiero*.
>
> **Por qué importa:** fíjate en que el resultado **ya no tiene las otras dos columnas**. Ese es el cambio de dimensión: `π` pasa de "muchas filas y muchas columnas" a "pocas filas y pocas columnas". Y el detalle fino: **π elimina duplicados**. Es una operación de conjuntos, no un simple recorte de columnas.
>
> **Ejemplo:** si `PRODUCTO` tuviera dos filas con la misma descripción (`Pasta` de la marca A y `Pasta` de la marca B), `π DESCRIPCION` devolvería **una sola** fila `Pasta`. Por eso en SQL la proyección casi siempre lleva `DISTINCT`: `SELECT DISTINCT DESCRIPCION FROM PRODUCTO`.

> [!example] 🧪 Ejemplo de proyección
>
> | CODIGO | DESCRIPCION | PRECIO |
> |---|---|---|
> | 101 | Pasta | 3.50 |
> | 104 | Gel | 4.00 |
>
> π DESCRIPCION (σ CÓDIGO = 104 (PRODUCTO)) devuelve:
>
> | DESCRIPCION |
> |---|
> | Gel |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-03-graph.svg]]
>
> **Se lee así:** el diagrama es el **operador completo**, no solo la proyección: la flecha va de `PRODUCTO` a un resultado con **una columna** (`Gel`), y el rótulo `π DESCRIPCION` dice que se проекó. En la tabla de arriba, la operación completa era `π DESCRIPCION (σ CÓDIGO = 104 (PRODUCTO))`: primero se filtra (queda `104 · Gel · 4.00`), después se recorta a la columna `DESCRIPCION`.
>
> **Por qué importa:** el **orden de las operaciones no es indiferente**. Si proyectaras primero (`π DESCRIPCION (PRODUCTO)`) y luego filtraras (`σ CÓDIGO = 104`), la proyección **ya habría tirado la columna `CODIGO`** y el filtro sería imposible de escribir. En álgebra relacional esto no es un detalle: el orden es parte de la expresión.
>
> **Ejemplo:** en SQL esto no es un problema porque el `WHERE` se aplica antes que el `SELECT`. En álgebra, `σ CODIGO = 104 (π DESCRIPCION (PRODUCTO))` es **una expresión mal formada**, no una expresión equivalente: `CODIGO` ya no existe en el resultado intermedio.

### 4️⃣ Producto Cruz ×

> [!note] 📋 Definición — Producto Cruz ×
>
> El producto cruz genera todas las combinaciones posibles de filas entre dos relaciones.
>
> Si la tabla A tiene m filas y la tabla B tiene n filas, el resultado tiene m×n filas.
>
> Sintaxis: relaciónA × relaciónB
>
> Resultado: una relación con todas las columnas de A y todas las columnas de B, y m×n filas.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-04-graph.svg]]
>
> **Se lee así:** el diagrama dibuja el producto cruz como **dos tablas que entran y una que sale**. Arriba, `PRODUCTO` con 3 filas; abajo, `VENTA` con 3 filas; y en el medio la caja del resultado: *"3 × 3 = 9 filas (todas las combinaciones)"*. Las dos flechas llevan el símbolo `×`.
>
> **Por qué importa:** el resultado tiene **todas las columnas de A y todas las de B**, y **m×n filas**. El dato importante es que el motor **no filtra nada**: combina cada fila de `PRODUCTO` con cada fila de `VENTA`,( las combinaciones absurdas como un champú con una venta de otra fecha). Por eso el producto cruz es la operación más cara y casi nunca la que quieres.
>
> **Ejemplo:** con 3 productos y 3 ventas salen 9 filas, de las cuales solo **3** tienen sentido (las que comparten `ID_PRODUCT`). Las otras 6 son ruido. Por eso el `JOIN` no es "otra cosa": es el producto cruz **filtrado**.

> [!example] 🧪 Ejemplo de producto cruz
>
> | CODIGO | DESCRIPCION | PRECIO |
> |---|---|---|
> | 101 | Pasta | 3.50 |
> | 104 | Gel | 4.00 |
> | 105 | Shampoo | 10.00 |
>
> | ID_VENTA | FECHA | ID_PRODUCT | CANTIDAD |
> |---|---|---|---|
> | 1 | 02/02/2020 | 104 | 54 |
> | 2 | 04/02/2020 | 101 | 2 |
> | 4 | 04/04/2020 | 110 | -2 |
>
> PRODUCTO × VENTA produce 9 filas (3 × 3): toda combinación. Casi nunca es lo que quieres, es el punto de partida de los joins.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-04-graph.svg]]
>
> **Se lee así:** el diagrama muestra las dos tablas concretas del ejemplo — `PRODUCTO` (101 Pasta, 104 Gel, 105 Shampoo) y `VENTA` (tres ventas con su fecha, su producto y su cantidad) — y avisa en el resultado: *"3 × 3 = 9 filas (todas las combinaciones)"*. Fíjate en que la tercera venta es `4 · 04/04/2020 · 110 · -2`: habla de un producto `110` que **no está** en `PRODUCTO` y tiene cantidad **negativa**. Es una venta de devolución, y no se combina con ningún producto.
>
> **Por qué importa:** ese detalle es la razón por la que el producto cruz no solo es caro: además es **incorrecto** por defecto. Las 9 filas incluyen combinaciones que no existen en la realidad (un champú con una venta de mayo) y además repiten datos. El `JOIN` resuelve las dos cosas de un golpe: une **solo** las filas que emparejan por la clave y de paso elimina las combinaciones inventadas.
>
> **Ejemplo:** el `JOIN` sobre `PRODUCTO.CODIGO = VENTA.ID_PRODUCT` deja 3 filas (101↔2, 104↔1, 105↔sin venta con `LEFT JOIN`). La venta del producto `110` **desaparece** con un `INNER JOIN`, porque no hay producto con ese código: el `JOIN` interno también es un filtro de integridad referencial.

> [!warning] ⚠️ Cuidado con el producto cruz
>
> El producto cruz genera muchas filas innecesarias.
>
> Siempre se usa como paso intermedio de un join, nunca como resultado final de una consulta útil.

### 5️⃣ Operadores de Conjuntos — ∪, −, ∩

> [!note] 📋 Definición — Operadores de conjuntos
>
> Operan sobre conjuntos completos de filas.
>
> Requieren que ambas relaciones tengan el mismo esquema (mismas columnas, mismos tipos).
>
> | Operador | Símbolo | Qué hace | SQL mental |
> |---|---|---|---|
> | Unión | ∪ | Todas las filas de A y de B, sin duplicados | UNION |
> | Diferencia | − | Filas de A que NO están en B | NOT IN / NOT EXISTS |
> | Intersección | ∩ | Filas que están tanto en A como en B | INTERSECT |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-05-graph.svg]]
>
> **Se lee así:** el diagrama es la **unión** como operación de conjuntos: `A = {a1, a2, a3}` y `B = {b1, b2, b3}` entran por dos flechas (rotuladas `∪`) y salen en una sola caja `A ∪ B`. La diferencia con las otras dos es que **los conjuntos no tienen por qué parecerse**: la unión suma todo lo que hay en cada uno.
>
> **Por qué importa:** la unión es la única de las tres que **no exige el mismo esquema**. `∪` une filas de relaciones distintas; `−` e `∩` exigen que ambas tengan exactamente las mismas columnas y los mismos dominios. Esa diferencia es la que hace que `UNION` en SQL sea la operación con la que se juntan tablas de origen distinto (por ejemplo, el histórico con el actual).
>
> **Ejemplo:** `SELECT DESCRIPCION FROM PRODUCTO UNION SELECT DESCRIPCION FROM PRODUCTO_ARCHIVADO` te da el catálogo completo, sin repetir los productos que están en las dos tablas. Fíjate en que `UNION` (no `UNION ALL`) **elimina los duplicados**: es el comportamiento de conjunto puro.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-06-graph.svg]]
>
> **Se lee así:** el diagrama es la **diferencia** con el ejemplo real de la nota. `AEROLINEA = {Avianca, Latam, Copa}` y `VUELO` (filtrado por `hora_salida = HOY`) `= {Avianca, Latam}` entran por dos flechas rotuladas `−`, y salen `A − B = {Copa}`. Abajo, una caja que lo traduce a palabras: *"Copa está en AEROLINEA pero no en VUELO de hoy"*.
>
> **Por qué importa:** la diferencia es **direccional**: `A − B` y `B − A` no son lo mismo. `A − B` responde *"qué hay en A que no está en B"*; `B − A` respondería *"qué vuelos de hoy son de aerolíneas que ya no operamos"*. Es la diferencia entre `NOT IN` y `NOT EXISTS` con la dirección cambiada.
>
> **Ejemplo:** la consulta de la nota (`Π nombre(AEROLINEA) − Π nombre(AEROLINEA ⨝ σ hora_salida=HOY(VUELO))`) tiene **tres operadores encadenados** y dos pasos: primero se projectiona el nombre de cadaهارlinea, después se quitan los que vuelan hoy. El diagrama muestra el paso final ya hecho: de tres, queda `Copa`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-07-graph.svg]]
>
> **Se lee así:** el diagrama muestra la **intersección** como el caso donde los conjuntos **sí se parecen**: `A = {a1, a2, a3}` y `B = {a2, a3, b3}` entran por dos flechas rotuladas `∩` y sale `A ∩ B = {a2, a3}`. Fíjate en la diferencia con la unión: aquí el resultado **solo contiene elementos que están en los dos**, y el elemento `b3` (que está solo en B) se queda fuera.
>
> **Por qué importa:** la intersección es la operación que **exige esquemas idénticos**: para comparar fila por fila, las dos relaciones tienen que tener las mismas columnas en el mismo orden y los mismos dominios. Por eso `INTERSECT` en SQL es la que más falla si las columnas no coinciden en tipo.
>
> **Ejemplo:** `SELECT DESCRIPCION FROM PRODUCTO INTERSECT SELECT DESCRIPCION FROM PRODUCTO_ACTIVO` devuelve las descripciones que están **en las dos tablas**. A diferencia de la unión, aquí el resultado **no puede** ser más grande que ninguna de las dos entradas: la intersección siempre es el conjunto más pequeño.

> [!example] 🧪 Ejemplo de diferencia
>
> Listar las aerolíneas que no tienen vuelos para hoy:
>
> ```
> 'Π nombre(AEROLINEA) − Π nombre(AEROLINEA ⨝ σ hora_salida=HOY(VUELO))'
> ```
>
> La diferencia es la negación: trae las aerolíneas ausentes en el conjunto de vuelos de hoy.
>
> ```mermaid
> erDiagram
>     AEROLINEA ||--o{ VUELO : opera
>     AEROLINEA {
>         string nombre PK
>         string pais
>     }
>     VUELO {
>         string numero_vuelo PK
>         string aerolinea_nombre FK
>         datetime hora_salida
>         string destino
>     }
> ```

---

## 🎯 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Selección y proyección encadenadas

> [!example] 📋 Planteamiento
>
> Dada la tabla ESTUDIANTE(carnet, nombre, carrera, promedio), escribe en álgebra relacional: obtener los nombres de los estudiantes de Sistemas con promedio mayor a 8.5.
>
> > [!success]- ✅ Solución
> >
> > π nombre (σ carrera='Sistemas' ∧ promedio>8.5 (ESTUDIANTE))
> >
> > **Por qué:** primero filtramos las filas que cumplen ambas condiciones (σ), luego elegimos solo la columna nombre (π).

### ✏️ Ejercicio 2 — Producto cruz seguido de selección

> [!example] 📋 Planteamiento
>
> Dadas CLIENTE(id, nombre) y PEDIDO(id, cliente_id, fecha), escribe en álgebra relacional: obtener nombre del cliente y fecha de cada pedido.
>
> > [!success]- ✅ Solución
> >
> > π CLIENTE.nombre, PEDIDO.fecha (σ CLIENTE.id = PEDIDO.cliente_id (CLIENTE × PEDIDO))
> >
> > **Por qué:** el producto cruz combina todo con todo, luego la selección filtra solo las combinaciones donde el cliente coincide, y la proyección elige las columnas que interesan.

### ✏️ Ejercicio 3 — Unión y diferencia

> [!example] 📋 Planteamiento
>
> Dadas MATERIAS_1ER_SEMESTRE(codigo, nombre) y MATERIAS_2DO_SEMESTRE(codigo, nombre), escribe en álgebra relacional: listar todas las materias que se dan en el año, sin repetir las que se dan en ambos semestres.
>
> > [!success]- ✅ Solución
> >
> > MATERIAS_1ER_SEMESTRE ∪ MATERIAS_2DO_SEMESTRE
> >
> > **Por qué:** la unión combina todas las filas de ambas tablas y elimina duplicados automáticamente.

### ✏️ Ejercicio 4 — Diferencia para exclusiones

> [!example] 📋 Planteamiento
>
> Dadas ESTUDIANTE(carnet, nombre) y MATRICULA(carnet, cod_materia), escribe en álgebra relacional: obtener nombres de estudiantes que NO se han matriculado en ninguna materia.
>
> > [!success]- ✅ Solución
> >
> > π nombre (ESTUDIANTE) − π nombre (ESTUDIANTE ⨝ MATRICULA)
> >
> > **Por qué:** la primera parte trae todos los estudiantes; la segunda, los que sí están matriculados; la diferencia da los que no están en ninguna.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino selección, proyección y producto cruz sin mirar.
> - [ ] Explico la diferencia entre σ (filtra filas) y π (elige columnas).
> - [ ] Aplico ∪, −, ∩ sobre dos tablas con el mismo esquema.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Encadeno σ y π en una misma expresión.
> - [ ] Detecto cuándo un producto cruz es innecesario y debo usar un join.
> - [ ] Escribo la equivalencia SQL mental de cada operador.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Dibujo el diagrama de ejecución (pasos numerados) de una expresión álgebraica.
> - [ ] Detecto consultas que se pueden reescribir para ser más eficientes.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - Diapositivas de clase: `3.1 Operaciones básicas del álgebra relacional` (σ, π, ×) y `3.2 Operaciones derivadas` (joins, división).
> - Guía: [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — 4 ejercicios resueltos de álgebra.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 3 — el álgebra relacional como base de SQL.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿σ (selección)?::Filtra filas que cumplen una condición → WHERE.
> - ¿π (proyección)?::Elige columnas y elimina duplicados → SELECT / DISTINCT.
> - × (producto cruz)?::Todas las combinaciones de filas (m × n) → FROM sin JOIN.
> - ∪ (unión)?::Filas de ambas tablas sin duplicados → UNION.
> - − (diferencia)?::Filas de A que no están en B → NOT IN / NOT EXISTS.
> - ∩ (intersección)?::Filas que están en ambas → INTERSECT.
> - ¿Por qué filtrar antes de proyectar?::Menos columnas que cargar, más eficiente.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[02 - Operadores Derivados y Joins]] — los operadores que se construyen sobre los básicos.
> - [[03 - Renombre y Agregación]] — renombre, agrupación y ordenamiento.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — 4 ejercicios resueltos de álgebra relacional.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[02 - Operadores Derivados y Joins]]
> - Guía de ejercicios: [[Guía de Problemas 2 - Álgebra Relacional y Normalización]]

---

**Tags:** #TICG1018 #unidad3 #algebra-relacional #operadores-basicos #bd