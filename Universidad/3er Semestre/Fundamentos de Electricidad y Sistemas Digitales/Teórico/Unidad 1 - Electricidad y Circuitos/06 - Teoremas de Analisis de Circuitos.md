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
> ```mermaid
> graph TD
>     A[Teoremas de Circuitos] --> B[Superposición]
>     A --> C[Thévenin]
>     A --> D[Norton]
>     A --> E[Máxima Transferencia<br/>de Potencia]
>     A --> F[Transformación<br/>de Fuentes]
> 
>     B --> B1[Una fuente<br/>a la vez]
>     C --> C1[Equivalente<br/>Vs + Rs]
>     D --> D1[Equivalente<br/>Is + Rp]
>     E --> E1[RL = RTh<br/>Pmáx]
>     F --> F1[Voltaje ↔ Corriente]
> 
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
>     style E fill:#f5e1ff
>     style F fill:#ffe1e1
> ```
> 
> |Teorema|Utilidad principal|
> |---|---|
> |**Superposición**|Circuitos con múltiples fuentes independientes|
> |**Thévenin**|Simplificar una red para analizar el elemento de carga|
> |**Norton**|Alternativa corriente al equivalente Thévenin|
> |**Máx. transferencia**|Encontrar $R_L$ que maximiza potencia entregada|
> |**Transformación de fuentes**|Convertir entre fuente de voltaje y corriente|

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
> ```mermaid
> graph TD
>     P1[1️⃣ Identificar todas las<br/>fuentes independientes] --> P2
>     P2[2️⃣ Dejar activa UNA fuente;<br/>apagar las demás] --> P3
>     P3[3️⃣ Calcular la respuesta<br/>parcial con esa fuente] --> P4
>     P4[4️⃣ Repetir para cada<br/>fuente restante] --> P5
>     P5[5️⃣ Sumar algebraicamente<br/>todas las respuestas parciales]
> 
>     style P1 fill:#e1f5ff
>     style P2 fill:#e1ffe1
>     style P3 fill:#fff4e1
>     style P4 fill:#e1f5ff
>     style P5 fill:#f5e1ff
> ```
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

![[ChatGPT Image 17 jun 2026, 00_07_49.png]]

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
> ```mermaid
> graph LR
>     A[Circuito simple] --> B{¿Tipo?}
>     B -->|Resistores en SERIE<br/>fuente de voltaje| C["Divisor de voltaje<br/>V_Ri = Vf·Ri / Req"]
>     B -->|Resistores en PARALELO<br/>fuente de corriente| D["Divisor de corriente<br/>I_Ri = Req·If / Rj"]
> 
>     style C fill:#e1f5ff
>     style D fill:#e1ffe1
> ```

![[ChatGPT Image 17 jun 2026, 00_10_30.png]]

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
> ```mermaid
> graph LR
>     subgraph Original["Red original compleja"]
>         F1[Fuentes y resistencias] --> A1[Terminal A]
>         F1 --> B1[Terminal B]
>     end
>     subgraph Equiv["Equivalente Thévenin"]
>         VTh["🔋 VTh"] --> RTh[RTh]
>         RTh --> A2[Terminal A]
>         VTh --> B2[Terminal B]
>     end
>     Original -->|"≡"| Equiv
> 
>     style VTh fill:#fff4e1
>     style RTh fill:#e1f5ff
> ```
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
> ```mermaid
> graph LR
>     subgraph Equiv["Equivalente Norton"]
>         IN["⬆ IN"] --> RN[RN]
>         IN --> A2[Terminal A]
>         RN --> B2[Terminal B]
>     end
> 
>     style IN fill:#fff4e1
>     style RN fill:#e1ffe1
> ```
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
> ```mermaid
> graph LR
>     A["Thévenin<br/>VTh + RTh (serie)"] <-->|"Transformación<br/>de fuentes"| B["Norton<br/>IN + RN (paralelo)"]
> 
>     style A fill:#e1f5ff
>     style B fill:#e1ffe1
> ```
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

![[ChatGPT Image 17 jun 2026, 00_16_27.png]]

---

## 🔁 Transformación de Fuentes

> [!note]- 🔁 Convertir entre fuente de voltaje y fuente de corriente
> 
> La **transformación de fuentes** es una técnica que permite intercambiar una fuente de voltaje con su resistencia en serie por una fuente de corriente con su resistencia en paralelo (y viceversa), manteniendo el comportamiento externo idéntico.
> 
> Es la base práctica de la relación Thévenin-Norton.
> 
> ```mermaid
> graph LR
>     subgraph V["Fuente de voltaje"]
>         Vs[🔋 Vs] --- Rs_s[Rs en serie]
>     end
>     subgraph I["Fuente de corriente"]
>         Is[⬆ Is] --- Rs_p[Rs en paralelo]
>     end
> 
>     V <-->|"Is = Vs/Rs<br/>Vs = Is·Rs"| I
> 
>     style Vs fill:#fff4e1
>     style Is fill:#e1ffe1
> ```
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

![[ChatGPT Image 17 jun 2026, 00_22_01.png]]

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

![[ChatGPT Image 17 jun 2026, 00_25_46.png]]

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
> ```mermaid
> graph TD
>     A[Diagonal principal<br/>Término PROPIO] -->|"Suma de R o G<br/>propios del nodo/malla"| B["Signo POSITIVO ✅"]
>     C[Fuera de diagonal<br/>Término MUTUO] -->|"R o G compartida<br/>entre nodos/mallas"| D["Signo NEGATIVO ❌"]
>     E[Vector de fuentes] -->|"Voltaje o corriente<br/>según sentido de recorrido"| F["Signo por convención"]
> 
>     style A fill:#e1ffe1
>     style C fill:#ffe1e1
>     style E fill:#fff4e1
> ```


![[ChatGPT Image 17 jun 2026, 00_30_37.png]]

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
> ```mermaid
> graph TD
>     A[Circuito complejo] --> B{¿Qué se busca?}
> 
>     B -->|Respuesta ante<br/>varias fuentes| C[Superposición]
>     B -->|Simplificar<br/>para la carga| D{¿Tipo de equivalente?}
>     B -->|Optimizar<br/>potencia| E[Máx. transferencia<br/>de potencia]
> 
>     D -->|Voltaje + serie| F[Thévenin]
>     D -->|Corriente + paralelo| G[Norton]
>     F <-->|Transformación| G
> 
>     style C fill:#e1f5ff
>     style F fill:#e1ffe1
>     style G fill:#fff4e1
>     style E fill:#f5e1ff
> ```

---

## 📊 Resumen Visual

```mermaid
mindmap
  root((Teoremas de<br/>Circuitos))
    Superposición
      Una fuente a la vez
      Apagar fuentes
      Sumar respuestas
      Solo cantidades lineales
    Divisores
      Voltaje → serie → Vf·Ri/Req
      Corriente → paralelo → Req·If/Rj
      Circuito simple de una malla/par de nodos
    Thévenin
      VTh = Voc
      RTh = Req sin fuentes
      Serie con carga
      Léon Thévenin 1883
    Norton
      IN = Isc
      RN = RTh
      Paralelo con carga
      Dual de Thévenin
    Transformación
      Vs/Rs ↔ Is·Rs
      Serie ↔ Paralelo
      Simplificación
    Máx. Transferencia
      RL = RTh
      Pmáx = VTh²/4RTh
      Eficiencia 50%
      Telecomunicaciones
    Métodos Matriciales
      Mallas R·I = V
      Nodos G·V = If
      Término propio positivo
      Término mutuo negativo
      G simétrica si solo fuentes independientes
      Circuito plano para mallas
```

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

---

**Tags:** #teoremas #superposición #thévenin #norton #transformación #potencia #divisorVoltaje #divisorCorriente #mallas #nodos #matricial #circuitoPlano #circuitos #análisis #EYAG1037 #FESD #ESPOL #unidad1