---
dg-publish: true
---

# 🧮 Ejercicios Recopilados — EYAG1037

> [!info] 📋 Sobre esta nota
> 
> Ejercicios de dificultad alta organizados por tema. Cada uno incluye:
> 
> - Una descripción del circuito para que puedas dibujarlo
> - Justificación de cada fórmula aplicada
> - Solución paso a paso con verificación
> 
> |S|Tema|Concepto clave|
> |---|---|---|
> |S1|Coulomb + Campo|Superposición de fuerzas vectoriales|
> |S2|Fuentes dependientes|VCCS en red con KVL|
> |S3|Ohm + Potencia|Validar diseño por disipación|
> |S4|KCL avanzado|Nodo con 4 corrientes desconocidas|
> |S5|KVL avanzado|Fuentes en oposición, signo crítico|
> |S6|Tres mallas|Sistema 3×3, rama compartida doble|
> |S7|Matricial mallas|Inspección directa 3×3 + Cramer|
> |S8|Matricial nodos|Inspección directa 3×3 conductancias|
> |S9|Fuentes mixtas|Reducción antes de plantear KVL|
> |S10|Mixto 5R|Tres etapas de simplificación|
> |S11|C y L combinados|Reducción en dos etapas|
> |S12|Divisor encadenado|Dos reducciones de paralelo + divisor|
> |S13|Divisor 3 ramas|Conductancias + verificación de potencia|
> |S14|Superposición 3 fuentes|Tres sub-circuitos independientes|
> |S15|Thévenin + dep.|Fuente de prueba para R_Th|
> |S16|Norton + MTP|Cadena completa de análisis|
> |S17|Transform. encadenada|Tres transformaciones sucesivas|

---

## 1. Ley de Coulomb + Campo Eléctrico

> [!example] ✏️ Tres cargas en línea — fuerza neta y campo en el punto central
> 
> **🖊️ Cómo se ve el circuito / diagrama:** Dibuja una línea horizontal. Coloca $q_1 = +6\,\mu\text{C}$ en el extremo izquierdo, $q_3 = -4\,\mu\text{C}$ en el extremo derecho, y un punto P en el centro exacto. La distancia entre $q_1$ y $q_3$ es $d = 0.4\,\text{m}$, así que P queda a $r = 0.2\,\text{m}$ de cada carga. Añade $q_2 = +3\,\mu\text{C}$ colocada en P.
> 
> **Dado:**
> 
> - $q_1 = +6\,\mu\text{C}$ en $x = 0$
> - $q_2 = +3\,\mu\text{C}$ en $x = 0.2\,\text{m}$ (punto P)
> - $q_3 = -4\,\mu\text{C}$ en $x = 0.4\,\text{m}$
> - $K_e = 9\times10^9\,\text{N·m}^2/\text{C}^2$
> 
> **Encontrar:** la fuerza neta sobre $q_2$ y el campo eléctrico total en P (sin $q_2$).
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $F = K_e\dfrac{\lvert q_a\rvert\lvert q_b\rvert}{r^2}$ | Calcular la magnitud de la fuerza entre cada par de cargas (Pasos 1-2) |
> | $\vec{F}_{neta} = \sum \vec{F}_i$ | Sumar vectorialmente las fuerzas individuales sobre $q_2$ (Paso 3) |
> | $E = K_e\dfrac{Q}{r^2}$ | Obtener el campo eléctrico que crea cada carga en el punto P, sin colocar ahí la carga de prueba (Paso 4) |
> | $F = q\cdot E$ | Verificar el resultado relacionando fuerza y campo (chequeo final) |
> 
> ![[ChatGPT Image 20 jun 2026, 23_16_31.png]]
> 
> ---
> 
> **¿Por qué usamos Coulomb vectorialmente?** Cuando hay más de dos cargas, la fuerza sobre una carga es la **suma vectorial** de todas las fuerzas individuales. Cada par de cargas sigue $F = K_e\frac{|q_a||q_b|}{r^2}$, y el signo de la dirección lo da la regla: igual signo → repulsión (se alejan), signo opuesto → atracción (se acercan).
> 
> **Paso 1 — Fuerza de $q_1$ sobre $q_2$ ($F_{12}$):**
> 
> $q_1$ y $q_2$ tienen el mismo signo (+), por lo tanto la fuerza sobre $q_2$ apunta **hacia la derecha** (+x).
> 
> $$F_{12} = K_e\frac{|q_1||q_2|}{r_{12}^2} = 9\times10^9 \cdot \frac{(6\times10^{-6})(3\times10^{-6})}{(0.2)^2} = 9\times10^9 \cdot \frac{18\times10^{-12}}{0.04} = 4.05\,\text{N} \quad (+x)$$
> 
> **Paso 2 — Fuerza de $q_3$ sobre $q_2$ ($F_{32}$):**
> 
> $q_3$ es negativa y $q_2$ es positiva → atracción → la fuerza sobre $q_2$ apunta **hacia la derecha** (+x) también (hacia $q_3$).
> 
> $$F_{32} = K_e\frac{|q_3||q_2|}{r_{32}^2} = 9\times10^9 \cdot \frac{(4\times10^{-6})(3\times10^{-6})}{(0.2)^2} = 9\times10^9 \cdot \frac{12\times10^{-12}}{0.04} = 2.7\,\text{N} \quad (+x)$$
> 
> **Paso 3 — Fuerza neta sobre $q_2$:**
> 
> Ambas fuerzas apuntan en la misma dirección, se suman directamente.
> 
> $$\boxed{F_{neta} = F_{12} + F_{32} = 4.05 + 2.7 = 6.75\,\text{N} \quad (+x)}$$
> 
> **Paso 4 — Campo eléctrico en P (sin $q_2$):**
> 
> El campo $E$ en un punto es la fuerza por unidad de carga de prueba positiva. Se calcula ignorando $q_2$ y evaluando la contribución de $q_1$ y $q_3$.
> 
> $$E = \frac{F}{q_{prueba}} = K_e\frac{Q}{r^2}$$
> 
> $E$ de $q_1$ en P → apunta hacia +x (carga positiva, campo sale de ella): $$E_1 = 9\times10^9 \cdot \frac{6\times10^{-6}}{(0.2)^2} = 1{,}350{,}000\,\text{V/m} = 1.35\,\text{MV/m} \quad (+x)$$
> 
> $E$ de $q_3$ en P → $q_3$ es negativa, el campo apunta **hacia** $q_3$, es decir hacia +x: $$E_3 = 9\times10^9 \cdot \frac{4\times10^{-6}}{(0.2)^2} = 900{,}000\,\text{V/m} = 0.9\,\text{MV/m} \quad (+x)$$
> 
> $$\boxed{E_{total} = 1.35 + 0.9 = 2.25\,\text{MV/m} \quad (+x)}$$
> 
> ✅ Consistencia: $F_{neta} = q_2 \cdot E_{total} = 3\times10^{-6} \times 2.25\times10^6 = 6.75\,\text{N}$ ✓

---

## 2. Fuentes Dependientes en Circuito Resistivo

> [!example] ✏️ Red con CCCS — encontrar voltaje de salida
> 
> **🖊️ Cómo se ve el circuito:** Dibuja una malla izquierda: fuente de voltaje $V_s = 20\,\text{V}$ en serie con $R_1 = 4\,\Omega$ y $R_2 = 6\,\Omega$. La corriente que circula por $R_1$ se llama $I_x$. Entre los nodos superior e inferior del lado derecho conecta una fuente de corriente dependiente tipo CCCS con valor $3I_x$ (dibújala como un rombo ◇ con flecha). En paralelo con esa fuente dependiente conecta $R_3 = 10\,\Omega$. Eso forma la malla derecha.
> 
> **Dado:**
> 
> - $V_s = 20\,\text{V}$, $R_1 = 4\,\Omega$, $R_2 = 6\,\Omega$, $R_3 = 10\,\Omega$
> - Fuente dependiente CCCS: $I_{dep} = 3I_x$ donde $I_x$ es la corriente a través de $R_1$
> 
> **Encontrar:** $I_x$, $V_{R3}$ y la potencia entregada por la fuente dependiente.
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | KVL: $\sum V = 0$ | Plantear la malla izquierda para hallar $I_x$, la variable controladora (Paso 1) |
> | $I_{dep} = 3I_x$ | Relación de la fuente dependiente; se evalúa **después** de conocer $I_x$, nunca antes (Paso 2) |
> | $V = I \times R$ (Ohm) | Obtener $V_{R3}$ una vez que toda la corriente de la fuente dependiente se conoce (Paso 3) |
> | $P = V \times I$ | Calcular la potencia entregada por la fuente dependiente (Paso 4) |
> 
> ![[ChatGPT Image 20 jun 2026, 23_19_46.png]]
> 
> ---
> 
> **¿Por qué la fuente dependiente no se apaga?** Las fuentes dependientes (controladas) no son fuentes de energía autónomas — su valor depende de una variable del circuito. Apagarlas alteraría esa variable y rompería el modelo. Solo se apagan las **independientes**.
> 
> **Paso 1 — Identificar $I_x$ con KVL en la malla izquierda:**
> 
> La malla izquierda contiene $V_s$, $R_1$ y $R_2$ en serie (la fuente dependiente está en la rama derecha, no comparte elementos con esta malla).
> 
> $$+20 - 4I_x - 6I_x = 0 \implies 20 = 10I_x \implies \boxed{I_x = 2\,\text{A}}$$
> 
> **Paso 2 — Calcular la corriente de la fuente dependiente:**
> 
> $$I_{dep} = 3I_x = 3 \times 2 = 6\,\text{A}$$
> 
> **Paso 3 — Voltaje en $R_3$ con KCL en el nodo superior:**
> 
> Toda la corriente de la fuente dependiente fluye por $R_3$ (es el único elemento en paralelo con ella):
> 
> $$V_{R3} = I_{dep} \times R_3 = 6 \times 10 = \boxed{60\,\text{V}}$$
> 
> **Paso 4 — Potencia de la fuente dependiente:**
> 
> La fuente dependiente tiene $V_{R3} = 60\,\text{V}$ en sus terminales y entrega $6\,\text{A}$:
> 
> $$P_{dep} = V_{R3} \times I_{dep} = 60 \times 6 = \boxed{360\,\text{W}}$$
> 
> ✅ Verificación — balance de potencia: $P_{Vs} = 20 \times 2 = 40\,\text{W}$ (entregada) $P_{R1} = (2)^2 \times 4 = 16\,\text{W}$, $P_{R2} = (2)^2 \times 6 = 24\,\text{W}$, $P_{R3} = 60^2/10 = 360\,\text{W}$ Total disipado: $16 + 24 + 360 = 400\,\text{W}$ = $40 + 360$ (fuentes) ✓

---

## 3. Ley de Ohm + Potencia

> [!example] ✏️ Diseño con restricción de disipación máxima
> 
> **🖊️ Cómo se ve el circuito:** Dibuja una fuente de voltaje $V_s$ (valor a determinar) conectada a tres resistencias en serie: $R_1 = 100\,\Omega/2\,\text{W}$, $R_2 = 150\,\Omega/1\,\text{W}$, $R_3 = 50\,\Omega/0.5\,\text{W}$. Cada resistencia tiene anotada su potencia máxima admisible.
> 
> **Dado:**
> 
> - $R_1 = 100\,\Omega$ (potencia máxima $P_{1,max} = 2\,\text{W}$)
> - $R_2 = 150\,\Omega$ (potencia máxima $P_{2,max} = 1\,\text{W}$)
> - $R_3 = 50\,\Omega$ (potencia máxima $P_{3,max} = 0.5\,\text{W}$)
> 
> **Encontrar:** el voltaje máximo $V_s$ que puede aplicarse sin dañar ninguna resistencia, y verificar cuál es el elemento limitante.
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $I_{max} = \sqrt{P_{max}/R}$ | Despejada de $P=I^2R$, da la corriente máxima que tolera cada resistencia (Paso 1) |
> | $I_{max,circuito} = \min(I_{1,max}, I_{2,max}, I_{3,max})$ | En serie la corriente es única, así que manda la resistencia más restrictiva (Paso 2) |
> | $R_{eq} = R_1+R_2+R_3$ (serie) | Reducir el circuito a una sola resistencia equivalente (Paso 3) |
> | $V = I \times R$ (Ohm) | Obtener el voltaje máximo aplicable con la corriente límite y $R_{eq}$ (Paso 3) |
> | $P = I^2 R$ | Verificar que ninguna resistencia exceda su potencia máxima (Paso 4) |
> 
> ![[ChatGPT Image 20 jun 2026, 23_21_32.png]]
> 
> ---
> 
> **¿Por qué usar $P = I^2 R$ y no $P = V^2/R$?** En un circuito serie la corriente $I$ es la misma en todos los elementos — es la incógnita natural. Expresar la potencia como $P = I^2 R$ permite calcular la corriente máxima que cada resistencia tolera directamente, sin necesidad de conocer el voltaje individual primero.
> 
> **Paso 1 — Corriente máxima que tolera cada resistencia:**
> 
> Despejando $I$ de $P = I^2 R$:
> 
> $$I_{max} = \sqrt{\frac{P_{max}}{R}}$$
> 
> $$I_{1,max} = \sqrt{\frac{2}{100}} = \sqrt{0.02} = 0.1414\,\text{A}$$
> 
> $$I_{2,max} = \sqrt{\frac{1}{150}} = \sqrt{0.00\overline{6}} = 0.0816\,\text{A}$$
> 
> $$I_{3,max} = \sqrt{\frac{0.5}{50}} = \sqrt{0.01} = 0.1\,\text{A}$$
> 
> **Paso 2 — Identificar el elemento limitante:**
> 
> En serie, la corriente es la misma para todas. El circuito falla cuando la primera resistencia alcanza su límite:
> 
> $$I_{max,circuito} = \min(0.1414,; 0.0816,; 0.1) = 0.0816\,\text{A} \quad \leftarrow R_2 \text{ es el cuello de botella}$$
> 
> **Paso 3 — Voltaje máximo aplicable:**
> 
> $$R_{eq} = 100 + 150 + 50 = 300\,\Omega$$
> 
> $$\boxed{V_{s,max} = I_{max} \times R_{eq} = 0.0816 \times 300 \approx 24.5\,\text{V}}$$
> 
> **Paso 4 — Verificar potencias con $I = 0.0816\,\text{A}$:**
> 
> $$P_1 = (0.0816)^2 \times 100 = 0.666\,\text{W} < 2\,\text{W} \quad ✓$$ $$P_2 = (0.0816)^2 \times 150 = 0.999\,\text{W} \approx 1\,\text{W} \quad ✓ \text{ (al límite)}$$ $$P_3 = (0.0816)^2 \times 50 = 0.333\,\text{W} < 0.5\,\text{W} \quad ✓$$

---

## 4. KCL — Nodo con Cuatro Ramas

> [!example] ✏️ Dos nodos desconocidos con fuente de corriente compartida
> 
> **🖊️ Cómo se ve el circuito:** Dibuja tres nodos en fila: tierra (izquierda), nodo A (centro), nodo B (derecha). Entre tierra y nodo A: $R_1 = 8\,\Omega$ (corriente $I_{R1}$ hacia arriba) y fuente de corriente $I_s = 5\,\text{A}$ apuntando hacia el nodo A. Entre nodo A y nodo B: $R_2 = 4\,\Omega$. Entre nodo B y tierra: $R_3 = 6\,\Omega$ y $R_4 = 12\,\Omega$ en paralelo. Una fuente de corriente $I_s2 = 2\,\text{A}$ sale del nodo B hacia tierra.
> 
> **Dado:**
> 
> - $I_{s1} = 5\,\text{A}$ (entra al nodo A desde tierra)
> - $I_{s2} = 2\,\text{A}$ (sale del nodo B hacia tierra)
> - $R_1 = 8\,\Omega$, $R_2 = 4\,\Omega$, $R_3 = 6\,\Omega$, $R_4 = 12\,\Omega$
> 
> **Encontrar:** $V_A$, $V_B$ y todas las corrientes de rama.
> 
> ![[ChatGPT Image 21 jun 2026, 00_52_30.png]]
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $R_{paralelo} = \dfrac{R_a R_b}{R_a+R_b}$ | Simplificar $R_3 \| R_4$ antes de plantear KCL (Paso 1) |
> | KCL: $\sum I_{entran} = \sum I_{salen}$ | Plantear una ecuación por cada nodo desconocido (Pasos 2-3) |
> | $I = \dfrac{\Delta V}{R}$ | Expresar cada corriente de rama en función de las tensiones de nodo $V_A$, $V_B$ (Pasos 2-3) |
> | Sistema de ecuaciones 2×2 | Resolver simultáneamente las dos ecuaciones de nodo (Paso 4) |
> 
> 
> 
> ---
> 
> **¿Por qué aplicar tensiones de nodo y no KCL directo?** Con dos nodos desconocidos, escribir las corrientes en función de $V_A$ y $V_B$ (usando $I = \Delta V / R$) genera automáticamente un sistema de dos ecuaciones. Si en cambio nombramos corrientes individuales, necesitaríamos más ecuaciones y más incógnitas.
> 
> **Paso 1 — Reducir el paralelo $R_3 | R_4$ para simplificar:**
> 
> $$R_{34} = \frac{6 \times 12}{6 + 12} = \frac{72}{18} = 4\,\Omega$$
> 
> **Paso 2 — KCL en el nodo A** (corrientes que salen = corrientes que entran):
> 
> $$I_{s1} = \frac{V_A}{R_1} + \frac{V_A - V_B}{R_2}$$
> 
> $$5 = \frac{V_A}{8} + \frac{V_A - V_B}{4} \implies 5 = \frac{V_A}{8} + \frac{2(V_A - V_B)}{8} = \frac{3V_A - 2V_B}{8}$$
> 
> $$\boxed{3V_A - 2V_B = 40 \quad (1)}$$
> 
> **Paso 3 — KCL en el nodo B:**
> 
> $$\frac{V_A - V_B}{R_2} = \frac{V_B}{R_3} + \frac{V_B}{R_4} + I_{s2}$$
> 
> $$\frac{V_A - V_B}{4} = \frac{V_B}{6} + \frac{V_B}{12} + 2$$
> 
> Lado derecho: $\dfrac{V_B}{6} + \dfrac{V_B}{12} = \dfrac{2V_B + V_B}{12} = \dfrac{3V_B}{12} = \dfrac{V_B}{4}$
> 
> $$\frac{V_A - V_B}{4} = \frac{V_B}{4} + 2 \implies V_A - V_B = V_B + 8$$
> 
> $$\boxed{V_A - 2V_B = 8 \quad (2)}$$
> 
> **Paso 4 — Resolver el sistema:**
> 
> De (2): $V_A = 2V_B + 8$. Sustituir en (1):
> 
> $$3(2V_B + 8) - 2V_B = 40 \implies 6V_B + 24 - 2V_B = 40 \implies 4V_B = 16$$
> 
> $$\boxed{V_B = 4\,\text{V}} \qquad \boxed{V_A = 2(4) + 8 = 16\,\text{V}}$$
> 
> **Paso 5 — Corrientes de rama:**
> 
> $$I_{R1} = \frac{V_A}{R_1} = \frac{16}{8} = 2\,\text{A} \qquad I_{R2} = \frac{V_A - V_B}{R_2} = \frac{16-4}{4} = 3\,\text{A}$$ $$I_{R3} = \frac{V_B}{R_3} = \frac{4}{6} = 0.667\,\text{A} \qquad I_{R4} = \frac{V_B}{R_4} = \frac{4}{12} = 0.333\,\text{A}$$
> 
> ✅ Verificación KCL en nodo A: $5 = 2 + 3$ ✓ ✅ Verificación KCL en nodo B: $3 = 0.667 + 0.333 + 2$ ✓

---

## 5. KVL — Malla con Dos Fuentes Opuestas

> [!example] ✏️ Tres fuentes en una sola malla — signo crítico
> 
> **🖊️ Cómo se ve el circuito:** Dibuja una malla rectangular cerrada. En el lado superior izquierdo coloca $V_{s1} = 24\,\text{V}$ con el polo + hacia arriba. En el lado superior derecho coloca $V_{s2} = 8\,\text{V}$ con el polo + hacia abajo (opuesta). En el lado inferior coloca $V_{s3} = 4\,\text{V}$ con el polo + hacia la derecha. Las resistencias son: $R_1 = 3\,\Omega$ (lado izquierdo), $R_2 = 5\,\Omega$ (lado derecho), $R_3 = 2\,\Omega$ (lado inferior). La corriente de malla $I$ circula en sentido horario.
> 
> **Dado:**
> 
> - $V_{s1} = 24\,\text{V}$ (polo + en dirección del recorrido horario: suma)
> - $V_{s2} = 8\,\text{V}$ (polo + contra el recorrido horario: resta)
> - $V_{s3} = 4\,\text{V}$ (polo + en dirección del recorrido: suma)
> - $R_1 = 3\,\Omega$, $R_2 = 5\,\Omega$, $R_3 = 2\,\Omega$
> 
> **Encontrar:** $I$, la potencia de cada fuente (¿entrega o absorbe?) y verificar balance.
> 
> ![[ChatGPT Image 20 jun 2026, 23_32_40.png]]
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | KVL: $\sum V = 0$ alrededor de la malla | Encontrar $I$, asignando signo según si el recorrido entra por − o + de cada fuente (Paso 1) |
> | $P = V \times I$ | Calcular la potencia de cada fuente; el signo indica si entrega o absorbe (Paso 2) |
> | $P = I^2 R$ | Calcular la potencia disipada en cada resistencia (Paso 2) |
> | Balance de potencia: $\sum P_{entregada} = \sum P_{absorbida}$ | Verificar que el resultado sea físicamente consistente |
> 
> 
> ---
> 
> **¿Por qué el signo de las fuentes en KVL es tan crítico?** El signo no viene del valor de la fuente sino de cómo la **atraviesa** la corriente de recorrido. Si la corriente entra por el terminal negativo (−) y sale por el positivo (+), la fuente **entrega energía** al circuito: contribución positiva a KVL. Si entra por el (+), la fuente **absorbe energía**: contribución negativa.
> 
> **Paso 1 — KVL en sentido horario** (de − a + es +, caída en R es −):
> 
> $$+V_{s1} - V_{s2} + V_{s3} - R_1 I - R_2 I - R_3 I = 0$$
> 
> $$24 - 8 + 4 = (3 + 5 + 2)I$$
> 
> $$20 = 10I \implies \boxed{I = 2\,\text{A}}$$
> 
> **Paso 2 — Potencia de cada elemento:**
> 
> |Elemento|Rol|Cálculo|Resultado|
> |---|---|---|---|
> |$V_{s1} = 24\,\text{V}$|Corriente entra por − → **entrega**|$P = 24 \times 2$|$+48\,\text{W}$|
> |$V_{s2} = 8\,\text{V}$|Corriente entra por + → **absorbe**|$P = 8 \times 2$|$-16\,\text{W}$|
> |$V_{s3} = 4\,\text{V}$|Corriente entra por − → **entrega**|$P = 4 \times 2$|$+8\,\text{W}$|
> |$R_1$|Disipa|$P = (2)^2 \times 3$|$12\,\text{W}$|
> |$R_2$|Disipa|$P = (2)^2 \times 5$|$20\,\text{W}$|
> |$R_3$|Disipa|$P = (2)^2 \times 2$|$8\,\text{W}$|
> 
> ✅ Balance: entregado $= 48 + 8 = 56\,\text{W}$; absorbido $= 16 + 12 + 20 + 8 = 56\,\text{W}$ ✓

---

## 6. Análisis de Tres Mallas

> [!example] ✏️ Tres mallas con dos ramas compartidas
> 
> **🖊️ Cómo se ve el circuito:** Dibuja tres mallas rectangulares en fila horizontal. Malla 1 (izquierda): $V_{s1} = 30\,\text{V}$ en el lado izquierdo, $R_1 = 2\,\Omega$ en la parte superior. Malla 2 (centro): $R_3 = 6\,\Omega$ en la parte superior. Malla 3 (derecha): $V_{s2} = 10\,\text{V}$ en el lado derecho (polo + arriba), $R_5 = 4\,\Omega$ en la parte superior. La rama entre malla 1 y 2 tiene $R_2 = 3\,\Omega$. La rama entre malla 2 y 3 tiene $R_4 = 5\,\Omega$. Las corrientes $I_1$, $I_2$, $I_3$ circulan en sentido horario.
> 
> **Dado:**
> 
> - $V_{s1} = 30\,\text{V}$, $V_{s2} = 10\,\text{V}$
> - $R_1 = 2\,\Omega$, $R_2 = 3\,\Omega$ (compartida M1-M2), $R_3 = 6\,\Omega$
> - $R_4 = 5\,\Omega$ (compartida M2-M3), $R_5 = 4\,\Omega$
> 
> **Encontrar:** $I_1$, $I_2$, $I_3$ y la corriente real en cada rama compartida.
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | KVL: $\sum V = 0$ por cada malla | Generar las tres ecuaciones del sistema (Paso 1) |
> | $I_{rama compartida} = I_k - I_j$ | Calcular la corriente real cuando dos mallas comparten un elemento (Paso 1 y Paso 4) |
> | Sistema matricial $[R][I]=[V]$ | Organizar las tres ecuaciones para resolver por Cramer (Paso 2) |
> | Regla de Cramer: $I_k = \dfrac{\Delta_k}{\Delta}$ | Resolver el sistema 3×3 despejando cada corriente de malla (Paso 3) |
> 
> ![[ChatGPT Image 20 jun 2026, 23_38_28.png]]
> 
> ---
> 
> **¿Por qué en la rama compartida se usa $I_1 - I_2$?** Dos corrientes de malla contiguas circulan por la rama compartida en sentidos opuestos. La corriente real en esa rama es la diferencia algebraica. Si el resultado es positivo, el sentido real coincide con $I_1$; si es negativo, con $I_2$.
> 
> **Paso 1 — KVL en cada malla:**
> 
> Malla 1: $+30 - 2I_1 - 3(I_1 - I_2) = 0$ $$30 = 5I_1 - 3I_2 \quad (1)$$
> 
> Malla 2: $-3(I_2 - I_1) - 6I_2 - 5(I_2 - I_3) = 0$ $$0 = -3I_1 + 14I_2 - 5I_3 \quad (2)$$
> 
> Malla 3: $-5(I_3 - I_2) - 4I_3 - 10 = 0$ $$-10 = -5I_2 + 9I_3 \quad (3)$$
> 
> **Paso 2 — Sistema matricial por inspección:**
> 
> $$\begin{bmatrix} 5 & -3 & 0 \\ -3 & 14 & -5 \\ 0 & -5 & 9 \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \\ I_3 \end{bmatrix} = \begin{bmatrix} 30 \\ 0 \\ -10 \end{bmatrix}$$
> 
> **Paso 3 — Resolver por sustitución/Cramer:**
> 
> $\Delta = 5(14\cdot9 - (-5)(-5)) - (-3)((-3)(9) - (-5)(0)) + 0$ $= 5(126 - 25) + 3(-27) = 5(101) - 81 = 505 - 81 = 424$
> 
> $$I_1 = \frac{1}{\Delta}\begin{vmatrix}30 & -3 & 0\\0 & 14 & -5\\-10 & -5 & 9\end{vmatrix}$$
> 
> $= \dfrac{30(126-25) - (-3)(0\cdot9-(-5)(-10)) + 0}{424} = \dfrac{30(101) + 3(0-50)}{424} = \dfrac{3030 - 150}{424} = \dfrac{2880}{424} \approx 6.79\,\text{A}$
> 
> $$I_2 = \frac{1}{424}\begin{vmatrix}5 & 30 & 0\\-3 & 0 & -5\\0 & -10 & 9\end{vmatrix} = \frac{5(0-50)-30(-27-0)+0}{424} = \frac{-250+810}{424} = \frac{560}{424} \approx 1.32\,\text{A}$$
> 
> $$I_3 = \frac{1}{424}\begin{vmatrix}5 & -3 & 30\\-3 & 14 & 0\\0 & -5 & -10\end{vmatrix} = \frac{5(-140-0)+3(30)+30(15)}{424} = \frac{-700+90+450}{424} = \frac{-160}{424} \approx -0.38\,\text{A}$$
> 
> El signo negativo de $I_3$ indica que su sentido real es **antihorario**.
> 
> **Paso 4 — Corrientes en ramas compartidas:**
> 
> $$I_{R2} = I_1 - I_2 = 6.79 - 1.32 = 5.47\,\text{A} \quad \text{(sentido de } I_1\text{)}$$ $$I_{R4} = I_2 - I_3 = 1.32 - (-0.38) = 1.70\,\text{A} \quad \text{(sentido de } I_2\text{)}$$

---

## 7. Forma Matricial — Mallas 3×3

> [!example] ✏️ Sistema completo por inspección directa con Cramer
> 
> **🖊️ Cómo se ve el circuito:** Es el mismo circuito de S6. Este ejercicio muestra cómo construir la matriz directamente sin escribir KVL línea por línea.
> 
> ![[ChatGPT Image 20 jun 2026, 23_38_28.png]]
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $R_{kk} = \sum R_{\text{propias de la malla }k}$ | Llenar la diagonal de la matriz sin escribir KVL explícitamente |
> | $R_{kj} = -R_{\text{compartida entre }k\text{ y }j}$ | Llenar las posiciones fuera de la diagonal |
> | $V_k = \sum$ fuentes de la malla $k$ (signo según orientación) | Llenar el vector del lado derecho del sistema |
> 
> **¿Por qué el método matricial directo es más eficiente?** Una vez memorizado el patrón (diagonal = suma de R propias, fuera de diagonal = −R compartida, vector derecho = suma algebraica de fuentes), puedes escribir el sistema completo de un vistazo. Evita errores de signo al recorrer mallas.
> 
> **Reglas de construcción:**
> 
> |Posición|Regla|Signo|
> |---|---|---|
> |$R_{kk}$ (diagonal)|Suma de **todas** las R en la malla $k$|+|
> |$R_{kj}$ (fuera diagonal)|R **compartida** entre malla $k$ y malla $j$|−|
> |$V_k$ (vector derecho)|Fuentes en malla $k$: $-\to+$ es $+$, $+\to-$ es $-$|según orientación|
> 
> **Aplicación al circuito de S6:**
> 
> - Malla 1: $R_{11} = R_1 + R_2 = 2+3 = 5\,\Omega$ — $R_{12} = -R_2 = -3\,\Omega$ — $R_{13} = 0$ (no comparten) — $V_1 = +30\,\text{V}$
> - Malla 2: $R_{22} = R_2 + R_3 + R_4 = 3+6+5 = 14\,\Omega$ — $R_{21} = -3$ — $R_{23} = -R_4 = -5$ — $V_2 = 0$
> - Malla 3: $R_{33} = R_4 + R_5 = 5+4 = 9\,\Omega$ — $R_{31} = 0$ — $R_{32} = -5$ — $V_3 = -10\,\text{V}$ (corriente $I_3$ entra por + de $V_{s2}$)
> 
> $$\boxed{\begin{bmatrix} 5 & -3 & 0 \\ -3 & 14 & -5 \\ 0 & -5 & 9 \end{bmatrix} \begin{bmatrix} I_1 \\ I_2 \\ I_3 \end{bmatrix} = \begin{bmatrix} 30 \\ 0 \\ -10 \end{bmatrix}}$$
> 
> Resultado (de S6): $I_1 \approx 6.79\,\text{A}$, $I_2 \approx 1.32\,\text{A}$, $I_3 \approx -0.38\,\text{A}$

---

## 8. Forma Matricial — Nodos 3×3

> [!example] ✏️ Tres nodos desconocidos con conductancias
> 
> **🖊️ Cómo se ve el circuito:** Dibuja cuatro nodos: tierra (abajo al centro), $V_1$ (arriba izquierda), $V_2$ (arriba centro), $V_3$ (arriba derecha). Conecta: $G_1 = 0.5\,\text{S}$ entre $V_1$ y tierra; $G_2 = 0.25\,\text{S}$ entre $V_1$ y $V_2$; $G_3 = 0.2\,\text{S}$ entre $V_2$ y tierra; $G_4 = 0.1\,\text{S}$ entre $V_2$ y $V_3$; $G_5 = 0.4\,\text{S}$ entre $V_3$ y tierra. Fuentes: $I_{s1} = 4\,\text{A}$ entra a $V_1$; $I_{s2} = 2\,\text{A}$ sale de $V_2$; $I_{s3} = 3\,\text{A}$ entra a $V_3$.
> 
> **Dado:**
> 
> - $G_1 = 0.5$, $G_2 = 0.25$, $G_3 = 0.2$, $G_4 = 0.1$, $G_5 = 0.4$ (todos en S)
> - $I_{s1} = 4\,\text{A}$ (↑ entra a $V_1$), $I_{s2} = 2\,\text{A}$ (↓ sale de $V_2$), $I_{s3} = 3\,\text{A}$ (↑ entra a $V_3$)
> 
> **Encontrar:** $V_1$, $V_2$, $V_3$.
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $G = 1/R$ | Convertir cada resistencia a conductancia antes de construir la matriz |
> | $G_{kk} = \sum G_{\text{propias del nodo }k}$ | Llenar la diagonal de la matriz de conductancias |
> | $G_{kj} = -G_{\text{compartida entre nodo }k\text{ y }j}$ | Llenar las posiciones fuera de la diagonal |
> | Regla de Cramer: $V_k = \dfrac{\Delta_k}{\Delta}$ | Resolver el sistema 3×3 para cada tensión de nodo |
> 
> ![[ChatGPT Image 20 jun 2026, 23_47_46.png]]
> 
> ---
> 
> **¿Por qué usar conductancias $G = 1/R$ en este método?** En el método nodal, las corrientes se expresan como $I = G \cdot \Delta V$. Trabajar con $G$ directamente evita fracciones en las ecuaciones y hace que el patrón de la matriz sea idéntico al de mallas pero con conductancias en lugar de resistencias.
> 
> **Construcción de la matriz $[G]\cdot[V] = [I_f]$:**
> 
> - $G_{11} = G_1 + G_2 = 0.5 + 0.25 = 0.75\,\text{S}$
> - $G_{22} = G_2 + G_3 + G_4 = 0.25 + 0.2 + 0.1 = 0.55\,\text{S}$
> - $G_{33} = G_4 + G_5 = 0.1 + 0.4 = 0.5\,\text{S}$
> - $G_{12} = G_{21} = -G_2 = -0.25\,\text{S}$
> - $G_{23} = G_{32} = -G_4 = -0.1\,\text{S}$
> - $G_{13} = G_{31} = 0$ (no hay ramal directo entre $V_1$ y $V_3$)
> 
> $$\begin{bmatrix} 0.75 & -0.25 & 0 \\ -0.25 & 0.55 & -0.1 \\ 0 & -0.1 & 0.5 \end{bmatrix} \begin{bmatrix} V_1 \\ V_2 \\ V_3 \end{bmatrix} = \begin{bmatrix} 4 \\ -2 \\ 3 \end{bmatrix}$$
> 
> **Resolución (Cramer):**
> 
> $\Delta = 0.75(0.55\times0.5 - (-0.1)(-0.1)) - (-0.25)((-0.25)(0.5) - 0) + 0$ $= 0.75(0.275 - 0.01) + 0.25(-0.125)$ $= 0.75(0.265) - 0.03125 = 0.19875 - 0.03125 = 0.1675$
> 
> $$V_1 = \frac{1}{0.1675}\begin{vmatrix}4 & -0.25 & 0\\-2 & 0.55 & -0.1\\3 & -0.1 & 0.5\end{vmatrix}$$
> 
> $= \dfrac{4(0.275-0.01)+0.25(-1+0.3)+0}{0.1675} = \dfrac{4(0.265)+0.25(-0.7)}{0.1675} = \dfrac{1.06 - 0.175}{0.1675} = \dfrac{0.885}{0.1675} \approx \boxed{5.28\,\text{V}}$
> 
> $$V_2 \approx \boxed{6.42\,\text{V}}$$
> 
> $$V_3 \approx \boxed{7.48\,\text{V}}$$
> 
> ✅ Verificación KCL nodo $V_1$: $I_{s1} = G_1 V_1 + G_2(V_1-V_2) = 0.5(5.28) + 0.25(5.28-6.42) = 2.64 - 0.285 \approx 4\,\text{A}$ ✓

---

## 9. Interconexión de Fuentes Mixtas

> [!example] ✏️ Reducción de fuentes antes de plantear KVL
> 
> **🖊️ Cómo se ve el circuito:** Dibuja una malla. En el ramal superior izquierdo: $V_{s1} = 15\,\text{V}$ (+ hacia derecha) en serie con $V_{s2} = 5\,\text{V}$ (+ hacia izquierda, opuesta). En el ramal superior derecho: $V_{s3} = 8\,\text{V}$ (+ hacia derecha). Resistencias: $R_1 = 4\,\Omega$ (ramal izquierdo), $R_2 = 6\,\Omega$ (ramal inferior), $R_3 = 2\,\Omega$ (ramal derecho). Además, en paralelo con $R_2$ hay dos fuentes de corriente: $I_{s1} = 3\,\text{A}$ (apunta hacia arriba) e $I_{s2} = 1\,\text{A}$ (apunta hacia abajo).
> 
> **Dado:**
> 
> - $V_{s1} = 15\,\text{V}$, $V_{s2} = 5\,\text{V}$ (opuesta), $V_{s3} = 8\,\text{V}$
> - $R_1 = 4\,\Omega$, $R_2 = 6\,\Omega$, $R_3 = 2\,\Omega$
> - $I_{s1} = 3\,\text{A}$ (↑), $I_{s2} = 1\,\text{A}$ (↓) en paralelo con $R_2$
> 
> **Encontrar:** reducir las fuentes y calcular la corriente en $R_2$.
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $V_{eq} = V_1 \pm V_2$ (fuentes de voltaje en serie) | Combinar $V_{s1}$ y $V_{s2}$ del ramal izquierdo en una sola fuente (Paso 1) |
> | $I_{eq} = I_1 \pm I_2$ (fuentes de corriente en paralelo) | Combinar $I_{s1}$ e $I_{s2}$ en una sola fuente (Paso 2) |
> | Transformación de fuente: $V = I \times R$ | Convertir la fuente de corriente equivalente en una fuente de voltaje en serie con $R_2$ (Paso 4) |
> | KVL: $\sum V = 0$ | Resolver la malla final ya simplificada (Paso 5) |
> 
> ![[ChatGPT Image 20 jun 2026, 23_50_21.png]]
> 
> ---
> 
> **¿Por qué reducir fuentes antes de resolver?** Fuentes del mismo tipo en serie o paralelo pueden combinarse en una sola equivalente. Esto reduce la cantidad de ecuaciones necesarias y clarifica la topología del circuito antes de aplicar KVL/KCL.
> 
> **Paso 1 — Reducir fuentes de voltaje en serie (ramal izquierdo):**
> 
> $V_{s1}$ y $V_{s2}$ están en serie pero en oposición: $$V_{izq} = V_{s1} - V_{s2} = 15 - 5 = 10\,\text{V}$$
> 
> **Paso 2 — Reducir fuentes de corriente en paralelo:**
> 
> $I_{s1}$ e $I_{s2}$ están en paralelo, en sentidos opuestos: $$I_{eq} = I_{s1} - I_{s2} = 3 - 1 = 2\,\text{A} \quad (\uparrow)$$
> 
> **Paso 3 — Circuito reducido:** Ahora hay una malla con $V_{izq} = 10\,\text{V}$, $V_{s3} = 8\,\text{V}$, y $R_1$, $R_3$ en serie. $I_{eq} = 2\,\text{A}$ en paralelo con $R_2$.
> 
> **Paso 4 — Transformación de fuente de corriente a voltaje** (Norton → Thévenin):
> 
> $$V_{eq2} = I_{eq} \times R_2 = 2 \times 6 = 12\,\text{V} \quad \text{(en serie con } R_2\text{)}$$
> 
> **Paso 5 — KVL en la malla final:**
> 
> $$10 + 8 + 12 - 4I - 6I - 2I = 0 \implies 30 = 12I \implies \boxed{I = 2.5\,\text{A}}$$
> 
> $$\boxed{V_{R2} = 2.5 \times 6 = 15\,\text{V}}$$

---

## 10. Circuito Mixto de Cinco Resistencias

> [!example] ✏️ Tres etapas de simplificación — topología compleja
> 
> **🖊️ Cómo se ve el circuito:** Fuente $V_s = 48\,\text{V}$. Desde el nodo positivo sale $R_1 = 6\,\Omega$ en serie. Luego se divide en dos ramas: rama A con $R_2 = 12\,\Omega$ y rama B con $R_3 = 4\,\Omega$ en serie con $R_4 = 8\,\Omega$. Esas dos ramas se unen en un nodo del que sale $R_5 = 3\,\Omega$ en serie hasta volver a la fuente.
> 
> **Dado:** $V_s = 48\,\text{V}$, $R_1 = 6\,\Omega$, $R_2 = 12\,\Omega$, $R_3 = 4\,\Omega$, $R_4 = 8\,\Omega$, $R_5 = 3\,\Omega$
> 
> **Encontrar:** $R_{eq}$, $I_{total}$, corriente en cada rama del paralelo y potencia total.
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $R_{serie} = R_a + R_b$ | Reducir $R_3$ y $R_4$, que están en serie dentro de la rama B (Paso 1) |
> | $R_{paralelo} = \dfrac{R_a R_b}{R_a+R_b}$ | Reducir el grupo paralelo $R_2 \| R_{34}$ (Paso 2) |
> | $R_{eq} = R_1 + R_{paralelo} + R_5$ | Obtener la resistencia equivalente total del circuito mixto (Paso 3) |
> | $I = V/R$ (Ohm) | Calcular la corriente total con $V_s$ y $R_{eq}$ (Paso 4) |
> | $V = I \times R$ (Ohm) | Calcular el voltaje sobre el grupo paralelo (Paso 5) |
> | $P = V \times I$ y $P = I^2 R$ | Calcular potencia total y por elemento, y verificar con el teorema de Tellegen (Paso 7) |
> 
> ![[ChatGPT Image 21 jun 2026, 00_00_35.png]]
> 
> ---
> 
> **¿Por qué simplificar de adentro hacia afuera?** En un circuito mixto, los grupos paralelos están "incrustados" entre resistencias en serie. Se reduce primero el paralelo interior, luego se suma con las series que lo rodean. Intentar resolver todo junto genera errores topológicos.
> 
> **Paso 1 — Reducir la rama B del paralelo ($R_3$ y $R_4$ en serie):**
> 
> $$R_{34} = R_3 + R_4 = 4 + 8 = 12\,\Omega$$
> 
> **Paso 2 — Reducir el paralelo ($R_2 | R_{34}$):**
> 
> $$R_{paralelo} = \frac{R_2 \times R_{34}}{R_2 + R_{34}} = \frac{12 \times 12}{12 + 12} = \frac{144}{24} = 6\,\Omega$$
> 
> **Paso 3 — Circuito serie equivalente:**
> 
> $$R_{eq} = R_1 + R_{paralelo} + R_5 = 6 + 6 + 3 = \boxed{15\,\Omega}$$
> 
> **Paso 4 — Corriente total:**
> 
> $$I_{total} = \frac{V_s}{R_{eq}} = \frac{48}{15} = 3.2\,\text{A}$$
> 
> **Paso 5 — Voltaje en el paralelo:**
> 
> $$V_{paralelo} = I_{total} \times R_{paralelo} = 3.2 \times 6 = 19.2\,\text{V}$$
> 
> **Paso 6 — Corrientes en cada rama** (mismo voltaje en paralelo):
> 
> $$I_{R2} = \frac{V_{paralelo}}{R_2} = \frac{19.2}{12} = 1.6\,\text{A}$$
> 
> $$I_{R34} = \frac{V_{paralelo}}{R_{34}} = \frac{19.2}{12} = 1.6\,\text{A}$$
> 
> **Paso 7 — Potencia total y verificación Tellegen:**
> 
> $$P_{total} = V_s \times I_{total} = 48 \times 3.2 = 153.6\,\text{W}$$
> 
> $P_{R1} = (3.2)^2 \times 6 = 61.44\,\text{W}$, $P_{R2} = (1.6)^2 \times 12 = 30.72\,\text{W}$ $P_{R3} = (1.6)^2 \times 4 = 10.24\,\text{W}$, $P_{R4} = (1.6)^2 \times 8 = 20.48\,\text{W}$, $P_{R5} = (3.2)^2 \times 3 = 30.72\,\text{W}$
> 
> ✅ Suma: $61.44 + 30.72 + 10.24 + 20.48 + 30.72 = 153.6\,\text{W}$ ✓

---

## 11. Capacitores e Inductores en Red Mixta

> [!example] ✏️ Reducción en dos etapas con C y L combinados
> 
> **🖊️ Cómo se ve el circuito:** **Sección capacitores:** $C_1 = 6\,\mu F$ en serie con la combinación paralela de $C_2 = 8\,\mu F$ y $C_3 = 4\,\mu F$. **Sección inductores:** $L_1 = 10\,\text{mH}$ en paralelo con la combinación serie de $L_2 = 6\,\text{mH}$ y $L_3 = 6\,\text{mH}$.
> 
> **Dado:**
> 
> - $C_1 = 6\,\mu F$, $C_2 = 8\,\mu F$, $C_3 = 4\,\mu F$
> - $L_1 = 10\,\text{mH}$, $L_2 = 6\,\text{mH}$, $L_3 = 6\,\text{mH}$
> 
> **Encontrar:** $C_{eq}$ y $L_{eq}$ de cada sección.
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $C_{paralelo} = C_a + C_b$ | Combinar $C_2$ y $C_3$, que están en paralelo |
> | $\dfrac{1}{C_{serie}} = \dfrac{1}{C_a}+\dfrac{1}{C_b}$ | Combinar $C_1$ en serie con el grupo $C_{23}$ |
> | $L_{serie} = L_a + L_b$ | Combinar $L_2$ y $L_3$, que están en serie |
> | $L_{paralelo} = \dfrac{L_a L_b}{L_a+L_b}$ | Combinar $L_1$ en paralelo con el grupo $L_{23}$ |
> 
> ![[ChatGPT Image 21 jun 2026, 00_06_46.png]]
> 
> ---
> 
> **¿Por qué C y L se combinan al revés entre sí?** La capacitancia en paralelo suma porque las áreas de las placas se suman. En serie, la distancia efectiva aumenta, reduciendo $C$. El inductor se comporta como una resistencia: serie suma, paralelo da producto sobre suma. Son duales eléctricos.
> 
> **Sección Capacitores:**
> 
> Paso 1 — Paralelo $C_2 | C_3$: $$C_{23} = C_2 + C_3 = 8 + 4 = 12\,\mu F$$
> 
> Paso 2 — Serie $C_1$ con $C_{23}$: $$\frac{1}{C_{eq}} = \frac{1}{6} + \frac{1}{12} = \frac{3}{12} = \frac{1}{4} \implies \boxed{C_{eq} = 4\,\mu F}$$
> 
> **Sección Inductores:**
> 
> Paso 1 — Serie $L_2 + L_3$: $$L_{23} = 6 + 6 = 12\,\text{mH}$$
> 
> Paso 2 — Paralelo $L_1 | L_{23}$: $$L_{eq} = \frac{10 \times 12}{10 + 12} = \frac{120}{22} \approx \boxed{5.45\,\text{mH}}$$

---

## 12. Divisor de Voltaje en Circuito de Tres Etapas

> [!example] ✏️ Divisor encadenado con dos grupos paralelos
> 
> **🖊️ Cómo se ve el circuito:** Fuente $V_s = 60\,\text{V}$. En serie: $R_1 = 5\,\Omega$, grupo paralelo A ($R_2 = 20\,\Omega | R_3 = 30\,\Omega$), $R_4 = 4\,\Omega$, grupo paralelo B ($R_5 = 15\,\Omega | R_6 = 10\,\Omega$).
> 
> **Dado:** $V_s = 60\,\text{V}$, $R_1 = 5\,\Omega$, $R_2 = 20\,\Omega$, $R_3 = 30\,\Omega$, $R_4 = 4\,\Omega$, $R_5 = 15\,\Omega$, $R_6 = 10\,\Omega$
> 
> **Encontrar:** voltaje sobre cada grupo paralelo usando el divisor.
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $R_{paralelo} = \dfrac{R_a R_b}{R_a+R_b}$ | Reducir cada grupo paralelo (A y B) a una sola resistencia (Paso 1) |
> | $R_{eq} = \sum R_i$ (serie) | Sumar todo el circuito ya reducido a una sola malla serie (Paso 2) |
> | Divisor de voltaje: $V_k = V_s \cdot \dfrac{R_k}{R_{eq}}$ | Repartir el voltaje de la fuente entre cada elemento serie, incluidos los grupos reducidos (Paso 3) |
> 
> ![[ChatGPT Image 21 jun 2026, 00_11_05.png]]
> 
> ---
> 
> **Paso 1 — Reducir grupos paralelos:**
> 
> $$R_A = \frac{20 \times 30}{50} = 12\,\Omega \qquad R_B = \frac{15 \times 10}{25} = 6\,\Omega$$
> 
> **Paso 2 — $R_{eq}$ total:**
> 
> $$R_{eq} = 5 + 12 + 4 + 6 = 27\,\Omega$$
> 
> **Paso 3 — Divisor:**
> 
> $$\boxed{V_A = 60 \cdot \frac{12}{27} \approx 26.67\,\text{V}} \qquad \boxed{V_B = 60 \cdot \frac{6}{27} \approx 13.33\,\text{V}}$$
> 
> ✅ KVL: $11.11 + 26.67 + 8.89 + 13.33 = 60\,\text{V}$ ✓

---

## 13. Divisor de Corriente con Tres Ramas

> [!example] ✏️ Distribución de corriente con verificación de potencia
> 
> **🖊️ Cómo se ve el circuito:** Fuente de corriente $I_f = 12\,\text{A}$ conectada a tres resistencias en paralelo: $R_1 = 2\,\Omega$, $R_2 = 3\,\Omega$, $R_3 = 6\,\Omega$.
> 
> **Dado:** $I_f = 12\,\text{A}$, $R_1 = 2\,\Omega$, $R_2 = 3\,\Omega$, $R_3 = 6\,\Omega$
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $\dfrac{1}{R_{eq}} = \sum \dfrac{1}{R_i}$ | Reducir las tres resistencias en paralelo a una sola (Paso 1) |
> | $V = I \times R$ (Ohm) | Obtener el voltaje común a las tres ramas, usando $I_f$ y $R_{eq}$ (Paso 2) |
> | Divisor de corriente: $I_{Ri} = I_f \cdot \dfrac{R_{eq}}{R_i}$ | Repartir la corriente de la fuente entre las tres ramas (Paso 3) |
> | $P = I^2 R$ | Verificar la potencia de cada rama y la potencia total (Paso 4) |
> 
> ![[ChatGPT Image 21 jun 2026, 00_12_48.png]]
> 
> **Paso 1 — $R_{eq}$:**
> 
> $$\frac{1}{R_{eq}} = \frac{1}{2} + \frac{1}{3} + \frac{1}{6} = 1 \implies R_{eq} = 1\,\Omega$$
> 
> **Paso 2 — Voltaje:** $V = 12 \times 1 = 12\,\text{V}$
> 
> **Paso 3 — Corrientes** ($I_{Ri} = I_f \cdot R_{eq}/R_i$):
> 
> $$I_{R1} = 6\,\text{A} \qquad I_{R2} = 4\,\text{A} \qquad I_{R3} = 2\,\text{A}$$
> 
> ✅ KCL: $6 + 4 + 2 = 12\,\text{A}$ ✓
> 
> **Paso 4 — Potencias:**
> 
> $$P_1 = 72\,\text{W} \qquad P_2 = 48\,\text{W} \qquad P_3 = 24\,\text{W} \qquad P_{total} = 144\,\text{W}\ ✓$$

---

## 14. Superposición con Tres Fuentes

> [!example] ✏️ Tres sub-circuitos independientes — verificación cruzada
> 
> **Dado:** $V_{s1} = 18\,\text{V}$, $V_{s2} = 12\,\text{V}$, $I_s = 4\,\text{A}$, $R_1 = 3\,\Omega$, $R_2 = 6\,\Omega$, $R_3 = 6\,\Omega$
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | Apagar fuentes: $V_s \to$ cortocircuito, $I_s \to$ circuito abierto | Crear cada sub-circuito dejando activa solo una fuente a la vez |
> | $R_{paralelo} = \dfrac{R_a R_b}{R_a+R_b}$ | Reducir la red resistiva en cada sub-circuito |
> | Divisor de voltaje: $V_k = V_s \cdot \dfrac{R_k}{R_{eq}}$ o $V = I\times R$ | Calcular la contribución de cada fuente sobre $V_A$ |
> | Superposición: $V_{total} = V' + V'' + V'''$ | Sumar algebraicamente las tres contribuciones individuales (resultado final) |
> 
> **Sub-circuito 1 — Solo $V_{s1}$:** $R_{23} = 3\,\Omega$ → $V_A' = 18 \times \frac{3}{6} = 9\,\text{V}$
> 
> **Sub-circuito 2 — Solo $V_{s2}$:** $R_{13} = 2\,\Omega$ → $V_A'' = -12 \times \frac{2}{8} = -3\,\text{V}$
> 
> **Sub-circuito 3 — Solo $I_s$:** $R_{123} = 1.5\,\Omega$ → $V_A''' = 4 \times 1.5 = 6\,\text{V}$
> 
> $$\boxed{V_A = 9 - 3 + 6 = 12\,\text{V}}$$

---

## 15. Thévenin con Fuente Dependiente

> [!example] ✏️ $R_{Th}$ con fuente de prueba — caso con fuente controlada
> 
> **Dado:** $V_s = 20\,\text{V}$, $R_1 = 5\,\Omega$, $R_2 = 10\,\Omega$, $R_3 = 4\,\Omega$, CCCS $= 2I_x$
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $V_{Th} = V_{ca}$ (voltaje a circuito abierto en las terminales de interés) | Calcular $V_{Th}$ a partir de $I_x$ y la caída en $R_2$ |
> | Fuente de prueba $V_x$, $I_x$ (con la fuente independiente apagada) | Calcular $R_{Th} = V_x/I_T$ cuando hay fuentes dependientes — apagar solo las independientes |
> | Divisor de corriente o KVL | Hallar la corriente en $R_L$ una vez que se tiene el equivalente Thévenin |
> 
> **$V_{Th}$:** $I_x = 20/15 = 4/3\,\text{A}$ → $V_{Th} = I_x \times R_2 = 40/3 \approx \boxed{13.33\,\text{V}}$
> 
> **$R_{Th}$** (fuente de prueba con $V_s = 0$): $$\boxed{R_{Th} = 8\,\Omega}$$
> 
> **Corriente en $R_L = 6\,\Omega$:**
> 
> $$I_L = \frac{13.33}{8 + 6} \approx \boxed{0.952\,\text{A}}$$

---

## 16. Norton y Máxima Transferencia de Potencia

> [!example] ✏️ Cadena completa: Thévenin → Norton → MTP
> 
> **Dado:** $V_s = 36\,\text{V}$, $R_s = 3\,\Omega$, $R_1 = 9\,\Omega$, $R_2 = 6\,\Omega$
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | $V_{Th} = V_{ca}$ | Calcular el voltaje Thévenin en las terminales de carga |
> | $R_{Th}$ = resistencia vista desde las terminales (fuentes independientes apagadas) | Obtener la resistencia equivalente del circuito |
> | $I_N = V_{Th}/R_{Th}$ | Convertir el equivalente Thévenin a su equivalente Norton ($R_N = R_{Th}$) |
> | Máxima transferencia de potencia: $R_L = R_{Th}$, $P_{max} = \dfrac{V_{Th}^2}{4R_{Th}}$ | Determinar la carga que extrae la mayor potencia posible y cuánta es |
> 
> **$V_{Th}$:** $I = 36/18 = 2\,\text{A}$ → $V_{Th} = 2 \times 9 = \boxed{18\,\text{V}}$
> 
> **$R_{Th}$:** $R_1 | (R_s + R_2) = 9|9 = \boxed{4.5\,\Omega}$
> 
> **Norton:** $I_N = 18/4.5 = \boxed{4\,\text{A}}$
> 
> **MTP:** $R_L = R_{Th} = 4.5\,\Omega$ → $P_{max} = \dfrac{18^2}{4 \times 4.5} = \boxed{18\,\text{W}}$
> 
> > 💡 En este punto la eficiencia es 50%: la fuente disipa $18\,\text{W}$ en $R_{Th}$ y entrega $18\,\text{W}$ a la carga. Aceptable en telecomunicaciones; inaceptable en sistemas de potencia.

---

## 17. Transformación de Fuentes Encadenada

> [!example] ✏️ Tres transformaciones sucesivas para simplificar a una malla
> 
> **Dado:** $V_{s1} = 10\,\text{V}$, $R_1 = 5\,\Omega$, $I_{s1} = 3\,\text{A}$, $R_2 = 10\,\Omega$, $V_{s2} = 6\,\text{V}$, $R_3 = 3\,\Omega$, $R_L = 2\,\Omega$
> 
> **🔑 Fórmulas que vamos a usar:**
> 
> | Fórmula | Para qué / cuándo |
> |---|---|
> | Voltaje → Corriente: $I_N = V_s/R_s$ (misma $R$) | Convertir $V_{s1}$ en una fuente de corriente equivalente para poder combinarla con $I_{s1}$ (T1) |
> | Fuentes de corriente en paralelo se suman; sus resistencias se combinan en paralelo | Combinar las dos fuentes de corriente en una sola |
> | Corriente → Voltaje: $V_{Th} = I_N \cdot R_N$ (misma $R$) | Convertir el resultado de vuelta a fuente de voltaje para combinarlo en serie con $V_{s2}$ (T2) |
> | Fuentes de voltaje en serie se suman; sus resistencias se combinan en serie | Reducir todo a una sola malla con una fuente y una resistencia equivalente |
> | $I = V/R$ (Ohm) | Calcular la corriente final en $R_L$ una vez reducido a una sola malla |
> 
> **T1 — Voltaje → Corriente:** $I_{N1} = 10/5 = 2\,\text{A}$ con $R_1 = 5\,\Omega$
> 
> **Combinar corrientes:** $I_{eq} = 2 + 3 = 5\,\text{A}$, $R_{eq} = 5|10 = 10/3\,\Omega$
> 
> **T2 — Corriente → Voltaje:** $V_{eq} = 5 \times 10/3 = 50/3\,\text{V}$ con $10/3\,\Omega$
> 
> **Combinar voltajes en serie:** $V_{total} = 50/3 + 6 = 68/3\,\text{V}$, $R_{total} = 10/3 + 3 = 19/3\,\Omega$
> 
> $$I_L = \frac{68/3}{19/3 + 2} = \frac{68}{25} = \boxed{2.72\,\text{A}}$$

---

## 📊 Resumen de Fórmulas Clave

> [!success] Formulas que necesitas para resolver los ejercicios
> 
> |Concepto|Fórmula|Ejercicio|
> |---|---|---|
> |Coulomb vectorial|$\vec{F}_{neta} = \sum K_e\dfrac{q_a q_b}{r^2}\hat{r}$|S1|
> |Potencia máxima tolerable|$I_{max} = \sqrt{P_{max}/R}$|S3|
> |Tensiones de nodo|$I_{saliente} = \dfrac{V_A - V_B}{R}$|S4, S8|
> |KVL con fuentes opuestas|Signo según $-!\to!+$ del recorrido|S5|
> |Mallas 3×3 matricial|$R_{kk} = \sum R_{\text{propias}}$, $R_{kj} = -R_{\text{compartida}}$|S7|
> |Nodos 3×3 matricial|$G_{kk} = \sum G_{\text{propias}}$, $G_{kj} = -G_{\text{compartida}}$|S8|
> |Divisor encadenado|Reducir paralelos → $V_k = V_s \cdot R_k/R_{eq}$|S12|
> |Divisor corriente 3 ramas|$I_{Ri} = I_f \cdot R_{eq}/R_i$|S13|
> |Superposición 3 fuentes|$V_{total} = V' + V'' + V'''$|S14|
> |$R_{Th}$ con dep.|$R_{Th} = V_x / I_T$ (fuente de prueba)|S15|
> |Máxima transferencia|$R_L = R_{Th}$, $P_{max} = V_{Th}^2/(4R_{Th})$|S16|
> |Transformación encadenada|$I_N = V_s/R_s$ ↔ $V_{Th} = I_N \cdot R_N$|S17|

---

**Tags:** #ejercicios #práctica #repaso #ohm #kirchhoff #KCL #KVL #thévenin #norton #superposición #serie #paralelo #mixto #divisor #fuentes #dependientes #matricial #EYAG1037 #FESD #ESPOL #unidad1