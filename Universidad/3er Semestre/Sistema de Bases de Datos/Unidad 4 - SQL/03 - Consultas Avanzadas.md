---
dg-publish: true
tags: [TICG1018, unidad4, sql, consultas-avanzadas, join, group-by, subquery, union, vista, trigger, grant, bd]
---

# 🔍 SQL — Consultas Avanzadas

## 🎯 Introducción

> [!info] 💡 ¿Qué cubre esta nota?
> Consultas que van más allá del SELECT básico: JOINs múltiples, GROUP BY con HAVING, subconsultas, operadores de conjuntos (UNION, INTERSECT, EXCEPT), vistas, índices, triggers, procedimientos almacenados y control de permisos.
> **Aplicaciones:**
> - Consultas reales: la mayoría de consultas de producción usan JOIN + GROUP BY.
> - Optimización: índices y EXPLAIN para ver el plan de ejecución.
> - Seguridad: usuarios, permisos por columna, vistas con acceso restringido.
> - Lección 1 (13-oct): JOIN, GROUP BY, HAVING, subquery, UNION.

> [!example] 📎 Diapositivas de referencia
> ![[../../Unidad 0 - Guias y Ejercicios/Diapositivas/SQL Avanzado.pptx]]

---

## 🛠️ JOINs Múltiples y Operadores de Conjuntos

### JOINs

> [!note] 📋 Definición — JOIN en SQL
> Combina filas de dos o más tablas basándose en una columna relacionada.
> | Tipo | Sintaxis | Qué trae |
> |---|---|---|
> | INNER JOIN | FROM a JOIN b ON a.x = b.x | Solo filas que casan en ambas |
> | LEFT JOIN | FROM a LEFT JOIN b ON a.x = b.x | Todas las de a, null en b si no casan |
> | RIGHT JOIN | FROM a RIGHT JOIN b ON a.x = b.x | Todas las de b, null en a si no casan |
> | SELF JOIN | FROM a JOIN a AS b ON ... | La misma tabla dos veces con alias |
> ```mermaid
graph TD
    A[Tabla A] -->|JOIN| B[Resultado combinado]
    C[Tabla B] -->|JOIN| B
    style A fill:#e1f5fe
    style C fill:#e1f5fe
    style B fill:#c8e6c9
```

> [!example] 🧪 Ejemplo de JOIN múltiple
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

### Operadores de Conjuntos

> [!note] 📋 Definición — UNION, INTERSECT, EXCEPT
> | Operador | Qué hace | SQL mental |
> |---|---|---|
> | UNION | Filas de ambas consultas, sin duplicados | UNION |
> | UNION ALL | Filas de ambas consultas, con duplicados | UNION ALL |
> | INTERSECT | Filas que aparecen en ambas consultas | INTERSECT |
> | EXCEPT | Filas de la primera que no están en la segunda | NOT IN / NOT EXISTS |

> [!example] 🧪 Ejemplo de INTERSECT
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

---

## 🛠️ GROUP BY y HAVING

> [!note] 📋 Definición — GROUP BY y HAVING
> GROUP BY agrupa filas por una columna. HAVING filtra grupos (después de agrupar), a diferencia de WHERE que filtra filas (antes de agrupar).
> Regla rápida: filtro de fila → WHERE; filtro de grupo → HAVING.
> ```mermaid
graph TD
    A[Filas] -->|GROUP BY| B[Grupos]
    B -->|HAVING| C[Grupos filtrados]
    style A fill:#e1f5fe
    style B fill:#fff3e0
    style C fill:#c8e6c9
```

> [!example] 🧪 Ejemplo de GROUP BY con HAVING
> ```sql
> -- Salario promedio por departamento, solo > 70000, ordenado desc
> SELECT dept_name, AVG(salary) AS salario_promedio
> FROM instructor
> GROUP BY dept_name
> HAVING AVG(salary) > 70000
> ORDER BY salario_promedio DESC;
> ```

---

## 🛠️ Subconsultas

> [!note] 📋 Definición — Subconsulta
> Una consulta anidada dentro de otra. Puede ir en FROM, WHERE o SELECT.
> | Tipo | Dónde va | Uso típico |
> |---|---|---|
> | Correlacionada | WHERE | Se ejecuta por cada fila externa |
> | No correlacionada | FROM o WHERE | Se ejecuta una vez |
> | Escalar | SELECT | Devuelve un solo valor |

> [!example] 🧪 Ejemplo de subconsulta correlacionada
> ```sql
> -- Estudiante que nunca tomó curso (EXCEPT)
> SELECT s.ID, s.name FROM student s
> EXCEPT
> SELECT t.ID FROM takes t;
> ```

---

## 🛠️ Vistas

> [!note] 📋 Definición — VISTA
> Una vista es una consulta guardada con nombre. Se comporta como una tabla virtual.
> Sintaxis:
> ```sql
> CREATE VIEW nombre_vista AS
> SELECT columnas FROM tabla WHERE condición;
> ```

> [!example] 🧪 Ejemplo de vista
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

> [!warning] ⚠️ Permisos para crear vistas
> Crear una vista requiere 3 derechos: SELECT de las tablas base, CREATE VIEW, y SELECT sobre la vista para leerla. Tener SELECT de las tablas base no garantiza poder crear la vista.

---

## 🛠️ Índices y EXPLAIN

> [!note] 📋 Definición — Índice compuesto
> Un índice compuesto se crea sobre varias columnas. El orden importa: el B+tree busca por prefijo, así que la columna de igualdad debe ir primero.
> Sintaxis:
> ```sql
> CREATE INDEX nombre_indice ON tabla (columna1, columna2);
> ```

> [!example] 🧪 Ejemplo de índice compuesto
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
> | Plan | Type | Key | Rows Scanned | Extra info |
> |---|---|---|---|---|
> | Antes | ALL | NULL | miles (scan completo) | Using where |
> | Después | range | idx_nombre_fecha | pocas (solo el mes) | Using index condition |

---

## 🛠️ Triggers y Procedimientos

> [!note] 📋 Definición — Trigger
> Un trigger es un procedimiento que se ejecuta automáticamente ante un evento (INSERT, UPDATE, DELETE) en una tabla.
> Sintaxis:
> ```sql
> CREATE TRIGGER nombre_trigger
> BEFORE/AFTER INSERT/UPDATE/DELETE ON tabla
> FOR EACH ROW
> BEGIN
>   -- lógica del trigger
> END;
> ```

> [!example] 🧪 Ejemplo de trigger con SIGNAL
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

> [!note] 📋 Definición — Procedimiento almacenado
> Un procedimiento es un bloque de código SQL guardado en la base de datos que se puede ejecutar con parámetros de entrada y salida.
> Sintaxis:
> ```sql
> CREATE PROCEDURE nombre_proc(IN parametro Tipo, OUT resultado Tipo)
> BEGIN
>   -- lógica
> END;
> ```

---

## 🛠️ Usuarios y Permisos (DCL)

> [!note] 📋 Definición — GRANT y REVOKE
> | Comando | Qué hace |
> |---|---|
> | CREATE USER | Crea un usuario de la base de datos |
> | GRANT | Asigna privilegios a un usuario |
> | REVOKE | Remueve privilegios asignados |
> | SHOW GRANTS | Muestra los permisos de un usuario |

> [!example] 🧪 Ejemplo de GRANT por columnas
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
> Cuando concedes SELECT (col1, col2) sobre una tabla, las columnas NO concedidas devuelven "No hay privilegios" al hacer SELECT *.

---

## 🎯 Ejercicios Propuestos

### ✏️ Ejercicio 1 — JOIN múltiple con agregación

> [!example] 📋 Planteamiento
> Dadas departamento(dept_name, ...) y instructor(ID, name, dept_name, salary), escribe SQL para: para cada departamento, mostrar nombre y número de instructores, incluyendo departamentos sin instructores.
> > [!success]- ✅ Solución
> > ```sql
> > SELECT d.dept_name, COUNT(i.ID) AS num_instructores
> > FROM department d
> >   LEFT JOIN instructor i ON d.dept_name = i.dept_name
> > GROUP BY d.dept_name;
> > ```
> > **Por qué:** LEFT JOIN conserva departamentos completos; COUNT(i.ID) ignora NULLs, así que departamentos sin instructores muestran 0.

### ✏️ Ejercicio 2 — Subconsulta para exclusión

> [!example] 📋 Planteamiento
> Dadas student(ID, name, ...) y takes(ID, course_id, ...), escribe SQL para: obtener ID y nombre de estudiantes que NUNCA han tomado un curso.
> > [!success]- ✅ Solución
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
> Crea una vista vProductoMasVendido que muestre, por sucursal, el producto más vendido (nombre de sucursal, nombre de producto, cantidad), usando subconsultas.
> > [!success]- ✅ Solución
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
> Escribe un procedimiento sp_registrar_alquiler que reciba cliente, juego y días; valide que días > 0 y stock > 0; si todo bien, inserte el alquiler y descuente 1 del stock en la misma transacción.
> > [!success]- ✅ Solución
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
> - Escribo un JOIN con dos tablas.
> - Uso GROUP BY con COUNT, SUM, AVG.
> - Distingo WHERE de HAVING.

> [!note] 📋 Nivel Intermedio
> - Escribo subconsultas correlacionadas y no correlacionadas.
> - Creo una vista y le asigno permisos.
> - Leo un plan EXPLAIN y sé cuándo un índice ayuda.

> [!note] 📋 Nivel Avanzado
> - Escribo triggers con SIGNAL para validación.
> - Diseño procedimientos con transacciones y manejo de errores.
> - Otorgaré permisos por columna y por procedimiento.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
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
> [!note] 🧠 Repasa con el plugin Spaced Repetition (Lección 1: 13-oct)

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
> - [[01 - Introducción a SQL]] — qué es SQL, estándares, DDL vs DML vs DCL.
> - [[02 - DDL y DML]] — CREATE TABLE, ALTER, DROP, INSERT, UPDATE, DELETE.
> - [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — 17 ejercicios resueltos con JOIN, triggers, vistas, permisos.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Anterior: [[02 - DDL y DML]]
> - Guía de ejercicios: [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]]

---

**Tags:** #TICG1018 #unidad4 #sql #consultas-avanzadas #join #vista #trigger #bd
