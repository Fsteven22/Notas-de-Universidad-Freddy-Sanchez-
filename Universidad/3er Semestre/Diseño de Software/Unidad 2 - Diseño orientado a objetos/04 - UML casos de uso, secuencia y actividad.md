---
dg-publish: true
tags: [CCPG1042, unidad2, uml, casos-de-uso, secuencia]
---

# 🎬 UML Comportamiento: Casos de Uso, Secuencia y Actividad

## 🎯 Introducción

> [!info] 💡 ¿Por Qué el Diagrama de Clases no Basta?
>
> Las clases muestran la **foto** (estructura); los diagramas de comportamiento muestran la **película** (qué pasa en el tiempo). Un sistema con clases perfectas pero sin flujos definidos falla en la primera historia de usuario — y el docente lo evalúa en S4-S5 tal cual.
>
> **Importancia histórica:** los casos de uso nacieron con Ivar Jacobson (uno de "los tres amigos" de UML) para capturar requisitos desde la perspectiva del usuario, no del programador. Los diagramas de secuencia vienen del mundo de telecomunicaciones (diagramas de traza de mensajes).
>
> **Relevancia actual:** historias de usuario ágiles, contratos de API y pruebas de aceptación viven de estos diagramas, aunque se dibujen en pizarras y no en herramientas formales.
>
> **Analogía del mundo real:** piensa en una receta:
>
> - **Clases** → Ingredientes en la despensa (qué hay).
> - **Casos de uso** → Platos del menú (qué quiere el cliente).
> - **Secuencia** → Paso a paso con tiempos (quién hace qué y cuándo).
> - **Actividad** → Diagrama de flujo de la cocina (decisiones y paralelos).
>
> | Diagrama | Pregunta que responde | Cuándo dibujarlo |
> |---|---|---|
> | **Casos de uso** | ¿Qué quiere lograr cada actor? | Al inicio, con el cliente |
> | **Secuencia** | ¿Quién llama a quién y en qué orden? | Antes de codear un flujo clave |
> | **Actividad** | ¿Qué decisiones y caminos hay? | Procesos con ramas/paralelo |

![[../Diagramas/dsw-u2-05-01-seq.svg]]

---

## 🧵 Los Tres Diagramas (Stevens caps. 7-11)

### 🎭 1. Casos de Uso: el Menú del Sistema

> [!note] 📋 Definición — Actor + Objetivo, Nada Más
>
> - **Actor** = rol externo (Estudiante, Docente, SistemaPagos), no persona concreta.
> - **Caso** = objetivo con valor observable: produce un resultado que el actor puede percibir ("Inscribirse", no "Clic en botón").
> - **Frontera del sistema** = el rectángulo que encierra los óvalos: DENTRO queda solo lo que construyes; FUERA quedan los actores (humanos o sistemas existentes). Con vacíos dentro/disqués fuera, el diagrama mentiría.
> - **Caso vs escenario:** el caso de uso es la **familia de caminos completos** hacia el valor; un **escenario es UN camino concreto** por dentro (el feliz de la descripción ch. 8 y cada alterno A1, A2...).
> - **`<<include>>`** = subrutina SIEMPRE ejecutada: la flecha nace **del caso base** y llega al incluido (Validar identidad).
> - **`<<extend>>`** = parche OPCIONAL: la flecha nace **del extendido** y llega **al caso base** (Aplicar descuento). La flecha puede anotar el **punto de extensión**: dónde y cuándo entra (ej. "en paso 4, cuando hay inconsistencia").
> - **Generalización** entre actores (y también entre casos) = "es-un" con triángulo hueco: `Observador ──▷ Ciudadano` — hace todo lo del ciudadano y algo más. Evita el actor vacío que "no sabe qué hacer".
>
> | Bien | Mal | Por qué |
> |---|---|---|
> | `Inscribirse a curso` | `Ingresar carnet` | El segundo es un paso, no un objetivo |
> | `Generar reporte` | `Conectarse a BD` | El segundo es interno, invisible al actor |
>
> **Test:** si el actor no lo pediría en voz alta, no es caso de uso.
>
> **Mnemotecnia de los sentidos:** *include* lo canta el base ("yo siempre llamo a validar"); *extend* lo canta el extra ("yo interrumpo si pasa algo").

![[../Diagramas/dsw-u2-04-04-flow.svg]]

### 📝 2. Descripción Textual del Caso de Uso (Stevens ch. 8)

> [!info] ℹ️ El formato de papel
>
> El diagrama ch. 7 señala los óvalos; la **especificación textual** ch. 8 es lo que se escribe debajo: convive en el Control03 (en papel, junto a Apéndice 1 de Pressman que repite lo mismo con menos detalle).

> [!example] 💡 Plantilla resuelta: `Inscribirse a curso`
>
> | Campo | Contenido |
> |---|---|
> | **Actor principal** | Estudiante |
> | **Precondiciones** | Estudiante autenticado; matrícula activa |
> | **Postcondición de éxito** | Existe una matrícula; el cupo del curso quedó en −1 |
> | **Escenario principal** | 1. Estudiante elige curso. 2. Sistema verifica prerrequisitos. 3. Sistema verifica cupo > 0. 4. Sistema crea matrícula. 5. Sistema confirma. |
> | **Flujo alternativo A1** | (en paso 3) **Curso sin cupo** → sistema ofrece lista de espera → si acepta, entra; si no, fin. |
> | **Flujo alternativo A2** | (en paso 2) **Prerrequisito no visto** → sistema avisa y rechaza; no queda matrícula. |
>
> **Reglas que suman puntos:**
>
> - Cada paso arranca con **actor** o **sistema** explícito y termina en un estado observable.
> - El escenario principal es recto: cualquier rama exigidora es un **flujo aparte** (A1, A2...) que numera desde qué paso se desvió.
> - La precondición es el estado requerido ANTES; la postcondición, el estado garantizado DESPUÉS — estados, no acciones.
> - Los flujos alternativos conectan con los `alt` de secuencia y con los `<<extend>>` del diagrama: son el mismo material en tres niveles.
>
> - **El escenario es una instancia concreta del caso: un recorrido, con datos, sin ramificaciones.** Dos actas de la misma JRV en la misma jornada son DOS escenarios de `Registrar acta de escrutinio`.

> [!example] 🏛️ Ejemplo de la clase: `Registrar acta de escrutinio` (SIEL)
>
> | Campo | Contenido |
> |---|---|
> | **Actor principal** | Presidente de JRV |
> | **Precondiciones** | La JRV está abierta y el presidente autenticado |
> | **Escenario principal** | 1. Presidente selecciona su JRV. 2. Sistema muestra candidaturas por dignidad. 3. Presidente ingresa votos por candidatura, nulos y blancos. 4. Sistema valida el acta contra el padrón de la junta. 5. Sistema registra el acta y emite comprobante. |
> | **Flujo alternativo A1** | (en paso 4) **Los votos superan a los electores del padrón** → el acta se envía a revisión. |
> | **Flujo alternativo A2** | (en paso 3) **El presidente cancela** → no se guarda nada. |
> | **Postcondición** | El acta queda registrada o en revisión |
>
> **Dos escenarios concretos:**
>
> - 🟢 **Escenario 1:** en la JRV 12 de Tarqui, el presidente registra 180 A, 95 B, 10 nulos y 5 blancos; el padrón tiene 320 → **acta registrada**.
> - 🔴 **Escenario 2:** la suma da 340 y el padrón 320 → **acta enviada a revisión** (el extend A1 se activó).

> [!example] 📖 El ejercicio del deck: "Registrarse en un paralelo" (pp. 6-7)
>
> El docente usa el sistema **AcademicChoice** (inscripción de materias y paralelos) como ejercicio de papel. El formato que pide es exactamente el de tu Control03:
>
> | Campo | Qué pide el deck |
> |---|---|
> | **Actores** | principales **y** secundarios |
> | **Precondiciones** | estado exigido antes |
> | **Flujo de eventos** | principal + alternativos, numerados |
> | **Postcondiciones** | resultado garantizado |
>
> Y el caso de uso a trabajar es **`Registrarse en un paralelo`**, con **al menos 2 refinamientos** de cada tipo (`<<include>>` y `<<extend>>`) y **2 escenarios** descritos.
>
> > [!tip] Traducción directa al SIEL
> > `Registrarse en un paralelo` ≈ `Inscribir candidatura`: mismo esqueleto (actor + precondición + flujo + postcondición). Los refinamientos del deck te dan la plantilla: **1 `include`** para la validación que siempre ocurre y **1 `extend`** para el parche opcional.

### 🎭 3. Secuencia: Quién Llama a Quién

> [!example] 🧪 Leer de Arriba Abajo
>
> - Eje vertical = tiempo (arriba primero).
> - Flecha sólida = llamada; punteada = retorno.
> - Cuadro `alt` = decisión; `loop` = repetición.
> - La vida del objeto (línea) nace y muere: crea tarde, destruye pronto.
>
> **Mapeo directo a código:** cada flecha entre objetos será una llamada a método. Si tu secuencia tiene 20 flechas cruzadas, tu diseño grita "acoplamiento alto" (ver U1-02).

#### 📚 El deck de cátedra: cómo se dibuja de verdad (pp. 32-44)

> [!info] 📖 De dónde sale esta sección
> Del deck `04aLenguajeUnificadoModelado.pdf` (Unidad 2, 2024): la parte de secuencia es la más extensa del deck y define la notación con precisión.

**Qué demuestra un diagrama de secuencia** (p. 32): el **comportamiento de los objetos en un caso de uso**, describiendo los objetos y los mensajes que transmiten. Se lee **de izquierda a derecha** y **de forma descendente** — el tiempo corre hacia abajo.

**Los elementos** (pp. 32-33): objetos sobre su **life-line**, la **activation** (el objeto activo, la barra vertical sobre la lifeline), los **messages** (las flechas) y el **destroy** (la X al final de la lifeline).

![[Archivos/04a-p33-elementos-secuencia.png]]

**Frames: `alt`, `opt`, `loop`** (pp. 38-41). El deck explica por qué existen: lo que dibujas al principio es una **instancia** del diagrama de interacción, *una posible* secuencia de mensajes. Pero un caso de uso puede incluir muchos escenarios → hace falta mostrar **comportamiento condicional** y **posibles iteraciones**. Un diagrama de interacción **genérico** muestra todas las secuencias posibles.

> | Frame | Qué ejecuta | Equivalencia / regla |
> |---|---|---|
> | **`alt`** | fragmento alternativo múltiple | **solo se ejecuta el que cuya condición (guard) sea verdadera** |
> | **`opt`** | fragmento opcional | se ejecuta solo si la condición se cumple: **equivale a un `alt` con una sola traza** |
> | **`loop`** | fragmento que puede ejecutarse **múltiples veces** | la **guard indica la base de las iteraciones** |

![[Archivos/04a-p39-alt.png]]

![[Archivos/04a-p40-opt.png]]

> [!tip] Cómo se usa en tu entrega
> `alt` para el flujo alternativo de la descripción (A1, A2), `opt` cuando el bloque es opcional (un parche `<<extend>>`), `loop` para lo que se repite (reintentar, recorrer una lista). La **guard** es la condición entre corchetes: `[cupo > 0]`, `[hay errores]`.

**Restricciones de tiempo** (p. 43): el deck muestra cómo anotar una restricción de tipo `time` sobre un mensaje, para cuando el orden no basta y necesitas el plazo.

![[Archivos/04a-p43-restricciones-tiempo.png]]

**Tipos de interacción** (p. 44): el deck distingue los mensajes **síncrono**, **asíncrono** y de **retorno**, y el mensaje tipo *choice* (la bifurcación). El aviso del propio deck: *algunas versiones de UML usan el mismo símbolo para los casos que aquí se distinguen*.

![[Archivos/04a-p44-tipos-interaccion.png]]

**El ejemplo canónico del deck** (p. 42): el diagrama de secuencia de la biblioteca, para comparar con el tuyo.

![[Archivos/04a-p42-biblioteca.png]]

### 🎭 4. Actividad: el Flujo con Decisiones

> [!example] 🧪 Cuándo Preferirla
>
> Úsala cuando hay ramas (si/no), paralelos (fork/join) o varios actores. Ejemplo: matrícula con validación de cupo + pago en paralelo.
>
> **Regla:** flujo lineal simple no necesita diagrama — una lista basta.

---

## 🗳️ Ejemplo de la Clase: el SIEL (Sistema de Elecciones Seccionales)

> [!info]- 🗳️ El caso de hoy (texto de la pizarra)
>
> El país se divide en **provincias → cantones → parroquias**. Las **organizaciones políticas** inscriben candidatura para **alcaldía (canton)** o **prefectura (provincia)**; para prefectura van candidato principal + vice. Un **funcionario electoral** califica la candidatura (aprueba o rechaza). El censo se importa del **Registro Civil**. El día de la elección, el **presidente de la JRV** registra el acta con votos por candidatura, nulos y blancos; el sistema la valida contra el padrón de la junta, y con inconsistencias el acta se envía a revisión. El **ciudadano** consulta su lugar de votación y los resultados; el **observador acreditado** descarga las actas escaneadas.

> [!info] 🎭 Actores del SIEL
> | Actor | Tipo | Casos que le piden al sistema |
> |---|---|---|
> | **Ciudadano** | humano | Consultar lugar de votación, Consultar resultados |
> | **Observador acreditado** | humano (es-un ciudadano) | Descargar actas escaneadas (+ todo lo del ciudadano) |
> | **Presidente de JRV** | humano | Registrar acta de escrutinio |
> | **Funcionario electoral** | humano | Calificar candidatura |
> | **Organización política** | rol institucional | Inscribir candidatura |
> | **Registro Civil** | «sistema» externo | Importar padrón |

![[../Diagramas/dsw-u2-04-05-use.svg]]

> [!note] 💡 ¿Para qué sirven y cómo se echan a perder?
>
> **Usos:** capturar requisitos en el lenguaje del usuario; planificar iteraciones (un paquete de casos por iteración); derivar pruebas a partir de escenarios.
>
> **Riesgos:** caer en diseño funcional (partir en funciones); detallar demasiado cada flujo; confundirlos con el diseño interno.
>
> | No (nivel interno) | Sí (nivel objetivo) |
> |---|---|
> | `Sumar votos en la tabla ACTAS` | `Registrar acta de escrutinio` |
>
> **Advertencia de Stevens:** no abuses de las flechas — un diagrama lleno de líneas cruzadas se confunde antes que un dibujo simple.

---

## 🗺️ Diagrama de Decisión: ¿Qué Diagrama Dibujo?

![[../Diagramas/dsw-u2-05-02-flow.svg]]

> [!tip] 💡 Lectura del diagrama
>
> La mayoría de los flujos de tu proyecto caen en secuencia; reserva actividad para los procesos con decisiones reales.

---

## ⚠️ Problemas Comunes y Soluciones

> [!danger] ❌ Error 1: Casos de Uso a Nivel de Botón (viola **objetivo con valor**)
>
> **Síntomas:** 30 óvalos (`Clic guardar`, `Abrir ventana`...) donde deberían ir 6 objetivos; el diagrama es un manual, no un menú.
>
> **Solución:**
>
> - Fusiona pasos en objetivos: 5-9 casos por sistema de curso.
> - El detalle va en la especificación textual o en secuencia, no en óvalos.

> [!danger] ❌ Error 2: Secuencia que Nadie Puede Seguir (viola **un escenario por diagrama**)
>
> **Síntomas:** 20 flechas cruzadas, vidas de objeto eternas, sin `alt`/`loop` donde hay ramas.
>
> **Solución:** parte el flujo por escenario (feliz vs error); cada diagrama, un escenario con sus ramas marcadas.

> [!danger] ❌ Error 3: Actividad para Todo, Incluso lo Lineal (viola **diagrama según decisión**)
>
> **Síntomas:** diagramas de actividad para flujos de 3 pasos sin decisiones.
>
> **Solución:** si no hay ramas ni paralelos, una lista numerada comunica mejor y más rápido.

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist de Comportamiento
>
> **1. Un flujo clave con secuencia antes de codear**
>
> El flujo "inscribirse" dibujado evita 3 bugs de orden por sprint.
>
> **2. Nombres de mensajes = métodos futuros**
>
> `verificarCupo()`, no "chequear cosa". El diagrama se vuelve código.
>
> **3. Actores reales, no roles inventados**
>
> Si ningún humano o sistema externo lo pide, no es caso de uso.
>
> **4. 5-9 casos por sistema de curso**
>
> Más = estás dibujando pasos; agrupa en objetivos.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Nivel 1 — Básico
>
> **1.** Define actor y caso de uso, y explica por qué "Ingresar carnet" no es un caso de uso.
>
> **2.** ¿Qué significan `<<include>>` y `<<extend>>`? Da un ejemplo de cada uno en un sistema de matrícula.
>
> **3.** Lee el diagrama de secuencia de la intro: ¿en qué orden ocurren las 4 llamadas?
>
> **4.** ¿Cuándo prefieres actividad sobre secuencia?
>
> **5.** Dibuja un `alt` y un `loop` mínimos y explica qué representa cada uno.
>
> > [!success]- ✅ Respuestas — Nivel 1
> >
> > - **1.** Actor = rol externo; caso = objetivo con valor. "Ingresar carnet" es un paso interno, ningún actor lo pediría como objetivo.
> > - **2.** Include: siempre incluido (Validar identidad). Extend: opcional (Aplicar descuento).
> > - **3.** inscribirse → verificar cupo → cupo OK → matrícula confirmada (de arriba abajo).
> > - **4.** Cuando hay ramas (si/no) o paralelos; lo lineal simple va en lista o secuencia.
> > - **5.** `alt`: ramas excluyentes (cupo sí/no). `loop`: repetición (reintentar pago 3 veces).

> [!example] 📋 Nivel 2 — Intermedio
>
> **6.** Escribe 5 casos de uso a nivel objetivo para un sistema de biblioteca (nada a nivel botón).
>
> **7.** Dibuja la secuencia de "devolver libro con multa": actores, llamadas, retornos y un `alt` (con/sin multa).
>
> **8.** Un flujo tiene validación de cupo Y pago en paralelo. ¿Secuencia o actividad? Justifica y dibújalo.
>
> **9.** Convierte tu diagrama de clases de la nota anterior (Biblioteca) en 3 casos de uso que lo usen.
>
> **10.** Detecta el error: un diagrama con 25 óvalos que incluyen "Abrir ventana" y "Guardar en BD".
>
> > [!success]- ✅ Respuestas — Nivel 2
> >
> > - **6.** Ej.: Buscar catálogo, Prestar libro, Devolver libro, Reservar ejemplar, Pagar multa.
> > - **7.** Lector→Sistema: devolver; Sistema→BD: buscar préstamo; alt con multa (calcular+cobrar) / sin multa (cerrar); retorno confirmación.
> > - **8.** Actividad: hay paralelo real (fork cupo/pago, join al confirmar). Secuencia forzaría un orden falso.
> > - **9.** Respuesta libre guiada: cada caso usa 2-3 clases del diagrama anterior como participantes.
> > - **10.** Casos a nivel botón/paso interno: fusionar en 5-7 objetivos ("Gestionar préstamo" absorbe abrir/guardar).

> [!example] 📋 Nivel 3 — Avanzado
>
> **11.** Diseña casos + secuencia + actividad coherentes para "inscripción con lista de espera": los 3 diagramas deben contar la misma historia.
>
> **12.** Argumenta dónde pondrías la validación "cupo > 0": ¿en secuencia (flujo), en actividad (regla) o en clases (invariante)? ¿Por qué?
>
> **13.** Un flujo crítico tiene 30 flechas en secuencia. Aplica la regla de partición por escenario y explica qué ganas y qué pierdes.
>
> **14.** Compara `alt`/`loop` de secuencia con rombos de actividad: ¿cuándo la misma rama se modela mejor en cada uno?
>
> **15.** Diseña los 3 diagramas de tu proyecto de curso para su flujo principal (5-9 casos, 1 secuencia del flujo feliz + 1 de error, actividad solo si hay ramas).
>
> > [!success]- ✅ Respuestas — Nivel 3
> >
> > - **11.** Casos: Inscribirse, Entrar en lista de espera, Notificar cupo. Secuencia por escenario. Actividad con fork validación/pago si aplica.
> > - **12.** En clases como invariante si es regla permanente del dominio; en flujo si es política temporal. Lo permanente va a estructura.
> > - **13.** Ganas legibilidad por escenario y revisiones focalizadas; pierdes la vista completa (compénsalo con el diagrama de actividad general).
> > - **14.** En secuencia cuando importa QUIÉN decide y el orden de mensajes; en actividad cuando importan los caminos y paralelos sin importar tanto el quién.
> > - **15.** Autocorrección con el checklist de esta nota + diagrama de decisión.

> [!example] 📋 Extra Control03 (formato papel)
>
> **16.** Escribe la descripción completa de `Devolver libro` (precondición, escenario principal en pasos, 1 flujo alternativo con multa, postcondición).
>
> **17.** Corrige la flecha y el tipo: `Prestar libro ──<<extend>>──▶ Pagar multa`. ¿Qué está mal?
>
> > [!success]- ✅ Respuestas — Extra
> >
> > - **16.** Tabla de 6 campos como la plantilla. Alterno: "(en paso 4, con atraso) **Con multa** → sistema calcula días × tarifa → registra pago → devuelve de todas formas". Post: la copia está disponible y el préstamo cerrado.
> > - **17.** Doble error: pagar multa es opcional ⇒ debe ser `<<extend>>`, pero LA flecha de extend nace en `Pagar multa` y llega a `Prestar libro` — escribo `Pagar multa - -<<extend>>- -▶ Prestar libro`.

> [!example] 📋 Extra SIEL (las 2 actividades de la clase)
>
> **18.** ¿Actor o no, para el SIEL? Juzga estos 8 candidatos con el test (¿es un ROL? ¿es EXTERNO? ¿interactúa con el sistema?):
> ① Presidente de JRV, ② María Pérez (presidenta de la JRV 12), ③ Ciudadano, ④ Base de datos del SIEL, ⑤ Sistema del Registro Civil, ⑥ Funcionario electoral, ⑦ Acta de escrutinio, ⑧ Delegado de una organización política.
>
> **19.** Modela los casos del SIEL: lista los actores, propón ≥6 casos con verbo + objeto, dibuja la frontera con un `<<include>>`, un `<<extend>>` y una generalización, y escribe la descripción de un caso con 2 escenarios con datos.
>
> > [!success]- ✅ Respuestas — Extra SIEL
> > >
> > > - **18.** ✅ Sí: **①** (rol), **③** (rol genérico), **⑤** (sistema externo con «sistema»), **⑥** (rol), **⑧** (rol; promueve `Inscribir candidatura`). ❌ No: **②** es una persona concreta, el actor es el ROL presidente de JRV; **④** es un componente interno — DENTRO de la frontera, no actor; **⑦** es un objeto del dominio que no interactúa.
> > > - **19.** Actores: la tabla de la sección 🗳️ (6). Casos: Inscribir candidatura, Calificar candidatura, Importar padrón, Registrar acta de escrutinio, Enviar acta a revisión, Consultar lugar de votación, Consultar resultados, Descargar actas escaneadas. Relaciones: `Registrar acta ──«include»──▶ Validar acta`; `Enviar acta a revisión - -«extend»- -▶ Registrar acta`; `Observador - -▷ Ciudadano` (generalización). Descripción + los 2 escenarios con datos: el ejemplo de la clase arriba (escenarios 🟢 y 🔴).

---

## 📋 Resumen Ejecutivo

> [!summary] 📋 Lo Esencial
>
> - **Casos de uso** = menú de objetivos del actor (5-9 por sistema, nada a nivel botón).
> - **Secuencia** = quién llama a quién en orden (1 escenario por diagrama, `alt`/`loop` marcados).
> - **Actividad** = solo con ramas o paralelos reales; lo lineal va en lista.
> - Cada flecha de secuencia será **una llamada a método**: diseñas código al dibujar.

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
> - [ ] Defino actor y caso de uso y distingo objetivos de pasos.
> - [ ] Leo una secuencia de arriba abajo con `alt` y `loop`.
> - [ ] Decido con el diagrama qué dibujar en cada situación.

> [!note] 🎯 Nivel Intermedio
> - [ ] Escribo 5-9 casos a nivel objetivo para un dominio nuevo.
> - [ ] Dibujo secuencias por escenario (feliz + error).
> - [ ] Uso actividad solo donde hay ramas o paralelo real.

> [!note] 🎯 Nivel Avanzado
> - [ ] Mantengo coherentes clases + casos + secuencias del mismo sistema.
> - [ ] Particiono secuencias gigantes por escenario con criterio.
> - [ ] Diseño los 3 diagramas del flujo principal de mi proyecto.

---

## 📊 Resumen Visual

![[../Diagramas/dsw-u2-05-03-mind.svg]]

> [!success] 🔍 Comparación Final
>
> | Aspecto | Solo Clases | Clases + Comportamiento |
> |---|---|---|
> | **Flujos** | ❌ Imaginados | ✅ Dibujados y revisables |
> | **Bugs de orden** | Aparecen en QA | Se ven en el diagrama |
> | **Decisión** | Adivinada | Con diagrama propio |
> | **Uso Recomendado** | Insuficiente solo | ✅ **Pack completo de diseño** |

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ Casos a nivel objetivo + diagrama de decisión propio
> ✅ Secuencia como futuro código + partición por escenario
> ✅ Actividad solo con ramas + 3 errores numerados
>
> **Próximo tema Unidad 3:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | **Del diagrama al código** | Traducir cada relación a Java | El diagrama se vuelve software que corre |
> | **Patrones de diseño** | Soluciones probadas con Shalloway | Dejas de reinventar la rueda |

---

## 🔁 Repaso SR (flashcards)

#flashcards/diseno-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Casos de uso qué son?::Menú de objetivos del actor: 5–9 por sistema, nada a nivel botón.
- ¿Actor y frontera?::Actor = rol externo (no persona). Frontera = el rectángulo: dentro lo que construyes, fuera los actores.
- ¿Caso vs escenario?::El caso es la familia de caminos completos hacia un valor observable; el escenario es UN camino concreto (el feliz, cada A1/A2).
> - ¿Secuencia qué muestra?::Quién llama a quién en orden — 1 escenario por diagrama, `alt`/`loop` marcados.
> - ¿Actividad cuándo?::Solo con ramas o paralelos reales; lo lineal va en lista.
> - ¿Flecha de secuencia = ?::Una llamada a método — diseñas código al dibujar.
> - ¿1 escenario por diagrama por qué?::Para que cada diagrama cuente una historia legible.
> - ¿Flecha del include?::Del caso base al incluido — el base SIEMPRE la llama.
> - ¿Flecha del extend?::Del extendido al base — el extra actúa solo si pasa algo.
> - ¿Pre vs postcondición?::Pre: estado requerido antes. Post: estado garantizado después — estados, no acciones.
> - ¿Los 6 campos de la descripción?::Actor, precondiciones, postcondición, escenario principal, flujos alternativos (con paso de origen).
> - ¿El escenario qué es?::Una instancia CONCRETA del caso: un recorrido con datos reales, sin ramificaciones (cada acta es un escenario).
> - ¿Generalización entre actores?::"Es-un" con triángulo hueco: el hijo hace TODO lo del padre y algo más — también aplica entre casos de uso.
> - ¿Nombre válido de caso de uso (test)?::Verbo + objeto con valor del actor: `Registrar acta de escrutinio`; NO `Sumar votos en la tabla ACTAS` (interno).

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[Diseño de Software]]
> - Índice Unidad 2: [[00 - Índice Unidad 2]]
> - Anterior: [[03 - UML clases, objetos y relaciones]]
> - Siguiente: [[05 - Del diagrama de clases al código]]
> - Syllabus: [[Bienvenida y Syllabus Diseño de Software]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - P. Stevens, R. Pooley, *Using UML*, 2nd ed., caps. 7-11 (casos de uso, secuencia, actividad).
> - I. Jacobson — casos de uso (origen con "los tres amigos" de UML).
> - Sílabo CCPG1042, Unidad 2: diseño orientado a objetos (7h).
> - Deck de cátedra: [[../Unidad 0 - Guias y Ejercicios/Diapositivas/04aLenguajeUnificadoModelado.pdf|04a Lenguaje unificado de modelado]] (50 p.) — notación UML, casos de uso, clases y **diagramas de secuencia** con frames `alt`/`opt`/`loop` y restricciones de tiempo; y [[../Unidad 0 - Guias y Ejercicios/Diapositivas/04bImplementaciónDesdeDiseno.pdf|04b Proceso de implementación desde un diseño]] (30 p.) — del diagrama de clases y de secuencia al código.
> - Capturas de la clase: [[SIEL - Casos de Uso]] (caso SIEL en pizarra) y [[SIEL - Modelo de Clases]].

---

**Tags:** #CCPG1042 #unidad2 #uml #secuencia #diseno-software
