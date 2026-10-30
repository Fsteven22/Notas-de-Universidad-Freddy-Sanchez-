---
dg-publish: true
tags: [TICG1018, unidad1, er, claves, relaciones]
---

# ðŸ§© Entidades, Atributos, Claves y Relaciones

## ðŸŽ¯ IntroducciÃ³n

> [!info] ðŸ’¡ Â¿Por QuÃ© Todo Diagrama Empieza con Sustantivos y Verbos?
>
> Un ERD mal leÃ­do aprueba diagramas imposibles: relaciones sin verbo, tablas sin clave, cardinalidades adivinadas. Este vocabulario (5 piezas) es el filtro con el que validarÃ¡s cada diagrama del curso, del proyecto y de la LecciÃ³n 1 â€” leerlo en voz alta detecta relaciones falsas en segundos.
>
> **Aplicaciones:**
> - **DiseÃ±o de BD:** cada diagrama del curso y del proyecto usa estas piezas.
> - **ValidaciÃ³n:** leer un ER en voz alta detecta relaciones falsas en segundos.
> - **LecciÃ³n 1 (13-oct):** definir cada pieza con ejemplo propio es pregunta segura.

![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-01-graph.svg]]

---

## ðŸ“‹ Definiciones Formales

> [!info] â„¹ï¸ CÃ³mo leer esta secciÃ³n
> Una definiciÃ³n por bloque, cada una con su ejemplo y su figura. Todo en Chen: rectÃ¡ngulo = entidad, rombo = relaciÃ³n, Ã³valo = atributo, subrayado = clave.

### 1ï¸âƒ£ Entidad â€” lo que existe por sÃ­ mismo

> [!note] ðŸ“‹ DefiniciÃ³n â€” Entidad
>
> Objeto distinguible del mundo real; cada instancia es Ãºnica y se identifica por clave. Dibuja rectÃ¡ngulo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-02-graph.svg]]
>
> **Ejemplo:** ESTUDIANTE existe aunque nadie lo mencione; `nombre` y `carrera` lo describen pero no son entidades.

### 2ï¸âƒ£ Atributo â€” lo que describe

> [!note] ðŸ“‹ DefiniciÃ³n â€” Atributo
>
> Propiedad que describe a una entidad (Ã³valo) o a una relaciÃ³n. La **clave** identifica; el resto describe.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-03-graph.svg]]
>
> **Ejemplo:** `cedula` identifica (clave, subrayada); `nombre` y `direccion` describen. Si un dato describe a otro dato, es atributo, no entidad.

> [!note] ðŸ“‹ TaxonomÃ­a â€” Simple, compuesto, derivado, multivaluado (unidad1.3-1.5 Â§15)
>
> | Tipo | QuÃ© es | Ejemplo | A tablas |
> |---|---|---|---|
> | **Simple** | AtÃ³mico, no se subdivide | `salario`, `cargo` | Columna directa |
> | **Compuesto** | Se parte en sub-atributos | `direccion` â†’ calle + mz; `fecha` â†’ dd-mm-yyyy | Columnas por parte |
> | **Derivado** | Se calcula de otros | `edad` â† `fecha_nacimiento`; `subtotal` | Preferir el base (no volÃ¡til) |
> | **Multivaluado** | N valores por instancia (1..*) | `telefono`, **`idiomas`** | âš ï¸ Pide tabla propia (1FN) |
>
> **VolÃ¡til vs no volÃ¡til:** la *edad* cambia sola (volÃ¡til, mala PK y mala columna); la *fecha_nacimiento* no (Ãºsala a ella).
>
> **Caso Idiomas (tu captura ERDPlus):** â˜‘ Multivalued en `Idiomas` = un empleado habla varios â†’ en el lÃ³gico nace `IDIOMA(cedula PK,FK + idioma PK)`. Marcar Unique serÃ­a mentir (se repite); Derived no (no se calcula); Composite no (no se parte).
>
> **Se lee asÃ­:** ante un atributo pregunta *Â¿uno o varios?* (multivaluado), *Â¿se parte?* (compuesto), *Â¿se calcula?* (derivado). Lo que sobre es simple.

> [!info] ðŸ“– El deck de cÃ¡tedra: la taxonomÃ­a de atributos en figuras (slides02, pp. 7-10)
> El deck del Ing. Magallanes recorre los tipos de atributo con su figura: el **compuesto** (un nÃºmero de telÃ©fono se subdivide en cÃ³digo de paÃ­s, cÃ³digo de Ã¡rea y nÃºmero), el **multivaluado** y el **derivado**.

![[Archivos/bd-s02-p8.png]]

![[Archivos/bd-s02-p10.png]]

> **Atributo requerido (p. 8):** *"un atributo que debe tener valor o no puede ser vacÃ­o (Not null)"*.
>
> **Identificadores (p. 9):** *"uno o mÃ¡s atributos que identifican a cada instancia de una Entidad"* â€” en el modelo relacional, la entidad es una tabla y el identificador es la clave primaria.

### 3ï¸âƒ£ RelaciÃ³n â€” el verbo que conecta

> [!note] ðŸ“‹ DefiniciÃ³n â€” RelaciÃ³n
>
> AsociaciÃ³n con significado entre entidades (rombo con verbo). Se lee en voz alta: *"Â¿quiÃ©n toma quÃ©?"*.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-04-graph.svg]]
>
> **Ejemplo:** *toma* conecta ESTUDIANTE con MATERIA. Sin verbo no hay relaciÃ³n (ver Error 1: lÃ­nea muda).

> [!info] ðŸ“– El deck de cÃ¡tedra: relaciÃ³n, cardinalidad y grado (slides02, pp. 11-19)
> *"Una RelaciÃ³n representa a un conjunto de asociaciones entre las instancias u ocurrencias de Entidades"* (p. 12). El deck dibuja la cardinalidad con el par (mÃ­n, mÃ¡x) por lado.

![[Archivos/bd-s02-p13.png]]

![[Archivos/bd-s02-p15.png]]

> **Las dos preguntas del deck (p. 14):** para Departamento, *"un empleado trabaja mÃ­nimo en cuÃ¡ntos departamentos?"* â€” si es 0, la participaciÃ³n del empleado es **opcional**; y el mÃ¡ximo define si es 1:1, 1:N o N:N.
>
> **Cardinalidad (p. 13):** *"el nÃºmero mÃ­n y mÃ¡x de ocurrencias de la Entidad con relaciÃ³n a una ocurrencia de la otra"*.
>
> **Grado (p. 16):** el nÃºmero de entidades que participan â€” casi todas son binarias, pero las ternarias y superiores estÃ¡n permitidas.

![[Archivos/bd-s02-p17.png]]

![[Archivos/bd-s02-p19.png]]

> **Relaciones recursivas (p. 17):** un empleado puede dirigir a muchos empleados (0,N) y ser dirigido por uno (0,1); un curso puede ser prerrequisito de otros.
>
> **Los cuatro tipos (p. 19):** *"en la fig. 'nace' es una relaciÃ³n N:1 y 'reside' es una relaciÃ³n N:N"*. El deck avisa: **una relaciÃ³n N:N en el E/R se convierte en una nueva tabla en el relacional** â€” es la regla 2 de la conversiÃ³n.

> [!info] ðŸ“– El deck de cÃ¡tedra: generalizaciÃ³n y herencia (slides02, pp. 26-28)
> *"Car y Truck son sub-clases o especializaciones de Vehicule y por lo tanto heredan los atributos y relaciones"* (p. 28).

![[Archivos/bd-s02-p26.png]]

![[Archivos/bd-s02-p28.png]]

### 4ï¸âƒ£ Claves â€” PK, FK, candidata y compuesta

> [!note] ðŸ“‹ DefiniciÃ³n â€” Claves
>
> - **Primaria (PK):** Ãºnica + no nula + estable + mÃ­nima. Identifica cada instancia.
> - **ForÃ¡nea (FK):** copia de una PK ajena que conecta tablas (vive en el lÃ³gico, se dibuja como Ã³valo marcado).
> - **Candidata:** podrÃ­a ser PK pero no fue elegida (queda como reserva Ãºnica).
> - **Compuesta:** PK de 2+ atributos que solo juntos identifican.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-05-graph.svg]]
>
> **Ejemplo:** en MATRÃCULA ni `carnet` ni `codigo` identifican solos; juntos sÃ­ â†’ PK compuesta donde cada parte es FK a su tabla.
>
> > [!tip]- ðŸ’¡ PK artificial + vocabulario ERDPlus (tu captura Dicta)
> >
> > - **Artificial:** incremental sin significado (`id_pref`, `idRenta`) â€” Ãºsala cuando ninguna candidata es estable; nunca describe nada.
> > - **Min (Mandatory/Optional/Unspecified):** Mandatory = mÃ­nimo 1 (todo curso se dicta); Optional = mÃ­nimo 0 (puede no participar). Es tu `x` de `(x,y)`.
> > - **Max (One/Many):** One = a lo mÃ¡s 1; Many = N. Es tu `y` â€” y decide si la FK viaja o nace intermedia.
> > - **â˜‘ Identifying:** prendido = la PK del padre **entra a la PK** del hijo (MATRÃCULA, dÃ©bil). Apagado = FK normal (Dicta: el curso se dicta exista o no esa fila).
> > - **Exact constraints:** para topes exactos (1..4) en vez de rangos.

### 5ï¸âƒ£ RestricciÃ³n â€” lo que el negocio manda

> [!note] ðŸ“‹ DefiniciÃ³n â€” RestricciÃ³n y reglas de negocio
>
> LÃ­mite que el diagrama debe cumplir: cardinalidad, cupos, prerrequisitos. Las **reglas de negocio** mandan sobre el dibujo: si el negocio dice "mÃ¡ximo 4 materias", el ER lo refleja.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-06-graph.svg]]
>
> **Se lee asÃ­:** cada regla cae en un elemento del dibujo. *"Sin cupo no hay matrÃ­cula"* â†’ FK obligatoria no nula. *"MÃ¡ximo 4 materias"* â†’ (1,4).
>
> **Ejemplo:** *"Cada profesor dicta de 1 a 4 clases"* â†’ cardinalidad (1,4) junto a CLASS. *"Sin cupo no hay matrÃ­cula"* â†’ FK obligatoria no nula.

### 6ï¸âƒ£ Conectividad â€” la clasificaciÃ³n en ambas direcciones

> [!note] ðŸ“‹ DefiniciÃ³n â€” Conectividad (Coronel 4.1.4)
>
> ClasificaciÃ³n 1:1, 1:M, M:N â€” siempre en **ambas direcciones**: *"un CLIENTE genera muchas FACTURAS"* + *"cada FACTURA es de un CLIENTE"* â†’ 1:M.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-07-graph.svg]]
>
> **Ejemplo:** lee el dibujo en voz alta en los dos sentidos antes de clasificar.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-08-er.svg]]
>
> **Leyenda pata de gallo â†’ (x,y):**
>
> - Barra `||` = exactamente 1 â†’ (1,1).
> - CÃ­rculo `o` = cero opcional â†’ (0,x).
> - Pata `}o` / `o{` = muchos â†’ (x,N).
> - `||--||` = (1,1)-(1,1).
> - `||--o{` = (1,1)-(0,N).
> - `}o--o{` = (0,N)-(0,N).
>
> Lee el sÃ­mbolo y ya no memorizas nÃºmeros.

### 7ï¸âƒ£ Cardinalidad â€” el (x,y) de cada lado

> [!note] ðŸ“‹ DefiniciÃ³n â€” Cardinalidad (x,y)
>
> Dos nÃºmeros por lado: **mÃ­nimo** (Â¿puede ser cero?) y **mÃ¡ximo** (Â¿cuÃ¡ntos a lo mÃ¡s?).
>
> - `(1,1)` = exactamente 1: mÃ­nimo 1 y mÃ¡ximo 1. Cada clase tiene un y solo un profesor.
> - `(1,4)` = de 1 a 4: mÃ­nimo 1 (todo profesor dicta al menos una) y mÃ¡ximo 4 (a lo mÃ¡s cuatro).
> - `(0,N)` = opcionales muchos: mÃ­nimo 0 (puede no tener) y mÃ¡ximo sin tope.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-09-graph.svg]]
>
> **CÃ³mo colocarlo:** Chen lo escribe del lado de la entidad **relacionada**; Crow's Foot/UML junto a la entidad a la que aplica. Y ojo: el DBMS **no** implementa cardinalidad en tablas â€” vive en la app o en triggers.
>
> **El cero importa:** `ALUMNO (0,n)` en *matricula* = un reciÃ©n ingresado aÃºn no se matriculÃ³ en nada. Lee siempre el mÃ­nimo: el 0 cuenta historias.
>
> **Se lee en patas:** del lado PROFESOR la barra `||` = cada clase tiene exactamente 1 profesor (1,1); del lado CLASE la pata `o{` = cada profesor dicta 0 a N clases (0,N). El (1,4) del ejemplo es una pata con tope: de 1 a 4.

### 8ï¸âƒ£ Dependencia â€” existir gracias a otro

> [!note] ðŸ“‹ DefiniciÃ³n â€” Dependencia de existencia (Coronel 4.1.5)
>
> - **Dependiente:** solo existe asociada a otra (FK obligatoria no nula). Ej.: DEPENDENT sin EMPLOYEE no existe.
> - **Fuerte (regular):** existe sola. Ej.: PART existe sin VENDOR si algunas partes son propias.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-10-graph.svg]]
>
> **Ejemplo:** borra al empleado y sus dependientes pierden sentido; borra un proveedor y tus partes propias siguen existiendo.

---

## ðŸ› ï¸ MÃ©todo para Construir el Vocabulario ER

> [!note] ðŸ“‹ Procedimiento General
>
> 1. Subraya sustantivos (entidades) y verbos (relaciones) del enunciado.
> 2. Asigna PK a cada entidad (sin clave no hay entidad).
> 3. Nombra cada relaciÃ³n con verbo + lectura en ambos sentidos.
> 4. Escribe la clasificaciÃ³n en ambas direcciones (pregunta de vuelta si falta una).
> 5. Anota cardinalidades (x,y) y lista las reglas de negocio 1:1 con el dibujo.
> 6. Verifica: Â¿todo se lee en voz alta? Â¿toda tabla futura tiene PK?
>
> **Principio clave:** lo que no estÃ¡ dibujado no existe; lo que no tiene clave no es entidad.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-11-flow.svg]]

---

## ðŸŽ¨ Ejemplos Trabajados

> [!info] â„¹ï¸ CÃ³mo trabajarlos
> Cada ejemplo trae su dibujo: tapa la soluciÃ³n, clasifica tÃº, compara.

### âœï¸ Ejemplo 1 â€” Clasificar DIVISIONâ€“EMPLOYEE

> [!example] ðŸŸ¢ La pregunta de vuelta decide
>
> Solo sabes: *"Una DIVISIÃ“N es manejada por un EMPLEADO"* â€” insuficiente (Â¿1:1 o 1:M?).
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-12-flow.svg]]
>
> **Moraleja:** sin la segunda frase, clasificar es adivinar. Escribe siempre ambas direcciones.

### âœï¸ Ejemplo 2 â€” Claves de ESTUDIANTEâ€“MATERIA

> [!example] ðŸŸ¢ Elegir PK como profesional
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-13-graph.svg]]
>
> **Se lee asÃ­ (Chen puro):** el estudiante *se matricula* en materias; `carnet` (estable) identifica, `email` (cambia) solo describe. Al traducir nacerÃ¡ MATRÃCULA con clave compuesta (Unidad 2).
>
> | DecisiÃ³n | ElecciÃ³n | Por QuÃ© |
> |---|---|---|
> | PK ESTUDIANTE | `carnet` | Ãšnico, no nulo, estable (el email cambia) |
> | PK MATERIA | `codigo` | Identifica sin dudar |
> | FKs en MATRÃCULA | `carnet + codigo` (compuesta) | Conecta ambas + identifica la matrÃ­cula |
> | Nombres | `STU_LNAME`, `CRS_CODE` | Prefijo de entidad: autodocumenta (Coronel 2.4.3) |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-14-er.svg]]
>
> **AnatomÃ­a de llaves:** `PK` = identifica la fila; `FK` = apunta a otra tabla; `UK` (candidata) = Ãºnica pero no elegida; `PK, FK` juntas = compuesta que ademÃ¡s referencia. Toda entidad nace con PK.

---

### âœï¸ Ejemplo 3 â€” La trampa CALIFICACIÃ“N (atributo que parecÃ­a entidad)

> [!example] ðŸŸ¢ Â¿Existe una nota por sÃ­ sola?
>
> Caso control acadÃ©mico: ALUMNOâ€“ASIGNATURA con *matricula(nota, fecha, intento)*. Casi todos crean la entidad CALIFICACION â€” **error**.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-15-graph.svg]]
>
> **Regla:** Â¿existe por sÃ­ sola? Una nota solo existe con un alumno Y una asignatura a la vez â†’ es **atributo de la relaciÃ³n**, no entidad. Trampa inversa a la del taller (allÃ­ sobraba un atributo que debÃ­a ser entidad).
>
> > [!quote] ðŸ“– C. Zavaleta, *MER: guÃ­a completa con ejemplos*, caso control acadÃ©mico (2026)

## ðŸ“‹ Tablas Comparativas

> [!note] ðŸ“‹ Fuerte vs Dependiente Â· Simple vs Compuesta
>
> | Entidad | Â¿Existe Sola? | Tipo |
> |---|---|---|
> | EMPLOYEE | SÃ­ | Fuerte |
> | DEPENDENT | No, exige EMPLOYEE | Dependiente |
> | PART (propias + compradas) | SÃ­ | Fuerte |
>
> | PK | CuÃ¡ndo | Ejemplo |
> |---|---|---|
> | **Simple** | Una columna identifica | `CLASS_CODE` |
> | **Compuesta** | Solo combinadas identifican | `CRS_CODE + CLASS_SECTION` |
> | **Candidata no elegida** | Reserva Ãºnica | `CLASS_CODE` si se elige la compuesta |

---

## âš ï¸ Errores Comunes y Principios LÃ³gicos

> [!warning] âš ï¸ CÃ³mo leer esta secciÃ³n
> Cada error trae su dibujo: lo âŒ que delata el problema y lo âœ… que lo evita.

### âŒ Error 1: RelaciÃ³n sin verbo ("lÃ­nea muda")

> [!danger] âŒ Viola: toda relaciÃ³n se lee en voz alta
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-16-graph.svg]]
>
> Dos rectÃ¡ngulos unidos que nadie sabe leer: nÃ³mbrala con verbo o bÃ³rrala.

### âŒ Error 2: Clasificar con una sola direcciÃ³n

> [!danger] âŒ Viola: conectividad siempre en ambas direcciones
>
> Sin la frase de vuelta es adivinanza (ver Ejemplo 1: DIVISIONâ€“EMPLOYEE puede ser 1:1 o 1:M). Escribe las dos frases antes de dibujar cardinalidades.

### âŒ Error 3: PK significativa que cambia

> [!danger] âŒ Viola: la PK debe ser estable
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-17-graph.svg]]
>
> Email o nombre como PK â†’ cascada de updates cuando cambian. Usa cÃ³digo estable (`carnet`, `codigo`): lo significativo describe, no identifica.

### âŒ Error 4: Todo es entidad / todo es atributo

> [!danger] âŒ Viola: existe por sÃ­ mismo vs describe
>
> Pregunta por cada sustantivo: Â¿existe por sÃ­ mismo (entidad) o solo describe a otro (atributo)? `DirecciÃ³n` describe a CLIENTE â†’ atributo. `MATERIA` existe sola â†’ entidad.

### âŒ Error 5: FK que apunta a nada

> [!danger] âŒ Viola: integridad referencial (carga el 1 primero)
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u1-02-18-flow.svg]]
>
> Carga el lado 1 primero o violas integridad referencial.

### âŒ Error 6: Multivaluado como columna

> [!danger] âŒ Viola: 1 celda = 1 valor (1FN desde ya)
>
> Columna `telefonos` con "099,088" o columnas `tel1, tel2, tel3` â†’ el multivaluado pide tabla propia `TELEFONO(cedula PK,FK + numero PK)` (ver U2-02 Â§6).

### âŒ Error 7: `edad` como PK o columna estrella

> [!danger] âŒ Viola: la PK debe ser estable (no volÃ¡til)
>
> La edad cambia sola cada aÃ±o â†’ cascada de updates y rupturas de FK. Usa `fecha_nacimiento` (no volÃ¡til) y deriva la edad.

---

## ðŸ“ Ejercicios Propuestos

> [!info] â„¹ï¸ CÃ³mo trabajarlos
> Tapa la soluciÃ³n, resuelve, compara. Respuestas colapsables abajo.

### âœï¸ Ejercicio 1 â€” Clasifica en ambas direcciones

> [!example] ðŸ“‹ Planteamiento
>
> *"Un PROFESOR dicta CLASES."* Escribe las dos frases y clasifica. Luego cambia el negocio a *"cada clase la dicta un solo profesor pero cada profesor dicta mÃ¡ximo 1 clase"* y reclasifica.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > VersiÃ³n 1: "un profesor dicta muchas clases" + "cada clase la dicta un profesor" â†’ 1:M. VersiÃ³n 2: ambas frases en singular â†’ 1:1. Sin la frase de vuelta era adivinanza.

### âœï¸ Ejercicio 2 â€” Elige las claves

> [!example] ðŸ“‹ Planteamiento
>
> ESTUDIANTE tiene `carnet, email, nombre`. MATERIA tiene `codigo, nombre`. DiseÃ±a MATRÃCULA con sus PK/FK justificando cada elecciÃ³n.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > PK ESTUDIANTE = `carnet` (estable; email cambia). PK MATERIA = `codigo`. MATRÃCULA(`carnet` PK,FK + `codigo` PK,FK): compuesta porque ninguno identifica solo y cada parte referencia a su tabla.

### âœï¸ Ejercicio 3 â€” Detecta la lÃ­nea muda

> [!example] ðŸ“‹ Planteamiento
>
> Un diagrama une CLIENTE con FACTURA sin verbo ni cardinalidad. Lista todo lo que falta y escribe las 2 frases que lo completarÃ­an (supÃ³n 1:M).
>
> > [!success]- âœ… SoluciÃ³n
> >
> > Falta: verbo (*genera*), clasificaciÃ³n en ambas direcciones y cardinalidad (x,y). Frases: "un cliente genera muchas facturas" + "cada factura es de un cliente" â†’ 1:M con (1,N)-(1,1).

### âœï¸ Ejercicio 4 â€” Entidad o instancia (unidad1.3-1.5 Â§12)

> [!example] ðŸ“‹ Planteamiento
>
> Clasifica: *Coca Cola, VehÃ­culo, $4.5, Cliente, Colgate, Tarjeta de CrÃ©dito, Labrador, 0987654321, Ciudad, Quito, Windows, RAM, Basket, Evento, Centro Comercial, BMW.*
>
> > [!success]- âœ… SoluciÃ³n
> >
> > - **Entidades (tipos):** VehÃ­culo, Cliente, Tarjeta de CrÃ©dito, Ciudad, Evento, Centro Comercial.
> > - **Instancias (valores):** Coca Cola, Colgate (marcas), Labrador, BMW (objetos concretos), Quito, $4.5, 0987654321, Windows, RAM, Basket.
> > - Regla: si lo puedes contar como *un ejemplar deâ€¦*, es instancia; si agrupa ejemplares, es entidad.

### âœï¸ Ejercicio 5 â€” PK de tablas y de la calle (unidad1.3-1.5 Â§Â§19â€“22)

> [!example] ðŸ“‹ Planteamiento
>
> a) Tablas a/b/c con filas (1,3,1),(1,2,2),(2,3,3): Â¿quÃ© columna(s) identifican? b) Elige PK para: VehÃ­culo, Persona, Estudiante, Factura, Usuario, Producto, Libro, PaÃ­s. c) Â¿QuÃ© atributo selecciona UN alumno de tu clase? Â¿y un libro en biblioteca?
>
> > [!success]- âœ… SoluciÃ³n
> >
> > - a) Columna **b** (3,2,3â€¦ verifica unicidad real en tus datos; el punto es: la PK se **comprueba** contra instancias, no se decreta).
> > - b) VehÃ­culoâ†’`placa`, Personaâ†’`cedula`, Estudianteâ†’`carnet`, Facturaâ†’`numero`, Usuarioâ†’`username`, Productoâ†’`codigo`, Libroâ†’`ISBN`, PaÃ­sâ†’`codigo_ISO`. Todas: Ãºnicas + no nulas + estables.
> > - c) Alumnoâ†’`carnet` (el nombre se repite: hay dos Pepes); libroâ†’`ISBN` (el tÃ­tulo no basta).

---

## ðŸŽ¯ Metas de Aprendizaje

> [!note] ðŸ“‹ Nivel BÃ¡sico
>
> - [ ] Defino entidad, atributo, relaciÃ³n, PK, FK y candidata sin mirar.
> - [ ] Leo un ERD en voz alta en ambas direcciones.
> - [ ] Elijo la PK correcta justificando unicidad, nulidad y estabilidad.
>
> [!note] ðŸ“‹ Nivel Intermedio
>
> - [ ] Clasifico 1:1/1:M/M:N escribiendo ambas frases.
> - [ ] Escribo cardinalidades (x,y) del lado correcto segÃºn notaciÃ³n.
> - [ ] Distingo entidad fuerte de dependiente con ejemplo propio.
>
> [!note] ðŸ“‹ Nivel Avanzado
>
> - [ ] Aplico el mÃ©todo de 6 pasos a un enunciado nuevo sin ayuda.
> - [ ] Detecto relaciones mudas y PKs cambiantes en diagramas ajenos.

---

## ðŸ“š Referencias

> [!quote] ðŸ“– Fuentes Consultadas
>
> - Diapositivas BD01 (Irene Cheung) + `unidad1.3-1.5.pdf`.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 4 Â§Â§4.1.3â€“4.1.5 y cap. 2 Â§2.4.3.
> - C. Zavaleta, *Modelo entidad-relaciÃ³n (MER): guÃ­a completa con ejemplos* (casos taller, universidad, empleados, banco), 2026 â€” https://cesarzavaleta.dev/modelo-entidad-relacion-mer/

---

## ðŸ” Repaso SR (flashcards)

#flashcards/bd-u1

> [!note] ðŸ§  Repasa con el plugin Spaced Repetition

- Â¿Entidad vs atributo vs relaciÃ³n?::Sustantivo que existe / propiedad que describe / verbo que conecta.
- Â¿Reglas de una buena PK?::Ãšnica + no nula + estable + mÃ­nima.
- Â¿Conectividad vs cardinalidad?::ClasificaciÃ³n 1:1/1:M/M:N vs mÃ­nimo-mÃ¡ximo (x,y).
- Â¿Entidad dÃ©bil (2 condiciones)?::Existencia-dependiente + PK derivada del padre.
- Â¿CÃ³mo sÃ© si una relaciÃ³n es 1:M y no 1:1?::Escribiendo ambas direcciones (pregunta de vuelta).
- Â¿Trampa CALIFICACIÃ“N?::La nota no existe sola (alumno + asignatura a la vez): atributo de la relaciÃ³n, no entidad.
- Â¿Simple/compuesto/derivado/multivaluado?::AtÃ³mico / se parte / se calcula / N valores (pide tabla).
- Â¿VolÃ¡til vs no volÃ¡til?::Edad cambia sola (mala); fecha_nacimiento no (Ãºsala).
- Â¿PK artificial cuÃ¡ndo?::Incremental sin significado, cuando ninguna candidata es estable.
- Â¿Mandatory vs Optional (ERDPlus)?::MÃ­nimo 1 vs mÃ­nimo 0 (tu x de (x,y)).
- Â¿Identifying prendido/apagado?::PK del padre entra a la PK del hijo vs FK normal.

---

## ðŸ”— Conexiones

> [!quote] ðŸ”— Notas Relacionadas
>
> - [[01 - Dato, informaciÃ³n y modelos de datos]] â€” el problema que este vocabulario resuelve.
> - [[03 - Modelo relacional, ERM y casos Tiny College]] â€” donde estas piezas se vuelven tablas.
> - Ver tambiÃ©n la nota de **Claves** integrada arriba si vienes de un link viejo: ahora vive aquÃ­.

---

## ðŸ”— Seguir estudiando

> [!info] ðŸ“š Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Ãndice Unidad 1: [[00 - Ãndice Unidad 1]] Â· Ãndice Unidad 2: [[00 - Ãndice Unidad 2]]
> - Anterior: [[01 - Dato, informaciÃ³n y modelos de datos]] Â· Siguiente: [[03 - Modelo relacional, ERM y casos Tiny College]]
> - ConversiÃ³n a tablas: [[01 - ConversiÃ³n MC a ML por cardinalidad]]

---

**Tags:** #TICG1018 #unidad1 #er #claves #relaciones #bd

