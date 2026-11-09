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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-18-er.svg]]
>
> ✅ **Es 1FN:** `CLIENTE(cédula, nombre)` y `TELEFONO(cédula, número)`  
> Cada fila tiene un solo teléfono. Un cliente puede tener N filas en TELEFONO.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-19-er.svg]]
>
> **Se lee así:** el diagrama es la **solución ya en notación de motor**, y hay que mirar tres cosas. Primera, `TELEFONO` tiene **dos columnas que forman la PK compuesta**: `cedula PK, FK` y `numero PK`. Segunda, la relación dice `CLIENTE ||--o{ TELEFONO : "un telefono por fila"` — de una a muchas, con la etiqueta en el lado de la-many. Tercera, la **relación tiene nombre en singular** (`un telefono por fila`), no `tiene`: es una convención de lectura que cada fila de `TELEFONO` representa *un* teléfono.
>
> **Por qué importa:** los atributos marcados `PK, FK` son el corazón de la normalización. `cedula` está en `TELEFONO` **por dos razones a la vez**: identifica la fila (junto a `numero`) y además señala a quién pertenece el teléfono. Por eso la PK de `TELEFONO` **no puede ser solo** `cedula`: si lo fuera, cada cliente podría tener un solo teléfono y estaríamos otra vez en la 1FN rota, solo que más escondida.
>
> **Ejemplo:** el cliente `0876456324` con tres teléfonos produce **tres filas** en `TELEFONO`: `(0876456324, 2345678)`, `(0876456324, 2345679)`, `(0876456324, 2345680)`. La tabla `CLIENTE` sigue teniendo una sola fila. Ese par de filas extra es, literalmente, lo que "normalizar" bought.

### 2️⃣ Las 5 condiciones de la 1FN

> [!note] 📋 Definición — Checklist de la 1FN
>
> Para que una tabla esté en **1FN**, debe cumplir las 5 condiciones. Si falla cualquiera, no está en 1FN:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-14-flow.svg]]
>
> | # | Condición | ¿Qué significa en lenguaje sencillo? |
> |---|---|---|
> | 1 | Sin orden en las filas | No importa si la fila 1 está arriba o abajo de la fila 2 |
> | 2 | Sin orden en las columnas | No importa si `nombre` está a la izquierda o derecha de `cédula` |
> | 3 | Sin filas duplicadas | No puede haber dos filas idénticas |
> | 4 | Un valor por celda | Cada celda guarda exactamente un dato, no una lista |
> | 5 | Columnas regulares | No hay columnas ocultas como `id_fila`, `timestamp`, ni IDs de objeto sueltos |

> [!info] 📖 El deck de cátedra: la 1FN en la pizarra (slides04 y BD 02.3)
>
> El deck del Ing. Magallanes define la 1FN como *"una tabla donde la intersección de cada fila y columna contiene solo un valor"* y da el ejemplo canónico de la rama con varios teléfonos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-s04-p8.png]]
>
> **Se lee así:** la lámina (p. 8) es la **definición y el ejemplo roto, en la misma pantalla**. Arriba, la definición: *"una tabla donde la intersección de cada fila y columna contiene solo un valor"*, y dos corolarios: *"esto prohíbe anidamientos o grupos repetidos"* y *"la intersección debe ser atómica"*. Abajo, la tabla `branchNo / branchAddress / telNos` con cuatro sucursales: `B001`, `B002`, `B003` y `B004`, y en la columna `telNos` los teléfonos **separados por comas** — `212-371-3000` para B001; `503-555-3618, 503-555-2727, 503-555-6241` para B003; `206-555-6756, 206-555-8234, 206-555-3131, 206-555-4112` para B004. La flecha de la lámina señala exactamente una de esas celdas: *"más de un valor, no está en 1NF"*.
>
> **Por qué importa:** la definición usa la palabra **intersección**, que es la misma imagen mental que da nombre al modelo relacional (Codd): una relación es un conjunto de pares ordenados, y cada par —una intersección fila-columna— debe tener un único valor. La 1FN no es una regla extra: es la **primera exigencia** de ese modelo. Por eso la lámina también marca `branchNo` como *Primary key*: aun con PK, la tabla sigue sin estar en 1FN.
>
> **Ejemplo:** la fila `B004 · 16 – 14th Avenue, Seattle, WA 98128 · 206-555-3131, 206-555-4112` es el ejemplo perfecto: la dirección también contiene comas, pero eso **no** viola la 1FN, porque sigue siendo **un** valor de texto. Lo que viola es la lista de teléfonos, que son **cuatro** valores en una celda. La distinción es "un texto que contiene separadores" ≠ "varios valores".
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Logico-Conversion/bd-023-p10.png]]
>
> **Se lee así:** la lámina (p. 10 de BD 02.3) es la **versión completa y formal** del checklist: *"una tabla está en 1FN si satisface las siguientes cinco condiciones: 1. No hay orden de arriba-a-abajo en las filas. 2. No hay orden de izquierda-a-derecha en las columnas. 3. No hay filas duplicadas. 4. Cada intersección de fila-y-columna contiene exactamente un valor del dominio aplicable y nada más. 5. Todas las columnas son regulares, es decir, las filas no tienen componentes como IDs de fila, IDs de objeto, o timestamps ocultos"*. Y remata con la intención histórica: *"la primera forma normal se definió para prohibir los atributos multivaluados, compuestos y sus combinaciones"*.
>
> **Por qué importa:** las condiciones 1 y 2 (sin orden) parecen raras, pero tienen una razón técnica: el modelo relacional es un **conjunto de tuplas**, no una lista. Si el motor te devolviera las filas en un orden fijo, ese orden se volvería un dato implícito que no podrías usar por error. La condición 5 es la más moderna: una columna `id_fila` o un `timestamp` de inserción son metadatos que el modelo relacional clásico no contempla, y por eso una tabla con esas columnas "no es regular".
>
> **Ejemplo:** el caso de la condición 3 en la vida real es una tabla `ALUMNO` importada del Excel donde el mismo alumno aparece dos veces porque alguien lo agregó dos veces. Con la PK `(cédula, código_materia)` no puede pasar: el motor rechaza el duplicado. La 1FN protege tu modelo de un error de carga, no solo de un error de diseño.

### 3️⃣ Violación de la 1FN

> [!note] 📋 Definición — Violación
>
> Una tabla **no está en 1FN** si incumple cualquiera de las 5 condiciones. La PK (clave primaria) no salva a una tabla que tiene grupos repetitivos.
>
> **Ejemplo:** `productos = "arroz, leche, pan"` en una sola celda viola la condición 4. No puedes filtrar por "arroz" sin leer toda la celda.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-16-graph.svg]]
>
> **Se lee así:** el diagrama tiene una **caja de partida y tres salidas**, y esa estructura es lo que hay que entender: la misma tabla rota (`CLIENTE` con `telefono1, telefono2, telefono3`) produce tres consecuencias distintas. (1) **La violación**, en rojo: *"una celda guarda '2345, 2654' → viola la 1FN, condición 4: un valor por celda"*. (2) **La consecuencia operativa**: *"no se puede filtrar por un solo teléfono"*. (3) **El remedio**, en verde: *"TELEFONO(cedula FK, numero), una fila por teléfono"*.
>
> **Por qué importa:** la salida (2) es la que conecta la definición con la vida real. La 1FN no es un capricho académico: es lo que permite que un `WHERE telefono = '2345'` devuelva exactamente lo que esperas. Con la lista en una celda, esa consulta devuelve filas enteras y tú tienes que filtrar el texto a mano. La condición 4 existe **por una razón de uso**.
>
> **Ejemplo:** el `SELECT` que sí funciona con la tabla normalizada es `SELECT * FROM TELEFONO WHERE numero = '2345'`. Con la tabla rota, el motor te devuelve la fila completa del cliente y tú tienes que buscar dentro de una lista de texto para saber si ese teléfono estaba. La base de datos no puede indexar ni comparar una lista de texto; por eso el modelo relacional la prohíbe.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-15-er.svg]]
>
> **Se lee así:** el diagrama es un ERD de **una sola entidad** (`CLIENTE`) donde cada columna lleva **el comentario de la especificación** al lado. `cedula int PK "mayor que 0, unico. Identifica al cliente"`, `nombre string "varchar(50), no vacio. Nombre completo"`, `direccion string "varchar(100). Direccion de facturacion"`, `telefono string "varchar(15), 7 a 15 digitos. Contacto principal"`.
>
> **Por qué importa:** ese comentario **es** el diccionario de datos, dibujado. Fíjate en que cada columna responde a las tres preguntas de la definición: **tipo** (`int`, `varchar(50)`), **dominio** (mayor que 0 y único / no vacío / 7 a 15 dígitos) y **descripción** (qué representa). El diccionario de datos no es un documento aparte y redundante: es la especificación de cada campo, y el diagrama es una forma compacta de verla.
>
> **Ejemplo:** `telefono varchar(15) "7 a 15 digitos. Contacto principal"` dice algo que el tipo solo no dice. `varchar(15)` permite 15 caracteres cualesquiera; el dominio "7 a 15 dígitos" es lo que la vuelve un teléfono. En SQL eso se escribe como `CHECK (telefono REGEXP '^[0-9]{7,15}$')`. El comentario del diagrama es el requisito; el `CHECK` es su traducción.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-17-er.svg]]
>
> **Se lee así:** el diagrama es **el mismo par `CLIENTE` / `TELEFONO` del ejemplo de arriba**, pero con la relación rotulada simplemente `tiene`. Compáralo con la versión anterior: ahí la etiqueta decía *"un telefono por fila"*; aquí dice `tiene`. Las dos son correctas, pero responder con la segunda es más fácil de leer en un ERD real.
>
> **Por qué importa:** la diferencia entre "dibujar bien" y "dibujar rápido" está en la relación. Cuando la relación se llama `tiene`, un lector nuevo no sabe si es 1:1 o 1:N sin mirar los símbolos. Cuando se llama *"un teléfono por fila"*, la cardinalidad **ya está en el nombre** y el diagrama se documenta solo. Es la misma idea que aplica al diccionario de datos: el nombre del elemento es su primera línea de documentación.
>
> **Ejemplo:** si el diagrama de tu proyecto dice `CLIENTE ||--o{ TELEFONO : tiene`, y en la entrega te piden "explique las cardinalidades", tienes que abrir la etiqueta y leer los símbolos. Si en cambio dice `CLIENTE ||--o{ TELEFONO : "un telefono por fila"`, la explicación está escrita. Ninguno es incorrecto; el segundo te ahorra la mitad de la defensa oral.

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

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Distingo una relación 1:1, 1:M y M:N solo con leerla en voz alta.
> - [ ] Sé en qué lado va la FK en cada cardinalidad.
> - [ ] Identifico cuándo una relación necesita tabla intermedia.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Convierto un ERD completo a modelo lógico aplicando las reglas de cardinalidad.
> - [ ] Detecto relaciones recursivas y supertipo-subtipo y elijo su traducción.
> - [ ] Hago la conversión inversa (del modelo lógico al conceptual) sin perder información.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Justifico por qué una 1:1 total-total se fusiona y cuándo no.
> - [ ] Reviso el esquema resultante y cuento tablas para detectar las que sobran.

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
>
> - ¿Objetivo de la 1FN?::Tablas fieles a una relación, sin grupos repetitivos.
> - ¿5 condiciones 1FN?::Filas sin orden, columnas sin orden, sin duplicadas, un valor por celda, columnas regulares.
> - ¿Qué mide cada FN?::Vulnerabilidad a inconsistencias: 1FN grupos repetitivos, 2FN dependencias parciales, 3FN transitivas.
> - ¿Diccionario de datos y sus 4 columnas?::Describe cada tabla: atributo, tipo de dato, dominio, descripción.

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

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[01 - Conversión MC a ML por cardinalidad]] — de dónde sale el esquema que hay que documentar.
> - [[03 - Segunda y tercera forma normal]] — el siguiente escalón: 2FN y 3FN.
> - [[04 - Normalización paso a paso]] — el protocolo completo, paso a paso.
> - [[../Unidad 1 - Modelos de Datos y ER/Guía de Problemas 1 - MC, ML y Normalización|Guía de Problemas 1]] — el caso de las recetas de farmacia, resuelto con este método.

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
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
