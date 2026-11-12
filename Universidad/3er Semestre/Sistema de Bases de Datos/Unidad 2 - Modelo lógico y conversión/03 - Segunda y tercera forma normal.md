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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-04-flow.svg]]
>
> **Se lee así:** el diagrama es **la cadena causal completa** de la normalización, y se lee de arriba abajo. Arriba está el punto de partida: *tabla en 1FN con datos duplicados entre filas*. Desde ahí salen **dos caminos** según lo que dependa de qué: a la izquierda, *"depende solo de parte de la PK"* → **dependencia parcial**; a la derecha, *"depende de otro dato no-clave"* → **dependencia transitiva**. Los dos caminos convergen en el mismo sitio: *información duplicada*. Y esa duplicada se manifiesta en **tres anomalías** (inserción con datos falsos, eliminación que borra de más, actualización que corrompe), que se curan **en orden**: primero 2FN, después 3FN.
>
> **Por qué importa:** el diagrama explica por qué existen dos formas normales y no una. Si solo te supieras las definiciones, memorizarías "2FN = parcial, 3FN = transitiva" sin entender nada. El diagrama te da la razón: **las dos anomalías nacen de la misma causa** (la duplicación) y por eso las dos formas normales atacan la misma causa por dos vías distintas. Y fíjate en el orden "2FN → 3FN": no es una convención, es que **no puedes quitar una transitiva si antes queda una parcial**, porque la parcial se apoya en la parte de la PK.
>
> **Ejemplo:** la tabla `StaffBranch` de la lámina del deck es 1FN (cada celda tiene un valor) pero repite `branchAddress` y `telNo` en cada fila de la sucursal. `branchNo` es la PK, y de ella dependen `branchAddress` y `telNo`: eso es dependencia **parcial** (dependen de parte de la PK, y además son datos de otra entidad). Al separar `BRANCH` y `STAFF` se resuelven las dos cosas de un tiro.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-01-graph.svg]]

> [!info] 📖 El deck de cátedra: la dependencia funcional (slides04 y BD 02.3)
> El deck del Ing. Magallanes define la DF así: *"la relación que existe entre las columnas de una tabla"* — considerando dos columnas A y B donde B queda determinado por A. El otro deck (BD 02.3, Unidad 2) añade el vocabulario formal.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p10.png]]
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-023-p12.png]]
>
> **Definición formal (BD 02.3, p. 12):** *"ocurre cuando el valor de un atributo o varios determina el valor de un segundo atributo o varios"* (A → B). El atributo a la izquierda es el **determinante**, el de la derecha el **dependiente**.
>
> **Ejemplo del deck (BD 02.3, p. 13):** `CLIENTE(Número_cliente, Nombre, Teléfono, Fecha_Nacimiento, Edad)` tiene las DF `Número_cliente → Nombre`, `Número_cliente → Teléfono`, `Número_cliente → Fecha_Nacimiento`… y `Fecha_Nacimiento → Edad` — que es **transitiva** y por eso va a la 3FN.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p11.png]]
>
> **El ejemplo del deck (slides04, p. 11):** el diagrama de flechas de `StdSSN`, `StdCity`, `StdClass → OfferNo`, `OffTerm`, `OffYear`, `Course` es la forma en que el docente espera ver las DF dibujadas.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-05-flow.svg]]

> [!info] 📖 El deck de cátedra: las anomalías, con su ejemplo (slides04, pp. 2-4 y BD 02.3, pp. 5-7)
>
> El deck arranca con la redundancia: *"las tablas que tienen datos redundantes pueden tener problemas llamados anomalías de actualización"*, y las clasifica en inserción, eliminación y modificación.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p2.png]]
>
> **Se lee así:** la lámina (p. 2) pone el **problema y su tabla a la vez**, y la tabla `StaffBranch` es el ejemplo canónico de todo el curso. Tiene las columnas `staffNo · name · position · salary · branchNo · branchAddress · telNo` y seis empleados. Ahora mira las dos primeras filas: `S1500 Tom Daniels` y `S0003 Sally Adams` son **ambos de B001**, y ambos repiten `8 Jeffesorn Way, Portland, OR 97201` y `503-555-3618`. Esa repetición es la redundancia. La tabla es 1FN (cada celda tiene un solo valor) y aun así tiene un problema serio.
>
> **Por qué importa:** la observación clave de la lámina es que la redundancia **no es un error de formato sino de diseño**: los datos de la sucursal se guardaron en la tabla del empleado porque era "lo más rápido". La 1FN no lo detecta porque cada celda tiene un valor; lo detecta la 2FN, porque `branchAddress` y `telNo` dependen de `branchNo`, no de `staffNo`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p3.png]]
>
> **Se lee así:** la lámina (p. 3) es la **anomalía de inserción**, y el deck la plantea como dos si/no. Primero: *"suponga el ingreso de un nuevo personal de la sucursal 2 (B002); para esto también hay que registrar correctamente el detalle de la sucursal B002, para tener consistencia de datos"*. Es decir: para **añadir una persona** estás obligado a **repetir la dirección y el teléfono de la sucursal**. Segundo: *"suponga el ingreso de una nueva sucursal sin miembros en el staff; necesitaría registrar NULL en los atributos de staff"*. Es decir: para **añadir una sucursal** tienes que **inventar un empleado**.
>
> **Por qué importa:** las dos anomalías de inserción son la **misma información en el lugar equivocado**. Insertar es la operación más común de cualquier sistema, y aquí obliga a tocar información que no tiene nada que ver con la que estás insertando. Por eso la solución no es "cuida con los NULL": es **no guardar los datos de la sucursal en la tabla del empleado**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p4.png]]
>
> **Se lee así:** la lámina (p. 4) trae las **anomalías de borrado y de modificación**, en el mismo formato de "suponga que…". Borrado: *"suponga el borrado del registro para el staff S0415; esto conlleva a que se elimine la sucursal B003, y la pérdida de la sucursal de la base de datos"*. Modificación: *"suponga que hay que modificar el número telefónico de la sucursal B001; esto supondría que haya que modificar las filas 1 y 2"*.
>
> **Por qué importa:** estas dos son las más peligrosas porque **no se ven al cargar los datos**. Con la tabla llena no hay ni un error visible: todo parece correcto. El problema aparece el día que alguien borra al único empleado de la sucursal de Nueva York, o el día que la central cambia el teléfono de Portland. En ese momento, el error ya está en la base y nadie lo nota hasta que alguien necesita el dato.
>
> **Ejemplo:** borra `S0415` (Art Peters, el único de B003) y la sucursal de Nueva York **desaparece** de la base de datos. Si mañana la empresa quiere abrir otra sucursal en Nueva York, tendrá que volver a escribir la dirección… y si el teléfono había cambiado en 2023, se perdió. Eso es la anomalía de borrado, y por eso `BRANCH` tiene que ser una tabla propia.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-023-p6.png]]
>
> **Se lee así:** la lámina (p. 6 de BD 02.3) dice lo mismo con otros palabras: *"almacenamiento redundante: información repetida"* y *"anomalías de actualización: actualización de datos en copias → modificar dirección de una sucursal (inconsistencia)"*. Luego baja a las de inserción: *"no es posible almacenar información a menos que otra información se almacene"*, con los dos casos: *"insertar nuevo empleado (valores coherentes para Branch)"* e *"insertar nueva sucursal (valores no nulos en staffNo)"*.
>
> **Por qué importa:** la frase clave es *"a menos que otra información se almacene"*. Define la anomalía de inserción de forma general: **no puedes guardar un hecho si no guardas también otro hecho que no debería estar ahí**. Por eso no se arregla con `DEFAULT` ni con una Trigger: se arregla moviendo el dato a su propia tabla.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-023-p7.png]]
>
> **Se lee así:** la lámina (p. 7) cierra el bloque con la anomalía de borrado: *"eliminar información sin perder otra"* → *"eliminar último empleado de una sucursal"*. Fíjate en la formulación: **eliminar** información **sin perder otra**. No dice "eliminar mal": dice que la operación borra algo que debería sobrevivir.
>
> **Por qué importa:** las tres anomalías se pueden resumir en una frase que ayuda a recordarlas: la redundancia te obliga a **inventar** datos (inserción), a **borrar** de más (eliminación) y a **cambiar** en varios sitios (actualización). Los tres verbos son verbos de escritura, no de lectura: la redundancia solo molesta cuando alguien escribe.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-023-p14.png]]
>
> **Se lee así:** esta lámina (p. 14) es el **puente hacia la 2FN**: *"existe una dependencia completa si B es dependiente completamente de A y no de un subconjunto de los atributos de A"*. Traducido: `A` es la PK compuesta y `B` depende de **toda** `A`, no solo de una parte.
>
> **Por qué importa:** el deck llama "completa" a la dependencia buena y "parcial" a la mala. La 2FN consiste en que **toda** dependencia de la PK sea completa: si `PROJ_NAME` depende solo de `PROJ_NUM`, esa dependencia es parcial y hay que partir la tabla.
>
> **Ejemplo:** en `ASSIGNMENT(PROJ_NUM, EMP_NUM, ASSIGN_HOURS)`, `ASSIGN_HOURS` depende de **las dos** columnas a la vez → dependencia **completa** → sobrevive en la 2FN. En cambio, si `PROJ_NAME` estuviera en esa misma tabla, dependería solo de `PROJ_NUM` → **parcial** → `PROJ_NAME` se va a `PROJECT`.
>
> **Ejercicios del deck (BD 02.3, pp. 15 y 18-19):** el deck incluye el diagrama de dependencias que hay que clasificar, el caso `empID` + `projNum` como PK compuesta, y la pregunta directa *"¿Está en 2FN? ¿Y en 3FN?"*.

---

## 🔑 Diferencia clave: 2FN vs 3FN

> [!tip] 🎯 La diferencia en una frase
>
> **2FN** elimina dependencias de **parte de la PK** (parciales).  
> **3FN** elimina dependencias de **otro dato no-clave** (transitivas).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-03-flow.svg]]
>
> **Se lee así:** el diagrama pone **las dos formas normales lado a lado**, y cada lado tiene su propio subgrafo con el título. El de arriba, *"2FN: corta parciales"*, tiene dos flechas desde la PK compuesta `(PROJ_NUM, EMP_NUM)`: una hacia `PROJ_NAME` rotulada `PROJ_NUM`, y otra hacia `EMP_NAME, JOB_CLASS, CHG_HOUR` rotulada `EMP_NUM`. El de abajo, *"3FN: corta transitivas"*, parte de `EMPLOYEE(EMP_NUM, JOB_CLASS, CHG_HOUR)` y saca `CHG_HOUR` con la flecha rotulada `JOB_CLASS`.
>
> **Por qué importa:** la diferencia se ve en **qué lado de la flecha se lee el determinante**. En la 2FN, el determinante es **una parte de la PK** (`PROJ_NUM` o `EMP_NUM`): por eso la flecha sale de la PK compuesta. En la 3FN, el determinante es **una columna que no es clave** (`JOB_CLASS`): por eso la flecha sale de `JOB_CLASS`, no de la PK. Esa es toda la diferencia entre "parcial" y "transitiva", y por eso es tan fácil confundirlas: ambas se dibujan como flechas hacia un atributo.
>
> **Ejemplo:** `CHG_HOUR` (la tarifa por hora) depende de `JOB_CLASS` (el cargo), y `JOB_CLASS` depende de `EMP_NUM`. Eso es una cadena `EMP_NUM → JOB_CLASS → CHG_HOUR`: la **transitiva**. `CHG_HOUR` no depende de `EMP_NUM` directamente; depende *a través* de `JOB_CLASS`. Por eso `JOB` tiene que ser una tabla aparte, y por eso cambiar la tarifa de "Programador" toca **una** fila y no todas las filas de los programadores.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-06-er.svg]]
>
> **Se lee así:** el diagrama es **el estado después de aplicar la 2FN**, y hay que mirarlo con lupa para ver por qué todavía no es 3FN. `PROJECT(PROJ_NUM PK, PROJ_NAME)` y `EMPLOYEE(EMP_NUM PK, EMP_NAME, JOB_CLASS FK, CHG_HOUR)` ya están **partidas por la PK compuesta**: `PROJ_NAME` salió a su tabla y `EMP_NAME` salió a la suya. `ASSIGNMENT(PROJ_NUM PK FK, EMP_NUM PK FK, ASSIGN_HOURS)` conserva la PK compuesta con sus dos FKs y su atributo propio, que depende **completa** de las dos.
>
> **Por qué importa:** mira `EMPLOYEE`: tiene `JOB_CLASS` **marcado como FK** y `CHG_HOUR` como atributo normal. Esa marca es la **pista del siguiente paso**: `CHG_HOUR` depende de `JOB_CLASS`, y `JOB_CLASS` no es clave, así que todavía hay una dependencia transitiva. Si `CHG_HOUR` no estuviera ahí, la tabla ya sería 3FN.
>
> **Ejemplo:** el diagrama te dice que la 2FN **siempre deja la puerta abierta** a la 3FN. Por eso la secuencia es obligatoria: primero se parte por la PK (2FN) y solo entonces se puede ver qué dependencias quedan colgadas de atributos no-clave (3FN). Al revés, buscando transitivas en una tabla que todavía tiene parciales, se mezclan los dos problemas.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-07-er.svg]]

> [!info] 📖 El deck de cátedra: la 3FN y la dependencia transitiva (slides04 y BD 02.3)
>
> El deck del Ing. Magallanes cierra con la tabla que **no** está en 3FN y su partición en 3FN.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p14.png]]
>
> **Se lee así:** la lámina (p. 14) da la **definición completa** de la 3FN: *"una tabla está en tercera forma normal cuando está en 1FN y 2FN, y cada columna que no es primary key es dependiente solo de las columnas de clave primaria y no de otras columnas"*. Y remata con el resumen que hay que aprenderse de memoria: *"para 2FN debemos remover dependencias parciales y en 3FN debemos remover dependencias transitivas"*. Abajo está la tabla `StaffBranch` con la Primary key marcada y una flecha que dice: `branchNo → branchAddress, telNo` y `staffNo → name, position, salary, branchNo, branchAddress, telNo` → *"No 3FN: dependencia transitiva"*.
>
> **Por qué importa:** fíjate en el detalle de la flecha: la dependencia transitiva no va de la PK directamente a `branchAddress`, sino **a través de `branchNo`**. `staffNo` determina a `branchNo`, y `branchNo` determina a `branchAddress` y `telNo`. Por eso el nombre "transitiva": la dependencia **pasa por un intermediario** en lugar de ser directa.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p15.png]]
>
> **Se lee así:** la lámina (p. 15) es **la partición, lado a lado**, y es la mejor ayuda visual de la unidad. De izquierda a derecha: `StaffBranch (No 3FN)` con sus 6 filas completas → `Branch (2FN)` con las 3 sucursales (`B001, B002, B004`… y `B003`) → `Branch (3FN)` con `branchNo, branchAddress, telNo` → `Staff (3FN)` con `staffNo, name, position, salary, branchNo`. Fíjate en las etiquetas: *"se han convertido en Clave Primaria"* sobre `branchNo` en `Branch`, y *"se han convertido en Clave Foránea"* sobre `branchNo` en `Staff`.
>
> **Por qué importa:** la lámina teaches el **gesto exacto** de la 3FN: el atributo que era clave en la tabla nueva (`branchNo`) **se queda** en la tabla de origen, pero **deja de ser clave ahí** y pasa a ser **clave foránea**. Fíjate que en `Staff (3FN)` las columnas son `staffNo, name, position, salary, branchNo` — sin `branchAddress` ni `telNo`. Y esas dos columnas se fueron a `Branch (3FN)` con `branchNo` como PK.
>
> **Ejemplo:** el resultado final son **cuatro tablas** en el ejemplo del deck (`Staff`, `Branch`, `Course`, `Student`) donde antes había una sola tabla que repetía la dirección de cada sucursal en cada fila de empleado. Cambiar el teléfono de B001 ahora es **un `UPDATE` sobre una fila**, no dos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-023-p20.png]]
>
> **Se lee así:** la lámina (p. 20 de BD 02.3) da la **definición lógica formal**: *"ocurre cuando el valor de un atributo o varios determina el valor de un segundo atributo o varios"*, con la notación `A → B` (*A determina funcionalmente a B*), y avisa de los dos nombres: el de la izquierda es el **determinante**, el de la derecha el **dependiente**. La definición de transitiva: *"si Y depende funcionalmente de X y Z de Y, pero X no depende funcionalmente de Y, se dice que Z depende transitivamente de X"*.
>
> **Por qué importa:** esa frase es la más precisa del tema y conviene entenderla **en palabras**: `X → Y` y `Y → Z`, pero **no** `X → Z`. Es decir, hay una cadena de dos pasos y el dato final **no** depende directamente de la PK, sino de un intermediario. La condición "X no depende funcionalmente de Y" está ahí para que no se confunda con la **dependencia parcial**: ahí sí habría una relación directa entre la parte de la PK y el atributo.
>
> **Ejemplo:** `EMP_NUM → JOB_CLASS` y `JOB_CLASS → CHG_HOUR`, pero no `EMP_NUM → CHG_HOUR` directamente. Por eso `CHG_HOUR` depende **transitivamente** de `EMP_NUM` y tiene que irse a la tabla `JOB`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-023-p21.png]]
>
> **Se lee así:** la lámina (p. 21) es el **caso real de la cátedra**, y por eso la puse: es el mismo razonamiento con nombres reales. El deck dice: *"la única clave foránea es {Torneo, Año}. La violación de la 3FN ocurre porque el atributo no primario Fecha de nacimiento del ganador es dependiente transitivamente de {Torneo, Año} vía el atributo no primario Ganador"*. Y explica el daño concreto: *"no hay nada que impida a la misma persona ser mostrada con diferentes fechas de nacimiento en diversos registros"*.
>
> **Por qué importa:** ese último detalle es **el corazón de la normalización**: la 3FN no existe para que las tablas se vean "bonitas", sino para **impedir que un mismo hecho se guarde de dos formas distintas**. Si el ganador es `Juan Pérez`, su fecha de nacimiento es un dato de **Juan Pérez**, no del torneo. Guardarla en la tabla del torneo es lo que permite que un error de captura produzca dos fechas distintas para la misma persona.
>
> **Ejemplo:** la solución que propone el deck es **dividir la tabla en dos**: una con `{Torneo, Año, Ganador}` y otra con `{Ganador, Fecha de nacimiento}`. La FK `Ganador` conecta ambas. Y el mismo razonamiento se aplica, palabra por palabra, al ejemplo de `JOB_CLASS → CHG_HOUR` del bloque anterior.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-03-02-er.svg]]
>
> **Se lee así:** el diagrama es **el resultado final**: cuatro tablas. `PROJECT(PROJ_NUM PK, PROJ_NAME)`, `EMPLOYEE(EMP_NUM PK, EMP_NAME, JOB_CLASS FK)`, `JOB(JOB_CLASS PK, CHG_HOUR)` y `ASSIGNMENT(PROJ_NUM PK FK, EMP_NUM PK FK, ASSIGN_HOURS)`. Compara con el diagrama anterior: lo **único** que cambió es que `CHG_HOUR` salió de `EMPLOYEE` y se quedó en `JOB`, que nació como tabla nueva con `JOB_CLASS` como PK.
>
> **Por qué importa:** mira la etiqueta `FK` que quedó en `EMPLOYEE.JOB_CLASS`: es el rastro de la separación. En SQL eso es `FOREIGN KEY (JOB_CLASS) REFERENCES JOB(JOB_CLASS)`, y el `NOT NULL` opcional. `EMPLOYEE` ahora dice **qué cargo tiene** y `JOB` dice **cuánto paga ese cargo**. Ninguna de las dos tablas repite el dato de la otra.
>
> **Ejemplo:** el cambio se nota en una operación concreta. Si la empresa sube la tarifa de `Programador` de 20 a 25, antes había que hacer un `UPDATE` sobre todas las filas de `EMPLOYEE` con `JOB_CLASS = 'PROG'`. Ahora es **un solo `UPDATE` sobre una fila** de `JOB`. Además, si el cargo existe pero ningún empleado lo tiene, el cargo sigue registrado en `JOB` — que es justo el problema de anomalía de inserción resuelto.

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
>
> - ¿DF en 1 línea?::X→Y: conociendo X conozco Y.
> - ¿3 anomalías?::Inserción (dummy), eliminación (borra de más), actualización (a medias corrompe).
> - ¿2FN?::1FN sin dependencias parciales; PK simple ⇒ automática.
> - ¿3FN?::2FN sin dependencias transitivas (no-primo → no-primo).
> - ¿Caso PROJECT?::Parciales → PROJECT + EMPLOYEE; transitiva → JOB.
> - ¿Determinante se va o se queda?::Se queda como FK (copiar, no mudar).
> - ¿BCNF en 1 línea?::Todo determinante es clave candidata.
> - ¿Diferencia 2FN vs 3FN?::2FN quita parciales (parte de la PK); 3FN quita transitivas (no-primo → no-primo).

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[02 - Primera forma normal y diccionario de datos]] — el piso sobre el que se construyen 2FN y 3FN.
> - [[04 - Normalización paso a paso]] — el protocolo completo, paso a paso.
> - [[01 - Conversión MC a ML por cardinalidad]] — el esquema que se normaliza sale de aquí.
> - [[../Unidad 1 - Modelos de Datos y ER/Guía de Problemas 1 - MC, ML y Normalización|Guía de Problemas 1]] — ejercicios de normalización con DF reales.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización|Guía de Problemas 2]] — el hotel 1FN→3FN resuelto.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
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
