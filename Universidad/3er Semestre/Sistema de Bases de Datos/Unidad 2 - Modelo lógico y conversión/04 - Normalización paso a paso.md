---
dg-publish: true
tags: [TICG1018, unidad2, normalizacion, paso-a-paso, bd]
---

# ðŸ› ï¸ NormalizaciÃ³n Paso a Paso

## ðŸŽ¯ IntroducciÃ³n

> [!info] ðŸ’¡ Normalizar es un Protocolo, No un Salto
>
> Las formas normales se aplican **en orden**: 1FN es el piso, 2FN cura las parciales, 3FN cura las transitivas y BCNF es el chequeo final. Cada curaciÃ³n sigue siempre el mismo gesto: **partir la tabla y dejar el determinante en la original como FK**.
>
> **AnalogÃ­a:** es una limpieza por capas â€” desarmas el mueble pieza por pieza; nunca arrancas la pata si aÃºn hay tornillos sueltos.

---

## ðŸ§° Lo que Necesitas Antes de Empezar

> [!info] ðŸ§° Los 4 pre-requisitos
>
> 1. **La tabla ya en 1FN** â€” un valor por celda, sin grupos repetitivos. Sin piso no se normaliza: [[02 - Primera forma normal y diccionario de datos]].
> 2. **La PK identificada** â€” si es compuesta, hay 2FN por hacer; si es simple, saltas directo a la 3FN.
> 3. **La lista completa de DFs** â€” no se inventan: salen de mirar quÃ© datos se repiten juntos. El repaso estÃ¡ en [[03 - Segunda y tercera forma normal]].
> 4. **El orden fijo** â€” 2FN antes que 3FN: una parcial sin curar se disfraza de transitiva.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-05-graph.svg]]
>
> **AnalogÃ­a:** antes de operar, plan leÃ­do y radiografÃ­a hecha. Sin los 4 Ã­tems, partes a ciegas.

---

## ðŸ› ï¸ MÃ©todo: el protocolo paso a paso

> [!note] ðŸ“‹ Protocolo
>
> 1. **Â¿EstÃ¡ en 1FN?** Un valor por celda, sin grupos repetitivos. Si no, corrige primero.
> 2. **Â¿2FN?** Si la PK es compuesta, busca DFs cuyo determinante sea *solo parte de la PK*. Por cada parcial: tabla nueva con Ã©l como PK, mueve sus dependientes y **dÃ©jalo en la original como FK**. Si la PK es simple, la 2FN es automÃ¡tica y pasas directo al paso 3.
> 3. **Â¿3FN?** Busca transitivas: un **no-primo** determinando a otro no-primo (`no-primo â†’ no-primo`). Por cada transitiva: tabla nueva con el determinante como PK, mueve sus dependientes y dÃ©jalo como FK.
> 4. **Â¿BCNF?** Chequea si **todo determinante es clave candidata**. Si algÃºn determinante no-clave sobrevive, parte una vez mÃ¡s.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-01-flow.svg]]
> ![[Figuras/bd-s04-p12.png]]

> [!tip] ðŸŽ¯ Regla de Oro: el Determinante Nunca Abandona
>
> Al partir una tabla, el determinante **se copia en la original como FK** (mudar nunca). Las tablas nuevas necesitan ese puente para reunir los datos con un JOIN; sin FK quedan huÃ©rfanas.
>
> **Ejemplo:** de `EMPLOYEE(EMP_NUM, EMP_NAME, JOB_CLASS, CHG_HOUR)` la transitiva `JOB_CLASS â†’ CHG_HOUR` saca la tabla `JOB`, pero `JOB_CLASS` vive en ambas:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-03-graph.svg]]

> [!note] ðŸ“‹ Herramienta: el Diagrama de Dependencias
>
> Antes de partir, dibuja las DFs: **PK en negrita**; sus flechas (sanas) **arriba**; las sospechosas (parciales y transitivas) **abajo**. Ese dibujo te dice de un vistazo quÃ© tabla nace y quÃ© deja detrÃ¡s.
>
> Las DFs no se inventan: salen de las filas. PregÃºntate por cada columna: Â¿con quÃ© valor aparece siempre acompaÃ±ada? `cod_estud` siempre llega con el mismo `nomb_estud` â‡’ `cod_estud â†’ nomb_estud`.
>
> Filas reales de MATRICULA:
>
> | cod_estud | cod_curso | nomb_estud | nomb_curso | creditos | cod_instructor | nomb_instructor | nota_final |
> |---|---|---|---|---|---|---|---|
> | 101 | BD01 | Ana | BD | 3 | 10 | Dra. RuÃ­z | 9.5 |
> | 101 | SO01 | Ana | SO | 4 | 20 | Ing. Ponce | 8.0 |
> | 102 | BD01 | Luis | BD | 3 | 10 | Dra. RuÃ­z | 7.5 |
>
> Mira: `nomb_estud` se repite con cada matrÃ­cula del estudiante (parcial), los datos del curso con cada matrÃ­cula del curso (parcial), y el instructor estÃ¡ escondido tras el curso (transitiva).
>
> **Caso `MATRICULA(cod_estud, cod_curso, nomb_estud, nomb_curso, creditos, cod_instructor, nomb_instructor, nota_final)`:**
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-02-graph.svg]]
> ![[Figuras/bd-023-p15.png]]

---

## ðŸŽ¨ Ejemplo Trabajado Completo

> [!example] ðŸŸ¢ De 1NF a BCNF sin perder datos
>
> Entrada: `MATRICULA(cod_estud, cod_curso, nomb_estud, nomb_curso, creditos, cod_instructor, nomb_instructor, nota_final)` â€” PK = `(cod_estud, cod_curso)`.
>
> > > [!success]- âœ… Pasos
> >
> > 1. **1FN:** cada celda un valor. âœ”
> > 2. **2FN (parciales):** `cod_estud â†’ nomb_estud` y `cod_curso â†’ nomb_curso, creditos, cod_instructor` nacen de *parte* de la PK.
> >    - â†’ `ESTUDIANTE(cod_estud, nomb_estud)` + `CURSO(cod_curso, nomb_curso, creditos, cod_instructor)` + original ahora `MATRICULA(cod_estud FK, cod_curso FK, nota_final)`.
> >
> >    ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-06-er.svg]]
> >
> > 3. **3FN (transitiva):** dentro de CURSO sobrevive `cod_instructor â†’ nomb_instructor` (no-primo â†’ no-primo).
> >    - â†’ `INSTRUCTOR(cod_instructor, nomb_instructor)` + `CURSO(cod_curso, nomb_curso, creditos, cod_instructor FK)`.
> > 4. **Chequeo BCNF:** los determinantes son `cod_estud`, `cod_curso`, `cod_instructor` â€” todos claves candidatas. âœ”
> >
> > Resultado: 4 tablas, 0 duplicados. Cambiar el nombre de un instructor toca **una** fila.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-04-04-er.svg]]

---

## âš ï¸ Errores Comunes

### âŒ Error 1: Buscar parciales con PK simple

> [!danger] âŒ Viola: sin PK compuesta no hay parciales
>
> Con PK de un solo atributo la 2FN es automÃ¡tica â€” no hay "parte" de la PK. El trabajo ahÃ­ es detectar la transitiva (paso 3). En la pizarra: dibuja la PK antes de decidir.

### âŒ Error 2: Mudar el determinante fuera

> [!danger] âŒ Viola: el determinante se queda como FK
>
> Al extraer `JOB`, borrar `JOB_CLASS` de EMPLOYEE rompe el puente: ya no puedes saber quÃ© clase tiene cada empleado. **Copia, no mudes.**

### âŒ Error 3: No revisar la tabla nueva

> [!danger] âŒ Viola: re-evaluar tras cada particiÃ³n
>
> Cada tabla nueva puede esconder su propia transitiva. Tras cada particiÃ³n: re-dibuja el diagrama de dependencias de la tabla nueva y vuelve al paso 3. Termina con el chequeo BCNF global.

### âŒ Error 4: Inventar PK nueva en las particiones

> [!danger] âŒ Viola: la PK de la tabla nueva es el determinante
>
> La tabla nueva nace con el **determinante como PK**. Si despuÃ©s inventas un `id` surrrogado, pierdes el chequeo de unicidad que detectaba las anomalÃ­as.

---

## ðŸŽ¯ Metas de Aprendizaje

> [!note] ðŸ“‹ Nivel BÃ¡sico
>
> - [ ] Repito el protocolo de 4 pasos sin mirar.
> - [ ] Distingo flecha sana (nace de la PK) de sospechosa (parcial o trans) en un diagrama.

> [!note] ðŸ“‹ Nivel Intermedio
>
> - [ ] Parto una tabla a 2FN y a 3FN dejando los FKs correctos.
> - [ ] Dibujo el diagrama de dependencias antes de tocar schemas.

> [!note] ðŸ“‹ Nivel Avanzado
>
> - [ ] Decido BCNF mirando si todo determinante es clave candidata.
> - [ ] Encuentro transitivas escondidas en las tablas nuevas tras cada particiÃ³n.

---

## ðŸ” Repaso SR (flashcards)

#flashcards/bd-u2

> [!note] ðŸ§  Repasa con el plugin Spaced Repetition

- Â¿Protocolo completo en 1 lÃ­nea?::1FN piso â†’ 2FN (parciales fuera) â†’ 3FN (transitivas fuera) â†’ BCNF (determinantes = claves).
- Â¿PK simple, necesario 2FN?::No, es automÃ¡tica; voy directo a buscar transitivas.
- Â¿QuÃ© hago con cada determinante parcial?::Tabla nueva con Ã©l como PK, muevo dependientes y lo dejo como FK en la original.
- Â¿CÃ³mo detecto una transitiva?::Un no-primo determinando a otro no-primo.
- Â¿DÃ³nde queda el determinante al partir?::En la tabla original como FK (copiar, no mudar).
- Â¿Chequeo BCNF?::Todo determinante debe ser clave candidata.

---

## ðŸš€ PrÃ³ximos Pasos

> [!quote] ðŸŒŸ Continuando
>
> **Has aprendido:**
> - âœ… El protocolo de normalizaciÃ³n en orden
> - âœ… El diagrama de dependencias como herramienta
> - âœ… La regla del determinante como FK
>
> **PrÃ³xima clase:** denormalizaciÃ³n y dudas del proyecto.

---

## ðŸ”— Seguir estudiando

> [!info] ðŸ“š Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Ãndice Unidad 2: [[00 - Ãndice Unidad 2]]
> - Anterior: [[03 - Segunda y tercera forma normal]]

---

## ðŸ“š Referencias

> [!quote] ðŸ“– Fuentes
>
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (proceso de normalizaciÃ³n, Â§6.3-6.6).
> - Diapositivas BD 02 MC_a_ML: mÃ©todos de conversiÃ³n y formas normales.

> [!info] Láminas del material de clase
>
> Renderizados del deck de la unidad, en orden de presentación.
>
> ![[bd-023-p10.png]]
> ![[bd-023-p12.png]]
> ![[bd-023-p14.png]]
> ![[bd-023-p15.png]]
> ![[bd-023-p20.png]]
> ![[bd-s03-p10.png]]
> ![[bd-s03-p16.png]]
> ![[bd-s03-p17.png]]
> ![[bd-s03-p20.png]]
> ![[bd-s03-p21.png]]
> ![[bd-s03-p3.png]]
> ![[bd-s03-p7.png]]
> ![[bd-s03-p8.png]]
> ![[bd-s04-p10.png]]
> ![[bd-s04-p11.png]]
> ![[bd-s04-p12.png]]
> ![[bd-s04-p14.png]]
> ![[bd-s04-p15.png]]
> ![[bd-s04-p8.png]]


---

**Tags:** #TICG1018 #unidad2 #normalizacion #paso-a-paso #bd

