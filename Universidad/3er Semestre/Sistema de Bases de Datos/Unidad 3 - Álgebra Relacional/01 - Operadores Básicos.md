---
dg-publish: true
tags: [TICG1018, unidad3, algebra-relacional, operadores-basicos, bd]
---

# 🧮 Álgebra Relacional — Operadores Básicos

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Álgebra Relacional?
>
> SQL esconde las operaciones matemáticas que hacen posible cada consulta. Entender el álgebra relacional es lo que separa escribir consultas que "funcionan" de escribir consultas que **se ejecutan de forma eficiente**. Es el lenguaje formal que subyace a todo motor de bases de datos relacionales.
>
> **Aplicaciones:**
> - **Diseño de consultas:** entender qué hace cada cláusula SQL bajo el capó.
> - **Optimización:** reescribir consultas para que corran más rápido.
> - **Lección 1 (13-oct):** operadores básicos σ, π, × y los de conjuntos ∪, −, ∩.

> [!note] ℹ️ Qué es el álgebra relacional
>
> Un lenguaje formal para expresar operaciones entre relaciones o tablas. Sus operaciones son **cerradas**: el resultado de aplicar cualquier operador es siempre otra relación, lo que permite anidar expresiones (el resultado de una operación se usa como entrada de la siguiente).

> [!example] 🧪 Operadores relacionales — resumen
>
> | Grupo | Operadores | Símbolo | Qué hace |
> |---|---|---|---|
> | Básicos | Selección, Proyección, Producto Cruz | σ, π, × | Filtra filas, elige columnas, combina todo con todo |
> | Derivados | Join (natural, equi, theta, outer) | ⨝, ⟕, ⟖ | Combina tablas por condición |
> | Conjuntos | Unión, Diferencia, Intersección | ∪, −, ∩ | Operaciones entre conjuntos completos |
> | Agregación | Agrupación | γ | Agrupa y calcula (COUNT, SUM, AVG) |
> | Otros | Renombre, Asignación | ρ, τ | Alias, ordenamiento |

> [!example] 📎 Diapositivas de referencia
>
> ![[../Unidad 0 - Guias y Ejercicios/Diapositivas/3.1 Operaciones Básicas_2025.pdf]]
> ![[../Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides5_1_TICG1018.pdf]]

---

## 📋 Definiciones Formales

### 1️⃣ Relación, tupla y atributo

> [!note] 📋 Definición — Vocabulario de tabla
>
> - **Relación (tabla):** intersección de filas y columnas.
> - **Tupla/fila:** una ocurrencia (un estudiante concreto).
> - **Atributo/columna:** una casilla (nombre, código).
>
> **Ejemplo:** la tabla es la relación; cada fila una tupla (`0876, Jorge`); cada columna un atributo (`nombre`).

> [!info] 📖 El deck de cátedra: seleccion, proyeccion y producto (slides05, pp. 3-9)
>
> El deck del Ing. Magallanes recorre los operadores básicos con ejemplos numéricos y tablas reales.

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-01-graph.svg]]

> **Selección (p. 5):** selecciona las filas (tuplas) que satisfacen una condición de selección. Se representa con el símbolo σ.
>
> Ejemplo: obtener el producto cuyo código es el 104:
>
> `σ CÓDIGO = 104 (PRODUCTO)`

![[Archivos/bd-s05-p5.png]]

> **Proyección y composición (p. 7):** `π maker, type (σ type='laptop' ∧ model≥2005 (Product))` — el deck dibuja el diagrama de ejecución con los pasos numerados (3 → 2 → 1) y el resultado. Es la mejor explicación de por qué se proyecta *después* de filtrar.

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-02-graph.svg]]

> **Producto cartesiano (p. 9):** el ejemplo `Department ⨯ Course` muestra por qué el producto casi nunca es lo que quieres — de ahí la necesidad del join.

![[Archivos/bd-s05-p9.png]]
![[Archivos/bd-s05-p15.png]]

---

## 🛠️ Operador σ — Selección

> [!note] 📋 Definición — Selección σ
>
> La selección **filtra filas** (tuplas) que satisfacen una condición. Se representa con σ y la condición va entre paréntesis antes del nombre de la relación.
>
> **Sintaxis:** `σ condición (relación)`
>
> **Resultado:** una relación con las mismas columnas, pero solo las filas que cumplen la condición.

> [!example] 🧪 Ejemplo de selección
>
> | CODIGO | DESCRIPCION | PRECIO |
> |---|---|---|
> | 101 | Pasta | 3.50 |
> | 102 | Cepillo | 4.50 |
> | 103 | Papel higiénico | 7.00 |
> | 104 | Gel | 4.00 |
>
> `σ CÓDIGO = 104 (PRODUCTO)` devuelve:
>
> | CODIGO | DESCRIPCION | PRECIO |
> |---|---|---|
> | 104 | Gel | 4.00 |

> [!info] 🔗 Reglas de composición
>
> La condición puede ser uno o varios términos unidos con operadores lógicos (`and`, `∧`, `or`, `∨`):
>
> `σ type='laptop' ∧ model≥2005 (Product)`

---

## 🛠️ Operador π — Proyección

> [!note] 📋 Definición — Proyección π
>
> La proyección **elige columnas** y elimina duplicadas. Se representa con π y las columnas van listadas después del símbolo.
>
> **Sintaxis:** `π columnas (relación)`
>
> **Resultado:** una relación con solo las columnas solicitadas, sin filas duplicadas.

> [!example] 🧪 Ejemplo de proyección
>
> | CODIGO | DESCRIPCION | PRECIO |
> |---|---|---|
> | 101 | Pasta | 3.50 |
> | 104 | Gel | 4.00 |
>
> `π DESCRIPCION (σ CÓDIGO = 104 (PRODUCTO))` devuelve:
>
> | DESCRIPCION |
> |---|
> | Gel |

> [!tip] 💡 Orden de operaciones
>
> Siempre se **filtra primero (σ)** y se **proyecta después (π)**. Proyectar antes de filtrar es posible pero menos eficiente: el motor tendría que cargar más columnas de las necesarias.

---

## 🛠️ Operador × — Producto Cruz

> [!note] 📋 Definición — Producto Cruz ×
>
> El producto cruz genera **todas las combinaciones posibles** de filas entre dos relaciones. Si la tabla A tiene m filas y la tabla B tiene n filas, el resultado tiene m×n filas.
>
> **Sintaxis:** `relaciónA × relaciónB`
>
> **Resultado:** una relación con todas las columnas de A y todas las columnas de B, y m×n filas.

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
> `PRODUCTO × VENTA` produce 9 filas (3 × 3): toda combinación. Casi nunca es lo que quieres, es el punto de partida de los joins.

> [!warning] ⚠️ Cuidado con el producto cruz
>
> El producto cruz genera muchas filas innecesarias. Siempre se usa como paso intermedio de un join, nunca como resultado final de una consulta útil.

---

## 🛠️ Operadores de Conjuntos — ∪, −, ∩

> [!note] 📋 Definición — Operadores de conjuntos
>
> Operan sobre **conjuntos completos de filas**. Requieren que ambas relaciones tengan el mismo esquema (mismas columnas, mismos tipos).
>
> | Operador | Símbolo | Qué hace | SQL mental |
> |---|---|---|---|
> | Unión | `∪` | Todas las filas de A y de B, sin duplicados | `UNION` |
> | Diferencia | `−` | Filas de A que NO están en B | `NOT IN / NOT EXISTS` |
> | Intersección | `∩` | Filas que están tanto en A como en B | `INTERSECT` |

> [!example] 🧪 Ejemplo de diferencia
>
> Listar las aerolíneas que no tienen vuelos para hoy:
>
> `Π nombre(AEROLINEA) − Π nombre(AEROLINEA ⨝ σ hora_salida=HOY(VUELO))`
>
> La diferencia es la negación: trae las aerolíneas ausentes en el conjunto de vuelos de hoy.

---

## 🎯 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Selección y proyección encadenadas

> [!example] 📋 Planteamiento
>
> Dada la tabla `ESTUDIANTE(carnet, nombre, carrera, promedio)`, escribe en álgebra relacional: "obtener los nombres de los estudiantes de Sistemas con promedio mayor a 8.5".
>
> > [!success]- ✅ Solución
> >
> > `π nombre (σ carrera='Sistemas' ∧ promedio>8.5 (ESTUDIANTE))`
> >
> > **Por qué:** primero filtramos las filas que cumplen ambas condiciones (σ), luego elegimos solo la columna nombre (π).

### ✏️ Ejercicio 2 — Producto cruz seguido de selección

> [!example] 📋 Planteamiento
>
> Dadas `CLIENTE(id, nombre)` y `PEDIDO(id, cliente_id, fecha)`, escribe en álgebra relacional: "obtener nombre del cliente y fecha de cada pedido".
>
> > [!success]- ✅ Solución
> >
> > `π CLIENTE.nombre, PEDIDO.fecha (σ CLIENTE.id = PEDIDO.cliente_id (CLIENTE × PEDIDO))`
> >
> > **Por qué:** el producto cruz combina todo con todo, luego la selección filtra solo las combinaciones donde el cliente coincide, y la proyección elige las columnas que interesan.

### ✏️ Ejercicio 3 — Unión y diferencia

> [!example] 📋 Planteamiento
>
> Dadas `MATERIAS_1ER_SEMESTRE(codigo, nombre)` y `MATERIAS_2DO_SEMESTRE(codigo, nombre)`, escribe en álgebra relacional: "listar todas las materias que se dan en el año, sin repetir las que se dan en ambos semestres".
>
> > [!success]- ✅ Solución
> >
> > `MATERIAS_1ER_SEMESTRE ∪ MATERIAS_2DO_SEMESTRE`
> >
> > **Por qué:** la unión combina todas las filas de ambas tablas y elimina duplicados automáticamente.

### ✏️ Ejercicio 4 — Diferencia para exclusiones

> [!example] 📋 Planteamiento
>
> Dadas `ESTUDIANTE(carnet, nombre)` y `MATRICULA(carnet, cod_materia)`, escribe en álgebra relacional: "obtener nombres de estudiantes que NO se han matriculado en ninguna materia".
>
> > [!success]- ✅ Solución
> >
> > `π nombre (ESTUDIANTE) − π nombre (ESTUDIANTE ⨝ MATRICULA)`
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

> [!note] 🧠 Repasa con el plugin Spaced Repetition (Lección 1: 13-oct)

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
