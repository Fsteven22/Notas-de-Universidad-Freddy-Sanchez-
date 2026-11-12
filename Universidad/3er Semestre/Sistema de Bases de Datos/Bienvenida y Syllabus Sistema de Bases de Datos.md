---
dg-publish: true
tags: [TICG1018, bienvenida, syllabus]
---

# 🗄️ Bienvenida y Syllabus Sistema de Bases de Datos

## 🎉 ¡Bienvenido/a a Sistema de Bases de Datos!

> [!info] 👋 Sobre esta materia
>
> | Dato | Detalle |
> |---|---|
> | **Materia** | Sistema de Bases de Datos |
> | **Código** | TICG1018 |
> | **Semestre** | 3ro · PAO 2026-2 |
> | **Docente** | Irene Cheung Ruiz (icheung@espol.edu.ec) — ESPOL, MSc RWTH Aachen |
> | **Horario** | Paralelo 1: Mar y Jue 11:00-13:00 |
> | **Oficina** | Vie 10:30-11:30 (previa cita) + foro 24h + Teams horario laboral |
> | **Plataformas** | Aula Virtual, Teams, Datacamp (cuenta con nombre completo + mail ESPOL + foto) |
> | **Políticas** | 📎 [[Unidad 0 - Guias y Ejercicios/Diapositivas/BD00 Políticas.pdf|BD00 Políticas.pdf]] |
>
> Las diapos usan códigos viejos (TICG1001/CCPG1043): es material reutilizado, el código oficial es TICG1018.

---

## 🎯 Objetivo General

> [!note] 📌 Qué vamos a lograr
>
> Aplicar diseño e implementación de bases de datos con SQL y modelos relacionales para administrar información.

> [!success] ✅ Reglas del juego (políticas)
>
> - 40% de faltas (≈11) = reprobado. Sin celulares en clase (los retiran).
> - Contenido publicado en AV se revisa con anticipación; material de referencia ≠ material de estudio.
> - Tareas semanales sin nota pero **requisito** para asentar lecciones.
> - Proyecto en grupos de 4 (no se disuelven), sustentación individual 5-7 min con preguntas de cualquier parte; sin 75% listo no se revisa.
> - Evaluaciones empezadas: nadie entra ni sale; no hay recuperación.

---

## 📋 Evaluación — 70 + 30

> [!warning] 📊 Cómo se evalúa
>
> **Teórico 70%:** tareas + Lecciones 1-3 y exámenes.
> **Práctico 30%:** proyecto (90 contenido + 10 participación) + talleres + participación.
>
> **Fechas (parciales I-II):**
>
> | Evaluación | Fecha |
> |---|---|
> | Lección 1 | Mar 13-oct, 11:00-12:00 |
> | Lección 2 | Mar 27-oct, 11:00-12:00 |
> | Lección 3 | Mar 10-nov, 11:00-12:00 |
> | Examen final | Mar 12-ene, 14:00-16:00 |
> | Mejoramiento | Mar 26-ene, 14:00-16:00 |

---

## 🗂️ Contenido (lo dado hasta ahora)

> [!tip] 📚 Unidad 1 — Modelos de datos
>
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/bienv-01-map.svg]]
>
> **Se lee así:** el diagrama es la **hoja de ruta de la materia** en dos ramas. Del nodo central (`🗄️ SBD · TICG1018`) sale una flecha hacia **U1 · Modelos y ER** (el bloque conceptual: datos, entidades, modelo relacional) y otra hacia **U2+ · SQL y diseño físico** (el bloque aplicado: convertir ER en tablas, normalizar y escribir SQL).
>
> **Por qué importa:** fíjate en que la división es **conceptual vs. aplicado**, no "semana 1 vs. semana 2". Todo lo de la Unidad 1 (E/R, cardinalidades, modelo relacional) es **diseño**: decidir qué se guarda y cómo se relaciona. Todo lo de la Unidad 2 en adelante es **implementación**: traducir ese diseño a tablas, normalizarlas y consultarlas con SQL. Si una duda no entra en ninguna de las dos ramas, es que todavía no sabes en qué nivel te la están preguntando.
>
> **Ejemplo:** *"¿cuál es la PK de `MATRICULA`?"* es una pregunta de la **Unidad 1** (es un modelo de clave compuesta). *"`SELECT` que sume las ventas por sucursal"* es de la **U2+** (SQL y agregación). Y el **proyecto** de la materia vive en las dos: primero diseñas el ER y lo justificas, y después lo entregas en tablas normalizadas con sus consultas.
>
> | Unidad | Tema | Fuente |
> |---|---|---|
> | **1** | Modelos de datos, ER, relacional | BD01 + unidad1.3-1.5.pdf |
> | **2+** | SQL y resto (cuando la docente avance) | Pendiente AV |
>
> **Bibliografía guía:** C. Coronel, S. Morris, *Database Systems: Design, Implementation, and Management*, 9th ed. (lectura asignada: cap. 4 §§4.1.3–4.1.7). Diapos citan Codd, Chen 1976.

---

**Tags:** #bases-de-datos #ESPOL #TICG1018

