---
dg-publish: true
tags: [TICG1018, unidad4, sql, ddl, dml, create, alter, drop, insert, update, delete, bd]
---

# 🛠️ SQL — DDL y DML

## 🎯 Introducción

> [!info] 💡 ¿Qué hace DDL y qué hace DML?
>
> **DDL** (Data Definition Language) define la estructura: crea, modifica y elimina tablas, vistas, índices, triggers. **DML** (Data Manipulation Language) manipula los datos: inserta, actualiza, borra y consulta.
>
> **Aplicaciones:**
> - **Implementación:** toda tabla del proyecto sale de DDL.
> - **Operación diaria:** INSERT, UPDATE, DELETE, SELECT son DML.
> - **Lección 1 (13-oct):** CREATE TABLE con restricciones, INSERT, UPDATE, DELETE.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-02-01-graph.svg]]
>
> **Se lee así:** DDL responde *"¿cómo es la tabla?"* y DML responde *"¿qué hay en la tabla?"*. Por eso un `CREATE TABLE` va antes que cualquier `INSERT`: si cambias la estructura después, los datos ya guardados dejan de encajar.

> [!info] 📖 El deck de cátedra: los tres lenguajes de SQL (BD04, pp. 7-9)
>
> El deck de la unidad de DDL abre con la tabla de los tres lenguajes de SQL y el comando que le corresponde a cada uno.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p7.png]]
>
> **Se lee así:** la lámina (p. 7) es la primera de las tres, y presenta la tabla de **DDL** con sus tres comandos. `CREATE` *"crea objetos en la base de datos: tablas, vistas, triggers, etc."*; `ALTER` *"modifica un objeto existente de la base de datos. Ej: tabla, vista, etc"*; `DROP` *"elimina un objeto de la base de datos"*. Fíjate en que la descripción de `ALTER` y `DROP` dice **"objeto"**, no "tabla": los tres comandos sirven para cualquier objeto del esquema.
>
> **Por qué importa:** la palabra **"objeto"** es la clave de DDL. Un objeto de la base de datos puede ser una tabla, una vista, un trigger, un índice, un procedimiento… y el mismo `CREATE`/`ALTER`/`DROP` sirve para todos ellos, cambiando solo el tipo de objeto. Por eso el `DROP` de la p. 30 tiene seis variantes distintas.
>
> **Ejemplo:** `CREATE TABLE films`, `CREATE VIEW v_films`, `CREATE TRIGGER trg_audit` y `CREATE INDEX idx_titulo` son **el mismo comando** `CREATE`, con distinto objeto. Eso explica por qué `CREATE` es tan polimórfico y por qué el manual de MySQL los documenta en páginas distintas del mismo capítulo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p8.png]]
>
> **Se lee así:** la lámina (p. 8) añade el **DML** (el deck lo anota también como *DRL*) con sus cuatro comandos: `SELECT` *"consulta datos en la base de datos"*, `INSERT` *"inserta registros en las tablas"*, `UPDATE` *"modifica o actualiza datos de las tablas"* y `DELETE` *"elimina datos de las tablas"*. Nota que la lámina va acumulando: arriba está DDL, y ahora se lista DDL + DML.
>
> **Por qué importa:** fíjate en la diferencia de **objeto** entre las dos láminas: DDL trabaja sobre la **estructura** (la tabla, la vista), DML trabaja sobre **las filas** (los datos dentro de una tabla que ya existe). Por eso la secuencia de una consulta tiene un orden fijo: primero la tabla existe (`CREATE`), después se le meten filas (`INSERT`), y solo entonces se pueden consultar (`SELECT`).
>
> **Ejemplo:** un `SELECT` sobre una tabla que no existe falla, y un `INSERT` sobre una tabla que no existe también. Ninguno de los dos puede "preparar" la estructura: para eso está `CREATE`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p9.png]]
>
> **Se lee así:** la lámina (p. 9) cierra la tríada con el **DCL** (*Data Control Language*): `GRANT` *"asigna privilegios a usuarios"* y `REVOKE` *"remueve privilegios asignados a los usuarios"*. Y ahora la lámina lista los tres: DDL, DML y DCL.
>
> **Por qué importa:** el DCL es el lenguaje que responde *"¿quién puede hacer qué?"*. Es el puente con la Unidad 4/03 y con la seguridad: `GRANT SELECT ON films TO usuario` le da permiso de lectura, y `REVOKE` se lo quita. Los tres lenguajes Covers **tres ejes distintos**: estructura (DDL), datos (DML) y permisos (DCL).
>
> **Ejemplo:** el mismo `DELETE FROM films` es un DML desde el punto de vista del **comando**, pero lo que decide si se ejecuta es el **DCL**: si el usuario no tiene el privilegio `DELETE` sobre esa tabla, el motor lo rechaza aunque la sintaxis sea perfecta. Por eso una consulta puede fallar por permisos y no por SQL.

---

## 📋 Definiciones Formales

### 1️⃣ CREATE TABLE — la tabla con su esqueleto

> [!note] 📋 Definición — CREATE TABLE
>
> Crea una tabla nueva con sus columnas, tipos de datos y restricciones.
>
> **Sintaxis:**
>
> ```sql
> CREATE TABLE nombre_de_tabla (
>   nombre_de_columna tipo_de_dato [DEFAULT expr_default] [restriccion_de_columna[, ...]],
>   [restriccion_de_tabla[, ...]]
> );
> ```
>
> **Tipos de datos:** `CHAR(n)`, `VARCHAR2(n)`, `INTEGER`, `NUMERIC`, `FLOAT`, `DOUBLE PRECISION`, `DATE`, `TIME`, `TIMESTAMP`, `SERIAL`.
>
> **Ejemplos:**
> - `DEFAULT 'Usuario Final'` — la columna nace con ese valor si el `INSERT` no lo da (deck p. 22).
> - `PRIMARY KEY` en la misma línea de la columna — la clave en línea, sin tabla aparte.

> [!example] 🧪 Ejemplo de CREATE TABLE
>
> ```sql
> CREATE TABLE films (
>   codigo CHAR(5) PRIMARY KEY,
>   titulo VARCHAR2(40) NOT NULL,
>   did DECIMAL(3),
>   fecha_prod DATE,
>   genero VARCHAR(10),
>   CONSTRAINT production UNIQUE(fecha_prod),
>   FOREIGN KEY (did) REFERENCES distribuidores(did)
> );
>
> CREATE TABLE distribuidores(
>   did DECIMAL(3) PRIMARY KEY,
>   nombre VARCHAR2(40),
>   CONSTRAINT cons1 CHECK (did > 100 AND nombre <> ' ')
> );
> ```
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-02-02-er.svg]]
>
> **Se lee así:** el diagrama es el mismo `films`/`distribuidores` del código — `FILM.did` es FK a `DISTRIBUIDOR.did`. Lo que el diagrama **no** muestra son las restricciones: el `CHECK (did > 100 AND nombre <> ' ')` vive en el SQL, no en el modelo.

> [!info] 📖 El deck de cátedra: la sintaxis del CREATE TABLE (BD04, pp. 22-25)
>
> El deck separa la sintaxis en tres láminas: la forma general, las restricciones de columna y las de tabla.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p22.png]]
>
> **Se lee así:** la lámina (p. 22) da la **forma general** en dos niveles. El nivel de tabla: `CREATE TABLE <tbl_name> (<def_col1, def_col2, … restricc_tbl>)`. El nivel de columna: `<col_name> <col_tipoDato> [DEFAULT def_value] [restricc_col]`. Y el ejemplo de abajo es mínimo a propósito: `CREATE TABLE registro (nombre VARCHAR(30) DEFAULT "Usuario Final");` — una sola columna, con valor por defecto.
>
> **Por qué importa:** fíjate en que los corchetes `[ ]` significan **opcional**. Eso ya te dice que el `DEFAULT` y las restricciones de columna son opcionales, y que las restricciones de tabla (la última parte, `restricc_tbl`) son **otra categoría**, no una columna más. Esa distinción es exactamente lo que explican las dos láminas siguientes.
>
> **Ejemplo:** `DEFAULT "Usuario Final"` es la forma más simple de un valor por defecto: si el `INSERT` no menciona la columna, el motor le pone ese texto. Es lo que evita que un registro nuevo tenga un `NULL` donde debería tener algo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p23.png]]
>
> **Se lee así:** la lámina (p. 23) es la tabla de **restricciones de columna**, con la definición de cada una: `NOT NULL` → *"la columna no permite valores nulos"*; `UNIQUE` → *"no permite valores repetidos (clave alternativa)"*; `PRIMARY KEY` → *"no permite valores repetidos ni nulos (clave primaria)"*; `CHECK (condiciones)` → *"la columna debe cumplir con las condiciones"*. El ejemplo de abajo: `CREATE TABLE registro (fecha DATE NOT NULL, cedula INT PRIMARY KEY, nombre VARCHAR(10), edad INT CHECK (edad>18));`.
>
> **Por qué importa:** esta lámina es la que convierte las restricciones de la Unidad 2 en **código**. `UNIQUE` es la clave candidata, `PRIMARY KEY` es la clave primaria elegida, `CHECK` es el dominio del atributo y `NOT NULL` es el "atributo requerido" del E/R. Todo lo que aprendiste en el modelo conceptual tiene aquí su sintaxis exacta.
>
> **Ejemplo:** `edad INT CHECK (edad>18)` es la traducción literal del dominio del atributo `edad` que definiste en el diccionario de datos: *"entero, mayor que 18"*. Y `cedula INT PRIMARY KEY` es la clave primaria con las dos reglas que la definían: no nulos y no repetidos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p24.png]]
>
> **Se lee así:** la lámina (p. 24) es la de **restricciones de tabla**, y la diferencia con la anterior está en el **paréntesis**: `UNIQUE (col1, col2, …)`, `PRIMARY KEY (col1, col2, …)`, `FOREIGN KEY (col1, col2, …) REFERENCES <tbl2>(<tbl2_col>)` y `CHECK (condiciones)`. Cuando aparece la lista de columnas, la restricción ya **no pertenece a una sola columna**: es de la tabla. El ejemplo: `CREATE TABLE registro (fecha DATE NOT NULL, cedula INT, edad INT, PRIMARY KEY(cedula), CHECK (edad>18 AND edad<60), FOREIGN KEY(cedula) REFERENCES customers(customerNumber));`.
>
> **Por qué importa:** aquí aparece el `FOREIGN KEY` **declarado explícitamente**, que es la forma "declarativa" de la integridad referencial: no basta con declarar `INT` en la columna, hay que decir a qué tabla y a qué columna apunta. El motor usa esa declaración para decidir qué filas puede rechazar.
>
> **Ejemplo:** `FOREIGN KEY(cedula) REFERENCES customers(customerNumber)` crea la relación entre `registro` y `customers`. Con esa declaración, un `INSERT` en `registro` con una cédula que no exista en `customers` es rechazado. Es la misma integridad referencial del diagrama de carga (padres antes que hijas), pero declarada **una sola vez** y aplicada por el motor.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p25.png]]
>
> **Se lee así:** la lámina (p. 25) baja del **`CREATE TABLE` genérico** a los **dos `CREATE TABLE` reales** del ejemplo: `films` y `distribuidores`. `films` tiene `codigo VARCHAR(5) PRIMARY KEY`, `titulo VARCHAR(40)`, `did INT(3)`, `fecha_prod DATE`, `genero VARCHAR(10)`, y al final `CONSTRAINT production UNIQUE(fecha_prod)` y `FOREIGN KEY (did) REFERENCES distribuidores(did)`. `distribuidores` tiene `did INT(3) PRIMARY KEY`, `nombre VARCHAR(40)` y `CONSTRAINT cons1 CHECK (did > 100 AND nombre <> ' ')`.
>
> **Por qué importa:** la lámina muestra el `CONSTRAINT <nombre>` explícito, que es un detalle práctico importante: **el motor guarda las reglas con nombre** y puedes referenciarlas después (`ALTER TABLE ... DROP CONSTRAINT cons1`). Sin nombre, el motor genera uno y ya no sabes cómo referirse a él. Fíjate además en que la restricción de tabla `UNIQUE(fecha_prod)` lleva nombre `production`, que es un nombre **de negocio**, no técnico.
>
> **Ejemplo:** `CONSTRAINT cons1 CHECK (did > 100 AND nombre <> ' ')` se lee como: el `did` debe ser mayor que 100 **y** el nombre no puede ser un espacio en blanco. La segunda parte (`nombre <> ' '`) es la que impide el dato basura que el `NOT NULL` no atrapa: el nombre existe, pero está vacío.

### 2️⃣ Restricciones — las reglas que el motor hace cumplir

> [!note] 📋 Definición — Restricciones
>
> | Restricción | Qué hace |
> |---|---|
> | `NOT NULL` | La columna no puede ser nula |
> | `UNIQUE` | Todos los valores de la columna son diferentes |
> | `PRIMARY KEY` | NOT NULL + UNIQUE; identifica cada fila |
> | `FOREIGN KEY` | Referencia la clave primaria de otra tabla |
> | `CHECK` | Los valores cumplen una condición específica |
> | `DEFAULT` | Valor por defecto si no se especifica uno |
> | `INDEX` | Índice para recuperar datos rápidamente |
>
> **Dos niveles:**
> - **De columna:** se escribe junto al tipo → `titulo VARCHAR(40) NOT NULL`.
> - **De tabla:** se escribe al final del `CREATE TABLE` → `CONSTRAINT production UNIQUE(fecha_prod)`.

> [!example] 🧪 Ejemplo de restricciones
>
> ```sql
> CREATE TABLE Marineros (
>   sid INTEGER PRIMARY KEY,
>   snombre CHAR(20),
>   rating INTEGER,
>   edad REAL
> );
>
> CREATE TABLE Botes (
>   bid INTEGER PRIMARY KEY,
>   bnombre CHAR(20),
>   color CHAR(10)
> );
>
> CREATE TABLE Reservacion (
>   sid INTEGER,
>   bid INTEGER,
>   dia DATE,
>   PRIMARY KEY (sid, bid, dia),
>   FOREIGN KEY (sid) REFERENCES Marineros,
>   FOREIGN KEY (bid) REFERENCES Botes
> );
> ```
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-02-03-er.svg]]
>
> **Se lee así:** `Reservacion` no tiene clave única de una sola columna: su PK es **compuesta** `(sid, bid, dia)`. El diagrama lo muestra con las tres columnas marcadas como PK — significa que la combinación identifica la fila, no cada columna por separado. Un marinero puede reservar muchos botes y un bote muchos marineros, pero no el mismo bote el mismo día dos veces.
>
> **Por qué importa:** la PK compuesta es la diferencia entre "una reserva" y "un par de claves que se repiten". Si dejas `sid` y `bid` sueltos, el motor acepta la fila duplicada y tu conteo de reservas miente.

> [!info] 📖 El deck de cátedra: el caso de las tres tablas (BD04, pp. 26-27)
>
> El deck da los datos y el DDL de las mismas tres tablas del ejemplo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p26.png]]
>
> **Se lee así:** la lámina (p. 26) es **la misma información en forma de datos**, y ver las dos versiones juntas es la mejor forma de entender qué hace un `CREATE TABLE`. `Marineros`: `22 Dustin 7 45.0`, `31 Lubber 8 55.5`, `95 Bob 3 63.5`. `Botes`: `101 Interlake azul`, `102 Interlake rojo`, `103 Clipper verde`, `104 Marine rojo`. `Reservacion`: `22 · 101 · 10/10/96` y `95 · 103 · 11/12/96`.
>
> **Por qué importa:** mira los **tipos** que deducen las filas: `edad` con valores `45.0` y `63.5` es `REAL`, no `INT`; `rating` con `7`, `8`, `3` es `INTEGER`; `dia` con `10/10/96` es `DATE`; y `snombre` como `CHAR(20)` (nombre corto, tamaño fijo). La lámina siguiente (p. 27) confirma esa lectura: los tipos del DDL no son arbitrarios, **salen de los datos**.
>
> **Ejemplo:** fíjate también en un dato que parece redundante: hay dos botes `Interlake` (101 azul y 102 rojo) y dos `rojo` (102 y 104). Eso no es un error: `bnombre` describe el **modelo** del bote y `color` el color, y dos botes del mismo modelo pueden ser de distinto color. Si `bnombre` fuera la PK, no podrían coexistir.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p27.png]]
>
> **Se lee así:** la lámina (p. 27) es el **DDL de las tres tablas del ejercicio**, y hay que leerlo con el modelo de la Unidad 2 al lado. `Marineros(sid INTEGER PRIMARY KEY, snombre CHAR(20), rating INTEGER, edad REAL)`. `Botes(bid INTEGER PRIMARY KEY, bnombre CHAR(20), color CHAR(10))`. Y `Reservacion(sid INTEGER, bid INTEGER, dia DATE, PRIMARY KEY (sid, bid, dia), FOREIGN KEY (sid) REFERENCES Marineros(sid), FOREIGN KEY (bid) REFERENCES Botes(bid))`.
>
> **Por qué importa:** `Reservacion` es **la tabla intermedia** de una relación N:N entre marineros y botes, y su PK compuesta `(sid, bid, dia)` lo demuestra: incluye **las dos FKs más la fecha**. La `dia` es el atributo propio de la relación (un marinero puede reservar el mismo bote en días distintos). Sin ella, un marinero no podría volver al mismo bote otro día.
>
> **Ejemplo:** el `sid` solo **no** identifica una reserva: el marinero 22 puede reservar varios botes. El `bid` solo tampoco: el bote 101 lo pueden reservar varios marineros. Solo la **combinación** `(sid, bid, dia)` es única. Esa es exactamente la definición de clave compuesta, y por eso el `CREATE TABLE` la escribe con paréntesis: `PRIMARY KEY (sid, bid, dia)`.

### 3️⃣ ALTER TABLE — cambiar la estructura con datos dentro

> [!note] 📋 Definición — ALTER TABLE
>
> Modifica un objeto existente (tabla, vista, etc.) cuando ya tiene datos.
>
> **Sintaxis:**
>
> ```sql
> ALTER TABLE nombre_tabla {ADD | MODIFY | DROP} elemento [definicion];
> ```
>
> **Ejemplos:**
> - `ADD` — agrega columna o restricción.
> - `MODIFY` — cambia el tipo de una columna.
> - `DROP` — elimina columna o restricción.

> [!example] 🧪 Ejemplos de ALTER TABLE
>
> ```sql
> ALTER TABLE Botes ADD COLUMN Edad REAL;
> ALTER TABLE Marineros MODIFY rating REAL;
> ALTER TABLE Distribuidores DROP CONSTRAINT cons1;
> ALTER TABLE Films DROP COLUMN genero;
> ALTER TABLE Botes ADD CONSTRAINT con CHECK (edad < 100);
> ```
>
> **Se lee así:** `ALTER` y `DROP` no se escriben igual. `DROP COLUMN genero` borra la columna; `DROP CONSTRAINT cons1` borra la regla, no el dato. El primero elimina información; el segundo abre la puerta a que la información que ya estaba sea inválida.

> [!info] 📖 El deck de cátedra: el ALTER TABLE (BD04, p. 31)
>
> El deck presenta el ALTER como un comando más de DDL, con su forma general y ejemplos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p31.png]]
>
> **Se lee así:** la lámina (p. 31) da la **sintaxis en dos niveles** y los **cuatro ejemplos**. La forma general: `ALTER <elemento> <nombre> <specification1>, <especification2>, …;`, y la forma concreta: `ALTER <objeto> <nombre> <specification1>, <especification2>, …;` con `ADD|MODIFY|DROP <elemento> <definición>`. Los ejemplos: `ALTER TABLE Botes ADD Edad INT;`, `ALTER TABLE Marineros MODIFY rating REAL;`, `ALTER TABLE Films DROP COLUMN genero;` y `ALTER TABLE Botes ADD CONSTRAINT con CHECK (edad<100);`. Abajo, un extra: `SHOW CREATE TABLE <tbl_name>`.
>
> **Por qué importa:** los tres verbos del `ALTER` tienen **consecuencias distintas sobre los datos**, y esa diferencia es lo que hay que entender. `ADD` **agrega** (y la columna nueva empieza vacía, o con su `DEFAULT`). `MODIFY` **cambia la definición** de algo que ya existe (y puede fallar si los datos actuales no caben en el tipo nuevo). `DROP` **elimina** (y con ella, los datos que tenía).
>
> **Ejemplo:** `ALTER TABLE Marineros MODIFY rating REAL` parece inofensivo, pero si el motor lo acepta, la tabla pasa a guardar `7` como `7.0`. Si en cambio escribieras `MODIFY rating INT` sobre una columna que ya tiene `7.5`, el motor **rechaza** el cambio: no puede perder el `.5` sin perder datos. Esa es la diferencia entre "cambiar el tipo" y "cambiar el nombre de la columna".
>
> **Por qué importa (la coma):** la sintaxis admite `specification1, specification2, …` — o sea, **varias especificaciones en un solo statement**. Y `SHOW CREATE TABLE` es la herramienta de diagnóstico: te devuelve el `CREATE TABLE` que el motor tiene realmente guardado, que no siempre es el que escribiste (por normalizaciones del motor o cambios automáticos).

### 4️⃣ DROP TABLE — sin marcha atrás

> [!note] 📋 Definición — DROP TABLE
>
> Elimina un objeto de la base de datos. **No tiene marcha atrás.**
>
> **Sintaxis:**
>
> ```sql
> DROP TABLE nombre_tabla;
> ```
>
> **Ejemplo:**
> - `DROP TABLE films;` — borra la tabla y todas sus filas.

> [!example] 🧪 Ejemplo de DROP TABLE
>
> ```sql
> DROP TABLE films;
> ```
>
> **Por qué importa:** el deck lo dice literal — *"no tiene marcha atrás"*. No hay `UNDO TABLE`. Si necesitas deshacer, la única salida es un backup, y por eso el `DROP` se escribe al final del ciclo de vida de una tabla, nunca al principio.

> [!info] 📖 El deck de cátedra: el DROP (BD04, pp. 29-30)
>
> El deck dedicó dos láminas al borrado de objetos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p29.png]]
>
> **Se lee así:** la lámina (p. 29) es la **advertencia con su sintaxis**: *"sintaxis para el borrado de un elemento: no tiene marcha atrás"*, con la forma `DROP <elemento> <nombre>` y el ejemplo `DROP TABLE films;`. Es una lámina corta a propósito: el deck quiere que el mensaje sea imposible de pasar por alto.
>
> **Por qué importa:** "no tiene marcha atrás" no es una frase de marketing. En SQL estándar **no existe** un `UNDO DROP`. Y a diferencia de un `DELETE` (que borra filas y se puede recuperar de una transacción con `ROLLBACK`), el `DROP` **es un DDL**: en MySQL provoca un **commit implícito**, así que ni siquiera un `ROLLBACK` posterior devuelve la tabla. El objeto desaparece del diccionario de datos.
>
> **Ejemplo:** la diferencia práctica es brutal. `DELETE FROM films WHERE codigo = 'F001'` se puede deshacer con `ROLLBACK` si estás dentro de una transacción. `DROP TABLE films;` **no**: la tabla y su estructura se borran del esquema, y la única forma de recuperarla es un `RESTORE` desde un backup. Por eso el `DROP` se escribe al final del ciclo de vida de una tabla, nunca al principio.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p30.png]]
>
> **Se lee así:** la lámina (p. 30) es la **tabla de la familia `DROP`**, y su valor está en que muestra que `DROP` no es solo de tablas: base de datos (`DROP DATABASE <nombreDB>`), índice (`DROP INDEX <nombreIndice> ON <nombreTabla>`), tabla (`DROP TABLE <nombreTabla>`), trigger (`DROP TRIGGER <nombreTrigger>`), procedimiento (`DROP PROCEDURE <nombreProcedure>`) y vista (`DROP VIEW <nombreVista>`).
>
> **Por qué importa:** cada objeto tiene **su propia forma de borrado**, y hay una diferencia sutil que importa: `DROP INDEX` **no** lleva `ON <tabla>`; los demás sí llevan su nombre de objeto. Si te lo saltas, el motor da error de sintaxis. Y fíjate en que `DROP INDEX` **no borra la tabla ni sus datos**: solo borra el índice, que era una estructura auxiliar. Es la diferencia entre borrar el **dato** y borrar el **índice** que lo acelera.
>
> **Ejemplo:** si tu consulta se puso lenta, la reacción habitual es `DROP INDEX idx_titulo` para "quitar el problema". Lo que estás haciendo es **empeorar** la consulta: sin índice, el motor tiene que recorrer la tabla entera. Lo correcto es `DROP INDEX` solo cuando el índice ya no sirve para nada, y para eso primero se consulta `SHOW INDEX FROM films;`.

### 5️⃣ DML — INSERT, UPDATE, DELETE y SELECT

> [!note] 📋 Definición — DML (INSERT, UPDATE, DELETE, SELECT)
>
> El DML manipula los **datos** que viven dentro de una tabla ya definida. Son cuatro comandos con una diferencia clave: **qué filas tocan**.
>
> | Comando | Qué hace | Si omitas el `WHERE` |
> |---|---|---|
> | `INSERT` | Inserta registros en la tabla | — (no aplica) |
> | `UPDATE` | Modifica o actualiza datos existentes | Modifica **todas** las filas |
> | `DELETE` | Elimina datos existentes | Borra **todas** las filas |
> | `SELECT` | Consulta datos en la base de datos | Devuelve toda la tabla |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-02-05-graph.svg]]
>
> **Se lee así:** `INSERT` **agrega** filas, `UPDATE` **cambia** filas existentes y `DELETE` **quita** filas. `SELECT` no modifica nada: es la operación más usada del DML y la única de las cuatro que no toca el estado de la tabla.

> [!note] 📋 Definición — INSERT
>
> Inserta registros en una tabla. El número de ítems debe coincidir con el número de columnas.
>
> **Sintaxis:**
>
> ```sql
> INSERT INTO nombreTabla[(lista_columnas)] VALUES (lista_valores);
> ```
>
> **Reglas del deck:**
> - El número de ítems debe ser el mismo de las columnas.
> - Correspondencia directa entre nombre de columna y lista de valores.
> - Los valores deben ser compatibles en tipo de dato.
> - La lista de columnas es opcional: si se omite, se asume el orden usado para crear la tabla.

> [!example] 🧪 Ejemplos de INSERT
>
> ```sql
> INSERT INTO Tarjeta VALUES (2, 'Vanessa E', '00112233445567', '2019-07-01');
>
> INSERT INTO Tarjeta (idTarjeta, nombre_tarjeta, numero_tarjeta, fecha_expiracion)
> VALUES (2, 'Vanessa E', '00112233445567', '2019-07-01');
> ```
>
> **Se lee así:** las dos formas son equivalentes **si** el orden de las columnas coincide con el de la definición. En cuanto la tabla crezca o cambie el orden, la segunda forma es la segura: nombra las columnas y no depende de memorizar posiciones.

> [!note] 📋 Definición — UPDATE
>
> Modifica o actualiza datos existentes en una tabla.
>
> **Sintaxis:**
>
> ```sql
> UPDATE nombre_tabla SET columna1 = valor1 [, columna2 = valor2, ...] WHERE condición;
> ```
>
> **Reglas del deck:**
> - Los nuevos valores deben ser compatibles con el tipo de la columna.
> - El `WHERE` es opcional: si se omite, se modifican **TODAS** las filas.

> [!example] 🧪 Ejemplo de UPDATE
>
> ```sql
> UPDATE empleado SET salario = 5000 WHERE id = 1;
> ```
>
> **Por qué importa:** el deck muestra los dos casos — `UPDATE COSTUMERS SET CREDITLIMIT = CREDITLIMIT*1.12` (modificación de **todos** los registros) y el mismo UPDATE con `WHERE CUSTOMERNUMBER=103` (modificación de **filas**). Un `UPDATE` sin `WHERE` es el error más caro de la unidad.

> [!note] 📋 Definición — DELETE
>
> Elimina datos existentes en una tabla.
>
> **Sintaxis:**
>
> ```sql
> DELETE FROM nombre_tabla WHERE condición;
> ```
>
> **Reglas del deck:**
> - El `WHERE` es opcional: si se omite, se borran **todas** las filas.
> - Si se especifica, borra las filas que cumplen con la condición.

> [!example] 🧪 Ejemplo de DELETE
>
> ```sql
> DELETE FROM empleado WHERE id = 1;
> ```
>
> **Se lee así:** `DELETE FROM COSTUMERS` borra todos los registros; `DELETE FROM COSTUMERS WHERE CUSTOMERNUMBER=102` borra registros específicos. El `WHERE` es la única diferencia entre las dos — y entre una prueba y un incidente.

> [!note] 📋 Definición — SELECT básico
>
> Consulta datos en la base de datos. Es la operación más usada de DML.
>
> **Sintaxis básica:**
>
> ```sql
> SELECT columnas FROM tabla WHERE condición;
> ```

> [!example] 🧪 Ejemplo de SELECT
>
> ```sql
> SELECT ID, name, dept_name FROM instructor WHERE name LIKE 'A%';
> ```
>
> **Ejemplos:**
> - `LIKE 'A%'` — nombres que **empiezan** con A (`%` = cualquier secuencia).
> - `LIKE 'A_'` — nombres de exactamente dos caracteres que empiezan con A (`_` = un solo carácter).
> - `LIKE '%a'` — nombres que **terminan** en a.

> [!info] 📖 El deck de cátedra: el DML en detalle (BD04, pp. 34-35, 39, 43)
>
> El deck dedicó cuatro láminas al DML: la síntesis, las reglas del INSERT, el UPDATE y el DELETE.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p34.png]]
>
> **Se lee así:** la lámina (p. 34) es la **síntesis del DML**, y la lectura importante es que el deck describe las tres operaciones de modificación **en una sola frase cada una**: `INSERT` *"ingresa datos (filas) a la base de datos"*; `UPDATE` *"modifica datos de las filas dependiendo de una condición"*; `DELETE` *"elimina filas de una tabla"*.
>
> **Por qué importa:** fíjate en la palabra que se repite en las tres: **"filas"**. INSERT, UPDATE y DELETE operan sobre **filas**, nunca sobre la estructura. Esa es la frontera con el DDL: `ALTER TABLE` cambia la estructura y `UPDATE` cambia las filas. Y fíjate en el matiz del `UPDATE`: *"dependiendo de una condición"* — la condición es lo que decide **a cuántas filas** afecta.
>
> **Ejemplo:** el mismo `UPDATE` con y sin `WHERE` es la diferencia entre *"cambia el rating de Dustin"* y *"cambia el rating de todos los marineros"*. La sintaxis es la misma; el daño es distinto.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p35.png]]
>
> **Se lee así:** la lámina (p. 35) da la sintaxis del `INSERT`: `INSERT INTO nombreTabla[(lista_columnas)] VALUES (lista_valores)`, y sobre todo las **cuatro reglas**. (1) *"el número de ítems debe ser el mismo de las columnas"*. (2) *"correspondencia directa entre nombre_columnas y lista_valores"*. (3) *"compatible en tipos de datos"*. (4) *"lista_columnas opcional"*, con dos casos: si se omite, se asume **el orden en que se creó la tabla**; si se especifica y se omiten columnas, esas columnas **debieron declararse como `NULL` o con un `DEFAULT`**.
>
> **Por qué importa:** la regla (4) es la que más confunde y la que más se pregunta. Si escribes `INSERT INTO films VALUES ('F001', 'Alien')` sin lista de columnas, el motor asigna `'F001'` a la **primera** columna y `'Alien'` a la **segunda**, sin mirar qué son. Si esa segunda columna es `fecha_prod DATE`, el motor te da un error de tipo. Con lista de columnas (`INSERT INTO films (codigo, titulo) VALUES (...)`) el desajuste desaparece.
>
> **Ejemplo:** la parte de *"debieron declararse como `NULL` o un valor `DEFAULT`"* se entiende con un ejemplo: si `films` tiene `fecha_prod DATE NOT NULL DEFAULT '2026-01-01'`, un `INSERT` que omita esa columna no falla: el motor le pone el `DEFAULT`. Si la columna fuera `NOT NULL` **sin** default, el `INSERT` sería rechazado. Por eso el `DEFAULT` y el `NOT NULL` se deciden juntos al crear la tabla.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p39.png]]
>
> **Se lee así:** la lámina (p. 39) es la del `UPDATE`: `UPDATE nombreTabla SET columna1 = valor1 [,columna2 = valor2] WHERE condicion`. Las dos reglas de arriba: *"nuevos valores deben ser compatibles"* y *"WHERE opcional"*. Y el deck desglosa el `WHERE` en los dos casos: *"si se omite: se modifican TODAS las filas"*; *"si se especifica: se modifican las filas que cumplen con la condición"*.
>
> **Por qué importa:** el `WHERE` **opcional** es la trampa clásica de SQL, y el deck lo pone en mayúsculas justamente por eso: `TODAS`. Un `UPDATE` sin `WHERE` no es "una consulta más amplia": es una operación **masiva e irreversible** que aplica a la tabla entera. La misma estructura aplica al `DELETE`, y por eso el `WHERE` va después del `SET`, no antes.
>
> **Ejemplo:** `UPDATE Marineros SET rating = 10 WHERE snombre = 'Dustin';` toca una fila. `UPDATE Marineros SET rating = 10;` toca las tres. La diferencia de caracteres es mínima y la diferencia de consecuencias, no. En MySQL, con `safe_updates` activado, el motor **rechaza** el `UPDATE` sin `WHERE` que no use la clave: es una red de seguridad que conviene tener puesta.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p43.png]]
>
> **Se lee así:** la lámina (p. 43) es la del `DELETE`: `DELETE FROM nombreTabla WHERE condicion`, con las mismas dos reglas del `UPDATE` pero con la diferencia de fondo: *"borra las filas de una tabla específica"* y, sobre el `WHERE`, *"si se omite: se borran todas las filas"*; *"si se especifica: borra las filas que cumplen con la condición"*.
>
> **Por qué importa:** compara las tres láminas entre sí: `INSERT` **agrega**, `UPDATE` **cambia**, `DELETE` **quita**. Y fíjate en que el `DELETE` **no** lleva `SET`: no dice qué valor poner, solo a quién. Eso lo hace más simple de escribir y **más fácil de ejecutar por error**.
>
> **Ejemplo:** `DELETE FROM Reservacion WHERE sid = 22 AND bid = 101;` borra **una** reserva (la del 10/10/96). `DELETE FROM Reservacion;` borra **todas** las reservas. Y para limpiar **todas las filas pero conservar la tabla**, la alternativa es `TRUNCATE TABLE Reservacion;`, que es más rápida porque no registra cada borrado en el log — pero que, igual que el `DROP`, no se puede deshacer con `ROLLBACK`.

---

## 🔄 El ciclo de vida de una tabla

> [!note] 📋 El orden que no se negocia
>
> 1. `CREATE TABLE` — la tabla existe con su esqueleto y sus reglas.
> 2. `INSERT` — llegan las filas.
> 3. `ALTER TABLE` — la estructura cambia (y hay que revisar qué datos quedan fuera).
> 4. `UPDATE` / `DELETE` — los datos cambian o desaparecen.
> 5. `DROP TABLE` — la tabla se va, sin marcha atrás.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-02-04-flow.svg]]
>
> **Por qué importa:** casi todos los errores de esta unidad son errores de **orden**. Un `INSERT` antes del `CREATE` no tiene tabla donde insertar; un `DROP` antes del `DROP`… no. El ciclo se lee de izquierda a derecha como se lee el SQL de un proyecto real.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Crear una tabla con restricciones

> [!example] 📋 Planteamiento
>
> Escribe el SQL para crear una tabla `PRODUCTO` con:
> - `codigo` (entero, PK)
> - `nombre` (texto hasta 100 caracteres, no nulo)
> - `precio` (decimal, debe ser mayor a 0)
> - `stock` (entero, valor por defecto 0)
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > CREATE TABLE PRODUCTO (
> >   codigo INTEGER PRIMARY KEY,
> >   nombre VARCHAR(100) NOT NULL,
> >   precio DECIMAL(10,2) CHECK (precio > 0),
> >   stock INTEGER DEFAULT 0
> > );
> > ```

### ✏️ Ejercicio 2 — INSERT con columnas parciales

> [!example] 📋 Planteamiento
>
> Dada la tabla `PRODUCTO(codigo PK, nombre, precio, stock DEFAULT 0)`, inserta un producto solo especificando código, nombre y precio (usa el valor por defecto para stock).
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > INSERT INTO PRODUCTO (codigo, nombre, precio) VALUES (1, 'Laptop', 1200.00);
> > ```

### ✏️ Ejercicio 3 — ALTER para agregar columna

> [!example] 📋 Planteamiento
>
> A la tabla `PRODUCTO` agrega una columna `categoria` (texto hasta 50 caracteres).
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > ALTER TABLE PRODUCTO ADD COLUMN categoria VARCHAR(50);
> > ```

### ✏️ Ejercicio 4 — UPDATE con condición

> [!example] 📋 Planteamiento
>
> Aumenta el precio en un 10% a todos los productos de la categoría 'Electrónica'.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > UPDATE PRODUCTO SET precio = precio * 1.10 WHERE categoria = 'Electrónica';
> > ```

### ✏️ Ejercicio 5 — DELETE con subconsulta

> [!example] 📋 Planteamiento
>
> Borra los productos que tienen stock 0 y pertenecen a la categoría 'Descontinuados'.
>
> > [!success]- ✅ Solución
> >
> > ```sql
> > DELETE FROM PRODUCTO WHERE stock = 0 AND categoria = 'Descontinuados';
> > ```

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo un CREATE TABLE con PK y al menos una restricción.
> - [ ] Hago INSERT, UPDATE y DELETE con WHERE.
> - [ ] Distingo DDL de DML.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Uso ALTER TABLE para agregar, modificar y eliminar columnas y restricciones.
> - [ ] Escribo INSERT especificando solo algunas columnas (usando DEFAULT).
> - [ ] Explico por qué DROP TABLE no tiene marcha atrás.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Diseño un esquema completo con múltiples tablas y FKs.
> - [ ] Detecto cuándo una restricción CHECK es necesaria vs cuándo se maneja en la aplicación.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - Diapositivas `BD04 DDL_dml_create_alter_drop.pdf` — Data Definition Language (DDL) y Data Manipulation Language (DML), 45 láminas (pp. 7-9, 21-31, 34-44).
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 8 — el modelo relacional y el lenguaje SQL.
> - Guía: [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — 17 ejercicios resueltos de SQL real.
> - Diagramas propios: `u4-02-01-graph` (DDL vs DML), `u4-02-02-er` (films/distribuidores), `u4-02-03-er` (Marineros/Botes/Reservacion), `u4-02-04-flow` (ciclo de vida), `u4-02-05-graph` (árbol DML).

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿CREATE TABLE?::Crea tablas con columnas, tipos y restricciones (DDL).
> - ¿ALTER TABLE?::Modifica una tabla existente: ADD, MODIFY, DROP columnas/restricciones.
> - ¿DROP TABLE?::Elimina una tabla. Sin marcha atrás.
> - ¿INSERT?::Inserta registros en una tabla (DML).
> - ¿UPDATE?::Modifica datos existentes con SET y WHERE (DML).
> - ¿DELETE?::Elimina registros con WHERE (DML).
> - ¿PRIMARY KEY?::NOT NULL + UNIQUE; identifica cada fila.
> - ¿FOREIGN KEY?::Referencia la PK de otra tabla; integridad referencial.
> - ¿CHECK?::Los valores deben cumplir una condición específica.
> - ¿PK compuesta?::Varias columnas que juntas identifican la fila (ej. sid, bid, dia).
> - ¿UPDATE sin WHERE?::Modifica TODAS las filas de la tabla.
> - ¿DELETE sin WHERE?::Borra TODAS las filas de la tabla.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[01 - Introducción a SQL]] — qué es SQL, estándares, tipos de datos.
> - [[03 - Consultas Avanzadas]] — JOIN, GROUP BY, subqueries, vistas, triggers.
> - [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — 17 ejercicios resueltos de SQL real.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[03 - Consultas Avanzadas]]
> - Anterior: [[01 - Introducción a SQL]]

---

**Tags:** #TICG1018 #unidad4 #sql #ddl #dml #bd
