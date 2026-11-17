---
dg-publish: true
tags: [EYAG1037, unidad1, electricidad]
---

# 🧩 Teoremas de Análisis de Circuitos

## 🎯 Introducción

> [!info]- 💡 ¿Por qué necesitamos teoremas de análisis?
> 
> Las leyes de Ohm y Kirchhoff permiten analizar cualquier circuito, pero en redes complejas generan sistemas de muchas ecuaciones simultáneas que resultan tediosos de resolver. Los **teoremas de análisis de circuitos** son herramientas que simplifican radicalmente ese proceso, permitiendo:
> 
> - Reducir circuitos complejos a equivalentes simples.
> - Calcular la respuesta ante una sola fuente o elemento a la vez.
> - Determinar la condición de máxima transferencia de potencia.
> - Reemplazar redes de múltiples fuentes y resistencias por modelos equivalentes de uno o dos componentes.
> 
> **Analogía del mundo real:**
> 
> - El **Teorema de Superposición** es como calcular el ruido total de una ciudad sumando por separado el ruido del tráfico, la música y la construcción.
> - El **Teorema de Thévenin** es como reemplazar una red eléctrica compleja por una sola batería con su resistencia interna.
> - El **Teorema de Norton** es el equivalente usando una fuente de corriente.
> - La **Máxima Transferencia de Potencia** responde cuándo una carga extrae el máximo de energía posible de la fuente.
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_01.svg]]
> 
> |Teorema|Utilidad principal|
> |---|---|
> |**Superposición**|Circuitos con múltiples fuentes independientes|
> |**Thévenin**|Simplificar una red para analizar el elemento de carga|
> |**Norton**|Alternativa corriente al equivalente Thévenin|
> |**Máx. transferencia**|Encontrar $R_L$ que maximiza potencia entregada|
> |**Transformación de fuentes**|Convertir entre fuente de voltaje y corriente|

> [!note] 🖼️ Introducción
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/ChatGPT Image 17 jun 2026, 22_31_35.png]]
> 
> **Se lee así:** Infografía de ESPOL sobre el **método de tensiones de nodo**: parte de la KCL en cada nodo (tomando tierra como referencia), expresa las corrientes en resistencias como $(V_i - V_j)/R$ y organiza todo en el sistema matricial $G\,V = I$, con un ejemplo numérico de tres nodos. Aunque aparece en la introducción, su contenido es el método de nodos, no un teorema.
> 
> **Por qué importa:** Los teoremas de análisis se apoyan en KCL/KVL y en sistemas de ecuaciones, no los reemplazan. Ver el método de nodos aquí evita tratar los teoremas como recetas memorizadas y recuerda que siempre hay una verificación sistemática disponible.

> [!note] 🖼️ Introducción
>
> ![[../../Unidad 0 - Guias y Ejercicios/Figuras/ChatGPT Image 17 jun 2026, 21_36_10.png]]
> 
> **Se lee así:** Infografía de la **forma matricial directa por inspección**: detalla las reglas para armar $[R]\cdot[I]=[V]$ por mallas (diagonal = suma de resistencias de la malla, fuera de diagonal = menos la compartida, vector $[V]$ con el signo según el sentido de recorrido) y $[G]\cdot[V]=[I]$ por nodos con conductancias, con ejemplos numéricos de dos mallas y dos nodos. Cierra con la nota de que en AC se usan $Z$ e $Y$ en lugar de $R$ y $G$.
> 
> **Por qué importa:** Es la base de la sección de métodos directos matriciales más adelante en la nota. Armar la matriz por inspección ahorra plantear KVL/KCL paso a paso y el error más caro que evita es equivocar el signo de los términos mutuos.

---

## 🔀 Teorema de Superposición

> [!note]- 🔀 Una fuente activa a la vez
> 
> El **Teorema de Superposición** establece que en un circuito lineal con múltiples fuentes independientes, la respuesta (voltaje o corriente) en cualquier elemento es la **suma algebraica** de las respuestas producidas por cada fuente actuando individualmente, mientras las demás se eliminan.
> 
> > _"La respuesta total es la superposición (suma) de las respuestas individuales de cada fuente."_
> 
> ### ⚙️ Procedimiento
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_02.svg]]
> 
> ### 🔕 Cómo "apagar" una fuente
> 
> |Tipo de fuente|Acción para apagarla|Equivalente eléctrico|
> |---|---|---|
> |**Fuente de voltaje independiente**|Reemplazar por un **cortocircuito** ($V = 0$)|Cable conductor|
> |**Fuente de corriente independiente**|Reemplazar por un **circuito abierto** ($I = 0$)|Desconexión|
> 
> > ⚠️ Las **fuentes dependientes** (controladas) **nunca se apagan**; permanecen activas durante todo el análisis.
> 
> ### 🧮 Ejemplo resuelto
> 
> > Dado: $V_s = 12\text{ V}$, $I_s = 2\text{ A}$, $R_1 = 6\ \Omega$, $R_2 = 3\ \Omega$. Encontrar $V_{R2}$.
> > 
> > **Paso 1 — Solo $V_s$ activa** (apagar $I_s$: circuito abierto):
> > 
> > $R_1$ y $R_2$ en serie → $R_{eq} = 6 + 3 = 9\ \Omega$
> > 
> > $I' = \dfrac{12}{9} = \dfrac{4}{3}\text{ A}$ → $V'_{R2} = \dfrac{4}{3} \times 3 = 4\text{ V}$
> > 
> > **Paso 2 — Solo $I_s$ activa** (apagar $V_s$: cortocircuito):
> > 
> > $R_1 | R_2 = \dfrac{6 \times 3}{6 + 3} = 2\ \Omega$
> > 
> > Divisor de corriente: $I''_{R2} = 2 \times \dfrac{6}{6+3} = \dfrac{4}{3}\text{ A}$ → $V''_{R2} = \dfrac{4}{3} \times 3 = 4\text{ V}$
> > 
> > **Paso 3 — Superposición:** $$V_{R2} = V'_{R2} + V''_{R2} = 4 + 4 = 8\text{ V}$$
> 
> ### ⚠️ Limitaciones
> 
> |Aplica|No aplica|
> |---|---|
> |Voltajes y corrientes (cantidades lineales)|Potencia ($P = I^2R$: no lineal)|
> |Circuitos con elementos lineales|Circuitos con elementos no lineales|

> [!note] 🖼️ Teorema de Superposición
>
> ![[../../Anexos/ChatGPT Image 17 jun 2026, 00_07_49.png]]
> 
> **Se lee así:** Infografía del **Teorema de Superposición**: enuncia $X = X_1 + X_2 + \cdots + X_n$ para voltajes o corrientes, muestra cómo desactivar cada tipo de fuente (voltaje → cortocircuito, corriente → circuito abierto, dependientes nunca se desactivan) y lo desarrolla paso a paso con un ejemplo de dos fuentes ($V_1 = 10\text{ V}$, $I_2 = 2\text{ A}$) que termina en $I_o \approx 1.889\text{ A}$. Incluye además las observaciones: aplica solo a circuitos lineales y a tensiones/corrientes, no a potencia.
> 
> **Por qué importa:** Es la versión en afiche de todo el procedimiento de la sección: apagar fuentes mal (o intentar sumar potencias parciales) es el error clásico de este teorema. Sirve de repaso visual antes del examen.

---

## ⚡ Divisor de Voltaje y Divisor de Corriente

> [!note]- ⚡ Atajos para circuitos simples de una malla o un par de nodos
> 
> Los **divisores** son fórmulas directas que evitan plantear KVL o KCL completo cuando el circuito tiene estructura simple. Son los atajos más rápidos en exámenes.
> 
> ### 🔽 Divisor de Voltaje
> 
> **Aplica a:** circuitos de **una sola malla** (resistores en serie con una fuente de voltaje).
> 
> > _"Método para hallar la tensión a través de una resistencia en un circuito de una sola malla."_
> 
> $$\boxed{V_{R_i} = \frac{V_f \cdot R_i}{R_{eq}}}$$
> 
> Donde $R_{eq}$ es la resistencia total equivalente de la malla y $V_f$ es la fuente de voltaje.
> 
> **Ejemplo resuelto:**
> 
> > Circuito: $V_S = 12\text{ V}$, $R_3 = 4\ \Omega$ (serie), $R_1 = 6\ \Omega | R_2 = 3\ \Omega$ en paralelo.
> > 
> > Paso 1 — Reducir paralelo: $R_{1|2} = \dfrac{6 \times 3}{6 + 3} = 2\ \Omega$
> > 
> > Paso 2 — $R_{eq} = R_3 + R_{1|2} = 4 + 2 = 6\ \Omega$
> > 
> > Paso 3 — Voltaje sobre el paralelo $R_{1|2}$: $$V_x = \frac{V_S \cdot R_{1|2}}{R_{eq}} = \frac{12 \times 2}{6} = 4\text{ V}$$
> 
> ---
> 
> ### 🔼 Divisor de Corriente
> 
> **Aplica a:** circuitos con **un solo par de nodos** (resistores en paralelo con una fuente de corriente).
> 
> > _"Método para hallar la corriente a través de una resistencia en un circuito con un solo par de nodos."_
> 
> $$\boxed{I_{R_i} = \frac{R_{eq} \cdot I_f}{R_i}}$$
> 
> Donde $R_{eq}$ es la resistencia equivalente del paralelo, $I_f$ es la fuente de corriente, y $R_i$ es la resistencia de la **rama donde se calcula** la corriente.
> 
> > 💡 **Equivalencia para dos resistores en paralelo:** las dos expresiones siguientes son idénticas algebraicamente: $$I_{R_1} = I_f \cdot \frac{R_{eq}}{R_1} \equiv I_f \cdot \frac{R_2}{R_1 + R_2}$$ La segunda forma surge de sustituir $R_{eq} = \dfrac{R_1 R_2}{R_1+R_2}$ y simplificar. Usa la que prefieras, pero no las mezcles en el mismo desarrollo.
> 
> **Ejemplo resuelto:**
> 
> > Circuito: fuente de corriente $I_f = 3\text{ A}$, $R_1 = 6\ \Omega$ y $R_2 = 3\ \Omega$ en paralelo. Encontrar $I_{R_1}$ e $I_{R_2}$.
> > 
> > $R_{eq} = \dfrac{6 \times 3}{6 + 3} = 2\ \Omega$
> > 
> > $$I_{R_1} = I_f \cdot \frac{R_{eq}}{R_1} = 3 \times \frac{2}{6} = 1\text{ A}$$
> > 
> > $$I_{R_2} = I_f \cdot \frac{R_{eq}}{R_2} = 3 \times \frac{2}{3} = 2\text{ A}$$
> > 
> > ✅ Verificación KCL: $1 + 2 = 3\text{ A} = I_f$ ✓
> 
> ### 📊 Comparación rápida
> 
> ||Divisor de voltaje|Divisor de corriente|
> |---|---|---|
> |**Configuración**|Resistores en **serie**|Resistores en **paralelo**|
> |**Fuente**|Fuente de voltaje $V_f$|Fuente de corriente $I_f$|
> |**Fórmula**|$V_{R_i} = \dfrac{V_f \cdot R_i}{R_{eq}}$|$I_{R_i} = \dfrac{R_{eq} \cdot I_f}{R_j}$|
> |**Estructura**|Una sola malla|Un solo par de nodos|
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_03.svg]]
> 
> **Se lee así:** Diagrama de decisión que parte de un circuito simple y bifurca según la estructura: resistores en **serie** con fuente de voltaje lleva al **divisor de voltaje** ($V_{Ri} = V_f \cdot R_i / R_{eq}$), y resistores en **paralelo** con fuente de corriente lleva al **divisor de corriente** ($I_{Ri} = R_{eq} \cdot I_f / R_j$). Es la síntesis gráfica de la regla "mira la topología antes de elegir la fórmula".
> 
> **Por qué importa:** El error más común con los divisores es aplicar la fórmula correcta a la topología equivocada. El diagrama obliga a clasificar el circuito (serie/voltaje vs. paralelo/corriente) antes de escribir cualquier ecuación.

> [!note] 🖼️ Divisor de Voltaje y Divisor de Corriente
>
> ![[../../Anexos/ChatGPT Image 17 jun 2026, 00_10_30.png]]
> 
> **Se lee así:** Infografía de los **divisores de voltaje y de corriente** lado a lado: a la izquierda el circuito en serie con $V_k = V_T \cdot R_k / (R_1 + \cdots + R_n)$ y su caso de dos resistencias (ejemplo $V_T = 12\text{ V}$, $4\ \Omega$ y $8\ \Omega$ → $4\text{ V}$ y $8\text{ V}$); a la derecha el circuito en paralelo con la corriente dividiéndose inversamente a las resistencias (ejemplo $I_T = 6\text{ A}$, $3\ \Omega$ y $6\ \Omega$ → $4\text{ A}$ y $2\text{ A}$). Cierra con las características de cada uno y la advertencia de no aplicarlos con fuentes dependientes o elementos no lineales.
> 
> **Por qué importa:** Refuerza la verificación de KCL/KVL ($V_T = V_1 + V_2 + \cdots$, $I_T = I_1 + I_2 + \cdots$) como control de sanidad del resultado. Evita el atajo de usar divisor de voltaje en un paralelo (o viceversa) solo porque "la fórmula se parece".

---

## 🟦 Teorema de Thévenin

> [!tip]- 🟦 Cualquier red lineal = una fuente + una resistencia
> 
> El **Teorema de Thévenin** establece que cualquier red lineal de fuentes y resistencias, vista desde dos terminales ($A$-$B$), puede reemplazarse por un circuito equivalente formado por:
> 
> - Una **fuente de voltaje** $V_{Th}$ (voltaje de Thévenin) en serie con
> - Una **resistencia** $R_{Th}$ (resistencia de Thévenin).
> 
> Fue enunciado por el ingeniero francés **Léon Charles Thévenin** en 1883.
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_04.svg]]
> 
> ### ⚙️ Procedimiento para obtener $V_{Th}$ y $R_{Th}$
> 
> **Cálculo de $V_{Th}$:**
> 
> 1. Retirar el elemento de carga $R_L$ (dejar terminales $A$-$B$ en circuito abierto).
> 2. Calcular el voltaje entre los terminales $A$ y $B$: ese es $V_{Th} = V_{oc}$.
> 
> **Cálculo de $R_{Th}$:**
> 
> |Condición del circuito|Método|
> |---|---|
> |**Solo fuentes independientes**|Apagar todas las fuentes; calcular $R_{eq}$ vista desde $A$-$B$|
> |**Con fuentes dependientes**|Aplicar fuente de prueba $V_x$ (o $I_x$) en $A$-$B$; $R_{Th} = V_x / I_x$|
> 
> **Uso del equivalente:**
> 
> Una vez obtenido el circuito Thévenin, la corriente en cualquier carga $R_L$ conectada a $A$-$B$ es:
> 
> $$\boxed{I_L = \frac{V_{Th}}{R_{Th} + R_L}}$$
> 
> $$V_L = I_L \cdot R_L = V_{Th} \cdot \frac{R_L}{R_{Th} + R_L}$$
> 
> ### 🧮 Ejemplo resuelto
> 
> > Dado: $V_s = 30\text{ V}$, $R_1 = 6\ \Omega$, $R_2 = 4\ \Omega$, $R_3 = 3\ \Omega$ (carga a retirar). Terminales $A$-$B$ tras retirar $R_3$.
> > 
> > **$V_{Th}$** (circuito abierto en $A$-$B$):
> > 
> > $I = \dfrac{30}{6+4} = 3\text{ A}$ → $V_{Th} = V_{AB} = 3 \times 4 = 12\text{ V}$
> > 
> > **$R_{Th}$** (apagar $V_s$: cortocircuito):
> > 
> > $R_{Th} = R_1 | R_2 = \dfrac{6 \times 4}{6+4} = 2.4\ \Omega$
> > 
> > **Corriente en $R_3$:**
> > 
> > $I_{R3} = \dfrac{12}{2.4 + 3} = \dfrac{12}{5.4} \approx 2.22\text{ A}$

---

## 🟧 Teorema de Norton

> [!tip]- 🟧 Equivalente con fuente de corriente
> 
> El **Teorema de Norton** es el dual del Teorema de Thévenin. Establece que cualquier red lineal vista desde dos terminales puede reemplazarse por:
> 
> - Una **fuente de corriente** $I_N$ (corriente de Norton) en paralelo con
> - Una **resistencia** $R_N$ (resistencia de Norton).
> 
> Fue enunciado por **Edward Lawry Norton** en 1926.
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_05.svg]]
> 
> ### ⚙️ Parámetros del equivalente Norton
> 
> |Parámetro|Definición|Cómo se obtiene|
> |---|---|---|
> |$I_N$|Corriente de cortocircuito entre $A$ y $B$|Cortocircuitar terminales $A$-$B$ y medir $I_{sc}$|
> |$R_N$|Resistencia vista desde $A$-$B$|Idéntica a $R_{Th}$|
> 
> $$\boxed{I_N = I_{sc} \qquad R_N = R_{Th}}$$
> 
> ### 🔄 Relación entre Thévenin y Norton
> 
> Los dos equivalentes son **intercambiables** mediante la transformación de fuentes:
> 
> $$V_{Th} = I_N \cdot R_N \qquad\qquad I_N = \frac{V_{Th}}{R_{Th}}$$
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_06.svg]]
> 
> ### 🧮 Ejemplo resuelto
> 
> > Usando el mismo circuito del ejemplo Thévenin: $V_s = 30\text{ V}$, $R_1 = 6\ \Omega$, $R_2 = 4\ \Omega$.
> > 
> > **$R_N = R_{Th} = 2.4\ \Omega$** (igual al caso Thévenin)
> > 
> > **$I_N$** (cortocircuito en $A$-$B$):
> > 
> > $I_N = \dfrac{V_{Th}}{R_{Th}} = \dfrac{12}{2.4} = 5\text{ A}$
> > 
> > ✅ Verificación: $V_{Th} = I_N \times R_N = 5 \times 2.4 = 12\text{ V}$ ✓

> [!note] 🖼️ Teorema de Norton
>
> ![[../../Anexos/ChatGPT Image 17 jun 2026, 00_16_27.png]]
> 
> **Se lee así:** Infografía doble lado a lado de **Thévenin y Norton**: en cada mitad se muestra el enunciado (red lineal de dos terminales → fuente de voltaje con $R_{Th}$ en serie, o fuente de corriente con $R_N$ en paralelo), cómo obtener los parámetros ($V_{Th} = V_{AB}$ en abierto y $R_{Th} = R_{AB}$ con fuentes desactivadas; $I_N = I_{sc}$ en corto y $R_N = R_{AB}$), la conexión con la carga $R_L$ y un ejemplo numérico rápido con el mismo circuito ($12\text{ V}$, $4\ \Omega$, $6\ \Omega$ → $V_{Th} = 7.2\text{ V}$, $R_{Th} = R_N = 2.4\ \Omega$; Norton: $I_N = 3\text{ A}$).
> 
> **Por qué importa:** Ver ambos equivalentes del mismo circuito hace visible que son intercambiables ($V_{Th} = I_N \cdot R_N$) y que elegir uno u otro es cuestión de conveniencia. Evita el error de recalcular todo desde cero cuando basta con transformar de un equivalente al otro.

---

## 🔁 Transformación de Fuentes

> [!note]- 🔁 Convertir entre fuente de voltaje y fuente de corriente
> 
> La **transformación de fuentes** es una técnica que permite intercambiar una fuente de voltaje con su resistencia en serie por una fuente de corriente con su resistencia en paralelo (y viceversa), manteniendo el comportamiento externo idéntico.
> 
> Es la base práctica de la relación Thévenin-Norton.
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_07.svg]]
> 
> ### ⚙️ Fórmulas de transformación
> 
> |De → A|Fórmula|Resistencia|
> |---|---|---|
> |Voltaje → Corriente|$I_s = \dfrac{V_s}{R_s}$|$R_s$ pasa de serie a **paralelo**|
> |Corriente → Voltaje|$V_s = I_s \cdot R_s$|$R_s$ pasa de paralelo a **serie**|
> 
> > ⚠️ La transformación aplica solo a **fuentes independientes**. Las fuentes dependientes no pueden transformarse de esta manera sin modificar las variables de control.
> 
> ### 🧮 Ejemplo resuelto
> 
> > Fuente de voltaje: $V_s = 20\text{ V}$, $R_s = 5\ \Omega$ en serie.
> > 
> > Equivalente Norton: $$I_s = \frac{20}{5} = 4\text{ A} \qquad \text{con } R_s = 5\ \Omega \text{ en paralelo}$$

> [!note] 🖼️ Transformación de Fuentes
>
> ![[../../Anexos/ChatGPT Image 17 jun 2026, 00_22_01.png]]
> 
> **Se lee así:** Infografía de la **transformación de fuentes**: presenta la equivalencia entre fuente de voltaje $V_s$ en serie con $R_s$ y fuente de corriente $I_s$ en paralelo con la misma $R_s$ ($I_s = V_s/R_s$; $V_s = I_s \cdot R_s$), con ejemplos numéricos en ambas direcciones ($12\text{ V}$/$6\ \Omega$ → $2\text{ A}$; $3\text{ A}$/$4\ \Omega$ → $12\text{ V}$), la verificación con una carga $R_L$ (mismo $V_{ab}$ en las dos configuraciones) y las condiciones de validez: fuentes ideales, resistencias lineales y equivalencia vista solo desde los terminales $a$-$b$.
> 
> **Por qué importa:** Es la herramienta práctica que convierte un equivalente Thévenin en Norton y viceversa para simplificar mallas o nodos sucesivos. Olvidar que la $R_s$ cambia de serie a paralelo (o al revés) es el error típico que rompe toda la cadena de simplificación.

---

## ⚡ Teorema de Máxima Transferencia de Potencia

> [!tip]- ⚡ ¿Cuándo la carga absorbe la máxima potencia?
> 
> El **Teorema de Máxima Transferencia de Potencia** establece la condición bajo la cual una carga $R_L$ extrae la mayor potencia posible de una red con equivalente Thévenin ($V_{Th}$, $R_{Th}$).
> 
> > _"La máxima potencia se transfiere a la carga cuando $R_L = R_{Th}$."_
> 
> $$\boxed{R_L = R_{Th}} \quad \Longrightarrow \quad P_{máx} = \frac{V_{Th}^2}{4 R_{Th}}$$
> 
> ### 📐 Deducción
> 
> La potencia entregada a $R_L$ es:
> 
> $$P_L = I_L^2 \cdot R_L = \left(\frac{V_{Th}}{R_{Th}+R_L}\right)^2 R_L$$
> 
> Para maximizar $P_L$ respecto a $R_L$, se toma $\dfrac{dP_L}{dR_L} = 0$, lo que conduce a:
> 
> $$R_L = R_{Th}$$
> 
> ### 📊 Comportamiento de la potencia en función de $R_L$
> 
> |Condición|Potencia en $R_L$|Eficiencia|
> |---|---|---|
> |$R_L \ll R_{Th}$|Baja (casi cortocircuito)|Baja|
> |$R_L = R_{Th}$|**Máxima**: $P_{máx} = \dfrac{V_{Th}^2}{4R_{Th}}$|50 %|
> |$R_L \gg R_{Th}$|Tiende a cero (casi circuito abierto)|Alta pero $P \to 0$|
> 
> > 💡 Nótese que la **eficiencia en el punto de máxima potencia es solo del 50 %**: la mitad de la potencia se disipa en $R_{Th}$. Este compromiso es aceptable en telecomunicaciones y electrónica de señal, pero no en sistemas de potencia, donde se prioriza la eficiencia.
> 
> ### 🧮 Ejemplo resuelto
> 
> > Dado el equivalente Thévenin: $V_{Th} = 12\text{ V}$, $R_{Th} = 3\ \Omega$.
> > 
> > **Condición:** $R_L = R_{Th} = 3\ \Omega$
> > 
> > $$P_{máx} = \frac{(12)^2}{4 \times 3} = \frac{144}{12} = 12\text{ W}$$
> > 
> > **Verificación:** $$I_L = \frac{12}{3+3} = 2\text{ A} \qquad P_L = (2)^2 \times 3 = 12\text{ W}\ ✓$$

> [!note] 🖼️ Teorema de Máxima Transferencia de Potencia
>
> ![[../../Anexos/ChatGPT Image 17 jun 2026, 00_25_46.png]]
> 
> **Se lee así:** Infografía del **Teorema de Máxima Transferencia de Potencia** aplicada a ambos equivalentes: con Thévenin la condición es $R_L = R_{Th}$ y $P_{L,máx} = V_{Th}^2 / 4R_{Th}$; con Norton la condición es $R_L = R_N$ y $P_{L,máx} = I_N^2 R_N / 4$. Incluye los desarrollos de $I_L$ y $P_L$ paso a paso, ejemplos numéricos en ambas modalidades ($12\text{ V}$/$6\ \Omega$ → $6\text{ W}$; $2\text{ A}$/$4\ \Omega$ → $4\text{ W}$) y recuerda que en el punto óptimo solo se transfiere el 50 % de la potencia disponible.
> 
> **Por qué importa:** Condensa la deducción de la nota en afiche y deja claro que la condición aplica a **cargas resistivas** y que $R_L \neq R_{Th}$ entrega menos potencia. Evita confundir "máxima potencia" con "máxima eficiencia", que ocurren en puntos distintos.

---

## 🗺️ Circuito Plano

> [!note]- 🗺️ Requisito previo para el método de mallas
> 
> El **método de corrientes de malla** (y su forma matricial) solo puede aplicarse a **circuitos planos**.
> 
> > _"Un circuito es plano si puede dibujarse en un plano de manera que ninguna rama pase sobre o por debajo de otra rama."_
> 
> |Tipo|Descripción|Método aplicable|
> |---|---|---|
> |**Circuito plano**|Se puede redibujar sin cruces de ramas|Mallas ✅|
> |**Circuito no plano**|Alguna rama inevitablemente cruza otra|Solo nodos ✅|
> 
> > 💡 La mayoría de circuitos en cursos introductorios son planos. Si un circuito parece tener cruces, intenta redibujarlo antes de concluir que es no plano.

---

## 🧮 Métodos Directos Matriciales — Mallas y Nodos

> [!tip]- 🧮 Construir el sistema de ecuaciones directamente por inspección
> 
> Los **métodos directos** permiten armar el sistema de ecuaciones completo sin escribir KVL o KCL en cada paso. La estructura del circuito dicta directamente los valores de cada entrada de la matriz.
> 
> ---
> 
> ### 📐 Método directo: Mallas → $[R]\cdot[I] = [V]$
> 
> Para $n$ mallas independientes en un circuito plano:
> 
> **Lado derecho — vector $[V]$:**
> 
> Para la malla $k$: suma algebraica de las fuentes de voltaje (independientes o controladas) conectadas a esa malla.
> 
> - Signo **positivo** si la corriente de malla la atraviesa de $-$ a $+$.
> - Signo **negativo** si la atraviesa de $+$ a $-$.
> 
> **Lado izquierdo — matriz $[R]$:**
> 
> |Entrada|Regla|Signo|
> |---|---|---|
> |**Término propio** $R_{kk}$|Corriente de malla $k$ × suma de **todas** las resistencias de la malla $k$|**Positivo**|
> |**Término mutuo** $R_{kj}$|Corriente de malla $j$ × resistencias **compartidas** entre malla $k$ y malla $j$|**Negativo** (corrientes opuestas)|
> 
> **Ejercicio de la Sesión 5 — dos mallas:**
> 
> > Circuito con $V_1$, $V_2$, $R_1$, $R_2$, $R_3$ (compartida entre mallas), $R_4$, $R_5$. Corrientes $I_1$ (malla izq.) e $I_2$ (malla der.).
> > 
> > Por inspección directa:
> > 
> > $$\begin{bmatrix} R_1+R_2+R_3 & -R_3 \ -R_3 & R_3+R_4+R_5 \end{bmatrix} \begin{bmatrix} I_1 \ I_2 \end{bmatrix} = \begin{bmatrix} V_1 \ -V_2 \end{bmatrix}$$
> > 
> > - $R_{11} = R_1 + R_2 + R_3$ → suma de todas las resistencias de la malla 1.
> > - $R_{22} = R_3 + R_4 + R_5$ → suma de todas las resistencias de la malla 2.
> > - $R_{12} = R_{21} = -R_3$ → resistencia compartida, signo negativo.
> > - $V_1$ positivo porque $I_1$ entra por el terminal $-$ de $V_1$.
> > - $-V_2$ porque $I_2$ entra por el terminal $+$ de $V_2$.
> 
> ---
> 
> ### 📐 Método directo: Nodos → $[G]\cdot[V] = [I_f]$
> 
> Para $n$ nodos principales (el sistema tiene $n-1$ ecuaciones, excluyendo el nodo de referencia tierra):
> 
> **Variables:** tensiones de nodo $V_1, V_2, \ldots$ referidas a tierra ($V=0$).
> 
> **Elementos pasivos expresados como conductancias** $G = 1/R$ [Siemens].
> 
> **Lado derecho — vector $[I_f]$:**
> 
> Para el nodo $k$: suma algebraica de las fuentes de corriente (independientes o controladas) conectadas a ese nodo.
> 
> - Signo **positivo** si la fuente se dirige **hacia** el nodo.
> - Signo **negativo** si se aleja del nodo.
> 
> **Lado izquierdo — matriz $[G]$:**
> 
> |Entrada|Regla|Signo|
> |---|---|---|
> |**Término propio** $G_{kk}$|Tensión $V_k$ × suma de **todas** las conductancias conectadas al nodo $k$|**Positivo**|
> |**Término mutuo** $G_{kj}$|Tensión $V_j$ × conductancias del ramal que une **directamente** el nodo $k$ con el nodo $j$|**Negativo**|
> 
> > 📌 **Propiedad importante:** la matriz $G$ es **simétrica respecto a la diagonal principal** ($G_{kj} = G_{jk}$) siempre que el circuito contenga únicamente fuentes de corriente independientes. Con fuentes dependientes esto puede no cumplirse.
> 
> **Ejercicio de la Sesión 5 — dos nodos:**
> 
> > Circuito: fuente $I_a$ (↑), $G_1$ y $G_2$ entre nodos, $I_b$ (↓), $G_3$. Nodo de referencia en tierra.
> > 
> > Por inspección directa:
> > 
> > $$\begin{bmatrix} G_1 + G_2 & -G_2 \ -G_2 & G_2 + G_3 \end{bmatrix} \begin{bmatrix} V_1 \ V_2 \end{bmatrix} = \begin{bmatrix} I_a \ -I_b \end{bmatrix}$$
> > 
> > - $G_{11} = G_1 + G_2$ → suma de conductancias conectadas al nodo 1.
> > - $G_{22} = G_2 + G_3$ → suma de conductancias conectadas al nodo 2.
> > - $G_{12} = G_{21} = -G_2$ → conductancia compartida, signo negativo.
> > - $I_a$ positivo (entra al nodo 1). $-I_b$ negativo (sale del nodo 2).
> > 
> > ✅ Verificar simetría: $G_{12} = G_{21} = -G_2$ ✓ (solo fuentes independientes).
> 
> ### ⚡ Regla mnemotécnica — mismo patrón para mallas y nodos
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_08.svg]]
> 
> **Se lee así:** Diagrama de la **regla mnemotécnica** para el método directo: la diagonal principal (término propio) es la suma de las $R$ o $G$ propias del nodo/malla y lleva **signo positivo**; los términos fuera de la diagonal (mutuos) son la $R$ o $G$ compartida entre nodos/mallas y llevan **signo negativo**; y el vector de fuentes toma su signo según el sentido de recorrido de la malla o de inyección en el nodo.
> 
> **Por qué importa:** Es el atajo que permite armar $[R]\cdot[I]=[V]$ o $[G]\cdot[V]=[I]$ sin escribir KVL/KCL. Recordar "diagonal suma propia → positivo, compartido → negativo" elimina los errores de signo más frecuentes en el examen.

> [!note] 🖼️ Métodos Directos Matriciales — Mallas y Nodos
>
> ![[../../Anexos/ChatGPT Image 17 jun 2026, 00_30_37.png]]
> 
> **Se lee así:** Infografía comparativa de los **métodos directos matriciales**: a la izquierda el método de mallas ($[Z]\{I_m\} = \{V_m\}$, corrientes en sentido horario) con la construcción de la matriz de impedancias, el vector de fuentes y un ejemplo numérico ($R_1 = 4\ \Omega$, $R_2 = 2\ \Omega$, $R_3 = 6\ \Omega$, $R_4 = 3\ \Omega$, $V_{s1} = 12\text{ V}$, $V_{s2} = 6\text{ V}$ → $I_1 = 1.2\text{ A}$, $I_2 = -0.6\text{ A}$); a la derecha el método de nodos ($[G]\{V_n\} = \{I_n\}$, tensiones respecto a tierra) con su ejemplo numérico equivalente. Incluye procedimientos paso a paso, ventajas de cada método y las convenciones de color (voltaje/malla vs. corriente/nodo).
> 
> **Por qué importa:** Muestra que ambos métodos producen los mismos resultados y que la elección depende de la topología y de las fuentes presentes. Evita mezclar convenciones (mallas en una sección, nodos en otra) dentro del mismo desarrollo.

---

## ⚖️ Comparación General de Teoremas

> [!success]- 📊 Resumen comparativo
> 
> |Teorema|Modelo equivalente|Condición|Ventaja principal|
> |---|---|---|---|
> |**Superposición**|Sin reducción|Múltiples fuentes|Analiza cada fuente por separado|
> |**Thévenin**|$V_{Th}$ + $R_{Th}$ en serie|Red lineal|Simplifica el análisis de la carga|
> |**Norton**|$I_N$ + $R_N$ en paralelo|Red lineal|Dual de Thévenin, útil con cargas en paralelo|
> |**Transf. de fuentes**|Intercambia Vs ↔ Is|Fuente + resistencia|Simplifica nodos o mallas sucesivos|
> |**Máx. transferencia**|$R_L = R_{Th}$|Red Thévenin conocida|Optimiza la potencia entregada|
> 
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_09.svg]]
> 
> **Se lee así:** Diagrama de decisión que parte de "¿qué se busca?" ante un circuito complejo: si es la respuesta ante varias fuentes, lleva a **Superposición**; si es simplificar la red para la carga, pregunta por el tipo de equivalente y lleva a **Thévenin** (voltaje + serie) o **Norton** (corriente + paralelo), conectados entre sí por la **transformación de fuentes**; y si es optimizar la potencia entregada, lleva a **Máxima transferencia de potencia**.
> 
> **Por qué importa:** Es el mapa mental de elección de teorema: primero identifica qué pide el problema y la topología, después aplica la herramienta. Evita lanzar KVL/KCL completos cuando un teorema resuelve el circuito en dos líneas.

---

## 📊 Resumen Visual

> [!note] 🖼️ Resumen Visual
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/06_-_Teoremas_de_Analisis_de_Circuitos_10.svg]]
> 
> **Se lee así:** Mapa mental de **Teoremas de Circuitos** con siete ramas: Superposición (una fuente a la vez, apagar fuentes, sumar respuestas, solo cantidades lineales), Divisores (voltaje → serie, corriente → paralelo), Thévenin ($V_{Th} = V_{oc}$, $R_{Th} = R_{eq}$ sin fuentes, serie con la carga, Thévenin 1883), Norton ($I_N = I_{sc}$, $R_N = R_{Th}$, paralelo con la carga, dual de Thévenin), Transformación ($V_s/R_s \leftrightarrow I_s \cdot R_s$, serie ↔ paralelo), Máxima transferencia ($R_L = R_{Th}$, $P_{máx} = V_{Th}^2/4R_{Th}$, eficiencia 50 %) y Métodos matriciales ($R \cdot I = V$, $G \cdot V = I_f$, propio positivo / mutuo negativo, $G$ simétrica con fuentes independientes, circuito plano para mallas).
> 
> **Por qué importa:** Condensa toda la unidad en una sola página: es el repaso ideal antes del examen y la referencia rápida para decidir qué teorema aplica. Si una rama del mapa no se entiende, ahí mismo señala qué sección de la nota hay que releer.

---

## 📚 Referencias

> [!quote]- 📖 Fuentes consultadas
> 
> [1] C. K. Alexander y M. N. O. Sadiku, _Fundamentals of Electric Circuits_, 6th ed. New York, USA: McGraw-Hill, 2016, pp. 139–200.
> 
> [2] R. L. Boylestad, _Introductory Circuit Analysis_, 13th ed. Hoboken, NJ, USA: Pearson, 2016, pp. 340–430.
> 
> [3] A. R. Hambley, _Electrical Engineering: Principles and Applications_, 7th ed. Hoboken, NJ, USA: Pearson, 2018, pp. 91–160.
> 
> [4] J. W. Nilsson y S. A. Riedel, _Electric Circuits_, 11th ed. Hoboken, NJ, USA: Pearson, 2019, pp. 138–210.
> 
> [5] A. Hermosa Donante, _Electrónica Aplicada_, 1.ª ed. Mexico: Alfaomega Grupo Editor, 2013, pp. 76–130. ISBN-13: 9786077074045.

## ✅ Metas de Aprendizaje
> [!note] Nivel Basico
>
> - [ ] Enuncio superposicion, Thevenin (Vth+Rth), Norton (IN+RN) y maxima transferencia.
> - [ ] Explico como apagar una fuente (voltaje->corto, corriente->abierto).
> - [ ] Aplico divisor de voltaje y de corriente como atajo.
>

> [!note] Nivel Intermedio
>
> - [ ] Calculo Vth (circuito abierto) y Rth y hallo IL=Vth/(Rth+RL).
> - [ ] Convierto Thevenin<->Norton con Vth=IN·RN.
> - [ ] Determino RL para Pmax y calculo Pmax=Vth2/(4Rth).
>

> [!note] Nivel Avanzado
>
> - [ ] Resuelvo red con 2 fuentes por superposicion sumando respuestas parciales.
> - [ ] Armo matriz R·I=V y G·V=If por inspeccion.
> - [ ] Decido teorema optimo segun lo que se pide y topologia.
>

---

## 🔗 Conexiones

> [!quote] 🔗 Conexiones
>
> - Previo: [[05 - Leyes de Ohm y Kirchhoff]] — base para Thevenin/Norton y mallas/nodos
> - Siguiente: [[04 - Circuitos de Filtrado y Fuentes Lineales]] — Thevenin aplicado a fuentes
> - Adelante: [[02 - Aplicaciones de los OPAMs - Minimización de Ruido]] — donde Thevenin reaparece con OPAMs

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Mapa de contenido: [[../../Fundamentos de Electricidad y Sistemas Digitales|⚡ Mapa de contenido]]
> - Índice de la materia: [[../../Índice de Contenido|Índice de Contenido]]
> - Siguiente: [[01 - Semiconductores y Bandas de Energía]]
> - Syllabus: [[../../Bienvenida y Syllabus Fundamentos de Electricidad y Sistemas Digitales|👋 Bienvenida y Syllabus]]

**Tags:** #teoremas #superposición #thévenin #norton #transformación #potencia #divisorVoltaje #divisorCorriente #mallas #nodos #matricial #circuitoPlano #circuitos #análisis #EYAG1037 #FESD #ESPOL #unidad1
