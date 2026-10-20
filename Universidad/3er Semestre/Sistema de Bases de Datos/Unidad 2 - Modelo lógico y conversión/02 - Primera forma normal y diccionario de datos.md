---
dg-publish: true
tags: [TICG1018, unidad2, primera-forma-normal, diccionario, ml]
---

# 📏 Primera Forma Normal y Diccionario de Datos

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Normalizar Después de Convertir?
>
> La conversión (MC → ML) te da tablas. La **normalización** verifica que esas tablas no escondan inconsistencias. Las formas normales miden qué tan vulnerable es una tabla a que los datos se contradigan.
>
> **Analogía:** la conversión es armar el mueble; la 1FN es verificar que no sobren tornillos ni falten patas.
>
> | Forma | Idea en 1 línea | Qué corrige |
> |---|---|---|
> | **1FN** | Un valor por celda, sin grupos repetitivos | Columnas como `teléfono1, teléfono2` |
> | **2FN** | Sin dependencias parciales | Datos que dependen de solo parte de la PK |
> | **3FN** | Sin dependencias transitivas | Datos que dependen de otro dato no-clave |

---

## 📋 Definiciones Formales

### 1️⃣ Objetivo de la 1FN

> [!note] 📋 Definición — Objetivo
>
> Una tabla está en **1FN** cuando cada celda contiene **exactamente un valor** y no hay grupos repetitivos.
>
> **Ejemplo real:**
>
> ❌ **No es 1FN:** `CLIENTE(cédula, nombre, teléfono1, teléfono2, teléfono3)`  
> Los teléfonos están repetidos en columnas diferentes. Si un cliente tiene 4 teléfonos, no caben.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-02-18-er.svg]]
>
> ✅ **Es 1FN:** `CLIENTE(cédula, nombre)` y `TELEFONO(cédula, número)`  
> Cada fila tiene un solo teléfono. Un cliente puede tener N filas en TELEFONO.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-02-19-er.svg]]

### 2️⃣ Las 5 condiciones de la 1FN

> [!note] 📋 Definición — Checklist de la 1FN
>
> Para que una tabla esté en **1FN**, debe cumplir las 5 condiciones. Si falla cualquiera, no está en 1FN:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-02-14-flow.svg]]
>
> | # | Condición | ¿Qué significa en lenguaje sencillo? |
> |---|---|---|
> | 1 | Sin orden en las filas | No importa si la fila 1 está arriba o abajo de la fila 2 |
> | 2 | Sin orden en las columnas | No importa si `nombre` está a la izquierda o derecha de `cédula` |
> | 3 | Sin filas duplicadas | No puede haber dos filas idénticas |
> | 4 | Un valor por celda | Cada celda guarda exactamente un dato, no una lista |
> | 5 | Columnas regulares | No hay columnas ocultas como `id_fila`, `timestamp`, ni IDs de objeto sueltos |

### 3️⃣ Violación de la 1FN

> [!note] 📋 Definición — Violación
>
> Una tabla **no está en 1FN** si incumple cualquiera de las 5 condiciones. La PK (clave primaria) no salva a una tabla que tiene grupos repetitivos.
>
> **Ejemplo:** `productos = "arroz, leche, pan"` en una sola celda viola la condición 4. No puedes filtrar por "arroz" sin leer toda la celda.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-02-16-graph.svg]]

### 4️⃣ Diccionario de datos

> [!note] 📋 Definición — Diccionario de datos
>
> Es un documento que describe cada tabla: por cada atributo, indica su tipo de dato, dominio (qué valores acepta) y descripción. Es el "manual de usuario" de tu base de datos.
>
> | Atributo | Tipo | Dominio | Descripción |
> |---|---|---|---|
> | `cedula` | `int` | > 0, único | PK del cliente |
> | `nombre` | `varchar(50)` | texto no vacío | Nombre completo |
> | `direccion` | `varchar(100)` | texto | Dirección de facturación |
> | `telefono` | `varchar(15)` | 7–15 dígitos | Contacto principal |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-02-15-graph.svg]]

### 5️⃣ Atributo multivaluado

> [!note] 📋 Definición — Atributo multivaluado
>
> Es un atributo que guarda varios valores para una misma entidad (ej. varios teléfonos de un cliente). Viola la 1FN hasta que se separa en su propia tabla.
>
> **Ejemplo:**
>
> ❌ `CLIENTE(cédula, nombre, teléfonos)` → `teléfonos = "2345, 2654"` (grupo repetitivo)
> ✅ `TELEFONO(cédula FK, número)` → una fila por teléfono
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-02-17-graph.svg]]

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
> **Chequeo 1FN:**
> - ¿Filas sin orden? Sí.
> - ¿Columnas sin orden? Sí.
> - ¿Sin filas duplicadas? Sí.
> - ¿Una celda, un valor? Sí.
> - ¿Columnas regulares? Sí.
> → **Está en 1FN.**
>
> **Contraejemplo:** `CLIENTE(cédula, nombre, telefono1, telefono2, telefono3)` → viola la condición 4 (grupos repetitivos). Remedio: tabla `TELEFONO(cédula FK, numero)`.

---

## 🛠️ Método: Documentar con Diccionario

> [!success] 🏆 Plantilla por tabla (Úsala en tu proyecto)
>
> | Atributo | Tipo de Dato | Dominio | Descripción |
> |---|---|---|---|
> | `idCliente` | `int` | > 0, único | PK: identifica al cliente |
> | `nombre` | `varchar(30)` | texto no vacío | Nombre completo |
> | `direccion` | `varchar(50)` | texto | Dirección de facturación |
> | `telefono` | `varchar(15)` | 7–15 dígitos | Contacto principal |
>
> **Regla:** cada tabla del ML termina con su fila en el diccionario. Sin diccionario, el ML está incompleto (la docente lo pide explícito).

---

## ⚠️ Errores Comunes

### ❌ Error 1: Varios valores por celda

> [!danger] ❌ Viola: 1FN condición 4
>
> `productos = "arroz, leche, pan"` en una sola celda. No puedes filtrar por "arroz" fácilmente.
>
> ✅ **Solución:** una fila por producto en una tabla `DETALLE(idReporte FK, producto)`.

### ❌ Error 2: Columnas numeradas

> [!danger] ❌ Viola: grupos repetitivos
>
> `materia1, materia2, materia3`. ¿Y la cuarta materia? Columnas finitas para relaciones infinitas.
>
> ✅ **Solución:** tabla intermedia de matrícula (una fila por par estudiante–materia).

### ❌ Error 3: ML sin diccionario

> [!danger] ❌ Viola: entregable completo
>
> Entregar el diagrama lógico sin describir tipos ni dominios. Nadie sabe si `teléfono` es `int` o texto, ni qué valores acepta.
>
> ✅ **Solución:** diccionario con las 4 columnas por cada atributo.

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist 1FN
>
> 1. **Cuenta valores por celda** — más de uno = no es 1FN.
> 2. **Busca columnas `cosa1, cosa2`** — es un grupo repetitivo disfrazado.
> 3. **Diccionario al mismo tiempo** — documenta cada tabla apenas la creas.
> 4. **Piensa en 2FN/3FN desde ya** — si un atributo depende de parte de la PK o de otro no-clave, anótalo.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Detectar la violación

> [!example] 📋 Planteamiento
>
> ¿Está en 1FN? `REPORTE(id, cliente, productos)` con `productos = "arroz, leche, pan"` en una celda.
>
> > [!success]- ✅ Solución
> >
> > No: viola la condición 4 (un valor por celda). Corrección: tabla `DETALLE_REPORTE(idReporte FK, producto)`.

### ✏️ Ejercicio 2 — Escribir un diccionario

> [!example] 📋 Planteamiento
>
> Escribe el diccionario de `DEPARTAMENTO(idDepartamento int PK, nombre varchar(30))`.
>
> > [!success]- ✅ Solución
> >
> > | Atributo | Tipo | Dominio | Descripción |
> > |---|---|---|---|
> > | idDepartamento | int | > 0, único | PK del departamento |
> > | nombre | varchar(30) | texto no vacío | Nombre oficial |

### ✏️ Ejercicio 3 — Las 3 FN en una frase

> [!example] 📋 Planteamiento
>
> Nombra las 3 FN y qué vulnerabilidad mide cada una.
>
> > [!success]- ✅ Solución
> >
> > 1FN (grupos repetitivos), 2FN (dependencias parciales de la PK), 3FN (dependencias transitivas entre no-claves).

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition

- ¿Objetivo de la 1FN?::Tablas fieles a una relación, sin grupos repetitivos.
- ¿5 condiciones 1FN?::Filas sin orden, columnas sin orden, sin duplicadas, un valor por celda, columnas regulares.
- ¿Qué mide cada FN?::Vulnerabilidad a inconsistencias: 1FN grupos repetitivos, 2FN dependencias parciales, 3FN transitivas.
- ¿Diccionario de datos y sus 4 columnas?::Describe cada tabla: atributo, tipo de dato, dominio, descripción.

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
> - ✅ 5 condiciones 1FN con ejemplo CLIENTE
> - ✅ Diccionario de datos por tabla
> - ✅ Vista previa 2FN/3FN
>
> **Próxima clase:** taller de conversión y normalización.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Anterior: [[01 - Conversión MC a ML por cardinalidad]]
> - Siguiente: [[03 - Segunda y tercera forma normal]]

---

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - Diapositivas BD 02 MC_a_ML: 1FN (objetivo + 5 condiciones + ejemplo CLIENTE), formas normales, diccionario de datos.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (normalización).

---

**Tags:** #TICG1018 #unidad2 #1fn #diccionario #bd
