?---
dg-publish: true
tags: [TICG1018, unidad2, primera-forma-normal, diccionario, ml]
---

# 📏 Primera Forma Normal y Diccionario de Datos

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Normalizar Después de Convertir?
>
> La conversión produce tablas; la **normalización** verifica que esas tablas no escondan inconsistencias. Las formas normales miden la **vulnerabilidad a anomalías lógicas**: mientras más alta la FN, menos formas de que los datos se contradigan.
>
> **Analogía del mundo real:** la conversión es armar el mueble; la 1FN es verificar que no sobren tornillos ni falten patas.
>
> | Forma | Idea en 1 línea | La verás en... |
> |---|---|---|
> | **1FN** | Sin grupos repetitivos: un valor por celda | Esta nota (Lección 1) |
> | **2FN** | Sin dependencias parciales (vista previa) | Próximas clases |
> | **3FN** | Sin dependencias transitivas (vista previa) | Próximas clases |

---

## 📋 Definiciones Formales

> [!info] ℹ️ Cómo leer esta sección
> Una definición por bloque. Las 5 condiciones de 1FN tienen número propio: si una tabla falla, citas cuál.

### 1️⃣ Objetivo 1FN — tablas que son relaciones de verdad

> [!note] 📋 Definición — Objetivo
>
> Convertir las entidades en tablas que sean representación fiel de una relación, libres de grupos repetitivos.
>
> **Ejemplo:** CLIENTE con una fila por cliente y un teléfono por celda es fiel; con `telefono1, telefono2` es un formulario disfrazado, no una relación.
>
> ```mermaid
> graph LR
>     E["Entidad"] --> T["Tabla"]
>     T --> V{"¿Fiel?<br/>sin repetidos"}
>     V -->|"Si"| O["✅ 1FN"]
>     V -->|"No"| R["❌ Formulario<br/>disfrazado"]
>     style O fill:#e1ffe1
>     style R fill:#ffe1e1
> ```

### 2️⃣ Las 5 condiciones — el checklist

> [!note] 📋 Definición — Tabla en 1FN
>
> 1. Sin orden arriba-abajo en las filas.
> 2. Sin orden izquierda-derecha en las columnas.
> 3. Sin filas duplicadas.
> 4. Cada celda, exactamente un valor del dominio.
> 5. Columnas regulares (sin IDs de fila, IDs de objeto ni timestamps ocultos).
>
>
> ```mermaid
> flowchart TD
>     A["¿Tabla en 1FN?"] --> C1{"¿Filas con orden<br/>o duplicadas?"}
>     C1 -->|"Si"| R["❌ Falla 1, 2 o 3"]
>     C1 -->|"No"| C2{"¿Celda con<br/>varios valores?"}
>     C2 -->|"Si"| R2["❌ Falla 4"]
>     C2 -->|"No"| C3{"¿Columnas<br/>raras?"}
>     C3 -->|"Si"| R3["❌ Falla 5"]
>     C3 -->|"No"| O["✅ 1FN"]
>     style O fill:#e1ffe1
> ```
>
>
> **Cómo usarlo:** ante cualquier tabla sospechosa, recorre las 5 en orden y cita el número que falla.

### 3️⃣ Violación — qué significa reprobar

> [!note] 📋 Definición — Violación de 1FN
>
> Incumplir cualquiera de las 5 = tabla no estrictamente relacional = no está en 1FN.
>
> **Ejemplo:** `productos = "arroz, leche, pan"` viola la 4; `materia1, materia2` viola la 4 disfrazada de columnas; dos filas idénticas violan la 3.
>
> ```mermaid
> graph TB
>     V["Viola 1 condición"] --> N["No es estrictamente<br/>relacional"]
>     N --> F["No está en 1FN<br/>aunque tenga PK"]
>     style F fill:#ffe1e1
> ```
>
> **Se lee así:** basta 1 falla de 5 para reprobar; la PK no salva una tabla con grupos repetitivos.

### 4️⃣ Formas normales — el termómetro

> [!note] 📋 Definición — FN
>
> Criterios del grado de vulnerabilidad a inconsistencias y anomalías lógicas: 1FN (grupos repetitivos) → 2FN (dependencias parciales) → 3FN (transitivas).
>
> **Ejemplo:** una tabla en 1FN puede seguir mintiendo si un dato depende solo de parte de la PK — eso lo mide 2FN (próximas clases).
>
> ```mermaid
> graph LR
>     A["1FN<br/>repetidos"] --> B["2FN<br/>parciales"]
>     B --> C["3FN<br/>transitivas"]
>     style A fill:#e1ffe1
> ```
>
> **Se lee así:** termómetro de 3 niveles; cada FN mide una vulnerabilidad distinta y se lee en orden.

### 5️⃣ Diccionario de datos — el manual de cada tabla

> [!note] 📋 Definición — Diccionario
>
> Documento que describe cada tabla: por atributo, tipo de dato, dominio y descripción.
>
> | Atributo | Tipo | Dominio | Descripción |
> |---|---|---|---|
> | cedula | int | > 0, único | PK del cliente |
>
> **Ejemplo:** sin esta fila, nadie sabe si `teléfono` admite 7 u 10 dígitos. Ver Método para la plantilla completa.

### 6️⃣ Atributo multivaluado — el que pide tabla propia

> [!note] 📋 Definición — Multivaluado
>
> El que guarda varios valores (ej. teléfonos) — viola 1FN hasta separarse en su propia tabla o filas.
>
> **Ejemplo:** `TELEFONO(cedula PK,FK, numero PK)`: el teléfono deja de ser columna repetida y pasa a ser filas identificadas.
>
> ```mermaid
> erDiagram
>     CLIENTE ||--o{ TELEFONO : tiene
>     TELEFONO {
>         int cedula PK, FK
>         int numero PK
>     }
> ```
>
> **Se lee así:** el multivaluado se vuelve entidad débil con PK compuesta; un cliente, N filas.

---
## 🎨 Ejemplo Trabajado: CLIENTE

> [!example] 💡 Verificando 1FN con datos reales
>
> | Cédula | Nombre | Dirección | Teléfono |
> |---|---|---|---|
> | 0876456324 | Jorge Santos | 1234 Av. 10 | 2345678 |
> | 0964532748 | Luis Tinoco | 6543 Av. 4 | 2654345 |
> | 1345234567 | Ana Ramírez | 34 Av. 6 | 2654567 |
>
> **Chequeo 1FN:** ¿orden de filas significativo? No. ¿Columnas ordenadas? No. ¿Duplicadas? No. ¿Una celda, un valor? Sí. ¿Columnas regulares? Sí → **está en 1FN**.
>
> **Contraejemplo (grupos repetitivos):** `CLIENTE(cédula, nombre, telefono1, telefono2, telefono3)` — viola (d): los teléfonos son un grupo repetitivo. Remedio: tabla `TELEFONO(cédula FK, numero)` o filas separadas.
>
>
> ```mermaid
> erDiagram
>     CLIENTE_MAL {
>         int cedula PK
>         int telefono1
>         int telefono2
>         int telefono3
>     }
> ```
>
>
> **❌ Así NO:** columnas numeradas = grupo repetitivo disfrazado.
>
>
> ```mermaid
> erDiagram
>     CLIENTE ||--o{ TELEFONO : tiene
>     CLIENTE {
>         int cedula PK
>         string nombre
>     }
>     TELEFONO {
>         int cedula PK, FK
>         int numero PK
>     }
> ```
>
>
> **✅ Así SÍ:** un teléfono por fila; la PK compuesta impide duplicados.

---

## 🛠️ Método: Documentar con Diccionario

> [!success] 🏆 Plantilla por tabla (Úsala en tu proyecto)
>
> | Atributo | Tipo de Dato | Dominio | Descripción |
> |---|---|---|---|
> | idCliente | int | > 0, único | PK: identifica al cliente |
> | nombre | char(30) | texto no vacío | Nombre completo |
> | dirección | char(50) | texto | Dirección de facturación |
> | teléfono | int | 7–10 dígitos | Contacto principal |
>
> **Regla:** cada tabla del ML termina con su fila en el diccionario. Sin diccionario, el ML está incompleto (la docente lo pide explícito).

---

## ⚠️ Errores Comunes y Principios Lógicos

> [!warning] ⚠️ Cómo leer esta sección
> Cada error trae su dibujo: lo ❌ que delata el problema y lo ✅ que lo evita.

### ❌ Error 1: Varios valores por celda

> [!danger] ❌ Viola: 1FN condición (d) — un valor por celda
>
>
> ```mermaid
> erDiagram
>     REPORTE {
>         int id PK
>         string productos
>     }
> ```
>
>
> ❌ **EL ERROR ESTÁ AQUÍ:** `productos = "arroz, leche, pan"` en una sola celda: imposible filtrar, contar o unir por producto.
>
>
> ```mermaid
> erDiagram
>     REPORTE ||--o{ DETALLE_REPORTE : contiene
>     DETALLE_REPORTE {
>         int idReporte PK, FK
>         string producto PK
>     }
> ```
>
>
> ✅ **Así SÍ:** una fila por producto; cada celda, un valor.

### ❌ Error 2: Columnas numeradas

> [!danger] ❌ Viola: grupos repetitivos
>
>
> ```mermaid
> erDiagram
>     ESTUDIANTE {
>         int matricula PK
>         string materia1
>         string materia2
>         string materia3
>     }
> ```
>
>
> ❌ **EL ERROR ESTÁ AQUÍ:** `materia1, materia2, materia3` — ¿y la cuarta materia? Columnas finitas para relaciones infinitas.
>
> ✅ **Así SÍ:** tabla intermedia de matrícula (una fila por par estudiante–materia).

### ❌ Error 3: ML sin diccionario

> [!danger] ❌ Viola: entregable completo
>
> ❌ **EL ERROR ESTÁ AQUÍ:** entregar el diagrama lógico sin describir tipos ni dominios — nadie sabe si `teléfono` es int o texto, ni qué valores acepta.
>
> ✅ **Así SÍ:** diccionario con las 4 columnas (atributo, tipo, dominio, descripción) por cada atributo. La docente lo pide explícito.

---
## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist 1FN
>
> **1. Cuenta valores por celda** — más de uno = no es 1FN.
>
> **2. Busca columnas `cosa1, cosa2`** — es un grupo repetitivo disfrazado.
>
> **3. Diccionario al mismo tiempo** — documenta cada tabla apenas la creas, no al final.
>
> **4. Piensa en 2FN/3FN desde ya** — si un atributo depende de parte de la PK o de otro no-clave, anótalo para la próxima normalización.

---

## 📝 Ejercicios Propuestos

> [!info] ℹ️ Cómo trabajarlos
> Cada ejercicio trae su planteamiento visual. Tapa la solución, resuelve, compara.

### ✏️ Ejercicio 1 — Detectar la violación

> [!example] 📋 Planteamiento
>
> ¿Esta tabla está en 1FN? `REPORTE(id, cliente, productos)` con `productos = "arroz, leche, pan"` en una celda. Justifica y corrige.
>
>
> ```mermaid
> erDiagram
>     REPORTE {
>         int id PK
>         string cliente
>         string productos
>     }
> ```
>
>
> > [!success]- ✅ Solución
> >
> > No: viola la condición (d), un valor por celda. Corrección: tabla `DETALLE_REPORTE(idReporte FK, producto)` con una fila por producto.

### ✏️ Ejercicio 2 — Escribir un diccionario

> [!example] 📋 Planteamiento
>
> Escribe el diccionario de `DEPARTAMENTO(idDepartamento int PK, nombre char(30))`.
>
> > [!success]- ✅ Solución
> >
> > | Atributo | Tipo | Dominio | Descripción |
> > |---|---|---|---|
> > | idDepartamento | int | > 0, único | PK del departamento |
> > | nombre | char(30) | texto no vacío | Nombre oficial |

### ✏️ Ejercicio 3 — Las 3 FN en una frase

> [!example] 📋 Planteamiento
>
> Nombra las 3 FN y qué vulnerabilidad mide cada nivel en una frase.
>
>
> ```mermaid
> graph LR
>     A["1FN"] --> B["2FN"]
>     B --> C["3FN"]
>     A -->|"mide"| V1["grupos<br/>repetitivos"]
>     B -->|"mide"| V2["dependencias<br/>parciales"]
>     C -->|"mide"| V3["dependencias<br/>transitivas"]
>     style A fill:#e1ffe1
> ```
>
>
> > [!success]- ✅ Solución
> >
> > 1FN (grupos repetitivos), 2FN (dependencias parciales de la PK), 3FN (dependencias transitivas entre no-claves). Todas miden vulnerabilidad a inconsistencias y anomalías.

---
## 🔁 Repaso SR (flashcards)

#flashcards/bd-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition (Lección 1: 13-oct)
>
> - ¿Objetivo de la 1FN?::Tablas fieles a una relación, sin grupos repetitivos.
> - ¿5 condiciones 1FN?::Filas sin orden, columnas sin orden, sin duplicadas, un valor por celda, columnas regulares.
> - ¿Qué mide cada FN?::Vulnerabilidad a inconsistencias: 1FN grupos repetitivos, 2FN dependencias parciales, 3FN transitivas.
> - ¿Diccionario de datos y sus 4 columnas?::Describe cada tabla: atributo, tipo de dato, dominio, descripción.

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ 5 condiciones 1FN con ejemplo CLIENTE
> ✅ Diccionario de datos por tabla
> ✅ Vista previa 2FN/3FN
>
> **Próxima clase:** taller de conversión (practica el protocolo de la nota 01 con el diagrama pata de gallo).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Anterior: [[01 - Conversión MC a ML por cardinalidad]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Diapositivas BD 02 MC_a_ML (Irene Cheung): 1FN (objetivo + 5 condiciones + ejemplo CLIENTE), formas normales, diccionario de datos.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (normalización).

---

**Tags:** #TICG1018 #unidad2 #1fn #diccionario #bd
