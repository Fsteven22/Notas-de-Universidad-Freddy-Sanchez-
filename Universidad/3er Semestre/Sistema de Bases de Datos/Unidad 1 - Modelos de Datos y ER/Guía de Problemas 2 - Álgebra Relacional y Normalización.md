---
dg-publish: true
tags: [TICG1018, unidad1, guia, taller2, bd]
---

# 📝 Guía de Problemas 2 — Álgebra Relacional y Normalización (Taller 2)

> [!info] ℹ️ Qué es esta guía
> Desarrollo completo del **Taller 2 (PAO 1 2026)**: 4 consultas de **álgebra relacional** (con la solución oficial del taller como base, explicada paso a paso) + la normalización **1FN→2FN→3FN** del hotel. Material puente entre la nota [[03 - Modelo relacional, ERM y casos Tiny College]] (operadores del álgebra) y [[03 - Segunda y tercera forma normal]] / [[04 - Normalización paso a paso]].
>
> | Bloque | Tema | Ejercicios | Alimenta |
> |---|---|---|---|
> | A | Álgebra relacional | 4 consultas | U1-03 (modelo relacional) |
| A·cat | Catálogo de operadores (diapositivas 3.1 / 3.2) | referencia | este bloque |
> | B | Normalización del hotel | 1FN, 2FN, 3FN | U2-03 y U2-04 |
>
> 📎 Esquema de referencia del taller (algebra): `RESERVA`, `PASAJERO`, `VUELO`, `AVION`, `AEROLINEA`, `AEROPUERTO`.

![[../Unidad 0 - Guias y Ejercicios/Talleres/Taller 2 PAO-2026-1  SOL.pdf]]

---

## 🅰️ Bloque A — Álgebra Relacional (4 consultas)

> [!tip] 📌 Cómo atacar cada consulta
> 1. Marca las tablas que participan y **sus claves** (si los nombres difieren, el `⨝` necesita condición explícita).
> 2. Encadena joins **antes** de filtrar (σ) y proyectar (π).
> 3. Reglas rápidas: `σ` = WHERE, `π` = SELECT de columnas, `γ` = GROUP BY con agregados, `-` = NOT IN / NOT EXISTS, `ρ` = alias para usos múltiples de la misma tabla.
> 4. Los operadores nuevos de clase (`X`, `⟕/⟖`, `⋉`, `τ`) están en el catálogo con el ejemplo PRODUCTO × VENTA justo debajo.

### 📚 Catálogo de operadores del álgebra (diapositivas 3.1 / 3.2)

Referencia rápida tomada de las diapositivas de clase (Unidad 3 — álgebra relacional). Vive junto a los 4 ejercicios porque varios operadores aparecen disfrazados en los enunciados.

| Operador | Símbolo | Qué hace | SQL mental |
|---|---|---|---|
| Selección | `σ` | Filtra **filas** que cumplen una condición | `WHERE` |
| Proyección | `π` | Elige **columnas** y elimina duplicadas | `SELECT` / `DISTINCT` |
| Producto cruz | `X` | Todas las combinaciones de filas (m × n = m·n filas) | `FROM a, b` sin `ON` |
| Join natural | `⨝` | `X` + σ por atributos **mismo nombre y valor** + π que borra la columna repetida | `JOIN ... ON` (claves con igual nombre) |
| Equi join | `⨝(a=b)` | Join con condición de **igualdad**; las columnas de la condición NO se eliminan | `JOIN ON` |
| Theta join | `⨝(F)` | Join con condición que no es igualdad (`≠`, `>`, `<`) | `JOIN ON` (comparación no-igualdad) |
| Left outer join | `⟕` | Trae TODAS las filas de la izquierda; las que no casan se rellenan con `null` | `LEFT JOIN` |
| Right outer join | `⟖` | Trae TODAS las filas de la derecha; `null` en el lado vacío | `RIGHT JOIN` |
| Semijoin | `⋉` | Filas de R que participan en el join con S — **solo atributos de R** | `WHERE ... IN / EXISTS` |
| Unión / Diferencia / Intersección | `∪ − ∩` | Operaciones entre conjuntos completos | `UNION / NOT IN / INTERSECT` |
| Agregación | `γ` | Agrupa y calcula (COUNT, SUM, AVG) | `GROUP BY (+ HAVING)` |
| Renombre | `ρ` | Alias de una tabla o expresión (misma tabla dos veces) | `AS` |
| Orden | `τ` | Ordena las filas asc / desc | `ORDER BY` |

**Ejemplo guía de la casa (PRODUCTO × VENTA, de las diapositivas):**

| CODIGO | DESCRIPCION | PRECIO |
|---|---|---|
| 101 | Pasta | 3.50 |
| 104 | Gel | 4.00 |
| 105 | Shampoo | 10.00 |

| ID_VENTA | FECHA | ID_PRODUCT | CANTIDAD |
|---|---|---|---|
| 1 | 02/02/2020 | 104 | 54 |
| 2 | 04/02/2020 | 101 | 2 |
| 4 | 04/04/2020 | 110 | -2 |

| Consulta | Resultado |
|---|---|
| `PRODUCTO X VENTA` | 9 filas (3 × 3): toda combinación; casi nunca lo quieres, es el punto de partida de los joins |
| `PRODUCTO ⨝ CODIGO=ID_PRODUCT VENTA` | 2 filas: 101↔venta 2, 104↔venta 1 |
| `PRODUCTO ⟕ VENTA` | las 2 anteriores **+** fila del Shampoo 105 con `null` en todo lo de VENTA |
| `PRODUCTO ⟖ VENTA` | las 2 anteriores **+** fila de la venta 4 (ID_PRODUCT=110) con `null` en todo lo de PRODUCTO |
| `VENTA ⋉ PRODUCTO` | ventas 1 y 2, solo columnas de VENTA (sus productos sí existen) |
| `τ precio desc (PRODUCTO)` | 105, 101, 104 — del más caro al más barato |

![[../Unidad 0 - Guias y Ejercicios/Diapositivas/3.1 Operaciones Básicas_2025.pdf]]

![[../Unidad 0 - Guias y Ejercicios/Diapositivas/3.2 Operaciones Derivadas-join-order2026.pdf]]

### ✏️ Ejercicio 1 — Pasajeros del vuelo 777 "boeing" de American Airlines

> [!example]- 📝 Enunciado y desarrollo
>
> **Enunciado:** listar los pasajeros (nombres, apellidos y `num_pasaporte`) del vuelo 777, modelo boeing, de la aerolínea "American Airlines".
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

### ✏️ Ejercicio 2 — Modelos con rango > 5000 km de aerolíneas con más de 50 aeronaves

> [!example]- 📝 Enunciado y desarrollo
>
> **Enunciado:** listar los modelos de aviones con rango mayor a 5000 km que pertenecen a aerolíneas con más de 50 aeronaves.
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

### ✏️ Ejercicio 3 — Aerolíneas que no vuelan hoy

> [!example]- 📝 Enunciado y desarrollo
>
> **Enunciado:** listar los nombres de las aerolíneas que no tienen vuelos para el día de hoy (`hora_salida`).
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

### ✏️ Ejercicio 4 — Vuelos de hoy que aterrizan en el mismo país, ciudad distinta

> [!example]- 📝 Enunciado y desarrollo
>
> **Enunciado:** listar los vuelos que salieron y llegaron hoy al mismo país pero a ciudades diferentes.
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

## 🅱️ Bloque B — Normalización del hotel (1FN → 2FN → 3FN)

> [!example]- 📝 Enunciado y desarrollo
>
> **Enunciado:** normalizar la tabla de reservas de hotel en 1FN, 2FN y 3FN:
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
> > El desarrollo completo está en [[03 - Segunda y tercera forma normal]] y el método en [[04 - Normalización paso a paso]] (misma marca 3 para este caso del taller ya trabajada en `Taller 2 SOL.pdf` — aquí queda la transcripción).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Modelo relacional y operadores: [[03 - Modelo relacional, ERM y casos Tiny College]]
> - Normalización completa: [[03 - Segunda y tercera forma normal]] · [[04 - Normalización paso a paso]]
> - Índice: [[00 - Índice Unidad 1]] · Mapa: [[Sistema de Bases de Datos]]
> - Guía anterior: [[Guía de Problemas 1 - MC, ML y Normalización]]

## 📚 Fuente

> [!quote] 📖 Fuente
> `Unidad 0 - Guias y Ejercicios/Talleres/Taller 2 PAO-2026-1  SOL.pdf` (solución oficial del taller; la transcripción y las explicaciones SQL son propias). Otro recurso citado: el ejercicio de normalización ya se desarrolló en [[Guía de Problemas 1 - MC, ML y Normalización]].
> Diapositivas de clase embebidas en el catálogo: `Unidad 0 - Guias y Ejercicios/Diapositivas/3.1 Operaciones Básicas_2025.pdf` y `Unidad 0 - Guias y Ejercicios/Diapositivas/3.2 Operaciones Derivadas-join-order2026.pdf`.

---

**Tags:** #TICG1018 #unidad1 #guia #taller2 #bd
