---
dg-publish: true
tags: [TICG1018, unidad3, algebra-relacional, joins, derivados, bd]
---

# 🔗 Álgebra Relacional — Operadores Derivados y Joins

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Joins y no solo Producto Cruz?
>
> El producto cruz × genera todas las combinaciones (m × n filas), casi nunca lo que quieres. Los joins son derivados del producto cruz + selección + proyección que combinan tablas de forma inteligente: solo las filas que "encajan" por una condición.
>
> **Aplicaciones:**
> - **Consultas reales:** casi toda consulta SQL usa al menos un join.
> - **Optimización:** elegir el join correcto cambia si la consulta corre en milisegundos o en segundos.
> - **Lección 1 (13-oct):** natural join, equi join, theta join, left/right outer join.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-02-04-graph.svg]]
>
> **Se lee así:** todos los joins derivados se pueden escribir como `σ F (A × B)`: el producto cruz genera todo, la selección se queda con lo que empareja y la proyección borra las columnas sobrantes. Lo que cambia entre join y join es **qué** se queda y **qué columnas se borran**.

---

## 📋 Definiciones Formales

### 1️⃣ Join Natural ⨝

> [!note] 📋 Definición — Join Natural ⨝
>
> El join natural combina dos relaciones sobre atributos con el mismo nombre y mismo valor, y luego elimina las columnas repetidas.
>
> **Sintaxis:** `relaciónA ⨝ relaciónB`
>
> **Base matemática:** `σ F (A × B)` donde F es el predicado de igualdad en atributos comunes, seguido de `π` que borra la columna duplicada.

> [!example] 🧪 Ejemplo de join natural
>
> | PRODUCTO |
> |---|
> | CODIGO | DESCRIPCION | PRECIO |
> | 101 | Pasta | 3.50 |
> | 104 | Gel | 4.00 |
> | 105 | Shampoo | 10.00 |
> | VENTA |
> |---|
> | ID_VENTA | FECHA | ID_PRODUCT | CANTIDAD |
> | 1 | 02/02/2020 | 104 | 54 |
> | 2 | 04/02/2020 | 101 | 2 |
> | 4 | 04/04/2020 | 110 | -2 |
>
> `PRODUCTO ⨝ VENTA` no tiene columnas de mismo nombre → producto cruz puro (9 filas).
>
> Si renombráramos `ID_PRODUCT` a `CODIGO`, el join natural haría `σ PRODUCTO.CODIGO = VENTA.CODIGO (PRODUCTO × VENTA)` y eliminaría la `CODIGO` duplicada, dejando 2 filas: 101↔venta 2, 104↔venta 1.

> [!info] 📖 El deck de cátedra: los joins y el natural join (slides05, pp. 14-15)
>
> El deck abre el bloque de joins con la definición del natural join y su ejemplo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p14.png]]
>
> **Se lee así:** la lámina (p. 14) define el join y **te da las dos tablas crudas**. La de arriba es `course` con `course_id, title, dept_name, credits` y cuatro filas (`BIO-301 Genetics Biology 4`, `BIO-399 Computational Biology Biology 3`, `CS-101 Intro. to CS Comp. Sci. 4`, `CS-190 Game Design Comp. Sci. 4`). La de abajo es `department` con `dept_name, building, budget` y tres filas (`Biology · Watson · 90000`, `Comp. Sci. · Taylor · 100000`, `History · Painter · 50000`). La lámina marca la **columna común** (`dept_name`) en las dos tablas: esa es la que se usa para emparejar.
>
> **Por qué importa:** fíjate ya en un detalle que define al natural join: la columna que empareja **se llama igual en las dos tablas**. No hay `ON course.dept = department.dept_name`; simplemente `dept_name` con `dept_name`. Esa es su única diferencia con el equi join, y también su debilidad: si las dos tablas no coinciden en el nombre, el natural join **no hace nada** y te devuelve el producto cruz.
>
> **Ejemplo:** en el ejemplo de esta nota, `PRODUCTO` tiene `CODIGO` y `VENTA` tiene `ID_PRODUCT`. Como los nombres difieren, `PRODUCTO ⨝ VENTA` **no puede ser un natural join**: es un producto cruz puro de 9 filas. Si renombraras `ID_PRODUCT` a `CODIGO`, el natural join funcionaría y dejaría solo las 2 filas que casan.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p15.png]]
>
> **Se lee así:** la lámina (p. 15) es la **lámina más útil del bloque de joins**, porque da el resultado y **los tres pasos para obtenerlo**: (1) obtener el producto cartesiano, (2) seleccionar las filas cuyos valores de `dept_name` son iguales (las *join columns*), (3) hacer la proyección del resultado eliminando las columnas duplicadas. El resultado final tiene `course_id, title, dept_name, credits, building, budget` y **4 filas**; fíjate en que `dept_name` aparece **una sola vez**.
>
> **Por qué importa:** esos tres pasos son la **definición operativa** del natural join, y explican por qué el `JOIN` de SQL es tan eficiente: el motor no genera las 12 filas del producto cartesiano para descartar 8; genera directamente las 4. En el modelo relacional el join es "producto cartesiano + filtro + proyección", y por eso su costo se mide por el del producto cartesiano… salvo que el optimizador lo evite.
>
> **Ejemplo:** el resultado de la lámina tiene **4 filas, no 5**: el departamento `History` (Painter, 50000) desaparece, porque ningún curso pertenece a Historia. Ese es el comportamiento del join **interno**: solo sobreviven las filas que casan. La lámina lo dice al final: *"el resultado final no incluye las filas que no concuerdan (no match) con las columnas de join"*.

### 2️⃣ Equi Join ⨝(a=b)

> [!note] 📋 Definición — Equi Join ⨝(a=b)
>
> Join con condición de igualdad explícita entre columnas que pueden tener nombres distintos. Las columnas de la condición **NO** se eliminan (a diferencia del natural join).
>
> **Sintaxis:** `relaciónA ⨝(columnaA = columnaB) relaciónB`
>
> **SQL mental:** `JOIN ... ON columnaA = columnaB`

> [!example] 🧪 Ejemplo de equi join
>
> `PRODUCTO ⨝(CODIGO = ID_PRODUCT) VENTA` devuelve 2 filas:
>
> | CODIGO | DESCRIPCION | PRECIO | ID_VENTA | FECHA | ID_PRODUCT | CANTIDAD |
> |---|---|---|---|---|---|---|
> | 101 | Pasta | 3.50 | 2 | 04/02/2020 | 101 | 2 |
> | 104 | Gel | 4.00 | 1 | 02/02/2020 | 104 | 54 |
>
> **Se lee así:** fíjate en la última tabla: `CODIGO` **y** `ID_PRODUCT` siguen las dos. Esa es exactamente la diferencia con el natural join, que habría dejado una sola columna de clave.

### 3️⃣ Theta Join ⨝(F)

> [!note] 📋 Definición — Theta Join ⨝(F)
>
> Join con una condición que no es igualdad (≠, >, <, ≥, ≤). Útil para comparaciones de rangos o exclusiones.
>
> **Sintaxis:** `relaciónA ⨝(condición) relaciónB`
>
> **SQL mental:** `JOIN ... ON` con comparación no-igualdad.

> [!example] 🧪 Ejemplo de theta join
>
> `VENTA ⨝(CANTIDAD > 50) PRODUCTO` — ventas donde la cantidad supera 50 unidades.

> [!info] 📖 El deck de cátedra: el theta join (slides05, p. 18)
>
> El deck distingue el theta join del equi join por el tipo de comparación.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p18.png]]
>
> **Se lee así:** la lámina (p. 18) da la **definición en una línea**: *"es una operación de Join que usa una condición C de comparación para juntar las tablas"*, y añade la precisión que importa: *"si la condición C está formada de sólo igualdades, se conoce como Equi-Join"*. Abajo, el ejemplo numérico: `DEPTO(DID, Nombre, Ciudad)` con `d1·dpto1·Cali` y `d2·dpto2·Bta`, y `EMPO(EID, Nombres, Apellidos, Sueldo, Depart_id)` con cuatro empleados (`e1·emp1·ap1·10·d1`, `e2·emp2·ap2·20·d2`, `e3·emp3·ap3·10·(vacío)`, `e6·emp6·ap6·30·(vacío)`). El join que se dibuja lleva la condición `EMPO.DEPART_ID = DEPTO.DID`.
>
> **Por qué importa:** la jerarquía del deck es exacta y es la que hay que usar para clasificar: **theta join es el caso general** (cualquier condición `C`); **equi join es el caso particular** donde `C` solo tiene igualdades. Y el ejemplo trae un detalle que explica el motivo de existir del theta join: dos empleados (`e3` y `e6`) **no tienen departamento asignado**. Con un `INNER JOIN` desaparecen; con una condición de no-igualdad (`DID NOT IN (...)`) sí se pueden seleccionar, que es justo el caso que trae la lámina.
>
> **Ejemplo:** `VENTA ⨝(CANTIDAD > 50) PRODUCTO` es theta join: la condición `CANTIDAD > 50` es una comparación que no es igualdad. `PRODUCTO ⨝(CODIGO = ID_PRODUCT) VENTA` es equi join: la condición es una igualdad. Y `VENTA ⨝(ID_PRODUCT NOT IN (SELECT CODIGO FROM PRODUCTO)) VENTA` es theta join de no-igualdad: es la versión que **conserva** las ventas de productos que no están en el catálogo, en lugar de perderlas.

### 4️⃣ Left Outer Join ⟕

> [!note] 📋 Definición — Left Outer Join ⟕
>
> Trae TODAS las filas de la izquierda; las de la derecha que no casan se rellenan con `null`.
>
> **Sintaxis:** `relaciónA ⟕ relaciónB`
>
> **SQL mental:** `LEFT JOIN ... ON`

> [!example] 🧪 Ejemplo de left outer join
>
> `PRODUCTO ⟕ VENTA` devuelve las 2 filas del join normal + la fila del Shampoo 105 con `null` en todo lo de VENTA.

> [!info] 📖 El deck de cátedra: el left outer join (slides05, p. 16)
>
> El deck dibuja el caso donde las filas de la derecha no encuentran pareja.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p16.png]]
>
> **Se lee así:** la lámina (p. 16) es la **definición con el caso difícil dibujado**, y por eso conviene mirarla con atención. Arriba está `course` (4 cursos) y `department` (3 departamentos). En `course`, el curso `CS-190 Game Design` tiene `dept_name` con un **guion** (`-`): es un curso **sin departamento asignado**. Abajo, el resultado de `course ⟕ department`: las 4 filas de `course` están (porque el `⟕` es *left*, la izquierda manda), y la fila extra del final es `History · - · Painter · 50000` — el departamento **History**, que no tiene ningún curso, aparece con `-` en las columnas de `course`.
>
> **Por qué importa:** fíjate en que la lámina muestra **las dos direcciones** de los outer join: `course ⟕ department` (abajo a la izquierda) y `department ⟕ course` (abajo a la derecha). En la primera sobreviven los 4 cursos; en la segunda sobreviven los 3 departamentos. El `⟕` **siempre garantiza la tabla de la izquierda**, sin importar si su columna tiene o no pareja.
>
> **Por qué importa (el `null`):** el guion de la lámina es el `null` real. Y un `null` en `dept_name` **no es lo mismo** que un valor: no es igual a nada, ni siquiera a otro `null` (en SQL, `NULL = NULL` es *unknown*, no verdadero). Por eso un `WHERE dept_name = '-'` sobre datos reales no funciona: hay que usar `IS NULL`.
>
> **Ejemplo:** la razón de usar `LEFT JOIN` es para **no perder información del lado izquierdo**. Con un `INNER JOIN`, el curso `CS-190` desaparecería del resultado y no sabrías que existe sin departamento. Con `LEFT JOIN` aparece con sus columnas de `department` en `null`, y ya puedes preguntarte: ¿debería tener departamento? En la nota, `PRODUCTO ⟕ VENTA` hace lo mismo con el champú `105`, que no tiene ninguna venta.

### 5️⃣ Right Outer Join ⟖

> [!note] 📋 Definición — Right Outer Join ⟖
>
> Trae TODAS las filas de la derecha; las de la izquierda que no casan se rellenan con `null`.
>
> **Sintaxis:** `relaciónA ⟖ relaciónB`
>
> **SQL mental:** `RIGHT JOIN ... ON`

> [!example] 🧪 Ejemplo de right outer join
>
> `PRODUCTO ⟖ VENTA` devuelve las 2 filas del join normal + la fila de la venta 4 (ID_PRODUCT=110) con `null` en todo lo de PRODUCTO.

> [!info] 📖 El deck de cátedra: el right outer join (slides05, p. 17)
>
> El deck muestra el caso simétrico: ahora la que manda es la relación derecha.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p17.png]]
>
> **Se lee así:** la lámina (p. 17) reutiliza **exactamente las mismas dos tablas** de la anterior (`course` y `department`), pero invierte el resultado. Abajo a la izquierda está `department ⟖ course` y abajo a la derecha `course ⟖ department`. Fíjate en la diferencia: en el primer caso el resultado termina con la fila `- - - - History - Painter 50000` (sobreviven los 3 departamentos); en el segundo termina con `- - - - - -` (sobreviven los 4 cursos).
>
> **Por qué importa:** la lámina es la demostración de que **`R ⟖ S` y `S ⟕ R` dan el mismo resultado**: los outer join no inventan datos, solo deciden **qué lado no se puede descartar**. Por eso `RIGHT JOIN` casi nunca se usa: siempre se puede escribir la consulta al revés y usar `LEFT JOIN`. Es una cuestión de estilo, no de potencia.
>
> **Ejemplo:** en el ejemplo de la nota, `PRODUCTO ⟖ VENTA` conserva la venta `4` (la del producto `110`, que no existe en `PRODUCTO`) con todos los campos de `PRODUCTO` en `null`. Esa venta es una devolución de un producto que ya no está en catálogo; el `RIGHT JOIN` es el que te deja verla. Y la versión equivalente sería `VENTA ⟕ PRODUCTO`, que además es la que se suele escribir porque el `LEFT` es el que todos los motores optimizan mejor.

### 6️⃣ Semijoin ⋉

> [!note] 📋 Definición — Semijoin ⋉
>
> Trae las filas de la relación izquierda que participan en el join con la derecha, pero solo con los atributos de la izquierda.
>
> **Sintaxis:** `relaciónA ⋉ relaciónB`
>
> **SQL mental:** `WHERE ... IN / EXISTS`

> [!example] 🧪 Ejemplo de semijoin
>
> `VENTA ⋉ PRODUCTO` devuelve ventas 1 y 2, solo columnas de VENTA (sus productos sí existen).

### 7️⃣ División

> [!note] 📋 Definición — División
>
> Útil para consultas con la expresión "para todo" o "para cada". Es el operador del ejercicio que pide ítems ordenados por todos los clientes.
>
> **Sintaxis:** `relaciónA ÷ relaciónB`
>
> **SQL mental:** doble `NOT EXISTS` o `GROUP BY ... HAVING COUNT = total`.

> [!info] 📖 El deck de cátedra: la división (slides05, pp. 19-22)
>
> El deck dedica cuatro láminas al operador que responde "para todo".
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p19.png]]
>
> **Se lee así:** la lámina (p. 19) da la **regla de existencia** y la **fórmula de los atributos**. Primero: *"es útil para consultas que incluyen la expresión 'para todo' o 'para cada'"*. Segundo: *"la operación R ÷ S está definida si los atributos de S son un subconjunto de los de R"*. Y la fórmula: si `R` tiene atributos `(A1, …, Am, B1, …, Bn)` y `S` tiene `(B1, …, Bn)`, entonces el resultado tiene los atributos `A − B = (A1, …, Am)`.
>
> **Por qué importa:** la fórmula explica **qué columnas tiene la respuesta**: las de `R` que **no** están en `S`. Y la condición de existencia explica **por qué no siempre se puede dividir**: si `S` tiene un atributo que `R` no tiene, la operación **no está definida**. Es una operación con precondiciones, y eso es raro en álgebra relacional.
>
> **Ejemplo:** con `R = PEDIDO(cliente, item)` y `S = CLIENTE(cliente)`, el resultado tiene la columna `item` (porque `cliente` está en `S` y `item` no). Y `R ÷ S` está bien definida porque `{cliente} ⊆ {cliente, item}`. Si `S` tuviera además una columna `ciudad`, la división dejaría de estar definida: `R` no tiene `ciudad`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p20.png]]
>
> **Se lee así:** la lámina (p. 20) es la **del ejemplo numérico**, y ahí está todo el ejercicio. La relación `A(sno, pno)` tiene nueve filas: `s1` con `p1, p2, p3, p4`; `s2` con `p1, p2`; `s3` solo con `p2`; y `s4` con `p2, p4`. Los divisores son `B1 = {p2}`, `B2 = {p1, p2, p4}` y `B3 = {p1, p2, p4}` (con `p2` repetido en la lista, lo que la lámina muestra como `pno pno`). Y los tres resultados: `A ÷ B1 = {s1, s2, s3, s4}`, `A ÷ B2 = {s1, s4}` y `A ÷ B3 = {s1}`.
>
> **Por qué importa:** lee los resultados con la definición en la mano y se entienden solos. Por ejemplo, `A ÷ B2 = {s1, s4}`: ¿quién aparece **con todos** los `pno` de `B2`, es decir `p1`, `p2` y `p4`? `s1` sí (los tiene todos) y `s4`… solo tiene `p2` y `p4`, le falta `p1`. Eso significa que la lista `B2` del divisor **no se está usando como un conjunto**, sino como una **multiset**: `p1` aparece dos veces en `B2` (`pno, pno`), y `s4` tiene que tener `p1` **dos veces** en `A` para aparecer en el resultado. Esa lectura es la clave para entender el caso `A ÷ B3`.
>
> **Ejemplo:** `A ÷ B3 = {s1}` porque `B3` exige `p1` **dos veces**, `p2` una vez y `p4` una vez. Solo `s1` cumple: tiene `p1` una vez… y por eso el deck lo muestra como resultado "truncado" precisamente para ilustrar la multiset. La forma de decirlo: **cada fila del divisor debe estar emparejada con una fila distinta de `A`**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p21.png]]
>
> **Se lee así:** la lámina (p. 21) repite los mismos datos y **solo destaca la regla de lectura**: *"el resultado de la división contiene todos los valores de las columnas no comunes, que están asociadas con todas las filas del divisor"*. Fíjate en la fórmula de la p. 20: el resultado tiene la columna `sno`, la que **no** está en el divisor `Bi`.
>
> **Por qué importa:** el deck escribe la regla dos veces, en dos láminas, y esa repetición es la señal de que es **lo que hay que memorizar**. La versión corta: *"la división devuelve las filas de R que se emparejan con TODAS las filas de S"*. La versión con truco: es un **`JOIN` + una comparación de conteos**.
>
> **Ejemplo:** `A ÷ B2` es, en SQL, `SELECT sno FROM A GROUP BY sno HAVING COUNT(DISTINCT pno) = (SELECT COUNT(DISTINCT pno) FROM B2)`. El `HAVING` con comparación de conteos es la traducción directa de "para todos".
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p22.png]]
>
> **Se lee así:** la lámina (p. 22) es la que **convierte el operador en un problema de negocio**. Plantea: dadas `clientes(cust)` y `órdenes(ord)`, *¿cuáles ítems han sido ordenados por todos los clientes?*. Y añade el argumento de por qué esto es difícil de responder con un `JOIN`: *"si hubieran 2 clientes, la consulta sería sencilla, pero no sabemos cuántos clientes hay, ¿qué pasaría si fueran 100 clientes o más?"*. La expresión de la lámina es `π iid, cid (ord) ÷ π cid (cust)`.
>
> **Por qué importa:** ese es el argumento de fondo de la división. Un `JOIN` te da *"los ítems que **algún** cliente pidió"*; un `LEFT JOIN` con `COUNT` te da *"los ítems que **todos** los clientes pidieron"*; pero en cuanto el número de clientes es desconocido, el `JOIN` **no puede** expresar la condición sin un subquery que lo cuente por separado. La división es la forma de decirlo de una vez.
>
> **Ejemplo:** la expresión de la lámina se lee así: primero `π cid (cust)` da **la lista de todos los clientes** (el divisor); luego `π iid, cid (ord)` da **qué cliente pidió qué ítem** (el dividendo); y la división devuelve los `iid` que aparecen **para cada** `cid` de la lista. En SQL real esto se hace con un doble `NOT EXISTS`: *"ítems para los que no existe un cliente que no lo haya pedido"*.

---

## 🛠️ Catálogo Completo de Operadores

> [!note] 📚 Catálogo de operadores del álgebra
>
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
>
> **Se lee así:** la primera mitad de la tabla son **operadores básicos** (se definieron desde cero) y la segunda son **derivados** (se construyen con los básicos). Si puedes escribir un join como `σ F (A × B)`, ya no necesitas memorizar su nombre.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Join natural vs equi join

> [!example] 📋 Planteamiento
>
> Dadas CLIENTE(id, nombre, ciudad) y PEDIDO(id, cliente_id, fecha, total), escribe en álgebra relacional: obtener nombre del cliente y total de cada pedido.
>
> > [!success]- ✅ Solución
> >
> > π CLIENTE.nombre, PEDIDO.total (CLIENTE ⨝(CLIENTE.id = PEDIDO.cliente_id) PEDIDO)
> >
> > **Por qué:** las columnas de las claves no se llaman igual (id vs cliente_id), así que usamos equi join con condición explícita.

### ✏️ Ejercicio 2 — Left outer join para inclusión

> [!example] 📋 Planteamiento
>
> Dadas DEPARTAMENTO(id, nombre) y EMPLEADO(id, nombre, depto_id), escribe en álgebra relacional: listar todos los departamentos, incluso los que no tienen empleados, con el nombre de sus empleados si los hay.
>
> > [!success]- ✅ Solución
> >
> > DEPARTAMENTO ⟕ EMPLEADO
> >
> > **Por qué:** el left outer join conserva todos los departamentos, incluso los sin empleados (que aparecen con null en columnas de EMPLEADO).

### ✏️ Ejercicio 3 — Semijoin para existencia

> [!example] 📋 Planteamiento
>
> Dadas PRODUCTO(codigo, nombre, precio) y VENTA(producto_id, cantidad, fecha), escribe en álgebra relacional: obtener códigos de productos que se han vendido al menos una vez.
>
> > [!success]- ✅ Solución
> >
> > π PRODUCTO.codigo (PRODUCTO ⋉ VENTA)
> >
> > **Por qué:** el semijoin trae solo los productos que aparecen en al menos una venta, con solo las columnas de PRODUCTO.

### ✏️ Ejercicio 4 — Theta join para rangos

> [!example] 📋 Planteamiento
>
> Dada VENTA(monto, fecha), escribe en álgebra relacional: obtener todas las ventas con monto mayor a 1000.
>
> > [!success]- ✅ Solución
> >
> > σ monto > 1000 (VENTA) — en este caso no se necesita join, solo selección con operador de comparación (theta implícito).
> >
> > Si comparas dos tablas: VENTA1 ⨝(VENTA1.monto > VENTA2.monto) VENTA2.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo join natural de equi join.
> - [ ] Sé cuándo usar left outer join vs right outer join.
> - [ ] Explico qué hace el semijoin.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Elijo el join correcto según el enunciado (inner, left, right).
> - [ ] Escribo la equivalencia SQL de cada operador derivado.
> - [ ] Detecto cuándo necesito renombrar (ρ) para un self-join.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Dibujo el diagrama de ejecución de una expresión con múltiples joins.
> - [ ] Detecto consultas que usan división y las reescribo con NOT EXISTS.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - Diapositivas `2026_1PAO_slides5_1_TICG1018.pdf` — Álgebra Relacional, pp. 14-22 (joins, outer joins, theta join y división).
> - Diapositivas `3.2 Operaciones Derivadas-join-order2026.pdf` — módulo de joins y orden de ejecución.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 8 — álgebra relacional y sus equivalentes en SQL.
> - Guía: [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — ejercicios resueltos de joins.
> - Diagramas propios: `u3-02-01-graph` … `u3-02-07-graph` (un diagrama por operador derivado).

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Join natural?::Combina por columnas del mismo nombre y elimina la duplicada.
> - ¿Equi join?::Join con condición de igualdad explícita entre columnas.
> - ¿Theta join?::Join con condición no-igualdad (>, <, ≠, etc.).
> - ¿Left outer join?::Todas las filas de la izquierda, null a la derecha si no casan.
> - ¿Right outer join?::Todas las filas de la derecha, null a la izquierda si no casan.
> - ¿Semijoin?::Filas de la izquierda que participan en el join, solo sus atributos.
> - ¿División?::Consultas "para todo" o "para cada".
> - ¿Equi join vs join natural?::El equi join conserva las columnas de la condición; el natural las elimina.
> - ¿Todos los joins derivados son?::σ F (A × B) — producto cruz + selección.
> - ¿Qué conserva el outer join?::Todas las filas del lado que manda; la otra se rellena con null.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[01 - Operadores Básicos]] — σ, π, ×, ∪, −, ∩ (la base de estos operadores derivados).
> - [[03 - Renombre y Agregación]] — ρ, γ, τ.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — 4 ejercicios resueltos con joins y álgebra.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[03 - Renombre y Agregación]]
> - Anterior: [[01 - Operadores Básicos]]

---

**Tags:** #TICG1018 #unidad3 #algebra-relacional #joins #derivados #bd
