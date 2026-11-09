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
> El deck del Ing. Jorge Magallanes abre la unidad de SQL: qué es, de dónde viene y qué promete.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p2.png]]
> 
> **Introducción a SQL (p. 2):** *"Structured Query Language (SQL), es un lenguaje declarativo de acceso a bases de datos que combina construcciones del álgebra relacional y del cálculo relacional"*, desarrollado en los '70 por IBM a partir del cálculo de predicados de Codd. La misma página lista los estándares: SEQUEL (IBM 1976), SQL-86, SQL-89, SQL-92, SQL:1999, SQL:2003 y SQL:2005-2016.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p3.png]]
> 
> **Características (p. 3):** *"Idealmente un lenguaje de DB debería permitir al usuario realizar lo siguiente con un mínimo esfuerzo"*: crear bases de datos y estructuras de relaciones, ejecutar tareas de administración de datos (inserción, modificación y borrado) y realizar consultas simples y complejas.

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
> El estándar SQL no se queda en "texto y número": separa los tipos en escalares exactos, aproximados, de cadena, de fecha y de intervalo.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p5.png]]
> 
> **Tipos escalares (p. 5):** *"los tipos character y bit son referidos como strings"*; los numéricos se dividen en *exact* y *approximate*.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p6.png]]
> 
> **Numéricos exactos (p. 6):** *"números con una representación exacta"*, que *"consisten de precisión y escala"*: precisión = dígitos totales (parte entera + decimal), escala = dígitos a la derecha del punto.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/SQL/bd-s06-p7.png]]
> 
> **Numéricos aproximados (p. 7):** representación inexacta, con notación similar a la científica donde la precisión es la mantisa; `FLOAT(precisión)` y `DOUBLE PRECISION` para cálculos con decimales.

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
