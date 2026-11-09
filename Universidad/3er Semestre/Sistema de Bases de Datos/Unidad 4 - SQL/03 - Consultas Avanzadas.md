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
> **Se lee así:** hay dos familias distintas de "juntar" datos. Los **JOIN** pegan tablas **horizontalmente** (una fila de A se une con una de B, Growing el número de columnas); los **operadores de conjuntos** (`UNION`, `INTERSECT`, `EXCEPT`) apilan resultados **verticalmente** (mismas columnas, filas de una consulta encima de otra). Confundirlos es el error más común de la unidad.

> [!info] 📖 El deck de cátedra: el temario de SQL Avanzado (SQL Avanzado, p. 1)
> El deck que acompaña a esta nota se organiza en tres bloques: vistas, disparadores y procedimientos almacenados.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p1.png]]
> 
> **El temario (p. 1):** *Vistas · Disparadores · Procedimientos Almacenados*. Es el orden del deck y el orden en que aparecen las definiciones más abajo.

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
> El deck define la vista y luego la usa sobre la base de ejemplo.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p2.png]]
> 
> **La definición (p. 2):** `CREATE VIEW nombre_de_vista [columnas] AS <expresion de consulta>`, *"utilizadas para aumentar las posibilidades de acceso a tablas"*, con el ejemplo de la vista `Rojos` sobre `SELECT B.bid, COUNT(*) AS s...`.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p3.png]]
> 
> **Vistas vs tablas (p. 3):** *"parecidas a las tablas, la diferencia es que las vistas son creadas a partir de una consulta"* — no almacenan datos, se calculan.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p4.png]]
> 
> **El ejemplo completo (p. 4):** `create view promedios_clientes as select c.first_name as nombres, c.last_name as apellidos, avg(p.amount) as promedios from customer as c inner join payment as p on c.customer_id = p.customer_id group by c.customer_id;` — una vista con JOIN + `AVG` + `GROUP BY`, exactamente el tipo de consulta que acabas de ver.

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
> El deck dedica nueve láminas a los triggers: qué son, cómo se escriben y cuatro casos reales.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p5.png]]
> 
> **Qué es un trigger (p. 5):** *"procedimiento que se ejecuta cuando se cumple una condición establecida al realizar una operación de inserción (INSERT), actualización (UPDATE) o borrado (DELETE)"*, usado para mejorar la administración...
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p6.png]]
> 
> **Las dos piezas (p. 6):** la **llamada de activación** es la sentencia que dispara el código; la **restricción** es la condición necesaria para ejecutarlo, y puede ser condicional o de otro tipo.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p7.png]]
> 
> **La sintaxis (p. 7):** `trigger_time: BEFORE or AFTER` y `trigger_event: INSERT, UPDATE OR DELETE`, seguidos del `CREATE TRIGGER <nombre> ... ON <tabla>` y del `DELIMITER` que delimita el bloque.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p8.png]]
> 
> **Un trigger de ejemplo (p. 8):** `CREATE TRIGGER testref BEFORE INSERT ON test1 FOR EACH ROW BEGIN INSERT INTO test2 ...; DELETE FROM test3 ...; UPDATE test4 ...; END` — un solo disparo, varias acciones.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p9.png]]
> 
> **Trigger de negocio (p. 9):** `CREATE TRIGGER update_limitecredito BEFORE INSERT ON PEDIDOS` que descuenta `new.IMPORTE` del `LIMITECREDITO` del cliente: la regla de negocio vive en la base de datos, no en la aplicación.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p10.png]]
> 
> **Trigger con IF/ELSEIF (p. 10):** `CREATE TRIGGER tr1 BEFORE INSERT ON PAYMENTS` que aplica un 10% de descuento si `new.amount < 100` y pone el importe en 0 si es mayor o igual.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p11.png]]
> 
> **Trigger AFTER UPDATE (p. 11):** `CREATE TRIGGER tr4 AFTER UPDATE ON PAYMENTS` que propaga el nuevo saldo al `creditLimit` del cliente.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p12.png]]
> 
> **Recalcular un total (p. 12):** `CREATE TRIGGER actualizar_promedio after update on payment` que vuelve a sumar `amount` del cliente y actualiza `totalcliente`.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p13.png]]
> 
> **Trigger con tabla temporal (p. 13):** `CREATE TRIGGER insertar_promedio after insert on payment` que cuenta los pagos del cliente en una tabla temporal y, si es el primero, inserta el total en `totalcliente`.

> [!info] 📖 El deck de cátedra: los procedimientos almacenados (SQL Avanzado, pp. 14-15)
> El deck cierra con el bloque de procedimientos.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p14.png]]
> 
> **Qué es un Stored Procedure (p. 14):** *"un programa (o procedimiento) el cual es almacenado físicamente en una base de datos"*. La ventaja: se ejecuta **directamente en el motor**, *"el cual usualmente corre en un servidor separado"*, así que *"solo necesita enviar sus resultados de regreso al usuario, deshaciéndose de la sobrecarga resultante de comunicar grandes cantidades de datos salientes y entrantes"*.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-sql-avanzado-p15.png]]
> 
> **El ejemplo con parámetros (p. 15):** `create procedure calcular_iva(in iva decimal(3,2), in valor decimal(5,2), out resultado decimal)` con `select valor*iva into resultado;`, invocada como `call calcular_iva(0.14, 100.34, @r);` — el `IN` entra, el `OUT` sale, y `@r` es la variable que lo recibe.

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
