---
dg-publish: true
tags: [FISG1001, unidad2, fisica-mecanica, dinamica, ley-de-la-gravitacion-universal]
---

# 🌍 Ley de la Gravitación Universal

## 🎯 Contexto Fundamental

> [!info] La Fuerza que Gobierna el Universo La **Ley de la Gravitación Universal** de Newton describe la **fuerza de atracción mutua** entre dos objetos debido a sus masas. Es la fuerza fundamental que:
>
> - 🪐 **Mantiene planetas en órbita** alrededor del Sol
> - 🌙 **Sostiene la Luna** en su trayectoria terrestre
> - 🏃‍♂️ **Nos mantiene pegados** al suelo
> - ⭐ **Rige el cosmos** entero a gran escala
>
> [!abstract] Principio Universal Esta ley se aplica a **todas las masas** en el universo, desde partículas microscópicas hasta galaxias enteras, siendo una de las **cuatro fuerzas fundamentales** de la naturaleza.

> [!note] 🖼️ Contexto Fundamental
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Ley_de_la_Gravitación_Universal_01.svg]]
>
> **Se lee así:** El diagrama abre la gravitación universal hacia cuatro escalas: el **sistema solar** (el Sol atrae a los planetas), el **sistema Tierra-Luna** (la Tierra atrae a la Luna), los **objetos en la superficie** (de ahí el peso) y las **escalas galácticas** (la estructura cósmica).
>
> **Por qué importa:** Muestra que una sola ley cubre desde el peso de una mochila hasta la dinámica de las galaxias. Cambia la escala, no la fórmula: `F = G m₁m₂/r²` sirve en los cuatro casos.

---

## 📊 Variables y Constantes

> [!tip] Magnitudes Fundamentales
>
> |Variable|Símbolo|Valor/Unidad|Descripción|
> |---|---|---|---|
> |Fuerza gravitacional|$\vec{F}_g$|N|Siempre atractiva 🧲|
> |Constante gravitacional|$G$|$6.674 \times 10^{-11} \frac{\text{N} \cdot \text{m}^2}{\text{kg}^2}$|Constante universal 🌌|
> |Masas|$m_1, m_2$|kg|Masas de los objetos interactuantes ⚖️|
> |Distancia|$r$|m|Entre centros de masa 📏|
> |Aceleración gravitacional|$g$|$9.8 \text{ m/s}^2$|En superficie terrestre 🌍|
>

> [!warning] Punto Importante La distancia $r$ se mide entre los **centros de masa** de los objetos, no entre sus superficies. Para objetos esféricos, esto simplifica considerablemente los cálculos.

---

## 🧮 Fórmulas Fundamentales

### 🌌 Ley Principal

> [!important] Fórmula de Newton $$F_g = G \frac{m_1 m_2}{r^2}$$
>
> **Características de la fuerza:**
>
> - 📍 **Dirección**: A lo largo de la línea que une los centros de masa
> - 🧲 **Sentido**: Siempre atractiva (nunca repulsiva)
> - 📈 **Dependencia**: Proporcional al producto de masas
> - 📉 **Dependencia**: Inversamente proporcional al cuadrado de la distancia

### 🌍 Aceleración Gravitacional

> [!note] Gravedad Terrestre **A nivel de superficie** ($h = 0$): $$g = G \frac{M_{Tierra}}{R_{Tierra}^2}$$
>
> **A una altura** $h$: $$g(h) = G \frac{M_{Tierra}}{(R_{Tierra} + h)^2}$$
>
> **Peso de un objeto**: $$W = mg$$

> [!note] 🖼️ Aceleración Gravitacional
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Ley_de_la_Gravitación_Universal_02.svg]]
>
> **Se lee así:** La cadena que lleva de la Tierra al peso de un objeto: la **masa de la Tierra** y el **radio de la Tierra** entran con la **constante G** y producen la **gravedad en la superficie**, que a su vez da el **peso de los objetos**.
>
> **Por qué importa:** Explica por qué el peso es `P = mg`: m es la masa del objeto, pero g no es una constante universal, es el valor local de `G M_Tierra / R_Tierra²`. La gravedad varía ligeramente con la latitud y la altitud.

---

## 🔬 Explicación Teórica

### 📐 Naturaleza de la Fuerza

> [!abstract] Características Fundamentales La **fuerza gravitacional** posee propiedades únicas:
>
> **🔄 Ley del inverso del cuadrado:**
>
> - Si duplicas la distancia → la fuerza se reduce a **1/4**
> - Si triplicas la distancia → la fuerza se reduce a **1/9**
> - Es una relación **no lineal** muy pronunciada
>
> **🧲 Siempre atractiva:**
>
> - No existe "antimateria gravitacional"
> - Todas las masas se atraen mutuamente
> - La fuerza actúa instantáneamente a cualquier distancia

### 📈 Dependencia de Variables

> [!note] 🖼️ Dependencia de Variables
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Ley_de_la_Gravitación_Universal_03.svg]]
>
> **Se lee así:** El diagrama de dependencias: la fuerza gravitacional es **proporcional a m₁ × m₂** y **proporcional a 1/r²**. De ahí las dos consecuencias: más masa significa más fuerza, y más distancia significa menos fuerza.
>
> **Por qué importa:** El inverso de la distancia al cuadrado es la parte no intuitiva: si duplicas la distancia, la fuerza cae a la **cuarta parte**, no a la mitad. Es lo que explica por qué las fuerzas gravitacionales son dominantes en lo macro y despreciables en lo micro.

---

## 🌍 Aplicaciones Prácticas

### 🪐 Órbitas Planetarias

> [!example] Sistema Solar **Mecanismo orbital:**
>
> - La gravedad del Sol proporciona la **fuerza centrípeta** ⭕
> - Los planetas se mantienen en **órbitas elípticas** 🥚
> - **Velocidad orbital** equilibra la atracción gravitacional
>
> **Relación clave:** $$F_{gravitacional} = F_{centrípeta}$$ $$G\frac{M_{Sol}m_{planeta}}{r^2} = \frac{m_{planeta}v^2}{r}$$

### ⚖️ El Peso

> [!tip] Peso vs. Masa **Diferencia conceptual:**
>
> - **Masa**: Cantidad de materia (invariante) 🧱
> - **Peso**: Fuerza gravitacional (variable) ⚖️
>
> **En la Tierra**: $W = mg = 9.8m$ N **En la Luna**: $W = 0.16mg$ (gravedad lunar ≈ 1/6 terrestre) **En el espacio**: $W \approx 0$ (pero $m$ sigue igual)

### 🚀 Astronautas en Órbita

> [!info] "Ingravidez" Aparente Los astronautas **no flotan porque la gravedad sea cero**:
>
> - La gravedad actúa normalmente sobre ellos 🌍
> - Están en **caída libre constante** alrededor de la Tierra 🔄
> - Su velocidad orbital equilibra la atracción gravitacional ⚖️
> - Experimentan **microgravedad**, no ausencia de gravedad

---

## 📈 Análisis Gráfico

### 📊 Fuerza vs. Distancia

> [!note] Gráfica $F_g$ vs. $r$ La relación $F_g \propto \frac{1}{r^2}$ produce una **curva hiperbólica**:
>
> - 📈 **Cerca del objeto**: Fuerza muy intensa
> - 📉 **Lejos del objeto**: Fuerza decrece rápidamente
> - ♾️ **Nunca llega a cero**: Alcance infinito (teóricamente)

> [!note] 🖼️ Fuerza vs. Distancia
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Ley_de_la_Gravitación_Universal_04.svg]]
>
> **Se lee así:** Una escala visual de tres casos: con **r pequeño** la fuerza es grande (**zona de alta gravedad**), con **r mediano** es moderada (**zona intermedia**) y con **r grande** es pequeña (**zona de baja gravedad**), con el color marcando las tres regiones.
>
> **Por qué importa:** Convierte el 1/r² en una intuición: cerca de una masa enorme (o dentro de un cuerpo muy denso) domina la gravedad; lejos, el resto de fuerzas casi desaparece. Es el mapa mental de la variación de g dentro y fuera de un planeta.

---

## 🧪 Ejemplo Detallado

### ☀️ Fuerza Sol-Tierra

> [!example] Cálculo Cósmico **Problema**: Calcular la fuerza gravitacional entre el Sol y la Tierra
>
> **Datos conocidos:**
>
> - Masa del Sol: $M_{☀️} = 1.989 \times 10^{30}$ kg
> - Masa de la Tierra: $M_{🌍} = 5.972 \times 10^{24}$ kg
> - Distancia promedio: $r = 1.496 \times 10^{11}$ m (1 UA)
> - Constante: $G = 6.674 \times 10^{-11} \frac{\text{N} \cdot \text{m}^2}{\text{kg}^2}$
>

> [!note] Desarrollo del Cálculo **Aplicando la fórmula:** $$F_g = G \frac{M_{☀️} \times M_{🌍}}{r^2}$$
>
> **Sustituyendo valores:** $$F_g = (6.674 \times 10^{-11}) \frac{(1.989 \times 10^{30})(5.972 \times 10^{24})}{(1.496 \times 10^{11})^2}$$
>
> **Resultado:** $$F_g \approx 3.54 \times 10^{22} \text{ N}$$
>
> **Interpretación**: ¡Una fuerza **gigantesca** que mantiene la Tierra en órbita! 🌍💫

---

## 🔗 Conexiones Conceptuales

> [!note] 🖼️ Conexiones Conceptuales
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Ley_de_la_Gravitación_Universal_05.svg]]
>
> **Se lee así:** El mapa mental organiza la gravitación universal en cuatro frentes: los **fundamentos matemáticos** (ley del inverso cuadrado, fuerza siempre atractiva, proporcional a las masas), las **aplicaciones astronómicas** (órbitas planetarias, sistema Tierra-Luna, trayectorias espaciales), los **efectos terrestres** (peso de objetos, mareas oceánicas, variaciones altitudinales) y los **principios físicos** (fuerza conservativa, energía potencial, dinámica newtoniana).
>
> **Por qué importa:** Añade el puente hacia la unidad siguiente: la gravitación es conservativa, así que la energía potencial gravitatoria `U = -Gm₁m₂/r` es la que permite luego aplicar la conservación de la energía.

> [!success] Relaciones Clave
>
> - **🎯 Dinámica**: Base para la segunda ley de Newton ($\sum F = ma$)
> - **💫 Energía Potencial**: Fuerza conservativa con $U_g = -G\frac{m_1m_2}{r}$
> - **🔄 Movimiento Circular**: Proporciona fuerza centrípeta en órbitas
> - **⭐ Astrofísica**: Explica estructura y evolución del universo

---

## 💡 Síntesis Conceptual

> [!abstract] Puntos Esenciales
>
> ### 🌌 **Universalidad**
>
> - Se aplica a **todas las masas** del universo
> - **Misma ley** para objetos microscópicos y galácticos
> - **Alcance infinito** (aunque decrece con distancia)
>
> ### 🧮 **Matemáticas**
>
> - **Ley simple**: $F_g = G \frac{m_1 m_2}{r^2}$
> - **Dependencia no lineal** con la distancia
> - **Constante universal** $G$ en toda la naturaleza
>
> ### 🎯 **Aplicaciones**
>
> - **Peso** y gravedad terrestre
> - **Órbitas** planetarias y satelitales
> - **Mareas** y efectos astronómicos

> [!note] 🖼️ Síntesis Conceptual
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Ley_de_la_Gravitación_Universal_06.svg]]
>
> **Se lee así:** El mapa de aplicaciones en dos columnas: **cósmicas** (sistema solar, sistema Tierra-Luna, misiones espaciales) y **terrestres** (peso de objetos, mareas, satélites), ambas colgando de la fórmula universal.
>
> **Por qué importa:** Separa las dos familias de ejercicios: los que piden la **fuerza** y los que piden trayectorias. En las aplicaciones cósmicas la ley se combina con la segunda ley para obtener la órbita; en las terrestres, normalmente basta con la aceleración en la superficie.

---

## 🔗 Referencias y Enlaces

> [!abstract] Notas Relacionadas
>
> ### 📚 Conceptos Fundamentales
>
> - [[Leyes de Newton]] - Marco dinámico general
> - [[Principios de Conservación de la Energía]] - Naturaleza de la gravedad
> - `Principio de Superposición` - Múltiples masas
>
>
> [!question] Para Profundizar
>
> ### 🔬 Temas Avanzados
>
> - `Relatividad General` - Teoría moderna de gravedad
> - `[[1er Semestre/Física Mecánica/01 - Cinemática/Aplicaciones de Cinemática Traslacional/Problemas de Encuentro.md]]` - Sistemas gravitacionales complejos
> - `Ondas Gravitacionales` - Perturbaciones del espaciotiempo
> - `Materia Oscura` - Efectos gravitacionales anómalos
>
> ### 🧪 Aspectos Experimentales
>
> - `Experimento de Cavendish` - Medición histórica de G
> - `Balance de Torsión` - Técnicas de medición precisa
> - `Gravimetría` - Medición de variaciones locales
> - `Geodesia` - Aplicaciones en ciencias de la Tierra
>
> ### 📊 Métodos Computacionales
>
> - `Simulaciones N-Cuerpos` - Modelado numérico
> - `Métodos de Perturbación` - Aproximaciones analíticas
> - `[[01 - Integración Numérica]]` - Solución de ecuaciones de movimiento

**Tags:** #FISG1001 #fisica-mecanica #unidad2 #ley-de-la-gravitacion-universal
