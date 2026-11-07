---
dg-publish: true
tags: [TICG1018, unidad3, algebra-relacional, operadores-basicos, bd]
---

# 🧮 Álgebra Relacional — Operadores Básicos

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Álgebra Relacional?
> SQL esconde las operaciones matemáticas que hacen posible cada consulta. Entender el álgebra relacional es lo que separa escribir consultas que "funcionan" de escribir consultas que se ejecutan de forma eficiente. Es el lenguaje formal que subyace a todo motor de bases de datos relacionales.
>
> **Aplicaciones:**
> - Diseño de consultas: entender qué hace cada cláusula SQL bajo el capó.
> - Optimización: reescribir consultas para que corran más rápido.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-01-graph.svg]]

---

## 📋 Definiciones Formales

### 1️⃣ Relación, tupla y atributo

> [!note] 📋 Definición — Vocabulario de tabla
> | Elemento | Definición | Ejemplo |
> |---|---|---|
> | Relación (tabla) | Intersección de filas y columnas | Tabla completa |
> | Tupla / fila | Una ocurrencia | Un estudiante concreto |
> | Atributo / columna | Una casilla | nombre, código |
>
> Ejemplo: la tabla es la relación; cada fila una tupla; cada columna un atributo.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-01-graph.svg]]

### 2️⃣ Selección σ

> [!note] 📋 Definición — Selección σ
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
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-02-graph.svg]]

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
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-02-graph.svg]]

### 3️⃣ Proyección π

> [!note] 📋 Definición — Proyección π
> La proyección elige columnas y elimina duplicadas.
>
> Se representa con π y las columnas van listadas después del símbolo.
>
> Resultado: una relación con solo las columnas solicitadas, sin filas duplicadas.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-03-graph.svg]]

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
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-03-graph.svg]]

### 4️⃣ Producto Cruz ×

> [!note] 📋 Definición — Producto Cruz ×
> El producto cruz genera todas las combinaciones posibles de filas entre dos relaciones.
>
> Si la tabla A tiene m filas y la tabla B tiene n filas, el resultado tiene m×n filas.
>
> Sintaxis: relaciónA × relaciónB
>
> Resultado: una relación con todas las columnas de A y todas las columnas de B, y m×n filas.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-04-graph.svg]]

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
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-04-graph.svg]]

> [!warning] ⚠️ Cuidado con el producto cruz
> El producto cruz genera muchas filas innecesarias.
>
> Siempre se usa como paso intermedio de un join, nunca como resultado final de una consulta útil.

### 5️⃣ Operadores de Conjuntos — ∪, −, ∩

> [!note] 📋 Definición — Operadores de conjuntos
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
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-05-graph.svg]]
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-06-graph.svg]]
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-07-graph.svg]]

> [!example] 🧪 Ejemplo de diferencia
> Listar las aerolíneas que no tienen vuelos para hoy:
>
> Π nombre(AEROLINEA) − Π nombre(AEROLINEA ⨝ σ hora_salida=HOY(VUELO))
>
> La diferencia es la negación: trae las aerolíneas ausentes en el conjunto de vuelos de hoy.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/u3-01-06-graph.svg]]

---

## 🎯 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Selección y proyección encadenadas

> [!example] 📋 Planteamiento
> Dada la tabla ESTUDIANTE(carnet, nombre, carrera, promedio), escribe en álgebra relacional: obtener los nombres de los estudiantes de Sistemas con promedio mayor a 8.5.
>
> > [!success]- ✅ Solución
> > π nombre (σ carrera='Sistemas' ∧ promedio>8.5 (ESTUDIANTE))
> >
> > **Por qué:** primero filtramos las filas que cumplen ambas condiciones (σ), luego elegimos solo la columna nombre (π).

### ✏️ Ejercicio 2 — Producto cruz seguido de selección

> [!example] 📋 Planteamiento
> Dadas CLIENTE(id, nombre) y PEDIDO(id, cliente_id, fecha), escribe en álgebra relacional: obtener nombre del cliente y fecha de cada pedido.
>
> > [!success]- ✅ Solución
> > π CLIENTE.nombre, PEDIDO.fecha (σ CLIENTE.id = PEDIDO.cliente_id (CLIENTE × PEDIDO))
> >
> > **Por qué:** el producto cruz combina todo con todo, luego la selección filtra solo las combinaciones donde el cliente coincide, y la proyección elige las columnas que interesan.

### ✏️ Ejercicio 3 — Unión y diferencia

> [!example] 📋 Planteamiento
> Dadas MATERIAS_1ER_SEMESTRE(codigo, nombre) y MATERIAS_2DO_SEMESTRE(codigo, nombre), escribe en álgebra relacional: listar todas las materias que se dan en el año, sin repetir las que se dan en ambos semestres.
>
> > [!success]- ✅ Solución
> > MATERIAS_1ER_SEMESTRE ∪ MATERIAS_2DO_SEMESTRE
> >
> > **Por qué:** la unión combina todas las filas de ambas tablas y elimina duplicados automáticamente.

### ✏️ Ejercicio 4 — Diferencia para exclusiones

> [!example] 📋 Planteamiento
> Dadas ESTUDIANTE(carnet, nombre) y MATRICULA(carnet, cod_materia), escribe en álgebra relacional: obtener nombres de estudiantes que NO se han matriculado en ninguna materia.
>
> > [!success]- ✅ Solución
> > π nombre (ESTUDIANTE) − π nombre (ESTUDIANTE ⨝ MATRICULA)
> >
> > **Por qué:** la primera parte trae todos los estudiantes; la segunda, los que sí están matriculados; la diferencia da los que no están en ninguna.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
> Defino selección, proyección y producto cruz sin mirar.
>
> Explico la diferencia entre σ (filtra filas) y π (elige columnas).
>
> Aplico ∪, −, ∩ sobre dos tablas con el mismo esquema.

> [!note] 📋 Nivel Intermedio
> Encadeno σ y π en una misma expresión.
>
> Detecto cuándo un producto cruz es innecesario y debo usar un join.
>
> Escribo la equivalencia SQL mental de cada operador.

> [!note] 📋 Nivel Avanzado
> Dibujo el diagrama de ejecución (pasos numerados) de una expresión álgebraica.
>
> Detecto consultas que se pueden reescribir para ser más eficientes.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
> ¿σ (selección)?::Filtra filas que cumplen una condición → WHERE.
>
> ¿π (proyección)?::Elige columnas y elimina duplicados → SELECT / DISTINCT.
>
> × (producto cruz)?::Todas las combinaciones de filas (m × n) → FROM sin JOIN.
>
> ∪ (unión)?::Filas de ambas tablas sin duplicados → UNION.
>
> − (diferencia)?::Filas de A que no están en B → NOT IN / NOT EXISTS.
>
> ∩ (intersección)?::Filas que están en ambas → INTERSECT.
>
> ¿Por qué filtrar antes de proyectar?::Menos columnas que cargar, más eficiente.

> [!note] 🧠 Repasa con el plugin Spaced Repetition (Lección 1: 13-oct)

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
> - [[02 - Operadores Derivados y Joins]] — los operadores que se construyen sobre los básicos.
> - [[03 - Renombre y Agregación]] — renombre, agrupación y ordenamiento.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — 4 ejercicios resueltos de álgebra relacional.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[02 - Operadores Derivados y Joins]]
> - Guía de ejercicios: [[Guía de Problemas 2 - Álgebra Relacional y Normalización]]

---

**Tags:** #TICG1018 #unidad3 #algebra-relacional #operadores-basicos #bd
