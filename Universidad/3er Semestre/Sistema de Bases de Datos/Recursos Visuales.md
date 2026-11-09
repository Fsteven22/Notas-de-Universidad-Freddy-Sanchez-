---
dg-publish: true
tags: [recursos-visuales, bases-de-datos]
---

# 🎬 Recursos Visuales — Bases de Datos

> [!info] ℹ️ Para qué sirve esta página
>
> Videos para entender la materia **viendo y escuchando**, no solo leyendo. Cada link está **verificado** (videoId + título real + canal + duración). **Complementa** las guías y los apuntes del curso: no los sustituye.
>
> **Cómo se usa esta página:** no la recorras de arriba abajo como si fuera una lista de tareas. Elige **un** video cuando una nota concreta te quede encallada: si no entiendes la notación de Chen, ve el de símbolos; si la normalización no te cuadra, ve el de 1FN/2FN/3FN desde cero. La columna *"Para qué sirve"* dice exactamente qué nota desbloquea cada video.
>
> **Por qué no sustituye a las notas:** un video te da la intuición en 10 minutos; la nota te da el vocabulario exacto que la docente usa en los exámenes. Lo ideal es **video primero** (para entender) y **nota después** (para saber decirlo con las palabras correctas).

---

## 📗 Unidad 1 — Modelos de Datos y ER

> [!info] 🎬 Videos de la unidad
>
> | Video | Enlace | Autor y duración | Para qué sirve |
> | --- | --- | --- | --- |
> | MODELO ENTIDAD-RELACIÓN (CONCEPTOS BÁSICOS) | [Link](https://www.youtube.com/watch?v=l5PDQtUVye8) | Eliezer De León, 9:56 | la base conceptual, antes de dibujar. |
> | El DIAGRAMA CONCEPTUAL del Modelo ENTIDAD-RELACIÓN, todo lo que necesitas saber | [Link](https://www.youtube.com/watch?v=6fcNDvQYZk0) | JAB: Programación, 11:30 | el diagrama explicado fácil. |
> | Modelo Entidad Relación - Tutorial Rápido | [Link](https://www.youtube.com/watch?v=NJp-uJGwg6k) | LoboTecnoKu, 3:09 | el video corto para repasar antes de la clase. |
> | Curso modelo entidad relación (MER): aprende a diseñar tus bases de datos | [Link](https://www.youtube.com/watch?v=J-zum0Z96g4) | DiscoDurodeRoer, 23:27 | el método completo de diseño. |
> | ERD Tutorial: qué es y cómo crearlo, parte 1 | [Link](https://www.youtube.com/watch?v=TKuxYHb-Hvc) | Lucid Software Español, 6:43 | la notación en la herramienta. |
> | Símbolos y entidad relación de la Notación Chen | [Link](https://www.youtube.com/watch?v=8vK21XGEoDc) | Arii, 6:46 | los símbolos de Chen uno por uno. |
> | Del DIAGRAMA CONCEPTUAL del modelo Entidad-Relación al ESQUEMA RELACIONAL, desde 0 y con draw.io | [Link](https://www.youtube.com/watch?v=HSkbTPeChb0) | JAB: Programación, 30:42 | el paso de ER a tablas. |
> | Diagrama Entidad-Relación con Draw.io | [Link](https://www.youtube.com/watch?v=SkjaSwvsB20) | Aylin Yepez, 35:10 | el diagrama dibujado en la herramienta del curso. |
>
> **Si solo vas a ver uno:** el de *JAB: Programación* sobre el diagrama conceptual (11:30). Es el que más se parece a cómo lo explica la cátedra, y cubre justo lo que la nota 02 de la Unidad 1 necesita: qué es una entidad, qué es una relación y por qué la cardinalidad se escribe en dos lados.

---

## 📘 Unidad 2 — Modelo lógico y conversión

> [!info] 🎬 Videos de la unidad
>
> | Video | Enlace | Autor y duración | Para qué sirve |
> | --- | --- | --- | --- |
> | NORMALIZACIÓN en BASES DE DATOS \| MASTER CLASS con ejercicio | [Link](https://www.youtube.com/watch?v=kvt2wE-q-yY) | TodoCode, 36:08 | normalización de punta a punta. |
> | Formas Normales (1FN, 2FN y 3FN) desde cero | [Link](https://www.youtube.com/watch?v=RlgbWESXySI) | Viera Class, 7:40 | cada forma normal por separado. |
> | Normalización (1FN, 2FN, 3FN) | [Link](https://www.youtube.com/watch?v=MdYvCMbQji4) | Daniela Bohórquez Escovar, 4:45 | el resumen rápido de las tres formas. |
>
> **Estrategia sugerida:** ve primero el de 4:45 (resumen) y luego el de 7:40 (cada forma por separado). El resumen te da el *qué*; el detallado te da el *por qué* de cada partición, que es justo lo que pide el parcial.
>
> **Ejemplo:** si te enredas con **por qué** partir una tabla, el video de 36:08 es el que lo explica con un ejercicio completo de principio a fin. Pero ojo: usa una notación de dependencias distinta a la de las notas. Úsalo para entender la *intuición* y vuelve a la nota 03 de la Unidad 2 para la notación que sí se examina.

---

## 📙 Unidad 3 — Álgebra Relacional

> [!info] 🎬 Videos de la unidad
>
> | Video | Enlace | Autor y duración | Para qué sirve |
> | --- | --- | --- | --- |
> | Álgebra Relacional: operaciones con ejemplos | [Link](https://www.youtube.com/watch?v=580_6ySKy4Q) | Denisse VM, 15:19 | para la guía de álgebra relacional del Taller 2. |
> | Álgebra Relacional: operadores básicos | [Link](https://www.youtube.com/watch?v=hsNZnJjYXGM) | Antonio FI UPM, 14:33 | selección, proyección y unión uno a uno. |
>
> **Sobre la notación:** los dos videos usan notación distinta a la de la guía (flechas, subíndices). Si los ves, fíjate solo en la **idea** de cada operador (filtrar, proyectar, unir) y usa la guía de la Unidad 3 para la notación que sí se examina.
>
> **Ejemplo:** un `SELECT` con `WHERE` es una **selección** (`σ`) y un `SELECT` con dos columnas es una **proyección** (`π`). Si reconoces eso en SQL, ya tienes el 80% del álgebra relacional sin necesidad de la notación formal.

---

## 📕 Unidad 4 — SQL y PL/SQL

> [!info] 🎬 Videos de la unidad
>
> | Video | Enlace | Autor y duración | Para qué sirve |
> | --- | --- | --- | --- |
> | CONSULTAS SQL: INNER JOIN con práctica | [Link](https://www.youtube.com/watch?v=0BstRqp6Svg) | TodoCode, 8:00 | para el Taller 3. |
> | CONSULTAS SQL: LEFT y RIGHT JOIN con práctica | [Link](https://www.youtube.com/watch?v=nw6tK0E5iyo) | TodoCode, 8:03 | para el Taller 3. |
> | Cómo hacer subconsultas en SQL con ejemplos | [Link](https://www.youtube.com/watch?v=GpC0XyiJPEo) | Becoming a Data Scientist, 8:20 | las subconsultas explicadas en español. |
> | Tutorial avanzado de SQL: subconsultas | [Link](https://www.youtube.com/watch?v=m1KcNV-Zhmc) | Alex The Analyst, 8:37 | los casos que se repiten en los exámenes. |
> | MySQL: SUBQUERIES | [Link](https://www.youtube.com/watch?v=i5acg3Hvu6g) | Bro Code, 6:46 | la sintaxis en la consola. |
> | Intro to correlated subqueries in SQL | [Link](https://www.youtube.com/watch?v=TUxadt94L0M) | We Learn SQL, 4:56 | la subconsulta correlacionada, que es la que cuesta. |
> | Cursores, ejercicios PL/SQL #9 | [Link](https://www.youtube.com/watch?v=VXmPNwz8YSA) | DiscoDurodeRoer, 11:54 | el cursor y su uso. |
> | CURSORES en PL/SQL - ORACLE | [Link](https://www.youtube.com/watch?v=G1xGpbFJ_-c) | Bilbao Labs, 6:48 | la estructura del cursor explícito. |
> | ¿Qué DIABLOS son los CURSORES en SQL? | [Link](https://www.youtube.com/watch?v=4C1cMA-00ag) | hdeleon.net, 10:32 | la idea detrás del cursor. |
> | ¿Qué diablos es un Trigger? ejemplo sencillo en SQL Server | [Link](https://www.youtube.com/watch?v=uTx7xd4ojkk) | hdeleon.net, 10:11 | el trigger con ejemplo mínimo. |
> | Curso de Oracle PL/SQL en español desde cero: TRIGGERS | [Link](https://www.youtube.com/watch?v=MfRjk5AKAiI) | INFORMATICONFIG, 9:37 | la sintaxis completa del trigger. |
>
> **Estrategia sugerida:** si vas al Taller 3, mira primero los dos de JOIN (8 min cada uno) — son el mismo contenido que la consulta 1 del taller, y verlos con ejemplos te ahorra media hora de ensayo y error.
>
> **Cuidado con los cursores:** hay tres videos porque PL/SQL tiene cursor explícito y cursor implícito, y cada video se queda con uno. El de *hdeleon.net* (10:32) es el que mejor explica la **idea**; el de *Informaticonfig* es el único que te da la sintaxis completa de Oracle, que es la que se usa en la cátedra.
>
> **Ejemplo:** el video de triggers de *hdeleon.net* es el que mejor prepara el punto 1 del Taller 4 (el disparador que valida la puntuación de una reseña). Usa SQL Server en vez de Oracle, así que el `DELIMITER` no aparece — pero la idea (`BEFORE INSERT` + validación + error) es idéntica a la que pide el enunciado.

---

## 🔗 Ver también

> [!info] 🔗 Ver también
>
> - [[Índice de Contenido|Índice de Contenido]] — índice de guías, material y lista negra de libros.
> - [[Guía de Problemas 1 - MC, ML y Normalización|Guía de Problemas 1]] — problemas de modelo conceptual, modelo lógico y normalización.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización|Guía de Problemas 2]] — consultas de álgebra relacional y normalización del hotel (Taller 2).
> - [[Guía de Problemas 3 - SQL, PL-SQL y Seguridad|Guía de Problemas 3]] — SQL, transacciones, triggers, usuarios y MongoDB (Talleres 3 y 4).

---

**Tags:** #recursos-visuales #bases-de-datos #TICG1018
