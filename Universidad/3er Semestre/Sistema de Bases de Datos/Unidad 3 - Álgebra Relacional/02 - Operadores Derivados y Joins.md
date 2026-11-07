---
dg-publish: true
tags: [TICG1018, unidad3, algebra-relacional, joins, derivados, bd]
---

# 🔗 Álgebra Relacional — Operadores Derivados y Joins

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Joins y no solo Producto Cruz?
> El producto cruz × genera todas las combinaciones (m × n filas), casi nunca lo que quieres. Los joins son derivados del producto cruz + selección + proyección que combinan tablas de forma inteligente: solo las filas que "encajan" por una condición.
> **Aplicaciones:**
> - Consultas reales: casi toda consulta SQL usa al menos un join.
> - Optimización: elegir el join correcto cambia si la consulta corre en milisegundos o en segundos.
> - Lección 1 (13-oct): natural join, equi join, theta join, left/right outer join.

> [!example] 📎 Diapositivas de referencia
> ![[../../Unidad 0 - Guias y Ejercicios/Diapositivas/3.2 Operaciones Derivadas-join-order2026.pdf]]
> ![[../../Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides5_1_TICG1018.pdf]]

---

## 📋 Definiciones Formales

### 1️⃣ Join Natural ⨝

> [!note] 📋 Definición — Join Natural ⨝
> El join natural combina dos relaciones sobre atributos con el mismo nombre y mismo valor, y luego elimina las columnas repetidas.
> Sintaxis: relaciónA ⨝ relaciónB
> Base matemática: σ F (A × B) donde F es el predicado de igualdad en atributos comunes, seguido de π que borra la columna duplicada.
> ```mermaid
graph TD
    A[Tabla A] -->|⨝| B[Resultado]
    C[Tabla B] -->|⨝| B
    style A fill:#e1f5fe
    style C fill:#e1f5fe
    style B fill:#c8e6c9
```

> [!example] 🧪 Ejemplo de join natural
> | PRODUCTO |
> |---|
> | CODIGO | DESCRIPCION | PRECIO |
> | 101 | Pasta | 3.50 |
> | 104 | Gel | 4.00 |
> | 105 | Shampoo | 10.00 |
>
> | VENTA |
> |---|
> | ID_VENTA | FECHA | ID_PRODUCT | CANTIDAD |
> | 1 | 02/02/2020 | 104 | 54 |
> | 2 | 04/02/2020 | 101 | 2 |
> | 4 | 04/04/2020 | 110 | -2 |
>
> PRODUCTO ⨝ VENTA no tiene columnas de mismo nombre → producto cruz puro (9 filas).
> Si renombráramos ID_PRODUCT a CODIGO, el join natural haría σ PRODUCTO.CODIGO = VENTA.CODIGO (PRODUCTO × VENTA) y eliminaría la CODIGO duplicada, dejando 2 filas: 101↔venta 2, 104↔venta 1.

> [!example] 📎 Diapositiva de referencia

---

### 2️⃣ Equi Join ⨝(a=b)

> [!note] 📋 Definición — Equi Join ⨝(a=b)
> Join con condición de igualdad explícita entre columnas que pueden tener nombres distintos. Las columnas de la condición NO se eliminan (a diferencia del natural join).
> Sintaxis: relaciónA ⨝(columnaA = columnaB) relaciónB
> SQL mental: JOIN ... ON columnaA = columnaB
> ```mermaid
graph TD
    A[Tabla A] -->|⨝(a=b)| B[Resultado]
    C[Tabla B] -->|⨝(a=b)| B
    style A fill:#e1f5fe
    style C fill:#e1f5fe
    style B fill:#c8e6c9
```

> [!example] 🧪 Ejemplo de equi join
> PRODUCTO ⨝(CODIGO = ID_PRODUCT) VENTA devuelve 2 filas:
> | CODIGO | DESCRIPCION | PRECIO | ID_VENTA | FECHA | ID_PRODUCT | CANTIDAD |
> |---|---|---|---|---|---|---|
> | 101 | Pasta | 3.50 | 2 | 04/02/2020 | 101 | 2 |
> | 104 | Gel | 4.00 | 1 | 02/02/2020 | 104 | 54 |

---

### 3️⃣ Theta Join ⨝(F)

> [!note] 📋 Definición — Theta Join ⨝(F)
> Join con una condición que no es igualdad (≠, >, <, ≥, ≤). Útil para comparaciones de rangos o exclusiones.
> Sintaxis: relaciónA ⨝(condición) relaciónB
> SQL mental: JOIN ... ON con comparación no-igualdad.

> [!example] 🧪 Ejemplo de theta join
> VENTA ⨝(CANTIDAD > 50) PRODUCTO — ventas donde la cantidad supera 50 unidades.

---

### 4️⃣ Left Outer Join ⟕

> [!note] 📋 Definición — Left Outer Join ⟕
> Trae TODAS las filas de la izquierda; las de la derecha que no casan se rellenan con null.
> Sintaxis: relaciónA ⟕ relaciónB
> SQL mental: LEFT JOIN ... ON
> ```mermaid
graph TD
    A[Tabla A] -->|⟕| B[Resultado: todas las de A]
    C[Tabla B] -->|⟕| B
    style A fill:#e1f5fe
    style C fill:#f3e5f5
    style B fill:#c8e6c9
```

> [!example] 🧪 Ejemplo de left outer join
> PRODUCTO ⟕ VENTA devuelve las 2 filas del join normal + la fila del Shampoo 105 con null en todo lo de VENTA.

---

### 5️⃣ Right Outer Join ⟖

> [!note] 📋 Definición — Right Outer Join ⟖
> Trae TODAS las filas de la derecha; las de la izquierda que no casan se rellenan con null.
> Sintaxis: relaciónA ⟖ relaciónB
> SQL mental: RIGHT JOIN ... ON

> [!example] 🧪 Ejemplo de right outer join
> PRODUCTO ⟖ VENTA devuelve las 2 filas del join normal + la fila de la venta 4 (ID_PRODUCT=110) con null en todo lo de PRODUCTO.

---

### 6️⃣ Semijoin ⋉

> [!note] 📋 Definición — Semijoin ⋉
> Trae las filas de la relación izquierda que participan en el join con la derecha, pero solo con los atributos de la izquierda.
> Sintaxis: relaciónA ⋉ relaciónB
> SQL mental: WHERE ... IN / EXISTS

> [!example] 🧪 Ejemplo de semijoin
> VENTA ⋉ PRODUCTO devuelve ventas 1 y 2, solo columnas de VENTA (sus productos sí existen).

---

### 7️⃣ División

> [!note] 📋 Definición — División
> Útil para consultas con la expresión "para todo" o "para cada". Es el operador del ejercicio que pide ítems ordenados por todos los clientes.
> Sintaxis: relaciónA ÷ relaciónB
> SQL mental: doble NOT EXISTS o GROUP BY ... HAVING COUNT = total.

> [!info] 📖 El deck de cátedra: división (slides05, p. 20)
> "es útil para consultas que incluye la expresión 'para todo' o 'para cada'".
> ![[../../Unidad 0 - Guias y Ejercicios/Archivos/Álgebra-Relacional/bd-s05-p20.png]]

---

## 🛠️ Catálogo Completo de Operadores

> [!note] 📚 Catálogo de operadores del álgebra
> | Operador | Símbolo | Qué hace | SQL mental |
> |---|---|---|---|
> | Selección | σ | Filtra filas que cumplen una condición | WHERE |
> | Proyección | π | Elige columnas y elimina duplicadas | SELECT / DISTINCT |
> | Producto cruz | × | Todas las combinaciones (m × n) | FROM a, b sin ON |
> | Join natural | ⨝ | × + σ por mismo nombre/valor + π borra duplicada | JOIN ... ON (claves iguales) |
> | Equi join | ⨝(a=b) | Join con condición de igualdad | JOIN ON |
> | Theta join | ⨝(F) | Join con condición no-igualdad | JOIN ON (comparación) |
> | Left outer join | ⟕ | Todas las filas de la izquierda + null a la derecha | LEFT JOIN |
> | Right outer join | ⟖ | Todas las filas de la derecha + null a la izquierda | RIGHT JOIN |
> | Semijoin | ⋉ | Filas de la izquierda que participan en el join | WHERE ... IN / EXISTS |
> | Unión | ∪ | Filas de ambas tablas sin duplicados | UNION |
> | Diferencia | − | Filas de A que no están en B | NOT IN / NOT EXISTS |
> | Intersección | ∩ | Filas en ambas tablas | INTERSECT |
> | Agregación | γ | Agrupa y calcula (COUNT, SUM, AVG) | GROUP BY (+ HAVING) |
> | Renombre | ρ | Alias de tabla o expresión | AS |
> | Orden | τ | Ordena filas asc / desc | ORDER BY |

---

## 🎯 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Join natural vs equi join

> [!example] 📋 Planteamiento
> Dadas CLIENTE(id, nombre, ciudad) y PEDIDO(id, cliente_id, fecha, total), escribe en álgebra relacional: obtener nombre del cliente y total de cada pedido.
> > [!success]- ✅ Solución
> > π CLIENTE.nombre, PEDIDO.total (CLIENTE ⨝(CLIENTE.id = PEDIDO.cliente_id) PEDIDO)
> > **Por qué:** las columnas de las claves no se llaman igual (id vs cliente_id), así que usamos equi join con condición explícita.

### ✏️ Ejercicio 2 — Left outer join para inclusión

> [!example] 📋 Planteamiento
> Dadas DEPARTAMENTO(id, nombre) y EMPLEADO(id, nombre, depto_id), escribe en álgebra relacional: listar todos los departamentos, incluso los que no tienen empleados, con el nombre de sus empleados si los hay.
> > [!success]- ✅ Solución
> > DEPARTAMENTO ⟕ EMPLEADO
> > **Por qué:** el left outer join conserva todos los departamentos, incluso los sin empleados (que aparecen con null en columnas de EMPLEADO).

### ✏️ Ejercicio 3 — Semijoin para existencia

> [!example] 📋 Planteamiento
> Dadas PRODUCTO(codigo, nombre, precio) and VENTA(producto_id, cantidad, fecha), escribe en álgebra relacional: obtener códigos de productos que se han vendido al menos una vez.
> > [!success]- ✅ Solución
> > π PRODUCTO.codigo (PRODUCTO ⋉ VENTA)
> > **Por qué:** el semijoin trae solo los productos que aparecen en al menos una venta, con solo las columnas de PRODUCTO.

### ✏️ Ejercicio 4 — Theta join para rangos

> [!example] 📋 Planteamiento
> Dada VENTA(monto, fecha), escribe en álgebra relacional: obtener todas las ventas con monto mayor a 1000.
> > [!success]- ✅ Solución
> > σ monto > 1000 (VENTA) — en este caso no se necesita join, solo selección con operador de comparación (theta implícito).
> > Si comparas dos tablas: VENTA1 ⨝(VENTA1.monto > VENTA2.monto) VENTA2.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
> - Distingo join natural de equi join.
> - Sé cuándo usar left outer join vs right outer join.
> - Explico qué hace el semijoin.

> [!note] 📋 Nivel Intermedio
> - Elijo el join correcto según el enunciado (inner, left, right).
> - Escribo la equivalencia SQL de cada operador derivado.
> - Detecto cuándo necesito renombrar (ρ) para un self-join.

> [!note] 📋 Nivel Avanzado
> - Dibujo el diagrama de ejecución de una expresión con múltiples joins.
> - Detecto consultas que usan división y las reescribo con NOT EXISTS.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
> - ¿Join natural?::Combina por columnas del mismo nombre y elimina la duplicada.
> - ¿Equi join?::Join con condición de igualdad explícita entre columnas.
> - ¿Theta join?::Join con condición no-igualdad (>, <, ≠, etc.).
> - ¿Left outer join?::Todas las filas de la izquierda, null a la derecha si no casan.
> - ¿Right outer join?::Todas las filas de la derecha, null a la izquierda si no casan.
> - ¿Semijoin?::Filas de la izquierda que participan en el join, solo sus atributos.
> - ¿División?::Consultas "para todo" o "para cada".
> - ¿Equi join vs join natural?::El equi join conserva las columnas de la condición; el natural las elimina.
> [!note] 🧠 Repasa con el plugin Spaced Repetition (Lección 1: 13-oct)

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
> - [[01 - Operadores Básicos]] — σ, π, ×, ∪, −, ∩ (la base de estos operadores derivados).
> - [[03 - Renombre y Agregación]] — ρ, γ, τ.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — 4 ejercicios resueltos con joins y álgebra.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[03 - Renombre y Agregación]]
> - Anterior: [[01 - Operadores Básicos]]

---

**Tags:** #TICG1018 #unidad3 #algebra-relacional #joins #derivados #bd
