---
dg-publish: true
tags: [TICG1018, unidad2, modelo-logico, conversion, ml]
---

# ðŸ”„ ConversiÃ³n del Modelo Conceptual al Modelo LÃ³gico

## ðŸŽ¯ IntroducciÃ³n

> [!info] ðŸ’¡ Â¿Por QuÃ© Convertir?
>
> El modelo conceptual (ER) dice **quÃ© existe**; el modelo lÃ³gico dice **cÃ³mo se guarda en tablas**. Convertir es traducir cada entidad, relaciÃ³n y restricciÃ³n a tablas + claves sin perder informaciÃ³n. Es el corazÃ³n de la LecciÃ³n 1.
>
> **DÃ³nde estamos en el diseÃ±o (3 pasos):**
>
> 1. **AnÃ¡lisis de requerimientos** â†’ quÃ© necesita el usuario.
> 2. **DiseÃ±o conceptual** â†’ se identifican datos y restricciones (ER).
> 3. **DiseÃ±o lÃ³gico y fÃ­sico** â†’ se crean tablas, relaciones, restricciones; luego procedimientos y triggers.
>
> **AnalogÃ­a del mundo real:** el ER es el plano arquitectÃ³nico; el ML es la lista de materiales con medidas exactas. El plano sin lista no se construye.
>
> | Concepto | Modelo Conceptual | Modelo LÃ³gico |
> |---|---|---|
> | **Entidad** | RectÃ¡ngulo Chen | Tabla |
> | **Atributo** | Ã“valo | Columna |
> | **Instancia** | â€” | Fila (tupla) |
> | **RelaciÃ³n** | Rombo | FK o tabla intermedia |
> | **Regla de oro** | QuÃ© existe | CÃ³mo se guarda |

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-01-graph.svg]]

---

## ðŸ“‹ Definiciones Formales

> [!info] â„¹ï¸ CÃ³mo leer esta secciÃ³n
> Una definiciÃ³n por bloque con su figura. Cada figura anticipa la regla donde se usa.

### 1ï¸âƒ£ Tabla, columna, fila â€” el vocabulario lÃ³gico

> [!note] ðŸ“‹ DefiniciÃ³n â€” Tabla, columna, fila, campo
>
> Tabla = relaciÃ³n; columna = atributo con dominio; fila = tupla; campo = intersecciÃ³n fila-columna.
> Equivalencia: tabla/fila/columna = archivo/registro/campo = relaciÃ³n/tupla/atributo.
>
> | Tabla EMPLEADO | idEmpleado (PK) | nombre |
> |---|---|---|
> | Fila 1 (tupla) | 101 | Ana |
> | Fila 2 (tupla) | 102 | Luis |
>
> **Ejemplo:** la columna `nombre` tiene dominio texto; el campo (102, nombre) vale `Luis`.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-02-graph.svg]]
>
> **Se lee asÃ­:** la tabla contiene filas y columnas; donde se cruzan hay un campo con exactamente un valor.

### 2ï¸âƒ£ Claves â€” PK, candidatas y compuestas

> [!note] ðŸ“‹ DefiniciÃ³n â€” Claves
>
> Una o mÃ¡s columnas que identifican filas. **Ãšnica** = una fila; **compuesta** = 2+ atributos; **primaria (PK)** = Ãºnica por tabla (representa la tabla en relaciones, organiza almacenamiento, genera Ã­ndices); **candidatas** = Ãºnicas adicionales no elegidas.
>
> **Ejemplo:** en REGISTRO ninguna columna sola identifica (un profesor dicta varias materias); `idProf + matricula + idMateria` sÃ­ â†’ PK compuesta de 3.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-03-er.svg]]
>
> **Se lee asÃ­:** `PK` identifica, `FK` referencia, `UK` es candidata no elegida (`nombre` Ãºnico pero no PK), `PK, FK` es compuesta que ademÃ¡s referencia.

### 3ï¸âƒ£ Integridad de entidad y referencial â€” lo que nunca se rompe

> [!note] ðŸ“‹ DefiniciÃ³n â€” Integridad
>
> - **De entidad:** la PK nunca es nula ni se repite.
> - **Referencial:** toda FK apunta a una PK que existe (la FK no necesita ser Ãºnica donde estÃ¡, pero sÃ­ donde apunta).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-04-flow.svg]]
>
> **Ejemplo:** matricular el carnet 999 inexistente se rechaza; la BD protege sola lo que en archivos habÃ­a que programar.

### 4ï¸âƒ£ Padre e hijo â€” quiÃ©n recibe la FK

> [!note] ðŸ“‹ DefiniciÃ³n â€” Padre / Hijo (en 1:M)
>
> El lado `1` es **padre**; el lado `M` es **hijo** y recibe la FK.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-05-er.svg]]
>
> **Ejemplo:** rotula el `1` primero y la direcciÃ³n sale sola (ver Regla 3).

### 5ï¸âƒ£ FusiÃ³n de tablas â€” el ML mÃ­nimo

> [!note] ðŸ“‹ DefiniciÃ³n â€” FusiÃ³n
>
> El ML debe tener el **mÃ­nimo de tablas posible**: las de un solo atributo se eliminan y las 1:1 total-total se fusionan.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-06-graph.svg]]
>
> **Ejemplo:** EQUIPOâ€“PRESIDENTE (1,1)-(1,1) â†’ una sola tabla con `cedula_presi` dentro (ver Regla 4, caso C).

### 6ï¸âƒ£ Modelo lÃ³gico â€” el refinamiento

> [!note] ðŸ“‹ DefiniciÃ³n â€” Modelo lÃ³gico
>
> Refinamiento del conceptual donde se reducen/aumentan entidades y solo quedan las que serÃ¡n tablas; despuÃ©s **se normaliza**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-07-graph.svg]]
>
> **Ejemplo:** el rombo *toma* (conceptual) se vuelve tabla MATRÃCULA (lÃ³gico); luego 1FN verifica que no tenga grupos repetitivos.

---

## ðŸ› ï¸ MÃ©todo: Convertir Paso a Paso

> [!success] ðŸ† Protocolo de conversiÃ³n (Ãºsalo en la LecciÃ³n 1)
>
> 1. **Entidades â†’ tablas directas:** cada entidad es una tabla; sus atributos, columnas; su PK se mantiene.
> 2. **M:N â†’ tabla intermedia:** con las PK de ambos lados (PK,FK) + atributos propios de la relaciÃ³n.
> 3. **1:M â†’ FK al hijo:** copia la PK del padre (lado 1) como FK en el hijo (lado M); los atributos de la relaciÃ³n viajan al hijo.
> 4. **1:1 â†’ segÃºn participaciÃ³n** (ver tabla de 3 casos abajo).
> 5. **Especiales:** supertipo/subtipo, dependencia, recursiva (ver secciÃ³n).
> 6. **Normaliza** el esquema resultante (mÃ­nimo [[02 - Primera forma normal y diccionario de datos|1FN]]).

> [!info] ðŸ“– El deck de cÃ¡tedra: los puntos clave de la conversiÃ³n (slides3, pp. 13-15)
> El deck del Ing. Magallanes enuncia las mismas reglas, con la formulaciÃ³n del docente: *"las relaciones del MER se clasifican como uno a uno (1:1), uno a muchos (1:N) y de muchos a muchos (M:N o N:N)"*.

![[Archivos/bd-s03-p16.png]]

> **El objetivo (p. 14):** *"traducir un modelo conceptual a un modelo lÃ³gico y luego validar si este modelo es de una estructura correcta"*.
>
> **Las estructuras que se derivan (p. 15):** entidad fuerte Â· entidad dÃ©bil Â· relaciÃ³n binariaâ€¦ â€” el deck cierra la lista con los casos especiales que esta nota develops en las reglas 5-8.

### ðŸ” Regla 1 â€” Entidades â†’ tablas directas

> [!note] ðŸ“‹ Cada entidad, una tabla
>
> Cada entidad del modelo conceptual se transforma directamente en una tabla: los atributos pasan a ser columnas y la clave primaria se mantiene.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-08-er.svg]]
>
> **Se lee asÃ­:** la entidad CLIENTE con 4 atributos produce una tabla de 4 columnas donde `idCliente` identifica cada fila.

---

### ðŸ” Regla 2 â€” M:N â†’ tabla intermedia siempre

> [!example] ðŸ§ª Rentar (CLIENTEâ€“PROPIEDAD)
>
> La relaciÃ³n se convierte en tabla con las claves primarias de **ambas** entidades (cada una PK y FK a la vez), mÃ¡s los atributos propios de la relaciÃ³n.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-09-er.svg]]
>
> **Se lee asÃ­:** `RENTAR` no existÃ­a como entidad, nace de la relaciÃ³n; sus dos claves apuntan a cada lado y las fechas viven con ella.
>
> **Mismo patrÃ³n â€” Venta:** `DETALLE(idProd PK, FK, codigo PK, FK, cantidad)` entre PRODUCTO y VENTA; los `=` del diagrama de clase confirman quÃ© columna referencia a quÃ© PK.

---

### ðŸ” Regla 3 â€” 1:M â†’ la FK vive en el hijo

> [!example] ðŸ§ª Trabaja (EMPLEADOâ€“DEPARTAMENTO)
>
> El lado `1` es el **padre** y el lado `M` es el **hijo**: se copia la PK del padre como FK en la tabla del hijo. Si la relaciÃ³n tiene atributos propios, tambiÃ©n bajan al hijo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-10-er.svg]]
>
> **Se lee asÃ­:** un departamento tiene muchos empleados; cada empleado guarda `idDepartamento` diciendo a cuÃ¡l pertenece. `fechaTrabaja` (atributo del rombo) baja con Ã©l.
>
> **Mismo patrÃ³n â€” Registra:** `RESERVACION(idReservacion PK, fechaLlegada, horaLlegada, diasPermanencia, FK idUsuario)` recibe ademÃ¡s `fechaReservacion, horaReservacion` de la relaciÃ³n; `USUARIO` no recibe nada.

---

### ðŸ” Regla 4 â€” 1:1 â†’ tres casos por participaciÃ³n

> [!note] ðŸ“‹ Memoriza cada caso con su ejemplo
>
> **Caso A â€” (0,1) vs (1,1): propaga del (1,1) al (0,1).** Ejemplo CLIENTEâ€“PREFERENCIA (`establece`):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-11-er.svg]]
>
> **Se lee asÃ­:** no todo cliente fija preferencia (0,1), pero toda preferencia es de un cliente (1,1); la PK viaja al lado opcional.
>
> **Caso B â€” participaciÃ³n parcial: decide PADRE e HIJO.** Ejemplo PERSONAâ€“LICENCIA (`posee`): no toda persona tiene licencia (parcial), pero toda licencia es de una persona. La persona es padre, la licencia hija:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-12-er.svg]]
>
> **Se lee asÃ­:** la PK del padre (`cedula`) se copia al hijo como FK. `PERSONA` no recibe nada. Sin persona no hay licencia (pero sÃ­ hay personas sin licencia).
>
> **Caso C â€” (1,1) vs (1,1): unifica en una sola tabla.** Ejemplo EQUIPOâ€“PRESIDENTE (`tiene`):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-13-er.svg]]
>
> **Se lee asÃ­:** una sola tabla con la PK de cualquiera de las dos; los datos del presidente viven como columnas (`cedula_presi, nombre_presi...`).

---

### ðŸ” Regla 5 â€” Ternaria â†’ una tabla con las 3 claves

> [!example] ðŸ§ª Registro (PROFESORâ€“MATERIAâ€“ESTUDIANTE)
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-14-er.svg]]
>
> **Se lee asÃ­:** `REGISTRO` combina las 3 PK como clave compuesta (las 3 son FK a la vez) y cuelga `calificacion, hora` de la combinaciÃ³n completa.

---

### ðŸ” Regla 6 â€” Supertipoâ€“subtipo â†’ el caso manda: (a) 3 tablas, (b) 1 tabla, (c) mixto, (d) ancha

> [!note] ðŸ“‹ Las 4 conversiones del deck BD02 (una por combinaciÃ³n)
>
> **(a) {obligatorio, sobrelapado} â†’ 3 tablas** (cada tipo la suya, banderas en el padre):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-15-er.svg]]
>
> **(b) {obligatorio, disjunto} â†’ 1 sola tabla** con discriminador (nadie es dos cosas: no hacen falta hijos):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-16-er.svg]]
>
> **(c) {opcional, disjunto} â†’ supertabla + hijos solo si aplican** (`Tipo` admite nulo; el hijo lleva la PK como (PK,FK) cuando existe).
>
> **(d) {opcional, sobrelapado} â†’ 1 tabla ancha** (banderas + todos los atributos propios juntos; sin tablas hijas).
>
> **Se lee asÃ­:** (a) separa porque hay solape real; (b) colapsa porque el discriminador basta; (c) respeta lo opcional con nulos; (d) todo junto porque nada obliga a partir. La regla vieja *"una tabla por tipo"* solo valÃ­a para (a).
>
> **CÃ³mo detectar la jerarquÃ­a (caso empleados):** caza 2 frases â€” *"hay personal que no encaja"* = parcial; *"nadie desempeÃ±a dos perfiles"* = exclusiva. Si el enunciado calla, **pregunta al cliente**: no se adivina.
>
> **Regla de oro:** las relaciones salen de los **subtipos**, no del supertipo â€” *atiende* cuelga de VENDEDOR (un desarrollador no atiende clientes). Colgarla de EMPLEADO afirma que cualquiera puede tener clientes: error de modelado.
>
> > [!quote] ðŸ“– C. Zavaleta, *MER: guÃ­a completa*, caso empleados con generalizaciÃ³n (2026)

---

### ðŸ” Regla 7 â€” Dependencia â†’ la dÃ©bil hereda la PK fuerte

> [!example] ðŸ§ª Edificioâ€“Departamento
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-17-er.svg]]
>
> **Se lee asÃ­:** el departamento dÃ©bil no se identifica solo (`hab_num` se repite entre edificios); su PK es compuesta: la del fuerte heredada + su nÃºmero.

---

### ðŸ” Regla 8 â€” Recursiva â†’ FK a sÃ­ misma o intermedia doble

> [!example] ðŸ§ª SupervisiÃ³n y grupos de empleados
>
> **Recursiva 1:M** (un jefe supervisa empleados):
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-18-er.svg]]
>
> **Se lee asÃ­:** `idSupervisor` es FK que apunta a `idEmpleado` de la **misma** tabla (`idEmpleado = idSupervisor`).
>
> **Roles obligatorios (caso banco):** en reflexivas etiqueta cada rama (*principal* / *dependiente*) o el diagrama es ilegible. *Depende* (SUCURSALâ€“SUCURSAL): principal (0,n) vs dependiente (0,1) â€” hay oficinas que no dependen de ninguna.
>
> > [!quote] ðŸ“– C. Zavaleta, *MER: guÃ­a completa*, caso entidad bancaria (2026)
>
> **Recursiva M:N** (grupos donde ambos roles son empleados): tabla intermedia con doble FK â†’ `EMPLEADO_GRUPOS(idEmpSupervisor PK, FK, idEmpSupervisado PK, FK)`.

---

## ðŸ” ConversiÃ³n inversa â€” del ML al MC (viceversa)

> [!note] ðŸ“‹ DefiniciÃ³n â€” Leer tablas y reconstruir el ER
>
> Dadas las tablas con sus PK/FK, recupera el conceptual: cada tabla es una entidad, cada FK es una relaciÃ³n y cada tabla intermedia es un rombo. Es la lectura inversa del protocolo MCâ†’ML: si sabes convertir hacia adelante, sabes leer hacia atrÃ¡s buscando las huellas que dejÃ³ cada regla.
>
> | Huella en las tablas | Origen en el ER |
> |---|---|
> | Tabla con PK compuesta de 2 (PK,FK) + atributos propios | M:N con intermedia (Regla 2) |
> | Tabla con PK compuesta de 3 (PK,FK) | Ternaria (Regla 5) |
> | FK simple en una tabla | 1:M: la tabla con la FK es el hijo (Regla 3) |
> | PK que es a la vez FK a otra tabla | Supertipoâ†’subtipo o 1:1 fusionable (Regla 6 / caso C) |
> | FK que apunta a la misma tabla | Recursiva 1:M (Regla 8) |
> | Tabla intermedia con doble FK a la misma tabla | Recursiva M:N (Regla 8) |
> | Tabla de (FK + un valor) con PK compuesta | Multivaluado (U2-02 Â§6) |
> | PK heredada del fuerte + nÃºmero local | Entidad dÃ©bil (Regla 7) |
>
> **Protocolo inverso (en orden):**
>
> 1. Marca todas las PK y FK de cada tabla.
> 2. Las tablas cuya PK es compuesta solo de FK â†’ intermedias: dibuja el rombo con sus participantes.
> 3. Las FK simples â†’ flechas 1:M hacia el padre (la tabla referenciada).
> 4. Las PK compartidas â†’ supertipo (padre) y subtipos (hijos); si no hay atributos propios, era una 1:1 fusionable.
> 5. Reconstruye cardinalidades preguntando el negocio en ambas direcciones (U1-02 Â§frases): las tablas no guardan (x,y), tÃº las deduces.

### âœï¸ Ejercicio inverso 1 â€” MATRÃCULA

> [!example] ðŸ§ª Planteamiento
> - Tablas: `ESTUDIANTE(carnet PK, nombre)`, `MATERIA(cod PK, nombre)`, `MATRICULA(carnet PK/FK, cod PK/FK, nota)`. Reconstruye el ER.
>
> > [!success]- SoluciÃ³n
> > - MATRICULA tiene PK compuesta de 2 FK + atributo propio (nota) â†’ intermedia de M:N.
> > - ER: ESTUDIANTE â€”*toma*â€” MATERIA (M:N, atributo nota en el rombo); carnet y cod subrayados como PK.

### âœï¸ Ejercicio inverso 2 â€” El supervisor fantasma

> [!example] ðŸ§ª Planteamiento
> - Tablas: `EMPLEADO(id PK, nombre, idSup FKâ†’EMPLEADO)`, `VENDEDOR(id PK/FKâ†’EMPLEADO, numVentas)`, `VENTA(id PK, fecha, idEmp FKâ†’EMPLEADO)`. Reconstruye el ER.
>
> > [!success]- SoluciÃ³n
> > - idSup a la misma tabla â†’ recursiva *supervisa* 1:M con roles (supervisor/supervisado).
> > - VENDEDOR con PK compartida + atributo propio â†’ subtipo de EMPLEADO (supertipo, caso a).
> > - VENTA con FK simple â†’ EMPLEADO 1:M *realiza* (cuelga del supertipo: cualquiera vende, como el caso subsidio de la GuÃ­a 1).

---

## ðŸŽ¨ Ejemplo Trabajado Completo

> [!example] ðŸ’¡ De ER a tablas: trabaja (EMPLEADOâ€“DEPARTAMENTO)
>
> **ER de partida:** `EMPLEADO(idEmpleado, nombre, direcciÃ³n, telÃ©fono)` â€”(trabaja, fechaTrabaja)â†’ `DEPARTAMENTO(idDepartamento, nombre)`, cardinalidad M:1.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-19-graph.svg]]
>
> **ConversiÃ³n:**
>
> 1. Entidades â†’ tablas (PK se mantienen).
> 2. RelaciÃ³n 1:M â†’ FK al hijo + atributo `fechaTrabaja` al hijo.
>
> **Tablas resultantes:**
>
> | Tabla | Columnas (PK/FK marcadas) |
> |---|---|
> | **EMPLEADO** | idEmpleado PK int, nombre char(30), direcciÃ³n char(50), telÃ©fono int, **FK** idDepartamento int, fechaTrabaja date |
> | **DEPARTAMENTO** | idDepartamento PK int, nombre char(30) |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-20-er.svg]]
>
> **Se lee asÃ­:** el Chen de arriba convertido: el rombo desaparece, nace la FK en el hijo y `fechaTrabaja` baja con ella. Compara ambos dibujos lÃ­nea por lÃ­nea.
>
> **VerificaciÃ³n:** Â¿puedo despedir un departamento con empleados? No â€” la FK lo impide (integridad referencial). Â¿Dos empleados con mismo id? No â€” PK Ãºnica.

---

## ðŸ—ºï¸ Diagrama de DecisiÃ³n: Â¿CÃ³mo Convierto Esta RelaciÃ³n?

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-21-flow.svg]]

---

## âš ï¸ Errores Comunes y Principios LÃ³gicos

> [!warning] âš ï¸ CÃ³mo leer esta secciÃ³n
> Cada error trae su diagrama: primero lo **malo** (âŒ) y luego lo **correcto** (âœ…). Si tu conversiÃ³n se parece al primero, ya sabes quÃ© regla aplicar.

### âŒ Error 1: FK al revÃ©s en 1:M

> [!danger] âŒ Viola: direcciÃ³n padreâ†’hijo
>
> Poner la FK en el padre (lado 1) es absurdo: un departamento tendrÃ­a que apuntar a **uno** de sus 50 empleados.
>
> âŒ AsÃ­ NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-22-er.svg]]
>
> âœ… AsÃ­ SÃ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-23-er.svg]]
>
> **Regla que lo evita:** en 1:M el hijo (M) recibe; el padre (1) no apunta a nadie.

---

### âŒ Error 2: M:N sin tabla intermedia

> [!danger] âŒ Viola: primera forma normal (grupos repetitivos)
>
> Aplanar la relaciÃ³n en columnas numeradas crea un grupo repetitivo: Â¿y si una venta lleva 4 productos?
>
> âŒ AsÃ­ NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-24-er.svg]]
>
> âœ… AsÃ­ SÃ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-25-er.svg]]
>
> **Regla que lo evita:** toda M:N produce tabla intermedia con las PK de ambos lados.

---

### âŒ Error 3: 1:1 total-total en dos tablas

> [!danger] âŒ Viola: fusiÃ³n mÃ­nima de tablas
>
> Si cada equipo tiene exactamente un presidente y viceversa, dos tablas solo generan un JOIN obligatorio en cada consulta.
>
> âŒ AsÃ­ NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-26-er.svg]]
>
> âœ… AsÃ­ SÃ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-27-er.svg]]
>
> **Regla que lo evita:** caso C (1,1)-(1,1) se unifica en una sola tabla.

---

### âŒ Error 4: Atributos de la relaciÃ³n olvidados

> [!danger] âŒ Viola: preservaciÃ³n de informaciÃ³n
>
> Convertir `Registra` bajando solo la FK pero perdiendo `fechaReservacion, horaReservacion` destruye datos del conceptual.
>
> âŒ AsÃ­ NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-28-er.svg]]
>
> âœ… AsÃ­ SÃ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-29-er.svg]]
>
> **Regla que lo evita:** todo atributo del rombo viaja a la tabla que absorbe la relaciÃ³n.

---

### âŒ Error 5: Subtipo sin PK heredada

> [!danger] âŒ Viola: identidad del supertipo
>
> Darle al subtipo una PK propia rompe el vÃ­nculo: ya no se sabe quÃ© empleado es ese vendedor.
>
> âŒ AsÃ­ NO:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-30-er.svg]]
>
> âœ… AsÃ­ SÃ:
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-31-er.svg]]
>
> **Regla que lo evita:** cada subtipo lleva la PK del supertipo como (PK,FK) â€” en los casos (a) y (c); en (b) y (d) no hay tablas hijas que hereden.

---

## ðŸŽ¯ Mejores PrÃ¡cticas

> [!tip] ðŸ† Checklist de conversiÃ³n
>
> **1. Marca padre e hijo antes de escribir** â€” en 1:M no hay ambigÃ¼edad si rotulas el `1`.
>
> **2. Dibuja los `=` de referencia** â€” como en el diagrama de clase: cada FK anota a quÃ© PK apunta.
>
> **3. Cuenta tablas al final** â€” Â¿alguna tiene un solo atributo? ElimÃ­nala. Â¿Alguna 1:1 total-total? FusiÃ³nala.
>
> **4. Lee la relaciÃ³n en voz alta** â€” "un empleado trabaja en un departamento" te dice dÃ³nde va la FK.
>
> **5. Normaliza despuÃ©s** â€” la conversiÃ³n produce el esquema; [[02 - Primera forma normal y diccionario de datos|1FN]] lo valida.

---

## ðŸ“ Ejercicios Propuestos

> [!info] â„¹ï¸ CÃ³mo trabajarlos
> Cada ejercicio trae su **planteamiento visual** (lo que te dan) y la **soluciÃ³n guiada** (cÃ³mo se llega). Tapa la soluciÃ³n, resuelve, compara.

### âœï¸ Ejercicio 1 â€” Ternaria con atributos

> [!example] ðŸ“‹ Planteamiento
>
> Convierte esta relaciÃ³n ternaria: `ESTUDIANTE(MatrÃ­cula PK, nombre, apellido)` â€”registra(calificaciÃ³n, hora)â†’ `MATERIA(idMateria PK, nombre, descripciÃ³n)`, con `PROFESOR(idProf PK, ...)` como tercer participante.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-32-er.svg]]
>
> > [!success]- âœ… SoluciÃ³n guiada
> >
> > 1. Las 3 entidades dan 3 tablas con sus PK intactas.
> > 2. La ternaria produce `REGISTRO` con las 3 PK como (PK,FK) cada una.
> > 3. `calificacion, hora` cuelgan de la combinaciÃ³n completa.
> >
> > | Tabla | Claves |
> > |---|---|
> > | ESTUDIANTE | Matricula PK, nombre, apellido |
> > | MATERIA | idMateria PK, nombre, descripciÃ³n |
> > | PROFESOR | idProf PK, ... |
> > | REGISTRO | idProf PK,FK + Matricula PK,FK + idMateria PK,FK + calificacion + hora |

---

### âœï¸ Ejercicio 2 â€” Supertipo con pregunta trampa

> [!example] ðŸ“‹ Planteamiento
>
> `PRODUCT` supertipo con subtipos `CD` y `BOOK`. Â¿Es obligatorio que toda instancia de PRODUCT estÃ© asociada a un CD? Â¿Puede un BOOK no aparecer en PRODUCT? Dibuja la implementaciÃ³n segÃºn tu respuesta.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-33-er.svg]]
>
> > [!success]- âœ… SoluciÃ³n guiada
> >
> > 1. La respuesta depende de la restricciÃ³n: si es {obligatorio, disjunto}, todo PRODUCT es CD o BOOK y ningÃºn BOOK vive fuera de PRODUCT.
> > 2. Si es {opcional,...}, sÃ­ puede haber PRODUCT sin subtipo.
> > 3. ImplementaciÃ³n: `CD(idProd PK,FK, ...)` y `BOOK(idProd PK,FK, ...)`; discriminante `tipo` si es disjunto.
> >
> > **Trampa del ejercicio:** sin la restricciÃ³n {obligatorio/opcional, disjunto/sobrelapado} no hay respuesta Ãºnica â€” en la lecciÃ³n, exige el dato antes de convertir.

---

### âœï¸ Ejercicio 3 â€” Taller pata de gallo

> [!example] ðŸ“‹ Planteamiento
>
> Convierte a lÃ³gico el diagrama del taller en notaciÃ³n pata de gallo (ejercicio de clase).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-34-flow.svg]]
>
> > [!success]- âœ… SoluciÃ³n guiada
> >
> > 1. Traduce cada pata a cardinalidad con el diagrama de decisiÃ³n de esta nota.
> > 2. Aplica el protocolo en orden: entidades â†’ M:N â†’ 1:M â†’ 1:1 â†’ especiales.
> > 3. Verifica con el checklist de Mejores PrÃ¡cticas antes de entregar.

---

### âœï¸ Ejercicio 4 â€” 1:1 con participaciÃ³n mixta

> [!example] ðŸ“‹ Planteamiento
>
> `CLIENTE(cÃ©dula PK, nombre, direcciÃ³n, telÃ©fono)` + `PREFERENCIA(id_pref PK, tipoPref, maxRent)`, relaciÃ³n `establece` con (0,1) del lado cliente y (1,1) del lado preferencia. Â¿QuÃ© caso 1:1 es y dÃ³nde va la FK?
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-01-35-er.svg]]
>
> > [!success]- âœ… SoluciÃ³n guiada
> >
> > 1. Participaciones (0,1) vs (1,1) â†’ **caso A**.
> > 2. La PK del lado (1,1) se propaga a la tabla del lado (0,1).
> > 3. Resultado: `PREFERENCIA(id_pref PK, tipoPref, maxRent, FK cedula)`; `CLIENTE` no recibe nada.

---

## ðŸ” Repaso SR (flashcards)

#flashcards/bd-u2
- Â¿3 pasos del diseÃ±o de BD?::Requerimientos â†’ conceptual (ER) â†’ lÃ³gico/fÃ­sico (tablas + triggers).
- Â¿Equivalencias tabla/fila/columna?::Archivo/registro/campo = relaciÃ³n/tupla/atributo.
- Â¿M:N al lÃ³gico?::Tabla intermedia con las PK de ambos lados como (PK,FK) + atributos de la relaciÃ³n.
- Â¿1:M dÃ³nde va la FK?::En el hijo (lado M); el padre (lado 1) no recibe nada.
- Â¿1:1 caso A, B y C?::A: (0,1)-(1,1) propaga PK del 1,1 al 0,1. B: parcial, PK del padre al hijo. C: (1,1)-(1,1) unifica en una tabla.
- Â¿Supertipo-subtipo al lÃ³gico?::(a) 3 tablas con banderas; (b) 1 tabla con discriminante tipo; (c) supertabla + hijos opcionales; (d) 1 tabla ancha.
- Â¿DÃ©bil y recursiva?::DÃ©bil: PK del fuerte como (PK,FK). Recursiva 1:M: FK a sÃ­ misma; M:N: intermedia con doble FK.
- Â¿FusiÃ³n de tablas en 1 lÃ­nea?::MÃ­nimo de tablas: elimina las de 1 atributo y fusiona 1:1 total-total.
- Â¿CÃ³mo detecto jerarquÃ­a parcial/exclusiva?::"No encaja en ninguno" = parcial; "nadie dos perfiles" = exclusiva; si calla, pregunto.
- Â¿Reflexiva bien dibujada?::Etiqueto roles (principal/dependiente) en cada rama.
- Â¿Intermedia con 2 FK en la PK quÃ© fue?::M:N con atributos propios (el rombo): la leo como relaciÃ³n, no como entidad.
- Â¿PK compartida como (PK,FK) quÃ© fue?::Subtipo del supertipo referenciado (o 1:1 total-total si no aporta nada).
- Â¿FK a sÃ­ misma quÃ© fue?::Recursiva 1:M con roles; doble FK a la misma tabla: recursiva M:N.

> [!note] ðŸ§  Repasa con el plugin Spaced Repetition (LecciÃ³n 1: 13-oct)
## ðŸš€ PrÃ³ximos Pasos

> [!quote] ðŸŒŸ Continuando
>
> **Has aprendido:**
>
> âœ… Protocolo de conversiÃ³n MCâ†’ML por cardinalidad
> âœ… Los 3 casos 1:1 + especiales (supertipo, dÃ©bil, recursiva)
> âœ… FusiÃ³n mÃ­nima de tablas
>
> **Siguiente:**
>
> | Tema | QuÃ© verÃ¡s | Por quÃ© importa |
> |---|---|---|
> | **1FN y diccionario** | 5 condiciones + documento por tabla | Valida tu conversiÃ³n (LecciÃ³n 1) |

---

## ðŸ”— Seguir estudiando

> [!info] ðŸ“š Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Ãndice Unidad 2: [[00 - Ãndice Unidad 2]]
> - Siguiente: [[02 - Primera forma normal y diccionario de datos]]
> - Base: [[01 - Dato, información y modelos de datos]] Â· [[02 - Entidades, atributos, claves y relaciones]] Â· [[03 - Modelo relacional, ERM y casos Tiny College]]

## ðŸ“š Referencias

> [!quote] ðŸ“– Fuentes
>
> - Diapositivas BD 02 MC_a_ML (Irene Cheung): diseÃ±o en 3 pasos, conversiÃ³n por cardinalidad, supertipo-subtipo, dependencia, recursiva, 1FN, diccionario.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 4 (claves) y cap. 6 (normalizaciÃ³n).

---

**Tags:** #TICG1018 #unidad2 #ml #conversion #bd

