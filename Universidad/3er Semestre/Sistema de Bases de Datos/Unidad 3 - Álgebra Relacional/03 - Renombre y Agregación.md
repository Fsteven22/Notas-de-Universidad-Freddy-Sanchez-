---
dg-publish: true
tags: [TICG1018, unidad3, algebra-relacional, renombre, agregacion, orden, bd]
---

# ⚙️ Álgebra Relacional — Renombre y Agregación

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Renombre y Agregación?
> Los operadores básicos y derivados nos permiten filtrar, proyectar y combinar tablas. Pero hay dos operaciones que faltan: darle alias a una tabla (para usarla dos veces en la misma consulta, como un self-join) y agrupar y calcular (como GROUP BY en SQL). Eso resuelven ρ (renombre) y γ (agregación).
> **Aplicaciones:**
> - Self-join: usar la misma tabla dos veces con nombres distintos.
> - Consultas agregadas: promedios, conteos, sumas por grupo.
> - Ordenamiento: ordenar resultados ascendente/descendente.
> - Lección 1 (13-oct): ρ para alias, γ para agregación, τ para orden.

> [!example] 📎 Diapositivas de referencia
> ![[../../Unidad 0 - Guias y Ejercicios/Diapositivas/3.4 Operaciones Derivadas-agregacion.pdf]]
> ![[../../Unidad 0 - Guias y Ejercicios/Diapositivas/2026_1PAO_slides5_1_TICG1018.pdf]]

---

## 📋 Definiciones Formales

### 1️⃣ Renombre ρ

> [!note] 📋 Definición — Renombre ρ
> El renombre le da un alias a una relación o a una expresión. Es esencial cuando necesitas usar la misma tabla dos veces en una consulta (self-join) o cuando quieres simplificar nombres largos.
> Sintaxis: ρ alias(expresión) o ρ nuevo_nombre(relación)
> SQL mental: AS
> ```mermaid
graph TD
    A[TABLA] -->|ρ S| B[S: copia 1]
    A -->|ρ L| C[L: copia 2]
    B -->|⨝| D[Resultado]
    C -->|⨝| D
    style A fill:#e1f5fe
    style B fill:#c8e6c9
    style C fill:#c8e6c9
    style D fill:#fff3e0
```

> [!example] 🧪 Ejemplo de renombre (self-join)
> Para comparar un aeropuerto de salida con uno de llegada (misma tabla AEROPUERTO dos veces):
> ρ S(AEROPUERTO) ⨝ ρ L(AEROPUERTO)
> Ahora S y L son dos copias distintas de la misma tabla, y puedes comparar S.pais = L.pais ∧ S.ciudad ≠ L.ciudad.

---

### 2️⃣ Agregación γ

> [!note] 📋 Definición — Agregación γ
> La agrupación agrupa filas y calcula funciones sobre cada grupo. Es el equivalente de GROUP BY con funciones de agregado en SQL.
> Sintaxis: γ columnas_de_agrupación; función1 → atributo1, función2 → atributo2 (relación)
> Funciones: COUNT, SUM, AVG, MIN, MAX.
> ```mermaid
graph TD
    A[RESERVA] -->|γ mid; COUNT(*)| B[Resultado: reservas por marinero]
    style A fill:#e1f5fe
    style B fill:#c8e6c9
```
> ![[../../Unidad 0 - Guias y Ejercicios/Archivos/Álgebra-Relacional/bd-s05-p24.png]]
> ![[../../Unidad 0 - Guias y Ejercicios/Archivos/Álgebra-Relacional/bd-s05-p26.png]]

> [!example] 🧪 Ejemplo de agregación
> | Marinero |
> |---|
> | mid | mnombre | rating | edad |
> | 22 | dustin | 7 | 45.0 |
> | 31 | lubber | 8 | 55.5 |
> | 58 | rusty | 10 | 35.0 |
>
> γ mid; COUNT(*) → n_reservas (RESERVA) agrupa reservas por marinero y cuenta cuántas tiene cada uno.
> γ avg(edad) (σ rating=10 (Marinero)) calcula la edad promedio de marineros con rating 10.

> [!info] 📖 El deck de cátedra: agregaciones (slides05, pp. 23-26)
> El deck del Ing. Magallanes cierra el módulo de álgebra con agregaciones y agrupamiento.
>
> Agregaciones (pp. 23-26): γ agrupa y calcula (G sum(rating) (R), G count(mid) (Marinero), G avg(edad) (σ rating=10 (Marinero))) y el agrupamiento aplica la función por grupos de datos.
> ![[../../Unidad 0 - Guias y Ejercicios/Archivos/Álgebra-Relacional/bd-s05-p26.png]]

---

### 3️⃣ Orden τ

> [!note] 📋 Definición — Orden τ
> El operador de orden ordena las filas de una relación ascendente o descendente.
> Sintaxis: τ columna asc/desc (relación)
> SQL mental: ORDER BY columna ASC / DESC
> ```mermaid
graph TD
    A[PRODUCTO] -->|τ PRECIO desc| B[Resultado: ordenado por precio]
    style A fill:#e1f5fe
    style B fill:#c8e6c9
```

> [!example] 🧪 Ejemplo de orden
> τ precio desc (PRODUCTO) devuelve: 105 (Shampoo, 10.00), 101 (Pasta, 3.50), 104 (Gel, 4.00) — del más caro al más barato.

---

## 🛠️ Composición de Operadores

> [!tip] 💡 Reglas de composición
> Los operadores del álgebra relacional son cerrados: el resultado de uno es entrada de otro. Esto permite encadenar operaciones:
> π columnas (σ condición (ρ alias (relación)))
> El orden importa: primero se renombra (si es necesario), luego se filtra, luego se proyecta, luego se agrega, luego se ordena.

> [!example] 🧪 Ejemplo de composición compleja
> Obtener el nombre del producto más caro:
> π DESCRIPCION (τ PRECIO desc (PRODUCTO))
> O equivalentemente, con agregación:
> π DESCRIPCION (σ PRECIO = γ MAX(PRECIO) (PRODUCTO) (PRODUCTO))

---

## 🎯 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Renombre para self-join

> [!example] 📋 Planteamiento
> Dada EMPLEADO(id, nombre, id_jefe), escribe en álgebra relacional: obtener el nombre de cada empleado y el nombre de su jefe.
> > [!success]- ✅ Solución
> > π E1.nombre, E2.nombre (EMPLEADO ⨝(E1.id_jefe = E2.id) (ρ E1(EMPLEADO) × ρ E2(EMPLEADO)))
> > **Por qué:** usamos ρ para crear dos copias de EMPLEADO (E1 como empleado, E2 como jefe) y las unimos por la condición de que el jefe del empleado es el id del jefe.

### ✏️ Ejercicio 2 — Agregación con agrupamiento

> [!example] 📋 Planteamiento
> Dada VENTA(producto_id, cantidad, fecha), escribe en álgebra relacional: obtener el total de cantidad vendida por producto.
> > [!success]- ✅ Solución
> > γ producto_id; SUM(cantidad) → total_vendido (VENTA)
> > **Por qué:** agrupamos por producto_id y sumamos las cantidades de cada grupo.

### ✏️ Ejercicio 3 — Agregación con filtro previo

> [!example] 📋 Planteamiento
> Dada RESERVA(pasajero_id, vuelo_id, fecha), escribe en álgebra relacional: obtener el número de reservas por pasajero, solo para pasajeros con más de 2 reservas.
> > [!success]- ✅ Solución
> > En álgebra relacional pura no hay HAVING directo. La solución es:
> > γ pasajero_id; COUNT(*) → n_reservas (RESERVA) seguido de σ n_reservas > 2 (resultado)
> > **Equivalente SQL:** SELECT pasajero_id, COUNT(*) FROM RESERVA GROUP BY pasajero_id HAVING COUNT(*) > 2

### ✏️ Ejercicio 4 — Ordenamiento descendente

> [!example] 📋 Planteamiento
> Dada PRODUCTO(codigo, nombre, precio), escribe en álgebra relacional: listar productos ordenados de mayor a menor precio.
> > [!success]- ✅ Solución
> > τ precio desc (PRODUCTO)
> > **Por qué:** τ ordena las filas; desc indica descendente.

### ✏️ Ejercicio 5 — Composición completa

> [!example] 📋 Planteamiento
> Dadas ESTUDIANTE(carnet, nombre, carrera) and MATRICULA(carnet, cod_materia, nota), escribe en álgebra relacional: obtener los nombres de estudiantes de Sistemas con nota mayor a 8 en alguna materia.
> > [!success]- ✅ Solución
> > π ESTUDIANTE.nombre (σ nota>8 (ESTUDIANTE ⨝(ESTUDIANTE.carnet = MATRICULA.carnet) MATRICULA)) ∩ σ carrera='Sistemas' (ESTUDIANTE)
> > **Por qué:** primero unimos estudiante con matrícula filtrando nota>8, luego intersectamos con los estudiantes de carrera Sistemas.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
> - Defino renombre, agregación y orden sin mirar.
> - Sé cuándo usar ρ para un self-join.
> - Escribo γ con COUNT, SUM, AVG.

> [!note] 📋 Nivel Intermedio
> - Encadeno ρ, σ, π, γ, τ en una expresión compleja.
> - Detecto cuándo necesito renombre para usar la misma tabla dos veces.
> - Escribo la equivalencia SQL de ρ, γ y τ.

> [!note] 📋 Nivel Avanzado
> - Dibujo el diagrama de ejecución de una expresión con renombre y agregación.
> - Detecto consultas que necesitan HAVING-equivalente en álgebra.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
> - ¿ρ (renombre)?::Alias de tabla o expresión → AS en SQL.
> - ¿γ (agregación)?::Agrupa y calcula COUNT, SUM, AVG → GROUP BY.
> - ¿τ (orden)?::Ordena filas asc/desc → ORDER BY.
> - ¿Para qué sirve ρ en un self-join?::Para usar la misma tabla dos veces con nombres distintos.
> - ¿Funciones de agregación?::COUNT, SUM, AVG, MIN, MAX.
> - ¿Equivalente SQL de γ?::GROUP BY con funciones de agregado.
> - ¿Equivalente SQL de τ?::ORDER BY.
> - ¿Operadores son cerrados?::Sí, el resultado de uno es entrada del siguiente.
> [!note] 🧠 Repasa con el plugin Spaced Repetition (Lección 1: 13-oct)

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
> - [[01 - Operadores Básicos]] — σ, π, ×, ∪, −, ∩.
> - [[02 - Operadores Derivados y Joins]] — ⨝, ⟕, ⟖, ⋉, división.
> - [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] — 4 ejercicios resueltos con renombre y agregación.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[../Unidad 4 - SQL/01 - Introducción a SQL|Introducción a SQL (Unidad 4)]]
> - Anterior: [[02 - Operadores Derivados y Joins]]

---

**Tags:** #TICG1018 #unidad3 #algebra-relacional #renombre #agregacion #bd
