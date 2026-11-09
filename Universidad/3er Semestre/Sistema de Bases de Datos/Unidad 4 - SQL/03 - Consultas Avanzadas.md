---
dg-publish: true
tags: [TICG1018, unidad4, sql, consultas-avanzadas, join, group-by, subquery, union, vista, trigger, grant, bd]
---

# 🔍 SQL — Consultas Avanzadas

## 🎯 Introducción

> [!info] 💡 ¿Qué cubre esta nota?
>
> Consultas que van más allá del SELECT básico: JOINs múltiples, GROUP BY con HAVING, subconsultas, operadores de conjuntos (UNION, INTERSECT, EXCEPT), vistas, índices, triggers, procedimientos almacenados y control de permisos.
>
> **Aplicaciones:**
> - **Consultas reales:** la mayoría de consultas de producción usan JOIN + GROUP BY.
> - **Optimización:** índices y EXPLAIN para ver el plan de ejecución.
> - **Seguridad:** usuarios, permisos por columna, vistas con acceso restringido.
> - **Lección 1 (13-oct):** JOIN, GROUP BY, HAVING, subquery, UNION.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-03-01-graph.svg]]
>
> **Se lee así:** hay dos familias distintas de "juntar" datos. Los **JOIN** pegan tablas **horizontalmente** (una fila de A se une con una de B, aumentando el número de columnas); los **operadores de conjuntos** (`UNION`, `INTERSECT`, `EXCEPT`) apilan resultados **verticalmente** (mismas columnas, filas de una consulta encima de otra). Confundirlos es el error más común de la unidad.

> [!info] 📖 El deck de cátedra: el temario de SQL Avanzado (SQL Avanzado, p. 1)
>
> El deck que acompaña a esta nota se organiza en tres bloques: vistas, disparadores y procedimientos almacenados.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p1.png]]
>
> **Se lee así:** la lámina (p. 1) es la **portada del deck** y su índice: tres títulos, *Vistas · Disparadores · Procedimientos Almacenados*. No hay ninguna definición en ella; su trabajo es decirte **en qué orden viene el temario**.
>
> **Por qué importa:** ese orden es también el **orden de dependencia** del bloque, y por eso conviene leerlo como una progresión y no como una lista. Las **vistas** guardan una *consulta*. Los **disparadores** guardan una *reacción* a un evento. Los **procedimientos** guardan *lógica de negocio* que se invoca a mano. De menos a más: de "consulta reutilizable" a "regla que se dispara sola" a "programa que se ejecuta bajo demanda".
>
> **Ejemplo:** si un cliente pide "dame siempre los botes rojos con su número de reservas", eso es una **vista**. Si el sistema debe "cada vez que alguien inserta un pedido, descontar el límite de crédito del cliente", eso es un **disparador**. Y si el sistema debe "cerrar el mes y recalcular los totales de cada cliente", eso es un **procedimiento**: lo llamas cuando toca y no se dispara solo.

---

## 📋 Definiciones Formales

### 1️⃣ JOIN — unir filas de varias tablas

> [!note] 📋 Definición — JOIN en SQL
>
> Combina filas de dos o más tablas basándose en una columna relacionada.
>
> | Tipo | Sintaxis | Qué trae |
> |---|---|---|
> | `INNER JOIN` | `FROM a JOIN b ON a.x = b.x` | Solo filas que casan en ambas |
> | `LEFT JOIN` | `FROM a LEFT JOIN b ON a.x = b.x` | Todas las de `a`, null en `b` si no casan |
> | `RIGHT JOIN` | `FROM a RIGHT JOIN b ON a.x = b.x` | Todas las de `b`, null en `a` si no casan |
> | `SELF JOIN` | `FROM a JOIN a AS b ON ...` | La misma tabla dos veces con alias |
>
> **Ejemplos:**
> - `LEFT JOIN` + `COUNT(i.ID)` — conserva los departamentos sin instructores y cuenta 0, no 1.
> - `SELF JOIN` — un empleado contra su jefe: `FROM empleado e JOIN empleado j ON e.jefe_id = j.id`.

> [!example] 🧪 Ejemplo de JOIN múltiple
>
> ```sql
> SELECT c.course_id, c.title,
>        COUNT(t.ID) AS estudiantes,
>        pc.title AS nombre_prerrequisito
> FROM course c
>   JOIN takes t      ON c.course_id = t.course_id
>   JOIN prerequisite pr ON c.course_id = pr.course_id
>   JOIN course pc    ON pr.prereq_id = pc.course_id
> GROUP BY c.course_id, c.title, pc.title
> HAVING COUNT(t.ID) > 5
> ORDER BY estudiantes DESC;
> ```
>
> **Se lee así:** la misma tabla `course` aparece dos veces con alias distintos (`c` y `pc`): la primera es el curso, la segunda es su prerrequisito. Por eso un JOIN no es "juntar dos tablas" sino **juntar filas** — y `course` se junta consigo misma.

> [!note] 📋 Definición — UNION, INTERSECT, EXCEPT
>
> | Operador | Qué hace | SQL mental |
> |---|---|---|
> | `UNION` | Filas de ambas consultas, sin duplicados | `UNION` |
> | `UNION ALL` | Filas de ambas consultas, con duplicados | `UNION ALL` |
> | `INTERSECT` | Filas que aparecen en ambas consultas | `INTERSECT` |
> | `EXCEPT` | Filas de la primera que no están en la segunda | `NOT IN / NOT EXISTS` |
>
> **Ejemplos:**
> - `UNION` vs `UNION ALL` — misma operación, distinta pregunta: ¿"qué filas aparecen" o "cuántas veces aparece cada fila"?
> - `EXCEPT` — "estudiantes que nunca took un curso" = todos menos los que aparecen en `takes`.

> [!example] 🧪 Ejemplo de INTERSECT
>
> ```sql
> -- course_id que aparecen tanto en takes como en teaches
> SELECT t.course_id, c.title
> FROM course c
> JOIN (
>   SELECT t1.course_id FROM takes t1
>   INTERSECT
>   SELECT t2.course_id FROM teaches t2
> ) x ON x.course_id = c.course_id;
> ```
>
> **Por qué importa:** `INTERSECT` **elimina duplicados** implícitamente. Si necesitas contar cuántas veces se repite un `course_id`, `INTERSECT` no sirve: usa `INTERSECT ALL` o cuenta antes de intersectar.

### 2️⃣ GROUP BY y HAVING — el orden de las cláusulas

> [!note] 📋 Definición — GROUP BY y HAVING
>
> `GROUP BY` agrupa filas por una columna. `HAVING` filtra grupos (después de agrupar), a diferencia de `WHERE` que filtra filas (antes de agrupar).
>
> **Regla rápida:** filtro de fila → `WHERE`; filtro de grupo → `HAVING`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-03-02-flow.svg]]
>
> **Se lee así:** las cláusulas se ejecutan en un orden fijo, no en el que las escribes. `WHERE` filtra **antes** de agrupar (más barato); `HAVING` filtra **después** (solo ve los grupos). Por eso un `HAVING` sobre `AVG(salary) > 70000` no se puede escribir como `WHERE AVG(salary) > ...` — en el `WHERE` todavía no existe el grupo.

> [!example] 🧪 Ejemplo de GROUP BY con HAVING
>
> ```sql
> -- Salario promedio por departamento, solo > 70000, ordenado desc
> SELECT dept_name, AVG(salary) AS salario_promedio
> FROM instructor
> GROUP BY dept_name
> HAVING AVG(salary) > 70000
> ORDER BY salario_promedio DESC;
> ```

> [!warning] ⚠️ La columna del GROUP BY y la del SELECT
>
> Toda columna del `SELECT` que **no** sea una función de agregación (`AVG`, `COUNT`, `SUM`, `MAX`, `MIN`) tiene que estar en el `GROUP BY`. Si no, el motor no sabe de qué fila tomar el valor y la consulta falla.

### 3️⃣ Subconsultas — una consulta dentro de otra

> [!note] 📋 Definición — Subconsulta
>
> Una consulta anidada dentro de otra. Puede ir en `FROM`, `WHERE` o `SELECT`.
>
> | Tipo | Dónde va | Uso típico |
> |---|---|---|
> | Correlacionada | `WHERE` | Se ejecuta por cada fila externa |
> | No correlacionada | `FROM` o `WHERE` | Se ejecuta una vez |
> | Escalar | `SELECT` | Devuelve un solo valor |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-03-03-flow.svg]]
>
> **Se lee así:** la subconsulta correlacionada **usa el valor de la fila que se está procesando** (`t.ID = s.ID`). Por eso el motor la reevalúa una vez por cada fila externa: es correcta, pero es la forma más lenta de las tres. Cuando puedas, usa `JOIN` o `EXCEPT`.

> [!example] 🧪 Ejemplo de subconsulta correlacionada
>
> ```sql
> -- Estudiante que nunca tomó curso (EXCEPT)
> SELECT s.ID, s.name FROM student s
> EXCEPT
> SELECT t.ID FROM takes t;
> ```
>
> **Ejemplos:**
> - **No correlacionada:** `WHERE salary > (SELECT AVG(salary) FROM instructor)` — el promedio se calcula una vez.
> - **Escalar:** `SELECT (SELECT COUNT(*) FROM takes) AS total_inscripciones` — devuelve un solo valor.

### 4️⃣ Vistas — la consulta guardada con nombre

> [!note] 📋 Definición — VISTA
>
> Una vista es una consulta guardada con nombre. Se comporta como una tabla virtual.
>
> **Sintaxis:**
>
> ```sql
> CREATE VIEW nombre_vista AS
> SELECT columnas FROM tabla WHERE condición;
> ```
>
> **Ejemplo:**
> - `CREATE VIEW vista_juegos_populares AS SELECT ...` — cada vez que la consultas, corre la consulta original.

> [!example] 🧪 Ejemplo de vista
>
> ```sql
> CREATE VIEW vista_juegos_populares AS
> SELECT v.titulo, v.plataforma,
>        COUNT(a.id_alquiler) AS numero_alquileres,
>        SUM(a.dias_alquilados) AS dias_acumulados
> FROM videojuegos v
>   JOIN alquileres a ON a.id_juego = v.id_juego
> GROUP BY v.titulo, v.plataforma
> HAVING SUM(a.dias_alquilados) > 100
> ORDER BY numero_alquileres ASC;
> ```
>
> **Se lee así:** la vista no guarda datos: guarda la **consulta**. Por eso necesita los mismos permisos que las tablas base, y por eso una vista con `GROUP BY` + `HAVING` es literalmente la consulta que se re-ejecuta cada vez.

> [!warning] ⚠️ Permisos para crear vistas
>
> Crear una vista requiere 3 derechos: SELECT de las tablas base, CREATE VIEW, y SELECT sobre la vista para leerla. Tener SELECT de las tablas base no garantiza poder crear la vista.

> [!info] 📖 El deck de cátedra: las vistas (SQL Avanzado, pp. 2-4)
>
> El deck define la vista y luego la usa sobre la base de ejemplo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p2.png]]
>
> **Se lee así:** la lámina (p. 2) da la **sintaxis** — `CREATE VIEW nombre_de_vista [<columnas>] AS <expresion de consulta>` — y el propósito: *"utilizadas para aumentar las posibilidades de acceso a tablas"*. Abajo, el ejemplo completo de la vista `Rojos`: `CREATE VIEW Rojos AS SELECT B.bid, COUNT(*) AS scount FROM Botes B, Reservacion R WHERE R.bid = B.bid AND B.color = 'rojo' GROUP BY B.bid;` — o sea, "qué botes rojos existen y cuántas reservas tiene cada uno".
>
> **Por qué importa:** fíjate en que la vista **hereda toda la complejidad** de la consulta: un `JOIN`, un `WHERE`, un `GROUP BY` y un `COUNT`. Eso es precisamente su valor: quien use la vista después escribe `SELECT * FROM Rojos;` y **no necesita saber** que hay dos tablas en juego. Y fíjate en el `AS` con su subconsulta: la vista **no guarda datos**, guarda la **consulta**.
>
> **Ejemplo:** el nombre `Rojos` es el **nombre de la vista** y `scount` el nombre de la columna (`AS scount`). Si el `AS` no estuviera, la columna se llamaría `COUNT(*)`, que es un nombre horrible para usar en un reporte. El `AS` dentro de la vista es lo que hace que la vista sea usable.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p3.png]]
>
> **Se lee así:** la lámina (p. 3) es la que explica **para qué sirve una vista**, y tiene tres motivos: *"parecidas a las tablas, la diferencia es que las vistas son creadas a partir de las tablas"*, y luego las tres razones: **"hace la programación simple"**, *"usadas normalmente para crear reportes"* y *"seguridad al compartir información"*.
>
> **Por qué importa:** esas tres razones son **exactamente** los tres motivos para usar una vista, y cada una tiene un uso distinto. *Simplificar*: encapsular una consulta complicada. *Reportes*: la vista es el reporte, y se consulta como si fuera una tabla. *Seguridad*: **es la razón más potente**, porque puedes darle a un usuario permiso de `SELECT` **solo sobre la vista** y sin acceso a las tablas base. El usuario ve exactamente las columnas del `SELECT`, ni una más.
>
> **Ejemplo:** la vista `promedios_clientes` del punto siguiente expone `nombres`, `apellidos` y `promedios`. Si le das acceso a un usuario de gerencia, él puede hacer `SELECT * FROM promedios_clientes` y **nunca** ver el `payment.amount` de otros clientes ni las columnas de la tabla `customer` que no necesitas. Es la misma idea del DCL del deck de DDL, pero aplicada al diseño de datos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p4.png]]
>
> **Se lee así:** la lámina (p. 4) es la **vista completa sobre la base `sakila`**: `create view promedios_clientes as select c.first_name as nombres, c.last_name as apellidos, avg(p.amount) as promedios from customer as c inner join payment as p on c.customer_id = p.customer_id group by c.customer_id;`. Es el mismo patrón de la vista `Rojos`, pero sobre un `JOIN` real.
>
> **Por qué importa:** mira lo que hace la vista: **une dos tablas, agrupa por cliente y promedia**. Con una sola sentencia. Y desde ese momento, cualquier persona que necesite "el promedio de gasto por cliente" escribe una consulta de **una línea** en lugar de la de ocho.
>
> **Ejemplo:** la diferencia práctica está en el **mantenimiento**. Si mañana el negocio cambia "promedio" por "total" y además quiere contar las compras, cambias **una vez** la definición de la vista y las 50 consultas que la usan se actualizan solas. Si las 50 consultas tuvieran el `JOIN` escrito a mano, tendrías que editar 50 archivos. Esa es la diferencia entre "copiar y pegar" y "definir una vista".

### 5️⃣ Índices y EXPLAIN — acelerar el acceso

> [!note] 📋 Definición — Índice compuesto
>
> Un índice compuesto se crea sobre varias columnas. El orden importa: el B+tree busca por prefijo, así que la columna de igualdad debe ir primero.
>
> **Sintaxis:**
>
> ```sql
> CREATE INDEX nombre_indice ON tabla (columna1, columna2);
> ```
>
> **Ejemplos:**
> - `CREATE INDEX idx_nombre_fecha ON alquileres (id_cliente, fecha_alquiler)` — sirve para filtrar por `id_cliente` **y** por el rango de `fecha_alquiler`.
> - `CREATE INDEX idx (apellido, nombre)` — ese índice **no** sirve para buscar solo por `nombre`.

> [!example] 🧪 Ejemplo de índice compuesto
>
> ```sql
> -- Antes: scan completo de la tabla
> EXPLAIN SELECT a.id_alquiler, a.id_juego, a.fecha_alquiler, a.dias_alquilados
> FROM alquileres a JOIN clientes c USING (id_cliente)
> WHERE c.nombre = 'Sofia Leon'
>   AND a.fecha_alquiler BETWEEN '2024-06-01' AND '2024-06-30';
>
> -- Después: índice compuesto
> CREATE INDEX idx_nombre_fecha ON alquileres (id_cliente, fecha_alquiler);
> ```

> [!info] 📊 Lectura esperada de EXPLAIN
>
> | Plan | Type | Key | Rows Scanned | Extra info |
> |---|---|---|---|---|
> | Antes | ALL | NULL | miles (scan completo) | Using where |
> | Después | range | idx_nombre_fecha | pocas (solo el mes) | Using index condition |
>
> **Se lee así:** `Type = ALL` es la alarma — el motor leyó toda la tabla. `Type = range` con `Key` poblado significa que el índice se usó y solo se recorrió el rango del mes. Un índice mal ordenado no cambia nada: el `EXPLAIN` sigue diciendo `ALL`.

### 6️⃣ Triggers y procedimientos almacenados

> [!note] 📋 Definición — Trigger
>
> Un trigger es un procedimiento que se ejecuta automáticamente ante un evento (INSERT, UPDATE, DELETE) en una tabla.
>
> **Sintaxis:**
>
> ```sql
> CREATE TRIGGER nombre_trigger
> BEFORE/AFTER INSERT/UPDATE/DELETE ON tabla
> FOR EACH ROW
> BEGIN
>   -- lógica del trigger
> END;
> ```
>
> **Ejemplos:**
> - `BEFORE INSERT` — valida o corrige el valor **antes** de que la fila exista.
> - `AFTER UPDATE` — recalcula totales **después** de que la fila cambió.
> - `FOR EACH ROW` — el cuerpo corre una vez por fila afectada.

> [!example] 🧪 Ejemplo de trigger con SIGNAL
>
> ```sql
> CREATE TRIGGER trg_validar_resena
> BEFORE INSERT ON resenas
> FOR EACH ROW
> BEGIN
>   IF NEW.puntuacion NOT BETWEEN 1 AND 5 THEN
>     SIGNAL SQLSTATE '45000'
>     SET MESSAGE_TEXT = 'Puntuación fuera de rango (1 a 5)';
>   END IF;
> END;
> ```
>
> **Se lee así:** `SIGNAL SQLSTATE '45000'` aborta la operación. Un trigger `BEFORE` puede **cancelar** la sentencia; uno `AFTER` ya no puede — para cuando corres, la fila ya está escrita.

> [!note] 📋 Definición — Procedimiento almacenado
>
> Un procedimiento es un bloque de código SQL guardado en la base de datos que se puede ejecutar con parámetros de entrada y salida.
>
> **Sintaxis:**
>
> ```sql
> CREATE PROCEDURE nombre_proc(IN parametro Tipo, OUT resultado Tipo)
> BEGIN
>   -- lógica
> END;
> ```
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-03-04-graph.svg]]
>
> **Se lee así:** vista, índice y trigger son tres caras de *"código que vive dentro de la base de datos"*. La **vista** guarda una consulta, el **índice** guarda una estructura de acceso y el **trigger** guarda una reacción automática. El **procedimiento** es el cuarto: guarda lógica de negocio que se invoca a mano con `CALL`.

> [!info] 📖 El deck de cátedra: los disparadores (SQL Avanzado, pp. 5-13)
>
> El deck dedica nueve láminas a los triggers: qué son, cómo se escriben y cuatro casos reales.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p5.png]]
>
> **Se lee así:** la lámina (p. 5) da la **definición**: un trigger es un *"procedimiento que se ejecuta cuando se cumple una condición establecida al realizar una operación de inserción (INSERT), actualización (UPDATE) o borrado (DELETE)"*, y el deck lo presenta como algo usado para mejorar la administración de la base de datos.
>
> **Por qué importa:** la definición tiene tres palabras clave: **procedimiento**, **condición** y **operación**. Un trigger no es una consulta que tú ejecutas: es un bloque de código que el motor **ejecuta solo** cuando ocurre el evento. Y el evento es siempre uno de los tres del DML: `INSERT`, `UPDATE` o `DELETE`.
>
> **Ejemplo:** el caso más claro: cada vez que se inserta un pago, el motor recalcula el total del cliente. La aplicación no tiene que acordarse de hacerlo — el motor lo hace porque alguien lo programó una vez. Esa es la diferencia entre "la aplicación que se porta bien" y "la base de datos que garantiza la regla".
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p6.png]]
>
> **Se lee así:** la lámina (p. 6) descompone el trigger en **dos piezas**, y esto es lo que hay que entender: la **llamada de activación** es *"la sentencia que permite 'disparar' el código a ejecutar"*, y la **restricción** es *"la condición necesaria para realizar el código"*, que *"puede ser de tipo condicional o de otro tipo"*.
>
> **Por qué importa:** esta separación explica por qué existen `BEFORE` y `AFTER`. La **llamada de activación** es el *cuándo* (el evento: `INSERT`, `UPDATE`, `DELETE`) y la **restricción** es el *condicional* (la condición que debe cumplirse). Un trigger `BEFORE` modifica el valor **antes** de que se grabe; uno `AFTER` actúa **después** de que ya se grabó.
>
> **Ejemplo:** un trigger `BEFORE INSERT` que aplica un descuento **cambia el valor que se va a guardar** (todavía no está guardado, por eso es `BEFORE`). Un trigger `AFTER INSERT` que recalcula un total **lee lo que ya se guardó** y escribe en otra tabla. Si te confunde el orden, pregúntate: *¿necesito ver el valor final?* Si sí, `AFTER`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p7.png]]
>
> **Se lee así:** la lámina (p. 7) es la **sintaxis**, y son solo dos palabras que hay que saber: `trigger_time: BEFORE or AFTER` y `trigger_event: INSERT, UPDATE OR DELETE`. Después, la forma completa: `CREATE TRIGGER <trigger_name> <trigger_time> <trigger_event> ON <table_name> FOR EACH ROW ...`, y el `DELIMITER` que delimita el bloque.
>
> **Por qué importa:** la estructura mental es `CREATE TRIGGER <nombre> <cuándo> <qué evento> ON <tabla>`. Es la misma estructura mental del `CREATE TABLE <nombre> (...)`: primero el **nombre**, luego las **características**. Y fíjate en el `FOR EACH ROW`: el trigger se ejecuta **una vez por cada fila afectada**, no una vez por sentencia. Por eso un `INSERT` de 500 filas dispara 500 veces el trigger.
>
> **Ejemplo:** `CREATE TRIGGER tr1 BEFORE INSERT ON PAYMENTS FOR EACH ROW BEGIN ... END` se lee de izquierda a derecha: "cada vez que se inserte en `PAYMENTS`, antes de guardarlo, haz esto". Y el `DELIMITER` existe porque el cuerpo del trigger tiene varios `;` (uno por sentencia) y MySQL necesita saber dónde acaba el bloque; con `DELIMITER $$` le dices que el bloque termina en `$$` y no en `;`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p8.png]]
>
> **Se lee así:** la lámina (p. 8) es el **trigger de ejemplo**, y su valor está en que **un solo disparo hace tres cosas**: `CREATE TRIGGER testref BEFORE INSERT ON test1 FOR EACH ROW BEGIN INSERT INTO test2 SET a2 = NEW.a1; DELETE FROM test3 WHERE a3 = NEW.a1; UPDATE test4 SET b4 = b4 + 1 WHERE a4 = NEW.a1; END`. Un `INSERT` en `test2`, un `DELETE` en `test3` y un `UPDATE` en `test4`, todos disparados por la misma inserción en `test1`.
>
> **Por qué importa:** fíjate en `NEW.a1`: esa es la forma de referirse al valor de la fila que se está insertando. El `NEW` es el "nuevo" valor; el otro pseudo-registro, `OLD`, es el valor anterior (solo tiene sentido en `UPDATE` y `DELETE`). Con `NEW` y `OLD` un trigger puede **comparar antes y después** sin consultar la tabla.
>
> **Ejemplo:** en un `AFTER UPDATE` sobre `PAYMENTS`, `OLD.amount` es el importe que tenía y `NEW.amount` el que tiene ahora. Con solo `NEW` sabes el valor nuevo; con los dos, puedes detectar el cambio y actuar solo si hubo cambio real. Un trigger `AFTER UPDATE` con `IF NOT (OLD.amount <=> NEW.amount) THEN ...` evita disparar trabajo inútil.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p9.png]]
>
> **Se lee así:** la lámina (p. 9) es el **primer caso de negocio real**, y es el que explica para qué sirve un trigger: `CREATE TRIGGER update_limitecredito BEFORE INSERT ON PEDIDOS FOR EACH ROW BEGIN update CLIENTES SET LIMITECREDITO = LIMITECREDITO - new.IMPORTE where CLIENTES.NUMCLIE = new.CLIE; END`.
>
> **Por qué importa:** la regla de negocio es *"cada pedido reduce el límite de crédito del cliente"*, y fíjate en que está escrita **en la base de datos**, no en la aplicación. Eso significa que se cumple **aunque el pedido lo inserte otra aplicación, un script o un usuario a mano**. Esa es la diferencia entre un trigger y una regla en el código.
>
> **Ejemplo:** sin trigger, cualquier programa que inserte en `PEDIDOS` tiene que acordarse de actualizar `CLIENTES.LIMITECREDITO`. Con tres programas distintos, el día que uno de ellos se olvide, el límite queda mal. Con el trigger, la regla está **en un solo sitio** y no se puede olvidar.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p10.png]]
>
> **Se lee así:** la lámina (p. 10) añade la **lógica condicional** dentro del trigger: `CREATE TRIGGER tr1 BEFORE INSERT ON PAYMENTS FOR EACH ROW BEGIN IF new.amount < 100 THEN SET new.amount = new.amount * 0.90; ELSEIF NEW.amount >= 100 THEN SET NEW.amount = 0; END IF; END`.
>
> **Por qué importa:** esta lámina conecta el trigger con la sección de la nota sobre **control de flujo**: dentro del `BEGIN…END` caben `IF`, `ELSEIF`, `ELSE`, variables y bucles. Un trigger no es un `INSERT` simple: es **programación** dentro de la base de datos. Y fíjate en el uso de `SET new.amount = …`: el trigger puede **reescribir** el valor que se va a insertar.
>
> **Ejemplo:** la regla es "los pagos menores de 100 reciben 10% de descuento; los de 100 o más, se anulan (importe 0)". Con `SET new.amount = new.amount * 0.90` el descuento se aplica **sobre el valor nuevo**, así que el `INSERT` guarda el importe ya descontado. Quien haga el `SELECT` después ve el valor final, sin saber que hubo trigger.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p11.png]]
>
> **Se lee así:** la lámina (p. 11) cambia el **momento**: `CREATE TRIGGER tr4 AFTER UPDATE ON PAYMENTS FOR EACH ROW BEGIN IF new.amount < 0 THEN UPDATE customers SET creditLimit = new.amount WHERE customerNumber = new.customerNumber; ELSEIF …`.
>
> **Por qué importa:** aquí el trigger es `AFTER UPDATE`, no `BEFORE INSERT`. La diferencia es **qué información tienes disponible**: en `BEFORE`, el pago todavía no está grabado, así que para actualizar el crédito del cliente tendrías que restar a mano. En `AFTER`, el pago **ya está en la tabla** y puedes leer el saldo real (`SELECT SUM(...)`) en lugar de mantenerlo a mano.
>
> **Ejemplo:** la regla "si el pago actualizado deja el saldo del cliente negativo, ajusta su `creditLimit`" **solo** se puede escribir correctamente con `AFTER UPDATE`: necesitas el saldo ya calculado. Con `BEFORE` tendrías que restar a ciegas.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p12.png]]
>
> **Se lee así:** la lámina (p. 12) es el caso de **recalcular un total**: `CREATE TRIGGER actualizar_promedio after update on payment` que vuelve a sumar los `amount` del cliente y actualiza el `totalcliente`.
>
> **Por qué importa:** este es el patrón clásico de **dato desnormalizado mantido por trigger**. `totalcliente` es un dato que **podría** calcularse con un `SUM`, pero se guarda para no tener que recalcularlo en cada consulta. El trigger es lo que garantiza que ese dato **no se quede viejo**.
>
> **Ejemplo:** la alternativa sin trigger sería un `SELECT SUM(amount) FROM payment WHERE customerNumber = X` en cada consulta que necesite el total. Funciona, pero es caro. La alternativa con trigger guarda el total **ya calculado**, y el `SELECT` es un `SELECT`. El precio es que ahora **dos** datos guardan la misma información, y ambos tienen que mantenerse consistentes.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p13.png]]
>
> **Se lee así:** la lámina (p. 13) es el caso del **trigger con tabla temporal**: `CREATE TRIGGER insertar_promedio after insert on payment` que cuenta los pagos del cliente en una tabla temporal y, si es el primero, inserta el total en `totalcliente`.
>
> **Por qué importa:** esta lámina resuelve el problema del trigger anterior: recalcular el total con un `SUM` en **cada** inserción es caro (el motor recorre todos los pagos del cliente una y otra vez). Con la tabla temporal, el trigger **acumula**: cada pago suma su importe a un acumulado y solo cuando el acumulado es el primero se crea la fila en `totalcliente`.
>
> **Ejemplo:** es el mismo razonamiento que usaste en la **Unidad 2** cuando decidiste guardar los datos calculados para no recalcularlos: la decisión es siempre la misma — *guardar vs. calcular* — y el trigger es el mecanismo que garantiza la consistencia del dato guardado.

> [!info] 📖 El deck de cátedra: los procedimientos almacenados (SQL Avanzado, pp. 14-15)
>
> El deck cierra con el bloque de procedimientos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p14.png]]
>
> **Se lee así:** la lámina (p. 14) define el *Stored Procedure* y, sobre todo, explica **por qué existe**: *"un programa (o procedimiento) el cual es almacenado físicamente en una base de datos"*. Y la ventaja, textualmente: *"al ser ejecutado, en respuesta a una petición de usuario, es ejecutado directamente en el motor de bases de datos, el cual usualmente corre en un servidor separado"*, de modo que *"sólo necesita enviar sus resultados de regreso al usuario, deshaciéndose de la sobrecarga resultante de comunicar grandes cantidades de datos salientes y entrantes"*.
>
> **Por qué importa:** el argumento es de **red**, no de programación. El programa vive **junto a los datos**, así que no tiene que traerlos al cliente para procesarlos ni devolverlos. En una base en las afueras de la ciudad, un `SELECT` de un millón de filas que se procesa en el servidor viaja como **una fila** de resultado.
>
> **Ejemplo:** un reporte que cruza `CUSTOMER`, `PAYMENT` y `RENTAL` y calcula tres totales: si lo escribes en la aplicación, el motor te manda los datos crudos y tú los procesas (si los datos están en otro servidor, el viaje es enorme). Como procedimiento, el motor hace todo el cruce **allá** y te devuelve solo los tres totales.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p15.png]]
>
> **Se lee así:** la lámina (p. 15) es el **ejemplo con parámetros**, y ahí está la diferencia con un trigger: el procedimiento **no se dispara solo**, **se lo invoca**. La firma es `create procedure calcular_iva(in iva decimal(3,2), in valor decimal(5,2), out resultado decimal)` con `select valor*iva into resultado;`, y la invocación es `call calcular_iva(0.14, 100.34, @r);`.
>
> **Por qué importa:** fíjate en los tres tipos de parámetro: `IN` **entra** al procedimiento, `OUT` **sale** de él, y `@r` es la **variable de MySQL** que recibe el resultado. El `INTO resultado` es lo que asigna el valor calculado al parámetro `OUT`. Y fíjate en el `decimal(3,2)`: un parámetro también tiene **tipo y precisión**, igual que una columna.
>
> **Ejemplo:** `call calcular_iva(0.14, 100.34, @r);` deja el 14% de 100.34 en `@r`. Fíjate en que se usa `decimal` y no `float`: **el dinero no se guarda en coma flotante**, y esa regla se aplica igual a los parámetros de un procedimiento. Es el mismo cuidado que con `DECIMAL(10,2)` en la tabla del DDL.
>
> **Por qué importa (trigger vs. procedimiento):** la diferencia final entre los dos es **quién decide cuándo se ejecuta**. El trigger se ejecuta **automáticamente** cuando ocurre el evento; el procedimiento se ejecuta **cuando alguien lo llama** con `CALL`. El trigger es una regla; el procedimiento es una herramienta.

### 7️⃣ Usuarios y permisos (DCL)

> [!note] 📋 Definición — GRANT y REVOKE
>
> | Comando | Qué hace |
> |---|---|
> | `CREATE USER` | Crea un usuario de la base de datos |
> | `GRANT` | Asigna privilegios a un usuario |
> | `REVOKE` | Remueve privilegios asignados |
> | `SHOW GRANTS` | Muestra los permisos de un usuario |
>
> **Ejemplos:**
> - `GRANT SELECT ON sakila.category TO 'fmalo'@'localhost'` — permiso de lectura.
> - `GRANT EXECUTE ON PROCEDURE ...` — permiso para correr un procedimiento, no para ver sus tablas.

> [!example] 🧪 Ejemplo de GRANT por columnas
>
> ```sql
> -- Usuario con SELECT solo de una columna
> GRANT SELECT (name) ON sakila.category TO 'fmalo'@'localhost';
>
> -- Usuario con SELECT, INSERT, DELETE sobre resenas
> GRANT SELECT, INSERT, DELETE ON DBalquiler.resenas TO 'analista_juegos'@'localhost';
>
> -- Permiso para ejecutar un procedimiento
> GRANT EXECUTE ON PROCEDURE DBalquiler.sp_registrar_alquiler TO 'soporte_alquileres'@'localhost';
> ```

> [!warning] ⚠️ GRANT por columnas
>
> Cuando concedes `SELECT (col1, col2)` sobre una tabla, las columnas NO concedidas devuelven "No hay privilegios" al hacer `SELECT *`.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — JOIN múltiple con agregación

> [!example] 📋 Planteamiento
>
> Dadas `departamento(dept_name, ...)` y `instructor(ID, name, dept_name, salary)`, escribe SQL para: "para cada departamento, mostrar nombre y número de instructores, incluyendo departamentos sin instructores".
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT d.dept_name, COUNT(i.ID) AS num_instructores
> > FROM department d
> >   LEFT JOIN instructor i ON d.dept_name = i.dept_name
> > GROUP BY d.dept_name;
> > ```
> >
> > **Por qué:** `LEFT JOIN` conserva departamentos completos; `COUNT(i.ID)` ignora NULLs, así que departamentos sin instructores muestran 0.

### ✏️ Ejercicio 2 — Subconsulta para exclusión

> [!example] 📋 Planteamiento
>
> Dadas `student(ID, name, ...)` y `takes(ID, course_id, ...)`, escribe SQL para: "obtener ID y nombre de estudiantes que NUNCA han tomado un curso".
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > -- Estándar SQL (EXCEPT)
> > SELECT s.ID, s.name FROM student s
> > EXCEPT
> > SELECT t.ID FROM takes t;
> >
> > -- MySQL (sin EXCEPT): NOT EXISTS
> > SELECT ID, name FROM student s
> > WHERE NOT EXISTS (SELECT 1 FROM takes t WHERE t.ID = s.ID);
> > ```

### ✏️ Ejercicio 3 — Vista con GROUP BY y HAVING

> [!example] 📋 Planteamiento
>
> Crea una vista `vProductoMasVendido` que muestre, por sucursal, el producto más vendido (nombre de sucursal, nombre de producto, cantidad), usando subconsultas.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > CREATE VIEW vProductoMasVendido AS
> > SELECT s.nombre AS sucursal, p.nombre AS producto,
> >        (SELECT SUM(dv.cantidad)
> >         FROM detalleventa dv2 JOIN venta v2 ON dv2.venta_id = v2.id
> >         WHERE v2.sucursal_id = v.sucursal_id AND dv2.producto_id = p.producto_id) AS cantidad
> > FROM detalleventa dv
> >   JOIN venta v ON dv.venta_id = v.id
> >   JOIN producto p ON dv.producto_id = p.id
> > WHERE (SELECT SUM(dv3.cantidad) FROM detalleventa dv3 JOIN venta v3 ON dv3.venta_id = v3.id
> >        WHERE v3.sucursal_id = v.sucursal_id AND dv3.producto_id = p.producto_id)
> >       = (SELECT MAX(cant.total) FROM (SELECT v4.sucursal_id AS suc, SUM(dv4.cantidad) AS total
> >                                         FROM detalleventa dv4 JOIN venta v4 ON dv4.venta_id = v4.id
> >                                         GROUP BY v4.sucursal_id) cant
> >            WHERE cant.suc = v.sucursal_id);
> > ```

### ✏️ Ejercicio 4 — Trigger con transacción

> [!example] 📋 Planteamiento
>
> Escribe un procedimiento `sp_registrar_alquiler` que reciba cliente, juego y días; valide que días > 0 y stock > 0; si todo bien, inserte el alquiler y descuente 1 del stock en la misma transacción.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > DELIMITER $$
> > CREATE PROCEDURE sp_registrar_alquiler(
> >   IN p_cliente INT, IN p_juego INT, IN p_dias INT, OUT p_resultado TINYINT
> > )
> > BEGIN
> >   DECLARE v_stock INT;
> >   SET p_resultado = 0;
> >   IF p_dias <= 0 THEN SET p_resultado = 0;
> >   ELSE
> >     START TRANSACTION;
> >       SELECT stock_disponible INTO v_stock FROM videojuegos WHERE id_juego = p_juego FOR UPDATE;
> >       IF v_stock IS NULL OR v_stock <= 0 THEN
> >         ROLLBACK; SET p_resultado = 0;
> >       ELSE
> >         INSERT INTO alquileres (id_cliente, id_juego, fecha_alquiler, dias_alquilados)
> >         VALUES (p_cliente, p_juego, CURDATE(), p_dias);
> >         UPDATE videojuegos SET stock_disponible = stock_disponible - 1 WHERE id_juego = p_juego;
> >         COMMIT; SET p_resultado = 1;
> >       END IF;
> >   END IF;
> > END$$
> > DELIMITER ;
> > ```

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo un JOIN con dos tablas.
> - [ ] Uso GROUP BY con COUNT, SUM, AVG.
> - [ ] Distingo WHERE de HAVING.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Escribo subconsultas correlacionadas y no correlacionadas.
> - [ ] Creo una vista y le asigno permisos.
> - [ ] Leo un plan EXPLAIN y sé cuándo un índice ayuda.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Escribo triggers con SIGNAL para validación.
> - [ ] Diseño procedimientos con transacciones y manejo de errores.
> - [ ] Otorgaré permisos por columna y por procedimiento.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - Diapositivas `SQL Avanzado.pptx` — Vistas, Disparadores y Procedimientos Almacenados (15 láminas).
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 8 — el modelo relacional y el lenguaje SQL.
> - Guía: [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — 17 ejercicios resueltos con JOIN, triggers, vistas, permisos.
> - Diagramas propios: `u4-03-01-graph` (joins y operadores de conjuntos), `u4-03-02-flow` (orden de las cláusulas), `u4-03-03-flow` (subconsulta correlacionada), `u4-03-04-graph` (vistas, índices y triggers).

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿INNER JOIN?::Solo filas que casan en ambas tablas.
> - ¿LEFT JOIN?::Todas las filas de la izquierda, null a la derecha si no casan.
> - ¿GROUP BY?::Agrupa filas por una columna.
> - ¿HAVING?::Filtra grupos (después de GROUP BY); WHERE filtra filas (antes).
> - ¿UNION vs UNION ALL?::UNION quita duplicados; UNION ALL los conserva.
> - ¿Vista?::Consulta guardada con nombre; tabla virtual.
> - ¿Índice compuesto?::Índice sobre varias columnas; el orden importa (prefijo).
> - ¿Trigger?::Se ejecuta automáticamente ante INSERT/UPDATE/DELETE.
> - ¿GRANT por columnas?::Concede SELECT solo de columnas específicas.
> - ¿EXCEPT?::Filas de la primera consulta que no están en la segunda.
> - ¿WHEN antes o después del agrupar?::WHERE filtra filas antes; HAVING filtra grupos después.
> - ¿BEFORE vs AFTER en un trigger?::BEFORE puede cancelar la sentencia; AFTER ya no.
> - ¿Procedimiento almacenado?::Bloque de código guardado en la BD, con parámetros IN/OUT, se invoca con CALL.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[01 - Introducción a SQL]] — qué es SQL, estándares, DDL vs DML vs DCL.
> - [[02 - DDL y DML]] — CREATE TABLE, ALTER, DROP, INSERT, UPDATE, DELETE.
> - [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — 17 ejercicios resueltos con JOIN, triggers, vistas, permisos.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Anterior: [[02 - DDL y DML]]
> - Guía de ejercicios: [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]]

---

**Tags:** #TICG1018 #unidad4 #sql #consultas-avanzadas #join #vista #trigger #bd
