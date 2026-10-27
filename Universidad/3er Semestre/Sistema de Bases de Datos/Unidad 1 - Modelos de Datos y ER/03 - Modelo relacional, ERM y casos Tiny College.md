---
dg-publish: true
tags: [TICG1018, unidad1, relacional, erm, chen, casos]
---

# 🗃️ Modelo Relacional, ERM y Casos Tiny College

## 🎯 Introducción

> [!info] 💡 ¿Por Qué las Tablas Ganaron y el Dibujo Manda?
>
> Desde 1970 casi todo lo que consultas vive en tablas, y desde 1976 casi todo lo que se diseña se dibuja primero. Entender por qué ganó cada uno —y qué resuelve cada notación— es lo que separa traducir un ER mecánicamente de diseñar uno que no se rompa al implementar.
>
> **Aplicaciones:**
> - **Implementación:** toda tabla del proyecto y del SQL futuro sale de aquí.
> - **Diseño gráfico:** el ERD es el plano que cliente y dev entienden sin código.
> - **Lección 1 (13-oct):** Codd en 1 frase + Chen en 1 frase + traducir 1 ER a tablas.
>
> | Concepto | Relacional (implementa) | ERM (diseña) |
> |---|---|---|
> | **Autor/año** | Codd | Chen 1976 |
> | **Pieza base** | Relación = tabla (filas × columnas) | Entidad + relación graficadas |
> | **Conexión** | Columna en común | Rombo/verbo + cardinalidad |
> | **Notaciones ERD** | — (no se dibuja: se escribe en tablas) | Chen, pata de gallo, clases |

![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-01-graph.svg]]

---

## 📋 Definiciones Formales

> [!info] ℹ️ Cómo leer esta sección
> Una definición por bloque, cada una con su ejemplo y su figura. Nivel lógico: aquí las tablas sí son las protagonistas.

### 1️⃣ Relación, tupla y atributo — el vocabulario de tabla

> [!note] 📋 Definición — Relación, tupla, atributo
>
> - **Relación (tabla):** intersección de filas y columnas.
> - **Tupla/fila:** una ocurrencia (un estudiante concreto).
> - **Atributo/columna:** una casilla (nombre, código).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-02-er.svg]]
>
> **Ejemplo:** la tabla es la relación; cada fila una tupla (`0876, Jorge`); cada columna un atributo (`nombre`). Sí: **relacional = tablas** — Codd propuso guardar todo en tablas relacionadas por columnas comunes, con base matemática.
>
> **Por qué "relacional" (campusMVP):** no es porque las tablas *se relacionen* con FK — es porque los datos se guardan como **relaciones** (listas = tablas). Tabla = Relación, literal.
>
> **Northwind (ejemplo clásico):** pedidos con Proveedores, Productos, Empleados, Clientes, Transportistas + `Order Details` como intermedia. Si la nombran en clase, ya sabes qué es.
>
> **Las 6 cualidades de un buen diseño (T. Grayson, vía campusMVP):** refleja el mundo real; representa todos los datos esperados en el tiempo; evita redundancia; acceso eficaz; mantiene integridad; claro y comprensible.
>
> > [!quote] 📖 campusMVP, "Diseñando una base de datos en el modelo relacional" (2014) — https://www.campusmvp.es/recursos/post/Disenando-una-base-de-datos-en-el-modelo-relacional.aspx

### 2️⃣ Tres niveles — del dibujo al disco

> [!note] 📋 Definición — Niveles conceptual, lógico y físico
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-03-graph.svg]]
>
> **Ejemplo:** el rombo *toma* (conceptual) → tabla MATRÍCULA con (PK,FK) (lógico) → índice sobre `carnet` (físico). Cada nivel decide cosas distintas.

> [!info] 📖 El deck de cátedra: del conceptual al lógico (slides3, p. 3)
> El deck del Ing. Magallanes abre la unidad del modelo lógico con el diagrama que resume todo el proceso: una **ciudad** y un **estudiante** en el modelo conceptual, con sus cardinalidades (1,1) y (0,n), y la misma información ya como tablas en el modelo lógico.

![[Archivos/bd-s03-p3.png]]

> **El diseño lógico (p. 4):** *"es el proceso de construir un modelo lógico a partir de un modelo conceptual"*, y tanto el conceptual como el lógico son **procesos iterativos**, no lineales.

### 3️⃣ Regla de traducción ER→tablas — el puente

> [!note] 📋 Definición — Traducción
>
> Entidad → tabla; atributo → columna; clave → PK; N:M → intermedia con 2 FK; 1:N → FK del lado N.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-04-graph.svg]]
>
> **Ejemplo:** ESTUDIANTE(entidad) → tabla; `carnet`(clave) → PK; *toma*(N:M) → MATRÍCULA con 2 FK. El detalle completo vive en la Unidad 2.

> [!info] 📖 El deck de cátedra: las tres formas de derivar relaciones (slides3, pp. 16-21)
> El deck cierra el módulo con la derivación del modelo lógico según la cardinalidad, y usa los mismos ejemplos que Tiny College.

![[Archivos/bd-s03-p16.png]]

![[Archivos/bd-s03-p17.png]]

![[Archivos/bd-s03-p20.png]]

![[Archivos/bd-s03-p21.png]]

> **Entidad fuerte y débil (p. 16):** `COURSE(CRS_CODE, …)` y `CLASS(CLASS_CODE, CRS_CODE, …)` con la `CRS_CODE` como foreign key.
>
> **1:N (p. 17):** la entidad **padre** es la del lado de uno y la **hija** la del lado de muchos; para representarla se copia el atributo clave del lado uno al lado muchos.
>
> **N:N (p. 20):** *"se crea una nueva Tabla para representar la relación (ER) y se incluyen todos los atributos de la relación"*.
>
> **Recursiva (p. 21):** *"se incluye una copia de la clave primaria pero se renombra"* — `EMPLOYEE(EMP_NUM, …, MANAGER_EMP)` con `MANAGER_EMP` como FK a la misma tabla.

> [!info] 📖 El deck de cátedra: elementos del modelo relacional (slides3, pp. 6-10)
> *"Creado por Edgar F. Codd a principios de los 70, laboratorios de IBM. Modelo lógico de datos no de muy alto nivel, orientado a registro. Sólida base teórica…"* (p. 6).

![[Archivos/bd-s03-p7.png]]

![[Archivos/bd-s03-p8.png]]

![[Archivos/bd-s03-p10.png]]

> **Claves (p. 8):** *"una clave candidata es el atributo o conjunto de atributos que identifica de manera única a cada tupla de la relación"*; la **clave primaria** es la candidata elegida; la **clave foránea** referencia la primaria de otra relación.
>
> **Representación del esquema (p. 10):** el deck escribe el esquema completo con la sintaxis `CLIENTE(codcli, nombre, …)` — el formato exacto que se usa en los ejercicios de conversión de la Unidad 2.

### 4️⃣ Entidad débil — doble condición

> [!note] 📋 Definición — Entidad débil (Coronel 4.1.6)
>
> Cumple AMBAS: existencia-dependiente + PK derivada del padre. Chen: rectángulo **doble**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-05-graph.svg]]
>
> **Ejemplo:** DEPENDENT se identifica con `EMP_NUM + DEP_NUM` juntos: `EMP_NUM` dice *de qué empleado es* (heredado del padre) y `DEP_NUM` lo distingue *entre los dependientes de ese empleado* (1º, 2º...). Ni uno solo identifica: el mismo `DEP_NUM = 1` existe en mil empleados. Sin el empleado no existe ni se identifica.
>
> **Pista del enunciado (caso banco):** *"se numera desde 1 dentro de cada cuenta"* = el número se repite entre cuentas → TRANSACCION es débil; en Chen su identificador va subrayado discontinuo y su clave real es `num_cuenta + num_transaccion`.
>
> > [!quote] 📖 C. Zavaleta, *MER: guía completa*, caso entidad bancaria (2026)
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-06-graph.svg]]
>
> **Se lee así:** rectángulo doble = débil (DEPENDENT cuelga de EMPLOYEE); rectángulo simple que existe solo = fuerte (PART con partes propias no necesita a VENDOR).

### 5️⃣ Fuerza de relación — punteada vs sólida

> [!note] 📋 Definición — Fuerza (Coronel 4.1.7)
>
> - **Débil (non-identifying):** la PK hija NO hereda del padre (solo FK); línea **punteada**. Ej.: CLASS con `CLASS_CODE` propia.
> - **Fuerte (identifying):** la PK hija hereda del padre (PK compuesta); línea **sólida**. Ej.: CLASS con `CRS_CODE + CLASS_SECTION`.
> - Chen no distingue fuerza (es conceptual); Crow's Foot sí (afecta implementación). La fuerza la decide el diseñador según transacciones y eficiencia.
>
> **Figuras:** ver los dos diagramas de CLASS en Ejemplos Trabajados (versión débil y versión fuerte).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-07-er.svg]]
>
> **Se lee en patas:** la línea **punteada** = no identifica (la hija tiene PK propia); la **sólida** = identifica (la PK hija hereda la del padre).

### 6️⃣ Supertipo–subtipo — lo común arriba, lo propio abajo (unidad1.3-1.5 §§41–45)

> [!note] 📋 Definición — Supertipo y subtipo
>
> - **Supertipo:** 2+ entidades comparten atributos o relaciones (CLIENTES: idCliente, nombre, dirección…).
> - **Subtipo:** tiene atributos o relaciones **propias** (EMPRESA: RUC; Persona: cédula) y **hereda todo** lo del supertipo, incluido el **identificador compartido**.
>
> **Notación:** línea **simple** = subtipo opcional; línea **doble** = supertipo obligatorio. Círculo **d** = solo un subtipo (disjunto); **o** = varios a la vez (sobrelapado).
>
> **Ejemplo:** todo EMPLEADO tiene idEmp/nombre; solo VENDEDOR tiene numVentas. La conversión a tablas depende del caso (a/b/c/d) — ver Regla 6 de la Unidad 2.

### 7️⃣ Recursiva — la entidad que se relaciona consigo misma

> [!note] 📋 Definición — Relación reflexiva
>
> La misma entidad en dos roles: EMPLEADO *supervisa* EMPLEADO (jefe vs supervisado). En tablas nace FK a sí misma (`idSupervisor` → `idEmpleado`); si es M:N, tabla puente con doble FK.
>
> **Ejemplo:** sin roles etiquetados el diagrama es ilegible — rotula cada rama.

### 8️⃣ Ternaria vs entidad + binarias — cuándo partir

> [!note] 📋 Definición — Ternaria (unidad1.3-1.5 §§37–38)
>
> Tres entidades en UNA relación (Cliente–Producto–Compra–Tienda) solo si el hecho necesita a las tres a la vez. Si se puede contar por pares, parte en binarias. En tablas: una tabla con las 3 PK como (PK,FK) + atributos propios (calificación).
>
> **Ejemplo:** REGISTRO(idProf, matricula, idMateria PK,FK + calificacion): la nota solo existe con profe + alumno + materia juntos.

---

## 🧵 Notación de Chen a Fondo

### 🎭 Cada Símbolo Tiene un Trabajo

> [!example] 🧪 Leer Chen como Profesional
>
> | Símbolo | Significado | Ejemplo |
> |---|---|---|
> | **Rectángulo simple** | Entidad fuerte | ESTUDIANTE |
> | **Rectángulo doble** | Entidad débil | DEPENDENT |
> | **Rombo** | Relación con verbo | *dicta*, *toma* |
> | **Óvalo** | Atributo | Nombre, código |
> | **Óvalo + línea punteada** | Atributo derivado (calculado) | Edad desde fecha |
> | **Subrayado** | Clave (PK) | `carnet` |
> | **Cardinalidad** | Del lado de la entidad **relacionada** | (1,4) junto a CLASS |
>
> Solo Chen marca derivados con punteada (Crow's Foot no tiene cómo). M:N existe en conceptual pero no va al relacional.
>
> *(Leyenda Chen: ver el diagrama dibujable de abajo — rectángulo, rombo, óvalo, punteada y subrayado.)*
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-08-graph.svg]]
>
> **Cómo leerlo:** rectángulo = entidad (`[[ ]]` = débil) · rombo `{ }` = relación · óvalo `([ ])` = atributo · punteada `-.-` = derivado · subrayado = PK. Compáralo con la tabla de arriba: es el mismo Chen, dibujable en cualquier nota.

---

## 🛠️ Método para Pasar del ERD a Tablas

> [!note] 📋 Procedimiento General
>
> 1. Verifica el ERD: toda entidad con PK, toda relación con verbo y cardinalidad.
> 2. Crea una tabla por entidad con sus columnas y PK.
> 3. Resuelve cada N:M con tabla intermedia (las 2 FK, PK compuesta).
> 4. Coloca cada FK del lado N con su contraparte PK.
> 5. Decide fuerza: ¿hereda la PK o no? Dibuja punteada/sólida en consecuencia.
> 6. Ordena creación y carga: lado 1 primero (padres antes que hijas).
>
> **Principio clave:** el orden de carga no es decorativo — violarlo rompe integridad referencial.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-09-flow.svg]]

---

## 🎨 Ejemplos Trabajados: Tiny College

> [!example] 🟢 Ejemplo — CLASS Débil vs Fuerte
>
> Misma realidad, dos decisiones de clave:
>
> | Versión | Definición CLASS | Línea | Cuándo |
> |---|---|---|---|
> | **Débil** | `CLASS(CLASS_CODE, CRS_CODE, ...)` — PK propia | Punteada | Identidad independiente |
> | **Fuerte** | `CLASS(CRS_CODE, CLASS_SECTION, ...)` — PK heredada | Sólida | Identidad ligada al padre |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-10-er.svg]]
>
> **Versión débil (punteada):** CLASS tiene PK propia; solo referencia al padre con FK.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-11-er.svg]]
>
> **Versión fuerte (sólida):** la PK de CLASS hereda `CRS_CODE` — sin el curso, la clase no se identifica.
>

> [!example] 🟢 Ejemplo — Clasificar DIVISION–EMPLOYEE
>
> Solo sabes *"Una DIVISIÓN es manejada por un EMPLEADO"* — insuficiente:
>
> | Paso | Acción |
> |---|---|
> | Pregunta de vuelta | ¿Puede uno manejar varias? |
> | Si sí | 1:M: "Un EMPLEADO maneja muchas DIVISIONes" |
> | Si no | 1:1: "Un EMPLEADO maneja una sola DIVISIÓN" |
>

![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-12-flow.svg]]

---

## 📋 Tablas Comparativas

> [!note] 📋 Chen vs Crow's Foot · Débil vs Fuerte
>
> | Aspecto | Chen | Crow's Foot |
> |---|---|---|
> | **Uso** | Teoría y parciales | Herramientas y pizarrón |
> | **Cardinalidad** | Lado de la relacionada | Junto a la entidad que aplica |
> | **Derivados** | Línea punteada ✅ | Sin marca ❌ |
> | **Fuerza** | No distingue | Punteada/sólida por PK |
>
> | Versión CLASS | PK | Línea | Cuándo |
> |---|---|---|---|
> | **Débil** | Propia | Punteada | Identidad independiente |
> | **Fuerte** | Heredada | Sólida | Identidad ligada al padre |

---

## ⚠️ Errores Comunes y Principios Lógicos

> [!warning] ⚠️ Cómo leer esta sección
> Cada error trae su dibujo: lo ❌ que delata el problema y lo ✅ que lo evita.

### ❌ Error 1: Tablas sin pasar por el ER

> [!danger] ❌ Viola: orden obligatorio ERD → tablas → SQL
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-13-graph.svg]]

### ❌ Error 2: Herencia de PK indecisa

> [!danger] ❌ Viola: decide fuerza antes de dibujar
>
> PK compuesta en el diagrama pero FK simple en tablas (o al revés): decide si hereda primero, verifica después.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-14-er.svg]]
>
> Si la línea es sólida, la PK hija **debe** contener la del padre. Si es punteada, la hija tiene PK propia.

### ❌ Error 3: Cargar el lado N primero

> [!danger] ❌ Viola: padres antes que hijas
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas draw.io/u1-03-15-flow.svg]]

### ❌ Error 4: M:N directo al relacional

> [!danger] ❌ Viola: M:N existe en conceptual, no en tablas
>
> Sin intermedia no hay modelo que funcione: toda M:N produce tabla con las 2 FK (ver Regla 2 de la Unidad 2).

### ❌ Error 5: Subtipo sin nada propio (o ternaria que era binaria)

> [!danger] ❌ Viola: el subtipo debe aportar + la ternaria debe necesitar a los tres
>
> Subtipo sin atributos ni relaciones propias = no es subtipo, es un valor (usa discriminador o bandera). Y ternaria separable en pares = dos binarias con sus intermedias.
>
> **EL ERROR ESTÁ AQUÍ:** crear VENDEDOR sin numVentas "por si acaso", o dibujar ternaria Cliente–Producto–Tienda cuando Compra se cuenta por pares.

---

## 📝 Ejercicios Propuestos

> [!info] ℹ️ Cómo trabajarlos
> Tapa la solución, resuelve, compara. Respuestas colapsables abajo.

### ✏️ Ejercicio 1 — ¿Débil o fuerte?

> [!example] 📋 Planteamiento
>
> CLASS con `CLASS_CODE` propia vs CLASS con `CRS_CODE + CLASS_SECTION`. ¿Cuál es débil, cuál fuerte, qué línea lleva cada una y cuándo elegirías cada versión?
>
> > [!success]- ✅ Solución
> >
> > Propia = débil (punteada): identidad independiente. Heredada = fuerte (sólida): identidad ligada al padre. Elige fuerte cuando la clase no se identifica sin el curso y las transacciones las piden juntas; débil cuando la clase tiene vida propia.

### ✏️ Ejercicio 2 — Los 7 símbolos Chen

> [!example] 📋 Planteamiento
>
> Nombra los 7 símbolos Chen con su significado y un ejemplo de Tiny College para cada uno.
>
> > [!success]- ✅ Solución
> >
> > Rectángulo simple (fuerte: ESTUDIANTE), doble (débil: DEPENDENT), rombo (relación: *toma*), óvalo (atributo: nombre), óvalo punteado (derivado: edad), subrayado (PK: carnet), cardinalidad del lado de la relacionada ((1,4) junto a CLASS).

### ✏️ Ejercicio 3 — Resuelve la N:M

> [!example] 📋 Planteamiento
>
> ESTUDIANTE–MATERIA M:N con *toma*. Escribe las 3 tablas con PK/FK y el orden de carga.
>
> > [!success]- ✅ Solución
> >
> > `ESTUDIANTE(carnet PK)`, `MATERIA(codigo PK)`, `MATRICULA(carnet PK,FK, codigo PK,FK)`. Carga: padres primero (las 2 entidades), intermedia al final. Sin intermedia no hay modelo que funcione.

### ✏️ Ejercicio 4 — Supertipo, recursiva y ternaria

> [!example] 📋 Planteamiento
>
> a) CLIENTES(idCliente, nombre) con EMPRESA(RUC) y Persona(cédula): ¿qué hereda cada subtipo y qué identificador usan? b) Dibuja EMPLEADO *supervisa* EMPLEADO con roles. c) ¿Compra de cliente/producto/tienda es ternaria o binarias? Justifica.
>
> > [!success]- ✅ Solución
> >
> > - a) Ambos heredan idCliente/nombre y el identificador compartido; EMPRESA aporta RUC, Persona aporta cédula. Sin aporte propio no hay subtipo.
> > - b) Una entidad, dos roles (jefe/supervisado); en tablas: `idSupervisor` FK a `idEmpleado`.
> > - c) Ternaria solo si la compra exige a los tres a la vez (REGISTRO con 3 FK + calificacion); si se cuenta por pares, parte en binarias.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino relación, tupla, niveles conceptual/lógico/físico sin mirar.
> - [ ] Dibujo los 7 símbolos Chen con su significado.
> - [ ] Traduzco un ER simple a tablas con PKs y FKs.
>
> [!note] 📋 Nivel Intermedio
>
> - [ ] Decido débil vs fuerte por la PK y dibujo su línea.
> - [ ] Resuelvo N:M con intermedia correcta.
> - [ ] Ordeno creación y carga sin romper integridad.
>
> [!note] 📋 Nivel Avanzado
>
> - [ ] Comparo CLASS débil vs fuerte justificando por transacciones.
> - [ ] Detecto en diagramas ajenos N:M olvidadas y fuerzas invertidas.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - `unidad1.3-1.5.pdf` (Irene Cheung) + Codd (relacional) · Chen 1976 (ERM).
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 4 §§4.1.6–4.1.7 y cap. 2 (Chen vs Crow's Foot).
> - C. Zavaleta, *MER: guía completa con ejemplos*, 2026 (casos prácticos citados arriba).

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition

- ¿Relacional en 1 frase (Codd)?::Todo en tablas unidas por columna común, con base matemática.
- ¿Chen 1976 aportó qué?::El ERD gráfico que complementa al relacional para diseñar.
- ¿Débil vs fuerte (línea y PK)?::Débil: solo FK, punteada. Fuerte: PK heredada compuesta, sólida.
- ¿N:M al relacional?::Tabla intermedia con las 2 FK.
- ¿Símbolo Chen de entidad débil y de derivado?::Rectángulo doble; óvalo con línea punteada.
- ¿Por qué "relacional" se llama así?::Porque guarda datos como relaciones (= tablas), no por las FK.
- ¿Supertipo vs subtipo?::Común arriba (identificador compartido); propio abajo (hereda todo).
- ¿d vs o (círculo)?::Disjunto (solo uno) vs sobrelapado (varios a la vez).
- ¿Ternaria cuándo?::Solo si el hecho exige a las tres entidades a la vez.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[02 - Entidades, atributos, claves y relaciones]] — el vocabulario que aquí se vuelve tablas.
> - [[01 - Dato, información y modelos de datos]] — el problema original.
> - Álgebra relacional aplicada al taller 2 (σ, π, ⨝ y catálogo con ⟕, ⟖, ⋉, τ): [[Guía de Problemas 2 - Álgebra Relacional y Normalización]].
> - Ver también la nota de **Claves** integrada en 02 si vienes de un link viejo: ahora vive ahí.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Índice Unidad 1: [[00 - Índice Unidad 1]] · Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Álgebra relacional con ejercicios: [[Guía de Problemas 2 - Álgebra Relacional y Normalización]] (catálogo de operadores, diapositivas 3.1/3.2)
> - Anterior: [[02 - Entidades, atributos, claves y relaciones]]
> - Conversión a tablas: [[01 - Conversión MC a ML por cardinalidad]] · [[02 - Primera forma normal y diccionario de datos]]

---

**Tags:** #TICG1018 #unidad1 #relacional #erm #chen #casos #bd
