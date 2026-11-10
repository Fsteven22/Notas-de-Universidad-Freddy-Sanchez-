---
dg-publish: true
tags: [CCPG1042, unidad5, git, versiones, colaboracion, diseno-software]
---

# 🔧 Control de Versiones con Git

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Git es Parte del Diseño y no Solo Herramienta?
>
> El **control de versiones** (Pressman cap. 22, SCM) guarda cada cambio con quién, cuándo y por qué — y permite ramas paralelas sin pisarse. El syllabus lo exige en el objetivo 4: software de calidad *en entorno colaborativo*.
>
> **Importancia histórica:** antes de Git reinaban CVS y Subversion centralizados — una caída del servidor paralizaba al equipo. Linus Torvalds creó Git (2005) distribuido por necesidad del kernel Linux: cada clon es el repositorio completo, y GitHub (2008) lo volvió social con pull requests.
>
> **Relevancia actual:** tu nota, tu proyecto y tu empleo viven en Git. Un historial limpio es tu currículum silencioso.
>
> **Analogía del mundo real:** piensa en Google Docs con esteroides:
>
> - **Sin control** → `proyecto_final_v3_REAL2.zip` por WhatsApp (¿cuál es la buena?)
> - **Con Git** → Historial único, ramas por función, fusiones revisadas.
> - **Rama** → Mesa de trabajo separada: experimentas sin romper lo estable.
> - **Commit** → Foto firmada del avance con mensaje que explica el porqué.
>
> | Razón | ZIPs por Chat | Git |
> |---|---|---|
> | **Historial** | Se pierde | Cada cambio trazable |
> | **Paralelo** | Se pisan | Ramas por persona/función |
> | **Errores** | Reescribir a mano | `revert` de 1 commit |
> | **Colaboración** | Turnos | Revisión por pull request |

> [!note] 🗺️ Diagrama — Introducción
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u5-03-01-graph.svg]]
>
> **Se lee así:** el diagrama parte de un **cambio en rama** y pregunta **¿flujo?**. La rama ❌
> es **push directo a main**, con las consecuencias **rompe a todos**, **sin revisión** y
> **culpa difusa**. La rama ✅ es **rama + PR + review**, que produce **tests en verde**,
> **2 ojos revisan** y **merge limpio**.
>
> **Por qué importa:** el diagrama contrapone dos costos distintos. El push directo no falla de
> forma visible: falla en diferido, cuando main ya está roto y nadie sabe quién lo rompió. La
> ruta con PR mueve el costo al momento de revisar, que es donde todavía se puede corregir
> barato.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, el compañero que empuja directo a main un
> viernes rompe la demo del lunes; el mismo cambio enviado por PR con los tests en verde se
> revisa y se fusiona sin sustos.

> [!note] 🖼️ captura 01b-p35 — Introducción
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p35.png]]
>
> **Se lee así:** es la **portada** de la lámina: el título «Control de versiones de software» y
> nada más. No hay diagrama ni texto de contenido; es la lámina que abre el bloque del material
> de clase.
>
> **Por qué importa:** sirve de ancla para el resto del bloque: las láminas que siguen
> desarrollan los comandos y los casos. Reconocerla evita confundirla con una lámina de
> contenido y deja claro que el material arranca por la teoría y recién después pasa a la
> práctica.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, esta es la lámina que se cita como deck 01b,
> p. 35 al referenciar el material de la unidad.

---

## 🧵 Flujo Mínimo de Equipo (Pressman cap. 22 + tus enlaces)

### 🎭 Rama, Commit, Push, PR

> [!note] 📋 Definición — El Ciclo Diario
>
> 1. **Actualiza y ramifica:** `git pull` en main, crea `feat/inscripciones` (1 rama = 1 función).
> 2. **Commits pequeños:** mensajes en imperativo — "agrega validación de cupo", no "cambios".
> 3. **Push + Pull Request:** la rama pide fusión; nadie se auto-aprueba.
> 4. **Review con checklist:** ¿compila? ¿tests verdes? ¿respeta capas? (ver Unidad 2).
> 5. **Merge y borra la rama:** main siempre verde y desplegable.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u5-03-02-graph.svg]]
>
> **Se lee así:** el diagrama es un ciclo cerrado que arranca en **main verde** y avanza por
> **rama feat**, **commits chicos**, **Pull Request** y **Review + tests**, para volver al punto
> de partida: **main verde**. La vuelta al origen es explícita, no implícita.
>
> **Por qué importa:** el ciclo muestra que la rama no es un estado alternativo: se crea desde un
> main verde y debe terminar dejando un main verde. Las condiciones de entrada y de salida son
> la misma, y por eso **main verde** aparece en los dos extremos del recorrido.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, abres `feat/validacion-cupo` desde main verde,
> haces commits chicos y el PR vuelve a main verde con la validación incluida.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p39.png]]
>
> **Se lee así:** la lámina dibuja el recorrido de un cambio por **cuatro zonas**: **directorio
> local**, **staging**, **repositorio local** y **repositorio público**, cada una con su
> descripción. Abajo aparecen los comandos: `git status`, `git add`, `git rm`, `git commit`,
> `git push` y `git pull`. Dice que en staging «se registran los cambios realizados» y que al
> repositorio local se le puede «reorganizar commit, agruparlos».
>
> **Por qué importa:** la lámina muestra que `commit` no es el final del viaje: hay un **staging**
> intermedio que permite elegir *qué* se versiona, y un **repositorio local** que es donde se
> puede reescribir la historia antes de compartirla. Por eso `git add` es un paso propio y no
> un detalle de `commit`.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, `git add -p` es la forma de elegir a mano qué
> hunks de `Pedido.java` entran al staging antes de `git commit -m "agrega validación de cupo"`.
>
> **Comandos que cubren el 90% del curso:**
>
> | Necesito | Comando |
> |---|---|
> | Ver estado | `git status` |
> | Guardar avance | `git add -p` + `git commit -m "verbo + qué"` |
> | Traer cambios | `git pull --rebase` |
> | Nueva función | `git checkout -b feat/nombre` |
> | Deshacer último commit local | `git reset --soft HEAD~1` |
> | Ver historia legible | `git log --oneline --graph -10` |
>
> Profundiza con tus enlaces guardados: [Video YouTube — Git (desde 1:30)](https://www.youtube.com/watch?v=4XpnKHJAok8&t=1m30s), [Git: cómo gestionar y cuidar nuestro código](https://www.enmilocalfunciona.io/git-como-gestionar-y-cuidar-nuestro-codigo/) y [Resolución de conflictos en GitHub — David Jurado](https://www.youtube.com/watch?v=H34vxQeQkgg) — todos en [[Recursos Visuales|Recursos Visuales]].

### 🔍 Buenas Prácticas que Evalúan Colaboración

> [!example] 🧪 Reglas de Equipo que Sí Puntúan
>
> - **Main protegido:** nada se sube sin PR aprobado (configúralo en GitHub desde el día 1).
> - **Convención de ramas:** `feat/`, `fix/`, `docs/` + nombre corto en minúsculas.
> - **Commits atómicos:** compila + tests verdes en cada commit, no "WIP" de 3 días.
> - **`.gitignore` desde el inicio:** `*.class`, `target/`, `.idea/`, credenciales — jamás binarios ni tokens.
> - **README vivo:** cómo compilar, probar y la arquitectura en 5 líneas (ver nota de arquitectura).

---

## 🗺️ Diagrama de Decisión: ¿Directo, Rama o PR?

> [!note] 🗺️ Diagrama — ️ Diagrama de Decisión: ¿Directo, Rama o PR
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u5-03-03-flow.svg]]
>
> **Se lee así:** el diagrama abre con **voy a cambiar código** y pregunta **¿toca main
> directo?**. Si estás en **solo mi rama**, la salida es **commit directo en tu rama**. Si es
> **main compartido**, pregunta **¿cambio trivial?**: para un **typo, 1 línea** la salida es
> **commit directo con buen mensaje**; para un **feature/fix real**, la salida es **rama + PR +
> review**.
>
> **Por qué importa:** el diagrama da un criterio de excepción en lugar de una prohibición
> absoluta. La regla general es rama y PR; el commit directo se acepta solo en el caso trivial, y
> **solo en tu rama**, que es donde no hay nadie más que pueda sufrirlo.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, corregir una tilde en el README va como commit
> directo, pero agregar la validación de cupo a `Pedido` sale por rama y PR.

> [!note] 🖼️ captura 01b-p42 — ️ Diagrama de Decisión: ¿Directo, Rama o PR
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p42.png]]
>
> **Se lee así:** la lámina es el **ejemplo de la lista de compras**, que arranca vacía en la
> **versión 0** y va creciendo por commits: primero una **hamburguesa**, después **verduras** y
> **cerveza**, hasta las **versiones 1, 2 y 3** de la lista. En el **repositorio** se ve el
> historial de esos commits, y una nota explica que al intentar hacer commit **no tiene la
> versión reciente**.
>
> **Por qué importa:** la lámina muestra el caso que el curso necesita que entiendas: el commit
> falla no porque el código esté mal, sino porque la copia local está **desactualizada**. Por eso
> la secuencia obligatoria es **pull antes de commit**, no después.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, si tú y un compañero editan el mismo
> `README.md`, tu commit falla con el mismo aviso de «no tiene la versión reciente» hasta que
> haces `git pull --rebase`.

> [!note] 🖼️ captura 01b-p43 — ️ Diagrama de Decisión: ¿Directo, Rama o PR
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p43.png]]
>
> **Se lee así:** es una lámina de una sola línea: el título **«Resolver un conflicto»**. No
> muestra código ni pasos: es el encabezado que anuncia la parte de la lámina donde se explica
> cómo salir de un conflicto.
>
> **Por qué importa:** aísla el concepto en su propio momento del material: el conflicto es el
> estado esperado del trabajo en equipo —no el error excepcional— y por eso tiene un
> procedimiento propio en lugar de resolverse improvisando.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, el aviso de conflicto al abrir un PR de
> `Pedido.java` se resuelve con `git pull --rebase`, se combinan las dos versiones a mano y se
> sigue con el merge.

> [!note] 🖼️ captura 01b-p44 — ️ Diagrama de Decisión: ¿Directo, Rama o PR
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p44.png]]
>
> **Se lee así:** la lámina repite el título del paso anterior con el resultado: **«Conflicto
> solucionado»**. Es la contraparte de la lámina 43: donde esa anunciaba el problema, esta
> muestra el final del procedimiento.
>
> **Por qué importa:** el par de láminas **«Resolver un conflicto» / «Conflicto solucionado»**
> convierte el conflicto en un procedimiento con salida, no en un callejón sin salida. Es la
> misma lógica del ciclo de la unidad: detectar, actuar, verificar.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, tras combinar las versiones y correr los tests
> en verde, el PR de `Pedido.java` se fusiona y ese es el «conflicto solucionado».

> [!tip] 💡 Lectura del diagrama
>
> La rama es el valor por defecto en equipo; el commit directo a main compartido casi nunca se justifica.

---

## ⚠️ Problemas Comunes y Soluciones

> [!danger] ❌ Error 1: Commits "Arreglos Varios" de 40 Archivos (viola **commit atómico**)
>
> **Síntomas:** review imposible, revertir rompe 3 funciones, nadie sabe qué cambió.
>
> **Solución:**
>
> - Límite: 1 commit = 1 idea, describible en 1 línea.
> - Mezclaste 2 ideas: `git reset --soft HEAD~1`, reagrupa con `git add -p` y recomitea.
> - Retraso crónico: commitea al terminar cada técnica de refactor (Unidad 4), no al final del día.

> [!danger] ❌ Error 2: Push Directo a Main Compartido (viola **revisión por pares**)
>
> **Síntomas:** main roto un lunes a las 8am y nadie sabe quién ni por qué.
>
> **Solución:** protege main en GitHub (requiere PR + checks verdes); el atajo de hoy es el incidente de mañana.

> [!danger] ❌ Error 3: Secretos Commiteados (viola **higiene del repo**)
>
> **Síntomas:** tokens y claves en el historial, visibles para siempre aunque los borres después.
>
> **Solución:** `.gitignore` desde el día 1 + variables de entorno; si se filtra uno, se rota el mismo día (no basta borrarlo).

---

## 🎯 Mejores Prácticas

> [!tip] 🏆 Checklist Colaborativo
>
> **1. Sincroniza cada mañana**
>
> `pull --rebase` antes de empezar: conflictos de 5 líneas, no de 500.
>
> **2. Revisa como te gustaría ser revisado**
>
> Comenta el código, pregunta antes de exigir, aprueba rápido lo bueno.
>
> **3. Todo secreto fuera del repo**
>
> Tokens y claves por variables de entorno; si se filtra uno, se rota el mismo día.
>
> **4. Ramas de vida corta**
>
> Días, no semanas: mientras más vive una rama, más duele su merge.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Nivel 1 — Básico
>
> **1.** Describe el ciclo rama → commit → push → PR → merge con tus palabras.
>
> **2.** ¿Qué hace cada comando: `status`, `add -p`, `commit -m`, `pull --rebase`, `checkout -b`, `log --oneline --graph`?
>
> **3.** Escribe 3 buenos y 3 malos mensajes de commit y explica la diferencia.
>
> **4.** ¿Qué debe tener un `.gitignore` Java mínimo y por qué cada entrada?
>
> **5.** ¿Por qué nadie debería pushear directo a main compartido?
>
> > [!success]- ✅ Respuestas — Nivel 1
> >
> > - **1.** Ramificas, commiteas chico, subes, pides revisión, fusionas y borras la rama.
> > - **2.** Estado, staging parcial, guardar con mensaje, traer con rebase, crear rama, historia legible.
> > - **3.** Buenos: verbo + qué ("agrega validación de cupo"). Malos: "cambios", "arreglos", "WIP final 2".
> > - **4.** `*.class`, `target/`, `.idea/`, `*.env`: compilados, IDE y secretos no viajan.
> > - **5.** Porque elimina la revisión y convierte main en zona de riesgo para todos.

> [!example] 📋 Nivel 2 — Intermedio
>
> **6.** Mezclaste 2 ideas en 1 commit ya pusheado a tu rama. Recupéralo paso a paso sin perder nada.
>
> **7.** Diseña la convención de ramas y mensajes para tu equipo de 4 (con ejemplos).
>
> **8.** Un compañero commiteó un token. Lista los pasos de respuesta en orden.
>
> **9.** Configura (en prosa) la protección de main en GitHub: ¿qué reglas activas y por qué?
>
> **10.** Resuelve un conflicto de merge típico (misma línea editada por 2): pasos exactos.
>
> > [!success]- ✅ Respuestas — Nivel 2
> >
> > - **6.** `reset --soft HEAD~1` → `add -p` por idea → 2 commits → `push --force-with-lease` (solo tu rama).
> > - **7.** `feat/`, `fix/`, `docs/` + nombre corto; mensajes imperativo + alcance. Ejemplos concretos del proyecto.
> > - **8.** Revocar/rotar el token YA → limpiar historial si es necesario → `.gitignore` + variables de entorno → avisar al equipo.
> > - **9.** Requerir PR + 1 aprobación + checks verdes + prohibir push directo: main siempre desplegable.
> > - **10.** `pull --rebase`, abre el conflicto, elige/combina a mano, `add`, continúa, tests, push.

> [!example] 📋 Nivel 3 — Avanzado
>
> **11.** Argumenta `rebase` vs `merge` para historiales de equipo: ¿cuándo cada uno?
>
> **12.** Diseña el flujo Git completo de tu proyecto (ramas, PRs, releases) en 1 diagrama + reglas.
>
> **13.** Un PR lleva 3 semanas abierto con 40 commits. Diagnostica y propón rescate concreto.
>
> **14.** ¿Cómo se relaciona "main siempre verde" con entrega continua (nota U5-03)? Argumenta la cadena.
>
> **15.** Escribe la guía Git de 1 página para tu equipo (la que leería un miembro nuevo el día 1).
>
> > [!success]- ✅ Respuestas — Nivel 3
> >
> > - **11.** Rebase: historial lineal legible (ramas propias). Merge: preserva contexto real (main compartido). Regla: rebase local, merge al integrar.
> > - **12.** Respuesta libre guiada: main protegido + ramas feat/fix + releases etiquetados + convenciones del checklist.
> > - **13.** Síntoma de rama eterna: pártelo en PRs chicos fusionables por semana; lo no listo va tras feature flag o se descarta.
> > - **14.** Main verde + tests = base desplegable en cada commit: sin eso no hay pipeline que valga.
> > - **15.** Respuesta libre guiada: ciclo diario, convenciones, protección de main, qué hacer si algo sale mal.

---

## 📋 Resumen Ejecutivo

> [!summary] 📋 Lo Esencial
>
> - **Rama por función**, commits atómicos, PR con review, main siempre verde.
> - `.gitignore` desde el día 1; secretos por variables de entorno.
> - Sincroniza a diario; ramas cortas; rebase local, merge al integrar.

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
>
> - [ ] Describo el ciclo completo rama→merge sin mirar.
> - [ ] Uso los 6 comandos base con soltura.
> - [ ] Escribo mensajes de commit que cuentan la historia.

> [!note] 🎯 Nivel Intermedio
>
> - [ ] Rescato commits mezclados sin perder trabajo.
> - [ ] Respondo a un secreto filtrado en orden correcto.
> - [ ] Configuro protección de main con criterio.

> [!note] 🎯 Nivel Avanzado
>
> - [ ] Decido rebase vs merge según el caso.
> - [ ] Diseño el flujo Git completo de un equipo.
> - [ ] Escribo la guía Git de 1 página para recién llegados.

---

## 📊 Resumen Visual

> [!note] 🗺️ Diagrama — Resumen Visual
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/dsw-u5-03-04-mind.svg]]
>
> **Se lee así:** es un mapa mental con raíz **Git en equipo** y tres ramas. **Flujo** recoge
> **rama por función**, **PR + review** y **main verde**. **Higiene** recoge **commits
> atómicos**, **`.gitignore`** y **sin secretos**. **Historia** fija la regla de reescritura:
> **rebase local**, **merge al integrar**.
>
> **Por qué importa:** el mapa separa las tres dimensiones de trabajar en equipo con Git: el
> proceso de entrega, la higiene del repositorio y el manejo del historial. La rama **Historia**
> es la que evita el error caro, porque un `rebase` publicado reescribe historia compartida.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, tu rama `feat/validacion-cupo` la rebases a
> diario, pero el `merge` a main lo hace quien aprueba el PR.

> [!success] 🔍 Comparación Final
>
> | Aspecto | ZIPs | Git con Flujo |
> |---|---|---|
> | **Trazabilidad** | ❌ Nula | Cada cambio firmado |
> | **Colaborar** | Turnos | Paralelo + review |
> | **Decisión** | Adivinada | Con diagrama propio |
> | **Uso Recomendado** | Nunca en equipo | ✅ **Objetivo 4 del syllabus** |

---

## 🚀 Próximos Pasos

> [!quote] 🌟 Continuando
>
> **Has aprendido:**
>
> ✅ Flujo diario + historia Git + diagrama de decisión propio
> ✅ 3 errores numerados + convenciones de equipo
> ✅ Protección de main y respuesta a secretos
>
> **Próximo tema:**
>
> | Tema | Qué verás | Por qué importa |
> |---|---|---|
> | **Entrega continua y DevOps** | Pipeline CI/CD | Donde tu Git se vuelve entrega |

---

## 🔁 Repaso SR (flashcards)

#flashcards/diseno-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Ramas cómo?::Una rama por función, cortas y sincronizadas a diario.
> - ¿Commits cómo?::Atómicos, con PR y review; main siempre verde.
> - ¿`.gitignore` cuándo?::Desde el día 1.
> - ¿Secretos dónde?::En variables de entorno, nunca en el repo.
> - ¿Rebase o merge?::Rebase en local, merge al integrar.

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../Diseño de Software|Diseño de Software]]
> - Anterior: [[01 - Pruebas unitarias con JUnit 5]]
> - Siguiente: [[03 - Entrega continua y DevOps]]
> - Syllabus: [[../Bienvenida y Syllabus Diseño de Software|Bienvenida y Syllabus Diseño de Software]]

## 📚 Referencias

> [!quote] 📖 Fuentes
>
> - R. Pressman, B. Maxim, *Software Engineering: A Practitioner's Approach*, 9th ed., cap. 22 (SCM).
> - L. Torvalds (2005), Git — historia; GitHub (2008), pull requests.
> - [Git: cómo gestionar y cuidar nuestro código](https://www.enmilocalfunciona.io/git-como-gestionar-y-cuidar-nuestro-codigo/) + [Video YouTube — Git](https://www.youtube.com/watch?v=4XpnKHJAok8&t=1m30s) + [Resolución de conflictos en GitHub — David Jurado](https://www.youtube.com/watch?v=H34vxQeQkgg).

> [!info] Láminas del material de clase
>
> Renderizados del deck de la unidad, en orden de presentación.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p35.png]]
>
> **Se lee así:** es la **portada** de la lámina, con el título «Control de versiones de
> software» y ningún otro contenido. Abre el bloque de láminas del material de clase.
>
> **Por qué importa:** fija el punto de partida del material: el bloque empieza por la teoría del
> control de versiones y recién después pasa a los comandos y a los casos de conflicto.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, esta es la lámina que se cita como deck 01b,
> p. 35 al referenciar el material de la unidad.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p39.png]]
>
> **Se lee así:** la lámina dibuja el recorrido de un cambio por **directorio local**, **staging**,
> **repositorio local** y **repositorio público**, con la descripción de cada zona. Debajo
> aparecen los comandos `git status`, `git add`, `git rm`, `git commit`, `git push` y `git pull`.
>
> **Por qué importa:** deja claro que `commit` no es el final del viaje: el **staging** decide
> qué se versiona y el **repositorio local** es donde todavía se puede reescribir la historia.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, `git add -p` es la forma de elegir a mano qué
> hunks de `Pedido.java` entran al staging antes del commit.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p42.png]]
>
> **Se lee así:** es el **ejemplo de la lista de compras**: parte vacía en la **versión 0** y
> crece por commits —**hamburguesa**, después **verduras** y **cerveza**— hasta las **versiones
> 1, 2 y 3**. Una nota del repositorio avisa que al intentar hacer commit **no tiene la versión
> reciente**.
>
> **Por qué importa:** muestra que el commit puede fallar no porque el código esté mal, sino
> porque la copia local está desactualizada, y por eso el `pull` va **antes** del commit.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, el mismo aviso aparece cuando tú y un compañero
> tocan el mismo `README.md` y hay que hacer `git pull --rebase` antes de seguir.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p43.png]]
>
> **Se lee así:** es una lámina de una sola línea con el título **«Resolver un conflicto»**. No
> muestra código ni pasos: anuncia la parte del material dedicada a salir de un conflicto.
>
> **Por qué importa:** convierte el conflicto en un estado con procedimiento propio y no en el
> error excepcional del trabajo en equipo, que es lo que exige un flujo ordenado de pull, merge
> y tests.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, el conflicto al abrir el PR de `Pedido.java` se
> resuelve con `git pull --rebase` y combinando las dos versiones a mano.
>
> ![[../Unidad 0 - Guias y Ejercicios/Archivos/Pruebas/dsw-01b-p44.png]]
>
> **Se lee así:** la lámina cierra la secuencia con el resultado: **«Conflicto solucionado»**. Es
> la contraparte directa de la lámina anterior, donde se anunciaba el problema.
>
> **Por qué importa:** el par **«Resolver un conflicto» / «Conflicto solucionado»** muestra que
> todo el flujo de Git tiene salida: detectar, actuar, verificar, y con eso el equipo puede
> seguir entregando.
>
> **Ejemplo:** en el proyecto de curso de ESPOL, tras combinar las versiones y correr los tests
> en verde, el PR de `Pedido.java` se fusiona y ese es el conflicto solucionado.

---

**Tags:** #CCPG1042 #unidad5 #git #versiones #colaboracion #diseno-software
