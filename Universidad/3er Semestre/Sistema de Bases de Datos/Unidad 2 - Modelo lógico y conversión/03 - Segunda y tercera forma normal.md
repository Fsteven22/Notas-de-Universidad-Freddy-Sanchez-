---
dg-publish: true
tags: [TICG1018, unidad2, fn, normalizacion, bd]
---

# 📐 Segunda y Tercera Forma Normal (y BCNF)

## 🎯 Introducción

> [!info] 💡 ¿Por Qué 1FN No Basta?
>
> Una tabla puede estar en 1FN y aún así tener problemas. Si un dato depende de **solo parte de la PK** (dependencia parcial) o de **otro dato que no es clave** (dependencia transitiva), aparece información duplicada y anomalías al insertar, borrar o actualizar.
>
> **La cura está en orden:** primero 2FN, luego 3FN.
>
> | Nivel | Qué elimina | Analogía |
> |---|---|---|
> | **1FN** | Grupos repetitivos | Una caja con un objeto, no una lista |
> | **2FN** | Dependencias parciales | Nada depende de solo "mitad" de la llave |
> | **3FN** | Dependencias transitivas | Nada depende de un "intermediario" no-clave |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-04-flow.svg]]

---

## 📋 Definiciones Formales

### 1️⃣ Dependencia funcional (DF)

> [!note] 📋 Definición — DF
>
> `X → Y` se lee: **"conociendo X, sé Y"**.
>
> Ejemplos:
> - `PROJ_NUM → PROJ_NAME` (si conozco el número del proyecto, conozco su nombre)
> - `EMP_NUM → EMP_NAME` (si conozco el número del empleado, conozco su nombre)
>
> **Determinante:** es X (el dato del que parte la flecha).
> **Dependiente:** es Y (el dato al que llega la flecha).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-01-graph.svg]]

### 2️⃣ Las 3 anomalías

> [!note] 📋 Las 3 anomalías
>
> Cuando los datos están duplicados, aparecen estas anomalías:
>
> | Anomalía | Qué pasa | Ejemplo |
> |---|---|---|
> | **Inserción** | Para agregar algo nuevo, necesitas inventar datos de otro | Agregar un producto nuevo obliga a crear una venta falsa |
> | **Eliminación** | Al borrar algo, borras información que no querías perder | Borrar la última venta de un producto borra el precio del producto |
> | **Actualización** | Cambiar un dato obliga tocar muchas filas, y si falla una, se corrompe | Cambiar el precio del "Arroz" en cada venta donde aparece |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-05-flow.svg]]

---

## 🔑 Diferencia clave: 2FN vs 3FN

> [!tip] 🎯 La diferencia en una frase
>
> **2FN** elimina dependencias de **parte de la PK** (parciales).  
> **3FN** elimina dependencias de **otro dato no-clave** (transitivas).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-03-flow.svg]]

### 2️⃣ Segunda forma normal (2FN)

> [!note] 📋 Definición — 2FN
>
> Una tabla está en **2FN** si:
> 1. Está en **1FN**.
> 2. No tiene **dependencias parciales**: ningún atributo no-clave depende de solo *parte* de la PK.
>
> **Importante:** si la PK es simple (un solo atributo), la tabla está automáticamente en 2FN (no hay "parte" de la PK).
>
> **Caso PROJECT (Coronel cap. 6):**
>
> Tabla original `1NF(PROJ_NUM, EMP_NUM, PROJ_NAME, EMP_NAME, JOB_CLASS, CHG_HOUR, HOURS)` tiene parciales:
> - `PROJ_NUM → PROJ_NAME`
> - `EMP_NUM → EMP_NAME, JOB_CLASS, CHG_HOUR`
>
> Se parte en:
> - `PROJECT(PROJ_NUM, PROJ_NAME)`
> - `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)`
> - `ASSIGNMENT(PROJ_NUM, EMP_NUM, ASSIGN_HOURS)`
>
> **Regla de oro:** el determinante se queda en la tabla original como FK (copiar, no mudar).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-06-er.svg]]

### 3️⃣ Tercera forma normal (3FN)

> [!note] 📋 Definición — 3FN
>
> Una tabla está en **3FN** si:
> 1. Está en **2FN**.
> 2. No tiene **dependencias transitivas**: ningún atributo no-clave depende de otro atributo no-clave.
>
> **¿Qué es un no-primo?** Es un atributo que **no forma parte de ninguna clave candidata**.
>
> **Caso JOB (Coronel cap. 6):**
>
> En `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)` sobrevive:
> - `JOB_CLASS → CHG_HOUR`
>
> Ambos son no-primos ⇒ transitiva. Se extrae:
> - `JOB(JOB_CLASS, CHG_HOUR)`
> - `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS FK)`
>
> Resultado: 4 tablas `PROJECT, EMPLOYEE, JOB, ASSIGNMENT`. Cambiar `CHG_HOUR` toca **una** fila.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-07-er.svg]]

### 4️⃣ BCNF (mención)

> [!note] 📋 Definición — Boyce-Codd Normal Form
>
> Todo **determinante es clave candidata**. Es una 3FN más estricta.
>
> **Ejemplo:** `R(A,B,C)` con `AB → C` y `C → B`, PK = AB.
> - Está en 3FN (B es primo, parte de la PK).
> - No está en BCNF: C determina a B sin ser clave.
> - Se parte en `R1(C,B)` + `R2(A,C)`.

---

## 🛠️ Método: Normalizar paso a paso

> [!note] 📋 Protocolo
>
> 1. **Dibuja el diagrama de dependencias:** PK en negrita; flechas sanas arriba, sospechosas abajo.
> 2. **A 2FN:** por cada determinante parcial, crea tabla con él como PK. Déjalo en la original como FK. Mueve sus dependientes.
> 3. **A 3FN:** por cada transitiva, crea tabla con su determinante como PK. Déjalo como FK. Mueve sus dependientes.
> 4. **Chequeo BCNF:** ¿toda flecha nace de una clave? Si sí, ya estás en BCNF.
>
> **Principio clave:** el determinante nunca abandona la tabla original. Se queda como FK (copiar, no mudar).

---

## 🎨 Ejemplo Trabajado Completo

> [!example] 🟢 De 1NF a 3FN sin perder datos
>
> Entrada: `1NF(PROJ_NUM, EMP_NUM, PROJ_NAME, EMP_NAME, JOB_CLASS, CHG_HOUR, HOURS)`.
>
> > [!success]- ✅ Pasos
> >
> > 1. Parciales → `PROJECT(PROJ_NUM, PROJ_NAME)` + `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)` + `ASSIGNMENT(PROJ_NUM, EMP_NUM, ASSIGN_HOURS)`.
> > 2. Transitiva `JOB_CLASS → CHG_HOUR` → `JOB(JOB_CLASS, CHG_HOUR)` + `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS FK)`.
> >
> > Resultado: 4 tablas, 0 duplicados. Cambiar `CHG_HOUR` toca solo la tabla `JOB`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-02-er.svg]]

---

## ⚠️ Errores Comunes

### ❌ Error 1: Normalizar PK simple a 2FN

> [!danger] ❌ Viola: sin PK compuesta no hay parciales
>
> Buscar dependencias parciales con PK de un solo atributo es imposible. Es 2FN automática. El trabajo real ahí es la transitiva (3FN).

### ❌ Error 2: Mover el determinante fuera

> [!danger] ❌ Viola: el determinante se queda como FK
>
> Sacar `PROJ_NUM` de ASSIGNMENT rompe el puente. Las tablas nuevas quedan huérfanas. Crea la tabla hija **copiando**, no mudando.

### ❌ Error 3: Confundir parcial con transitiva

> [!danger] ❌ Viola: parcial = parte de la PK; transitiva = no-primo → no-primo
>
> - ❌ **Error:** tratar `(JOB_CLASS → CHG_HOUR)` como parcial.
> - ✅ **Correcto:** JOB_CLASS no es parte de la PK ⇒ es transitiva ⇒ tabla JOB.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Detecta la vulnerabilidad

> [!example] 📋 Planteamiento
>
> `VENTA(codigo PK, fecha, idProd, nombreProd, precio, cantidad)`: ¿qué depende de parte de la PK y qué depende de otro no-primo?
>
> > [!success]- ✅ Solución
> >
> > - Parcial: `idProd → nombreProd, precio` (el producto se sabe sin la venta).
> > - Transitiva: ninguna clásica aquí (precio no depende de nombreProd directamente; si existiera `categoria → descuento`, sí sería transitiva).

### ✏️ Ejercicio 2 — Lleva a 3FN

> [!example] 📋 Planteamiento
>
> Parte `VENTA` a 2FN y luego a 3FN con schemas finales.
>
> > [!success]- ✅ Solución
> >
> > - 2FN: `PRODUCTO(idProd, nombreProd, precio)` + `VENTA(codigo, fecha, idProd FK, cantidad)`.
> > - 3FN: verificar si hay transitivas. Si `idProd → categoria → descuento`, nace `CATEGORIA`.

### ✏️ Ejercicio 3 — Chequeo BCNF

> [!example] 📋 Planteamiento
>
> `R(A,B,C)` con `AB → C` y `C → B`, PK = AB. ¿Está en 3FN? ¿Y en BCNF?
>
> > [!success]- ✅ Solución
> >
> > - 3FN: sí (B es primo).
> > - BCNF: no (C determina a B sin ser clave). Se parte en `R1(C,B)` + `R2(A,C)`.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino DF, determinante, parcial y transitiva sin mirar.
> - [ ] Nombro las 3 anomalías con ejemplo propio.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Llevo una tabla 1FN → 2FN → 3FN con schemas.
> - [ ] Decido BCNF mirando si todo determinante es clave.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Dibujo el diagrama de dependencias antes de partir.
> - [ ] Detecto en el proyecto columnas que esconden transitivas.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition

- ¿DF en 1 línea?::X→Y: conociendo X conozco Y.
- ¿3 anomalías?::Inserción (dummy), eliminación (borra de más), actualización (a medias corrompe).
- ¿2FN?::1FN sin dependencias parciales; PK simple ⇒ automática.
- ¿3FN?::2FN sin dependencias transitivas (no-primo → no-primo).
- ¿Caso PROJECT?::Parciales → PROJECT + EMPLOYEE; transitiva → JOB.
- ¿Determinante se va o se queda?::Se queda como FK (copiar, no mudar).
- ¿BCNF en 1 línea?::Todo determinante es clave candidata.
- ¿Diferencia 2FN vs 3FN?::2FN quita parciales (parte de la PK); 3FN quita transitivas (no-primo → no-primo).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Anterior: [[02 - Primera forma normal y diccionario de datos]]
> - Siguiente: [[04 - Normalización paso a paso]]

---

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (DFs, anomalías, 2FN §6.3.2, 3FN §6.3.3, BCNF §6.6.1).
> - Deck BD 02 MC_a_ML: 1FN base + formas listadas; esta nota completa 2FN/3FN/BCNF.

---

**Tags:** #TICG1018 #unidad2 #2fn #3fn #bcnf #normalizacion #bd
