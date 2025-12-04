# ⚡ Energía en la Rotación

> [!abstract] 📋 Resumen La **energía cinética de rotación** es la energía que posee un objeto debido a su movimiento de rotación alrededor de un eje. Es fundamental para comprender fenómenos como la rodadura, el almacenamiento de energía en volantes, y la conservación de energía en sistemas rotacionales. Se complementa con la energía cinética de traslación para formar la energía cinética total del sistema.

---

## 🔍 Contexto y Definición

> [!info] 💡 Concepto Fundamental Así como un objeto en movimiento lineal posee **energía cinética de traslación**, un objeto que gira alrededor de un eje posee **energía cinética de rotación**. Esta energía es proporcional al momento de inercia y al cuadrado de la velocidad angular.

> [!note] 🎯 Analogía con Energía Lineal
> 
> |**Movimiento Lineal**|**Movimiento Rotacional**|
> |---|---|
> |$K_{lineal} = \frac{1}{2}mv^2$|$K_{rot} = \frac{1}{2}I\omega^2$|
> |Masa $m$|Momento de inercia $I$|
> |Velocidad $v$|Velocidad angular $\omega$|

---

> [!note] 📊 Variables Fundamentales
> 
> |Variable|Símbolo|Unidades|Descripción|
> |---|---|---|---|
> |Energía cinética rotacional|$K_{rot}$|$\text{J}$|Energía debido a rotación|
> |Energía cinética traslacional|$K_{trasl}$|$\text{J}$|Energía debido a traslación|
> |Momento de inercia|$I$|$\text{kg·m}^2$|"Masa rotacional"|
> |Velocidad angular|$\omega$|$\text{rad/s}$|Rapidez de rotación|
> |Velocidad del CM|$v_{CM}$|$\text{m/s}$|Velocidad del centro de masa|
> |Trabajo rotacional|$W_{rot}$|$\text{J}$|Trabajo realizado por torque|
> |Energía potencial|$U_g$|$\text{J}$|Energía de posición|

---

## ⚖️ Ecuaciones Fundamentales

> [!note] 🔧 Fórmulas de Energía Rotacional
> 
> ### Energía Cinética de Rotación
> 
> $$K_{rot} = \frac{1}{2}I\omega^2$$
> 
> ### Energía Cinética Total (Objeto que Rueda)
> 
> $$K_{total} = K_{trasl} + K_{rot} = \frac{1}{2}Mv_{CM}^2 + \frac{1}{2}I\omega^2$$
> 
> ### Trabajo Realizado por Torque
> 
> $$W_{rot} = \tau \Delta\theta$$
> 
> ### Teorema Trabajo-Energía Rotacional
> 
> $$W_{neto,rot} = \Delta K_{rot} = \frac{1}{2}I\omega_f^2 - \frac{1}{2}I\omega_i^2$$

> [!warning] ⚠️ Puntos Clave
> 
> - La energía rotacional depende del **cuadrado** de la velocidad angular
> - El momento de inercia actúa como la "masa rotacional"
> - En rodadura sin deslizar: $v_{CM} = \omega R$

---

## 🔄 Conservación de Energía en Sistemas Rotacionales

> [!info] ⚡ Principio de Conservación En ausencia de fuerzas no conservativas, la energía mecánica total se conserva:
> 
> $$E_{inicial} = E_{final}$$ $$K_{total,i} + U_{g,i} = K_{total,f} + U_{g,f}$$
> 
> ```mermaid
> flowchart LR
>    A[🏔️ Energía Potencial] --> B[⚡ Energía Cinética Total]
>    B --> C[🏃 Traslacional]
>    B --> D[🔄 Rotacional]
>    C --> E[½Mv²]
>    D --> F[½Iω²]
>    
>    style A fill:#81c784
>    style C fill:#64b5f6
>    style D fill:#ffb74d
> ```

---

## 📈 Distribución de Energía en Rodadura

> [!note] 🎯 Análisis por Forma Geométrica Para objetos rodando desde la misma altura, la distribución de energía cinética depende del momento de inercia:
> 
> |Objeto|Momento de Inercia|% Traslacional|% Rotacional|
> |---|---|---|---|
> |**Esfera sólida**|$I = \frac{2}{5}MR^2$|71%|29%|
> |**Cilindro sólido**|$I = \frac{1}{2}MR^2$|67%|33%|
> |**Aro/Anillo**|$I = MR^2$|50%|50%|

> [!info] 📊 Visualización de Distribución Energética
> 
> ```mermaid
> pie title Energía Cinética: Cilindro Rodando
>    "Traslacional (67%)" : 67
>    "Rotacional (33%)" : 33
> ```

> [!tip] 🎯 Implicación Práctica **Los objetos con menor momento de inercia llegan más rápido** al final de una rampa porque dedican más energía a la traslación que a la rotación.

---

## 🎲 Ejemplos y Aplicaciones

> [!example] 🏔️ Ejemplo 1: Cilindro Rodando por Rampa
> 
> **📋 Problema:** Un cilindro sólido de masa $M$ y radio $R$ rueda por una rampa de altura $h$. Encontrar la velocidad del centro de masa al final.
> 
> **🔧 Solución usando conservación de energía:**
> 
> 1. **Estado inicial:** $E_i = U_g = Mgh$ (en reposo en la cima)
> 2. **Estado final:** $E_f = K_{total} = \frac{1}{2}Mv_{CM}^2 + \frac{1}{2}I\omega^2$
> 3. **Para cilindro:** $I = \frac{1}{2}MR^2$ y $\omega = \frac{v_{CM}}{R}$
> 4. **Sustituyendo:** $$Mgh = \frac{1}{2}Mv_{CM}^2 + \frac{1}{2}\left(\frac{1}{2}MR^2\right)\left(\frac{v_{CM}}{R}\right)^2$$ $$Mgh = \frac{1}{2}Mv_{CM}^2 + \frac{1}{4}Mv_{CM}^2 = \frac{3}{4}Mv_{CM}^2$$
> 
> **📊 Resultado:** $v_{CM} = \sqrt{\frac{4gh}{3}}$

> [!example] ⚙️ Ejemplo 2: Volante de Inercia (Flywheel)
> 
> **📋 Situación:** Un volante de inercia almacena energía rotacional para suavizar la entrega de potencia en motores.
> 
> **🔧 Análisis energético:**
> 
> - **Almacenamiento:** $K_{rot} = \frac{1}{2}I\omega^2$
> - **Ventaja:** Alta densidad energética por masa
> - **Aplicación:** Almacenar energía cuando hay exceso, liberarla cuando hay demanda
> 
> **📊 Ejemplo numérico:** Si $I = 50 \text{ kg·m}^2$ y $\omega = 3000 \text{ rpm} = 314 \text{ rad/s}$: $$K_{rot} = \frac{1}{2}(50)(314)^2 = 2.47 \times 10^6 \text{ J} = 2.47 \text{ MJ}$$

> [!example] 💽 Ejemplo 3: Disco Duro
> 
> **📋 Situación:** El motor acelera el disco desde reposo hasta velocidad operativa.
> 
> **🔧 Análisis:**
> 
> - **Trabajo motor:** $W = \Delta K_{rot} = \frac{1}{2}I\omega_{final}^2 - 0$
> - **Potencia requerida:** $P = \frac{W}{t} = \frac{I\omega_{final}^2}{2t}$
> - **Mantenimiento:** Una vez girando, la energía se conserva (despreciando fricción)

---

## 🏃 Carrera de Objetos: Análisis Energético

> [!example] 🏁 Comparación de Velocidades Finales
> 
> **📋 Situación:** Diferentes objetos ruedan desde la misma altura $h$ por una rampa.
> 
> **🔧 Análisis general:** $$Mgh = \frac{1}{2}Mv_{CM}^2 + \frac{1}{2}I\omega^2 = \frac{1}{2}Mv_{CM}^2\left(1 + \frac{I}{MR^2}\right)$$
> 
> **📊 Velocidades finales:** $$v_{CM} = \sqrt{\frac{2gh}{1 + \frac{I}{MR^2}}}$$
> 
> |Objeto|Factor $\frac{I}{MR^2}$|Velocidad Final|
> |---|---|---|
> |**Esfera**|$\frac{2}{5} = 0.4$|$v = \sqrt{\frac{10gh}{7}} \approx 1.20\sqrt{gh}$|
> |**Cilindro**|$\frac{1}{2} = 0.5$|$v = \sqrt{\frac{4gh}{3}} \approx 1.15\sqrt{gh}$|
> |**Aro**|$1.0$|$v = \sqrt{gh} = 1.00\sqrt{gh}$|
> 
> **🏆 Orden de llegada:** Esfera → Cilindro → Aro

---

## ⚙️ Trabajo y Potencia Rotacional

> [!note] 🔧 Conceptos de Trabajo Rotacional
> 
> ### Trabajo Realizado por Torque
> 
> $$W_{rot} = \tau \Delta\theta$$
> 
> - $\tau$: Torque aplicado (constante)
> - $\Delta\theta$: Desplazamiento angular en radianes
> 
> ### Potencia Rotacional
> 
> $$P_{rot} = \tau \omega$$
> 
> - Análogo a $P = Fv$ en movimiento lineal
> 
> ### Teorema Trabajo-Energía
> 
> $$W_{neto} = \Delta K_{rot}$$ El trabajo neto realizado sobre un objeto rotatorio cambia su energía cinética rotacional.

> [!example] 🔧 Aplicación: Motor Eléctrico
> 
> **📋 Situación:** Un motor aplica torque constante $\tau$ para acelerar un disco desde reposo hasta $\omega_f$ en tiempo $t$.
> 
> **🔧 Cálculos:**
> 
> - **Trabajo realizado:** $W = \Delta K_{rot} = \frac{1}{2}I\omega_f^2$
> - **Potencia promedio:** $P_{prom} = \frac{W}{t} = \frac{I\omega_f^2}{2t}$
> - **Potencia final:** $P_f = \tau \omega_f$

---

## 🔗 Conexiones Conceptuales

> [!info] 🌐 Red de Conceptos
> 
> ```mermaid
> mindmap
>  root((⚡ Energía Rotación))
>    🔄 Fundamentos
>      Momento de Inercia
>      Velocidad Angular
>      Energía Cinética
>    ⚖️ Conservación
>      Energía Mecánica
>      Conversión Potencial-Cinética
>      Método Energético
>    🎯 Aplicaciones
>      Rodadura
>      Volantes de Inercia
>      Discos Duros
>      Motores
>    🔧 Trabajo y Potencia
>      Trabajo Rotacional
>      Potencia Rotacional
>      Teorema Trabajo-Energía
>    📊 Análisis
>      Distribución Energética
>      Comparación Objetos
>      Eficiencia Energética
> ```

> [!tip] 🎯 Estrategias de Resolución
> 
> 1. **Identifica** los tipos de energía presentes (traslacional, rotacional, potencial)
> 2. **Aplica** conservación de energía si no hay fuerzas no conservativas
> 3. **Usa** la condición de rodadura sin deslizar cuando aplique
> 4. **Calcula** el momento de inercia apropiado para la geometría
> 5. **Verifica** que las unidades y el resultado tengan sentido físico

---

## 📚 Referencias y Enlaces

> [!quote] 🔗 Links a Otras Notas
> 
> - > [[Física Mecanica/Notas antiguas/Dinámica Rotacional/Momento de Inercia]] - Fundamento de la energía rotacional
>     
> - > [[Dinámica Rotacional]] - Torque y aceleración angular
>     
> - > [[Rodadura]] - Aplicación principal de energía rotacional
>     
> - > [[Conservación de Energía]] - Principio fundamental
>     
> - > [[Trabajo y Energía]] - Conceptos base de energía
>     
> - > [[Conservación del Momento Angular]] - Otra cantidad conservada
>     
> - > [[Energía Cinética]] - Concepto análogo lineal
>     
> - > [[Potencia]] - Rapidez de transferencia energética
>     
> - > [[Volantes de Inercia]] - Aplicación tecnológica
>     

> [!quote] 📖 Material de Referencia
> 
> - > Tutorial: Energía en la rotación.pdf
>     
> - > Libro de texto: Capítulo de Energía y Trabajo
>     
> - > Experimentos: Rodadura de objetos por rampas
>     
> - > Videos demostrativos: Volantes de inercia en acción
>     
> - > Problemas resueltos: Conservación de energía rotacional
>     

---

> [!note] 🏷️ Tags #física #mecánica #energía #rotación #energía-cinética #conservación-energía #rodadura #momento-inercia #trabajo-rotacional #potencia #volante-inercia #teorema-trabajo-energía