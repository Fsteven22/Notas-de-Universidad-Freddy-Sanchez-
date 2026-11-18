---
dg-publish: true
tags: [CCPG1004, cysoc, unidad1, computadoras-tempranas]
---

# 🖥️ Computadoras Modernas Tempranas

## 🎯 Introducción

> [!info] 💡 ¿Cómo pasamos de máquinas mecánicas a computadoras electrónicas?
>
> Entre finales del siglo XIX y mediados del XX, los avances en electromecánica y electrónica permitieron dar el salto de las calculadoras mecánicas a las primeras computadoras programables. Este período sentó las bases de la arquitectura que usamos hasta hoy.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Computadoras_Modernas_Tempranas_01.svg]]
>
> **Se lee así:** etapas de la construcción de la computación moderna: máquinas mecánicas del siglo XIX (cálculo por engranajes), tabuladores electromecánicos (el censo de Hollerith), teoría de computación (máquina de Turing y algoritmos), primeras computadoras electrónicas (ENIAC) y, como culminación, la arquitectura Von Neumann.
> **Por qué importa:** muestra por qué modernas computadoras son básicamente el mismo diseño: la idea de programa almacenado definida en 1945 sigue siendo el modelo de todo ordenador personal.
> **Ejemplo:** cuando compilas código en tu laptop, el procesador ejecuta instrucciones desde la memoria según la arquitectura de Von Neumann descrita aquí.

---

## 📊 Herman Hollerith — El tabulador electromecánico (s. XIX)

> [!note] 📊 Automatizando el censo
>
> **Herman Hollerith** inventó el primer **tabulador electromecánico**, una máquina capaz de leer y procesar tarjetas perforadas de forma automática. Fue desarrollado para procesar el censo de los Estados Unidos de 1890, reduciendo el tiempo de procesamiento de años a meses.
>
> Su empresa eventualmente se fusionaría con otras para formar **IBM**.
>
> | Dato | Detalle |
> |---|---|
> | **Época** | Finales s. XIX |
> | **Innovación** | Primer tabulador electromecánico |
> | **Aplicación** | Censo de EE.UU. de 1890 |
> | **Legado** | Su empresa derivó en IBM |

---

## 🧠 Alan Turing — La Máquina de Turing (1937)

> [!important] 🧠 El fundamento teórico de la computación moderna
>
> En **1937**, **Alan Turing** publicó un célebre artículo en el que definió una máquina calculadora de capacidad infinita — la **Máquina de Turing** — que operaba basándose en una serie de instrucciones lógicas.
>
> Este modelo teórico sentó las bases del concepto moderno de **algoritmo** y demostró que mediante dispositivos formales y simples era posible resolver cualquier problema matemático representable mediante un algoritmo.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Computadoras_Modernas_Tempranas_02.svg]]
>
> | Dato | Detalle |
> |---|---|
> | **Año** | 1937 |
> | **Aporte** | Definición formal de algoritmo y computabilidad |
> | **Relevancia** | Base teórica de toda la computación moderna |
> | **Legado** | El Premio Turing es el equivalente al Nobel en computación |

---

## 🏛️ Mark I — Harvard (1944)

> [!note] 🏛️ La primera computadora electromecánica de gran escala
>
> En **1944**, la **Universidad de Harvard** construyó la **Mark I**, una computadora electromecánica de gran escala liderada por **Howard H. Aiken**. Fue una de las primeras máquinas capaces de ejecutar secuencias largas de operaciones aritméticas de forma automática.
>
> | Dato | Detalle |
> |---|---|
> | **Año** | 1944 |
> | **Institución** | Universidad de Harvard |
> | **Líder** | Howard H. Aiken |
> | **Tipo** | Electromecánica |
> | **Relevancia** | Primera computadora de gran escala en EE.UU. |

---

## ⚡ ENIAC — Universidad de Pensilvania (1947)

> [!important] ⚡ La primera computadora electrónica
>
> En **1947**, la **Universidad de Pensilvania** construyó la **ENIAC** (*Electronic Numerical Integrator And Calculator*), considerada la **primera computadora electrónica** de propósito general. Fue liderada por **John Mauchly y John Eckert**.
>
> A diferencia de la Mark I, la ENIAC usaba **válvulas de vacío** en lugar de relés electromecánicos, lo que la hacía miles de veces más rápida.
>
> | Dato | Detalle |
> |---|---|
> | **Año** | 1947 |
> | **Institución** | Universidad de Pensilvania |
> | **Líderes** | John Mauchly y John Eckert |
> | **Tecnología** | Válvulas de vacío |
> | **Título** | Primera computadora electrónica |
> | **Limitación** | Se programaba cambiando cables físicamente |

---

## 🔬 John von Neumann — La arquitectura moderna (1950)

> [!important] 🔬 La idea que cambió todo
>
> **John von Neumann**, quien era consultor en el proyecto ENIAC, comenzó a trabajar en la **EDVAC** (*Electronic Discrete Variable Automatic Computer*), completando su trabajo en **1950**.
>
> Su idea fundamental fue permitir que en la **memoria** coexistan **datos e instrucciones**, de modo que la computadora pudiera ser **programada en un lenguaje**, y no por medio de alambres que eléctricamente interconectaban secciones de control como en la ENIAC.
>
> ### Arquitectura Von Neumann
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Computadoras_Modernas_Tempranas_03.svg]]
>
> **Se lee así:** los tres bloques de Von Neumann y sus subdivisiones: CPU con la Unidad de Control (coordina), ALU (operaciones) y registros (valores inmediatos); memoria principal, donde viven datos e instrucciones; y sistema de entrada/salida, que conecta con teclado, monitor y disco.
> **Por qué importa:** es la anatomía interna de cualquier computadora; entenderla te permite razonar por qué un programa puede quedarse sin memoria o por qué usar el disco es más lento que la RAM.
> **Ejemplo:** tu juego cargado en RAM es ejecutado por la CPU instrucción por instrucción; cuando minimizas se pausa porque el control de CPU cede la E/S.
>
> | Componente | Función |
> |---|---|
> | **CPU** | Unidad de Control + ALU + Registros |
> | **Memoria principal** | Almacena programas y datos |
> | **Sistema E/S** | Comunicación con el exterior |
> | **Bus** | Interconexión entre componentes |
>
> > 💡 Esta arquitectura es la base de prácticamente todas las computadoras actuales, casi 75 años después.
>
> ### Legado adicional
>
> En **1951** se lanzó a la venta la **UNIVAC**, primera computadora comercial.
> Su impacto fue tal que en **1952 predijo correctamente el resultado de la
> elección presidencial de EE.UU.** — un hito que demostró al público general
> el poder real de las computadoras para procesar y analizar datos.

---

## 📅 Línea de Tiempo

> [!summary] 📅 De Hollerith a Von Neumann
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/02_-_Computadoras_Modernas_Tempranas_04.svg]]
>
> **Se lee así:** cronología: 1890 (Hollerith tabulador para el censo de EE.UU.), 1937 (Turing presenta la máquina de Turing), 1944 (Mark I liderada por Aiken), 1947 (ENIAC en UPenn, primera electrónica general), 1950 (EDVAC, programa almacenado), 1951 (UNIVAC, primera computadora comercial).
> **Por qué importa:** la II Guerra Mundial comprimió décadas de avance: en solo 10 años pasamos de kilómetros de engranajes a máquinas electrónicas de propósito general.
> **Ejemplo:** UNIVAC fue el antepasado directo de la venta comercial de computadoras; tu PC es descendiente directa de ese primer aparato pagado por un cliente en 1951.

---

## 📚 Referencias

> [!info] 📚 Referencias
>
> - Dale, Nell & Lewis, John. *Computer Science Illuminated* (6th ed.). Jones & Bartlett Learning.
> - Quinn, Michael J. *Ethics for the Information Age* (7th ed.). Pearson.
> - Syllabus oficial de Computación y Sociedad (CCPG1004), ESPOL, coordinadora Otilia M. Alejandro Molina.
**Tags:** #historia #computación #hollerith #turing #ENIAC #markI #vonneumann #EDVAC #UNIVAC #arquitectura #unidad1 #EYAG1037