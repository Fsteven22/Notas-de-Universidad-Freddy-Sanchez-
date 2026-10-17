---
dg-publish: true
tags: [TICG1018, unidad2, fn, normalizacion, bd]
---

# 📐 Segunda y Tercera Forma Normal (y BCNF)

## 🎯 Introducción

> [!info] 💡 ¿Por Qué 1FN No Basta?
>
> Una tabla en 1FN puede seguir mintiendo: si un dato depende de **parte** de la PK (parcial) o de **otro no-primo** (transitiva), cada fila duplica datos y aparecen anomalías — insertar exige inventar, borrar destruye de más, actualizar a medias corrompe. 2FN y 3FN son la cura, en ese orden.
>
> **Aplicaciones:**
> - **Diseño:** todo esquema convertido (U2-01) se valida aquí antes del SQL.
> - **Lección 1:** detectar parcial vs transitiva en un diagrama de dependencias es pregunta segura.
> - **Proyecto:** tablas en 3FN no duplican hechos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-01-graph.svg]]

---

## 📋 Definiciones Formales

### 1️⃣ Dependencia funcional — X determina Y

> [!note] 📋 Definición — DF (Coronel cap. 6)
>
> `X → Y`: conociendo X conoces Y (X = **determinante**). Ej.: `PROJ_NUM → PROJ_NAME`; `EMP_NUM → EMP_NAME, JOB_CLASS`.
>
> **Se lee así:** dibuja flechas del determinante al dependiente (diagrama de dependencias): las flechas *sobre* la PK son sanas; las de *abajo* (parciales, transitivas) son las que se eliminan.

### 2️⃣ Anomalías — lo que duele sin normalizar

> [!note] 📋 Las 3 anomalías (Coronel cap. 1/6)
>
> - **Inserción:** para agregar un agente nuevo hay que inventar un cliente falso (dummy).
> - **Eliminación:** borrar los últimos clientes borra al agente con ellos.
> - **Actualización:** cambiar el teléfono de Leah Hahn exige tocar cada fila donde aparece — a medias, corrompe.
>
> **Ejemplo:** `EMP_NAME` de Dave Senior escrito como *DaveSenior* en una fila y *D.Senior* en otra: duplicar hechos invita a mentir.

### 3️⃣ Segunda forma normal — fuera parciales

> [!note] 📋 Definición — 2FN (Coronel 6.3.2)
>
> 1FN + **sin dependencias parciales** (ningún atributo depende de *parte* de la PK). Solo aplica con PK **compuesta**: PK de un atributo ⇒ 2FN automática.
>
> **Caso PROJECT (libro):** `1NF(PROJ_NUM, EMP_NUM, PROJ_NAME, EMP_NAME, JOB_CLASS, CHG_HOUR, HOURS)` con parciales `(PROJ_NUM → PROJ_NAME)` y `(EMP_NUM → EMP_NAME, JOB_CLASS, CHG_HOUR)` se parte en:
>
> - `PROJECT(PROJ_NUM, PROJ_NAME)` · `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)` · `ASSIGNMENT(PROJ_NUM, EMP_NUM, ASSIGN_HOURS)`
>
> Los determinantes **se quedan** en la original como FK (así nacen las relaciones). Lo que depende de la PK completa (`HOURS` → `ASSIGN_HOURS`) no se mueve.

### 4️⃣ Tercera forma normal — fuera transitivas

> [!note] 📋 Definición — 3FN (Coronel 6.3.3)
>
> 2FN + **sin dependencias transitivas** (ningún no-primo depende de otro no-primo).
>
> **Caso JOB (libro):** en `EMPLOYEE` sobrevive `(JOB_CLASS → CHG_HOUR)` — ambos no-primos ⇒ se extrae `JOB(JOB_CLASS, CHG_HOUR)` y en `EMPLOYEE` queda `JOB_CLASS` como FK. Final: 4 tablas `PROJECT, EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS), JOB, ASSIGNMENT`.

### 5️⃣ BCNF — el caso borde (mención)

> [!note] 📋 Definición — Boyce-Codd (Coronel 6.6.1)
>
> Todo **determinante es clave candidata** (3FN especial). Aparece con claves candidatas solapadas: ej. `R(A,B,C)` con `AB → C` y `C → B` está en 3FN pero C determina sin ser clave ⇒ se parte.
>
> **Se lee así:** si ya estás en 3FN y cada flecha nace de una clave, estás en BCNF sin hacer nada más.

---

## 🛠️ Método: Normalizar Paso a Paso

> [!note] 📋 Protocolo Coronel (Fig. 6.3 → 6.4 → 6.5)
>
> 1. Dibuja el diagrama de dependencias (PK en negrita; flechas sanas arriba, sospechosas abajo).
> 2. **A 2FN:** por cada determinante parcial, crea tabla con él como PK (déjalo en la original como FK); mueve sus dependientes.
> 3. **A 3FN:** por cada transitiva, crea tabla con su determinante como PK (déjalo como FK); mueve sus dependientes.
> 4. **Chequeo BCNF:** ¿toda flecha nace de una clave? Si sí, listo.
>
> **Principio clave:** el determinante nunca abandona la tabla original — se queda como FK.

---

## 🎨 Ejemplo Trabajado Completo

> [!example] 🟢 De 1NF a 3FN sin perder datos
>
> Entrada: `1NF(PROJ_NUM, EMP_NUM, PROJ_NAME, EMP_NAME, JOB_CLASS, CHG_HOUR, HOURS)`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u2-03-02-er.svg]]
>
> **Se lee así:** parciales → PROJECT + EMPLOYEE (+ASSIGNMENT con lo completo); transitiva → JOB. 4 tablas, 0 duplicados: cambiar `CHG_HOUR` toca **una** fila.

---

## ⚠️ Errores Comunes y Principios Lógicos

### ❌ Error 1: Normalizar PK simple a 2FN

> [!danger] ❌ Viola: sin PK compuesta no hay parciales
>
> Buscar dependencias parciales con PK de un atributo es caza imposible: es 2FN automática. El trabajo real ahí es la transitiva (3FN).

### ❌ Error 2: Mover el determinante fuera

> [!danger] ❌ Viola: el determinante se queda como FK
>
> Sacar `PROJ_NUM` de ASSIGNMENT rompe el puente: las tablas nuevas quedan huérfanas. Crea la tabla hija **copiando**, no mudando.

### ❌ Error 3: Confundir parcial con transitiva

> [!danger] ❌ Viola: parcial = parte de la PK; transitiva = no-primo → no-primo
>
> - ❌ **EL ERROR ESTÁ AQUÍ:** tratar `(JOB_CLASS → CHG_HOUR)` como parcial.
> - ✅ Así sí: JOB_CLASS no es parte de ninguna PK ⇒ transitiva ⇒ tabla JOB.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Detecta la vulnerabilidad

> [!example] 📋 Planteamiento
>
> `VENTA(codigo PK, fecha, idProd, nombreProd, precio, cantidad)`: ¿qué depende de parte de la PK y qué depende de otro no-primo? Nombra parcial y transitiva sin partir nada.
>
> > [!success]- ✅ Solución
> >
> > - Parcial: `(idProd → nombreProd, precio)` — el producto se sabe sin la venta.
> > - Transitiva: ninguna clásica aquí (precio no depende de nombreProd); si `categoria → descuento` existiera, sería transitiva.

### ✏️ Ejercicio 2 — Lleva a 3FN

> [!example] 📋 Planteamiento
>
> Parte VENTA a 2FN y luego a 3FN con schemas finales.
>
> > [!success]- ✅ Solución
> >
> > - 2FN: `PRODUCTO(idProd, nombreProd, precio)` + `VENTA(codigo, fecha, idProd FK, cantidad)`.
> > - 3FN: nada más que mover (verifica: ¿algún no-primo determina a otro? Si `idProd → categoria → descuento`, nace `CATEGORIA`).

### ✏️ Ejercicio 3 — Chequeo BCNF

> [!example] 📋 Planteamiento
>
> `R(A,B,C)` con `AB → C` y `C → B`, PK = AB. ¿Está en 3FN? ¿Y en BCNF?
>
> > [!success]- ✅ Solución
> >
> > - 3FN sí (B es primo: parte de la PK). BCNF no: C determina a B sin ser clave ⇒ se parte en `R1(C,B)` + `R2(A,C)`.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino DF, determinante, parcial y transitiva sin mirar.
> - [ ] Nombro las 3 anomalías con ejemplo propio.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Llevo una tabla 1NF→2FN→3FN con schemas.
> - [ ] Decido BCNF mirando si todo determinante es clave.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Dibujo el diagrama de dependencias antes de partir.
> - [ ] Detecto en el proyecto columnas que esconden transitivas.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition

- ¿DF en 1 línea?::X→Y: conociendo X conoces Y (X determinante).
- ¿3 anomalías?::Inserción (dummy), eliminación (borra de más), actualización (a medias corrompe).
- ¿2FN?::1FN sin parciales; PK simple ⇒ automática.
- ¿3FN?::2FN sin transitivas (no-primo → no-primo fuera).
- ¿Caso PROJECT?::Parciales→PROJECT+EMPLOYEE; transitiva→JOB; completo queda en ASSIGNMENT.
- ¿Determinante se va o se queda?::Se queda como FK (copiar, no mudar).
- ¿BCNF en 1 línea?::Todo determinante es clave candidata.
- ¿Parcial vs transitiva?::Parte de la PK vs no-primo que determina a otro no-primo.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Anterior: [[02 - Primera forma normal y diccionario de datos]] · Conversión: [[01 - Conversión MC a ML por cardinalidad]]
> - Diccionario: [[02 - Primera forma normal y diccionario de datos]]

---

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (DFs, anomalías, 2FN §6.3.2, 3FN §6.3.3, BCNF §6.6.1).
> - Deck BD 02 MC_a_ML: 1FN base + formas listadas; este nota completa 2FN/3FN/BCNF.

---

**Tags:** #TICG1018 #unidad2 #2fn #3fn #bcnf #normalizacion #bd
