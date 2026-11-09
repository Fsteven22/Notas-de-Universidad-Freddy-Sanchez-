---
dg-publish: true
tags: [TICG1018, unidad3, guia, taller2, algebra-relacional, normalizacion, bd]
---

# 📝 Guía de Problemas 2 — Álgebra Relacional y Normalización (Taller 2)

## 🎯 Introducción

> [!info] ℹ️ Qué es esta guía
>
> Desarrollo completo del **Taller 2 (PAO 1 2026)**: 4 consultas de **álgebra relacional** (con la solución oficial del taller como base, explicada paso a paso) + la normalización **1FN→2FN→3FN** del hotel. Material puente entre la nota [[../Unidad 1 - Modelos de Datos y ER/03 - Modelo relacional, ERM y casos Tiny College]] (operadores del álgebra) y [[../Unidad 2 - Modelo lógico y conversión/03 - Segunda y tercera forma normal]] / [[../Unidad 2 - Modelo lógico y conversión/04 - Normalización paso a paso]].
>
> | Bloque | Tema | Ejercicios | Alimenta |
> |---|---|---|---|
> | A | Álgebra relacional | 4 consultas | U1-03 (modelo relacional) |
> | A·cat | Catálogo de operadores (diapositivas 3.1 / 3.2) | referencia | este bloque |
> | B | Normalización del hotel | 1FN, 2FN, 3FN | U2-03 y U2-04 |
>
> 📎 Esquema de referencia del taller (algebra): `RESERVA`, `PASAJERO`, `VUELO`, `AVION`, `AEROLINEA`, `AEROPUERTO`.
>
> **Se lee así:** el bloque A enseña a *escribir* la consulta en álgebra y el bloque B a *romper* una tabla mal diseñada. Los dos usan la misma lógica: primero decides qué filas y qué columnas quieres (σ, π), después decides de dónde vienen (⨝, γ, ρ).

> [!info] 📖 El enunciado y la solución oficial del taller (Taller 2, pp. 1-3)
> Los PDFs del taller son material de clase y no se embeben: cada página se cita con su captura.
>
> **Taller 2 — álgebra relacional, enunciado y primera solución (`Taller 2 PAO-2026-1  SOL.pdf`, p. 1):**
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Talleres/bd-taller2-p1.png]]
>
> **Las consultas 2, 3 y 4 + el enunciado de normalización (p. 2):**
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Talleres/bd-taller2-p2.png]]
>
> **La tabla de reservas a normalizar (p. 3):**
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Talleres/bd-taller2-p3.png]]
>
> **Se lee así:** esta es la **solución comentada** del taller, y está escrita como una cadena de tres pasos que se leen de arriba abajo. Primero la **1FN**: la columna `Habitaciones` guarda algo como `"101:Doble, 102:Doble"` — un valor compuesto y repetido — así que se rompe en filas sueltas (`NumHabitacion`, `TipoHabitacion`) y, como `ReservaID` se repite en esas filas nuevas, la PK pasa a ser **compuesta** `(ReservaID, NumHabitacion)`. Luego la **2FN**: `TipoHabitacion` depende solo de `NumHabitacion`, y los datos de la reserva dependen solo de `ReservaID`, así que salen dos tablas (`Habitacion` y `Reserva_Detalle`) y queda la `Reserva`. Y por último la **3FN**: en la `Reserva` que quedó, `ClienteNombre` depende de `ClienteID`, y `ClienteID` depende de `ReservaID` — una transitiva clásica —, así que el cliente se extrae a su propia tabla.
>
> **Por qué importa:** es el mismo protocolo de la nota 04 aplicado a un caso real de la carrera, y por eso sirve como plantilla: **la 1FN siempre va primero** (si no partes los valores repetidos, las DFs que veas después son falsas), **la PK se vuelve compuesta en cuanto rompes un grupo**, y **cada atributo que "sobra" en una tabla se va con su determinante**. Al final quedan cuatro tablas y ninguna repite datos.
>
> **Ejemplo:** el error clásico aquí es quedarse en la 1FN y entregar la tabla con `Habitaciones` como texto. El enunciado pide el *esquema final en 3FN*, así que la respuesta incompleta no es "tabla con menos campos", sino **más tablas**: `Cliente`, `Habitacion`, `Reserva` y `Reserva_Habitacion`.

---

## 📝 Ejercicios Propuestos
#### 🅰️ Bloque A — Álgebra Relacional (4 consultas)

> [!tip] 📌 Cómo atacar cada consulta
>
> 1. Marca las tablas que participan y **sus claves** (si los nombres difieren, el `⨝` necesita condición explícita).
> 2. Encadena joins **antes** de filtrar (σ) y proyectar (π).
> 3. Reglas rápidas: `σ` = WHERE, `π` = SELECT de columnas, `γ` = GROUP BY con agregados, `-` = NOT IN / NOT EXISTS, `ρ` = alias para usos múltiples de la misma tabla.
> 4. Los operadores nuevos de clase (`X`, `⟕/⟖`, `⋉`, `τ`) están en el catálogo con el ejemplo PRODUCTO × VENTA justo debajo.

#### 📚 Catálogo de operadores del álgebra (diapositivas 3.1 / 3.2)

> [!info] 🔗 Catálogo de operadores del álgebra (diapositivas 3.1 / 3.2)
>
> Referencia rápida tomada de las diapositivas de clase (Unidad 3 — álgebra relacional). Vive junto a los 4 ejercicios porque varios operadores aparecen disfrazados en los enunciados.

> [!note] 📚 Catálogo de operadores del álgebra
>
> | Operador | Símbolo | Qué hace | SQL mental |
> |---|---|---|---|
> | Selección | `σ` | Filtra **filas** que cumplen una condición | `WHERE` |
> | Proyección | `π` | Elige **columnas** y elimina duplicadas | `SELECT` / `DISTINCT` |
> | Producto cruz | `X` | Todas las combinaciones de filas (m × n = m·n filas) | `FROM a, b` sin `ON` |
> | Join natural | `⨝` | `X` + σ por atributos **mismo nombre y valor** + π que borra la columna repetida | `JOIN ... ON` (claves con igual nombre) |
> | Equi join | `⨝(a=b)` | Join con condición de **igualdad**; las columnas de la condición NO se eliminan | `JOIN ON` |
> | Theta join | `⨝(F)` | Join con condición que no es igualdad (`≠`, `>`, `<`) | `JOIN ON` (comparación no-igualdad) |
> | Left outer join | `⟕` | Trae TODAS las filas de la izquierda; las que no casan se rellenan con `null` | `LEFT JOIN` |
> | Right outer join | `⟖` | Trae TODAS las filas de la derecha; `null` en el lado vacío | `RIGHT JOIN` |
> | Semijoin | `⋉` | Filas de R que participan en el join con S — **solo atributos de R** | `WHERE ... IN / EXISTS` |
> | Unión / Diferencia / Intersección | `∪ − ∩` | Operaciones entre conjuntos completos | `UNION / NOT IN / INTERSECT` |
> | Agregación | `γ` | Agrupa y calcula (COUNT, SUM, AVG) | `GROUP BY (+ HAVING)` |
> | Renombre | `ρ` | Alias de una tabla o expresión (misma tabla dos veces) | `AS` |
> | Orden | `τ` | Ordena las filas asc / desc | `ORDER BY` |

> [!example] 🧪 Ejemplo guía de la casa (PRODUCTO × VENTA, de las diapositivas)
>
> | CODIGO | DESCRIPCION | PRECIO |
> |---|---|---|
> | 101 | Pasta | 3.50 |
> | 104 | Gel | 4.00 |
> | 105 | Shampoo | 10.00 |
>
> | ID_VENTA | FECHA | ID_PRODUCT | CANTIDAD |
> |---|---|---|---|
> | 1 | 02/02/2020 | 104 | 54 |
> | 2 | 04/02/2020 | 101 | 2 |
> | 4 | 04/04/2020 | 110 | -2 |
>
> | Consulta | Resultado |
> |---|---|
> | `PRODUCTO X VENTA` | 9 filas (3 × 3): toda combinación; casi nunca lo quieres, es el punto de partida de los joins |
> | `PRODUCTO ⨝ CODIGO=ID_PRODUCT VENTA` | 2 filas: 101↔venta 2, 104↔venta 1 |
> | `PRODUCTO ⟕ VENTA` | las 2 anteriores **+** fila del Shampoo 105 con `null` en todo lo de VENTA |
> | `PRODUCTO ⟖ VENTA` | las 2 anteriores **+** fila de la venta 4 (ID_PRODUCT=110) con `null` en todo lo de PRODUCTO |
> | `VENTA ⋉ PRODUCTO` | ventas 1 y 2, solo columnas de VENTA (sus productos sí existen) |
> | `τ precio desc (PRODUCTO)` | 105, 101, 104 — del más caro al más barato |

> [!info] 📖 El deck de cátedra: cada operador con su figura (slides05, pp. 4-27)
>
> El deck del Ing. Magallanes recorre el álgebra relacional operador por operador, con ejemplos numéricos. Estas son las figuras que corresponden al catálogo de arriba.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p5.png]]
>
> **Se lee así:** la lámina (p. 5) es la **selección con dos condiciones encadenadas**, y por eso es la que explica cómo se combinan. La tabla `Product` tiene seis filas (`maker, model, type`): cuatro `pc` (1001-1003) y dos `laptop` (2004, 2005)… y la condición es `σ type='laptop' ∧ model≥2005 (Product)`. Debajo, el resultado `R` con solo las filas que cumplen **las dos** condiciones a la vez: `A · 2005 · laptop` y `A · 2006 · laptop`. Abajo del todo, la **forma general**: `R2 = σ <condición> (R1)`, con la nota *"operar sobre la nueva relación"*.
>
> **Por qué importa:** el `∧` es lo que cambia respecto a la selección simple: con `type='laptop'` solo, saldrían también los modelos 2004 y 2006… es decir, `model≥2005` **filtra dentro** del resultado anterior. Y la forma general de abajo es la que se repite en todo el tema: **cada operador recibe una relación y devuelve otra relación**, así que se pueden encadenar sin problemas.
>
> **Ejemplo:** el `A` en la primera columna es el *maker* (el fabricante), no una letra de la condición. La condición completa se lee: de todos los productos, quédate con los que son *laptop* **y** además son del modelo 2005 en adelante. La conjunción se evalúa primero y el resultado se puede ir acotando paso a paso.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p7.png]]
>
> **Se lee así:** la lámina (p. 7) es **la composición de operaciones** — dos operadores encadenados: `π maker, type (σ type='laptop' ∧ model≥2005 (Product))`. Y lo interesante es que la lámina dibuja un **diagrama de ejecución con los pasos numerados en orden inverso**: `3 → 2 → 1`. El resultado final tiene solo dos columnas (`maker`, `type`) con tres filas: `A · laptop`, `F · laptop`, `G · laptop`.
>
> **Por qué importa:** ese diagrama de ejecución es la explicación visual de por qué **se proyecta después de filtrar**. El paso 1 (abajo) es la selección, el 2 es la proyección y el 3 es el resultado; pero el motor **los ejecuta al revés**, de adentro hacia afuera: primero filtra (1), luego proyecta (2), y por último entrega (3). El orden de escritura va de afuera hacia adentro; el de ejecución, de adentro hacia afuera.
>
> **Ejemplo:** los makers `A`, `F` y `G` que salen son los que tienen **algún** laptop del modelo 2005 en adelante. Fíjate en que `F` y `G` no estaban en el `Product` de la lámina anterior: son filas que la selección anterior no mostraba porque esa lámina usaba otros datos. La idea no cambia: el resultado tiene **menos columnas** y **solo las filas que cumplen la condición**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p9.png]]
>
> **Se lee así:** la lámina (p. 9) es el **producto cartesiano con el esquema del resultado**, y es la lámina que mejor explica por qué el `×` casi nunca se quiere. `Department` tiene 3 filas (Biology, Comp. Sci., History) y `Course` tiene 4 (BIO-301, BIO-399, CS-101, CS-190) → **12 filas**. La lámina dibuja además el esquema del resultado: `R(department.dept_name, department.building, department.budget, course.course_id, course.title, course.dept_name, course.credits)` — y avisa: *"en caso de que R1 y R2 tengan columnas con el mismo nombre, el resultado tendrá estas 2 columnas"*.
>
> **Por qué importa:** fíjate en el esquema: aparecen **`department.dept_name` y `course.dept_name`**, las dos. Es el detalle técnico que distingue el producto cartesiano del natural join: el producto **conserva las dos columnas** aunque se llamen igual, y para poder distinguirlas el motor las califica con el nombre de la tabla. Ese es el motivo por el que el `×` se llama también "producto cruzado con esquema-qualified".
>
> **Ejemplo:** de las 12 filas, solo 4 tienen sentido: cada curso con **su** departamento. Las otras 8 emparejan un curso de Biology con el edificio de Comp. Sci. y así sucesivamente. De ahí la necesidad del join.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p15.png]]
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p16.png]]
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p18.png]]
>
> **Se lee así (los joins, pp. 15-18):** estas tres láminas son el bloque de joins del deck, y se leen como una progresión. La **p. 15** es el natural join (`department ⨝ course`): el resultado tiene `dept_name` **una sola vez** y las filas que no casan desaparecen. La **p. 16** es el *left outer join* (`R ⟕ S`): las filas de `R` que no encuentran pareja se quedan con `-` en las columnas de `S`. Y la **p. 18** es el *theta join* (`R ⨝c S`): un join con **cualquier condición de comparación**, y con el aviso de que si la condición solo tiene igualdades, es un *equi-join*.
>
> **Por qué importa:** la diferencia entre las tres se ve en **qué filas sobreviven**. En el natural join sobreviven las que casan por las dos partes; en el left outer sobreviven **todas** las de la izquierda; en el theta join lo decide la condición `C`, que puede ser cualquier cosa. Si solo te sabe una de las tres, es casi seguro que la vas a confundir con otra.
>
> **Ejemplo:** en la p. 16, el curso `CS-190 Game Design` aparece con `dept_name = -` porque no tiene departamento asignado, y el departamento `History` aparece con todos los campos de `course` en `-` porque no tiene cursos. En la p. 15, en cambio, History **desaparece**: es un join interno.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p20.png]]
>
> **Se lee así (la división, p. 20):** la lámina es el ejemplo numérico de la división, con `A(sno, pno)` y los divisores `B1`, `B2` y `B3`. La regla que rotula la lámina es: *"el resultado de la división contiene todos los valores de las columnas no comunes, que están asociadas con todas las filas del divisor"*. Los resultados son `A ÷ B1 = {s1, s2, s3, s4}`, `A ÷ B2 = {s1, s4}` y `A ÷ B3 = {s1}`.
>
> **Por qué importa:** la palabra clave de la lámina es **"todas"**. La división no es un join: un join te da las filas que casan *con alguna* fila de la otra relación; la división te da las que casan *con todas*. Y el caso `B3` muestra la versión fuerte: el divisor puede pedir el mismo valor **dos veces**, y entonces la fila de `A` tiene que dos veces también.
>
> **Ejemplo:** `A ÷ B2 = {s1, s4}` quiere decir que `s1` y `s4` son los únicos que aparecen **con todos** los `pno` que pide `B2`. `s2` aparece con `p1` y `p2` pero le falta `p4`, así que no sale. Esa es exactamente la lógica de "ítems ordenados por todos los clientes".
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p24.png]]
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p26.png]]
>
> **Se lee así (las agregaciones, pp. 24 y 26):** la **p. 24** explica la agregación sin agrupar: `G sum(rating) (R)` sobre la relación `Marinero` (`mid, mnombre, rating, edad`) da `135`; `G max(rating) (R)` da `10`; `G min(edad) (R)` da `35`; `G avg(rating) (R)` da `8.3`; `G count(rating) (R)` da `3`. Y explica la notación: *"Gamma significa que se debe aplicar una función agregación, y el subíndice indica la operación de agregación a aplicar"*. La **p. 26** añade el **agrupamiento**: `nombre-sucursal G sum(sueldo) (R)` da `Centro · 5300`, `Leganés · 3100`, `Navacerrada · 8100`.
>
> **Por qué importa:** las dos láminas juntas explican por qué el `G` (o `γ`) del álgebra **no se parece** al `GROUP BY` de SQL: en álgebra el agrupamiento va **dentro del operador** (`γ columna-de-agrupamiento; función → atributo`), mientras que en SQL es una cláusula aparte (`GROUP BY columna`). No es que sean distintos: es que el álgebra mete en una sola caja lo que SQL separa en dos.
>
> **Ejemplo:** `G sum(rating) (R)` sin columna de agrupamiento es el agregado global: una sola fila con la suma de todos los ratings. `nombre-sucursal G sum(sueldo) (R)` es el agregado por grupo: una fila por cada valor distinto de `nombre-sucursal`. El primero responde *"¿cuánto es el total?"*; el segundo, *"¿cuánto es el total de cada sucursal?"*.

#### ✏️ Ejercicio 1 — Pasajeros del vuelo 777 "boeing" de American Airlines
> [!example]- 📝 Enunciado y desarrollo
>
>
> > **Enunciado:** listar los pasajeros (nombres, apellidos y `num_pasaporte`) del vuelo 777, modelo boeing, de la aerolínea "American Airlines".
>
> > [!success]- ✅ Solución (oficial del taller, explicada)
> >
> > La cadena parte de `RESERVA` — la tabla que conecta al pasajero — y se abre paso hasta `AEROLINEA` cruzada por `AVION`:
> >
> > ```text
> > -- 1. Unimos RESERVA con PASAJERO indicando las claves diferentes
> > Paso1 = RESERVA ⨝(pasajero = pasajero_id) PASAJERO
> >
> > -- 2. Unimos con VUELO
> > Paso2 = Paso1 ⨝ VUELO
> >
> > -- 3. Unimos con AVION indicando sus claves distintas
> > Paso3 = Paso2 ⨝(avion = avion_id) AVION
> >
> > -- 4. Unimos con AEROLINEA (aerolinea_id se llama igual)
> > Paso4 = Paso3 ⨝ AEROLINEA
> >
> > -- 5. Filtramos (σ) y proyectamos (π) al final
> > π nombres, apellidos, num_pasaporte (
> >   σ vuelo_id=777 ∧ modelo='boeing' ∧ nombre='American Airlines' (Paso4)
> > )
> > ```
> >
> > **Por qué funciona así:**
> > - Cuando las columnas de las claves **no se llaman igual** (`pasajero` en RESERVA vs `pasajero_id` en PASAJERO), el join exige condición: `⨝(izq = der)`. Si se llaman igual (Paso 2 y 4), basta `⨝` natural.
> > - El `σ` y el `π` van al **final**: primero llega la "mesa completa" (el join con todos los atributos) y al cierre se recorta qué filas (σ) y qué columnas (π).
> > - El filtro de texto usa el valor exacto guardado en la tabla (`'American Airlines'`), no como viene escrito en el enunciado.
> >
> > **SQL equivalente (mental):**
> >
> > ```sql
> > SELECT p.nombres, p.apellidos, p.num_pasaporte
> > FROM reserva r
> >   JOIN pasajero p ON r.pasajero = p.pasajero_id
> >   JOIN vuelo v    ON r.vuelo = v.vuelo_id
> >   JOIN avion a    ON v.avion = a.avion_id
> >   JOIN aerolinea al ON a.aerolinea_id = al.aerolinea_id
> > WHERE v.vuelo_id = 777 AND a.modelo = 'boeing'
> >   AND al.nombre = 'American Airlines';
> > ```
#### ✏️ Ejercicio 2 — Modelos con rango > 5000 km de aerolíneas con más de 50 aeronaves
> [!example]- 📝 Enunciado y desarrollo
>
>
> > **Enunciado:** listar los modelos de aviones con rango mayor a 5000 km que pertenecen a aerolíneas con más de 50 aeronaves.
>
> > [!success]- ✅ Solución (oficial del taller, explicada)
> >
> > ```text
> > Π modelo(
> >   σ rango>5000(AVION)
> >   ⨝ Π aereolinea_id(
> >       σ total_aviones>50(
> >         γ aereolinea_id; COUNT(avion_id) → total_aviones
> >         (AVION))))
> > ```
> >
> > **Lectura desde adentro hacia afuera:**
> > 1. `γ aereolinea_id; COUNT(avion_id) → total_aviones` agrupa los aviones por aerolínea y cuenta cuántos tiene cada una — es el GROUP BY con HAVING de SQL.
> > 2. `σ total_aviones>50` se queda con las aerolíneas con más de 50 aviones (aquí vive el HAVING).
> > 3. `π aereolinea_id`  deja solo la clave para que el join con la parte filtrada pueda cerrar.
> > 4. `σ rango>5000(AVION)` filtra los aviones con rango mayor a 5000 km y los une con esas aerolíneas.
> > 5. `π modelo` entrega la respuesta final.
> >
> > **SQL equivalente (mental):**
> >
> > ```sql
> > SELECT DISTINCT a.modelo
> > FROM avion a
> > WHERE a.rango > 5000
> >   AND a.aerolinea_id IN (
> >     SELECT av.aerolinea_id FROM avion av
> >     GROUP BY av.aerolinea_id
> >     HAVING COUNT(av.avion_id) > 50);
> > ```
#### ✏️ Ejercicio 3 — Aerolíneas que no vuelan hoy
> [!example]- 📝 Enunciado y desarrollo
>
>
> > **Enunciado:** listar los nombres de las aerolíneas que no tienen vuelos para el día de hoy (`hora_salida`).
>
> > [!success]- ✅ Solución (oficial del taller, explicada)
> >
> > ```text
> > Π nombre(AEROLINEA)
> > - Π nombre(AEROLINEA ⨝ σ hora_salida=HOY(VUELO))
> > ```
> >
> > **Por qué es una diferencia (`-`) y no un filtro:**
> > - Queremos las aerolíneas **ausentes** en el conjunto de vuelos de hoy — la negación no se expresa con `σ` (que solo compara atributos) sino con **diferencia de conjuntos**.
> > - El operando izquierdo trae TODAS las aerolíneas; el derecho, las que tienen un vuelo con `hora_salida = HOY` (join con VUELO y filtro).
> > - En SQL mental: `NOT EXISTS` o `NOT IN` sobre la subconsulta de vuelos de hoy.
#### ✏️ Ejercicio 4 — Vuelos de hoy que aterrizan en el mismo país, ciudad distinta
> [!example]- 📝 Enunciado y desarrollo
>
>
> > **Enunciado:** listar los vuelos que salieron y llegaron hoy al mismo país pero a ciudades diferentes.
>
> > [!success]- ✅ Solución (oficial del taller, explicada)
> >
> > ```text
> > Π vuelo_id(
> >   σ S.pais=L.pais ∧ S.ciudad≠L.ciudad(
> >     (σ hora_salida=HOY ∧ hora_llegada=HOY(VUELO))
> >     ⨝ aerop_id_salida = S.airport_id  ρ S(AEROPUERTO)
> >     ⨝ aerop_id_llegada = L.airport_id ρ L(AEROPUERTO)))
> > ```
> >
> > **Los dos trucos que el ejercicio enseña:**
> > 1. `ρ` (renombrar): se usa la MISMA tabla `AEROPUERTO` dos veces — una como aeropuerto de salida (alias `S`) y otra como de llegada (alias `L`). Sin `ρ`, el motor no distingue qué lado comparar.
> > 2. La condición del `σ` compara **entre columnas de las dos copias**: `S.pais = L.pais` (mismo país) `∧ S.ciudad ≠ L.ciudad` (ciudad distinta). Es un join de la tabla consigo misma + un filtro cruzado — exactamente lo que en SQL sería un `self-join`.
> > - El filtro temporal (`hora_salida=HOY ∧ hora_llegada=HOY`) va ANTES de los joins: menos filas arrastradas.
---
#### 🅱️ Bloque B — Normalización del hotel (1FN → 2FN → 3FN)
> [!example]- 📝 Enunciado y desarrollo
>
>
> > **Enunciado:** normalizar la tabla de reservas de hotel en 1FN, 2FN y 3FN:
>
> | ReservaID | FechaEntrada | FechaSalida | ClienteID | ClienteNombre | Habitaciones (Num:Tipo) | PrecioTotal |
> |---|---|---|---|---|---|---|
> | R001 | 1/6/25 | 5/6/25 | C001 | María García | 101:Doble, 102:Doble | 400 |
> | R002 | 3/6/25 | 4/6/25 | C002 | Pedro Herrera | 201:Suite | 300 |
> | R003 | 4/6/25 | 6/6/25 | C001 | María García | 103:Individual, 104:Doble | 350 |
>
> > [!success]- ✅ 1FN — atomicidad
> >
> > **Diagnóstico:** la columna `Habitaciones (Num:Tipo)` guarda **valores múltiples** en una celda ("101:Doble, 102:Doble") — no cumple atomicidad (1FN).
> > **Cura (dictada por la solución oficial):** separar cada habitación en su propia fila y dividir el campo en dos columnas (`NumHabitacion`, `TipoHabitacion`). Como `ReservaID` se repite en las filas divididas, la PK pasa a ser **compuesta** `(ReservaID, NumHabitacion)`.
> >
> > **Tabla 1FN:** `ReservaID, FechaEntrada, FechaSalida, ClienteID, ClienteNombre, NumHabitacion, TipoHabitacion, PrecioTotal`.
> [!success]- ✅ 2FN — dependencias parciales en la.pk compuesta
> >
> > **Diagnóstico:** en la 1FN, con PK compuesta:
> > - `TipoHabitacion` depende **solo** de `NumHabitacion` (la habitación es una vez tipo Suite, siempre Suite) → **dependencia parcial** viola 2FN.
> > - `FechaEntrada`, `FechaSalida`, `ClienteID`, `ClienteNombre`, `PrecioTotal` dependen de `ReservaID` (TODO de la PK).
> > **Cura:** separar la `Habitacion` en tabla y crear la tabla-relación `Reserva_Habitacion` que las conecta:
> >
> > ```text
> > Habitacion:        NumHabitacion (PK), TipoHabitacion
> > Reserva_Habitacion: ReservaID (PK/FK), NumHabitacion (PK/FK)
> > Reserva:            ReservaID (PK), FechaEntrada, FechaSalida, ClienteID, ClienteNombre, PrecioTotal
> > ```
> [!success]- ✅ 3FN — dependencias transitivas
> >
> > **Diagnóstico:** en la tabla `Reserva` de la 2FN, `ClienteNombre` depende de `ClienteID`, que a su vez depende de la PK `ReservaID` → **dependencia transitiva** viola 3FN.
> > **Cura:** extraer la entidad `Cliente`:
> >
> > ```text
> > Cliente:            ClienteID (PK), ClienteNombre
> > Habitacion:         NumHabitacion (PK), TipoHabitacion
> > Reserva:            ReservaID (PK), FechaEntrada, FechaSalida, ClienteID (FK), PrecioTotal
> > Reserva_Habitacion: ReservaID (PK/FK), NumHabitacion (PK/FK)
> > ```
> >
> > El desarrollo completo está en [[../Unidad 2 - Modelo lógico y conversión/03 - Segunda y tercera forma normal]] y el método en [[../Unidad 2 - Modelo lógico y conversión/04 - Normalización paso a paso]] (misma marca 3 para este caso del taller ya trabajada en `Taller 2 SOL.pdf` — aquí queda la transcripción).
---

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - `Unidad 0 - Guias y Ejercicios/Talleres/Taller 2 PAO-2026-1  SOL.pdf` — solución oficial del taller (3 páginas; citada por captura arriba).
> - Diapositivas `3.1 Operaciones Básicas_2025.pdf` y `3.2 Operaciones Derivadas-join-order2026.pdf` (Unidad 0 — Diapositivas) — el catálogo de operadores; sus figuras se citan como capturas de `slides05`.
> - Diapositivas `2026_1PAO_slides5_1_TICG1018.pdf` — álgebra relacional, pp. 4-27 (operadores básicos, joins y agregaciones).
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 8 — álgebra relacional y sus equivalentes en SQL.
> - La transcripción, las explicaciones SQL y los diagramas son propios.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[../Unidad 1 - Modelos de Datos y ER/03 - Modelo relacional, ERM y casos Tiny College|03 - Modelo relacional, ERM y casos Tiny College]] — el modelo relacional donde viven σ, π, ⨝, γ y ρ.
> - [[../Unidad 3 - Álgebra Relacional/01 - Operadores Básicos|01 - Operadores Básicos]] — σ, π, ×, ∪, −, ∩.
> - [[../Unidad 3 - Álgebra Relacional/02 - Operadores Derivados y Joins|02 - Operadores Derivados y Joins]] — joins, outer joins, semijoin y división.
> - [[../Unidad 3 - Álgebra Relacional/03 - Renombre y Agregación|03 - Renombre y Agregación]] — ρ y γ.
> - [[../Unidad 2 - Modelo lógico y conversión/03 - Segunda y tercera forma normal|03 - Segunda y tercera forma normal]] — el bloque B en detalle.
> - [[../Unidad 2 - Modelo lógico y conversión/04 - Normalización paso a paso|04 - Normalización paso a paso]] — el método paso a paso.
> - [[Guía de Problemas 1 - MC, ML y Normalización|Guía de Problemas 1]] — la guía anterior (modelado y normalización).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir Studying
>
> - Modelo relacional y operadores: [[../Unidad 1 - Modelos de Datos y ER/03 - Modelo relacional, ERM y casos Tiny College]]
> - Normalización completa: [[../Unidad 2 - Modelo lógico y conversión/03 - Segunda y tercera forma normal]] · [[../Unidad 2 - Modelo lógico y conversión/04 - Normalización paso a paso]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]] · Mapa: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Guía anterior: [[Guía de Problemas 1 - MC, ML y Normalización]]

---

**Tags:** #TICG1018 #unidad3 #guia #taller2 #algebra-relacional #normalizacion #bd
