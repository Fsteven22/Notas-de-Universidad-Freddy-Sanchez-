---
dg-publish: true
tags: [TICG1018, unidad1, datos, modelos, historia]
---

# 💾 Dato, Información y Modelos de Datos

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Modelar Antes de Guardar?
>
> Todo sistema que uses — Aula Virtual, banca móvil, el inventario de una tienda — vive sobre un modelo decidido antes de escribir código. Equivocarse ahí cuesta reescrituras (los egipcios en papiros del 2000 a.C. ya registraban; el medio cambió, el costo de no modelar no). Esta nota responde qué se guarda, cómo se organiza y cómo evolucionó esa respuesta en 60 años.
>
> **¿Dónde se usa?**
> - **Diseño de BD:** todo sistema (notas 02-03, proyecto del curso).
> - **Migraciones:** pasar de Excel/archivos a tablas sin perder nada.
> - **Lección 1 (13-oct):** dato vs información + archivos vs BD, seguro evaluado.
> 
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-01-graph.svg]]
>
> **Se lee así:** el diagrama es una bifurcación, y la pregunta que decide es única: *¿el dato tiene contexto y estructura?*. Si **no**, caes en la rama de archivos sueltos, y de ahí solo pueden salir tres cosas: redundancia, inconsistencia y programas a medida. Si **sí**, caes en la rama del modelo de datos, y de ahí salen las tres cosas buenas: estructura con relaciones, restricciones que se imponen solas e información confiable.
>
> **Por qué importa:** fíjate en que los dos lados terminan con **tres** resultados. No es que los archivos "tengan menos problemas": es que los tres problemas de la izquierda son la causa directa de los tres de la derecha. Si entiendes esa cadena, ya no necesitas memorizar la definición de base de datos: entiendes por qué existe.

---

## 📋 Definiciones Formales

### 1️⃣ Dato — el valor crudo

> [!note] 📋 Definición — Dato
>
> Valor crudo sin contexto. Por sí solo no dice nada ni permite decidir.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-02-graph.svg]]
>
> **Ejemplos:** `"19"`, `"Irene"`, `"2026-10-13"`. ¿19 qué? Sin contexto es solo un símbolo guardado.

### 2️⃣ Información — el dato con contexto

> [!note] 📋 Definición — Información
>
> Dato interpretado en un contexto que permite decidir o actuar.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-03-graph.svg]]
>
> **Ejemplo:** *"19 estudiantes aprobaron SBD"* — ahora sí hay decisión posible (¿festejar? ¿reforzar?). El modelo de datos existe para producir información, no para acumular datos.

### 3️⃣ Modelo de datos — el plano antes de guardar

> [!note] 📋 Definición — Modelo de datos
>
> Representación lógica y estructurada que define estructura, relaciones, restricciones y transformaciones. Es iterativo y es el lenguaje común entre cliente, analista y dev.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-04-graph.svg]]
>
> **Por qué importa (diapositivas):** cubre requerimientos desde el diseño; minimiza cambios continuos, redundancia y problemas de acceso; sin buen diseño no hay hardware ni UI que salve el desempeño.
>
> **Ejemplo:** tabla ESTUDIANTE con PK `carnet` — el modelo decidió qué se guarda y cómo se conecta antes de escribir una línea de código.

### 4️⃣ Archivos vs Base de datos — por qué modelar gana

> [!note] 📋 Definición — Sistema de archivos vs base de datos
>
> | Aspecto | Archivos Tradicionales | Base de Datos |
> |---|---|---|
> | **Redundancia** | Mismo dato en N archivos | Definido una vez |
> | **Consistencia** | Se desincroniza | Restricciones la garantizan |
> | **Acceso** | Programas a medida | Lenguaje común (SQL) |
> | **Escala** | Colapsa con usuarios | Concurrente y segura |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-05-graph.svg]]
>
> **Historia real:** egipcios en papiros (2000 a.C.) — el medio cambia, la necesidad de registrar no. Los archivos repiten el problema del papiro (copias que se desincronizan); la BD lo resuelve con unicidad + restricciones.

> [!info] 📖 El deck de cátedra: por qué existieron los SBD (slides01, pp. 4-11)
>
> El deck del Ing. Jorge Magallanes abre el curso explicando el problema que las bases de datos resolvieron. Estas son sus figuras literales.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s01-p4.png]]
>
> **Se lee así:** la lámina (p. 4) es el **título del problema**: *"Sistemas basados en archivos — procesamiento de datos y limitaciones"*. No explica nada todavía; solo planta la bandera del tema que ocupa el resto del bloque. La palabra clave es *procesamiento*: en los años 60-70 la computadora no guardaba datos, los **procesaba**; guardar era el peaje, no el objetivo.
>
> **Por qué importa:** entender el marco te dice qué esperar del deck. No viene a enseñar SQL: viene a justificar por qué hace falta un negocio de datos. Si en un parcial te preguntan *"¿cuál fue el problema original??"*, la respuesta es esta lámina.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s01-p6.png]]
>
> **Se lee así:** esta es la lámina que **más se estudia** del bloque, porque destila las limitaciones del enfoque de archivos en cinco puntos. Léelos como una lista de síntomas de una empresa real: (1) **dependencia de los datos** — la definición del dato vive *dentro* del programa, así que cambiar la estructura obliga a reprogramar; (2) **búsquedas complejas difíciles** — para cualquier consulta nueva necesitas tocar los archivos de catálogo; (3) **redundancia** — cada departamento guarda su propia copia; (4) **pérdida de integridad** — al actualizar en varios archivos se desincronizan; (5) **consultas fijas y proliferación de aplicaciones** — cada pregunta nueva es un programa nuevo.
>
> **Se lee así (traducción):** la raíz común de los cinco es que **no hay un lugar único donde viva la definición del dato**. Todo lo demás se deriva de ahí. El DBMS se crea exactamente para eso: un catálogo central con la definición, y programas que ya no la llevan dentro.
>
> **Ejemplo:** la secretaría de la carrera guarda "archivos de estudiantes" en el registro de matrícula y en el de pagos. La misma persona está en dos sitios: si cambias tu dirección en uno, el otro queda desactualizado. Eso es el punto 4 (*pérdida de integridad*) y el punto 3 (*redundancia*) al mismo tiempo.

> [!note] 📖 Del archivo al DBMS: el salto del deck (slides01, pp. 8-11)
>
> *"Un sistema de bases de datos se define como un conjunto de programas de aplicación que acceden a la base de datos a través de un sistema de gestión de bases de datos (DBMS)"* (p. 8). El **DBMS** (p. 9) es el conjunto de programas que permite definir, crear, mantener y controlar el acceso a los datos.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s01-p13.png]]
>
> **Se lee así:** la lámina (p. 13) dibuja la **arquitectura de 2 capas** como un recorrido de la petición. El cliente (MySQL Workbench) abre una conexión TCP-IP al servidor — la lámina incluso da los datos reales: host `128.169.1.27`, puerto `3306` — y pide datos con **SQL**. El servidor, que tiene el DBMS, valida, accede y devuelve el conjunto de datos. Lo importante es dónde cae cada responsabilidad: la **primera capa** (el cliente) lleva GUI + lógica del negocio + lógica de datos; la **segunda** (el servidor) lleva validación + acceso.
>
> **Por qué importa:** el punto que se evalúa es que **el SQL viaja, los datos no**. La consulta es texto que se manda por la red; el motor la ejecuta donde están los datos. Por eso el mismo SQL sirve para 3 personas conectadas a la vez, y por eso el acceso se puede auditar en un solo punto.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s01-p14.png]]
>
> **Se lee así:** la misma idea, pero con **una capa más** (p. 14). Ahora el servidor de aplicaciones se separa del servidor de base de datos: capa 1 = GUI, capa 2 = lógica de negocio y de procesamiento, capa 3 = validación y acceso a datos. Y fíjate en la diferencia fina: **la conexión TCP ahora se establece desde el servidor de aplicaciones hacia el de bases de datos**, no desde el escritorio del usuario.
>
> **Por qué importa:** esa diferencia es toda la diferencia entre 2 y 3 capas, y es la que hace posible lo que hoy llamamos *"la web"*. En 2 capas, si el cliente es un navegador, expones el servidor de base de datos a internet. En 3 capas, el navegador solo habla con el servidor de aplicaciones y **nadie** alcanza la base de datos directamente.
>
> **Ejemplo:** MySQL Workbench hablando con `128.169.1.27:3306` es 2 capas. Una app web de la ESPOL que consulta la base del portal es 3 capas: el navegador pide al servidor de aplicaciones, y ese servidor es el único que habla con el DBMS.

> [!tip] 📖 El proceso de diseño, según el deck (slides01, pp. 15-18)
>
> *"La información es el activo más importante de las organizaciones"* (p. 16) — por eso el diseño de la base es un proceso formal y no una ocurrencia.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s01-p17.png]]
>
> **Se lee así:** la lámina (p. 17) da la definición formal y, más importante, los **tres niveles de abstracción** que ordenan toda la materia. El **conceptual** sirve para entender el dominio del negocio (entidades y relaciones, sin importar el motor); el **lógico** ya habla de tablas, registros y restricciones de integridad, pero todavía independiente del DBMS; el **físico** ya depende del motor: espacios de tablas, estructuras de almacenamiento y de acceso.
>
> **Por qué importa:** estos tres niveles son el mapa de la unidad. La Unidad 1 es el nivel **conceptual** y el **relacional**; la Unidad 2 es el **lógico** (convertir el conceptual en tablas y normalizarlas); la Unidad 4 toca lo **físico** (índices, almacenamiento). Cuando una pregunta te sobre, pregúntate en qué nivel está y la respuesta se ordena sola.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Modelos-ER/bd-s01-p18.png]]
>
> **Se lee así:** la lámina (p. 18) es el **mapa completo del proceso de diseño**, y la lectura correcta es por columnas: la de la izquierda son los **niveles**, la del medio las **etapas**, la de la derecha las **tareas**. Recorre la primera fila de arriba abajo: *determinar vistas de usuario y requerimientos → definir entidades, relaciones, atributos y dominios → verificar el modelo → definir tablas, columnas y restricciones → normalizar → verificar los requerimientos → definir índices y almacenamiento → definir usuarios y control de acceso → establecer parámetros de ejecución*. La columna de las tareas es la que te dice qué dominio de las siguientes unidades corresponde a cada paso.
>
> **Por qué importa:** fíjate en que **"verificar" aparece dos veces**: una después de definir el modelo y otra después de normalizar. El proceso no es una flecha recta, es un ciclo con dos puntos de control. Ese matiz es lo que separa un diseño serio de uno que "funciona pero se rompe".
>
> **Ejemplo:** la fila "definir entidades, relaciones, atributos y dominios" es literalmente la Unidad 1. La fila "definir tablas, columnas y restricciones → normalizar tablas" es la Unidad 2. La fila "definir índices y organización de almacenamiento" es SQL Avanzado. Cuando te pidan en el examen "definir las etapas del proceso de diseño", esta tabla es la respuesta, y el diagrama de flujo del principio de la nota es la versión resumida.

---

## 🧵 Evolución de los Modelos (Coronel cap. 2)

> [!note] 📋 Un Modelo por Época
>
> | Generación | Época | Modelo | Idea |
> |---|---|---|---|
> | Archivos | 1960s-70s | VSAM, planos | Registros, no relaciones |
> | Segunda | 1970s | **Jerárquico** (IMS, Apollo 1969) | Árbol invertido: un padre, N hijos |
> | Segunda | 1970s | **Red** (ADABAS, IDS-II) | Grafo multipadre + schema/subschema/DML/DDL |
> | Tercera | 1970s-hoy | **Relacional** (Codd 1970) | Tablas + SQL declarativo |
> | Tercera | 1976-hoy | **ER** (Chen) | El plano gráfico del relacional |
> | Cuarta | 1980s-hoy | **OO / Objeto-Relacional** | Objetos con métodos; tipos extensibles |
> | Siguiente | Hoy-futuro | **XML, híbridas, nube** | No estructurado + servicios |
>

### 🔍 Cada generación, dibujada

> [!example] 🧪 Ver los 4 modelos clave
>
> **Jerárquico (un padre, N hijos):** lo compartido se duplica.
>
> Historia: *Ana trabaja en las direcciones Norte y Sur. Como cada hijo tiene un solo padre, su ficha debe copiarse bajo cada dirección.*
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-06-graph.svg]]
>
> **Se lee así:** `dup` = duplicado por obligación del modelo. Cambia el teléfono de Ana y debes cambiarlo en 2 fichas o mienten (redundancia + inconsistencia, los 2 males de archivos).
>
> **Red (multipadre):** grafo con schema/subschema; murió por falta de consultas ad hoc.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-07-graph.svg]]
>
> **Relacional (Codd 1970):** tablas + SQL declarativo + independencia física.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-08-er.svg]]
>
> **ER (Chen 1976):** el plano gráfico del relacional — rectángulos, rombos y óvalos antes de crear tablas.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-09-graph.svg]]
>
> **Se lee así:** el mismo EMPLEADO–PROYECTO del relacional, pero en Chen puro: todavía no hay tablas ni FK, solo qué existe y cómo se conecta.
>
> **Detalles que evalúan:** el jerárquico duplica lo compartido; la red murió por falta de consultas ad hoc; Codd publicó en CACM (junio 1970); M:N existe en conceptual pero no va al relacional.
>

---

## 🛠️ Método: Del Enunciado al Modelo

> [!note] 📋 Procedimiento General
>
> 1. Subraya sustantivos (candidatos a entidad) y verbos (candidatos a relación).
> 2. Pregunta por cada tabla futura: "¿qué decisión se toma con esto?" (sin pregunta, no hay tabla).
> 3. Dibuja ERD con claves desde el día 1.
> 4. Traduce a tablas y verifica con las reglas de negocio.
> 5. Itera: el modelo se refina, no nace perfecto.
>
> **Principio clave:** modela lo permanente (Estudiantes, Materias), no los formularios — las pantallas cambian, el negocio no.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-10-flow.svg]]
>
> **Se lee así:** el diagrama es el método de los 5 pasos, dibujado como una decisión y no como una lista. La diferencia con la lista numerada está en la **tercera caja**: *"¿qué decisión se toma con esta tabla futura?"*. Si la respuesta es **ninguna**, el diagrama te devuelve al principio con un *"sobra la tabla"*. Esa pregunta es un **filtro**, no un paso: puede matar tu modelo antes de que lo dibujes.
>
> **Por qué importa:** es la diferencia entre modelar y collectionar. Un modelo con diez tablas donde nueve no alimentan ninguna decisión es un modelo de archivos con nombres más bonitos. El filtro te obliga a justificar cada tabla con algo que alguien realmente va a preguntar.
>
> **Ejemplo:** en el mini-caso de la sección siguiente, la tabla `MATRICULA` sobrevive porque responde a *"¿qué nota tiene cada estudiante en cada materia?"*. La tabla `HORARIO` sobraría: nadie decide nada con ella.

---

## 🎨 Ejemplo Trabajado

> [!example] 🟢 Mini-caso SBD
>
> Enunciado: *"Irene dicta SBD1; cada estudiante toma varias materias."*
>
> | Paso | Resultado |
> |---|---|
> | Sustantivos | Irene→PROFESOR, SBD1→MATERIA, estudiante→ESTUDIANTE |
> | Verbos | *dicta*, *toma* |
> | Claves | carnet, código |
> | Clasificación | PROFESOR–MATERIA 1:M; ESTUDIANTE–MATERIA M:N (pide intermedia) |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-11-graph.svg]]
>
> **Se lee así (Chen puro, sin tablas todavía):** Irene (PROFESOR) *dicta* SBD1; cada estudiante *toma* varias materias. La M:N *toma* pedirá una intermedia al traducir (Unidad 2), pero en el conceptual solo existe el rombo.

---

## 🗂️ ¿Cuándo Bastan Archivos?

> [!note] 📋 La excepción que confirma la regla
>
> Solo para datos de usar y tirar: logs simples de una app, cachés temporales, exportaciones de un solo uso. En cuanto haya 2 usuarios, reportes repetidos o decisiones encima → modela.
>
> | Señal | Archivos bastan | Pide BD |
> |---|---|---|
> | **Usuarios** | 1 | Varios concurrentes |
> | **Preguntas** | Siempre las mismas 2 | Nuevas cada semana |
> | **Vida del dato** | Horas/días | Meses/años |

---

## ⚠️ Errores Comunes y Principios Lógicos

### ❌ Error 1: Modelar pantallas, no el negocio

> [!danger] ❌ Viola: permanencia del modelo
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-12-graph.svg]]
>
> Al cambiar la UI muere la BD. Modela entidades permanentes: las pantallas cambian, el negocio no.

### ❌ Error 2: Tabla sin pregunta

> [!danger] ❌ Viola: toda tabla responde una decisión
>
> Si ningún reporte ni decisión usa la tabla, sobra (todavía). Pregunta por cada tabla futura: *"¿qué decisión se toma con esto?"*. Sin respuesta → no la crees.

### ❌ Error 3: Confundir dato con información

> [!danger] ❌ Viola: contexto antes que almacenamiento
>
> Guardar todo sin contexto es archivar, no diseñar. `19` solo es información cuando sabes que son *"19 estudiantes que aprobaron SBD"* — el modelo captura ese contexto en estructura + restricciones.

### ❌ Error 4: Saltarse el ERD

> [!danger] ❌ Viola: orden obligatorio ERD → tablas → SQL
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-13-graph.svg]]
>
> Ir directo a tablas garantiza N:M olvidadas y FKs inventadas.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Dato, información o modelo

> [!example] 📋 Planteamiento
>
> Clasifica:
> - (a) `"19"`,
> - (b) *"19 estudiantes aprobaron SBD"*,
> - (c) tabla ESTUDIANTE con PK `carnet`.
>
> > [!success]- ✅ Solución
> >
> > (a) Dato: sin contexto. 
> > (b) Información: dato + contexto que permite decidir. 
> > (c) Modelo: estructura que produce información de forma repetible.

### ✏️ Ejercicio 2 — ¿Archivos o BD?

> [!example] 📋 Planteamiento
>
> - Caso A: app de 1 usuario con 2 reportes fijos y datos de una semana.
> - Caso B: matrícula multiusuario con reportes nuevos cada mes. ¿Qué pide cada uno y por qué?
>
> > [!success]- ✅ Solución
> >
> > A: archivos bastan (1 usuario, preguntas fijas, vida corta). 
> > B: BD modelada (concurrencia, preguntas cambiantes, decisiones encima). 
> > Regla: 2+ usuarios o reportes nuevos → modela.

### ✏️ Ejercicio 3 — Ordena las generaciones

> [!example] 📋 Planteamiento
>
> Ordena (jerárquico, red, relacional, archivos) y explica con 1 línea por qué la red murió aunque era más flexible que el jerárquico.
>
> - Pista 1: el orden es cronológico (60s → 70s).
> - Pista 2: la red pedía programas a medida para preguntar.
> - Pista 3: el relacional trajo SQL declarativo.
>
> > [!success]- ✅ Solución
> >
> > Archivos → jerárquico → red → relacional. 
> > La red murió por falta de consultas ad hoc: potente pero solo accesible con programas a medida; el SQL declarativo del relacional la volvió obsoleta.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino dato, información y modelo sin mirar.
> - [ ] Explico archivos vs BD con 3 diferencias y 1 ejemplo propio.
> - [ ] Ubico los 6 modelos en su generación con un ejemplo cada uno.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico el método de 5 pasos a un enunciado nuevo.
> - [ ] Justifico por qué ganó el relacional (SQL + independencia).
> - [ ] Detecto qué modelo pide un caso dado.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - Diapositivas BD01 (Irene Cheung) + `BD01 Introducción_datamodel.pdf`.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 2 §§2.5.1–2.5.7.

---

## 🔁 Repaso SR (flashcards)

#flashcards/bd-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
> 
> - ¿Dato vs información?::Valor crudo sin contexto vs dato interpretado en contexto.
> - ¿Tres problemas de archivos tradicionales?::Redundancia, inconsistencia y programas a medida.
> - ¿Modelo jerárquico en 1 línea?::Árbol invertido: un padre, N hijos (solo un padre por hijo).
> - ¿Qué aportó la red y por qué murió?::Multipadre + schema/subschema/DML/DDL; murió por falta de consultas ad hoc.
> - ¿Codd, año y aporte?::1970: tablas + SQL declarativo e independencia física.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[02 - Entidades, atributos, claves y relaciones]] — el vocabulario para dibujar lo de aquí.
> - Ver también [[03 - Modelo relacional, ERM y casos Tiny College]] para la traducción a tablas.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]] · Índice: [[../Sistema de Bases de Datos|Sistema de Bases de Datos]]
> - Siguiente: [[02 - Entidades, atributos, claves y relaciones]]
> - Conversión a tablas: [[01 - Conversión MC a ML por cardinalidad]]
> - Syllabus: [[../Bienvenida y Syllabus Sistema de Bases de Datos|Bienvenida y Syllabus Sistema de Bases de Datos]]

---

**Tags:** #TICG1018 #unidad1 #datos #modelos #bd
