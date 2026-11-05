---
dg-publish: true
tags: [indice, base-de-datos, 3er-semestre]
---

# 🗄️ Sistema de Bases de Datos — Unidad 0

> [!info] 📚 ¿Qué es este índice?
> Esta es la **guía de contenido** de la Unidad 0 de **Sistema de Bases de Datos** (3er Semestre · PAO 2-2026).
> Acá figura todo el material de apoyo que se integró al vault: diapositivas, exámenes, talleres,
> lecciones, scripts SQL, modelos de base de datos, material del proyecto y participaciones.
>
> Los archivos que no se publican en el sitio web quedan solo en tu vault local (ver nota de copyright abajo).

---

## 🗃️ Archivos descargables

> [!note] 📦 ZIP: Scripts SQL, Modelos y Textos de Apoyo
>
> **Archivo:** `Archivos/Bases de Datos/BD - Scripts SQL Modelos y Textos de Apoyo.zip`
>
> Un solo archivo comprimido con todo el material suelto que no tiene una nota propia en el vault.
> Úsalo si querés descargar de una vez todos los scripts, modelos y textos de referencia.
>
> **¿Qué hay adentro?**
> - **`.sql`** → scripts de base de datos (tablas, datos de ejemplo, consultas). Ábrelos en MySQL Workbench, phpMyAdmin o cualquier cliente SQL.
> - **`.mwb`** → modelo de base de datos hecho en MySQL Workbench. Ábrelo con MySQL Workbench para ver el diagrama Entidad-Relación.
> - **`.txt`** → textos de consulta, respuestas de participaciones y notas sueltas.
>
> **¿Qué NO hay adentro?**
> - El video del proyecto (`VideoBSDPrimerParcial.mp4`) quedó fuera por peso y está en `_no-publicar.txt`.
> - Los archivos de diagrama (`.drawio`, `.svg`) no entran acá: están en la carpeta `Diagramas/`.

> [!note] 🗃️ Bases de datos de ejemplo (dentro del ZIP)

| Archivo | Qué es | Para qué sirve |
|---|---|---|
| `sakila-db.zip` | Base de datos Sakila (MySQL) | Ejemplo clásico de alquiler de películas. Úsala para practicar consultas, joins y normalización. |
| `world-db.zip` | Base de datos World (MySQL) | Datos de países, ciudades e idiomas. Ideal para practicar consultas geográficas y agregaciones. |
| `crm_completo_20.sql` | Script CRM completo | Crear y poblar una base de datos de gestión de clientes. |
| `iswc.sql` | Script ISWC | Base de datos de ejemplo para práctica. |
| `mercado.sql` | Script mercado | Modelo de ventas de un mercado/supermercado. |
| `proyectos.sql` | Script proyectos | Gestión de proyectos y tareas. |
| `psicotest.sql` | Script psicotest | Base de datos de pruebas psicológicas. |
| `Northwind/northwind.sql` | Esquema Northwind | Base de datos clásica de Microsoft (clientes, órdenes, productos). |
| `Northwind/northwind-data.sql` | Datos de Northwind | Datos de ejemplo para poblar Northwind. |
| `supermercado.mwb` | Modelo MySQL Workbench | Diagrama Entidad-Relación de un supermercado. Ábrelo en MySQL Workbench. |

> [!note] 📜 Scripts SQL sueltos (dentro del ZIP)

| Archivo | Qué es |
|---|---|
| `SQL/ddl joins.sql` | Sentencias DDL y ejemplos de JOINs. |
| `SQL/sp_triggers_fun 2025.sql` | Procedimientos almacenados, triggers y funciones. |
| `SQL/subscription_queries.sql` | Consultas de suscripción/registro. |

> [!note] 👥 Participaciones (dentro del ZIP)

| Archivo | Qué es |
|---|---|
| `Participaciones/Participación 1 2025 PAO 1/Participación 1 2025 PAO 1.txt` | Respuesta escrita a la Participación 1. |
| `Participaciones/Participación 1 2025 PAO 1/Solución Grupo 8.pdf` | Solución del grupo 8 a la Participación 1. |
| `Participaciones/Participación 2 2025 PAO 1/Participación 2 2025 PAO 1.txt` | Respuesta escrita a la Participación 2. |
| `Participaciones/Participación 2 2025 PAO 1/ML.png` | Diagrama Modelo Lógico de la Participación 2. |
| `Participaciones/Participación 4 2025 PAO 1/Participación 4 2025 PAO 1.txt` | Respuesta escrita a la Participación 4. |
| `Participaciones/Participación 4 2025 PAO 1/Participacion 4 Grupo 8.sql` | Script SQL del grupo 8 para la Participación 4. |
| `Participaciones/Participación 4 2025 PAO 1/iswc.sql` | Script ISWC usado en la Participación 4. |
| `Participaciones/Participación 5 2025 PAO 1/Participación 5 2025 PAO 1.txt` | Respuesta escrita a la Participación 5. |
| `Participaciones/Participación 5 2025 PAO 1/Solución John Carreño.txt` | Solución individual a la Participación 5. |

> [!note] 🏗️ Proyecto (dentro del ZIP)

| Archivo | Qué es |
|---|---|
| `Proyecto/Segundo Parcial/ProyectoGrupo8.sql` | Script SQL final del proyecto del grupo 8. |

---

## 🎞️ Diapositivas

> [!example] Presentaciones del curso
>
> Estos archivos se encuentran en `Diapositivas/`. Se suben al sitio web como descarga.

| Archivo | Tema | Tamaño |
|---|---|---|
| `Diapositivas/Modelo Conceptual.pptx` | Modelo Entidad-Relación conceptual | 504 KB |
| `Diapositivas/Modelo Lógico.pptx` | Modelo lógico de bases de datos | 2.9 MB |
| `Diapositivas/Normalización.pptx` | Formas normales y normalización | 2.9 MB |
| `Diapositivas/Transacciones.pptx` | Transacciones y control de concurrencia | 699 KB |
| `Diapositivas/Algebra Relacional.pptx` | Álgebra relacional | 844 KB |
| `Diapositivas/Control y Seguridad.pptx` | Control de acceso y seguridad | 170 KB |
| `Diapositivas/Data Warehouse.pptx` | Almacenes de datos | 1.9 MB |
| `Diapositivas/Desnormalizacion.pdf` | Desnormalización | 404 KB |
| `Diapositivas/SQL.pptx` | SQL básico | 1 MB |
| `Diapositivas/SQL Avanzado.pptx` | SQL avanzado | 504 KB |
| `Diapositivas/Supertipo.pptx` | Supertipos y subtipos en ER | 1.2 MB |

---

## 📝 Exámenes

> [!example] Exámenes parciales (con soluciones cuando corresponde)
>
> Estos archivos se encuentran en `Exámenes/`. Se suben al sitio web como descarga.

| Archivo | Año/Periodo | Tamaño |
|---|---|---|
| `Exámenes/2017-1T-2P-BD-sol.pdf` | 2017, 1er trimestre, 2do parcial (con solución) | 196 KB |
| `Exámenes/2017-2T-2P-BD-sol.pdf` | 2017, 2do trimestre, 2do parcial (con solución) | 444 KB |
| `Exámenes/2018-1T-2P-BDsol.pdf` | 2018, 1er trimestre, 2do parcial (con solución) | 426 KB |
| `Exámenes/2023-1T-1P-BD.docx` | 2023, 1er trimestre, 1er parcial | 242 KB |
| `Exámenes/2023-1T-2P-BD.docx` | 2023, 1er trimestre, 2do parcial | 295 KB |
| `Exámenes/2023-2T-1P-BD.docx` | 2023, 2do trimestre, 1er parcial | 575 KB |
| `Exámenes/2023-2T-2P-BD.docx` | 2023, 2do trimestre, 2do parcial | 686 KB |
| `Exámenes/2024-1T-1P-BD.docx` | 2024, 1er trimestre, 1er parcial | 539 KB |
| `Exámenes/2024-1T-2P-BD.docx` | 2024, 1er trimestre, 2do parcial | 260 KB |
| `Exámenes/2024-2T-1P-BD.docx` | 2024, 2do trimestre, 1er parcial | 920 KB |
| `Exámenes/2024-2T-2P-BD.docx` | 2024, 2do trimestre, 2do parcial | 923 KB |
| `Exámenes/Examenes BSD.pdf` | Compilado de exámenes BSD | 3.5 MB |

---

## 📖 Lecciones

> [!tip] Material de lectura y teoría
>
> Estos archivos se encuentran en `Lecciones/`. Se suben al sitio web como descarga.

| Archivo | Contenido | Tamaño |
|---|---|---|
| `Lecciones/Lección 1 PAO 1 2025.pdf` | Lección 1 del curso | 309 KB |
| `Lecciones/Lección 3 PAO 1 2025.png` | Lección 3 (imagen) | 314 KB |

---

## 🛠️ Talleres

> [!example] Talleres prácticos y soluciones
>
> Estos archivos se encuentran en `Talleres/`. Se suben al sitio web como descarga.

| Archivo | Qué es | Tamaño |
|---|---|---|
| `Talleres/Taller 1 2025 PAO 1/Taller 1 2025 PAO 1.pdf` | Enunciado del Taller 1 | 182 KB |
| `Talleres/Taller 1 2025 PAO 1/Solución G8.pdf` | Solución del grupo 8 al Taller 1 | 66 KB |
| `Talleres/Taller 2 2025 PAO 1/Taller 2 2025 PAO 1.pdf` | Enunciado del Taller 2 | 456 KB |
| `Talleres/Taller 2 2025 PAO 1/Taller 2 John Carreño.pdf` | Solución individual al Taller 2 | 411 KB |
| `Talleres/Taller 2 2025 PAO 1/EntradasDB_con_datos.sql` | Script con datos de entrada para el Taller 2 | 7 KB |
| `Talleres/Taller 3 2025 PAO 1/Taller 3 2025 PAO 1.pdf` | Enunciado del Taller 3 | 184 KB |
| `Talleres/Taller 3 2025 PAO 1/Taller3 Grupo8.sql` | Script SQL del grupo 8 para el Taller 3 | 3 KB |
| `Talleres/Taller 4 2025 PAO 1/Taller 4 2025 PAO 1.txt` | Enunciado/respuesta del Taller 4 | 239 bytes |
| `Talleres/Taller 4 2025 PAO 1/Taller 4 JohnCarreño.txt` | Solución individual al Taller 4 | 4 KB |
| `Talleres/Taller 4 2025 PAO 1/psicotest.png` | Imagen relacionada al Taller 4 | 77 KB |
| `Talleres/Taller 4 2025 PAO 1/psicotest.sql` | Script psicotest para el Taller 4 | 5 KB |

---

## 📎 Material de clase

> [!example] Apuntes y recursos sueltos
>
> Estos archivos se encuentran en `Material de clase/`. Se suben al sitio web como descarga.

| Archivo | Qué es | Tamaño |
|---|---|---|
| `Material de clase/ans3ed-oddonly.pdf` | Resolución de ejercicios impares (ans3ed) | 1 MB |
| `Material de clase/Apuntes DDL y DML.pdf` | Apuntes de DDL y DML | 163 KB |
| `Material de clase/MongoDB.txt` | Notas sueltas sobre MongoDB | 2 KB |

---

## 📊 Diagramas y figuras (solo en vault local)

> [!info] Estos archivos están en tu vault pero no se listan aquí por cantidad (más de 150 SVG y drawio).
>
> Estos se pueden abrir directamente desde Obsidian. No se publican individualmente en el sitio web.

| Carpeta | Contenido | Tamaño total aprox. |
|---|---|---|
| `Diagramas/` | Diagramas Entidad-Relación (`.drawio`, `.svg`) y ejercicios resueltos | 159 archivos |
| `Diagramas/ej01-*.svg` hasta `ej16-*.svg` | 16 ejercicios de diagramado resueltos | varía |
| `Diagramas/u1-01-0*.svg` | Diagramas de la Unidad 1 | varios archivos |

---

## ⚠️ ¿Qué NO se publica en el sitio web?

> [!warning] Algunos archivos quedaron fuera del sitio por decisión de copyright o peso. Quedan solo en tu vault local:

| Archivo | Motivo |
|---|---|
| `Archivos/Proyecto/Primer Parcial/VideoBSDPrimerParcial.mp4` | 13 MB. No se sube a Vercel por peso (listado en `_no-publicar.txt`). |
| `Universidad/_no-publicar.txt` | Lista negra de archivos que no se publican. |

---

## 💡 ¿Cómo usar este material?

| Si querés... | Usá... |
|---|---|
| Practicar consultas SQL | Los scripts `.sql` del ZIP (abrí en MySQL Workbench o phpMyAdmin). |
| Ver un modelo Entidad-Relación | `supermercado.mwb` (MySQL Workbench) o los diagramas en `Diagramas/`. |
| Estudiar para un parcial | Los exámenes en `Exámenes/` (algunos tienen solución). |
| Repasar teoría | Las diapositivas en `Diapositivas/` y las lecciones en `Lecciones/`. |
| Hacer un taller | Los enunciados y soluciones en `Talleres/`. |
| Ver cómo se estructuró un proyecto real | Los archivos de `Proyecto/` (documentación, SQL, código Python). |

---

> [!success] Todo este material está disponible en tu vault de Obsidian bajo `3er Semestre/Sistema de Bases de Datos/Unidad 0 - Guias y Ejercicios/`. Los archivos marcados como "descarga" también están disponibles en el sitio web publicado.
