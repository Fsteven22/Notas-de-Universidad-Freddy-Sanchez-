---
dg-publish: true
tags: [TICG1018, unidad2, fn, normalizacion, bd]
---

# ðŸ“ Segunda y Tercera Forma Normal (y BCNF)

## ðŸŽ¯ IntroducciÃ³n

> [!info] ðŸ’¡ Â¿Por QuÃ© 1FN No Basta?
>
> Una tabla puede estar en 1FN y aÃºn asÃ­ tener problemas. Si un dato depende de **solo parte de la PK** (dependencia parcial) o de **otro dato que no es clave** (dependencia transitiva), aparece informaciÃ³n duplicada y anomalÃ­as al insertar, borrar o actualizar.
>
> **La cura estÃ¡ en orden:** primero 2FN, luego 3FN.
>
> | Nivel | QuÃ© elimina | AnalogÃ­a |
> |---|---|---|
> | **1FN** | Grupos repetitivos | Una caja con un objeto, no una lista |
> | **2FN** | Dependencias parciales | Nada depende de solo "mitad" de la llave |
> | **3FN** | Dependencias transitivas | Nada depende de un "intermediario" no-clave |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-04-flow.svg]]

---

## ðŸ“‹ Definiciones Formales

### 1ï¸âƒ£ Dependencia funcional (DF)

> [!note] ðŸ“‹ DefiniciÃ³n â€” DF
>
> `X â†’ Y` se lee: **"conociendo X, sÃ© Y"**.
>
> Ejemplos:
> - `PROJ_NUM â†’ PROJ_NAME` (si conozco el nÃºmero del proyecto, conozco su nombre)
> - `EMP_NUM â†’ EMP_NAME` (si conozco el nÃºmero del empleado, conozco su nombre)
>
> **Determinante:** es X (el dato del que parte la flecha).
> **Dependiente:** es Y (el dato al que llega la flecha).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-01-graph.svg]]

> [!info] ðŸ“– El deck de cÃ¡tedra: la dependencia funcional (slides04 y BD 02.3)
> El deck del Ing. Magallanes define la DF asÃ­: *"la relaciÃ³n que existe entre las columnas de una tabla"* â€” considerando dos columnas A y B donde B queda determinado por A. El otro deck (BD 02.3, Unidad 2) aÃ±ade el vocabulario formal.

![[Archivos/bd-s04-p10.png]]

![[Archivos/bd-023-p12.png]]

> **DefiniciÃ³n formal (BD 02.3, p. 12):** *"ocurre cuando el valor de un atributo o varios determina el valor de un segundo atributo o varios"* (A â†’ B). El atributo a la izquierda es el **determinante**, el de la derecha el **dependiente**.
>
> **Ejemplo del deck (BD 02.3, p. 13):** `CLIENTE(NÃºmero_cliente, Nombre, TelÃ©fono, Fecha_Nacimiento, Edad)` tiene las DF `NÃºmero_cliente â†’ Nombre`, `NÃºmero_cliente â†’ TelÃ©fono`, `NÃºmero_cliente â†’ Fecha_Nacimiento`â€¦ y `Fecha_Nacimiento â†’ Edad` â€” que es **transitiva** y por eso va a la 3FN.

![[Archivos/bd-s04-p11.png]]

> **El ejemplo del deck (slides04, p. 11):** el diagrama de flechas de `StdSSN`, `StdCity`, `StdClass â†’ OfferNo`, `OffTerm`, `OffYear`, `Course` es la forma en que el docente espera ver las DF dibujadas.

### 2ï¸âƒ£ Las 3 anomalÃ­as

> [!note] ðŸ“‹ Las 3 anomalÃ­as
>
> Cuando los datos estÃ¡n duplicados, aparecen estas anomalÃ­as:
>
> | AnomalÃ­a | QuÃ© pasa | Ejemplo |
> |---|---|---|
> | **InserciÃ³n** | Para agregar algo nuevo, necesitas inventar datos de otro | Agregar un producto nuevo obliga a crear una venta falsa |
> | **EliminaciÃ³n** | Al borrar algo, borras informaciÃ³n que no querÃ­as perder | Borrar la Ãºltima venta de un producto borra el precio del producto |
> | **ActualizaciÃ³n** | Cambiar un dato obliga tocar muchas filas, y si falla una, se corrompe | Cambiar el precio del "Arroz" en cada venta donde aparece |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-05-flow.svg]]

> [!info] ðŸ“– El deck de cÃ¡tedra: las anomalÃ­as, con su ejemplo (slides04, pp. 2-4 y BD 02.3, pp. 5-7)
> El deck arranca con la redundancia: *"las tablas que tienen datos redundantes pueden tener problemas llamados anomalÃ­as de actualizaciÃ³n"*, y las clasifica en inserciÃ³n, eliminaciÃ³n y modificaciÃ³n.

![[Archivos/bd-s04-p8.png]]

![[Archivos/bd-023-p14.png]]

> **Dependencia completa y parcial (BD 02.3, p. 14):** *"existe una dependencia completa si B es dependiente completamente de A y no de un subconjunto de los atributos de A"* â€” la definiciÃ³n exacta de la 2FN.
>
> **Ejercicios del deck (BD 02.3, pp. 15 y 18-19):** el deck incluye el diagrama de dependencias que hay que clasificar, el caso `empID` + `projNum` como PK compuesta, y la pregunta directa *"Â¿EstÃ¡ en 2FN? Â¿Y en 3FN?"*.

---

## ðŸ”‘ Diferencia clave: 2FN vs 3FN

> [!tip] ðŸŽ¯ La diferencia en una frase
>
> **2FN** elimina dependencias de **parte de la PK** (parciales).  
> **3FN** elimina dependencias de **otro dato no-clave** (transitivas).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-03-flow.svg]]

### 2ï¸âƒ£ Segunda forma normal (2FN)

> [!note] ðŸ“‹ DefiniciÃ³n â€” 2FN
>
> Una tabla estÃ¡ en **2FN** si:
> 1. EstÃ¡ en **1FN**.
> 2. No tiene **dependencias parciales**: ningÃºn atributo no-clave depende de solo *parte* de la PK.
>
> **Importante:** si la PK es simple (un solo atributo), la tabla estÃ¡ automÃ¡ticamente en 2FN (no hay "parte" de la PK).
>
> **Caso PROJECT (Coronel cap. 6):**
>
> Tabla original `1NF(PROJ_NUM, EMP_NUM, PROJ_NAME, EMP_NAME, JOB_CLASS, CHG_HOUR, HOURS)` tiene parciales:
> - `PROJ_NUM â†’ PROJ_NAME`
> - `EMP_NUM â†’ EMP_NAME, JOB_CLASS, CHG_HOUR`
>
> Se parte en:
> - `PROJECT(PROJ_NUM, PROJ_NAME)`
> - `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)`
> - `ASSIGNMENT(PROJ_NUM, EMP_NUM, ASSIGN_HOURS)`
>
> **Regla de oro:** el determinante se queda en la tabla original como FK (copiar, no mudar).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-06-er.svg]]

### 3ï¸âƒ£ Tercera forma normal (3FN)

> [!note] ðŸ“‹ DefiniciÃ³n â€” 3FN
>
> Una tabla estÃ¡ en **3FN** si:
> 1. EstÃ¡ en **2FN**.
> 2. No tiene **dependencias transitivas**: ningÃºn atributo no-clave depende de otro atributo no-clave.
>
> **Â¿QuÃ© es un no-primo?** Es un atributo que **no forma parte de ninguna clave candidata**.
>
> **Caso JOB (Coronel cap. 6):**
>
> En `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)` sobrevive:
> - `JOB_CLASS â†’ CHG_HOUR`
>
> Ambos son no-primos â‡’ transitiva. Se extrae:
> - `JOB(JOB_CLASS, CHG_HOUR)`
> - `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS FK)`
>
> Resultado: 4 tablas `PROJECT, EMPLOYEE, JOB, ASSIGNMENT`. Cambiar `CHG_HOUR` toca **una** fila.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-07-er.svg]]

> [!info] ðŸ“– El deck de cÃ¡tedra: la 3FN y la dependencia transitiva (slides04 y BD 02.3)
> El deck del Ing. Magallanes cierra con la tabla que **no** estÃ¡ en 3FN y su particiÃ³n en 3FN.

![[Archivos/bd-s04-p14.png]]

![[Archivos/bd-s04-p15.png]]

![[Archivos/bd-023-p20.png]]

> **3FN segÃºn el deck (slides04, p. 14):** *"una tabla estÃ¡ en tercera forma normal cuando estÃ¡ en 1FN y 2FN, y cada columna que non-primary-key es dependiente solo de las columnas de clave primaria yâ€¦ "*.
>
> **Dependencia transitiva (BD 02.3, p. 20):** *"si Y depende funcionalmente de X y Z de Y, pero X no depende funcionalmente de Y, se dice que Z depende transitivamente de X"*.
>
> **El caso del deck (BD 02.3, p. 21):** *"la Ãºnica clave forÃ¡nea es {Torneo, AÃ±o}. La violaciÃ³n de la 3FN ocurre porque el atributo no primario Fecha de nacimiento del ganador es dependiente transitivamente de {Torneo, AÃ±o} vÃ­a el atributo no primario Ganador"*.

### 4ï¸âƒ£ BCNF (menciÃ³n)

> [!note] ðŸ“‹ DefiniciÃ³n â€” Boyce-Codd Normal Form
>
> Todo **determinante es clave candidata**. Es una 3FN mÃ¡s estricta.
>
> **Ejemplo:** `R(A,B,C)` con `AB â†’ C` y `C â†’ B`, PK = AB.
> - EstÃ¡ en 3FN (B es primo, parte de la PK).
> - No estÃ¡ en BCNF: C determina a B sin ser clave.
> - Se parte en `R1(C,B)` + `R2(A,C)`.

---

## ðŸ› ï¸ MÃ©todo: Normalizar paso a paso

> [!note] ðŸ“‹ Protocolo
>
> 1. **Dibuja el diagrama de dependencias:** PK en negrita; flechas sanas arriba, sospechosas abajo.
> 2. **A 2FN:** por cada determinante parcial, crea tabla con Ã©l como PK. DÃ©jalo en la original como FK. Mueve sus dependientes.
> 3. **A 3FN:** por cada transitiva, crea tabla con su determinante como PK. DÃ©jalo como FK. Mueve sus dependientes.
> 4. **Chequeo BCNF:** Â¿toda flecha nace de una clave? Si sÃ­, ya estÃ¡s en BCNF.
>
> **Principio clave:** el determinante nunca abandona la tabla original. Se queda como FK (copiar, no mudar).

---

## ðŸŽ¨ Ejemplo Trabajado Completo

> [!example] ðŸŸ¢ De 1NF a 3FN sin perder datos
>
> Entrada: `1NF(PROJ_NUM, EMP_NUM, PROJ_NAME, EMP_NAME, JOB_CLASS, CHG_HOUR, HOURS)`.
>
> > [!success]- âœ… Pasos
> >
> > 1. Parciales â†’ `PROJECT(PROJ_NUM, PROJ_NAME)` + `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)` + `ASSIGNMENT(PROJ_NUM, EMP_NUM, ASSIGN_HOURS)`.
> > 2. Transitiva `JOB_CLASS â†’ CHG_HOUR` â†’ `JOB(JOB_CLASS, CHG_HOUR)` + `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS FK)`.
> >
> > Resultado: 4 tablas, 0 duplicados. Cambiar `CHG_HOUR` toca solo la tabla `JOB`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-02-er.svg]]

---

## âš ï¸ Errores Comunes

### âŒ Error 1: Normalizar PK simple a 2FN

> [!danger] âŒ Viola: sin PK compuesta no hay parciales
>
> Buscar dependencias parciales con PK de un solo atributo es imposible. Es 2FN automÃ¡tica. El trabajo real ahÃ­ es la transitiva (3FN).

### âŒ Error 2: Mover el determinante fuera

> [!danger] âŒ Viola: el determinante se queda como FK
>
> Sacar `PROJ_NUM` de ASSIGNMENT rompe el puente. Las tablas nuevas quedan huÃ©rfanas. Crea la tabla hija **copiando**, no mudando.

### âŒ Error 3: Confundir parcial con transitiva

> [!danger] âŒ Viola: parcial = parte de la PK; transitiva = no-primo â†’ no-primo
>
> - âŒ **Error:** tratar `(JOB_CLASS â†’ CHG_HOUR)` como parcial.
> - âœ… **Correcto:** JOB_CLASS no es parte de la PK â‡’ es transitiva â‡’ tabla JOB.

---

## ðŸ“ Ejercicios Propuestos

### âœï¸ Ejercicio 1 â€” Detecta la vulnerabilidad

> [!example] ðŸ“‹ Planteamiento
>
> `VENTA(codigo PK, fecha, idProd, nombreProd, precio, cantidad)`: Â¿quÃ© depende de parte de la PK y quÃ© depende de otro no-primo?
>
> > [!success]- âœ… SoluciÃ³n
> >
> > - Parcial: `idProd â†’ nombreProd, precio` (el producto se sabe sin la venta).
> > - Transitiva: ninguna clÃ¡sica aquÃ­ (precio no depende de nombreProd directamente; si existiera `categoria â†’ descuento`, sÃ­ serÃ­a transitiva).

### âœï¸ Ejercicio 2 â€” Lleva a 3FN

> [!example] ðŸ“‹ Planteamiento
>
> Parte `VENTA` a 2FN y luego a 3FN con schemas finales.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > - 2FN: `PRODUCTO(idProd, nombreProd, precio)` + `VENTA(codigo, fecha, idProd FK, cantidad)`.
> > - 3FN: verificar si hay transitivas. Si `idProd â†’ categoria â†’ descuento`, nace `CATEGORIA`.

### âœï¸ Ejercicio 3 â€” Chequeo BCNF

> [!example] ðŸ“‹ Planteamiento
>
> `R(A,B,C)` con `AB â†’ C` y `C â†’ B`, PK = AB. Â¿EstÃ¡ en 3FN? Â¿Y en BCNF?
>
> > [!success]- âœ… SoluciÃ³n
> >
> > - 3FN: sÃ­ (B es primo).
> > - BCNF: no (C determina a B sin ser clave). Se parte en `R1(C,B)` + `R2(A,C)`.

---

## ðŸŽ¯ Metas de Aprendizaje

> [!note] ðŸ“‹ Nivel BÃ¡sico
>
> - [ ] Defino DF, determinante, parcial y transitiva sin mirar.
> - [ ] Nombro las 3 anomalÃ­as con ejemplo propio.

> [!note] ðŸ“‹ Nivel Intermedio
>
> - [ ] Llevo una tabla 1FN â†’ 2FN â†’ 3FN con schemas.
> - [ ] Decido BCNF mirando si todo determinante es clave.

> [!note] ðŸ“‹ Nivel Avanzado
>
> - [ ] Dibujo el diagrama de dependencias antes de partir.
> - [ ] Detecto en el proyecto columnas que esconden transitivas.

---

## ðŸ” Repaso SR (flashcards)

#flashcards/bd-u2

> [!note] ðŸ§  Repasa con el plugin Spaced Repetition

- Â¿DF en 1 lÃ­nea?::Xâ†’Y: conociendo X conozco Y.
- Â¿3 anomalÃ­as?::InserciÃ³n (dummy), eliminaciÃ³n (borra de mÃ¡s), actualizaciÃ³n (a medias corrompe).
- Â¿2FN?::1FN sin dependencias parciales; PK simple â‡’ automÃ¡tica.
- Â¿3FN?::2FN sin dependencias transitivas (no-primo â†’ no-primo).
- Â¿Caso PROJECT?::Parciales â†’ PROJECT + EMPLOYEE; transitiva â†’ JOB.
- Â¿Determinante se va o se queda?::Se queda como FK (copiar, no mudar).
- Â¿BCNF en 1 lÃ­nea?::Todo determinante es clave candidata.
- Â¿Diferencia 2FN vs 3FN?::2FN quita parciales (parte de la PK); 3FN quita transitivas (no-primo â†’ no-primo).

---

## ðŸ”— Seguir estudiando

> [!info] ðŸ“š Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Ãndice Unidad 2: [[00 - Ãndice Unidad 2]]
> - Anterior: [[02 - Primera forma normal y diccionario de datos]]
> - Siguiente: [[04 - NormalizaciÃ³n paso a paso]]

---

## ðŸ“š Referencias

> [!quote] ðŸ“– Fuentes
>
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (DFs, anomalÃ­as, 2FN Â§6.3.2, 3FN Â§6.3.3, BCNF Â§6.6.1).
> - Deck BD 02 MC_a_ML: 1FN base + formas listadas; esta nota completa 2FN/3FN/BCNF.

---

**Tags:** #TICG1018 #unidad2 #2fn #3fn #bcnf #normalizacion #bd

