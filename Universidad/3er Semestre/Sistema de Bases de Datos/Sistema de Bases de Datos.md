---
dg-publish: true
tags: [TICG1018, bases-de-datos, mapa-de-contenido]
---

# 🗄️ Sistema de Bases de Datos

> [!info] ℹ️ Mapa de contenido de la materia
>
> Esta nota es el acceso directo a Sistema de Bases de Datos. Se actualiza a mano para que funcione igual en Obsidian y en Neonotes.
>
> **Cómo se lee este mapa:** cada bloque es una unidad del curso. Las notas numeradas (`01`, `02`, `03`…) son las **lecciones**: todas siguen el mismo guion — qué es el concepto, cómo se aplica, qué errores te vas a topar y qué ejercicios para practicar. Las **guías de problemas** (`Guía de Problemas N`) no repiten la teoría: son ejercicios resueltos con material real de la carrera (talleres, participaciones, exámenes).
>
> **Si solo tienes 20 minutos hoy:** lee la Introducción y las Definiciones Formales de la primera nota de la unidad, y haz un ejercicio de la guía. El orden del bloque inferior (Unidad 0) es el orden en que la cátedra va soltando el material: policies → introducción → modelo conceptual → conversión.

---

## 📗 Unidad 1 — Modelos de Datos y ER

> [!tip] 🎯 De los archivos a las tablas
>
> En esta unidad pasas de *"¿qué es un dato?"* a *"dibuja mi modelo"*. Es el lenguaje en el que se habla de bases de datos: el **modelo conceptual** (entidades, atributos, relaciones) y el **modelo relacional** (tablas, claves, tuplas).
>
> - [[01 - Dato, información y modelos de datos]] — de qué son datos e información y por qué los archivos conectados fallan; los tres modelos que nos trajeron hasta aquí.
> - [[02 - Entidades, atributos, claves y relaciones]] — el vocabulario del MER: entidad fuerte y débil, claves candidatas, cardinalidad, generalización.
> - [[03 - Modelo relacional, ERM y casos Tiny College]] — las tablas del modelo relacional y el caso completo de Tiny College, de principio a fin.
>
> **Material de la unidad:** `unidad1.3-1.5.pdf` (modelo conceptual, relacional y ERM) y `BD01 Introducción_datamodel.pdf` + `BD01 Introducción-1.pdf` (intro y archivos vs BD).

---

## 📘 Unidad 2 — Modelo Lógico y Conversión

> [!tip] 🎯 Del diagrama a las tablas, y de las tablas al orden
>
> Aquí el diagrama conceptual se **traduce**: cada cardinalidad se convierte en una regla concreta de dónde va la clave foránea. Y después se **ordena**: el modelo entra al protocolo de normalización hasta llegar a 3FN/BCNF.
>
> - [[01 - Conversión MC a ML por cardinalidad]] — las reglas de conversión (1:1, 1:M, M:N, recursivas, supertipo-subtipo) con el diagrama de decisión.
> - [[02 - Primera forma normal y diccionario de datos]] — el piso: una celda, un valor; y cómo documentar el esquema resultante.
> - [[03 - Segunda y tercera forma normal]] — las parciales y las transitivas, con sus anomalías de inserción, actualización y borrado.
> - [[04 - Normalización paso a paso]] — el protocolo completo, de la 1FN al chequeo BCNF, con el diagrama de dependencias.
>
> **Material de la unidad:** `BD 02 MC_a_ML.pdf` (conversión MC→ML, 1FN y diccionario de datos).

---

## 📙 Unidad 3 — Álgebra Relacional

> [!tip] 🎯 El lenguaje que pregunta a la base de datos
>
> El álgebra relacional es el idioma con el que se **expresa** una consulta antes de escribir SQL. Cada operador es un paso: filtra (`σ`), proyecta (`π`), une (`⨝`), agrega (`γ`), renombra (`ρ`).
>
> - [[01 - Operadores Básicos]] — selección, proyección y diferencia: el núcleo con el que se resuelve casi todo.
> - [[02 - Operadores Derivados y Joins]] — los joins (natural, equi, theta, outer) y la intersección como operador derivado.
> - [[03 - Renombre y Agregación]] — `ρ` para evitar colisiones de nombre y `γ` para agrupar y contar.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización|Guía de Problemas 2]] — el Taller 2 resuelto: 4 consultas de álgebra + la normalización del hotel.
>
> **Material de la unidad:** `2026_1PAO_slides5_1_TICG1018.pdf` (álgebra relacional).

---

## 📕 Unidad 4 — SQL

> [!tip] 🎯 De la pregunta a la sentencia
>
> Última unidad: aquí el álgebra se convierte en **SQL real** — DDL para crear, DML para tocar datos, y consultas con joins, subconsultas y funciones de ventana. Se cierra con lo que se usa en la vida profesional: transacciones, triggers, procedimientos y seguridad.
>
> - [[01 - Introducción a SQL]] — qué es SQL, el papel de cada dialecto (DDL / DML / DCL) y cómo se guarda y consulta.
> - [[02 - DDL y DML]] — `CREATE`, `ALTER`, `DROP` e `INSERT`, `UPDATE`, `DELETE`, con las restricciones que el motor te va a reclamar.
> - [[03 - Consultas Avanzadas]] — joins, subconsultas, CTE, funciones de ventana y agregaciones.
> - [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad|Guía de Problemas 3]] — los Talleres 3 y 4 resueltos: SQL, transacciones, triggers, usuarios y MongoDB.
>
> **Material de la unidad:** `BD04 DDL_dml_create_alter_drop.pdf` y `SQL Avanzado.pptx`.

---

## 📂 Unidad 0 — Guías y Ejercicios

> [!info] 📂 Material de apoyo
>
> - 🔗 [[Guía de Problemas 1 - MC, ML y Normalización|Guía de Problemas 1]] — Control 1: modelo conceptual, modelo lógico y normalización.
> - 🔗 [[Guía de Problemas 2 - Álgebra Relacional y Normalización|Guía de Problemas 2]] — Taller 2: consultas de álgebra relacional y normalización.
> - 🔗 [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad|Guía de Problemas 3]] — Talleres 3 y 4: SQL, transacciones, triggers y usuarios.
> - `BD00 Políticas.pdf` — docente, horario, fechas, proyecto.
> - `BD01 Introducción_datamodel.pdf` + `BD01 Introducción-1.pdf` — intro y archivos vs BD.
> - `unidad1.3-1.5.pdf` — modelo conceptual, relacional y ERM.
> - `BD 02 MC_a_ML.pdf` — conversión MC→ML, 1FN y diccionario.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Syllabus completo: [[Bienvenida y Syllabus Sistema de Bases de Datos]]
> - Plataformas: Aula Virtual, Teams, Datacamp
> - Videos por tema: [[Recursos Visuales|Recursos Visuales]]
> - Índice completo de archivos: [[Índice de Contenido|Índice de Contenido]]

---

**Tags:** #bases-de-datos #ESPOL #TICG1018
