---
dg-publish: true
tags: [TICG1018, unidad1, relacional, erm, chen, casos]
---

# ðŸ—ƒï¸ Modelo Relacional, ERM y Casos Tiny College

## ðŸŽ¯ IntroducciÃ³n

> [!info] ðŸ’¡ Â¿Por QuÃ© las Tablas Ganaron y el Dibujo Manda?
>
> Desde 1970 casi todo lo que consultas vive en tablas, y desde 1976 casi todo lo que se diseÃ±a se dibuja primero. Entender por quÃ© ganÃ³ cada uno â€”y quÃ© resuelve cada notaciÃ³nâ€” es lo que separa traducir un ER mecÃ¡nicamente de diseÃ±ar uno que no se rompa al implementar.
>
> **Aplicaciones:**
> - **ImplementaciÃ³n:** toda tabla del proyecto y del SQL futuro sale de aquÃ­.
> - **DiseÃ±o grÃ¡fico:** el ERD es el plano que cliente y dev entienden sin cÃ³digo.
> - **LecciÃ³n 1 (13-oct):** Codd en 1 frase + Chen en 1 frase + traducir 1 ER a tablas.
>
> | Concepto | Relacional (implementa) | ERM (diseÃ±a) |
> |---|---|---|
> | **Autor/aÃ±o** | Codd | Chen 1976 |
> | **Pieza base** | RelaciÃ³n = tabla (filas Ã— columnas) | Entidad + relaciÃ³n graficadas |
> | **ConexiÃ³n** | Columna en comÃºn | Rombo/verbo + cardinalidad |
> | **Notaciones ERD** | â€” (no se dibuja: se escribe en tablas) | Chen, pata de gallo, clases |

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-01-graph.svg]]

---

## ðŸ“‹ Definiciones Formales

> [!info] â„¹ï¸ CÃ³mo leer esta secciÃ³n
> Una definiciÃ³n por bloque, cada una con su ejemplo y su figura. Nivel lÃ³gico: aquÃ­ las tablas sÃ­ son las protagonistas.

### 1ï¸âƒ£ RelaciÃ³n, tupla y atributo â€” el vocabulario de tabla

> [!note] ðŸ“‹ DefiniciÃ³n â€” RelaciÃ³n, tupla, atributo
>
> - **RelaciÃ³n (tabla):** intersecciÃ³n de filas y columnas.
> - **Tupla/fila:** una ocurrencia (un estudiante concreto).
> - **Atributo/columna:** una casilla (nombre, cÃ³digo).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-02-er.svg]]
>
> **Ejemplo:** la tabla es la relaciÃ³n; cada fila una tupla (`0876, Jorge`); cada columna un atributo (`nombre`). SÃ­: **relacional = tablas** â€” Codd propuso guardar todo en tablas relacionadas por columnas comunes, con base matemÃ¡tica.
>
> **Por quÃ© "relacional" (campusMVP):** no es porque las tablas *se relacionen* con FK â€” es porque los datos se guardan como **relaciones** (listas = tablas). Tabla = RelaciÃ³n, literal.
>
> **Northwind (ejemplo clÃ¡sico):** pedidos con Proveedores, Productos, Empleados, Clientes, Transportistas + `Order Details` como intermedia. Si la nombran en clase, ya sabes quÃ© es.
>
> **Las 6 cualidades de un buen diseÃ±o (T. Grayson, vÃ­a campusMVP):** refleja el mundo real; representa todos los datos esperados en el tiempo; evita redundancia; acceso eficaz; mantiene integridad; claro y comprensible.
>
> > [!quote] ðŸ“– campusMVP, "DiseÃ±ando una base de datos en el modelo relacional" (2014) â€” https://www.campusmvp.es/recursos/post/Disenando-una-base-de-datos-en-el-modelo-relacional.aspx

### 2ï¸âƒ£ Tres niveles â€” del dibujo al disco

> [!note] ðŸ“‹ DefiniciÃ³n â€” Niveles conceptual, lÃ³gico y fÃ­sico
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-03-graph.svg]]
>
> **Ejemplo:** el rombo *toma* (conceptual) â†’ tabla MATRÃCULA con (PK,FK) (lÃ³gico) â†’ Ã­ndice sobre `carnet` (fÃ­sico). Cada nivel decide cosas distintas.

> [!info] ðŸ“– El deck de cÃ¡tedra: del conceptual al lÃ³gico (slides3, p. 3)
> El deck del Ing. Magallanes abre la unidad del modelo lÃ³gico con el diagrama que resume todo el proceso: una **ciudad** y un **estudiante** en el modelo conceptual, con sus cardinalidades (1,1) y (0,n), y la misma informaciÃ³n ya como tablas en el modelo lÃ³gico.

![[Archivos/bd-s03-p3.png]]

> **El diseÃ±o lÃ³gico (p. 4):** *"es el proceso de construir un modelo lÃ³gico a partir de un modelo conceptual"*, y tanto el conceptual como el lÃ³gico son **procesos iterativos**, no lineales.

### 3ï¸âƒ£ Regla de traducciÃ³n ERâ†’tablas â€” el puente

> [!note] ðŸ“‹ DefiniciÃ³n â€” TraducciÃ³n
>
> Entidad â†’ tabla; atributo â†’ columna; clave â†’ PK; N:M â†’ intermedia con 2 FK; 1:N â†’ FK del lado N.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-04-graph.svg]]
>
> **Ejemplo:** ESTUDIANTE(entidad) â†’ tabla; `carnet`(clave) â†’ PK; *toma*(N:M) â†’ MATRÃCULA con 2 FK. El detalle completo vive en la Unidad 2.

> [!info] ðŸ“– El deck de cÃ¡tedra: las tres formas de derivar relaciones (slides3, pp. 16-21)
> El deck cierra el mÃ³dulo con la derivaciÃ³n del modelo lÃ³gico segÃºn la cardinalidad, y usa los mismos ejemplos que Tiny College.

![[Archivos/bd-s03-p16.png]]

![[Archivos/bd-s03-p17.png]]

![[Archivos/bd-s03-p20.png]]

![[Archivos/bd-s03-p21.png]]

> **Entidad fuerte y dÃ©bil (p. 16):** `COURSE(CRS_CODE, â€¦)` y `CLASS(CLASS_CODE, CRS_CODE, â€¦)` con la `CRS_CODE` como foreign key.
>
> **1:N (p. 17):** la entidad **padre** es la del lado de uno y la **hija** la del lado de muchos; para representarla se copia el atributo clave del lado uno al lado muchos.
>
> **N:N (p. 20):** *"se crea una nueva Tabla para representar la relaciÃ³n (ER) y se incluyen todos los atributos de la relaciÃ³n"*.
>
> **Recursiva (p. 21):** *"se incluye una copia de la clave primaria pero se renombra"* â€” `EMPLOYEE(EMP_NUM, â€¦, MANAGER_EMP)` con `MANAGER_EMP` como FK a la misma tabla.

> [!info] ðŸ“– El deck de cÃ¡tedra: elementos del modelo relacional (slides3, pp. 6-10)
> *"Creado por Edgar F. Codd a principios de los 70, laboratorios de IBM. Modelo lÃ³gico de datos no de muy alto nivel, orientado a registro. SÃ³lida base teÃ³ricaâ€¦"* (p. 6).

![[Archivos/bd-s03-p7.png]]

![[Archivos/bd-s03-p8.png]]

![[Archivos/bd-s03-p10.png]]

> **Claves (p. 8):** *"una clave candidata es el atributo o conjunto de atributos que identifica de manera Ãºnica a cada tupla de la relaciÃ³n"*; la **clave primaria** es la candidata elegida; la **clave forÃ¡nea** referencia la primaria de otra relaciÃ³n.
>
> **RepresentaciÃ³n del esquema (p. 10):** el deck escribe el esquema completo con la sintaxis `CLIENTE(codcli, nombre, â€¦)` â€” el formato exacto que se usa en los ejercicios de conversiÃ³n de la Unidad 2.

### 4ï¸âƒ£ Entidad dÃ©bil â€” doble condiciÃ³n

> [!note] ðŸ“‹ DefiniciÃ³n â€” Entidad dÃ©bil (Coronel 4.1.6)
>
> Cumple AMBAS: existencia-dependiente + PK derivada del padre. Chen: rectÃ¡ngulo **doble**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-05-graph.svg]]
>
> **Ejemplo:** DEPENDENT se identifica con `EMP_NUM + DEP_NUM` juntos: `EMP_NUM` dice *de quÃ© empleado es* (heredado del padre) y `DEP_NUM` lo distingue *entre los dependientes de ese empleado* (1Âº, 2Âº...). Ni uno solo identifica: el mismo `DEP_NUM = 1` existe en mil empleados. Sin el empleado no existe ni se identifica.
>
> **Pista del enunciado (caso banco):** *"se numera desde 1 dentro de cada cuenta"* = el nÃºmero se repite entre cuentas â†’ TRANSACCION es dÃ©bil; en Chen su identificador va subrayado discontinuo y su clave real es `num_cuenta + num_transaccion`.
>
> > [!quote] ðŸ“– C. Zavaleta, *MER: guÃ­a completa*, caso entidad bancaria (2026)
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-06-graph.svg]]
>
> **Se lee asÃ­:** rectÃ¡ngulo doble = dÃ©bil (DEPENDENT cuelga de EMPLOYEE); rectÃ¡ngulo simple que existe solo = fuerte (PART con partes propias no necesita a VENDOR).

### 5ï¸âƒ£ Fuerza de relaciÃ³n â€” punteada vs sÃ³lida

> [!note] ðŸ“‹ DefiniciÃ³n â€” Fuerza (Coronel 4.1.7)
>
> - **DÃ©bil (non-identifying):** la PK hija NO hereda del padre (solo FK); lÃ­nea **punteada**. Ej.: CLASS con `CLASS_CODE` propia.
> - **Fuerte (identifying):** la PK hija hereda del padre (PK compuesta); lÃ­nea **sÃ³lida**. Ej.: CLASS con `CRS_CODE + CLASS_SECTION`.
> - Chen no distingue fuerza (es conceptual); Crow's Foot sÃ­ (afecta implementaciÃ³n). La fuerza la decide el diseÃ±ador segÃºn transacciones y eficiencia.
>
> **Figuras:** ver los dos diagramas de CLASS en Ejemplos Trabajados (versiÃ³n dÃ©bil y versiÃ³n fuerte).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-07-er.svg]]
>
> **Se lee en patas:** la lÃ­nea **punteada** = no identifica (la hija tiene PK propia); la **sÃ³lida** = identifica (la PK hija hereda la del padre).

### 6ï¸âƒ£ Supertipoâ€“subtipo â€” lo comÃºn arriba, lo propio abajo (unidad1.3-1.5 Â§Â§41â€“45)

> [!note] ðŸ“‹ DefiniciÃ³n â€” Supertipo y subtipo
>
> - **Supertipo:** 2+ entidades comparten atributos o relaciones (CLIENTES: idCliente, nombre, direcciÃ³nâ€¦).
> - **Subtipo:** tiene atributos o relaciones **propias** (EMPRESA: RUC; Persona: cÃ©dula) y **hereda todo** lo del supertipo, incluido el **identificador compartido**.
>
> **NotaciÃ³n:** lÃ­nea **simple** = subtipo opcional; lÃ­nea **doble** = supertipo obligatorio. CÃ­rculo **d** = solo un subtipo (disjunto); **o** = varios a la vez (sobrelapado).
>
> **Ejemplo:** todo EMPLEADO tiene idEmp/nombre; solo VENDEDOR tiene numVentas. La conversiÃ³n a tablas depende del caso (a/b/c/d) â€” ver Regla 6 de la Unidad 2.

### 7ï¸âƒ£ Recursiva â€” la entidad que se relaciona consigo misma

> [!note] ðŸ“‹ DefiniciÃ³n â€” RelaciÃ³n reflexiva
>
> La misma entidad en dos roles: EMPLEADO *supervisa* EMPLEADO (jefe vs supervisado). En tablas nace FK a sÃ­ misma (`idSupervisor` â†’ `idEmpleado`); si es M:N, tabla puente con doble FK.
>
> **Ejemplo:** sin roles etiquetados el diagrama es ilegible â€” rotula cada rama.

### 8ï¸âƒ£ Ternaria vs entidad + binarias â€” cuÃ¡ndo partir

> [!note] ðŸ“‹ DefiniciÃ³n â€” Ternaria (unidad1.3-1.5 Â§Â§37â€“38)
>
> Tres entidades en UNA relaciÃ³n (Clienteâ€“Productoâ€“Compraâ€“Tienda) solo si el hecho necesita a las tres a la vez. Si se puede contar por pares, parte en binarias. En tablas: una tabla con las 3 PK como (PK,FK) + atributos propios (calificaciÃ³n).
>
> **Ejemplo:** REGISTRO(idProf, matricula, idMateria PK,FK + calificacion): la nota solo existe con profe + alumno + materia juntos.

---

## ðŸ§µ NotaciÃ³n de Chen a Fondo

### ðŸŽ­ Cada SÃ­mbolo Tiene un Trabajo

> [!example] ðŸ§ª Leer Chen como Profesional
>
> | SÃ­mbolo | Significado | Ejemplo |
> |---|---|---|
> | **RectÃ¡ngulo simple** | Entidad fuerte | ESTUDIANTE |
> | **RectÃ¡ngulo doble** | Entidad dÃ©bil | DEPENDENT |
> | **Rombo** | RelaciÃ³n con verbo | *dicta*, *toma* |
> | **Ã“valo** | Atributo | Nombre, cÃ³digo |
> | **Ã“valo + lÃ­nea punteada** | Atributo derivado (calculado) | Edad desde fecha |
> | **Subrayado** | Clave (PK) | `carnet` |
> | **Cardinalidad** | Del lado de la entidad **relacionada** | (1,4) junto a CLASS |
>
> Solo Chen marca derivados con punteada (Crow's Foot no tiene cÃ³mo). M:N existe en conceptual pero no va al relacional.
>
> *(Leyenda Chen: ver el diagrama dibujable de abajo â€” rectÃ¡ngulo, rombo, Ã³valo, punteada y subrayado.)*
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-08-graph.svg]]
>
> **CÃ³mo leerlo:** rectÃ¡ngulo = entidad (doble rectÃ¡ngulo = dÃ©bil) Â· rombo `{ }` = relaciÃ³n Â· Ã³valo `([ ])` = atributo Â· punteada `-.-` = derivado Â· subrayado = PK. CompÃ¡ralo con la tabla de arriba: es el mismo Chen, dibujable en cualquier nota.

---

## ðŸ› ï¸ MÃ©todo para Pasar del ERD a Tablas

> [!note] ðŸ“‹ Procedimiento General
>
> 1. Verifica el ERD: toda entidad con PK, toda relaciÃ³n con verbo y cardinalidad.
> 2. Crea una tabla por entidad con sus columnas y PK.
> 3. Resuelve cada N:M con tabla intermedia (las 2 FK, PK compuesta).
> 4. Coloca cada FK del lado N con su contraparte PK.
> 5. Decide fuerza: Â¿hereda la PK o no? Dibuja punteada/sÃ³lida en consecuencia.
> 6. Ordena creaciÃ³n y carga: lado 1 primero (padres antes que hijas).
>
> **Principio clave:** el orden de carga no es decorativo â€” violarlo rompe integridad referencial.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-09-flow.svg]]

---

## ðŸŽ¨ Ejemplos Trabajados: Tiny College

> [!example] ðŸŸ¢ Ejemplo â€” CLASS DÃ©bil vs Fuerte
>
> Misma realidad, dos decisiones de clave:
>
> | VersiÃ³n | DefiniciÃ³n CLASS | LÃ­nea | CuÃ¡ndo |
> |---|---|---|---|
> | **DÃ©bil** | `CLASS(CLASS_CODE, CRS_CODE, ...)` â€” PK propia | Punteada | Identidad independiente |
> | **Fuerte** | `CLASS(CRS_CODE, CLASS_SECTION, ...)` â€” PK heredada | SÃ³lida | Identidad ligada al padre |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-10-er.svg]]
>
> **VersiÃ³n dÃ©bil (punteada):** CLASS tiene PK propia; solo referencia al padre con FK.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-11-er.svg]]
>
> **VersiÃ³n fuerte (sÃ³lida):** la PK de CLASS hereda `CRS_CODE` â€” sin el curso, la clase no se identifica.
>

> [!example] ðŸŸ¢ Ejemplo â€” Clasificar DIVISIONâ€“EMPLOYEE
>
> Solo sabes *"Una DIVISIÃ“N es manejada por un EMPLEADO"* â€” insuficiente:
>
> | Paso | AcciÃ³n |
> |---|---|
> | Pregunta de vuelta | Â¿Puede uno manejar varias? |
> | Si sÃ­ | 1:M: "Un EMPLEADO maneja muchas DIVISIONes" |
> | Si no | 1:1: "Un EMPLEADO maneja una sola DIVISIÃ“N" |
>

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-12-flow.svg]]

---

## ðŸ“‹ Tablas Comparativas

> [!note] ðŸ“‹ Chen vs Crow's Foot Â· DÃ©bil vs Fuerte
>
> | Aspecto | Chen | Crow's Foot |
> |---|---|---|
> | **Uso** | TeorÃ­a y parciales | Herramientas y pizarrÃ³n |
> | **Cardinalidad** | Lado de la relacionada | Junto a la entidad que aplica |
> | **Derivados** | LÃ­nea punteada âœ… | Sin marca âŒ |
> | **Fuerza** | No distingue | Punteada/sÃ³lida por PK |
>
> | VersiÃ³n CLASS | PK | LÃ­nea | CuÃ¡ndo |
> |---|---|---|---|
> | **DÃ©bil** | Propia | Punteada | Identidad independiente |
> | **Fuerte** | Heredada | SÃ³lida | Identidad ligada al padre |

---

## âš ï¸ Errores Comunes y Principios LÃ³gicos

> [!warning] âš ï¸ CÃ³mo leer esta secciÃ³n
> Cada error trae su dibujo: lo âŒ que delata el problema y lo âœ… que lo evita.

### âŒ Error 1: Tablas sin pasar por el ER

> [!danger] âŒ Viola: orden obligatorio ERD â†’ tablas â†’ SQL
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-13-graph.svg]]

### âŒ Error 2: Herencia de PK indecisa

> [!danger] âŒ Viola: decide fuerza antes de dibujar
>
> PK compuesta en el diagrama pero FK simple en tablas (o al revÃ©s): decide si hereda primero, verifica despuÃ©s.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-14-er.svg]]
>
> Si la lÃ­nea es sÃ³lida, la PK hija **debe** contener la del padre. Si es punteada, la hija tiene PK propia.

### âŒ Error 3: Cargar el lado N primero

> [!danger] âŒ Viola: padres antes que hijas
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-03-15-flow.svg]]

### âŒ Error 4: M:N directo al relacional

> [!danger] âŒ Viola: M:N existe en conceptual, no en tablas
>
> Sin intermedia no hay modelo que funcione: toda M:N produce tabla con las 2 FK (ver Regla 2 de la Unidad 2).

### âŒ Error 5: Subtipo sin nada propio (o ternaria que era binaria)

> [!danger] âŒ Viola: el subtipo debe aportar + la ternaria debe necesitar a los tres
>
> Subtipo sin atributos ni relaciones propias = no es subtipo, es un valor (usa discriminador o bandera). Y ternaria separable en pares = dos binarias con sus intermedias.
>
> **EL ERROR ESTÃ AQUÃ:** crear VENDEDOR sin numVentas "por si acaso", o dibujar ternaria Clienteâ€“Productoâ€“Tienda cuando Compra se cuenta por pares.

---

## ðŸ“ Ejercicios Propuestos

> [!info] â„¹ï¸ CÃ³mo trabajarlos
> Tapa la soluciÃ³n, resuelve, compara. Respuestas colapsables abajo.

### âœï¸ Ejercicio 1 â€” Â¿DÃ©bil o fuerte?

> [!example] ðŸ“‹ Planteamiento
>
> CLASS con `CLASS_CODE` propia vs CLASS con `CRS_CODE + CLASS_SECTION`. Â¿CuÃ¡l es dÃ©bil, cuÃ¡l fuerte, quÃ© lÃ­nea lleva cada una y cuÃ¡ndo elegirÃ­as cada versiÃ³n?
>
> > [!success]- âœ… SoluciÃ³n
> >
> > Propia = dÃ©bil (punteada): identidad independiente. Heredada = fuerte (sÃ³lida): identidad ligada al padre. Elige fuerte cuando la clase no se identifica sin el curso y las transacciones las piden juntas; dÃ©bil cuando la clase tiene vida propia.

### âœï¸ Ejercicio 2 â€” Los 7 sÃ­mbolos Chen

> [!example] ðŸ“‹ Planteamiento
>
> Nombra los 7 sÃ­mbolos Chen con su significado y un ejemplo de Tiny College para cada uno.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > RectÃ¡ngulo simple (fuerte: ESTUDIANTE), doble (dÃ©bil: DEPENDENT), rombo (relaciÃ³n: *toma*), Ã³valo (atributo: nombre), Ã³valo punteado (derivado: edad), subrayado (PK: carnet), cardinalidad del lado de la relacionada ((1,4) junto a CLASS).

### âœï¸ Ejercicio 3 â€” Resuelve la N:M

> [!example] ðŸ“‹ Planteamiento
>
> ESTUDIANTEâ€“MATERIA M:N con *toma*. Escribe las 3 tablas con PK/FK y el orden de carga.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > `ESTUDIANTE(carnet PK)`, `MATERIA(codigo PK)`, `MATRICULA(carnet PK,FK, codigo PK,FK)`. Carga: padres primero (las 2 entidades), intermedia al final. Sin intermedia no hay modelo que funcione.

### âœï¸ Ejercicio 4 â€” Supertipo, recursiva y ternaria

> [!example] ðŸ“‹ Planteamiento
>
> a) CLIENTES(idCliente, nombre) con EMPRESA(RUC) y Persona(cÃ©dula): Â¿quÃ© hereda cada subtipo y quÃ© identificador usan? b) Dibuja EMPLEADO *supervisa* EMPLEADO con roles. c) Â¿Compra de cliente/producto/tienda es ternaria o binarias? Justifica.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > - a) Ambos heredan idCliente/nombre y el identificador compartido; EMPRESA aporta RUC, Persona aporta cÃ©dula. Sin aporte propio no hay subtipo.
> > - b) Una entidad, dos roles (jefe/supervisado); en tablas: `idSupervisor` FK a `idEmpleado`.
> > - c) Ternaria solo si la compra exige a los tres a la vez (REGISTRO con 3 FK + calificacion); si se cuenta por pares, parte en binarias.

---

## ðŸŽ¯ Metas de Aprendizaje

> [!note] ðŸ“‹ Nivel BÃ¡sico
>
> - [ ] Defino relaciÃ³n, tupla, niveles conceptual/lÃ³gico/fÃ­sico sin mirar.
> - [ ] Dibujo los 7 sÃ­mbolos Chen con su significado.
> - [ ] Traduzco un ER simple a tablas con PKs y FKs.
>
> [!note] ðŸ“‹ Nivel Intermedio
>
> - [ ] Decido dÃ©bil vs fuerte por la PK y dibujo su lÃ­nea.
> - [ ] Resuelvo N:M con intermedia correcta.
> - [ ] Ordeno creaciÃ³n y carga sin romper integridad.
>
> [!note] ðŸ“‹ Nivel Avanzado
>
> - [ ] Comparo CLASS dÃ©bil vs fuerte justificando por transacciones.
> - [ ] Detecto en diagramas ajenos N:M olvidadas y fuerzas invertidas.

---

## ðŸ“š Referencias

> [!quote] ðŸ“– Fuentes Consultadas
>
> - `unidad1.3-1.5.pdf` (Irene Cheung) + Codd (relacional) Â· Chen 1976 (ERM).
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 4 Â§Â§4.1.6â€“4.1.7 y cap. 2 (Chen vs Crow's Foot).
> - C. Zavaleta, *MER: guÃ­a completa con ejemplos*, 2026 (casos prÃ¡cticos citados arriba).

---

## ðŸ” Repaso SR (flashcards)

#flashcards/bd-u1

> [!note] ðŸ§  Repasa con el plugin Spaced Repetition

- Â¿Relacional en 1 frase (Codd)?::Todo en tablas unidas por columna comÃºn, con base matemÃ¡tica.
- Â¿Chen 1976 aportÃ³ quÃ©?::El ERD grÃ¡fico que complementa al relacional para diseÃ±ar.
- Â¿DÃ©bil vs fuerte (lÃ­nea y PK)?::DÃ©bil: solo FK, punteada. Fuerte: PK heredada compuesta, sÃ³lida.
- Â¿N:M al relacional?::Tabla intermedia con las 2 FK.
- Â¿SÃ­mbolo Chen de entidad dÃ©bil y de derivado?::RectÃ¡ngulo doble; Ã³valo con lÃ­nea punteada.
- Â¿Por quÃ© "relacional" se llama asÃ­?::Porque guarda datos como relaciones (= tablas), no por las FK.
- Â¿Supertipo vs subtipo?::ComÃºn arriba (identificador compartido); propio abajo (hereda todo).
- Â¿d vs o (cÃ­rculo)?::Disjunto (solo uno) vs sobrelapado (varios a la vez).
- Â¿Ternaria cuÃ¡ndo?::Solo si el hecho exige a las tres entidades a la vez.

---

## ðŸ”— Conexiones

> [!quote] ðŸ”— Notas Relacionadas
>
> - [[02 - Entidades, atributos, claves y relaciones]] â€” el vocabulario que aquÃ­ se vuelve tablas.
> - [[01 - Dato, informaciÃ³n y modelos de datos]] â€” el problema original.
> - Ãlgebra relacional aplicada al taller 2 (Ïƒ, Ï€, â¨ y catÃ¡logo con âŸ•, âŸ–, â‹‰, Ï„): [[GuÃ­a de Problemas 2 - Ãlgebra Relacional y NormalizaciÃ³n]].
> - Ver tambiÃ©n la nota de **Claves** integrada en 02 si vienes de un link viejo: ahora vive ahÃ­.

---

## ðŸ”— Seguir estudiando

> [!info] ðŸ“š Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Ãndice Unidad 1: [[00 - Ãndice Unidad 1]] Â· Ãndice Unidad 2: [[00 - Ãndice Unidad 2]]
> - Ãlgebra relacional con ejercicios: [[GuÃ­a de Problemas 2 - Ãlgebra Relacional y NormalizaciÃ³n]] (catÃ¡logo de operadores, diapositivas 3.1/3.2)
> - Anterior: [[02 - Entidades, atributos, claves y relaciones]]
> - ConversiÃ³n a tablas: [[01 - ConversiÃ³n MC a ML por cardinalidad]] Â· [[02 - Primera forma normal y diccionario de datos]]

---

**Tags:** #TICG1018 #unidad1 #relacional #erm #chen #casos #bd

