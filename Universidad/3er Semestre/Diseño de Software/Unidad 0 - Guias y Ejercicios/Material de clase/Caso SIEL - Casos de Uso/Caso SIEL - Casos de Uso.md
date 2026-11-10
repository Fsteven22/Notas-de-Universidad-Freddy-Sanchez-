---
dg-publish: true
tags: [CCPG1042, unidad2, siel, casos-de-uso]
---

# 🗳️ Caso SIEL — Casos de Uso (capturas de pizarra)

> [!info] ℹ️ Qué es esto
>
> Capturas de la pizarra de la clase de casos de uso: el caso **SIEL** (Sistema de Elecciones Seccionales) trabajado de punta a punta para Control03.

## 📎 Deck oficial de la cátedra

> [!tip] 📖 Material complementario
> El deck de clase que cubre esta misma sesión (teoría de UML, casos de uso, clases y secuencia) es [[../../Diapositivas/04aLenguajeUnificadoModelado.pdf|04a Lenguaje unificado de modelado]].
> No es el mismo material: el deck explica la notación y da el ejemplo de *AcademicChoice*; estas capturas son el caso **SIEL** trabajado en la pizarra.
>
> **Se lee así:** el callout apunta al deck oficial `04a Lenguaje unificado de modelado` (50 páginas, Unidad 2) como material complementario y aclara de entrada que no es lo mismo que estas capturas: el deck explica la notación con el ejemplo de *AcademicChoice* (registrarse en un paralelo, pp. 6-7), mientras que las láminas son el caso **SIEL** dibujado en la pizarra.
>
> **Por qué importa:** saber qué cubre cada uno evita mezclar la teoría del deck con la práctica de la pizarra, y sobre todo indica dónde está el formato de la descripción textual que pide el Control03.
>
> **Ejemplo:** si necesitas la notación de `«include»`/`«extend»` o el ejemplo de *AcademicChoice*, abre `04a Lenguaje unificado de modelado`; si necesitas el modelo de actores del SIEL, quédate en estas capturas.

## 📚 Dónde quedó el contenido

> [!info] 📖 Dónde quedó el contenido
>
> Todo lo transcrito ya está integrado en [[04 - UML casos de uso, secuencia y actividad]]:
>
> - El caso SIEL como sección trabajada con su diagrama (`dsw-u2-04-05-use`)
> - Descripción textual de `Registrar acta de escrutinio` con 2 escenarios concretos
> - Generalización de actores (`Observador ──▷ Ciudadano`) y punto de extensión del `<<extend>>`
> - Usos y riesgos de los casos de uso (test "Registrar acta" ✓ vs "Sumar votos" ✗)
> - Las 2 actividades de la pizarra = ejercicios 18 y 19
>
> **Se lee así:** el callout es un mapa de destinos: cada viñeta dice en qué sección de [[04 - UML casos de uso, secuencia y actividad]] quedó el material de la pizarra (el diagrama `dsw-u2-04-05-use`, la descripción de `Registrar acta de escrutinio`, la generalización `Observador ──▷ Ciudadano`, los usos y riesgos de los casos de uso y las dos actividades que son los ejercicios 18 y 19).
>
> **Por qué importa:** evita duplicar contenido y deja claro que estas capturas son el original, no la versión que hay que estudiar para el parcial.
>
> **Ejemplo:** si necesitas la descripción textual con sus dos escenarios, la tienes en la sección de `Registrar acta de escrutinio` de la nota 04, no aquí.

## 🗂️ Originales

> [!example]- 📷 Capturas de pizarra (en orden)
>
> ![[Casos de uso SIEL-1.png]]
>
> **Se lee así:** la lámina enfrenta las tres relaciones del diagrama de casos de uso y fija la dirección de cada flecha: `«include»` es obligatorio y común a varios casos, y su flecha va del caso base al incluido (`Registrar acta` → `Validar acta`); `«extend»` es opcional o condicional, y su flecha va del que extiende al base, con un punto de extensión explícito ("inconsistencia detectada"); la generalización es el "es un" (el Observador hace todo lo del Ciudadano y algo más) y también aplica entre casos de uso. Cierra con la advertencia de Stevens: no abuses de estas relaciones, un diagrama lleno de flechas se vuelve confuso.
>
> **Por qué importa:** invertir una flecha es el error más caro del parcial, porque hace que el diagrama diga justo lo contrario de lo que hace el sistema; y un `extend` sin punto de extensión escrito no se puede revisar ni implementar.
>
> **Ejemplo:** `Registrar acta ──«include»──▶ Validar acta` y `Enviar acta a revisión ──«extend»──▶ Registrar acta`, con el punto de extensión "inconsistencia detectada".
>
> ![[Casos de uso SIEL-2.png]]
>
> **Se lee así:** la lámina llena el formato en papel de Stevens cap. 7 con el caso `Registrar acta de escrutinio`: actor (Presidente de JRV), precondición (la JRV está abierta y el presidente se autenticó), flujo principal de 5 pasos, dos flujos alternativos (`4a`: los votos superan a los electores del padrón → el acta se envía a revisión; `3a`: el presidente cancela → no se guarda nada) y postcondición (el acta queda registrada o en revisión). A la derecha van los dos escenarios con datos: en la JRV 12 de Tarqui el presidente registra 180 para A, 95 para B, 10 nulos y 5 blancos contra un padrón de 320 → acta registrada; y con 340 votos contra 320 → acta enviada a revisión.
>
> **Por qué importa:** muestra en una sola lámina la diferencia entre caso y escenario: el caso es la familia de caminos y el escenario es UN recorrido con datos; además fija el formato exacto que se entrega en el Control03.
>
> **Ejemplo:** los mismos 5 pasos del flujo principal dan dos resultados distintos según los números que se ingresen en el paso 3.
>
> ![[Casos de uso SIEL-3.png]]
>
> **Se lee así:** define los tres elementos del diagrama con el ejemplo del SIEL: el actor es un rol externo al sistema, no una persona concreta, y puede ser un humano u otro sistema (`Ciudadano`, `Presidente de JRV`, el `«sistema»` Registro Civil); el caso de uso es una tarea que entrega un resultado de valor a un actor y se nombra con verbo + objeto (`Registrar acta de escrutinio`, `Consultar resultados`, `Importar padrón`); la frontera del sistema es el rectángulo que separa lo que el sistema hace de su entorno.
>
> **Por qué importa:** los tres errores de partida salen de aquí: poner a la persona concreta en vez del rol, bajar el nombre del caso a un paso interno o meter al sistema externo dentro de la frontera; cada uno rompe el significado del diagrama entero.
>
> **Ejemplo:** el Registro Civil entra como actor externo con el estereotipo `«sistema»`, no como una clase dentro del rectángulo del SIEL.
>
> ![[Casos de uso SIEL-4.png]]
>
> **Se lee así:** la lámina separa en dos columnas los usos y los riesgos de los casos de uso. Usos: capturar requisitos en el lenguaje del usuario, planificar iteraciones por casos de uso y derivar pruebas a partir de escenarios. Riesgos: diseño funcional (descomponer el sistema en funciones), demasiado detalle en cada flujo y confundirlos con diseño interno. Debajo está el contraste canónico: no "Sumar votos en la tabla ACTAS", sí "Registrar acta de escrutinio".
>
> **Por qué importa:** anticipa los tres errores que más se repiten en los trabajos: un diagrama que es un inventario de pantallas, un diagrama que ahoga el caso en micro-pasos, o un diagrama que en realidad es el diseño de la base de datos.
>
> **Ejemplo:** "Registrar acta de escrutinio" es un objetivo que el actor pediría en voz alta; "Sumar votos en la tabla ACTAS" es interno y por eso no puede ser un óvalo del diagrama.
>
> ![[Casos de uso SIEL-5.png]]
>
> **Se lee así:** la actividad de filtro, con ocho candidatos a actor del SIEL numerados: `Presidente de JRV`; `María Pérez, presidenta de la JRV 12`; `Ciudadano`; `Base de datos del SIEL`; `Sistema del Registro Civil`; `Funcionario electoral`; `Acta de escrutinio`; `Delegado de una organización política`. Pide escribir en el chat los números que NO son actores y, para cada uno, el criterio que falla: ¿es un rol?, ¿es externo al sistema?, ¿interactúa con él?
>
> **Por qué importa:** es el filtro que separa "actor" de "todo lo demás" y el que se pregunta en el examen; aplicarlo con esos tres criterios evita diagramas con veinte óvalos y cinco actores de sobra.
>
> **Ejemplo:** "María Pérez" no es actor (es una persona concreta: el rol es `Presidente de JRV`) y "Base de datos del SIEL" tampoco, porque es un componente interno que va dentro de la frontera.
>
> ![[Casos de uso SIEL-6.png]]
>
> **Se lee así:** la consigna del trabajo grupal, con su tiempo: 3 min para listar actores y al menos 6 casos de uso, cada uno con verbo + objeto; después dibujar el diagrama con frontera incluyendo al menos un `«include»`, un `«extend»` y una generalización, cada uno justificado; 7 min para describir un caso de uso (actor, precondición, flujo principal y dos alternativos); y 3 min para escribir dos escenarios concretos de ese caso, con datos. El entregable es la captura del diagrama más la descripción, y avisa que el escenario se reutiliza en la Actividad 4.
>
> **Por qué importa:** fija el entregable y el orden: sin la justificación de cada relación el diagrama está a medias, y los escenarios que escriban son los que después se convierten en pruebas de aceptación.
>
> **Ejemplo:** el `«include»` sería `Registrar acta ──«include»──▶ Validar acta` y la generalización `Observador ──▷ Ciudadano`, con la razón escrita al lado.
>
> ![[Casos de uso SIEL-7.png]]
>
> **Se lee así:** el enunciado completo del caso, rotulado como ficticio y con fines didácticos: el país se divide en provincias → cantones → parroquias; las organizaciones políticas inscriben candidaturas para la alcaldía de un cantón o la prefectura de una provincia, con candidato principal y, en prefectura, un viceprefecto; un funcionario electoral califica cada candidatura (aprueba o rechaza); el padrón electoral se importa desde el sistema del Registro Civil; el día de la elección el presidente de cada JRV registra el acta de escrutinio con los votos de cada candidatura, los nulos y los blancos, el sistema la valida contra el padrón de la junta y, si encuentra inconsistencias, la envía a revisión; cualquier ciudadano consulta su lugar de votación y los resultados, y un observador acreditado, además, descarga las actas escaneadas.
>
> **Por qué importa:** es la fuente de la que salen los actores, los casos y las clases del SIEL, y la misma que se reutiliza en las cuatro actividades; sin el enunciado, cualquier diagrama del caso es inventado.
>
> **Ejemplo:** la frase "el presidente de cada junta receptora del voto (JRV) registra el acta de escrutinio" es la que produce el actor `Presidente de JRV` y el caso `Registrar acta de escrutinio`.

---

> [!note] 📋 ️ Originales
>
> - Mapa de contenido: [[../../../Diseño de Software|Diseño de Software]]
> - Complemento: [[Caso SIEL - Modelo de Clases]]

**Tags:** #CCPG1042 #unidad2 #siel #casos-de-uso
