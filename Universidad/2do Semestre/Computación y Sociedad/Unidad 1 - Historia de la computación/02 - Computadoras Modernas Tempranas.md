# 🖥️ Computadoras Modernas Tempranas

## 🎯 Introducción

> [!info]- 💡 ¿Cómo pasamos de máquinas mecánicas a computadoras electrónicas?
>
> Entre finales del siglo XIX y mediados del XX, los avances en electromecánica y electrónica permitieron dar el salto de las calculadoras mecánicas a las primeras computadoras programables. Este período sentó las bases de la arquitectura que usamos hasta hoy.
>
> ```mermaid
> graph LR
>     A[Máquinas mecánicas<br/>s. XIX] --> B[Tabuladores<br/>electromecánicos]
>     B --> C[Teoría de<br/>computación]
>     C --> D[Primeras computadoras<br/>electrónicas]
>     D --> E[Arquitectura<br/>Von Neumann]
>
>     style A fill:#fff4e1
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#f5e1ff
>     style E fill:#ffe1e1
> ```

---

## 📊 Herman Hollerith — El tabulador electromecánico (s. XIX)

> [!note]- 📊 Automatizando el censo
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

> [!important]- 🧠 El fundamento teórico de la computación moderna
>
> En **1937**, **Alan Turing** publicó un célebre artículo en el que definió una máquina calculadora de capacidad infinita — la **Máquina de Turing** — que operaba basándose en una serie de instrucciones lógicas.
>
> Este modelo teórico sentó las bases del concepto moderno de **algoritmo** y demostró que mediante dispositivos formales y simples era posible resolver cualquier problema matemático representable mediante un algoritmo.
>
> ```mermaid
> graph TD
>     A[Cinta infinita<br/>de símbolos] --> B[Cabezal lector/escritor]
>     B --> C[Tabla de reglas<br/>estado + símbolo → acción]
>     C --> D[Nuevo estado<br/>+ símbolo escrito]
>     D --> B
>
>     style A fill:#e1f5ff
>     style B fill:#e1ffe1
>     style C fill:#fff4e1
>     style D fill:#f5e1ff
> ```
>
> | Dato | Detalle |
> |---|---|
> | **Año** | 1937 |
> | **Aporte** | Definición formal de algoritmo y computabilidad |
> | **Relevancia** | Base teórica de toda la computación moderna |
> | **Legado** | El Premio Turing es el equivalente al Nobel en computación |

---

## 🏛️ Mark I — Harvard (1944)

> [!note]- 🏛️ La primera computadora electromecánica de gran escala
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

> [!important]- ⚡ La primera computadora electrónica
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

> [!important]- 🔬 La idea que cambió todo
>
> **John von Neumann**, quien era consultor en el proyecto ENIAC, comenzó a trabajar en la **EDVAC** (*Electronic Discrete Variable Automatic Computer*), completando su trabajo en **1950**.
>
> Su idea fundamental fue permitir que en la **memoria** coexistan **datos e instrucciones**, de modo que la computadora pudiera ser **programada en un lenguaje**, y no por medio de alambres que eléctricamente interconectaban secciones de control como en la ENIAC.
>
> ### Arquitectura Von Neumann
>
> ```mermaid
> graph TD
>     CPU["CPU
>     ├── Unidad de Control
>     ├── ALU (Unidad Aritmético-Lógica)
>     └── Registros"] <--> MEM[Memoria Principal<br/>Datos + Instrucciones]
>     CPU <--> IO[Sistema de<br/>Entrada / Salida]
>
>     style CPU fill:#e1f5ff
>     style MEM fill:#e1ffe1
>     style IO fill:#fff4e1
> ```
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

> [!summary]- 📅 De Hollerith a Von Neumann
>
> ```mermaid
> timeline
>     title Computadoras Modernas Tempranas
>     1890 : Hollerith — Tabulador electromecánico para el censo
>     1937 : Alan Turing — Máquina de Turing y teoría de algoritmos
>     1944 : Harvard — Mark I liderada por Howard H. Aiken
>     1947 : UPenn — ENIAC, primera computadora electrónica
>     1950 : Von Neumann — EDVAC y arquitectura de programa almacenado
>     1951 : UNIVAC — Primera computadora comercial
> ```

---

**Tags:** #historia #computación #hollerith #turing #ENIAC #markI #vonneumann #EDVAC #UNIVAC #arquitectura #unidad1 #EYAG1037