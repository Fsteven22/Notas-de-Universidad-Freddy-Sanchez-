---
dg-publish: true
tags: [TICG1018, unidad3, algebra-relacional, renombre, agregacion, orden, bd]
---

# ⚙️ Álgebra Relacional — Renombre y Agregación

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Renombre y Agregación?
>
> Los operadores básicos y derivados nos permiten filtrar, proyectar y combinar tablas. Pero hay dos operaciones que faltan: **darle alias a una tabla** (para usarla dos veces en la misma consulta, como un self-join) y **agrupar y calcular** (como GROUP BY en SQL). Eso resuelven ρ (renombre) y γ (agregación).
>
> **Aplicaciones:**
> - **Self-join:** usar la misma tabla dos veces con nombres distintos.
> - **Consultas agregadas:** promedios, conteos, sumas por grupo.
> - **Ordenamiento:** ordenar resultados ascendente/descendente.
> - **Lección 1 (13-oct):** ρ para alias, γ para agregación, τ para orden.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-03-04-graph.svg]]
>
> **Se lee así:** los tres operadores de esta nota son **equivalencias**, no traducciones literales. ρ es un `AS`, γ es un `GROUP BY` con función de agregación, y τ es un `ORDER BY`. Cuando aprendes álgebra relacional aprendes tres formas de decir lo mismo que SQL ya dice — y por eso el examen pregunta *"¿qué equivalente en SQL tiene esta expresión?"*.

---

## 📋 Definiciones Formales

### 1️⃣ Renombre ρ

> [!note] 📋 Definición — Renombre ρ
>
> El renombre le da un **alias** a una relación o a una expresión. Es esencial cuando necesitas usar la misma tabla dos veces en una consulta (self-join) o cuando quieres simplificar nombres largos.
>
> **Sintaxis:** `ρ alias(expresión)` o `ρ nuevo_nombre(relación)`
>
> **SQL mental:** `AS`
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-03-01-graph.svg]]
>
> **Se lee así:** ρ **duplica** la relación con un nombre nuevo — no la modifica. Por eso `ρ S(AEROPUERTO)` y `ρ L(AEROPUERTO)` son dos copias distintas del mismo conjunto de filas, y el self-join es posible: sin ρ, la tabla no podría aparecer dos veces en la misma expresión con atributos distinguibles.

> [!example] 🧪 Ejemplo de renombre (self-join)
>
> Para comparar un aeropuerto de salida con uno de llegada (misma tabla `AEROPUERTO` dos veces):
>
> `ρ S(AEROPUERTO) ⨝ ρ L(AEROPUERTO)`
>
> Ahora `S` y `L` son dos copias distintas de la misma tabla, y puedes comparar `S.pais = L.pais ∧ S.ciudad ≠ L.ciudad`.

> [!info] 📖 El deck de cátedra: el renombramiento (slides05, p. 27)
> La última lámina del deck define el operador ρ con la misma fórmula que esta nota.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p27.png]]
> 
> **Renombramiento (p. 27):** *"permite renombrar atributos y relaciones. Asigna el nombre S a la relación resultante de la expresión E, y los nombres a1, a2, ... , ak a sus atributos"* — el `S` del deck es exactamente el `S` del self-join de arriba.

### 2️⃣ Agregación γ

> [!note] 📋 Definición — Agregación γ
>
> La agrupación **agrupa filas y calcula funciones** sobre cada grupo. Es el equivalente de `GROUP BY` con funciones de agregado en SQL.
>
> **Sintaxis:** `γ columnas_de_agrupación; función1 → atributo1, función2 → atributo2 (relación)`
>
> **Funciones:** COUNT, SUM, AVG, MIN, MAX.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-03-02-graph.svg]]
>
> **Se lee así:** γ tiene dos mitades: **dónde agrupas** (la columna o columnas de agrupamiento) y **qué calculas** (las funciones). Sin columna de agrupamiento, γ opera sobre toda la relación como un único grupo — el agregado global.

> [!example] 🧪 Ejemplo de agregación
>
> | Marinero |
> |---|
> | mid | mnombre | rating | edad |
> | 22 | dustin | 7 | 45.0 |
> | 31 | lubber | 8 | 55.5 |
> | 58 | rusty | 10 | 35.0 |
>
> `γ mid; COUNT(*) → n_reservas (RESERVA)` agrupa reservas por marinero y cuenta cuántas tiene cada uno.
>
> `γ avg(edad) (σ rating=10 (Marinero))` calcula la edad promedio de marineros con rating 10.

> [!info] 📖 El deck de cátedra: las agregaciones (slides05, pp. 23-26)
> El deck del Ing. Magallanes dedica cuatro láminas a la operación gamma: qué es, qué funciones tiene, cómo se pregunta y cómo se agrupa.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p23.png]]
> 
> **Agregaciones (p. 23):** la lámina introduce la **Operación Gamma (γ)** — la que agrupa y aplica una función de agregación sobre el grupo.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p24.png]]
> 
> **Funciones de agregación (p. 24):** *"la función de agregación suma, toma la columna ratings de la relación R y suma la colección de valores: G sum(rating) (R)"* — y la regla general: **γ** significa aplicar una función de agregación a un grupo de tuplas.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p25.png]]
> 
> **Ejemplos de preguntas (p. 25):** *"¿Cuántos marineros hay?: G count(mid) (Marinero)"*, *"la edad promedio de los marineros con rating 10: G avg(edad) (σ rating=10 (Marinero))"* — el deck combina agregación con selección en una sola línea.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s05-p26.png]]
> 
> **Agrupamiento (p. 26):** *"la función de agregación se puede aplicar por grupos de datos, de acuerdo a la columna o columnas especificadas"* — es la γ con más de una columna de agrupamiento.

### 3️⃣ Orden τ

> [!note] 📋 Definición — Orden τ
>
> El operador de orden **ordena las filas** de una relación ascendente o descendente.
>
> **Sintaxis:** `τ columna asc/desc (relación)`
>
> **SQL mental:** `ORDER BY columna ASC / DESC`
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u3-03-03-graph.svg]]
>
> **Se lee así:** τ es el único operador de la unidad que **no cambia el conjunto de datos**: las mismas filas, en otro orden. Por eso puede ir al final de la cadena sin alterar el resultado — y por eso el SQL lo pone al final por convención.

> [!example] 🧪 Ejemplo de orden
>
> `τ precio desc (PRODUCTO)` devuelve: 105 (Shampoo, 10.00), 101 (Pasta, 3.50), 104 (Gel, 4.00) — del más caro al más barato.

---

## 🛠️ Composición de Operadores

> [!tip] 💡 Reglas de composición
>
> Los operadores del álgebra relacional son **cerrados**: el resultado de uno es entrada de otro. Esto permite encadenar operaciones:
>
> `π columnas (σ condición (ρ alias (relación)))`
>
> El orden importa: primero se renombra (si es necesario), luego se filtra, luego se proyecta, luego se agrega, luego se ordena.

> [!example] 🧪 Ejemplo de composición compleja
>
> Obtener el nombre del producto más caro:
>
> `π DESCRIPCION (τ PRECIO desc (PRODUCTO))`
>
> O equivalentemente, con agregación:
>
> `π DESCRIPCION (σ PRECIO = γ MAX(PRECIO) (PRODUCTO) (PRODUCTO))`
>
> **Se lee así:** las dos versiones devuelven lo mismo con operadores distintos — una **ordena y toma el primero**, la otra **calcula el máximo y filtra**. La segunda no necesita τ, y por eso no depende de que el orden esté bien definido.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Renombre para self-join

> [!example] 📋 Planteamiento
>
> Dada `EMPLEADO(id, nombre, id_jefe)`, escribe en álgebra relacional: "obtener el nombre de cada empleado y el nombre de su jefe".
>
> > [!success]- ✅ Solución
> >
> > `π E1.nombre, E2.nombre (EMPLEADO ⨝(E1.id_jefe = E2.id) (ρ E1(EMPLEADO) × ρ E2(EMPLEADO)))`
> >
> > **Por qué:** usamos ρ para crear dos copias de EMPLEADO (E1 como empleado, E2 como jefe) y las unimos por la condición de que el jefe del empleado es el id del jefe.

### ✏️ Ejercicio 2 — Agregación con agrupamiento

> [!example] 📋 Planteamiento
>
> Dada `VENTA(producto_id, cantidad, fecha)`, escribe en álgebra relacional: "obtener el total de cantidad vendida por producto".
>
> > [!success]- ✅ Solución
> >
> > `γ producto_id; SUM(cantidad) → total_vendido (VENTA)`
> >
> > **Por qué:** agrupamos por producto_id y sumamos las cantidades de cada grupo.

### ✏️ Ejercicio 3 — Agregación con filtro previo

> [!example] 📋 Planteamiento
>
> Dada `RESERVA(pasajero_id, vuelo_id, fecha)`, escribe en álgebra relacional: "obtener el número de reservas por pasajero, solo para pasajeros con más de 2 reservas".
>
> > [!success]- ✅ Solución
> >
> > En álgebra relacional pura no hay HAVING directo. La solución es:
> >
> > `γ pasajero_id; COUNT(*) → n_reservas (RESERVA)` seguido de `σ n_reservas > 2 (resultado)`
> >
> > **Equivalente SQL:** `SELECT pasajero_id, COUNT(*) FROM RESERVA GROUP BY pasajero_id HAVING COUNT(*) > 2`

### ✏️ Ejercicio 4 — Ordenamiento descendente

> [!example] 📋 Planteamiento
>
> Dada `PRODUCTO(codigo, nombre, precio)`, escribe en álgebra relacional: "listar productos ordenados de mayor a menor precio".
>
> > [!success]- ✅ Solución
> >
> > `τ precio desc (PRODUCTO)`
> >
> > **Por qué:** τ ordena las filas; `desc` indica descendente.

### ✏️ Ejercicio 5 — Composición completa

> [!example] 📋 Planteamiento
>
> Dadas `ESTUDIANTE(carnet, nombre, carrera)` and `MATRICULA(carnet, cod_materia, nota)`, escribe en álgebra relacional: "obtener los nombres de estudiantes de Sistemas con nota mayor a 8 en alguna materia".
>
> > [!success]- ✅ Solución
> >
> > `π ESTUDIANTE.nombre (σ nota>8 (ESTUDIANTE ⨝(ESTUDIANTE.carnet = MATRICULA.carnet) MATRICULA)) ∩ σ carrera='Sistemas' (ESTUDIANTE)`
> >
> > **Por qué:** primero unimos estudiante con matrícula filtrando nota>8, luego intersectamos con los estudiantes de carrera Sistemas.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino renombre, agregación y orden sin mirar.
> - [ ] Sé cuándo usar ρ para un self-join.
> - [ ] Escribo γ con COUNT, SUM, AVG.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Encadeno ρ, σ, π, γ, τ en una expresión compleja.
> - [ ] Detecto cuándo necesito renombre para usar la misma tabla dos veces.
> - [ ] Escribo la equivalencia SQL de ρ, γ y τ.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Dibujo el diagrama de ejecución de una expresión con renombre y agregación.
> - [ ] Detecto consultas que necesitan HAVING-equivalente en álgebra.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - Diapositivas `2026_1PAO_slides5_1_TICG1018.pdf` — Álgebra Relacional, pp. 23-27 (agregaciones, agrupamiento y renombramiento).
> - Diapositivas `3.4 Operaciones Derivadas-agregacion.pdf` — módulo de operaciones derivadas y agregación.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 8 — álgebra relacional y sus equivalencias en SQL.
> - Guía: [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — ejercicios resueltos de renombre y agregación.
> - Diagramas propios: `u3-03-01-graph` (ρ y self-join), `u3-03-02-graph` (γ), `u3-03-03-graph` (τ), `u3-03-04-graph` (ρ/γ/τ y su equivalente SQL).

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿ρ (renombre)?::Alias de tabla o expresión → AS en SQL.
> - ¿γ (agregación)?::Agrupa y calcula COUNT, SUM, AVG → GROUP BY.
> - ¿τ (orden)?::Ordena filas asc/desc → ORDER BY.
> - ¿Para qué sirve ρ en un self-join?::Para usar la misma tabla dos veces con nombres distintos.
> - ¿Funciones de agregación?::COUNT, SUM, AVG, MIN, MAX.
> - ¿Equivalente SQL de γ?::GROUP BY con funciones de agregado.
> - ¿Equivalente SQL de τ?::ORDER BY.
> - ¿Operadores son cerrados?::Sí, el resultado de uno es entrada del siguiente.
> - ¿Sintaxis de γ?::γ col_agrup; función → atributo (relación).
> - ¿τ cambia los datos?::No, solo el orden de las filas.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[01 - Operadores Básicos]] — σ, π, ×, ∪, −, ∩.
> - [[02 - Operadores Derivados y Joins]] — ⨝, ⟕, ⟖, ⋉, división.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — 4 ejercicios resueltos con renombre y agregación.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[../Unidad 4 - SQL/01 - Introducción a SQL|Introducción a SQL (Unidad 4)]]
> - Anterior: [[02 - Operadores Derivados y Joins]]

---

**Tags:** #TICG1018 #unidad3 #algebra-relacional #renombre #agregacion #bd
