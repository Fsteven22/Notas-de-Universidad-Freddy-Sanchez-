---
dg-publish: true
---

# 🧩 Bienvenida y Syllabus Diseño de Software

## 🎉 ¡Bienvenido/a a Diseño de Software!

> [!info] 👋 Sobre esta materia
>
> | Dato | Detalle |
> |---|---|
> | **Materia** | Diseño de Software |
> | **Código** | CCPG1042 |
> | **Semestre** | 3ro · PAO 2026-2 |
> | **Créditos** | 3.8 ECTS |
> | **Horas semanales** | 2h docencia + 2h prácticas + 2h autónomas |
> | **Horario** | Lun y Mié — Par 01: 13:00-14:50 · Par 03: 15:00-16:45 (CL lunes, talleres miércoles) |
> | **Prerrequisito** | Programación Orientada a Objetos |
> | **Docente** | MSc. David Jurado (djurado@espol.edu.ec, djurado@fiec.espol.edu.ec) — oficina por Teams |
> | **Syllabus base** | 📎 [[Unidad 0 - Guias y Ejercicios/SPA-SyllabusEUR_ACE-CCPG1042.pdf\|SPA-SyllabusEUR_ACE-CCPG1042.pdf]] (EUR-ACE) |
> | **Políticas oficiales** | 📎 [[Unidad 0 - Guias y Ejercicios/01aPoliticasCurso-2026-2.pdf\|01aPoliticasCurso-2026-2.pdf]] |
> | **Deck Semana 1** | 📎 [[Unidad 0 - Guias y Ejercicios/01bDisenoSoftware.pdf\|01bDisenoSoftware.pdf]] |
> | **Enlaces Aula Virtual** | 🔗 [[Unidad 0 - Guias y Ejercicios/Enlaces del Aula Virtual\|Enlaces del Aula Virtual]] |

---

## 🎯 Objetivo General

> [!note] 📌 Qué vamos a lograr
>
> Presentar los paradigmas, patrones y técnicas de modelado para desarrollar un sistema que cumpla los requerimientos con calidad, mantenible y extensible — usando construcción de proyectos, control de versiones y marcos de validación.

> [!success] ✅ Resultados de aprendizaje
>
> | # | Capacidad |
> |---|---|
> | 1 | Diseñar software OO robusto, mantenible y escalable |
> | 2 | Aplicar patrones de diseño en diagramas UML para resolver problemas |
> | 3 | Refactorizar código para simplificar mantenimientos futuros |
> | 4 | Usar control de versiones + pruebas unitarias en entorno colaborativo |

---

## 📋 Evaluación

> [!warning] 📊 Evaluación oficial (políticas 2026-2)
>
> **Teórico (EHD):** Examen 50% + Tareas 35% (con coevaluación) + Controles de lectura 15%. 3ra evaluación = 100% examen.
> **Práctico (EHP):** Talleres 100% (grupos con presentes, hasta 4).
> **Lecciones:** 2 en papel reemplazan el examen parcial — 19-oct y 4-nov.
> **Final/mejoramiento:** lunes de semana de exámenes, 14:00-15:30, Aula A107.
>
> **Reglas:** 40% faltas reprueba · celular guardado · puntualidad 10 min · deshonestidad = cero · tareas/talleres solo por AV · auto-registro de grupos.
>
> **Plan semanal oficial (S1-S14):**
>
> | Sem | Tema | Sem | Tema |
> |---|---|---|---|
> | 1 | Políticas + Intro | 8 | Repaso patrones |
> | 2 | Paradigmas | 9 | Patrones comportamiento |
> | 3 | SOLID | 10 | JUnit5 |
> | 4 | UML casos + clases | 11 | Smells |
> | 5 | UML secuencias | 12-13 | Refactoring 1 y 2 |
> | 6 | Patrones creacionales | 14 | Entrega continua / DevOps |
> | 7 | Patrones estructurales | — | — |

---

## 🗂️ Contenido del Curso

> [!tip] 📚 Programa CCPG1042
>
> ```mermaid
> graph LR
>     A[🧩 Diseño SW\nCCPG1042] --> B[U1 Intro<br/>5h]
>     A --> C[U2 Diseño OO<br/>7h]
>     A --> D[U3 Patrones<br/>7h]
>     A --> E[U4 Refactor<br/>5h]
>     A --> F[U5 Pruebas<br/>4h]
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
>     style E fill:#ffe1e1
>     style F fill:#f0e1ff
> ```
>
> | Unidad | Tema | Horas |
> |---|---|---|
> | **1** | Introducción al diseño | 5h |
> | **2** | Diseño orientado a objetos | 7h |
> | **3** | Patrones de diseño | 7h |
> | **4** | Refactorización | 5h |
> | **5** | Pruebas unitarias | 4h |
> | — | Actividades de evaluación | 4h |

---

## 📚 Bibliografía (la que ya tienes en Unidad 0)

> [!quote] 📖 Fuentes oficiales
>
> **Obligatoria:**
> - [1] R. Pressman, B. Maxim, *Software Engineering: A Practitioner's Approach*, 9th ed. → `01_Software Engineering...pdf`
>
> **Adicional (docente):**
> - [2] P. Stevens, *Using UML*, 2nd ed. → `02_Using UML...pdf`
> - [3] A. Shalloway, J. Trott, *Design Patterns Explained*, 2nd ed. → `03_Design patterns explained...pdf`
> - [4] M. Fowler, *Refactoring*, 2nd ed. → `04_Refactoring...2nd Edition...pdf`
> - [5] E. Gamma et al., *Design Patterns (GoF)*, 1st ed., 1994.
> - [6] C. Otero, *Software Engineering Design: Theory and Practice*, 2012.

---

## 🗺️ Índice de Notas

> [!example] 📂 Estructura del repositorio
>
> ```
> 📁 Diseño de Software/
> ├── 📄 Diseño de Software.md (mapa de contenido)
> ├── 📄 Bienvenida y Syllabus Diseño de Software.md  ← estás aquí
> ├── 📁 Unidad 0 - Guias y Ejercicios/
> │   ├── syllabus EUR-ACE + políticas oficiales + deck S1 + 4 libros
> │   └── 📄 Enlaces del Aula Virtual.md (incl. video del docente)
> ├── 📁 Unidad 1 - Introducción al diseño/
> ├── 📁 Unidad 2 - Diseño orientado a objetos/
> ├── 📁 Unidad 3 - Patrones de diseño/
> ├── 📁 Unidad 4 - Refactorización/
> └── 📁 Unidad 5 - Pruebas unitarias/
> ```

---

**Tags:** #diseno-software #ESPOL #CCPG1042
