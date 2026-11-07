---
dg-publish: true
tags: [indice, base-de-datos, 3er-semestre, unidad0, recursos, ticg1018]
---

# 📂 Índice de Contenido — Sistema de Bases de Datos

> [!info] ℹ️ Portal de material de la materia
> Este es el **índice único** de **Sistema de Bases de Datos** (3er Semestre · PAO 2-2026).
> Reúne el material de la Unidad 0 (diapositivas, exámenes, talleres, lecciones, scripts SQL,
> modelos de base de datos, proyecto y participaciones) y los puntos de entrada a las demás unidades.
>
> Cada archivo enlazado se abre o se descarga desde el sitio web. Lo que no se publica
> (por copyright o por peso) queda solo en tu vault local.

## 🧭 Navegación por la materia

> [!note] 💛 Syllabus
> ![[Unidad 0 - Guias y Ejercicios/Diagramas/bienv-01-map.svg]]
> Ver [[Bienvenida y Syllabus Sistema de Bases de Datos|Bienvenida y Syllabus]] — objetivos, evaluación y contenido.

> [!tip] 🚪 Entradas por unidad
> Primera nota de cada bloque: el punto de partida.
> - [[Unidad 1 - Modelos de Datos y ER/01 - Dato, información y modelos de datos|01 - Dato, información y modelos de datos]] — *Unidad 1 - Modelos de Datos y ER*
> - [[Unidad 2 - Modelo lógico y conversión/01 - Conversión MC a ML por cardinalidad|01 - Conversión MC a ML por cardinalidad]] — *Unidad 2 - Modelo lógico y conversión*
> - [[Unidad 3 - SQL y PL-SQL/Guía de Problemas 3 - SQL, PL-SQL y Seguridad|Guía de Problemas 3 - SQL, PL-SQL y Seguridad]] — *Unidad 3 - SQL y PL-SQL*

> [!note] 🗂️ Notas de la materia
> - [[Sistema de Bases de Datos|Sistema de Bases de Datos]] — índice de la materia.
> - [[Unidad 0 - Guias y Ejercicios/Material de clase/Recursos Visuales|Recursos Visuales]] — diagramas y capturas de las unidades.
> - [[01 - Dato, información y modelos de datos]] — *U1 · Dato, información y modelos*
> - [[02 - Entidades, atributos, claves y relaciones]] — *U1 · Entidades y claves*
> - [[03 - Modelo relacional, ERM y casos Tiny College]] — *U1 · Modelo relacional*
> - [[04 - Normalización paso a paso]] — *U2 · Normalización*

---

## 📦 Paquete único de scripts y modelos

> [!note] 📦 ZIP: Scripts SQL, Modelos y Textos de Apoyo
>
> **Archivo:** [[Unidad 0 - Guias y Ejercicios/Archivos/Bases de Datos/BD - Scripts SQL Modelos y Textos de Apoyo.zip|BD - Scripts SQL Modelos y Textos de Apoyo.zip]]
>
> Un solo archivo comprimido con los 25 archivos sueltos que **no tienen formato web**
> (`.sql`, `.mwb`, `.txt`): el sitio no los puede previsualizar, así que van todos juntos.
> Descargalo una vez y tenés todo a mano.
>
> **¿Qué hay adentro?**
> - **`.sql`** → scripts de base de datos (tablas, datos de ejemplo, consultas). Abrilos en MySQL Workbench, phpMyAdmin o cualquier cliente SQL.
> - **`.mwb`** → modelo de base de datos hecho en MySQL Workbench. Abrilo con MySQL Workbench para ver el diagrama Entidad-Relacional.
> - **`.txt`** → textos de consulta, respuestas de participaciones y notas sueltas.
>
> **¿Qué NO hay adentro?**
> - El video del proyecto (`VideoBSDPrimerParcial.mp4`) quedó fuera por peso y está en `_no-publicar.txt`.
> - Los diagramas (`.svg`, `.drawio`) no entran acá: están en la carpeta `Diagramas/` y se listan más abajo.
> - El código Python del CRUD (`Crud_Grupo8/*.py`) tampoco entra: queda solo en el vault local.

### Qué hay en el ZIP, archivo por archivo

> [!note] 📜 Contenido del paquete
>
> Los archivos van con la misma estructura de carpetas que tenés en el vault.
>
> | Dentro del ZIP | Qué es |
> |---|---|
> | `Archivos/Bases de Datos/Northwind/northwind.sql` | Esquema Northwind: clientes, órdenes y productos. |
> | `Archivos/Bases de Datos/Northwind/northwind-data.sql` | Datos de ejemplo para poblar Northwind. |
> | `Archivos/Bases de Datos/crm_completo_20.sql` | Script CRM completo: crear y poblar una base de gestión de clientes. |
> | `Archivos/Bases de Datos/iswc.sql` | Script ISWC: base de datos de ejemplo para práctica. |
> | `Archivos/Bases de Datos/mercado.sql` | Modelo de ventas de un mercado/supermercado. |
> | `Archivos/Bases de Datos/proyectos.sql` | Gestión de proyectos y tareas. |
> | `Archivos/Bases de Datos/psicotest.sql` | Base de datos de pruebas psicológicas (Taller 4). |
> | `Archivos/Bases de Datos/supermercado.mwb` | Modelo MySQL Workbench: diagrama Entidad-Relacional de un supermercado. |
> | `Archivos/SQL/ddl joins.sql` | Sentencias DDL y ejemplos de JOINs. |
> | `Archivos/SQL/sp_triggers_fun 2025.sql` | Procedimientos almacenados, triggers y funciones. |
> | `Archivos/SQL/subscription_queries.sql` | Consultas de suscripción y registro. |
> | `Archivos/Participaciones/Participación 1 2025 PAO 1/Participación 1 2025 PAO 1.txt` | Respuesta escrita a la Participación 1. |
> | `Archivos/Participaciones/Participación 2 2025 PAO 1/Participación 2 2025 PAO 1.txt` | Respuesta escrita a la Participación 2. |
> | `Archivos/Participaciones/Participación 4 2025 PAO 1/Participación 4 2025 PAO 1.txt` | Respuesta escrita a la Participación 4. |
> | `Archivos/Participaciones/Participación 4 2025 PAO 1/Participacion 4 Grupo 8.sql` | Script SQL del grupo 8 para la Participación 4. |
> | `Archivos/Participaciones/Participación 4 2025 PAO 1/iswc.sql` | Script ISWC usado en la Participación 4. |
> | `Archivos/Participaciones/Participación 5 2025 PAO 1/Participación 5 2025 PAO 1.txt` | Respuesta escrita a la Participación 5. |
> | `Archivos/Participaciones/Participación 5 2025 PAO 1/Solución John Carreño.txt` | Solución individual a la Participación 5. |
> | `Archivos/Proyecto/Segundo Parcial/ProyectoGrupo8.sql` | Script SQL final del proyecto del grupo 8. |
> | `Material de clase/MongoDB.txt` | Notas sueltas sobre MongoDB (bases de datos no relacionales). |
> | `Talleres/Taller 2 2025 PAO 1/EntradasDB_con_datos.sql` | Script con los datos de entrada del Taller 2. |
> | `Talleres/Taller 3 2025 PAO 1/Taller3 Grupo8.sql` | Script SQL del grupo 8 para el Taller 3. |
> | `Talleres/Taller 4 2025 PAO 1/Taller 4 2025 PAO 1.txt` | Enunciado/respuesta del Taller 4. |
> | `Talleres/Taller 4 2025 PAO 1/Taller 4 JohnCarreño.txt` | Solución individual al Taller 4. |
> | `Talleres/Taller 4 2025 PAO 1/psicotest.sql` | Script psicotest para el Taller 4. |

### Bases de datos de ejemplo

> [!note] 🗃️ Para practicar con datos listos
>
> Estas dos bases vienen comprimidas **aparte** (no están dentro del ZIP de scripts).
> Descargalas si querés practicar consultas sobre datos reales de ejemplo.
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Bases de Datos/sakila-db.zip]] | Base Sakila de MySQL (alquiler de películas) comprimida: sirve para practicar joins, agregaciones y normalización. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Bases de Datos/world-db.zip]] | Base World de MySQL (países, ciudades, idiomas) comprimida: sirve para practicar agregaciones y consultas geográficas. |

---

## 🎞️ Diapositivas

> [!example] Presentaciones del curso
> Cada PDF se abre con el visor embebido del sitio; los PPTX se descargan.
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides01_1_TICG1018.pdf]] | Slides 01 · Introducción al curso (TICG1018). |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides02_final_1_TICG1018.pdf]] | Slides 02 · Presentación final del curso. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides3_final_1_TICG1018.pdf]] | Slides 03 · Presentación final del curso. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides4_1_TICG1018.pdf]] | Slides 04 · Material del curso. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides5_1_TICG1018.pdf]] | Slides 05 · Material del curso. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides6_1_TICG1018.pdf]] | Slides 06 · Material del curso. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/3.1 Operaciones Básicas_2025.pdf]] | Operaciones básicas del álgebra relacional (selección, proyección, unión). |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/3.2 Operaciones Derivadas-join-order2026.pdf]] | Operaciones derivadas y orden de joins. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/3.4 Operaciones Derivadas-agregacion.pdf]] | Operaciones derivadas: agregación y agrupamiento. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Algebra Relacional.pptx]] | Álgebra relacional: operadores y equivalencias. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/BD 02 MC_a_ML.pdf]] | Del modelo conceptual (MC) al modelo lógico (ML). |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/BD 02.3 Normalizacion.pdf]] | Normalización: 1FN, 2FN, 3FN y dependencias. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/BD00 Políticas.pdf]] | Políticas del curso (rúbrica, entregas y evaluaciones). |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/BD01 Introducción-1.pdf]] | Introducción a las bases de datos (parte 1). |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/BD01 Introducción_datamodel.pdf]] | Introducción al modelo de datos. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/BD04 DDL_dml_create_alter_drop.pdf]] | DDL y DML: CREATE, ALTER y DROP. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Control y Seguridad.pptx]] | Control de acceso y seguridad en bases de datos. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Data Warehouse.pptx]] | Data warehouse: modelo dimensional y ETL. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Desnormalizacion.pdf]] | Desnormalización y sus criterios de aplicación. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Modelo Conceptual.pptx]] | Modelo Entidad-Relacional conceptual. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Modelo Logico.pptx]] | Modelo lógico: tablas, claves y restricciones. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Normalización.pptx]] | Formas normales y normalización de relaciones. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/SQL Avanzado.pptx]] | SQL avanzado: joins, subconsultas y funciones. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/SQL.pptx]] | SQL básico: DDL, DML y consultas. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Supertipo.pptx]] | Supertipos y subtipos en el modelo Entidad-Relacional. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/Transacciones.pptx]] | Transacciones y control de concurrencia. |
> | [[Unidad 0 - Guias y Ejercicios/Diapositivas/unidad1.3-1.5.pdf]] | Unidad 1 · secciones 1.3 a 1.5 (modelo de datos). |

---

## 📝 Exámenes

> [!example] Exámenes parciales y evaluaciones
> Los que dicen *incluye solución* traen la resolución resuelta.
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2017-1T-2P-BD-sol.pdf]] | 2017 · 1.er trimestre · 2.do parcial · incluye solución. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2017-2T-2P-BD-sol.pdf]] | 2017 · 2.do trimestre · 2.do parcial · incluye solución. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2018-1T-2P-BDsol.pdf]] | 2018 · 1.er trimestre · 2.do parcial · incluye solución. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2019-2PAO-2E-SBD.pdf]] | 2019 · 2.do PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2021-1PAO-2E-SBD-1.pdf]] | 2021 · 1.er PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2021-2PAO-2E-SBD-1.pdf]] | 2021 · 2.do PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2022-2PAO-1E-SBD.docx]] | 2022 · 2.do PAO · 1.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-1PAO-1E-SBD.docx]] | 2023 · 1.er PAO · 1.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-1PAO-2E-SBD.pdf]] | 2023 · 1.er PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-1T-1P-BD.docx]] | 2023 · 1.er trimestre · 1.er parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-1T-2P-BD.docx]] | 2023 · 1.er trimestre · 2.do parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-2PAO-1E-SBD.docx]] | 2023 · 2.do PAO · 1.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-2PAO-2E-SBD.pdf]] | 2023 · 2.do PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-2PAO-3E-SBD.docx]] | 2023 · 2.do PAO · 3.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-2T-1P-BD.docx]] | 2023 · 2.do trimestre · 1.er parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2023-2T-2P-BD.docx]] | 2023 · 2.do trimestre · 2.do parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-1PAO-1E-SBD.docx]] | 2024 · 1.er PAO · 1.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-1PAO-2E-SBD.pdf]] | 2024 · 1.er PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-1PAO-3E-SBD.docx]] | 2024 · 1.er PAO · 3.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-1T-1P-BD.docx]] | 2024 · 1.er trimestre · 1.er parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-1T-2P-BD.docx]] | 2024 · 1.er trimestre · 2.do parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-2PAO-1E-SBD.docx]] | 2024 · 2.do PAO · 1.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-2PAO-2E-SBD.pdf]] | 2024 · 2.do PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-2PAO-3E-SBD.docx]] | 2024 · 2.do PAO · 3.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-2T-1P-BD.docx]] | 2024 · 2.do trimestre · 1.er parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2024-2T-2P-BD.docx]] | 2024 · 2.do trimestre · 2.do parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2025-1PAO-1E-SBD.docx]] | 2025 · 1.er PAO · 1.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2025-1PAO-2E-SBD.docx]] | 2025 · 1.er PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2025-1PAO-3E-SBD.docx]] | 2025 · 1.er PAO · 3.er evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/2025-2PAO-2E-SBD.docx]] | 2025 · 2.do PAO · 2.do evaluación. |
> | [[Unidad 0 - Guias y Ejercicios/Exámenes/Examenes BSD.pdf]] | Compilado de exámenes de BSD. |

---

## 📖 Lecciones

> [!tip] Material de lectura y teoría
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Lecciones/2026_1PAO_Lección_2_TICG1018.pdf]] | Lección 2 del curso (PAO 1 · 2026). |
> | [[Unidad 0 - Guias y Ejercicios/Lecciones/LECCION 2 - PAO 1 - 2026.pdf]] | Lección 2 · PAO 1 · 2026. |
> | [[Unidad 0 - Guias y Ejercicios/Lecciones/Leccion 1 - PAO I 2024.pdf]] | Lección 1 · PAO 1 · 2024. |
> | [[Unidad 0 - Guias y Ejercicios/Lecciones/Leccion 2 - PAO I 2024.pdf]] | Lección 2 · PAO 1 · 2024. |
> | [[Unidad 0 - Guias y Ejercicios/Lecciones/Leccion 4 - PAO I 2024.pdf]] | Lección 4 · PAO 1 · 2024. |
> | [[Unidad 0 - Guias y Ejercicios/Lecciones/Lección 1 PAO 1 2025.pdf]] | Lección 1 · PAO 1 · 2025. |
> | [[Unidad 0 - Guias y Ejercicios/Lecciones/Lección 3 PAO 1 2025.png]] | Lección 3 · PAO 1 · 2025 (imagen del material). |

---

## 🛠️ Talleres

> [!example] Talleres prácticos con sus soluciones
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Talleres/2024_1PAO_Taller_1_TICG1018.pdf]] | Taller 1 · PAO 1 · 2024. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/2026_1PAO_Taller_1_TICG1018.pdf]] | Taller 1 · PAO 1 · 2026. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/ENUNCIADO.pdf]] | Enunciado del taller sin identificar. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/SF_1PAO_Taller_1_TICG1018.pdf]] | Taller 1 · PAO 1 · 2024 (versión SF). |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/SF_PAE_Taller_3_TICG1018.pdf]] | Taller 3 · PAE (versión SF). |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 1 2025 PAO 1/Solución G8.pdf]] | Solución del grupo 8 al Taller 1 · PAO 1 · 2025. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 1 2025 PAO 1/Taller 1  2025 PAO 1.pdf]] | Enunciado del Taller 1 · PAO 1 · 2025. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 2 2025 PAO 1/Taller 2  John Carreño.pdf]] | Solución individual al Taller 2 · PAO 1 · 2025. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 2 2025 PAO 1/Taller 2 2025 PAO 1.pdf]] | Enunciado del Taller 2 · PAO 1 · 2025. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 2 PAO-2026-1  SOL.pdf]] | Taller 2 · PAO 1 · 2026, con solución. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 3 2025 PAO 1/Taller 3 2025 PAO 1.pdf]] | Enunciado del Taller 3 · PAO 1 · 2025. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 3 2026 PAO 1.pdf]] | Taller 3 · PAO 1 · 2026. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 4 - PAO I 2024 - Triggers, Vistas e Usuarios.pdf]] | Taller 4 · PAO 1 · 2024 (triggers, vistas y usuarios). |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 4 2025 PAO 1/psicotest.png]] | Captura del enunciado del Taller 4 (modelo psicotest). |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Taller 4_20agorep.pdf]] | Taller 4 · versión del 20 de agosto. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Tarea 1.pdf]] | Tarea 1. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/Tarea 2.pdf]] | Tarea 2. |
> | [[Unidad 0 - Guias y Ejercicios/Talleres/tarea03_algebra y Normalización.pdf]] | Tarea 3 · álgebra relacional y normalización. |

---

## 📎 Material de clase

> [!example] Apuntes y recursos sueltos
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Material de clase/Apuntes DDL y DML.pdf]] | Apuntes de DDL (definición) y DML (manipulación) en SQL. |
> | [[Unidad 0 - Guias y Ejercicios/Material de clase/ans3ed-oddonly.pdf]] | Resolución de los ejercicios impares del libro (capítulo 3). |

---

## 🏗️ Proyecto

> [!example] Entregas del proyecto (Primer y Segundo Parcial)

### Primer Parcial

> [!info] 📊 Primer Parcial
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Primer Parcial/G8 Feedback.pdf]] | Retroalimentación del docente sobre la entrega del Primer Parcial. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Primer Parcial/Modelo Conceptual Proyecto.png]] | Diagrama Entidad-Relacional conceptual del proyecto. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Primer Parcial/Modelo Lógico Proyecto.png]] | Diagrama del modelo lógico (tablas y claves) del proyecto. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Primer Parcial/Propuesta Individual John Carreño.pdf]] | Propuesta individual de John Carreño. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Primer Parcial/Proyecto Grupo 8.docx]] | Entrega del Primer Parcial (editable). |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Primer Parcial/Proyecto Grupo 8.pdf]] | Entrega del Primer Parcial (PDF). |

### Segundo Parcial

> [!info] 📊 Segundo Parcial
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Segundo Parcial/Analisis Sostenibilidad Grupo 8.pdf]] | Análisis de sostenibilidad del proyecto. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Segundo Parcial/BSD_Diapositivas_Narrativa Sistema.pdf]] | Diapositivas de la narrativa del sistema (presentación del proyecto). |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Segundo Parcial/Crud_Grupo8/ImportTrackLogo.png]] | Imagen de la interfaz CRUD con el logo importado. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Segundo Parcial/Crud_Grupo8/Logo.png]] | Logo del proyecto (usado en la interfaz CRUD). |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Segundo Parcial/Informe Análisis Comparativo Grupo 8.pdf]] | Informe comparativo entre los modelos y las bases de datos del proyecto. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Segundo Parcial/Manual de Operaciones CRUD para la Tabla Cliente.pdf]] | Manual de operaciones CRUD sobre la tabla Cliente. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Segundo Parcial/ModeloLogicoFinal.png]] | Modelo lógico final del proyecto (con las correcciones del docente). |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Segundo Parcial/Proyecto Entrega Final.pdf]] | Entrega final del Segundo Parcial. |

> [!note] 🧩 Código Python del CRUD (solo en el vault)
> El código fuente del módulo CRUD (`Crud_Grupo8/Clientes.py`, `Conexion.py`, `PythonMySQL.py`,
> `tempCodeRunnerFile.py`) queda solo en tu vault: no tiene formato web ni entra en el ZIP.

---

## 👥 Participaciones

> [!example] Respuestas y soluciones de las participaciones
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Participaciones/Participación 1 2025 PAO 1/Solución Grupo 8.pdf]] | Solución del grupo 8 a la Participación 1. |
> | [[Unidad 0 - Guias y Ejercicios/Archivos/Participaciones/Participación 2 2025 PAO 1/ML.png]] | Diagrama del modelo lógico de la Participación 2. |

---

## 📊 Diagramas y figuras

> [!info] Diagramas del material
> La carpeta `Diagramas/` tiene los modelos Entidad-Relacional, los ejercicios de diagramado
> resueltos y los diagramas de cada unidad. Abajo están los que se publican desde este índice;
> en Obsidian además tenés los `.drawio` editables (4 de ellos).

### Ejercicios de diagramado resueltos

> [!info] 📊 Ejercicios de diagramado resueltos
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej01-lavanderia.svg]] | Ejercicio 1 resuelto · lavanderia. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej02-taxigo.svg]] | Ejercicio 2 resuelto · taxigo. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej03-azm.svg]] | Ejercicio 3 resuelto · azm. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej04-subsidio.svg]] | Ejercicio 4 resuelto · subsidio. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej05-concursos.svg]] | Ejercicio 5 resuelto · concursos. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej06-naren.svg]] | Ejercicio 6 resuelto · naren. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej07-phograh.svg]] | Ejercicio 7 resuelto · phograh. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej08-expreso.svg]] | Ejercicio 8 resuelto · expreso. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej09-hipotecario.svg]] | Ejercicio 9 resuelto · hipotecario. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej10-ecolife.svg]] | Ejercicio 10 resuelto · ecolife. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej11-dep-flow.svg]] | Ejercicio 11 resuelto · dep flow. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej11-diagrama-dependencias.svg]] | Ejercicio 11 resuelto · diagrama dependencias. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej11-modelo-3fn.svg]] | Ejercicio 11 resuelto · modelo 3fn. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej12-dependencias.svg]] | Ejercicio 12 resuelto · dependencias. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej12-modelo-3fn.svg]] | Ejercicio 12 resuelto · modelo 3fn. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej13-modelo.svg]] | Ejercicio 13 resuelto · modelo. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej14-modelo.svg]] | Ejercicio 14 resuelto · modelo. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej15-dep-flow.svg]] | Ejercicio 15 resuelto · dep flow. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej15-dependencias.svg]] | Ejercicio 15 resuelto · dependencias. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej16-dep-flow.svg]] | Ejercicio 16 resuelto · dep flow. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej16-more-stuff.svg]] | Ejercicio 16 resuelto · more stuff. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/ej16-store-item.svg]] | Ejercicio 16 resuelto · store item. |

### Notación Chen (material de la Unidad 0)

> [!info] 📊 Notación Chen (material de la Unidad 0)
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/drawio-01-entidad-relacion-atributo.drawio.svg]] | Diagrama en notación Chen · Entidad-Relación y atributos. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/drawio-02-claves.drawio.svg]] | Diagrama en notación Chen · Claves primarias y foráneas. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/drawio-03-conectividad.drawio.svg]] | Diagrama en notación Chen · Conectividad (1:1, 1:N, N:M). |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/drawio-04-cardinalidad.drawio.svg]] | Diagrama en notación Chen · Cardinalidad de las relaciones. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/drawio-05-debil-fuerte.drawio.svg]] | Diagrama en notación Chen · Entidades débiles y fuertes. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/drawio-06-leyenda-chen.drawio.svg]] | Diagrama en notación Chen · Leyenda de la notación. |

### Diagramas de trabajo de la Unidad 1 y la Unidad 2

> [!note] 🗂️ 112 SVG de trabajo
> `Diagramas/` tiene además **112 SVG** de trabajo de la U1 y la U2
> (`u1-01-01-graph.svg` … `u2-04-06-er.svg`): grafos de dependencias, diagramas
> Entidad-Relacional y diagramas de flujo de cada tema de esas unidades.
> **100 de ellos ya están embebidos** en las notas de la U1 y la U2, donde corresponde,
> así que no se repiten acá.

> [!warning] 12 diagramas sin nota que los embeba
> Estos 12 SVG de trabajo no los menciona ninguna nota de la materia. Se listan acá
> para que al menos se puedan abrir desde la web:
>
> | Archivo | Qué es |
> |---|---|
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-01-graph.svg]] | U2 · tema 02 · 01 · grafo de dependencias. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-02-flow.svg]] | U2 · tema 02 · 02 · diagrama de flujo. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-03-graph.svg]] | U2 · tema 02 · 03 · grafo de dependencias. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-04-graph.svg]] | U2 · tema 02 · 04 · grafo de dependencias. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-05-er.svg]] | U2 · tema 02 · 05 · diagrama Entidad-Relacional. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-06-er.svg]] | U2 · tema 02 · 06 · diagrama Entidad-Relacional. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-07-er.svg]] | U2 · tema 02 · 07 · diagrama Entidad-Relacional. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-08-er.svg]] | U2 · tema 02 · 08 · diagrama Entidad-Relacional. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-09-er.svg]] | U2 · tema 02 · 09 · diagrama Entidad-Relacional. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-10-er.svg]] | U2 · tema 02 · 10 · diagrama Entidad-Relacional. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-11-er.svg]] | U2 · tema 02 · 11 · diagrama Entidad-Relacional. |
> | [[Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-12-graph.svg]] | U2 · tema 02 · 12 · grafo de dependencias. |

---

## ⚠️ ¿Qué NO se publica en el sitio web?

> [!warning] Archivos que quedan solo en tu vault local
>
> | Archivo | Motivo |
> |---|---|
> | `Unidad 0 - Guias y Ejercicios/Archivos/Proyecto/Primer Parcial/VideoBSDPrimerParcial.mp4` | 13 MB. No se sube por peso (listado en `_no-publicar.txt`). |
> | `Unidad 0 - Guias y Ejercicios/Diapositivas/Database Systems - Design, Implementation, and Management (9th Edition).pdf` | Libro completo con copyright: no se redistribuye. |
> | `Universidad/_no-publicar.txt` | Lista negra de archivos que no se publican. |

> [!note] Scripts SQL sueltos
> Los archivos `.sql`, `.mwb` y `.txt` no tienen formato web, por eso van todos dentro del
> ZIP de la sección *Paquete único de scripts y modelos*.

---

## 💡 ¿Cómo usar este material?

> [!info] 📊 ¿Cómo usar este material?
>
> | Si querés... | Usá... |
> |---|---|
> | Practicar consultas SQL | Los scripts `.sql` del ZIP (abrilos en MySQL Workbench o phpMyAdmin). |
> | Ver un modelo Entidad-Relacional | `supermercado.mwb` (dentro del ZIP) o los diagramas de `Diagramas/`. |
> | Estudiar para un parcial | Los exámenes de la sección *Exámenes* (algunos con solución). |
> | Repasar teoría | Las diapositivas en *Diapositivas* y las lecciones en *Lecciones*. |
> | Hacer un taller | Los enunciados y soluciones en *Talleres*. |
> | Ver cómo se estructuró un proyecto real | Los archivos de *Proyecto* (documentación, SQL y código). |
> | Usar datos de ejemplo ya listos | `sakila-db.zip` y `world-db.zip` (sección *Bases de datos de ejemplo*). |

---

> [!success] Todo este material está en tu vault de Obsidian bajo
> `3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/`.
> Los archivos con enlace se descargan o abren desde la web; el resto queda en el vault local.
