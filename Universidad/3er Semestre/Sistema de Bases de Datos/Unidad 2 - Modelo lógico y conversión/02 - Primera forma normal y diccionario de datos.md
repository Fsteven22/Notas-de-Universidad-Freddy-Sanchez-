---
dg-publish: true
tags: [TICG1018, unidad2, primera-forma-normal, diccionario, ml]
---

# ðŸ“ Primera Forma Normal y Diccionario de Datos

## ðŸŽ¯ IntroducciÃ³n

> [!info] ðŸ’¡ Â¿Por QuÃ© Normalizar DespuÃ©s de Convertir?
>
> La conversiÃ³n (MC â†’ ML) te da tablas. La **normalizaciÃ³n** verifica que esas tablas no escondan inconsistencias. Las formas normales miden quÃ© tan vulnerable es una tabla a que los datos se contradigan.
>
> **AnalogÃ­a:** la conversiÃ³n es armar el mueble; la 1FN es verificar que no sobren tornillos ni falten patas.
>
> | Forma | Idea en 1 lÃ­nea | QuÃ© corrige |
> |---|---|---|
> | **1FN** | Un valor por celda, sin grupos repetitivos | Columnas como `telÃ©fono1, telÃ©fono2` |
> | **2FN** | Sin dependencias parciales | Datos que dependen de solo parte de la PK |
> | **3FN** | Sin dependencias transitivas | Datos que dependen de otro dato no-clave |

---

## ðŸ“‹ Definiciones Formales

### 1ï¸âƒ£ Objetivo de la 1FN

> [!note] ðŸ“‹ DefiniciÃ³n â€” Objetivo
>
> Una tabla estÃ¡ en **1FN** cuando cada celda contiene **exactamente un valor** y no hay grupos repetitivos.
>
> **Ejemplo real:**
>
> âŒ **No es 1FN:** `CLIENTE(cÃ©dula, nombre, telÃ©fono1, telÃ©fono2, telÃ©fono3)`  
> Los telÃ©fonos estÃ¡n repetidos en columnas diferentes. Si un cliente tiene 4 telÃ©fonos, no caben.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-18-er.svg]]
>
> âœ… **Es 1FN:** `CLIENTE(cÃ©dula, nombre)` y `TELEFONO(cÃ©dula, nÃºmero)`  
> Cada fila tiene un solo telÃ©fono. Un cliente puede tener N filas en TELEFONO.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-19-er.svg]]

### 2ï¸âƒ£ Las 5 condiciones de la 1FN

> [!note] ðŸ“‹ DefiniciÃ³n â€” Checklist de la 1FN
>
> Para que una tabla estÃ© en **1FN**, debe cumplir las 5 condiciones. Si falla cualquiera, no estÃ¡ en 1FN:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-14-flow.svg]]
>
> | # | CondiciÃ³n | Â¿QuÃ© significa en lenguaje sencillo? |
> |---|---|---|
> | 1 | Sin orden en las filas | No importa si la fila 1 estÃ¡ arriba o abajo de la fila 2 |
> | 2 | Sin orden en las columnas | No importa si `nombre` estÃ¡ a la izquierda o derecha de `cÃ©dula` |
> | 3 | Sin filas duplicadas | No puede haber dos filas idÃ©nticas |
> | 4 | Un valor por celda | Cada celda guarda exactamente un dato, no una lista |
> | 5 | Columnas regulares | No hay columnas ocultas como `id_fila`, `timestamp`, ni IDs de objeto sueltos |

> [!info] ðŸ“– El deck de cÃ¡tedra: la 1FN en la pizarra (slides04 y BD 02.3)
> El deck del Ing. Magallanes define la 1FN como *"una tabla donde la intersecciÃ³n de cada fila y columna contiene solo un valor"* y da el ejemplo canÃ³nico de la rama con varios telÃ©fonos.

![[Archivos/bd-s04-p8.png]]

![[Archivos/bd-023-p10.png]]

> **Las 5 condiciones (BD 02.3, p. 10):** *"1. No hay orden de arriba-a-abajo en las filas. 2. No hay orden de izquierda-a-derecha en las columnas. 3. No hay filas duplicadas. 4. Cada intersecciÃ³nâ€¦"* â€” el checklist de esta nota es el mismo, con la condiciÃ³n 5 (columnas regulares) completada.
>
> **El ejemplo del deck (slides04, p. 9):** la tabla `branchNo / branchAddress / telNos` con `B001 Â· 8 Jeffesorn Way, Portland, OR 97201 Â· 212-â€¦` y varios telÃ©fonos separados por comas â€” la celda con lista que viola la 1FN.

### 3ï¸âƒ£ ViolaciÃ³n de la 1FN

> [!note] ðŸ“‹ DefiniciÃ³n â€” ViolaciÃ³n
>
> Una tabla **no estÃ¡ en 1FN** si incumple cualquiera de las 5 condiciones. La PK (clave primaria) no salva a una tabla que tiene grupos repetitivos.
>
> **Ejemplo:** `productos = "arroz, leche, pan"` en una sola celda viola la condiciÃ³n 4. No puedes filtrar por "arroz" sin leer toda la celda.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-16-graph.svg]]

### 4ï¸âƒ£ Diccionario de datos

> [!note] ðŸ“‹ DefiniciÃ³n â€” Diccionario de datos
>
> Es un documento que describe cada tabla: por cada atributo, indica su tipo de dato, dominio (quÃ© valores acepta) y descripciÃ³n. Es el "manual de usuario" de tu base de datos.
>
> | Atributo | Tipo | Dominio | DescripciÃ³n |
> |---|---|---|---|
> | `cedula` | `int` | > 0, Ãºnico | PK del cliente |
> | `nombre` | `varchar(50)` | texto no vacÃ­o | Nombre completo |
> | `direccion` | `varchar(100)` | texto | DirecciÃ³n de facturaciÃ³n |
> | `telefono` | `varchar(15)` | 7â€“15 dÃ­gitos | Contacto principal |
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-15-graph.svg]]

### 5ï¸âƒ£ Atributo multivaluado

> [!note] ðŸ“‹ DefiniciÃ³n â€” Atributo multivaluado
>
> Es un atributo que guarda varios valores para una misma entidad (ej. varios telÃ©fonos de un cliente). Viola la 1FN hasta que se separa en su propia tabla.
>
> **Ejemplo:**
>
> âŒ `CLIENTE(cÃ©dula, nombre, telÃ©fonos)` â†’ `telÃ©fonos = "2345, 2654"` (grupo repetitivo)
> âœ… `TELEFONO(cÃ©dula FK, nÃºmero)` â†’ una fila por telÃ©fono
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/u2-02-17-graph.svg]]

---

## ðŸŽ¨ Ejemplo Trabajado: CLIENTE

> [!example] ðŸ’¡ Verificando 1FN con datos reales
>
> | CÃ©dula | Nombre | DirecciÃ³n | TelÃ©fono |
> |---|---|---|---|
> | 0876456324 | Jorge Santos | 1234 Av. 10 | 2345678 |
> | 0964532748 | Luis Tinoco | 6543 Av. 4 | 2654345 |
> | 1345234567 | Ana RamÃ­rez | 34 Av. 6 | 2654567 |
>
> **Chequeo 1FN:**
> - Â¿Filas sin orden? SÃ­.
> - Â¿Columnas sin orden? SÃ­.
> - Â¿Sin filas duplicadas? SÃ­.
> - Â¿Una celda, un valor? SÃ­.
> - Â¿Columnas regulares? SÃ­.
> â†’ **EstÃ¡ en 1FN.**
>
> **Contraejemplo:** `CLIENTE(cÃ©dula, nombre, telefono1, telefono2, telefono3)` â†’ viola la condiciÃ³n 4 (grupos repetitivos). Remedio: tabla `TELEFONO(cÃ©dula FK, numero)`.

---

## ðŸ› ï¸ MÃ©todo: Documentar con Diccionario

> [!success] ðŸ† Plantilla por tabla (Ãšsala en tu proyecto)
>
> | Atributo | Tipo de Dato | Dominio | DescripciÃ³n |
> |---|---|---|---|
> | `idCliente` | `int` | > 0, Ãºnico | PK: identifica al cliente |
> | `nombre` | `varchar(30)` | texto no vacÃ­o | Nombre completo |
> | `direccion` | `varchar(50)` | texto | DirecciÃ³n de facturaciÃ³n |
> | `telefono` | `varchar(15)` | 7â€“15 dÃ­gitos | Contacto principal |
>
> **Regla:** cada tabla del ML termina con su fila en el diccionario. Sin diccionario, el ML estÃ¡ incompleto (la docente lo pide explÃ­cito).

---

## âš ï¸ Errores Comunes

### âŒ Error 1: Varios valores por celda

> [!danger] âŒ Viola: 1FN condiciÃ³n 4
>
> `productos = "arroz, leche, pan"` en una sola celda. No puedes filtrar por "arroz" fÃ¡cilmente.
>
> âœ… **SoluciÃ³n:** una fila por producto en una tabla `DETALLE(idReporte FK, producto)`.

### âŒ Error 2: Columnas numeradas

> [!danger] âŒ Viola: grupos repetitivos
>
> `materia1, materia2, materia3`. Â¿Y la cuarta materia? Columnas finitas para relaciones infinitas.
>
> âœ… **SoluciÃ³n:** tabla intermedia de matrÃ­cula (una fila por par estudianteâ€“materia).

### âŒ Error 3: ML sin diccionario

> [!danger] âŒ Viola: entregable completo
>
> Entregar el diagrama lÃ³gico sin describir tipos ni dominios. Nadie sabe si `telÃ©fono` es `int` o texto, ni quÃ© valores acepta.
>
> âœ… **SoluciÃ³n:** diccionario con las 4 columnas por cada atributo.

---

## ðŸŽ¯ Mejores PrÃ¡cticas

> [!tip] ðŸ† Checklist 1FN
>
> 1. **Cuenta valores por celda** â€” mÃ¡s de uno = no es 1FN.
> 2. **Busca columnas `cosa1, cosa2`** â€” es un grupo repetitivo disfrazado.
> 3. **Diccionario al mismo tiempo** â€” documenta cada tabla apenas la creas.
> 4. **Piensa en 2FN/3FN desde ya** â€” si un atributo depende de parte de la PK o de otro no-clave, anÃ³talo.

---

## ðŸ“ Ejercicios Propuestos

### âœï¸ Ejercicio 1 â€” Detectar la violaciÃ³n

> [!example] ðŸ“‹ Planteamiento
>
> Â¿EstÃ¡ en 1FN? `REPORTE(id, cliente, productos)` con `productos = "arroz, leche, pan"` en una celda.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > No: viola la condiciÃ³n 4 (un valor por celda). CorrecciÃ³n: tabla `DETALLE_REPORTE(idReporte FK, producto)`.

### âœï¸ Ejercicio 2 â€” Escribir un diccionario

> [!example] ðŸ“‹ Planteamiento
>
> Escribe el diccionario de `DEPARTAMENTO(idDepartamento int PK, nombre varchar(30))`.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > | Atributo | Tipo | Dominio | DescripciÃ³n |
> > |---|---|---|---|
> > | idDepartamento | int | > 0, Ãºnico | PK del departamento |
> > | nombre | varchar(30) | texto no vacÃ­o | Nombre oficial |

### âœï¸ Ejercicio 3 â€” Las 3 FN en una frase

> [!example] ðŸ“‹ Planteamiento
>
> Nombra las 3 FN y quÃ© vulnerabilidad mide cada una.
>
> > [!success]- âœ… SoluciÃ³n
> >
> > 1FN (grupos repetitivos), 2FN (dependencias parciales de la PK), 3FN (dependencias transitivas entre no-claves).

---

## ðŸ” Repaso SR (flashcards)

#flashcards/bd-u2

> [!note] ðŸ§  Repasa con el plugin Spaced Repetition

- Â¿Objetivo de la 1FN?::Tablas fieles a una relaciÃ³n, sin grupos repetitivos.
- Â¿5 condiciones 1FN?::Filas sin orden, columnas sin orden, sin duplicadas, un valor por celda, columnas regulares.
- Â¿QuÃ© mide cada FN?::Vulnerabilidad a inconsistencias: 1FN grupos repetitivos, 2FN dependencias parciales, 3FN transitivas.
- Â¿Diccionario de datos y sus 4 columnas?::Describe cada tabla: atributo, tipo de dato, dominio, descripciÃ³n.

---

## ðŸš€ PrÃ³ximos Pasos

> [!quote] ðŸŒŸ Continuando
>
> **Has aprendido:**
> - âœ… 5 condiciones 1FN con ejemplo CLIENTE
> - âœ… Diccionario de datos por tabla
> - âœ… Vista previa 2FN/3FN
>
> **PrÃ³xima clase:** taller de conversiÃ³n y normalizaciÃ³n.

---

## ðŸ”— Seguir estudiando

> [!info] ðŸ“š Seguir estudiando
>
> - Mapa de contenido: [[Sistema de Bases de Datos]]
> - Ãndice Unidad 2: [[00 - Ãndice Unidad 2]]
> - Anterior: [[01 - ConversiÃ³n MC a ML por cardinalidad]]
> - Siguiente: [[03 - Segunda y tercera forma normal]]

---

## ðŸ“š Referencias

> [!quote] ðŸ“– Fuentes
>
> - Diapositivas BD 02 MC_a_ML: 1FN (objetivo + 5 condiciones + ejemplo CLIENTE), formas normales, diccionario de datos.
> - C. Coronel, S. Morris, *Database Systems*, 9th ed., cap. 6 (normalizaciÃ³n).

---

**Tags:** #TICG1018 #unidad2 #1fn #diccionario #bd

