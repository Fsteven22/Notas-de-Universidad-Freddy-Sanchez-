---
dg-publish: true
tags: [TICG1018, unidad4, sql, ddl, dml, create, alter, drop, insert, update, delete, bd]
---

# 🛠️ SQL — DDL y DML

## 🎯 Introducción

> [!info] 💡 ¿Qué hace DDL y qué hace DML?
> DDL (Data Definition Language) define la estructura: crea, modifica y elimina tablas, vistas, índices, triggers. DML (Data Manipulation Language) manipula los datos: inserta, actualiza, borra y consulta.
> **Aplicaciones:**
> - Implementación: toda tabla del proyecto sale de DDL.
> - Operación diaria: INSERT, UPDATE, DELETE, SELECT son DML.
> - Lección 1 (13-oct): CREATE TABLE con restricciones, INSERT, UPDATE, DELETE.

> [!example] 📎 Diapositivas de referencia
> ![[../../Unidad 0 - Guias y Ejercicios/Diapositivas/BD04 DDL_dml_create_alter_drop.pdf]]

---

## 🛠️ DDL — Data Definition Language

### CREATE TABLE

> [!note] 📋 Definición — CREATE TABLE
> Crea una tabla nueva con sus columnas, tipos de datos y restricciones.
> Sintaxis:
> ```sql
> CREATE TABLE nombre_de_tabla (
>   nombre_de_columna tipo_de_dato [DEFAULT expr_default] [restriccion_de_columna[, ...]],
>   [restriccion_de_tabla[, ...]]
> );
> ```
> Tipos de datos: CHAR(n), VARCHAR2(n), INTEGER, NUMERIC, FLOAT, DOUBLE PRECISION, DATE, TIME, TIMESTAMP, SERIAL.
> ```mermaid
graph TD
    A[CREATE TABLE] --> B[Columnas + tipos]
    B --> C[Restricciones PK/FK/CHECK]
    C --> D[Tabla creada]
    style A fill:#e1f5fe
    style D fill:#c8e6c9
```

> [!example] 🧪 Ejemplo de CREATE TABLE
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

### Restricciones de Columna y de Tabla

> [!note] 📋 Definición — Restricciones
> | Restricción | Qué hace |
> |---|---|
> | NOT NULL | La columna no puede ser nula |
> | UNIQUE | Todos los valores de la columna son diferentes |
> | PRIMARY KEY | NOT NULL + UNIQUE; identifica cada fila |
> | FOREIGN KEY | Referencia la clave primaria de otra tabla |
> | CHECK | Los valores cumplen una condición específica |
> | DEFAULT | Valor por defecto si no se especifica uno |
> | INDEX | Índice para recuperar datos rápidamente |

> [!example] 🧪 Ejemplo de restricciones
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

### ALTER TABLE

> [!note] 📋 Definición — ALTER TABLE
> Modifica un objeto existente (tabla, vista, etc.) cuando ya tiene datos.
> Sintaxis:
> ```sql
> ALTER TABLE nombre_tabla {ADD | MODIFY | DROP} elemento [definicion];
> ```

> [!example] 🧪 Ejemplos de ALTER TABLE
> ```sql
> ALTER TABLE Botes ADD COLUMN Edad REAL;
> ALTER TABLE Marineros MODIFY rating REAL;
> ALTER TABLE Distribuidores DROP CONSTRAINT cons1;
> ALTER TABLE Films DROP COLUMN genero;
> ALTER TABLE Botes ADD CONSTRAINT con CHECK (edad < 100);
> ```

### DROP TABLE

> [!note] 📋 Definición — DROP TABLE
> Elimina un objeto de la base de datos. No tiene marcha atrás.
> Sintaxis:
> ```sql
> DROP TABLE nombre_tabla;
> ```

> [!example] 🧪 Ejemplo de DROP TABLE
> ```sql
> DROP TABLE films;
> ```

---

## 🛠️ DML — Data Manipulation Language

### INSERT

> [!note] 📋 Definición — INSERT
> Inserta registros en una tabla. El número de ítems debe coincidir con el número de columnas.
> Sintaxis:
> ```sql
> INSERT INTO nombreTabla[(lista_columnas)] VALUES (lista_valores);
> ```

> [!example] 🧪 Ejemplos de INSERT
> ```sql
> INSERT INTO Tarjeta VALUES (2, 'Vanessa E', '00112233445567', '2019-07-01');
> 
> INSERT INTO Tarjeta (idTarjeta, nombre_tarjeta, numero_tarjeta, fecha_expiracion)
> VALUES (2, 'Vanessa E', '00112233445567', '2019-07-01');
> ```

### UPDATE

> [!note] 📋 Definición — UPDATE
> Modifica o actualiza datos existentes en una tabla.
> Sintaxis:
> ```sql
> UPDATE nombre_tabla SET columna1 = valor1 [, columna2 = valor2, ...] WHERE condición;
> ```

> [!example] 🧪 Ejemplo de UPDATE
> ```sql
> UPDATE empleado SET salario = 5000 WHERE id = 1;
> ```

### DELETE

> [!note] 📋 Definición — DELETE
> Elimina datos existentes en una tabla.
> Sintaxis:
> ```sql
> DELETE FROM nombre_tabla WHERE condición;
> ```

> [!example] 🧪 Ejemplo de DELETE
> ```sql
> DELETE FROM empleado WHERE id = 1;
> ```

### SELECT básico

> [!note] 📋 Definición — SELECT
> Consulta datos en la base de datos. Es la operación más usada de DML.
> Sintaxis básica:
> ```sql
> SELECT columnas FROM tabla WHERE condición;
> ```

> [!example] 🧪 Ejemplo de SELECT
> ```sql
> SELECT ID, name, dept_name FROM instructor WHERE name LIKE 'A%';
> ```

---

## 🎯 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Crear una tabla con restricciones

> [!example] 📋 Planteamiento
> Escribe el SQL para crear una tabla PRODUCTO con:
> - codigo (entero, PK)
> - nombre (texto hasta 100 caracteres, no nulo)
> - precio (decimal, debe ser mayor a 0)
> - stock (entero, valor por defecto 0)
> > [!success]- ✅ Solución
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
> Dada la tabla PRODUCTO(codigo PK, nombre, precio, stock DEFAULT 0), inserta un producto solo especificando código, nombre y precio (usa el valor por defecto para stock).
> > [!success]- ✅ Solución
> > ```sql
> > INSERT INTO PRODUCTO (codigo, nombre, precio) VALUES (1, 'Laptop', 1200.00);
> > ```

### ✏️ Ejercicio 3 — ALTER para agregar columna

> [!example] 📋 Planteamiento
> A la tabla PRODUCTO agrega una columna categoria (texto hasta 50 caracteres).
> > [!success]- ✅ Solución
> > ```sql
> > ALTER TABLE PRODUCTO ADD COLUMN categoria VARCHAR(50);
> > ```

### ✏️ Ejercicio 4 — UPDATE con condición

> [!example] 📋 Planteamiento
> Aumenta el precio en un 10% a todos los productos de la categoría 'Electrónica'.
> > [!success]- ✅ Solución
> > ```sql
> > UPDATE PRODUCTO SET precio = precio * 1.10 WHERE categoria = 'Electrónica';
> > ```

### ✏️ Ejercicio 5 — DELETE con subconsulta

> [!example] 📋 Planteamiento
> Borra los productos que tienen stock 0 y pertenecen a la categoría 'Descontinuados'.
> > [!success]- ✅ Solución
> > ```sql
> > DELETE FROM PRODUCTO WHERE stock = 0 AND categoria = 'Descontinuados';
> > ```

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
> - Escribo un CREATE TABLE con PK y al menos una restricción.
> - Hago INSERT, UPDATE y DELETE con WHERE.
> - Distingo DDL de DML.

> [!note] 📋 Nivel Intermedio
> - Uso ALTER TABLE para agregar, modificar y eliminar columnas y restricciones.
> - Escribo INSERT especificando solo algunas columnas (usando DEFAULT).
> - Explico por qué DROP TABLE no tiene marcha atrás.

> [!note] 📋 Nivel Avanzado
> - Diseño un esquema completo con múltiples tablas y FKs.
> - Detecto cuándo una restricción CHECK es necesaria vs cuándo se maneja en la aplicación.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
> - ¿CREATE TABLE?::Crea tablas con columnas, tipos y restricciones (DDL).
> - ¿ALTER TABLE?::Modifica una tabla existente: ADD, MODIFY, DROP columnas/restricciones.
> - ¿DROP TABLE?::Elimina una tabla. Sin marcha atrás.
> - ¿INSERT?::Inserta registros en una tabla (DML).
> - ¿UPDATE?::Modifica datos existentes con SET y WHERE (DML).
> - ¿DELETE?::Elimina registros con WHERE (DML).
> - ¿PRIMARY KEY?::NOT NULL + UNIQUE; identifica cada fila.
> - ¿FOREIGN KEY?::Referencia la PK de otra tabla; integridad referencial.
> - ¿CHECK?::Los valores deben cumplir una condición específica.
> [!note] 🧠 Repasa con el plugin Spaced Repetition (Lección 1: 13-oct)

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
> - [[01 - Introducción a SQL]] — qué es SQL, estándares, tipos de datos.
> - [[03 - Consultas Avanzadas]] — JOIN, GROUP BY, subqueries, vistas, triggers.
> - [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — 17 ejercicios resueltos de SQL real.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[03 - Consultas Avanzadas]]
> - Anterior: [[01 - Introducción a SQL]]

---

**Tags:** #TICG1018 #unidad4 #sql #ddl #dml #bd
