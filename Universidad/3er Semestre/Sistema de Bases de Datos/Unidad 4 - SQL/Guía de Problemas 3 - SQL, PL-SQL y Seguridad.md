---
dg-publish: true
tags: [TICG1018, unidad4, guia, taller3, taller4, bd]
---

# 📝 Guía de Problemas 3 — SQL, PL-SQL y Seguridad (Talleres 3 y 4)

## 🎯 Introducción

> [!info] ℹ️ Qué es esta guía
>
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
> Teoría base: consultas y agregación → [[../Unidad 3 - Álgebra Relacional/Guía de Problemas 2 - Álgebra Relacional y Normalización]] (σ = WHERE, γ = GROUP BY); normalización del campo `línea` → [[../Unidad 2 - Modelo lógico y conversión/03 - Segunda y tercera forma normal]], [[../Unidad 2 - Modelo lógico y conversión/04 - Normalización paso a paso]].
>
> **Se lee así:** la guía se lee bloque por bloque — cada bloque es un taller independiente con su propia base de datos. El enunciado va arriba de cada ejercicio y la solución va plegada debajo, para que puedas intentar antes de desplegar.

> [!info] 📖 Los enunciados originales de los talleres (capturas de página)
>
> Los PDFs de los talleres son material de clase y no se embeben: cada enunciado se cita con la captura de su página y el número de página.
>
> **Taller 3 — consultas sobre la base University (`ENUNCIADO.pdf`, p. 1):**
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Talleres/bd-taller3-p1.png]]
>
> **Se lee así:** el enunciado pide **11 consultas SQL sobre la base `University`**, y están numeradas con su puntaje (de 7 a 13 puntos). Los primeros cinco puntos de cada consulta son la clave: (1) ID, name y dept_name de los instructores cuyo nombre **empiece con "A"** → `LIKE 'A%'`; (2) course_id, title y los créditos **duplicados** (`credits * 2 AS "doble creditos"`) de cursos con créditos **entre 3 y 5** → `BETWEEN` + alias de columna; (3) estudiantes **sin asesor asignado** → `LEFT JOIN` + `IS NULL`; (4) por cada departamento, **incluyendo los que aún no tienen instructores**, su número de instructores → `LEFT JOIN` + `COUNT` + `GROUP BY`; (5) dept_name y **salario promedio** por departamento, solo los que superen **70000**, ordenados de mayor a menor → `HAVING` + `ORDER BY`.
>
> **Por qué importa:** la segunda mitad del taller (puntos 8 a 11) es la que cambia de tema: pide explícitamente **operadores de conjuntos** — *"obtener el ID de todas las personas que son estudiantes o instructores del departamento de Comp. Sci (sin duplicados)"* → `UNION`; *"course_id que aparecen en `takes` y en `teaches`"*, con y sin duplicados → `UNION` vs `UNION ALL`; *"course_id que aparecen tanto en `takes` como en `teaches`"* → `INTERSECT`; y *"estudiantes que nunca han tomado ningún curso"* → `EXCEPT`/`MINUS`. Es la traducción literal del bloque de conjuntos de la Unidad 3.
>
> **Ejemplo:** el punto 4 es el que mejor resume el taller: para incluir a los departamentos **sin** instructores hay que usar `LEFT JOIN` y contar con `COUNT(i.instructor_id)` en vez de `COUNT(*)`, porque `COUNT(*)` cuenta la fila del `NULL` y daría 1 en vez de 0. El enunciado incluso avisa al final: *"presta atención a la diferencia entre JOIN, LEFT JOIN y RIGHT JOIN al momento de incluir o excluir filas sin coincidencia"*.
>
> **Taller 3 2026 — base supermercado (`Taller 3 2026 PAO 1.pdf`, p. 1):**
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Talleres/bd-taller3b-p1.png]]
>
> **Se lee así:** este taller **no son solo consultas**: tiene cuatro entregables de lo más heterogeneous. (1) **Normalizar un campo**: crear la tabla `linea (id, nombre)` y enlazarla a `producto`, usando **`UPDATE` con `JOIN`**. (2) **Promedio de ventas por sucursal**, sin considerar descuentos. (3) El **producto que más se vende en cada sucursal**, usando `cantidad` de `detalleventa`, y esa consulta **tiene que ser una vista** llamada `vProductoMasVendido` que presente nombre de sucursal, nombre de producto y cantidad de veces vendida, resuelta **con subqueries**. (4) Un **procedimiento** `sPCrearVenta` que recibe producto, tipo de pago y cajero, usando **transacciones**. Y (5) un **disparador** `tgrResumenProductos` que mantenga una tabla de resumen `tblResumenProductos` (id_producto, nombre_producto, cantidad_vendida, valor_ventas) **acumulando** si el producto aparece en una segunda venta.
>
> **Por qué importa:** este taller es el **examen final de la materia** disfrazado de ejercicio. Cada bullet es un tema de una unidad distinta: normalizar un campo es **Unidad 2**; el promedio por sucursal es **Unidad 3/4** (agregación); la vista con subqueries es **Unidad 4/03**; el procedimiento con transacciones y el trigger de acumulación son **Unidad 4/03** otra vez; y el `UPDATE` con `JOIN` es la técnica de **migración de datos** que no se explica en las notas pero se pide.
>
> **Ejemplo:** el punto (1) tiene una sutileza que conviene ver: el enunciado no pide "borrar el campo `linea`", pide **crear la tabla nueva y enlazarla**. El `UPDATE ... JOIN` es lo que copia los valores del campo texto a la nueva tabla (`UPDATE producto p JOIN linea l ON l.nombre = p.linea SET p.id_linea = l.id`), y **después** hay que quitar la columna redundante. Ese orden es el mismo que usaste al normalizar en la Unidad 2, pero automating con SQL.
>
> **Taller 4 — base DBalquiler (`Taller 4_20agorep.pdf`, pp. 1-2):**
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Talleres/bd-taller4-p1.png]]
>
> **Se lee así:** la primera página del taller 4 pide **cinco entregables** sobre la base `DBalquiler`. (1) El procedimiento `sp_registrar_alquiler`: inicia **transacción**, valida que `dias_alquilados > 0` y que `id_juego` tenga `stock_disponible > 0`, y si algo falla **revierte** sin insertar; si todo pasa, **confirma**, inserta el alquiler y **descuenta 1** del stock **dentro de la misma transacción**, devolviendo 1 o 0. (2) El trigger `trg_validar_resena`, **antes** de insertar, que bloquea la inserción con un **error controlado** si `puntuacion` no está entre 1 y 5. (3) La vista `vista_juegos_populares`: por título de videojuego, la plataforma, el número de alquileres y el total de días alquilados, **solo los que superen 100 días**, ordenados por total de alquileres de menor a mayor. (4) El procedimiento `sp_reporte_popularidad_juegos`, que **consulta esa vista** filtrando por plataforma y devuelve la cantidad de filas con mayor puntuación promedio. (5) El **análisis de impacto de un índice**: `EXPLAIN` de una consulta que filtra alquileres por cliente y rango de fechas, antes y después de crear un índice compuesto.
>
> **Por qué importa:** el punto (1) es el **ejemplo canónico de transacción** y por eso merece leerse despacio: el enunciado insiste en que la validación, el `INSERT` y el `UPDATE` del stock ocurren **en la misma transacción**. Si el descuento de stock estuviera fuera, otra sesión podría leer un stock viejo entre el `INSERT` y el `UPDATE`. Y fíjate en el retorno `1`/`0`: el procedimiento **notifica** el resultado sin lanzar un error, que es un patrón distinto al del trigger.
>
> **Ejemplo:** el punto (5) es el que conecta con el bloque de índices de la nota: el enunciado pide una consulta con `JOIN` + `WHERE nombre = 'Sofía Leon' AND fecha_alquiler BETWEEN '2024-06-01' AND '2024-06-30'`, y luego el mismo `EXPLAIN` después de crear el índice. La lectura del resultado es: comparar el **tipo de acceso** (`ALL` vs `ref`/`range`) y el **número de filas examinadas**. Si no baja, el índice está mal colocado.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Talleres/bd-taller4-p2.png]]
>
> **Se lee así:** la segunda página **continúa el punto (5)**: tras crear el índice compuesto hay que **volver a ejecutar la misma consulta con `EXPLAIN`** y comparar. Es la segunda mitad del ejercicio, y por eso la captura se cita aparte: sin ella falta el "después", que es justamente la prueba de que el índice sirvió.
>
> **Por qué importa:** el ejercicio está construido como un **antes y después** deliberado. El `EXPLAIN` inicial muestra el plan de la consulta sin índice; el final muestra el plan con índice. Si los dos planes son iguales, el índice no se está usando y hay que revisar el orden de las columnas del índice compuesto.
>
> **Ejemplo:** el orden importa: un índice compuesto sobre `(nombre, fecha_alquiler)` sirve para filtrar **por nombre y luego por rango de fecha**. Si el índice fuera `(fecha_alquiler, nombre)`, el filtro por nombre no lo usaría bien, porque el nombre no es la columna **prefijo**. Esa es la regla de oro del índice compuesto, y el taller la hace verificar a mano con `EXPLAIN`.
>
> **Taller 4 2024 — seguridad en sakila (`Taller 4 - PAO I 2024 - Triggers, Vistas e Usuarios.pdf`, p. 1):**
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Talleres/bd-taller4b-p1.png]]
>
> **Se lee así:** el taller 2024 es **el bloque de seguridad completo**, y cada viñeta es una pieza distinta del DCL y de las vistas. (1) Un **disparador** que encripte con **MD5** el nombre y apellido de los clientes nuevos. (2) `CREATE USER` con la **primera letra del nombre + el apellido** (el ejemplo del enunciado: *Frank Malo → `fmalo`*, dominio `localhost`). (3) `GRANT SELECT` sobre `payment`, `customer`, `country` y `city`. (4) `GRANT SELECT` sobre **una sola columna** (`name`) de `category`. (5) `GRANT INSERT` y `UPDATE` sobre `address` y `country`. Y al final, **hacer login con ese usuario** y crear una vista con las ciudades y sus países, *"de generar error por permisos, solucionarlo"*.
>
> **Por qué importa:** el punto (4) es el que demuestra que el SQL estándar permite **privilegios por columna**, algo que muchos motores no implementan. Y el último punto es el que hay que entender de verdad: la vista se crea **con el usuario administrador**, y el usuario nuevo **no puede verla** porque no tiene `SELECT` sobre la vista. La solución es `GRANT SELECT ON vista_ciudades TO 'fmalo'@'localhost';` — y ese es exactamente el tercer motivo de las vistas del deck ("seguridad al compartir información").
>
> **Ejemplo:** el trigger con MD5 es un ejemplo **didáctico, no de producción**: MD5 no es un hash de contraseñas, es criptografía débil y no debe usarse para nada real. En producción se usan `bcrypt`, `Argon2` o `SHA-256` con sal. El taller lo pide porque sirve para practicar triggers, no porque sea una buena práctica.

> [!info] 📖 El deck de cátedra: SQL y las restricciones (slides06, pp. 10-18)
>
> El deck del Ing. Jorge Magallanes cierra el curso con SQL. Estas son las figuras que definen la sintaxis que usan los ejercicios de esta guía.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p10.png]]
>
> **Se lee así:** la lámina (p. 10) es la **base de todo**: *"esta tarea se consigue usando la sentencia `CREATE TABLE`"*, y da la tabla `department` con sus tres atributos: `dept_name VARCHAR(200)`, `building VARCHAR(15)` y `budget NUMERIC(12, 2)`, más `PRIMARY KEY (dept_name)`. Y hace una observación estructural que conviene retener: *"se divide en 2 secciones: (1) la definición de columnas, y (2) las restricciones de integridad"*. Al pie, el contrapeso: *"para remover una relación se utiliza la sentencia `DROP TABLE t;`"*.
>
> **Por qué importa:** esa división en dos secciones es **exactamente** la estructura de un `CREATE TABLE` y por eso el enunciado de los talleres se puede leer así: primero las columnas, después las reglas. Y fíjate en que la PK se declara **al final**, como restricción de tabla: `PRIMARY KEY (dept_name)`. No es que la clave sea "la última columna": es que es una **regla sobre el conjunto**.
>
> **Ejemplo:** `dept_name VARCHAR(200)` con `PRIMARY KEY (dept_name)` significa "una columna de texto de hasta 200 caracteres que, además, no puede repetirse ni ser nula". El `VARCHAR(200)` es la **columna**; el `PRIMARY KEY` es la **restricción**. Son dos capas distintas y por eso pueden escribirse en lugares distintos del `CREATE`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p11.png]]
>
> **Se lee así:** la lámina (p. 11) añade la **restricción de clave foránea**, y el ejemplo completo es `CREATE TABLE course (course_id VARCHAR(7), title VARCHAR(50) NOT NULL, dept_name VARCHAR(20), credits NUMERIC(2,0), PRIMARY KEY (course_id), FOREIGN KEY (dept_name) REFERENCES department);`. El deck define: *"la especificación de `foreign key({L}) references s` define la lista L de atributos de clave foránea y que deben coincidir con algún valor de la clave primaria en s"*.
>
> **Por qué importa:** el deck cierra con la consecuencia práctica: *"en cada tupla de `course`, el valor de `dept_name` debe existir en el atributo de PK de `department`, sin esto, es posible que las tuplas de `course` especifiquen un `dept_name` que no existe"*. Eso **es** la integridad referencial, y es la regla que el motor aplica en cada `INSERT` y en cada `UPDATE`.
>
> **Ejemplo:** la FK `dept_name → department.dept_name` crea la relación que en el ER era `department 1—N course`. Si insertas un curso con `dept_name = 'Física'` y no existe ese departamento, el motor **rechaza** el `INSERT`. Es la misma regla del diagrama "carga el 1 primero" de la Unidad 1, pero automatizada y garantizada por el motor.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p13.png]]
>
> **Se lee así:** la lámina (p. 13) da la **definición general de restricción de integridad**: *"una restricción de integridad (integrity constraint) asegura que un cambio realizado en la DB no conduzca a la pérdida de la consistencia de datos"*. Y da tres ejemplos que son literalmente las tres reglas de la Unidad 2: el nombre de un instructor no puede ser `null`; dos instructores no pueden tener el mismo ID; y cada `dept_name` en `course` debe coincidir con uno de `department`.
>
> **Por qué importa:** el deck añade un detalle práctico que no aparece en las notas: *"usualmente las restricciones de integridad son parte de la definición de las tablas, sin embargo, pueden ser agregadas mediante la sentencia `ALTER TABLE table-name ADD constraint`"*. Es la puerta de entrada al `ALTER TABLE` que se usa en los talleres: **no siempre puedes reconstruir la tabla**, a veces lo que puedes es añadir la restricción después.
>
> **Ejemplo:** si la tabla `course` ya existe con miles de filas y quieres imponer la FK, no reescribes la tabla: haces `ALTER TABLE course ADD CONSTRAINT fk_course_dept FOREIGN KEY (dept_name) REFERENCES department(dept_name);`. Si alguna fila existente incumple la regla, el motor **rechaza** el `ALTER` — lo cual es una forma rápida de auditar si tus datos son válidos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p14.png]]
>
> **Se lee así:** la lámina (p. 14) es la de las **restricciones solo de tabla**, y introduce tres. `not null`: *"es utilizado [para] columnas obligatorias"* (ejemplos: `name VARCHAR(20) NOT NULL`, `budget NUMERIC(2,0) NOT NULL`). `unique({L})`: *"define la lista L de atributos de una clave candidata, a diferencia de PK, los atributos declarados pueden ser nulos"*. Y `check(P)`: *"se especifica un predicado P, es usado para campos que deben satisfacer una condición"*.
>
> **Por qué importa:** la diferencia entre `UNIQUE` y `PRIMARY KEY` que hace el deck es **el punto que más se pregunta**: un `UNIQUE` **admite `NULL`s** (en el SQL estándar, varios `NULL` no se consideran "repetidos"), mientras que la PK **no admite ninguno**. Por eso una clave candidata alternativa puede tener nulos y la primaria no. Y el `check(P)` se presenta además como la forma de **simular datos enumerados**: *"la columna semestre debe ser uno de estos valores: 'Fall', 'Winter', 'Spring' o 'Summer'"*.
>
> **Ejemplo:** el `CHECK` de dominio es la traducción directa del **dominio del atributo** que definiste en el diccionario de datos de la Unidad 2. `semestre VARCHAR(10) CHECK (semestre IN ('Fall','Winter','Spring','Summer'))` es exactamente "el dominio de `semestre` es ese conjunto". Y fíjate en que el deck dice que el `CHECK`, como el `NOT NULL`, **puede aparecer junto a la definición de la columna**, además de como restricción de tabla.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p17.png]]
>
> **Se lee así:** la lámina (p. 17) es la de la **integridad referencial**, y su contenido clave está al final. Define: *"las restricciones de clave foránea son la manera de asegurarnos que los valores de unos atributos coincidan con algún valor de la clave primaria en otra relación"*, y muestra las dos formas de declararla: como restricción de tabla (`foreign key(dept_name) references department(dept_name)`) o **junto a la columna** (`dept_name varchar(20) references department`). Pero lo importante es lo que viene después: *"cuando una restricción de clave foránea es violada, lo normal es que se rechace la acción. Sin embargo, puede especificarse algo distinto cuando una operación de `delete` o de `update` viola la restricción"*, con el ejemplo `on update cascade` / `on delete cascade`.
>
> **Por qué importa:** hasta ahora la integridad referencial solo se había visto como "el motor rechaza". La lámina dice que hay **tres opciones**, y que la elección depende de la regla de negocio: rechazar (por defecto), propagar (`cascade`), o poner `null`/`default` (`set null`, `set default`). No es un detalle: define qué pasa con las filas **hijas** cuando el padre desaparece.
>
> **Ejemplo:** con `ON DELETE CASCADE` en `course.dept_name`, si borras el departamento *"Comp. Sci."*, **se borran también** sus cursos. Con `ON DELETE SET NULL`, los cursos se quedan pero con `dept_name` vacío. Con el comportamiento por defecto (sin cláusula), el `DELETE` del departamento es **rechazado**. Los tres son válidos; lo que no vale es no decidir y que el motor decida por ti.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p18.png]]
>
> **Se lee así:** la lámina (p. 18) es la **consecuencia** de la anterior, con el caso concreto. Plantea: *"¿qué sucede con las tuplas que hacen referencia?"* cuando se intenta **borrar** la tupla con `dept_name = 'Comp. Sci.'` en `department`, o **cambiar** ese mismo valor. Y lista las opciones: **`cascade`** (*"es propagar el cambio, e.g., en una operación delete se propaga el borrado"*) y **`set null`, o `set default`** (*"se establece null o el valor default respectivamente"*). Abajo, las dos tablas del ejemplo (`course` con sus 4 filas y `department` con sus 3), con la columna `dept_name` marcada como *join columns*.
>
> **Por qué importa:** fíjate en que `CS-101` y `CS-190` son los dos cursos de `Comp. Sci.`: son las **filas hijas** que se ven afectadas. La lámina cierra el bloque de SQL del deck mostrándote que la integridad referencial **no es solo una regla de inserción**: es una regla que obliga a **decidir qué pasa con los hijos** cuando el padre cambia o desaparece. Esa decisión es una regla de negocio, y por eso se escribe en el `CREATE TABLE`.
>
> **Ejemplo:** si en la ESPOL se decide que al **borrar** un curso también se borran las notas de los alumnos que lo tomó, la FK debe llevar `ON DELETE CASCADE`. Si en cambio se decide que las notas **se conservan** (porque son histórico), lo correcto es `ON DELETE SET NULL` o， borrar el curso con un `DELETE` restringido. La misma sintaxis, dos políticas opuestas.
>
> **Violación (p. 18):** qué pasa con las tuplas que hacen referencia cuando se borra o cambia la tupla referenciada — la pregunta que responde el bloque D de esta guía con `ON DELETE` / `ON UPDATE`.

---

## 📝 Ejercicios Propuestos
### 🅰️ Bloque A — SQL sobre la base University (Taller 3, 11 consultas)

> [!tip] 📌 Cómo trabajar cada pregunta
>
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

### 🅱️ Bloque B — Supermercado: normalización + consultas + transacción + trigger (Taller 3 2026)

> [!info] 📋 Esquema asumido (el enunciado deja detalles libres)
>
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

### 🅲 Bloque C — Alquileres de videojuegos: PL-SQL, índices y MongoDB (Taller 4, 20-agosto-2026)

> [!info] 📋 Esquema asumido
>
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

### 🅳 Bloque D — Seguridad en sakila: MD5, usuarios y GRANT por columna (Taller 4 2024)

> [!info] 📋 Contexto
>
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

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - Diapositivas `2026_1PAO_slides6_1_TICG1018.pdf` — SQL: creación de tablas, restricciones de clave, integridad referencial (pp. 10-18).
> - Taller 3 (base University) — `Unidad 0 - Guias y Ejercicios/Talleres/ENUNCIADO.pdf` (11 consultas con puntaje).
> - Taller 3 2026 (base supermercado) — `Unidad 0 - Guias y Ejercicios/Talleres/Taller 3 2026 PAO 1.pdf`.
> - Taller 4 (base DBalquiler) — `Unidad 0 - Guias y Ejercicios/Talleres/Taller 4_20agorep.pdf` (20-agosto-2026).
> - Taller 4 2024 (base sakila) — `Unidad 0 - Guias y Ejercicios/Talleres/Taller 4 - PAO I 2024 - Triggers, Vistas e Usuarios.pdf`.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 3 (SQL: DDL, DML, vistas, seguridad) y cap. 5 (restricciones e integridad).
> - Núcleo DDL/DML de MySQL 8; las soluciones de consulta son propias.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[../Unidad 4 - SQL/01 - Introducción a SQL|01 - Introducción a SQL]] — el lenguaje y su estándar.
> - [[../Unidad 4 - SQL/02 - DDL y DML|02 - DDL y DML]] — `CREATE TABLE`, `ALTER`, `DROP`, `INSERT`, `UPDATE`, `DELETE`.
> - [[../Unidad 4 - SQL/03 - Consultas Avanzadas|03 - Consultas Avanzadas]] — JOIN, subconsultas, vistas y triggers.
> - [[../Unidad 3 - Álgebra Relacional/Guía de Problemas 2 - Álgebra Relacional y Normalización|Guía de Problemas 2]] — σ = `WHERE`, γ = `GROUP BY`, ρ = alias.
> - [[../Unidad 2 - Modelo lógico y conversión/03 - Segunda y tercera forma normal|03 - Segunda y tercera forma normal]] — por qué el campo `línea` sale de `producto`.
> - [[../Unidad 2 - Modelo lógico y conversión/04 - Normalización paso a paso|04 - Normalización paso a paso]] — el paso a paso de 1FN a 3FN.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Normalización del campo `línea` (B1): [[../Unidad 2 - Modelo lógico y conversión/03 - Segunda y tercera forma normal]] · [[../Unidad 2 - Modelo lógico y conversión/04 - Normalización paso a paso]]
> - Operadores del álgebra que hacen de fondo: [[../Unidad 3 - Álgebra Relacional/Guía de Problemas 2 - Álgebra Relacional y Normalización]]
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]

---

**Tags:** #TICG1018 #unidad4 #guia #taller3 #taller4 #sql #bd
