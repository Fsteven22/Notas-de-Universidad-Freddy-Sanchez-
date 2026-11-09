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
> El deck de la unidad de DDL abre con la tabla de los tres lenguajes de SQL y el comando que le corresponde a cada uno.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p7.png]]
> 
> **DDL (p. 7):** `CREATE` crea objetos en la base de datos — tablas, vistas, triggers, etc.; `ALTER` modifica un objeto existente (tabla, vista...); `DROP` elimina un objeto.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p8.png]]
> 
> **DML (p. 8):** `SELECT` consulta datos en la base de datos, `INSERT` inserta registros en las tablas, `UPDATE` modifica o actualiza datos de las tablas y `DELETE` los elimina.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p9.png]]
> 
> **DCL (p. 9):** `GRANT` asigna privilegios a usuarios y `REVOKE` remueve los privilegios asignados.

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
> El deck separa la sintaxis en tres láminas: la forma general, las restricciones de columna y las de tabla.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p22.png]]
> 
> **La forma general (p. 22):** `CREATE TABLE <tbl_name> (<def_col1, def_col2,... restricc_tbl>)`, con cada columna como `<col_name> <col_tipoDato> [DEFAULT def_value] [restricc_col]`. El `DEFAULT` *"agrega un valor a la columna en caso de que no se defina durante el ingreso del registro"*.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p23.png]]
> 
> **Restricciones de columna (p. 23):** `NOT NULL`, `UNIQUE`, `PRIMARY KEY` y `CHECK` se declaran junto a la columna que restringen.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p24.png]]
> 
> **Restricciones de tabla (p. 24):** `UNIQUE (col1, col2, ...)`, `PRIMARY KEY (col1, col2, ...)` y `FOREIGN KEY` se declaran al final, cuando afectan a varias columnas.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p25.png]]
> 
> **Los ejemplos del deck (p. 25):** `films` con su `UNIQUE(fecha_prod)` y su FK a `distribuidores`, y `distribuidores` con el `CHECK` que exige `did > 100` y un nombre no vacío. Son los mismos dos `CREATE TABLE` de arriba.

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
> El deck da los datos y el DDL de las mismas tres tablas del ejemplo.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p26.png]]
> 
> **Los datos (p. 26):** Marineros (sid, snombre, rating, edad), Botes (bid, bnombre, color) y Reservacion (sid, bid, dia) con sus filas — la tabla `Reservacion` es la que se repite por día.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p27.png]]
> 
> **El DDL (p. 27):** `CREATE TABLE Marineros`, `CREATE TABLE Botes` y `CREATE TABLE Reservacion` con la PK compuesta y las dos FKs.

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
> El deck presenta el ALTER como un comando más de DDL, con su forma general y ejemplos.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p31.png]]
> 
> **La forma (p. 31):** `ALTER <elemento> <nombre> <specification1>, <especification2>,...` — por eso el `ALTER TABLE` admite **varias** especificaciones separadas por coma en un solo statement.
> 
> **Los ejemplos (p. 31):** `ALTER TABLE Botes ADD Edad INT`, `ALTER TABLE Marineros MODIFY rating REAL`, `ALTER TABLE Films DROP COLUMN genero` y `ALTER TABLE Botes ADD CONSTRAINT con CHECK (...)`.

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
> El deck dedicó dos láminas al borrado de objetos.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p29.png]]
> 
> **La advertencia (p. 29):** *"Sintáxis para el borrado de un elemento: no tiene marcha atrás"*, con `DROP TABLE films;` como ejemplo.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p30.png]]
> 
> **La familia de comandos (p. 30):** el DROP no es solo de tablas — también de base de datos (`DROP DATABASE`), índices (`DROP INDEX`), triggers (`DROP TRIGGER`) y procedimientos (`DROP PROCEDURE`).

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
> El deck dedicó cuatro láminas al DML: la síntesis, las reglas del INSERT, el UPDATE y el DELETE.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p34.png]]
> 
> **La síntesis (p. 34):** `INSERT` ingresa datos (filas) a la base de datos; `UPDATE` modifica datos de las filas dependiendo de una condición; `DELETE` elimina filas de una tabla.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p35.png]]
> 
> **Las reglas del INSERT (p. 35):** *"el número de ítems debe ser el mismo de las columnas"*, con correspondencia directa entre nombre de columna y lista de valores y compatibilidad de tipos.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p39.png]]
> 
> **El UPDATE (p. 39):** `UPDATE nombreTabla SET columna1 = valor1 [,columna2 = valor2...] WHERE condicion` — y la advertencia de que sin `WHERE` se modifican todas las filas.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-04-p43.png]]
> 
> **El DELETE (p. 43):** `DELETE FROM nombreTabla WHERE condicion` — *"si se omite: se borran todas las filas"*.

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
