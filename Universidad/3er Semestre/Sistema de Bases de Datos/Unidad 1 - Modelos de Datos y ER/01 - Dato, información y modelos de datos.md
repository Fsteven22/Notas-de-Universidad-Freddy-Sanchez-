---
dg-publish: true
tags: [TICG1018, unidad1, datos, modelos, historia]
---

# ðŸ’¾ Dato, InformaciÃ³n y Modelos de Datos

## ðŸŽ¯ IntroducciÃ³n

> [!info] ðŸ’¡ Â¿Por QuÃ© Modelar Antes de Guardar?
>
> Todo sistema que uses â€” Aula Virtual, banca mÃ³vil, el inventario de una tienda â€” vive sobre un modelo decidido antes de escribir cÃ³digo. Equivocarse ahÃ­ cuesta reescrituras (los egipcios en papiros del 2000 a.C. ya registraban; el medio cambiÃ³, el costo de no modelar no). Esta nota responde quÃ© se guarda, cÃ³mo se organiza y cÃ³mo evolucionÃ³ esa respuesta en 60 aÃ±os.
>
> **Â¿DÃ³nde se usa?**
> - **DiseÃ±o de BD:** todo sistema (notas 02-03, proyecto del curso).
> - **Migraciones:** pasar de Excel/archivos a tablas sin perder nada.
> - **LecciÃ³n 1 (13-oct):** dato vs informaciÃ³n + archivos vs BD, seguro evaluado.

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-01-graph.svg]]

---

## ðŸ“‹ Definiciones Formales

> [!info] â„¹ï¸ CÃ³mo leer esta secciÃ³n
> Una definiciÃ³n por bloque, cada una con su ejemplo y su figura.

### 1ï¸âƒ£ Dato â€” el valor crudo

> [!note] ðŸ“‹ DefiniciÃ³n â€” Dato
>
> Valor crudo sin contexto. Por sÃ­ solo no dice nada ni permite decidir.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-02-graph.svg]]
>
> **Ejemplos:** `"19"`, `"Irene"`, `"2026-10-13"`. Â¿19 quÃ©? Sin contexto es solo un sÃ­mbolo guardado.

### 2ï¸âƒ£ InformaciÃ³n â€” el dato con contexto

> [!note] ðŸ“‹ DefiniciÃ³n â€” InformaciÃ³n
>
> Dato interpretado en un contexto que permite decidir o actuar.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-03-graph.svg]]
>
> **Ejemplo:** *"19 estudiantes aprobaron SBD"* â€” ahora sÃ­ hay decisiÃ³n posible (Â¿festejar? Â¿reforzar?). El modelo de datos existe para producir informaciÃ³n, no para acumular datos.

### 3ï¸âƒ£ Modelo de datos â€” el plano antes de guardar

> [!note] ðŸ“‹ DefiniciÃ³n â€” Modelo de datos
>
> RepresentaciÃ³n lÃ³gica y estructurada que define estructura, relaciones, restricciones y transformaciones. Es iterativo y es el lenguaje comÃºn entre cliente, analista y dev.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-04-graph.svg]]
>
> **Por quÃ© importa (diapositivas):** cubre requerimientos desde el diseÃ±o; minimiza cambios continuos, redundancia y problemas de acceso; sin buen diseÃ±o no hay hardware ni UI que salve el desempeÃ±o.
>
> **Ejemplo:** tabla ESTUDIANTE con PK `carnet` â€” el modelo decidiÃ³ quÃ© se guarda y cÃ³mo se conecta antes de escribir una lÃ­nea de cÃ³digo.

### 4ï¸âƒ£ Archivos vs Base de datos â€” por quÃ© modelar gana

> [!note] ðŸ“‹ DefiniciÃ³n â€” Sistema de archivos vs base de datos
>
> | Aspecto | Archivos Tradicionales | Base de Datos |
> |---|---|---|
> | **Redundancia** | Mismo dato en N archivos | Definido una vez |
> | **Consistencia** | Se desincroniza | Restricciones la garantizan |
> | **Acceso** | Programas a medida | Lenguaje comÃºn (SQL) |
> | **Escala** | Colapsa con usuarios | Concurrente y segura |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-05-graph.svg]]
>
> **Historia real:** egipcios en papiros (2000 a.C.) â€” el medio cambia, la necesidad de registrar no. Los archivos repiten el problema del papiro (copias que se desincronizan); la BD lo resuelve con unicidad + restricciones.

> [!info] ðŸ“– El deck de cÃ¡tedra: por quÃ© existieron los SBD (slides01, pp. 4-11)
> El deck del Ing. Jorge Magallanes abre el curso explicando el problema que las bases de datos resolvieron. Estas son sus figuras literales.

![[Archivos/bd-s01-p4.png]]

> **Sistemas basados en archivos (p. 5):** *"una colecciÃ³n de programas de aplicaciÃ³n, donde cada programa define y maneja sus propios datos"*. Las instituciones con distintas localidades tenÃ­an sistemas aislados â€” de ahÃ­ el nombre "sistemas basados en archivos".

![[Archivos/bd-s01-p6.png]]

> **Las limitaciones del deck (p. 6):** la definiciÃ³n de los datos embebida en los programas hace que los cambios posteriores en la estructura de datos dificulten el mantenimiento; y cada programa trabaja con su propio archivo.

> [!note] ðŸ“– Del archivo al DBMS: el salto del deck (slides01, pp. 8-11)
> *"Un sistema de bases de datos se define como un conjunto de programas de aplicaciÃ³n que acceden a la base de datos a travÃ©s de un sistema de gestiÃ³n de bases de datos (DBMS)"* (p. 8). El **DBMS** (p. 9) es el conjunto de programas que permite definir, crear, mantener y controlar el acceso a los datos.

![[Archivos/bd-s01-p13.png]]

![[Archivos/bd-s01-p14.png]]

> **Arquitectura cliente-servidor (2 capas, p. 13) y arquitectura web (3 capas, p. 14):** el deck las dibuja como el camino que sigue la peticiÃ³n â€” del cliente al servidor de aplicaciones y de ahÃ­ a la base de datos. La de 3 capas es la que separa GUI, lÃ³gica de negocio y datos en servidores distintos.

> [!tip] ðŸ“– El proceso de diseÃ±o, segÃºn el deck (slides01, pp. 15-18)
> *"La informaciÃ³n es el activo mÃ¡s importante de las organizaciones"* (p. 16) â€” por eso el diseÃ±o de la base es un proceso formal y no una ocurrencia.

![[Archivos/bd-s01-p17.png]]

![[Archivos/bd-s01-p18.png]]

> **Modelo de datos (p. 17):** *"conjunto de conceptos que describen la estructura de los datos en el contexto de un modelo de negocio"*.
>
> **Proceso de diseÃ±o (p. 18):** determinar vistas de usuario y requerimientos de datos â†’ definir entidades, relaciones, atributos y dominios â†’ verificar el modelo â†’ definirâ€¦ (el resto del proceso son las unidades siguientes).

---

## ðŸ§µ EvoluciÃ³n de los Modelos (Coronel cap. 2)

> [!note] ðŸ“‹ Un Modelo por Ã‰poca
>
> | GeneraciÃ³n | Ã‰poca | Modelo | Idea |
> |---|---|---|---|
> | Archivos | 1960s-70s | VSAM, planos | Registros, no relaciones |
> | Segunda | 1970s | **JerÃ¡rquico** (IMS, Apollo 1969) | Ãrbol invertido: un padre, N hijos |
> | Segunda | 1970s | **Red** (ADABAS, IDS-II) | Grafo multipadre + schema/subschema/DML/DDL |
> | Tercera | 1970s-hoy | **Relacional** (Codd 1970) | Tablas + SQL declarativo |
> | Tercera | 1976-hoy | **ER** (Chen) | El plano grÃ¡fico del relacional |
> | Cuarta | 1980s-hoy | **OO / Objeto-Relacional** | Objetos con mÃ©todos; tipos extensibles |
> | Siguiente | Hoy-futuro | **XML, hÃ­bridas, nube** | No estructurado + servicios |
>

### ðŸ” Cada generaciÃ³n, dibujada

> [!example] ðŸ§ª Ver los 4 modelos clave
>
> **JerÃ¡rquico (un padre, N hijos):** lo compartido se duplica.
>
> Historia: *Ana trabaja en las direcciones Norte y Sur. Como cada hijo tiene un solo padre, su ficha debe copiarse bajo cada direcciÃ³n.*
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-06-graph.svg]]
>
> **Se lee asÃ­:** `dup` = duplicado por obligaciÃ³n del modelo. Cambia el telÃ©fono de Ana y debes cambiarlo en 2 fichas o mienten (redundancia + inconsistencia, los 2 males de archivos).
>
> **Red (multipadre):** grafo con schema/subschema; muriÃ³ por falta de consultas ad hoc.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-07-graph.svg]]
>
> **Relacional (Codd 1970):** tablas + SQL declarativo + independencia fÃ­sica.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-08-er.svg]]
>
> **ER (Chen 1976):** el plano grÃ¡fico del relacional â€” rectÃ¡ngulos, rombos y Ã³valos antes de crear tablas.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-09-graph.svg]]
>
> **Se lee asÃ­:** el mismo EMPLEADOâ€“PROYECTO del relacional, pero en Chen puro: todavÃ­a no hay tablas ni FK, solo quÃ© existe y cÃ³mo se conecta.
>
> **Detalles que evalÃºan:** el jerÃ¡rquico duplica lo compartido; la red muriÃ³ por falta de consultas ad hoc; Codd publicÃ³ en CACM (junio 1970); M:N existe en conceptual pero no va al relacional.
>

---

## ðŸ› ï¸ MÃ©todo: Del Enunciado al Modelo

> [!note] ðŸ“‹ Procedimiento General
>
> 1. Subraya sustantivos (candidatos a entidad) y verbos (candidatos a relaciÃ³n).
> 2. Pregunta por cada tabla futura: "Â¿quÃ© decisiÃ³n se toma con esto?" (sin pregunta, no hay tabla).
> 3. Dibuja ERD con claves desde el dÃ­a 1.
> 4. Traduce a tablas y verifica con las reglas de negocio.
> 5. Itera: el modelo se refina, no nace perfecto.
>
> **Principio clave:** modela lo permanente (Estudiantes, Materias), no los formularios â€” las pantallas cambian, el negocio no.
>

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-10-flow.svg]]

---

## ðŸŽ¨ Ejemplo Trabajado

> [!example] ðŸŸ¢ Mini-caso SBD
>
> Enunciado: *"Irene dicta SBD1; cada estudiante toma varias materias."*
>
> | Paso | Resultado |
> |---|---|
> | Sustantivos | Ireneâ†’PROFESOR, SBD1â†’MATERIA, estudianteâ†’ESTUDIANTE |
> | Verbos | *dicta*, *toma* |
> | Claves | carnet, cÃ³digo |
> | ClasificaciÃ³n | PROFESORâ€“MATERIA 1:M; ESTUDIANTEâ€“MATERIA M:N (pide intermedia) |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-11-graph.svg]]
>
> **Se lee asÃ­ (Chen puro, sin tablas todavÃ­a):** Irene (PROFESOR) *dicta* SBD1; cada estudiante *toma* varias materias. La M:N *toma* pedirÃ¡ una intermedia al traducir (Unidad 2), pero en el conceptual solo existe el rombo.

---

## ðŸ—‚ï¸ Â¿CuÃ¡ndo Bastan Archivos?

> [!note] ðŸ“‹ La excepciÃ³n que confirma la regla
>
> Solo para datos de usar y tirar: logs simples de una app, cachÃ©s temporales, exportaciones de un solo uso. En cuanto haya 2 usuarios, reportes repetidos o decisiones encima â†’ modela.
>
> | SeÃ±al | Archivos bastan | Pide BD |
> |---|---|---|
> | **Usuarios** | 1 | Varios concurrentes |
> | **Preguntas** | Siempre las mismas 2 | Nuevas cada semana |
> | **Vida del dato** | Horas/dÃ­as | Meses/aÃ±os |

---

## âš ï¸ Errores Comunes y Principios LÃ³gicos

> [!warning] âš ï¸ CÃ³mo leer esta secciÃ³n
> Cada error trae su dibujo: lo âŒ que delata el problema y lo âœ… que lo evita.

### âŒ Error 1: Modelar pantallas, no el negocio

> [!danger] âŒ Viola: permanencia del modelo
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-12-graph.svg]]
>
> Al cambiar la UI muere la BD. Modela entidades permanentes: las pantallas cambian, el negocio no.

### âŒ Error 2: Tabla sin pregunta

> [!danger] âŒ Viola: toda tabla responde una decisiÃ³n
>
> Si ningÃºn reporte ni decisiÃ³n usa la tabla, sobra (todavÃ­a). Pregunta por cada tabla futura: *"Â¿quÃ© decisiÃ³n se toma con esto?"*. Sin respuesta â†’ no la crees.

### âŒ Error 3: Confundir dato con informaciÃ³n

> [!danger] âŒ Viola: contexto antes que almacenamiento
>
> Guardar todo sin contexto es archivar, no diseÃ±ar. `19` solo es informaciÃ³n cuando sabes que son *"19 estudiantes que aprobaron SBD"* â€” el modelo captura ese contexto en estructura + restricciones.

### âŒ Error 4: Saltarse el ERD

> [!danger] âŒ Viola: orden obligatorio ERD â†’ tablas â†’ SQL
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-01-13-graph.svg]]
>
> Ir directo a tablas garantiza N:M olvidadas y FKs inventadas.

---

## ðŸ“ Ejercicios Propuestos

> [!info] â„¹ï¸ CÃ³mo trabajarlos
> Tapa la soluciÃ³n, resuelve, compara. Respuestas colapsables abajo.

### âœï¸ Ejercicio 1 â€” Dato, informaciÃ³n o modelo

> [!example] ðŸ“‹ Planteamiento
>
> Clasifica:
> - (a) `"19"`,
> - (b) *"19 estudiantes aprobaron SBD"*,
> - (c) tabla ESTUDIANTE con PK `carnet`.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > (a) Dato: sin contexto. (b) InformaciÃ³n: dato + contexto que permite decidir. (c) Modelo: estructura que produce informaciÃ³n de forma repetible.

### âœï¸ Ejercicio 2 â€” Â¿Archivos o BD?

> [!example] ðŸ“‹ Planteamiento
>
> - Caso A: app de 1 usuario con 2 reportes fijos y datos de una semana.
> - Caso B: matrÃ­cula multiusuario con reportes nuevos cada mes. Â¿QuÃ© pide cada uno y por quÃ©?
>
> > [!success]- âœ… SoluciÃ³n
> >
> > A: archivos bastan (1 usuario, preguntas fijas, vida corta). B: BD modelada (concurrencia, preguntas cambiantes, decisiones encima). Regla: 2+ usuarios o reportes nuevos â†’ modela.

### âœï¸ Ejercicio 3 â€” Ordena las generaciones

> [!example] ðŸ“‹ Planteamiento
>
> Ordena (jerÃ¡rquico, red, relacional, archivos) y explica con 1 lÃ­nea por quÃ© la red muriÃ³ aunque era mÃ¡s flexible que el jerÃ¡rquico.
>
> - Pista 1: el orden es cronolÃ³gico (60s â†’ 70s).
> - Pista 2: la red pedÃ­a programas a medida para preguntar.
> - Pista 3: el relacional trajo SQL declarativo.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > Archivos â†’ jerÃ¡rquico â†’ red â†’ relacional. La red muriÃ³ por falta de consultas ad hoc: potente pero solo accesible con programas a medida; el SQL declarativo del relacional la volviÃ³ obsoleta.

---

## ðŸŽ¯ Metas de Aprendizaje

> [!note] ðŸ“‹ Nivel BÃ¡sico
>
> - [ ] Defino dato, informaciÃ³n y modelo sin mirar.
> - [ ] Explico archivos vs BD con 3 diferencias y 1 ejemplo propio.
> - [ ] Ubico los 6 modelos en su generaciÃ³n con un ejemplo cada uno.
>
> [!note] ðŸ“‹ Nivel Intermedio
>
> - [ ] Aplico el mÃ©todo de 5 pasos a un enunciado nuevo.
> - [ ] Justifico por quÃ© ganÃ³ el relacional (SQL + independencia).
> - [ ] Detecto quÃ© modelo pide un caso dado.

---

## ðŸ“š Referencias

> [!quote] ðŸ“– Fuentes Consultadas
>
> - Diapositivas BD01 (Irene Cheung) + `BD01 IntroducciÃ³n_datamodel.pdf`.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 2 Â§Â§2.5.1â€“2.5.7.

---

## ðŸ” Repaso SR (flashcards)

#flashcards/bd-u1

> [!note] ðŸ§  Repasa con el plugin Spaced Repetition

- Â¿Dato vs informaciÃ³n?::Valor crudo sin contexto vs dato interpretado en contexto.
- Â¿Tres problemas de archivos tradicionales?::Redundancia, inconsistencia y programas a medida.
- Â¿Modelo jerÃ¡rquico en 1 lÃ­nea?::Ãrbol invertido: un padre, N hijos (solo un padre por hijo).
- Â¿QuÃ© aportÃ³ la red y por quÃ© muriÃ³?::Multipadre + schema/subschema/DML/DDL; muriÃ³ por falta de consultas ad hoc.
- Â¿Codd, aÃ±o y aporte?::1970: tablas + SQL declarativo e independencia fÃ­sica.

---

## ðŸ”— Conexiones

> [!quote] ðŸ”— Notas Relacionadas
>
> - [[02 - Entidades, atributos, claves y relaciones]] â€” el vocabulario para dibujar lo de aquÃ­.
> - Ver tambiÃ©n [[03 - Modelo relacional, ERM y casos Tiny College]] para la traducciÃ³n a tablas.

---

## ðŸ”— Seguir estudiando

> [!info] ðŸ“š Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Ãndice Unidad 1: [[00 - Ãndice Unidad 1]] Â· Ãndice Unidad 2: [[00 - Ãndice Unidad 2]]
> - Siguiente: [[02 - Entidades, atributos, claves y relaciones]]
> - ConversiÃ³n a tablas: [[01 - ConversiÃ³n MC a ML por cardinalidad]]
> - Syllabus: [[Bienvenida y Syllabus Sistema de Bases de Datos]]

---

**Tags:** #TICG1018 #unidad1 #datos #modelos #bd

