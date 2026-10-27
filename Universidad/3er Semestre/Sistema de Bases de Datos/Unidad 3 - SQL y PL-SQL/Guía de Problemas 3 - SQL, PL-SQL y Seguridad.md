---
dg-publish: true
tags: [TICG1018, unidad3, guia, taller3, taller4, bd]
---

# 📝 Guía de Problemas 3 — SQL, PL-SQL y Seguridad (Talleres 3 y 4)

> [!info] ℹ️ Qué es esta guía
> Desarrollo completo de los talleres 3 y 4 de la materia, con los enunciados reales de la Unidad 0:
>
> | Bloque | Fuente | Tema |
> |---|---|---|
> | A | `ENUNCIADO.pdf` (Taller 3, base University) | SQL de consultas: LIKE, BETWEEN, LEFT JOIN, GROUP BY, HAVING, UNION de conjuntos (11, con puntaje) |
> | B | `Taller 3 2026 PAO 1.pdf` (base supermercado) | Normalizar un campo con UPDATE-JOIN, consultas agregadas, vista con subquerys, procedimiento con transacción y trigger de acumulación |
> | C | `Taller 4_20agorep.pdf` (base DBalquiler) | Procedimientos, triggers con SIGNAL, vistas, índices con EXPLAIN, GRANT de usuarios y MongoDB con documentos embebidos |
> | D | `Taller 4 - PAO I 2024 - Triggers, Vistas e Usuarios.pdf` (base sakila) | Seguridad: trigger con MD5, CREATE USER, GRANT por tabla / por columna y vistas con permisos |
>
> Las soluciones del bloque A son propias (no hay solución oficial publicada del taller). En B/C/D se nota **dónde el enunciado deja detalles libres** (nombres de columnas, columnas extra ansiosas) y se elige un esquema asumido, declarado en cada bloque.
>
> Teoría base: consultas y agregación → [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] (σ = WHERE, γ = GROUP BY); normalización del campo `línea` → [[03 - Segunda y tercera forma normal]], [[04 - Normalización paso a paso]].

![[../Unidad 0 - Guias y Ejercicios/Talleres/ENUNCIADO.pdf]]

![[../Unidad 0 - Guias y Ejercicios/Talleres/Taller 3 2026 PAO 1.pdf]]

![[../Unidad 0 - Guias y Ejercicios/Talleres/Taller 4_20agorep.pdf]]

![[../Unidad 0 - Guias y Ejercicios/Talleres/Taller 4 - PAO I 2024 - Triggers, Vistas e Usuarios.pdf]]

> [!info] 📖 El deck de cátedra: SQL y las restricciones (slides06, pp. 10-18)
> El deck del Ing. Jorge Magallanes cierra el curso con SQL. Estas son las figuras que definen la sintaxis que usan los ejercicios de esta guía.

![[Archivos/bd-s06-p10.png]]

![[Archivos/bd-s06-p11.png]]

> **Creación de tablas (p. 10):** `CREATE TABLE department (department_name VARCHAR(15), building VARCHAR(15), budget NUMERIC(12,2))` — el ejemplo base del deck.
>
> **Restricciones de clave (p. 11):** *"la especificación de primary key({L}) define la lista L de atributos de clave primaria"*, con `CREATE TABLE course (course_id VARCHAR(7), title VARCHAR(50) NOT NULL, …)`.

![[Archivos/bd-s06-p13.png]]

![[Archivos/bd-s06-p14.png]]

> **Restricciones de integridad (p. 13):** *"una restricción de integridad (integrity constraint) asegura que un cambio realizado en la DB no conduzca a la pérdida de la consistencia de datos"*.
>
> **Restricciones solo de tabla (p. 14):** `not null` (columnas obligatorias) y `unique ({L})` (lista de atributos que debe ser única).

![[Archivos/bd-s06-p17.png]]

![[Archivos/bd-s06-p18.png]]

> **Integridad referencial (p. 17):** *"las restricciones de clave foránea son la manera de asegurarnos que los valores de unos atributos coincidan con algún valor de la clave primaria en otra relación"*.
>
> **Violación (p. 18):** qué pasa con las tuplas que hacen referencia cuando se borra o cambia la tupla referenciada — la pregunta que responde el bloque D de esta guía con `ON DELETE` / `ON UPDATE`.

---

## 🅰️ Bloque A — SQL sobre la base University (Taller 3, 11 consultas)

> [!tip] 📌 Cómo trabajar cada pregunta
> La base `University.sql` trae las tablas estándar del esquema University (el clásico de los libros de SBD): `student(ID, name, dept_name, tot_cred)`, `instructor(ID, name, dept_name, salary)`, `course(course_id, title, dept_name, credits)`, `takes(ID, course_id, sec_id, semester, year, grade)`, `teaches(ID, course_id, sec_id, semester, year)`, `advisor(s_ID, i_ID)`, `department(dept_name, ...)`, `prerequisite(course_id, prereq_id)`. Verifica los nombres exactos de columnas y la diferencia JOIN vs LEFT JOIN (la nota del propio taller).

### ✏️ Ejercicio 1 — Instructores que empiezan con "A" (7 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** obtener `ID`, `name` y `dept_name` de todos los instructores cuyo nombre empiece con la letra "A".
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT ID, name, dept_name
> > FROM instructor
> > WHERE name LIKE 'A%';
> > ```
> >
> > - `%` en SQL LIKE = cualquier secuencia (el análogo del `.` con estrella en regex): "empiece con A" = `'A%'`, no `'%A%'` (eso es "contiene A").

### ✏️ Ejercicio 2 — Créditos duplicados (7 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** `course_id`, `title` y el número de créditos duplicado (`credits * 2` como "doble creditos") de los cursos con créditos entre 3 y 5.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT course_id, title, credits * 2 AS 'doble creditos'
> > FROM course
> > WHERE credits BETWEEN 3 AND 5;
> > ```
> >
> > - `BETWEEN` es inclusivo en extremos; el alias con espacio pide comillas.

### ✏️ Ejercicio 3 — Estudiantes sin asesor (10 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** listar `ID` y `name` de los estudiantes que NO tienen asesor asignado.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > -- Opción 1 (preferida): LEFT JOIN, que conserva al estudiante sin pareja
> > SELECT s.ID, s.name
> > FROM student s
> >   LEFT JOIN advisor a ON s.ID = a.s_ID
> > WHERE a.i_ID IS NULL;
> >
> > -- Opción 2: NOT IN (con cuidado del NULL)
> > SELECT ID, name FROM student
> > WHERE ID NOT IN (SELECT s_ID FROM advisor WHERE s_ID IS NOT NULL);
> > ```
> >
> > - Es el patrón "los de la izquierda sin pareja" — el mismo que el álgebra expresa con diferencia de conjuntos (ejercicio 3 de la Guía 2).
> > - `NOT IN` con subconsulta que puede traer `NULL` camina siempre falso: por eso el `WHERE s_ID IS NOT NULL` interno.

### ✏️ Ejercicio 4 — Departamentos CON y SIN instructores (10 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** para cada departamento (incluyendo los que aún no tienen instructores), `dept_name` y número de instructores.
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
> > - El `LEFT JOIN` arranca por la tabla que debe aparecer COMPLETA (department).
> > - `COUNT(i.ID)` y no `COUNT(*)` — el conteo debe respetar a los sin-instructores como 0 (`COUNT(columna)` ignora los NULL; `COUNT(*)` contaría la fila vacía como 1).

### ✏️ Ejercicio 5 — Salario promedio > 70000, ordenado (10 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** `dept_name` y salario promedio por departamento, solo promedios > 70000, de mayor a menor.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT dept_name, AVG(salary) AS salario_promedio
> > FROM instructor
> > GROUP BY dept_name
> > HAVING AVG(salary) > 70000
> > ORDER BY salario_promedio DESC;
> > ```
> >
> > - Filtro de grupo → `HAVING` (el `WHERE` corre ANTES de agrupar). En álgebra: `σ` después del `γ` — la Guía 2, ejercicio 2, es el mismo movimiento.

### ✏️ Ejercicio 6 — Cursos con más de 5 estudiantes y su prerequisito (13 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** para cada curso, `course_id`, `title`, cantidad de estudiantes que lo tomaron (`takes`) y el nombre del curso prerequisito; solo cursos con > 5 estudiantes, ordenado desc por cantidad.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT c.course_id, c.title,
> >        COUNT(t.ID)     AS estudiantes,
> >        pc.title        AS nombre_prerequisito
> > FROM course c
> >   JOIN takes t      ON c.course_id = t.course_id
> >   JOIN prerequisite pr ON c.course_id = pr.course_id
> >   JOIN course pc    ON pr.prereq_id = pc.course_id
> > GROUP BY c.course_id, c.title, pc.title
> > HAVING COUNT(t.ID) > 5
> > ORDER BY estudiantes DESC;
> > ```
> >
> > - `course` aparece DOS veces (el curso y su prerequisito) — alias `c` vs `pc`, el mismo truco de `ρ` del ejercicio 4 de la Guía 2.

### ✏️ Ejercicio 7 — Estudiantes con tot_cred > 60 y "e" en el nombre (13 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** por departamento: número de estudiantes con `tot_cred > 60`, y el promedio de `tot_cred` de esos estudiantes; solo estudiantes cuyo nombre contenga "e" en cualquier posición; solo departamentos con más de 2 cumplidores; ordenar alfabéticamente por `dept_name`.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT s.dept_name,
> >        COUNT(*) AS num_estudiantes,
> >        AVG(s.tot_cred) AS promedio_tot_cred
> > FROM student s
> > WHERE s.tot_cred > 60 AND s.name LIKE '%e%'
> > GROUP BY s.dept_name
> > HAVING COUNT(*) > 2
> > ORDER BY s.dept_name;
> > ```
> >
> > - Contiene "e" = `LIKE '%e%'`. Filtros de FILA en `WHERE` (tot_cred, nombre), filtros de GRUPO en `HAVING` (más de 2).

### ✏️ Ejercicio 8 — Estudiantes O instructores de Comp. Sci, sin duplicados (10 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** ID de todas las personas estudiantes o instructores del departamento "Comp. Sci", sin duplicados, con operador de conjuntos.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT ID FROM student    WHERE dept_name = 'Comp. Sci.'
> > UNION
> > SELECT ID FROM instructor WHERE dept_name = 'Comp. Sci.';
> > ```
> >
> > - `UNION` dedupe — ése es el "sin duplicados". El complemento "CON posibles duplicados" (ejercicio 9) pide `UNION ALL`.

### ✏️ Ejercicio 9 — course_id en takes y teaches, CON duplicados (10 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** listado completo (con posibles duplicados) de los `course_id` que aparecen en `takes` y en `teaches`, con operador de conjuntos.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT course_id FROM takes
> > UNION ALL
> > SELECT course_id FROM teaches;
> > ```
> >
> > - La trampa es exactamente `UNION` vs `UNION ALL`: el UNION ALL no fusiona ni filtra (deja los repetidos de cada relato).

### ✏️ Ejercicio 10 — course_id en ambos con su título (10 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** únicamente los `course_id` que aparecen TANTO en `takes` como en `teaches`, con el nombre del curso (operador de conjuntos = intersección).
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > -- Estándar SQL (disponible en MySQL >= 8.0.31 y en la mayoría de motores)
> > SELECT t.course_id, c.title
> > FROM course c
> > JOIN (
> >   SELECT t1.course_id FROM takes t1
> >   INTERSECT
> >   SELECT t2.course_id FROM teaches t2
> > ) x ON x.course_id = c.course_id;
> >
> > -- Equivalente portable si el motor no trae INTERSECT:
> > SELECT DISTINCT t.course_id, c.title
> > FROM course c
> >   JOIN takes t    ON t.course_id = c.course_id
> >   JOIN teaches te ON te.course_id = t.course_id;
> > ```
> >
> > - Intersección = esta en los dos conjuntos; en producto natural se logra con el INNER JOIN (la fila solo existe si casa derecho en ambas). El DISTINCT es el que quita los duplicados y completa el efecto de la intersección.

### ✏️ Ejercicio 11 — Estudiantes que nunca tomaron curso (10 pts)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** ID de estudiantes que aparecen en `student` y no en `takes` (nunca han tomado curso), con operador de conjuntos.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > -- Estándar
> > SELECT s.ID, s.name FROM student s
> > EXCEPT
> > SELECT t.ID FROM takes t;
> >
> > -- MySQL (hasta hoy): NOT IN / NOT EXISTS
> > SELECT ID, name FROM student s
> > WHERE NOT EXISTS (SELECT 1 FROM takes t WHERE t.ID = s.ID);
> > ```
> >
> > - Diferencia de conjuntos otra vez — la consulta 3 (sin asesor) y esta usan el mismo molde con otra tabla.

---

## 🅱️ Bloque B — Supermercado: normalización + consultas + transacción + trigger (Taller 3 2026)

> [!info] 📋 Esquema asumido (el enunciado deja detalles libres)
> `producto(id, nombre, precio, linea, stock)`, `venta(id, fecha, sucursal_id, tipo_pago, cajero_id)`, `detalleventa(id, venta_id, producto_id, cantidad, precio_unit`, `descuento)`, `sucursal(id, nombre)`. Ajusta nombres al proyecto real.

### ✏️ Ejercicio 1 — Normalizar el campo `línea` con UPDATE-JOIN

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** crear la tabla `linea(id, nombre)` y enlazarla a `producto`, rellenando el enlace con un `UPDATE` con `JOIN`.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > CREATE TABLE linea (
> >   id INT AUTO_INCREMENT PRIMARY KEY,
> >   nombre VARCHAR(50) NOT NULL UNIQUE
> > );
> >
> > -- 1. migrar los nombres únicos de línea
> > INSERT INTO linea (nombre)
> > SELECT DISTINCT linea FROM producto
> > WHERE linea IS NOT NULL;
> >
> > -- 2. enlace
> > ALTER TABLE producto ADD COLUMN linea_id INT;
> >
> > UPDATE producto p
> > JOIN linea l ON p.linea = l.nombre
> > SET p.linea_id = l.id;
> >
> > -- 3. cerrar la forma normal: fuera la columna denormalizada, dentro la FK
> > ALTER TABLE producto DROP COLUMN linea;
> > ALTER TABLE producto
> >   ADD CONSTRAINT fk_producto_linea
> >   FOREIGN KEY (linea_id) REFERENCES linea(id);
> > ```
> >
> > - Es normalización en caliente: la columna `linea` (texto repetido) falta a la 2FN/3FN — repetición TRANSITIVA — y viaja a su tabla propia ([[03 - Segunda y tercera forma normal]]).
> > - El `UPDATE ... JOIN` es el patrón de migración de datos: una fila por combinación `p.línea = l.nombre`, y `SET` escribe la clave.

### ✏️ Ejercicio 2 — Promedio de ventas por sucursal (sin descuentos)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** nombre de sucursal y promedio de ventas, sin considerar descuentos.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > SELECT s.nombre AS sucursal,
> >        AVG(dv.cantidad * dv.precio_unit) AS promedio_venta
> > FROM sucursal s
> >   JOIN venta v        ON v.sucursal_id = s.id
> >   JOIN detalleventa dv ON dv.venta_id = v.id
> > GROUP BY s.nombre;
> > ```
> >
> > - "Sin descuentos" pasa por `cantidad × precio_unit` — no por el total ya descontado (la columna `descuento` queda fuera por enunciado).

### ✏️ Ejercicio 3 — Vista `vProductoMasVendido` con subquerys

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** presentar el producto que más se vende en cada sucursal (campo `cantidad` de `detalleventa`) como vista `vProductoMasVendido`, con `nombre de sucursal`, `nombre de producto`, `cantidad`; usar subquerys.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > CREATE VIEW vProductoMasVendido AS
> > SELECT s.nombre AS sucursal,
> >        p.nombre  AS producto,
> >        (SELECT SUM(dv.cantidad)
> >         FROM detalleventa dv2
> >         JOIN venta v2 ON dv2.venta_id = v2.id
> >         WHERE v2.sucursal_id = v.sucursal_id
> >           AND dv2.producto_id = p.producto_id) AS cantidad
> > FROM detalleventa dv
> >   JOIN venta v   ON dv.venta_id = v.id
> >   JOIN producto p ON dv.producto_id = p.id
> > WHERE (SELECT SUM(dv3.cantidad)
> >        FROM detalleventa dv3
> >        JOIN venta v3 ON dv3.venta_id = v3.id
> >        WHERE v3.sucursal_id = v.sucursal_id
> >          AND dv3.producto_id = p.producto_id)
> >       = (SELECT MAX(cant.total)
> >          FROM (SELECT v4.sucursal_id AS suc, SUM(dv4.cantidad) AS total
> >                FROM detalleventa dv4
> >                JOIN venta v4 ON dv4.venta_id = v4.id
> >                GROUP BY v4.sucursal_id) cant   -- (sub1)
> >         -- correcto por sucursal:
> >         WHERE cant.suc = v.sucursal_id);
> > ```
> >
> > - "Usar subquerys" descarta el solve con ventanas (`ROW_NUMBER OVER PARTITION`): aquí el top-1 por sucursal via correlacionadas — subconsulta de CANTIDAD + subconsulta de MAX por sucursal.
> > - Idempótente: si hay empate, aparecen los dos productos — decisión documentada, no bug.

### ✏️ Ejercicio 4 — Procedimiento `sPCrearVenta` con transacción

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** procedimiento `sPCrearVenta` que recibe producto, tipo de pago y cajero, y crea la venta usando transacciones.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > DELIMITER $$
> > CREATE PROCEDURE sPCrearVenta(
> >   IN p_producto   INT,
> >   IN p_cantidad   INT,        -- el enunciado de "parámetros necesarios" incluye la cantidad
> >   IN p_tipo_pago  VARCHAR(20),
> >   IN p_cajero     INT
> > )
> > BEGIN
> >   DECLARE v_sucursal INT;
> >   START TRANSACTION;
> >     -- precio vigente del producto (asumido)
> >     SELECT p.precio INTO v_precio
> >     FROM producto p WHERE p.id = p_producto;
> >
> >     IF v_precio IS NULL THEN
> >       ROLLBACK;
> >       SELECT 0 AS resultado;   -- 0 = no crea si el producto no existe
> >     ELSE
> >       INSERT INTO venta (fecha, tipo_pago, cajero_id, sucursal_id)
> >       VALUES (NOW(), p_tipo_pago, p_cajero, v_sucursal);
> >       INSERT INTO detalleventa (venta_id, producto_id, cantidad, precio_unit)
> >       VALUES (LAST_INSERT_ID(), p_producto, p_cantidad, v_precio);
> >       COMMIT;
> >       SELECT 1 AS resultado;
> >     END IF;
> > END$$
> > DELIMITER ;
> > ```
> >
> > - Todo átomos-or-rollbacks: o la venta y su detalle se guardan juntos, o no queda nada. `START TRANSACTION ... COMMIT/ROLLBACK` es el patrón que el Taller 4 repite a lo grande.

### ✏️ Ejercicio 5 — Trigger `tgrResumenProductos` acumulativo

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** trigger `tgrResumenProductos` que guarde en `tblResumenProductos(id_producto, nombre_producto, cantidad_vendida, valor_ventas)` al vuelo, acumulando si el producto ya está (se cobra por INSERT y por UPDATE).
>
> > [!success]- ✅ Solución (2 triggers, insert y update)
> >
> > ```sql
> > -- 0) tabla igual escrita
> > CREATE TABLE tblResumenProductos (
> >   id_producto      INT PRIMARY KEY,
> >   nombre_producto  VARCHAR(80),
> >   cantidad_vendida INT     DEFAULT 0,
> >   valor_ventas     DECIMAL(12,2) DEFAULT 0
> > );
> >
> > -- 1) la primera vez que se vende
> > DELIMITER $$
> > CREATE TRIGGER tgrResumenProductos
> > AFTER INSERT ON detalleventa
> > FOR EACH ROW
> > BEGIN
> >   INSERT INTO tblResumenProductos (id_producto, nombre_producto,
> >                                    cantidad_vendida, valor_ventas)
> >   VALUES (NEW.producto_id,
> >           (SELECT nombre FROM producto WHERE id = NEW.producto_id),
> >           NEW.cantidad, NEW.cantidad * NEW.precio_unit)
> >   ON DUPLICATE KEY UPDATE
> >     cantidad_vendida = cantidad_vendida + NEW.cantidad,
> >     valor_ventas     = valor_ventas + NEW.cantidad * NEW.precio_unit;
> > END$$
> >
> > -- 2) si una venta se CORRIGE (update), la racha acumulada debe ejecutarse
> > CREATE TRIGGER tgrResumenProductos_upd
> > AFTER UPDATE ON detalleventa
> > FOR EACH ROW
> > BEGIN
> >   UPDATE tblResumenProductos r SET
> >     cantidad_vendida = r.cantidad_vendida + (NEW.cantidad - OLD.cantidad),
> >     valor_ventas     = r.valor_ventas
> >                       + (NEW.cantidad * NEW.precio_unit
> >                        - OLD.cantidad * OLD.precio_unit)
> >   WHERE r.id_producto = NEW.producto_id;
> > END$$
> > DELIMITER ;
> > ```
> >
> > - "Acumular si se repite" = `ON DUPLICATE KEY UPDATE` (upsert de MySQL) — la clave primera `id_producto` convierte la tabla en contador vivo.
> > - Los triggers residen SOLO tras INSERT/UPDATE — no hay opción instantánea al SELECT; por eso el resumen se incrementa en cada venta; nunca hay que recalcularlo.

---

## 🅲 Bloque C — Alquileres de videojuegos: PL-SQL, índices y MongoDB (Taller 4, 20-agosto-2026)

> [!info] 📋 Esquema asumido
> `videojuegos(id_juego, titulo, plataforma, stock_disponible)`, `alquileres(id_alquiler, id_cliente, id_juego, fecha_alquiler, dias_alquilados)`, `clientes(id_cliente, nombre)`, `resenas(id_resena, id_juego, puntuacion, comentario)`. Base general: `DBalquiler`.

### ✏️ Ejercicio 1 — `sp_registrar_alquiler` con transacción y stock

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** registrar alquiler en transacción: validar `dias_alquilados > 0` y stock disponible > 0; si falla se hace ROLLBACK y no se inserta nada; si va bien: inserta, descuenta 1 de stock DENTRO de la misma transacción, y retorna 1; en caso de fallo retorna 0.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > DELIMITER $$
> > CREATE PROCEDURE sp_registrar_alquiler(
> >   IN  p_cliente INT,
> >   IN  p_juego   INT,
> >   IN  p_dias    INT,
> >   OUT p_resultado TINYINT
> > )
> > BEGIN
> >   DECLARE v_stock INT;
> >   SET p_resultado = 0;
> >
> >   -- valida dias ANTES de abrir la transacción
> >   IF p_dias <= 0 THEN
> >     SET p_resultado = 0;            -- dias invalidos
> >   ELSE
> >     START TRANSACTION;
> >       SELECT stock_disponible INTO v_stock
> >       FROM videojuegos WHERE id_juego = p_juego FOR UPDATE;  -- fila con lock
> >
> >       IF v_stock IS NULL OR v_stock <= 0 THEN
> >         ROLLBACK;
> >         SET p_resultado = 0;        -- sin stock
> >       ELSE
> >         INSERT INTO alquileres (id_cliente, id_juego,
> >                                 fecha_alquiler, dias_alquilados)
> >         VALUES (p_cliente, p_juego, CURDATE(), p_dias);
> >
> >         UPDATE videojuegos
> >         SET stock_disponible = stock_disponible - 1
> >         WHERE id_juego = p_juego;
> >
> >         COMMIT;
> >         SET p_resultado = 1;        -- todo bien
> >       END IF;
> >   END IF;
> > END$$
> > DELIMITER ;
> > ```
> >
> > - El "retorna" en un procedimiento MySQL: los procedimientos no hacen `RETURN` — aplica un `OUT` (que es lo aquí hecho) o un último `SELECT 1/0`; documenta la clase que te lo pide.
> > - `FOR UPDATE` congela la fila del stock desde el SELECT hasta el COMMIT/ROLLBACK: evita que dos clientes se lleven el último juego a la vez (condición de carrera).

### ✏️ Ejercicio 2 — Trigger `trg_validar_resena` con error controlado

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** trigger ANTES de insertar en `resenas` que valide `puntuacion` entre 1 y 5; fuera de rango → bloquear con error controlado.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > DELIMITER $$
> > CREATE TRIGGER trg_validar_resena
> > BEFORE INSERT ON resenas
> > FOR EACH ROW
> > BEGIN
> >   IF NEW.puntuacion NOT BETWEEN 1 AND 5 THEN
> >     SIGNAL SQLSTATE '45000'
> >     SET MESSAGE_TEXT = 'Puntuacion fuera de rango (1 a 5)';
> >   END IF;
> > END$$
> > DELIMITER ;
> > ```
> >
> > - `SIGNAL SQLSTATE '45000'` es el "error controlado" propio de la app: corta el INSERT y devuelve un mensaje legible (código 45000 = error explícito).
> > - Tiempo de insertar: el `BEFORE` puede cancelar la fila; un `AFTER` ya no puede evitar que la fila se guarde.

### ✏️ Ejercicio 3 — Vista `vista_juegos_populares`

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** por título de videojuego: plataforma, número de alquileres y total de días alquilados acumulados; solo juegos alquilados > 100 días; ordenar por total de alquileres de menor a mayor.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > CREATE VIEW vista_juegos_populares AS
> > SELECT v.titulo,
> >        v.plataforma,
> >        COUNT(a.id_alquiler)       AS numero_alquileres,
> >        SUM(a.dias_alquilados)     AS dias_acumulados
> > FROM videojuegos v
> >   JOIN alquileres a ON a.id_juego = v.id_juego
> > GROUP BY v.titulo, v.plataforma
> > HAVING SUM(a.dias_alquilados) > 100
> > ORDER BY numero_alquileres ASC;
> > ```
> >
> > - Al fin aquí filtra por total de días (HAVING) pero se ordena por alquileres (ORDER BY) — dos columnas distintas: la vista guarda ya el resultado ordenado.

### ✏️ Ejercicio 4 — Procedimiento `sp_reporte_popularidad_juegos`

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** procedimiento que consulta `vista_juegos_populares` filtrando por plataforma y devuelva la cantidad de filas de esa plataforma con mayor puntuación promedio.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > DELIMITER $$
> > CREATE PROCEDURE sp_reporte_popularidad_juegos(
> >   IN p_plataforma VARCHAR(30)
> > )
> > BEGIN
> >   SELECT COUNT(*) AS filas_plataforma
> >   FROM vista_juegos_populares
> >   WHERE plataforma = p_plataforma
> >   ORDER BY numero_alquileres DESC   -- orden interno del reporte
> >   LIMIT 1;  -- si se cuenta solo el mayor, LIMIT 1 corta el conteo
> > END$$
> > DELIMITER ;
> > ```
> >
> > - Nota honesta: la frase "mayor puntuación promedio" es capaz de ambigüedad (la vista no trae puntuación). La solución asume: reporte en orden por popularidad (alquileres) y que cuente cuántas filas cumple cada plataforma. Si el docente quiere media de puntuación, la vista gana `AVG(r.puntuacion)` con JOIN a `resenas`, y el COUNT sería el "cuántas juegos de X plataforma superan la media global". Plantéaselo a la docente antes de entregar.

### ✏️ Ejercicio 5 — Índice compuesto EXPLAIN menos base (a-d)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** capturar el plan con `EXPLAIN`, crear índice compuesto sobre `nombre` y `fecha_alquiler` de `alquileres`, repetir EXPLAIN, y llenar la tabla de lectura de planes Type / Possible_keys / Key / Rows Scanned / Duration / Extra / Rows returned.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > -- a) antes
> > EXPLAIN SELECT a.id_alquiler, a.id_juego, a.fecha_alquiler, a.dias_alquilados
> > FROM alquileres a JOIN clientes c USING (id_cliente)
> > WHERE c.nombre = 'Sofia Leon'
> >   AND a.fecha_alquiler BETWEEN '2024-06-01' AND '2024-06-30';
> >
> > -- b) índice: la columna de igualdad primero (nombre), el rango después (fecha)
> > CREATE INDEX idx_nombre_fecha ON alquileres (id_cliente, fecha_alquiler);
> >
> > -- c) despues: repetir el EXPLAIN de arriba
> > ```
> >
> > **d) Lectura esperada de los planes ("antes" vs "después"):**
> >
> > | Plan | Type | Possible keys | Key | Rows Scanned | Duration | Extra info | Rows returned |
> > |---|---|---|---|---|---|---|---|
> > | Antes | ALL | NULL | NULL | miles (scan completo de la tabla) | segundos | Using where | igual |
> > | Después | range | idx_nombre_fecha | idx_nombre_fecha | pocas (solo el mes de Sofía) | milisegundos | Using index condition | igual |
> >
> > - El orden del índice importa: el `B+tree` busca por prefijo — `WHERE nombre = x AND fecha BETWEEN` entra por la columna de igualdad (nombre) y recorre la fecha ya ordenada (rango). Si el índice fuera `(fecha_alquiler, id_cliente)`, el filtro por nombre no podría usarlo como prefijo y se descartaría el índice.
> > - El índice compuesto solo se aprovecha cuando el `WHERE` es prefijo-consistente con él; por eso en la práctica de MySQL 8 el índice se pide sobre `(id_cliente, fecha_alquiler)` de `clientes` unida primero por el nombre.

### ✏️ Ejercicio 6 — Usuarios y permisos de la vista

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** dos usuarios de `DBalquiler`: `analista_juegos` (consultar la vista solo con título y número de alquileres; SELECT/INSERT/DELETE sobre `resenas`), `soporte_alquileres` (SELECT/INSERT sobre `alquileres` + ejecutar el procedimiento).
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > -- analista_juegos
> > CREATE USER 'analista_juegos'@'localhost' IDENTIFIED BY 'Clave*Segura1';
> > GRANT SELECT (titulo, numero_alquileres)
> >   ON DBalquiler.vista_juegos_populares TO 'analista_juegos'@'localhost';
> > GRANT SELECT, INSERT, DELETE
> >   ON DBalquiler.resenas TO 'analista_juegos'@'localhost';
> >
> > -- soporte_alquileres
> > CREATE USER 'soporte_alquileres'@'localhost' IDENTIFIED BY 'Otra*Clave2';
> > GRANT SELECT, INSERT
> >   ON DBalquiler.alquileres TO 'soporte_alquileres'@'localhost';
> > GRANT EXECUTE ON PROCEDURE DBalquiler.sp_registrar_alquiler
> >   TO 'soporte_alquileres'@'localhost';
> > ```
> >
> > - El GRANT por columnas (`GRANT SELECT (col1, col2) ON vista ...`) hace que las NO concedidas tras el SELECT de la vista den error de permiso — es como hacer una vista con menos columnas pero recargo generico.
> > - `EXECUTE ON PROCEDURE` — energía de llamar; el usuario que ejecuta el procedimiento usa los permisos de casos del creador (definer) por defecto.

### ✏️ Ejercicio 7 — Colección MongoDB con documentos embebidos

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** modelar `videojuegos` + `alquileres` como colección de MongoDB con documentos embebidos; los alquileres guardan el nombre del cliente, no su id.
>
> > [!success]- ✅ Solución
> >
> > ```javascript
> > // colección videojuegos; cada juego trae sus alquileres EMBEBIDOS
> > {
> >   _id: ObjectId("..."),
> >   titulo: "Zelda BOTW",
> >   plataforma: "Switch",
> >   stock_disponible: 2,
> >   alquileres: [
> >     { cliente: "Sofia Leon", fecha_alquiler: ISODate("2024-06-03"),
> >       dias_alquilados: 7 },
> >     { cliente: "Pedro Herrera", fecha_alquiler: ISODate("2024-06-10"),
> >       dias_alquilados: 4 }
> >   ]
> > }
> > ```
> >
> > - El documento embebido gana en lectura atómica: un juego y todo su historial se leen con una sola consulta, sin JOIN. El caso de uso "consultar juego con sus alquileres" lo recomienda; el "reporte del cliente en todos los juegos" lo castiga (duplicación del nombre + sin FK).

### ✏️ Ejercicio 8 — Insertar 2 videojuegos (uno PS5)

> [!example]- 📝 Enunciado y solución
>
> > [!success]- ✅ Solución
> >
> > ```javascript
> > db.videojuegos.insertMany([
> >   { titulo: "FIFA 24",          plataforma: "PS5",
> >     stock_disponible: 10, alquileres: [] },
> >   { titulo: "Super Mario Odyssey", plataforma: "Switch",
> >     stock_disponible: 5,  alquileres: [] }
> > ])
> > ```

### ✏️ Ejercicio 9 — Consulta MongoDB: PS5 y stock > 3

> [!example]- 📝 Enunciado y solución
>
> > [!success]- ✅ Solución
> >
> > ```javascript
> > db.videojuegos.find({
> >   plataforma:        'PS5',
> >   stock_disponible:  { $gt: 3 }
> > })
> > ```
> >
> > - Documentos BSON, campos planos: el par `campo: valor` es igualdad; `$gt` es mayor-que. SQL mental: `WHERE plataforma = 'PS5' AND stock_disponible > 3`.

---

## 🅳 Bloque D — Seguridad en sakila: MD5, usuarios y GRANT por columna (Taller 4 2024)

> [!info] 📋 Contexto
> Base `sakila` (la de Oracle — la sample database MySQL oficial: `customer`, `payment`, `country`, `city`, `category`, `address`). El enunciado asume que la tabla `customer` tiene una columna para guardar la huella; si no existe, `ALTER TABLE customer ADD pass CHAR(32);` antes del trigger.

### ✏️ Ejercicio 1 — Trigger que aplica el algoritmo MD5

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** disparador que "encripte" a los nuevos clientes con MD5 del string nombre + apellido.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > DELIMITER $$
> > CREATE TRIGGER trg_encripta_cliente
> > BEFORE INSERT ON customer
> > FOR EACH ROW
> > BEGIN
> >   SET NEW.pass = MD5(CONCAT(NEW.first_name, ' ', NEW.last_name));
> > END$$
> > DELIMITER ;
> > ```
> >
> > - MD5 es **hash**, no encriptado (no se reversa): devuelve `CHAR(32)` hexadecimal. El trigger lo computa al VUELO en el `BEFORE` — la app inserta el cliente normal y el trigger calcula el hash sin que nadie lo vea.

### ✏️ Ejercicio 2 — Usuario con la regla del nombre

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** crear usuario con la primera letra del nombre + apellido; dominio `localhost` (ejemplo Frank Malo → `fmalo`).
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > -- corriendo como admin:
> > CREATE USER 'fmalo'@'localhost' IDENTIFIED BY 'ClaveFuerte*1';
> > ```

### ✏️ Ejercicios 3-6 — GRANTs solicitados

> [!example]- 📝 Enunciado (Resumen) y soluciones
>
> > [!success]- ✅ GRANTs del 2024 (uno por acá)
> >
> > ```sql
> > -- 3) SELECT en tablas: payment, customer, country, city
> > GRANT SELECT ON sakila.payment  TO 'fmalo'@'localhost';
> > GRANT SELECT ON sakila.customer TO 'fmalo'@'localhost';
> > GRANT SELECT ON sakila.country  TO 'fmalo'@'localhost';
> > GRANT SELECT ON sakila.city     TO 'fmalo'@'localhost';
> >
> > -- 4) SELECT SOLO de una columna: category(name)
> > GRANT SELECT (name) ON sakila.category TO 'fmalo'@'localhost';
> >
> > -- 5) INSERT + UPDATE en address y country
> > GRANT INSERT, UPDATE ON sakila.address TO 'fmalo'@'localhost';
> > GRANT INSERT, UPDATE ON sakila.country TO 'fmalo'@'localhost';
> > ```
> >
> > - El GRANT por COLUMNA (`SELECT (name)`) es el punto importante de este bloque: el resto de columnas de `category` devuelve "No hay privilegios" al `SELECT *`.
> > - `SHOW GRANTS FOR 'fmalo'@'localhost'` para revisar los permisos otorgados.

### ✏️ Ejercicio 7 — Vista de ciudades (y el error de permisos)

> [!example]- 📝 Enunciado y solución
>
> **Enunciado:** con el login `fmalo`, crear vista `ciudad_pais` (nombre de ciudad, nombre de país). Si da error de permisos, solucionarlo.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > -- como fmalo (la primera try falla)
> > CREATE VIEW ciudad_pais AS
> > SELECT ci.city, co.country
> > FROM city ci JOIN country co ON ci.country_id = co.country_id;
> > -- ERROR 1142 (CREATE VIEW): acceso denegado a city/ccountry de fmalo
> > -- fmalo tiene SELECT, pero no tiene el permiso CREATE VIEW.
> >
> > -- dos curas desde admin:
> > -- Opción A: conceder el CREATE (y seguir SELECT implícito)
> > GRANT CREATE VIEW ON sakila.* TO 'fmalo'@'localhost';
> >
> > -- Opción B (recomendada): el ADMIN crea la vista; fmalo SELECT
> > CREATE VIEW sakila.ciudad_pais AS ...  -- (admin, DEFINER admin)
> > GRANT SELECT ON sakila.ciudad_pais TO 'fmalo'@'localhost';
> > ```
> >
> > - El detalle pedagógico: crear una vista requiere 3 derechos (SELECT de las tablas base — ya otorgados; CREATE VIEW; SELECT sobre la vista para leerla). La trampa del taller es que "tener SELECT de las tablas" no garantiza "crear la vista": hacen falta permisos distintos.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Normalización del campo `línea` (B1): [[03 - Segunda y tercera forma normal]] · [[04 - Normalización paso a paso]]
> - Operadores del álgebra que hace de fondo: [[Guía de Problemas 2 - Álgebra Relacional y Normalización]]
> - Índice: [[00 - Índice Unidad 3]] · Mapa: [[Sistema de Bases de Datos]]

## 📚 Fuentes

> [!quote] 📖 Fuentes
> `Unidad 0 - Guias y Ejercicios/Talleres/ENUNCIADO.pdf` · `Taller 3 2026 PAO 1.pdf` · `Taller 4_20agorep.pdf` (20-agosto-2026) · `Taller 4 - PAO I 2024 - Triggers, Vistas e Usuarios.pdf`. Base University: esquema estándar de ejemplo para SBD. Soluciones de consulta propias; núcleo DDL/DML de MySQL 8.

---

**Tags:** #TICG1018 #unidad3 #guia #taller3 #taller4 #bd
