---
dg-publish: true
tags: [EYAG1037, unidad1, electricidad]
---

# ⚡ Circuitos en Serie, Paralelo y Mixtos

## 🎯 Introducción

> [!info]- 💡 ¿Cómo se conectan los elementos de un circuito?
>
> Cuando múltiples elementos eléctricos forman parte de un mismo circuito, pueden combinarse de distintas maneras según la trayectoria que siga la corriente. La forma en que se conectan determina completamente el comportamiento del circuito: la distribución de voltaje, la corriente en cada rama y la resistencia equivalente total.
>
> **Analogía del mundo real:**
>
> - Un circuito en **serie** es como un collar de perlas: si una se rompe, todas se desconectan.
> - Un circuito en **paralelo** es como los carriles de una autopista: si uno se cierra, los demás siguen funcionando.
> - Un circuito **mixto** combina ambas configuraciones, como las instalaciones eléctricas de un edificio.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Circuitos_en_Serie_Paralelo_y_Mixtos_01.svg]]
>
> | Configuración | Corriente | Voltaje | Aplicación típica |
> |---|---|---|---|
> | **Serie** | Igual en todos los elementos | Se divide entre elementos | Guirnaldas, fusibles |
> | **Paralelo** | Se divide entre ramas | Igual en todas las ramas | Instalaciones domésticas |
> | **Mixto** | Varía por sección | Varía por sección | Circuitos electrónicos |

> [!note] 🖼️ Introducción
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/Pasted image 20260519230523.png]]
> 
> **Se lee así:** Muestra tres circuitos simulados lado a lado: uno en serie (fuente de 9 V, resistencia de 10 Ω y dos lámparas en un solo camino), uno mixto (20 V con secciones en serie y un grupo de lámparas en paralelo) y uno en paralelo (9 V con 10 Ω alimentando dos lámparas entre los mismos nodos). Las tres imágenes contrastan cómo se comporta el mismo tipo de elementos según la trayectoria de la corriente.
> 
> **Por qué importa:** Fija la intuición visual de las tres topologías antes de memorizar fórmulas. Evita el error de asumir que el circuito se comporta igual sin importar cómo estén conectados sus elementos.

> [!note] 🖼️ Introducción
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/ChatGPT Image 17 jun 2026, 22_43_52.png]]
> 
> **Se lee así:** Infografía sobre interconexión de fuentes: las fuentes de voltaje en serie se reemplazan por una equivalente cuya tensión es la suma algebraica según la polaridad (misma polaridad se suman, opuesta se restan) y las fuentes de corriente en paralelo se combinan igual según el sentido de la flecha. Incluye las expresiones generales $V_{eq} = \sum(\pm V_k)$ e $I_{eq} = \sum(\pm I_k)$, ejemplos numéricos y las restricciones: solo fuentes ideales independientes, no mezclar tipos de fuente y mantener una referencia de polaridad o sentido.
> 
> **Por qué importa:** Permite reducir varias fuentes a una equivalente única antes de analizar el circuito, igual que se reduce un grupo de resistencias. Evita el error de combinar fuentes incompatibles (voltajes distintos en paralelo, corrientes distintas en serie) o de sumar ignorando la polaridad y el sentido.

---

## 🔗 Circuito en Serie

> [!note]- 🔗 Una sola trayectoria para la corriente
>
> En un **circuito en serie**, los elementos están conectados uno tras otro formando una única trayectoria. La misma corriente recorre todos los elementos secuencialmente.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Circuitos_en_Serie_Paralelo_y_Mixtos_02.svg]]
>
> ### ⚙️ Leyes fundamentales en serie
>
> **1. Corriente:** La corriente es la misma en todos los elementos.
>
> $$I_{total} = I_1 = I_2 = I_3 = \cdots = I_n$$
>
> **2. Voltaje:** El voltaje de la fuente se distribuye (divide) entre los elementos. Esta es la **Ley de Kirchhoff de Voltaje (KVL)**:
>
> $$V_s = V_1 + V_2 + V_3 + \cdots + V_n$$
>
> **3. Resistencia equivalente:** Las resistencias se suman directamente.
>
> $$R_{eq} = R_1 + R_2 + R_3 + \cdots + R_n$$
>
> > 📌 **Nota:** En serie, $R_{eq}$ siempre es **mayor** que cualquiera de las resistencias individuales.
>
> ### 📐 Divisor de voltaje
>
> La tensión en cada resistor es proporcional a su valor:
>
> $$V_k = V_s \cdot \frac{R_k}{R_{eq}}$$
>
> **Ejemplo resuelto:**
>
> > Dado: $V_s = 12\text{ V}$, $R_1 = 100\ \Omega$, $R_2 = 200\ \Omega$, $R_3 = 300\ \Omega$
> >
> > $R_{eq} = 100 + 200 + 300 = 600\ \Omega$
> >
> > $I = \dfrac{12}{600} = 0.02\text{ A} = 20\text{ mA}$
> >
> > $V_1 = 20\text{ mA} \times 100\ \Omega = 2\text{ V}$
> >
> > $V_2 = 20\text{ mA} \times 200\ \Omega = 4\text{ V}$
> >
> > $V_3 = 20\text{ mA} \times 300\ \Omega = 6\text{ V}$
> >
> > ✅ Verificación KVL: $2 + 4 + 6 = 12\text{ V}$ ✓
>
> ### ⚠️ Características importantes
>
> | Característica | Descripción |
> |---|---|
> | **Fallo en cadena** | Si un elemento falla (circuito abierto), toda la corriente se interrumpe |
> | **Mayor resistencia** | $R_{eq}$ siempre supera a cualquier resistencia individual |
> | **Distribución de voltaje** | Elementos de mayor R tienen mayor caída de voltaje |
> | **Misma potencia base** | $P = I^2 R$ varía según la resistencia de cada elemento |
> 

> [!note] 🖼️ Circuito en Serie
>
> ![[../../Anexos/ChatGPT Image 30 may 2026, 20_14_44.png]]
> 
> **Se lee así:** Infografía del circuito en serie: diagrama con la fuente V y las resistencias R1, R2, R3 en un único camino; características (la corriente es la misma en todos los elementos, el voltaje se divide y un fallo en cadena interrumpe todo); y ecuaciones ($R_T = R_1 + R_2 + R_3 + \cdots$, $I = V/R_T$, $V_n = I \cdot R_n$). Cierra con un ejemplo numérico (12 V, 2+3+5 Ω → $R_T$ = 10 Ω, $I$ = 1.2 A, caídas de 2.4/3.6/6.0 V que suman 12 V) y la idea clave de que $R_T$ siempre supera a cualquier resistencia individual.
> 
> **Por qué importa:** Conecta la fórmula con un caso verificado por KVL, tal como se trabajó en el ejemplo resuelto de la sección. Evita el error de suponer que el voltaje es el mismo en cada resistor serie.

---

## 🔀 Circuito en Paralelo

> [!note]- 🔀 Múltiples trayectorias para la corriente
>
> En un **circuito en paralelo**, los elementos comparten los mismos dos nodos (terminales), por lo que el voltaje en todos ellos es idéntico. La corriente total se reparte entre las ramas disponibles.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Circuitos_en_Serie_Paralelo_y_Mixtos_03.svg]]
> 
> **Se lee así:** Diagrama de una fuente Vs conectada a tres ramas en paralelo entre el nodo positivo y el nodo negativo: la corriente se reparte como I1, I2 e I3 hacia cada rama y todas reconfluyen en el nodo inferior para cerrar el lazo. Es la vista mínima de "las mismas dos terminales" que define a un circuito en paralelo.
> 
> **Por qué importa:** Hace evidente que el voltaje es común a todas las ramas y que la corriente se divide según KCL. Evita el error de tratar las ramas como si estuvieran en serie al plantear el divisor de corriente o el equivalente.
>
> ### ⚙️ Leyes fundamentales en paralelo
>
> **1. Voltaje:** El voltaje es el mismo en todas las ramas.
>
> $$V_s = V_1 = V_2 = V_3 = \cdots = V_n$$
>
> **2. Corriente:** La corriente total se divide entre las ramas. Esta es la **Ley de Kirchhoff de Corriente (KCL)**:
>
> $$I_{total} = I_1 + I_2 + I_3 + \cdots + I_n$$
>
> **3. Resistencia equivalente:** Se calcula mediante la suma de recíprocos.
>
> $$\frac{1}{R_{eq}} = \frac{1}{R_1} + \frac{1}{R_2} + \frac{1}{R_3} + \cdots + \frac{1}{R_n}$$
>
> > 📌 **Caso especial — dos resistencias en paralelo:**
> >
> > $$R_{eq} = \frac{R_1 \cdot R_2}{R_1 + R_2}$$
>
> > 📌 **Nota:** En paralelo, $R_{eq}$ siempre es **menor** que la menor resistencia del conjunto.
>
> ### 📐 Divisor de corriente
>
> La corriente en cada rama es inversamente proporcional a su resistencia:
>
> $$I_k = I_{total} \cdot \frac{R_{eq}}{R_k}$$
>
> **Ejemplo resuelto:**
>
> > Dado: $V_s = 12\text{ V}$, $R_1 = 60\ \Omega$, $R_2 = 30\ \Omega$
> >
> > $R_{eq} = \dfrac{60 \times 30}{60 + 30} = \dfrac{1800}{90} = 20\ \Omega$
> >
> > $I_{total} = \dfrac{12}{20} = 0.6\text{ A}$
> >
> > $I_1 = \dfrac{12}{60} = 0.2\text{ A}$
> >
> > $I_2 = \dfrac{12}{30} = 0.4\text{ A}$
> >
> > ✅ Verificación KCL: $0.2 + 0.4 = 0.6\text{ A}$ ✓
>
> ### ⚠️ Características importantes
>
> | Característica | Descripción |
> |---|---|
> | **Independencia de ramas** | El fallo de una rama no afecta a las demás |
> | **Menor resistencia** | $R_{eq}$ siempre es menor que cualquier $R_k$ |
> | **Mismo voltaje** | Todos los elementos operan a la misma tensión |
> | **Mayor corriente total** | Al agregar ramas, la corriente de la fuente aumenta |

> [!note] 🖼️ Circuito en Paralelo
>
> ![[../../Anexos/ChatGPT Image 30 may 2026, 20_24_25.png]]
> 
> **Se lee así:** Infografía del circuito en paralelo: diagrama de la fuente V con R1, R2, R3 entre los mismos dos nodos; características (voltaje igual en todas las ramas, la corriente total es la suma de las ramas, un fallo en una rama no afecta a las demás y $R_T$ es menor que la menor resistencia); y ecuaciones ($1/R_T = \sum 1/R_k$, $I_T = \sum I_n$, $I_n = V/R_n$). Incluye ejemplo numérico (12 V, 2/3/6 Ω → $R_T$ = 1 Ω, corrientes de 6/4/2 A, $I_T$ = 12 A) verificado con KCL.
> 
> **Por qué importa:** Refuerza con números la aplicación de KCL al paralelo y la regla de que $R_T$ es menor que la menor resistencia. Evita el error de sumar resistencias en paralelo como si fueran serie.

---

## 🔋 Capacitores en Serie y Paralelo

> [!tip]- ⚡ Combinación de Capacitores
>
> Las reglas para capacitores son **inversas** a las de resistencias:
>
> **En paralelo** — las áreas se suman, equivale a un capacitor más grande:
>
> $$C_t = C_1 + C_2 + C_3 + \ldots$$
>
> **En serie** — la distancia entre placas aumenta, equivale a un capacitor más pequeño:
>
> $$\frac{1}{C_t} = \frac{1}{C_1} + \frac{1}{C_2} + \frac{1}{C_3} + \ldots$$
>
> > 💡 **Regla mnemotécnica:** Los capacitores se combinan al **revés** que las resistencias — paralelo suma directo, serie suma inversos.
>
> | Configuración | Fórmula | Resultado vs C individual |
> |---|---|---|
> | **Paralelo** | $C_t = C_1 + C_2 + \ldots$ | Mayor |
> | **Serie** | $\frac{1}{C_t} = \frac{1}{C_1} + \frac{1}{C_2} + \ldots$ | Menor |
>
> **Ejemplo:**
>
> > $C_1 = 4\,\mu F$, $C_2 = 6\,\mu F$
> >
> > En paralelo: $C_t = 4 + 6 = 10\,\mu F$
> >
> > En serie: $C_t = \frac{4 \times 6}{4 + 6} = \frac{24}{10} = 2.4\,\mu F$

> [!note] 🖼️ ⊣⊢ Capacitores en Serie y Paralelo
>
> ![[../../Anexos/ChatGPT Image 30 may 2026, 20_29_23.png]]
> 
> **Se lee así:** Infografía doble de capacitores: a la izquierda, serie (uno tras otro, la carga es la misma en todos, el voltaje se divide, $1/C_{eq} = \sum 1/C_n$ y $C_{eq}$ queda menor que el menor; ejemplo 2/3/6 µF → 1 µF); a la derecha, paralelo (entre los mismos nodos, el voltaje es el mismo, la carga se divide, $C_{eq} = \sum C_n$ y $C_{eq}$ queda mayor que el mayor; ejemplo → 11 µF). Cada panel trae diagrama, características, ecuaciones y ejemplo numérico completo.
> 
> **Por qué importa:** Deja las dos reglas cruzadas en un solo vistazo: paralelo suma directo y serie suma invertidos, al revés que las resistencias. Evita aplicar a capacitores las reglas de resistencias o inductores por inercia.

---

## ⌇ Inductores en Serie y Paralelo

> [!tip]- 🧲 Combinación de Inductores
>
> Los inductores se combinan **igual que las resistencias** (asumiendo que no hay acoplamiento magnético entre ellos):
>
> **En serie:**
>
> $$L_t = L_1 + L_2 + L_3 + \ldots$$
>
> **En paralelo:**
>
> $$\frac{1}{L_t} = \frac{1}{L_1} + \frac{1}{L_2} + \frac{1}{L_3} + \ldots$$
>
> > 💡 **Regla mnemotécnica:** Inductores = Resistencias en cuanto a combinación. Capacitores = al revés.
>
> | Configuración | Fórmula | Resultado vs L individual |
> |---|---|---|
> | **Serie** | $L_t = L_1 + L_2 + \ldots$ | Mayor |
> | **Paralelo** | $\frac{1}{L_t} = \frac{1}{L_1} + \frac{1}{L_2} + \ldots$ | Menor |
>
> **Ejemplo:**
>
> > $L_1 = 3\,mH$, $L_2 = 6\,mH$
> >
> > En serie: $L_t = 3 + 6 = 9\,mH$
> >
> > En paralelo: $L_t = \frac{3 \times 6}{3 + 6} = \frac{18}{9} = 2\,mH$

> [!note] 🖼️ Inductores en Serie y Paralelo
>
> ![[../../Anexos/file_000000006634720e8575d8d5057e5f59.png]]
> 
> **Se lee así:** Infografía doble de inductores, en espejo con la de capacitores: a la izquierda, serie (el mismo camino para la corriente, $L_{eq} = L_1 + L_2 + L_3$, el voltaje se reparte entre ellos y $L_{eq}$ es mayor que la mayor inductancia); a la derecha, paralelo (entre los mismos nodos, $1/L_{eq} = \sum 1/L_n$, el voltaje es común y $L_{eq}$ es menor que la menor). Incluye ejemplo numérico con V = 12 V y L = 2/3/6 mH (serie → 11 mH; paralelo → 1 mH) usando reactancias $X_L = 2\pi f L$.
> 
> **Por qué importa:** Confirma que, sin acoplamiento magnético, los inductores se combinan exactamente igual que las resistencias. Evita el error de aplicarles las reglas inversas de los capacitores.

---
## 🔁 Circuito Mixto (Serie-Paralelo)

> [!tip]- 🔁 Combinación de ambas configuraciones
>
> Un **circuito mixto** (o serie-paralelo) combina secciones en serie con grupos en paralelo. Son los circuitos más comunes en la práctica real.
>
> El método de análisis consiste en **simplificar progresivamente** el circuito, reduciendo grupos paralelos o series a su equivalente, hasta obtener un único $R_{eq}$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Circuitos_en_Serie_Paralelo_y_Mixtos_04.svg]]
>
> ### 🧮 Metodología de simplificación paso a paso
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Circuitos_en_Serie_Paralelo_y_Mixtos_05.svg]]
>
> **Ejemplo resuelto:**
>
> > Dado: $V_s = 24\text{ V}$, $R_1 = 4\ \Omega$ (serie), $R_2 = 12\ \Omega$ y $R_3 = 6\ \Omega$ (paralelo entre sí), $R_4 = 2\ \Omega$ (serie)
> >
> > **Paso 1:** Calcular equivalente de $R_2 \| R_3$:
> > $$R_{23} = \frac{12 \times 6}{12 + 6} = \frac{72}{18} = 4\ \Omega$$
> >
> > **Paso 2:** Circuito reducido en serie: $R_1$, $R_{23}$, $R_4$
> > $$R_{eq} = 4 + 4 + 2 = 10\ \Omega$$
> >
> > **Paso 3:** Corriente total:
> > $$I = \frac{24}{10} = 2.4\text{ A}$$
> >
> > **Paso 4:** Voltaje en el grupo paralelo:
> > $$V_{23} = I \times R_{23} = 2.4 \times 4 = 9.6\text{ V}$$
> >
> > **Paso 5:** Corrientes en cada rama del paralelo:
> > $$I_2 = \frac{9.6}{12} = 0.8\text{ A} \qquad I_3 = \frac{9.6}{6} = 1.6\text{ A}$$
> >
> > ✅ Verificación KCL: $0.8 + 1.6 = 2.4\text{ A}$ ✓

> [!note] 🖼️ Circuito Mixto (Serie-Paralelo)
>
> ![[../../Anexos/file_00000000bdc471f7b12b164a687c03e7.png]]
> 
> **Se lee así:** Infografía de un circuito mixto resuelto paso a paso; el ejemplo está planteado con inductores (L1 en serie, L2‖L3 en la sección central, L4 en serie), pero el método es el mismo que el de un mixto resistivo: identificar el grupo en paralelo, calcular su equivalente ($L_p$ = 2 mH), reemplazarlo, combinar lo que queda en serie ($L_{eq}$ = 8 mH) y recién entonces hallar $I_T$ y los voltajes y corrientes de cada tramo, con verificación $V_T$ = 24 V.
> 
> **Por qué importa:** Modela el procedimiento completo de "simplificar por partes" que la sección exige: primero el paralelo, después la serie y al final repartir valores. Evita atacar el circuito completo de una sola vez y perder la topología al redibujarlo.

---
## 🔋 Potencia en Circuitos

> [!tip]- ⚡ Potencia disipada y suministrada
>
> La **potencia** indica la rapidez con que se transfiere o disipa energía en el circuito. Se expresa en vatios (W).
>
> $$P = V \cdot I = I^2 \cdot R = \frac{V^2}{R}$$
>
> **Conservación de energía — Teorema de Tellegen:**
>
> $$\sum P_{suministrada} = \sum P_{disipada}$$
>
> La potencia total entregada por las fuentes debe ser igual a la potencia consumida por todos los elementos pasivos.
>
> **Comparación de potencia según configuración:**
>
> | Parámetro | Serie | Paralelo |
> |---|---|---|
> | **Potencia total** | $P_T = I^2 R_{eq}$ | $P_T = \dfrac{V_s^2}{R_{eq}}$ |
> | **Potencia por elemento** | $P_k = I^2 R_k$ (mayor R → mayor P) | $P_k = \dfrac{V_s^2}{R_k}$ (menor R → mayor P) |
> | **Al agregar elementos** | $R_{eq}$ aumenta → $P_T$ disminuye | $R_{eq}$ disminuye → $P_T$ aumenta |

---

## 📊 Comparación General

> [!success]- 📊 Serie vs. Paralelo vs. Mixto
>
> | Característica | Serie | Paralelo | Mixto |
> |---|---|---|---|
> | **Trayectorias de corriente** | Una sola | Múltiples | Combinadas |
> | **Corriente** | $I_1 = I_2 = \cdots$ | Se divide | Varía por sección |
> | **Voltaje** | Se divide | $V_1 = V_2 = \cdots$ | Varía por sección |
> | **$R_{eq}$** | $\sum R_k$ (mayor) | $< R_{min}$ (menor) | Depende del circuito |
> | **Ley aplicada** | KVL | KCL | KVL + KCL |
> | **Fallo de un elemento** | Interrumpe todo | Solo esa rama | Depende de la ubicación |
> | **Ejemplo real** | Luces navideñas antiguas | Tomacorrientes del hogar | Circuitos electrónicos |
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Circuitos_en_Serie_Paralelo_y_Mixtos_06.svg]]
> 
> **Se lee así:** Diagrama de decisión que parte de "Fuente Vs" y se bifurca en tres tipos de circuito: Serie (I constante, V se divide, Req = ΣRk), Paralelo (V constante, I se divide, Req < Rmin) y Mixto (simplificar paso a paso, KVL + KCL). Cada rama resume el comportamiento y la estrategia de análisis de esa topología.
> 
> **Por qué importa:** Funciona como mapa rápido al enfrentar un circuito nuevo: primero se identifica la topología y después se elige la herramienta. Evita aplicar el divisor de voltaje a un paralelo o KCL de ramas a una serie única.

---

## 📊 Resumen Visual

> [!note] 🖼️ Resumen Visual
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/04_-_Circuitos_en_Serie_Paralelo_y_Mixtos_07.svg]]
> 
> **Se lee así:** Mapa mental con raíz "Circuitos Eléctricos" y cuatro ramas: Serie (I constante, V se divide, KVL, divisor de voltaje), Paralelo (V constante, I se divide, KCL, divisor de corriente), Mixto (simplificación paso a paso, KVL + KCL, aplicaciones reales) y Leyes de Kirchhoff (KCL en nodos, KVL en mallas, conservación). Resume en una sola vista todo lo desarrollado en la nota.
> 
> **Por qué importa:** Es la vista de repaso del capítulo antes de un examen o de resolver ejercicios. Evita mezclar qué ley gobierna cada configuración o saltarse la verificación por conservación.

---

## 📝 Ejercicios Prácticos

> [!example]- ✏️ Ejercicio 1 — Resistencia Total en Circuito Mixto (terminales AO)
>
> **Dado** el siguiente circuito con R1 a R6, encontrar la resistencia total vista desde los terminales A y O.
>
> **Estrategia de solución:**
>
> | Paso | Acción |
> |---|---|
> | **1** | Identificar qué resistencias están en serie y cuáles en paralelo |
> | **2** | Reducir los grupos paralelos primero: $R_{paralelo} = \frac{R_a \cdot R_b}{R_a + R_b}$ |
> | **3** | Sumar los resultados en serie con las resistencias restantes |
> | **4** | Verificar con KVL/KCL si el enunciado da valores de voltaje o corriente |
>
> > 💡 Siempre redibuja el circuito simplificado después de cada reducción para no perder la topología.
>

> [!example]- ✏️ Ejercicio 2 — Circuito con Cruce de Corrientes (I1, I2)
>
> **Dado** un circuito con dos corrientes de malla I1 e I2 que se cruzan, encontrar los valores de cada corriente.
>
> **Estrategia de solución:**
>
> | Paso | Acción |
> |---|---|
> | **1** | Identificar los lazos independientes del circuito |
> | **2** | Asignar sentido horario a cada corriente de malla (I1, I2) |
> | **3** | Aplicar KVL a cada lazo: $\sum V = 0$ |
> | **4** | En la rama compartida, la corriente neta es $I_1 - I_2$ (o $I_2 - I_1$ según sentido) |
> | **5** | Resolver el sistema de ecuaciones resultante |
>
> > 💡 En la rama común a dos mallas, la corriente que circula es la **diferencia algebraica** de las corrientes de malla, respetando el sentido asignado.

---
## 📚 Referencias

> [!quote]- 📖 Fuentes consultadas
>
> [1] R. L. Boylestad, *Introductory Circuit Analysis*, 13th ed. Hoboken, NJ, USA: Pearson, 2016, pp. 131–210.
>
> [2] C. K. Alexander y M. N. O. Sadiku, *Fundamentals of Electric Circuits*, 6th ed. New York, USA: McGraw-Hill, 2016, pp. 29–70.
>
> [3] A. R. Hambley, *Electrical Engineering: Principles and Applications*, 7th ed. Hoboken, NJ, USA: Pearson, 2018, pp. 33–90.
>
> [4] J. W. Nilsson y S. A. Riedel, *Electric Circuits*, 11th ed. Hoboken, NJ, USA: Pearson, 2019, pp. 22–100.
>
> [5] A. Hermosa Donante, *Electrónica Aplicada*, 1.ª ed. Mexico: Alfaomega Grupo Editor, 2013, pp. 76–130. ISBN-13: 9786077074045.

## ✅ Metas de Aprendizaje
> [!note] Nivel Basico
>
> - [ ] Enuncio leyes de serie (I igual, V se divide, Req suma) y paralelo (V igual, I se divide).
> - [ ] Calculo Req en serie y paralelo (caso 2 resistencias: R1·R2/(R1+R2)).
> - [ ] Aplico divisor de voltaje Vk=Vs·Rk/Req y divisor de corriente.
>

> [!note] Nivel Intermedio
>
> - [ ] Simplifico un circuito mixto reduciendo grupos paralelos y sumando en serie.
> - [ ] Calculo C e L equivalentes en serie/paralelo.
> - [ ] Verifico con KVL/KCL y balances de potencia.
>

> [!note] Nivel Avanzado
>
> - [ ] Resuelvo un mixto con 4+ resistencias y determino voltajes y corrientes.
> - [ ] Predigo efecto de agregar/quitar una rama paralela sobre Req y potencia.
> - [ ] Justifico por que un fallo en serie interrumpe todo y en paralelo no.
>

---

## 🔗 Conexiones

> [!quote] 🔗 Conexiones
>
> - Previo: [[03 - Elementos Basicos de un Circuito Electrico]] — R, C, L que combinas aqui
> - Siguiente: [[05 - Leyes de Ohm y Kirchhoff]] — KVL/KCL que usas para resolver mixtos
> - Adelante: [[04 - Circuitos de Filtrado y Fuentes Lineales]] — filtros que usan estas mismas combinaciones

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../../Fundamentos de Electricidad y Sistemas Digitales|⚡ Mapa de contenido]]
> - Índice de la materia: [[../../Índice de Contenido|Índice de Contenido]]
> - Siguiente: [[05 - Leyes de Ohm y Kirchhoff]]
> - Syllabus: [[../../Bienvenida y Syllabus Fundamentos de Electricidad y Sistemas Digitales|👋 Bienvenida y Syllabus]]

**Tags:** #circuito #serie #paralelo #mixto #kirchhoff #KVL #KCL #divisor #resistencia #potencia #EYAG1037 #FESD #ESPOL #unidad1
