---
dg-publish: true
tags: [TICG1018, unidad4, sql, introduccion, estandares, bd]
---

# 🗄️ SQL — Introducción

## 🎯 Introducción

> [!info] 💡 ¿Qué es SQL?
>
> SQL (**Structured Query Language**) es un lenguaje declarativo de acceso a bases de datos que combina construcciones del álgebra relacional y del cálculo relacional. Fue desarrollado originalmente en los '70 por IBM en su Research Laboratory de San José a partir del cálculo de predicados creado por Codd.
>
> Como lenguaje declarativo, en SQL se especifica **qué datos se requiere obtener**, no **cómo se obtienen** (el cómo es el método de acceso, que decide el motor).
>
> **Aplicaciones:**
> - **Consultas:** recuperar datos de una o varias tablas.
> - **Definición:** crear tablas, vistas, índices, triggers.
> - **Administración:** usuarios, permisos, seguridad.
> - **Lección 1 (13-oct):** SQL en 1 frase, estándares principales, DDL vs DML vs DCL.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-01-04-flow.svg]]
>
> **Se lee así:** pides el **qué** y el optimizador decide el **cómo** (índices, joins, orden). Si el plan no es el esperado, la respuesta no es "SQL más mágico": es reescribir la consulta o revisar el índice.

> [!info] 📖 El deck de cátedra: qué es SQL (slides06, pp. 1-3)
>
> El deck del Ing. Jorge Magallanes abre la unidad de SQL: qué es, de dónde viene y qué promete.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p2.png]]
>
> **Se lee así:** la lámina (p. 2) es la **ficha de identidad de SQL**, y trae cuatro datos que se preguntan en examen. (1) El **nombre y su origen**: *"Structured Query Language (SQL), es un lenguaje declarativo de acceso a bases de datos que combina construcciones del álgebra relacional y del cálculo relacional"*. (2) La **procedencia**: *"originalmente fue desarrollado en los '70 por IBM en su Research Laboratory de San José a partir del cálculo de predicados creado por Codd"*. (3) La **genealogía**: SEQUEL (IBM, 1976) → SQL-86 → SQL-89 → SQL-92 → SQL:1999 → SQL:2003 → SQL:2005-2016. (4) El **qué trae cada revisión**: SQL-92 fue la "gran revisión", SQL:1999 añadió disparadores y algo de OO, SQL:2003 añadió XML, secuencias y columnas autonuméricas, y SQL:2016 permite búsqueda de patrones.
>
> **Por qué importa:** el punto (1) es la conexión con la Unidad 3: SQL es **álgebra relacional con sintaxis**. Lo que en álgebra escribías `π DESCRIPCION (σ CODIGO = 104 (PRODUCTO))`, en SQL lo escribes `SELECT DESCRIPCION FROM PRODUCTO WHERE CODIGO = 104`. No es "parecido": es la misma operación con otra notación. Y el punto (2) explica el diseño: viene del **cálculo de predicados**, que es declarativo — por eso SQL dice *qué* quieres y no *cómo* obtenerlo.
>
> **Ejemplo:** el dato de SQL:2003 ("columnas autonuméricas") es la historia de tu `id INT AUTO_INCREMENT` de MySQL: el estándar lo llamó "columnas generadas" y cada motor le puso su nombre. Conocer la genealogía del estándar explica por qué dos motores que "siguen el estándar" tienen sintaxis distintas para lo mismo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p3.png]]
>
> **Se lee así:** la lámina (p. 3) es la que **organiza toda la unidad**, porque divide SQL en dos grupos. Arriba, el **ideal** de un lenguaje de bases de datos: crear bases de datos y estructuras de relaciones, ejecutar tareas de administración de datos (inserción, modificación y borrado) y realizar consultas simples y complejas, todo *"con un mínimo esfuerzo"*. Abajo, la **división oficial**: **DDL** (*Data Definition Language*), para definir la estructura de la base y controlar el acceso a los datos; y **DML** (*Data Manipulation Language*), para recuperar y actualizar datos.
>
> **Por qué importa:** la frase que cierra la lámina es la más importante de toda la unidad de SQL: *"SQL es un lenguaje en donde se especifica **qué** datos se requiere obtener, en lugar de **cómo** se obtienen. El cómo se obtienen se refiere al método de acceso"*. Esa es la definición de **declarativo**, y es la que explica el diagrama del principio de la nota: tú pides el qué, el optimizador decide el cómo (índices, joins, orden).
>
> **Ejemplo:** la diferencia se ve entre `SELECT * FROM VENTA WHERE CANTIDAD > 50` y un `SELECT` con `JOIN`s explícitos, índices forzados y `ORDER BY` manual. El primero dice *"dame las ventas de más de 50 unidades"* y deja que el motor decida. El segundo dice *"cómo* obténgalas" — y por eso el primero es el que se puede **optimizar** y el segundo, no.

---

## 📋 Definiciones Formales

### 1️⃣ Estándares SQL

> [!note] 📋 Definición — Estándares SQL
>
> Existe un compendio de revisiones del estándar SQL definidos por ANSI e ISO:
>
> | Estándar | Año | Novedad principal |
> |---|---|---|
> | SEQUEL | 1976 | IBM, precursor de SQL |
> | SQL-86 (SQL1) | 1986 | Primer estándar ANSI |
> | SQL-89 | 1989 | Revisión menor |
> | SQL-92 (SQL2) | 1992 | Gran revisión del estándar |
> | SQL:1999 (SQL3) | 1999 | Añade disparadores, OO, y más |
> | SQL:2003 | 2003 | Añade XML, secuencias, columnas autonuméricas |
> | SQL:2005, 2008, 2011, 2016 | 2005-2016 | Búsqueda de patrones, y más |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-01-01-graph.svg]]
>
> **Se lee así:** la línea del tiempo va de un lenguaje de una sola empresa (SEQUEL, IBM 1976) a un estándar internacional que se revisa cada pocos años. SQL:1999 es el salto grande (disparadores, orientación a objetos) y la línea sigue abierta: por eso "el SQL" nunca es una sola versión.

### 2️⃣ Grupos de lenguaje — DDL, DML y DCL

> [!note] 📋 Definición — Características de SQL
>
> Idealmente, un lenguaje de base de datos debería permitir al usuario realizar con el mínimo esfuerzo:
>
> 1. **Crear bases de datos y estructuras de relaciones** (tablas, vistas, índices).
> 2. **Ejecutar tareas de administración de datos:** inserción, modificación y borrado de datos desde las relaciones.
> 3. **Realizar consultas (queries) simples y complejas.**
>
> Como lenguaje, el estándar ISO SQL define dos grupos principales:
>
> | Grupo | Nombre completo | Qué hace |
> |---|---|---|
> | **DDL** | Data Definition Language | Define la estructura de la BD y controla el acceso a los datos |
> | **DML** | Data Manipulation Language | Recupera y actualiza datos. Embebido en lenguajes de programación |
> | **DCL** | Data Control Language | Asigna y remueve privilegios a usuarios (GRANT, REVOKE) |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-01-02-graph.svg]]
>
> **Ojo:** el deck dice "dos grupos principales" y luego lista **tres** (DDL, DML, DCL) — el "dos" cuenta DDL y DML, y DCL se agrega después. Memoriza la tabla de abajo, no el número.

> [!example] 🧪 Ejemplo de clasificación
>
> | Comando | Grupo | Qué hace |
> |---|---|---|
> | `CREATE TABLE` | DDL | Crea objetos: tablas, vistas, triggers |
> | `ALTER TABLE` | DDL | Modifica un objeto existente |
> | `DROP TABLE` | DDL | Elimina un objeto |
> | `SELECT` | DML | Consulta datos |
> | `INSERT` | DML | Inserta registros |
> | `UPDATE` | DML | Modifica datos existentes |
> | `DELETE` | DML | Elimina datos |
> | `GRANT` | DCL | Asigna privilegios a usuarios |
> | `REVOKE` | DCL | Remueve privilegios asignados |
>
> **Se lee así:** `CREATE TABLE` define estructura (DDL), `SELECT` recupera datos (DML), `GRANT` asigna privilegios (DCL). Todo comando cae en una de las tres.

### 3️⃣ Tipos de datos atómicos

> [!note] 📋 Definición — Tipos de datos atómicos
>
> Todos los atributos deben tener un tipo de dato atómico estándar de SQL:
>
> | Tipo | Qué guarda | Ejemplo |
> |---|---|---|
> | `CHAR(n)` | Cadena de caracteres de tamaño fijo | `'SMITH'` (rellena con espacios) |
> | `VARCHAR(n)` | Cadena de caracteres de tamaño variable | `'SMITH'` (guarda solo lo escrito) |
> | `INT` / `INTEGER` | Números enteros | `42` |
> | `FLOAT` / `REAL` | Números decimales | `3.14` |
> | `MONEY` | Monetario | `19.99` |
> | `DATETIME` / `DATE` / `TIME` | Fecha y hora | `'2026-11-07'` |
> | `SERIAL` / `AUTO_INCREMENT` | ID único para indexar y referencia | `1, 2, 3...` |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u4-01-03-graph.svg]]
>
> **Ejemplos:** `SERIAL` es el atajo para el "id único" que en SQL es una clave primaria de un solo atributo; `MONEY` es un tipo del estándar, aunque cada motor lo implementa con su propio sabor (el nombre literal `MONEY` no siempre existe).

> [!tip] 💡 CHAR vs VARCHAR
>
> `CHAR(20)` guarda exactamente 20 caracteres (rellena con espacios si es necesario). `VARCHAR(50)` guarda solo los caracteres que se escriben, ahorrando espacio.

> [!info] 📖 El deck de cátedra: los tipos de datos del estándar (slides06, pp. 4-7)
>
> El estándar SQL no se queda en "texto y número": separa los tipos en escalares exactos, aproximados, de cadena, de fecha y de intervalo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p4.png]]
>
> **Se lee así:** la lámina (p. 4) es la **portada del bloque**: *"Data Definition: Tipos de datos SQL"*. Es un separador, pero conviene saber que existe porque te dice que lo que viene es **DDL**: la definición de la estructura. Los tipos de datos son parte de la **estructura**, no de los datos.
>
> **Por qué importa:** esa distinción es la que separa DDL de DML. `INT`, `VARCHAR(30)` y `DECIMAL(10,2)` son **declaraciones de estructura**: viven en el `CREATE TABLE` y se cambian con `ALTER TABLE`. Un `INSERT` no declara un tipo: solo mete un valor en una estructura que ya lo tiene.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p5.png]]
>
> **Se lee así:** la lámina (p. 5) es la **taxonomía completa de los tipos escalares**, y hay que leerla como un mapa de **cuatro familias**. La tabla del centro clasifica: `BOOLEAN`; los *character* `CHAR` y `VARCHAR`; los *bit* `BIT` y `BIT VARYNG`; los *exact numeric* `NUMERIC`, `DECIMAL`, `INTEGER`, `SMALLINT`, `BIGINT`; los *approximate numeric* `FLOAT`, `REAL`, `DOUBLE PRECISION`; los *datetime* `DATE`, `TIME`, `TIMESTAMP`; `INTERVAL`; y los *large objects* `CHARACTER LARGE OBJECT` y `BINARY LARGE OBJECT`.
>
> **Por qué importa:** fíjate en el detalle de la esquina inferior derecha: *"character consiste en una secuencia de caracteres. Cuando se define una columna de este tipo se debe especificar la longitud: fija o variable. Ejemplo: `branchNo CHAR(4)`, `address VARCHAR(30)`"*. Ahí está el origen de la discusión `CHAR` vs `VARCHAR` de esta nota: en el estándar son **dos tipos distintos**, no una abreviatura del mismo.
>
> **Ejemplo:** `branchNo CHAR(4)` es el código de sucursal: siempre 4 caracteres, padded con espacios. `address VARCHAR(30)` es la dirección: hasta 30, los que se escriban. Si el estándar no hubiera distinguido longitud fija de variable, el motor no podría saber cuánto espacio reservar.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p6.png]]
>
> **Se lee así:** la lámina (p. 6) desarrolla los **numéricos exactos**: *"números con una representación exacta. Consisten de precisión y escala: la precisión es el número de dígitos que incluye los de la parte entera y decimal. La escala es el número de lugares decimales"*. Y el ejemplo visual es el que hay que recordar: `1 2 . 3 4 5` → **precisión 5, escala 3**. Los tipos de esta familia son `NUMERIC(precision, scale)`, `DECIMAL(precision, scale)`, `INTEGER`, `SMALLINT` y `BIGINT`.
>
> **Por qué importa:** la **precisión y la escala son cosas distintas**, y confundirlas es el error más común al elegir un tipo. La precisión es el **tope de dígitos**; la escala es **cuántos de esos dígitos son decimales**. `DECIMAL(10,2)` admite hasta 8 dígitos enteros y 2 decimales, no "10 enteros y 2 decimales".
>
> **Ejemplo:** el deck propone un caso real: una columna `rooms` que representa el número de cuartos de una propiedad → `rooms SMALLINT`. La razón es que el rango de `SMALLINT` (hasta 32767) es de sobra y ocupa menos espacio que `INTEGER`. Elegir el tipo más **justo** para el dominio es lo que hace un diseño sólido.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p7.png]]
>
> **Se lee así:** la lámina (p. 7) cierra con los **numéricos aproximados** y los demás grupos. Aproximados: *"números con una representación inexacta. La notación es similar a la notación científica, donde la precisión es la mantisa"*, con los tipos `FLOAT[precision]`, `REAL` y `DOUBLE PRECISION`. `datetime`: `DATE` (con `YEAR`, `MONTH`, `DAY`), `TIME` (con `HOUR`, `MINUTE`, `SECOND`) y `TIMESTAMP` (que guarda DATE y TIME juntos). Y *large objects*: `BLOB` (binario) y `CLOB` (texto largo), para archivos de texto largos o archivos gráficos.
>
> **Por qué importa:** la diferencia entre **exacto** y **aproximado** no es cosmética, es de **resultados**. En un tipo exacto, `0.1 + 0.2 = 0.3` (el motor guarda la representación decimal exacta). En un tipo aproximado (binario en coma flotante), el resultado puede ser `0.30000000000000004`. Por eso **los valores de dinero nunca deben ir en `FLOAT`**: van en `DECIMAL`, y el error de redondeo se acumula en cada suma.
>
> **Ejemplo:** una columna `precio DECIMAL(10,2)` guarda `19.99` exacto. La misma columna como `FLOAT` devolvería `19.989999999999998` al consultarla, y al sumar 1000 precios el total no cuadra con el centavo. Es el motivo por el que los motores  el error "no uses FLOAT para dinero".

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Identificar el grupo de un comando

> [!example] 📋 Planteamiento
>
> Clasifica cada comando en DDL, DML o DCL:
>
> - `CREATE TABLE departamento (...)`
> - `SELECT nombre FROM empleado`
> - `GRANT SELECT ON tabla TO usuario`
> - `UPDATE empleado SET salario = 5000 WHERE id = 1`
> - `DROP VIEW vista_ventas`
>
> > [!success]- ✅ Solución
> >
> > - `CREATE TABLE` → DDL
> > - `SELECT` → DML
> > - `GRANT` → DCL
> > - `UPDATE` → DML
> > - `DROP VIEW` → DDL

### ✏️ Ejercicio 2 — Elegir el tipo de dato

> [!example] 📋 Planteamiento
>
> Para cada atributo, elige el tipo de dato SQL más apropiado:
>
> - cédula de identidad
> - nombre completo
> - salario mensual
> - fecha de nacimiento
> - número de teléfono
>
> > [!success]- ✅ Solución
> >
> > - cédula: `VARCHAR(20)` (puede tener letras y guiones)
> > - nombre completo: `VARCHAR(100)`
> > - salario mensual: `DECIMAL(10,2)` o `MONEY`
> > - fecha de nacimiento: `DATE`
> > - número de teléfono: `VARCHAR(20)` (puede tener +, -, paréntesis)

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino SQL en una frase.
> - [ ] Distingo DDL, DML y DCL con un ejemplo cada uno.
> - [ ] Elijo el tipo de dato SQL apropiado para un atributo dado.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Nombro los estándares SQL principales y su año.
> - [ ] Explico la diferencia entre CHAR y VARCHAR.
> - [ ] Clasifico cualquier comando SQL en su grupo correcto.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Explico por qué SQL es declarativo y qué implica eso para el optimizador.
> - [ ] Diseño el esquema de tipos de datos para una base de datos completa.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - Diapositivas del Ing. Jorge Magallanes: `2026_1PAO_slides6_1_TICG1018.pdf` — Lenguaje de Consultas SQL (pp. 1-19).
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 8 — el modelo relacional y el lenguaje SQL.
> - Guía: [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — 17 ejercicios resueltos de SQL real.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u4

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿SQL en 1 frase?::Lenguaje declarativo de acceso a bases de datos que combina álgebra y cálculo relacional.
> - ¿DDL?::Data Definition Language: define la estructura de la BD y controla el acceso.
> - ¿DML?::Data Manipulation Language: recupera y actualiza datos.
> - ¿DCL?::Data Control Language: asigna y remueve privilegios (GRANT, REVOKE).
> - ¿CHAR vs VARCHAR?::CHAR es tamaño fijo (rellena con espacios); VARCHAR es variable (guarda solo lo escrito).
> - ¿Estándar SQL-92?::Gran revisión del estándar (1992).
> - ¿SQL:1999?::Añade disparadores, OO, y más.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[02 - DDL y DML]] — cómo crear tablas y manipular datos.
> - [[03 - Consultas Avanzadas]] — JOIN, GROUP BY, subqueries, vistas, triggers.
> - [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — 17 ejercicios resueltos de SQL real.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[02 - DDL y DML]]
> - Guía de ejercicios: [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad]]

---

**Tags:** #TICG1018 #unidad4 #sql #introduccion #estandares #bd
