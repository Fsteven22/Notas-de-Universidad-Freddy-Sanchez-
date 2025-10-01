# 🎯 Centro de Masa

> [!info] 📖 Definición Fundamental El centro de masa es un punto imaginario que representa la **posición promedio** de la masa total de un sistema. Para efectos dinámicos, podemos considerar que toda la masa está concentrada en este punto único.

---

## 🔧 Variables y Magnitudes

> [!tip] 📏 Magnitudes Principales
> 
> - **Posición del centro de masa** ($\vec{r}_{CM}$): Vector posición en metros [m]
> - **Masa de partícula** ($m_i$): Masa individual en kilogramos [kg]
> - **Masa total** ($M_{total}$): Suma de todas las masas [kg]
> - **Velocidad del CM** ($\vec{v}_{CM}$): Velocidad en m/s
> - **Aceleración del CM** ($\vec{a}_{CM}$): Aceleración en m/s²

---

## 🧮 Fórmulas Fundamentales

> [!note] 📐 Ecuaciones Clave
> 
> ### Posición del Centro de Masa
> 
> $\vec{r}_{CM} = \frac{\sum m_i \vec{r}_i}{M_{total}} = \frac{m_1\vec{r}_1 + m_2\vec{r}_2 + ...}{m_1 + m_2 + ...}$
> 
> ### Componentes Cartesianas
> 
> $x_{CM} = \frac{\sum m_i x_i}{M_{total}} \qquad y_{CM} = \frac{\sum m_i y_i}{M_{total}}$
> 
> ### Velocidad del Centro de Masa
> 
> $\vec{v}_{CM} = \frac{d\vec{r}_{CM}}{dt} = \frac{\sum m_i \vec{v}_i}{M_{total}} = \frac{\vec{P}_{total}}{M_{total}}$
> 
> ### Aceleración del Centro de Masa
> 
> $\vec{a}_{CM} = \frac{d\vec{v}_{CM}}{dt} = \frac{\sum \vec{F}_{ext}}{M_{total}}$

---

## 🎓 Marco Teórico

> [!abstract] 🧠 Conceptos Fundamentales
> 
> **Principio de Equivalencia**: El centro de masa se comporta como si toda la masa del sistema estuviera concentrada en ese punto único.
> 
> **Independencia de Fuerzas Internas**: Solo las fuerzas externas afectan el movimiento del centro de masa. Las fuerzas internas (colisiones, explosiones) no alteran su trayectoria.

---

## 🔗 Diagrama Conceptual

> [!abstract] 📊 Mapa de Relaciones
> 
> ```mermaid
> graph TD
>    A[Sistema de Partículas] --> B[Cálculo del Centro de Masa]
>    B --> C[Posición: r_CM = Σm_i·r_i / M_total]
>    B --> D[Velocidad: v_CM = P_total / M_total]
>    B --> E[Aceleración: a_CM = ΣF_ext / M_total]
>    
>    F[Fuerzas Externas] --> E
>    G[Fuerzas Internas] -.-> H[No afectan al CM]
>    
>    C --> I[Simplificación del Sistema]
>    D --> I
>    E --> I
>    
>    I --> J[Análisis como Partícula Única]
> ```

---

## 🌍 Aplicaciones Prácticas

> [!example] 🎯 Casos de Estudio
> 
> ### 🏗️ Cuerpos Rígidos
> 
> - **Regulares**: Centro geométrico = Centro de masa
> - **Irregulares**: Puede estar fuera del cuerpo físico (ej: boomerang)
> 
> ### 💥 Colisiones y Explosiones
> 
> - Los objetos individuales cambian velocidad y dirección
> - El centro de masa mantiene velocidad constante (sin fuerzas externas)
> - **Ejemplo**: Granada que explota en el aire mantiene trayectoria parabólica en su CM

---

## 🔄 Flujo de Resolución

> [!info] 🛠️ Metodología de Solución
> 
> ```mermaid
> flowchart LR
>    A[Identificar Partículas] --> B[Determinar Masas m_i]
>    B --> C[Localizar Posiciones r_i]
>    C --> D[Calcular Masa Total M]
>    D --> E[Aplicar Fórmula del CM]
>    E --> F[Obtener r_CM]
>    
>    G[Si se requiere] --> H[Calcular v_CM]
>    H --> I[Calcular a_CM]
> ```

---

## 📊 Ejemplo Resuelto

> [!warning] 🧮 Problema Tipo **Enunciado**: Tres partículas con masas $m_1=1\text{ kg}$, $m_2=2\text{ kg}$ y $m_3=3\text{ kg}$ se ubican en las posiciones (1,0), (0,1) y (-1,-1) respectivamente.

> [!success] ✅ Solución Paso a Paso
> 
> **1. Masa Total**: $$M_{total} = 1 + 2 + 3 = 6\text{ kg}$$
> 
> **2. Componente X**: $$x_{CM} = \frac{(1)(1) + (2)(0) + (3)(-1)}{6} = \frac{-2}{6} = -\frac{1}{3}\text{ m}$$
> 
> **3. Componente Y**: $$y_{CM} = \frac{(1)(0) + (2)(1) + (3)(-1)}{6} = \frac{-1}{6}\text{ m}$$
> 
> **4. Resultado Final**: $$\vec{r}_{CM} = \left(-\frac{1}{3}, -\frac{1}{6}\right)\text{ m}$$

---

## 🔗 Conexiones Temáticas

> [!note] 🌐 Relaciones Conceptuales
> 
> ### [[Conservación del Momentum]]
> 
> - $\vec{P}_{total} = M_{total}\vec{v}_{CM} = \text{constante}$ (sin fuerzas externas)
> - La velocidad del CM es constante cuando se conserva el momentum
> 
> ### [[Leyes de Newton]]
> 
> - Segunda Ley aplicada al CM: $\sum \vec{F}_{ext} = M_{total}\vec{a}_{CM}$
> - Simplificación de sistemas complejos a partícula puntual
> 
> ### [[Dinámica de Sistemas]]
> 
> - Base para análisis de [[Colisiones]]
> - Fundamento de [[Explosiones]] y fragmentaciones

---

## 📝 Síntesis Clave

> [!summary] 🎯 Puntos Esenciales
> 
> - **Definición**: Punto que representa la posición promedio ponderada por masa
> - **Fórmula Base**: $\vec{r}_{CM} = \frac{\sum m_i \vec{r}_i}{M_{total}}$
> - **Comportamiento**: Solo afectado por fuerzas externas
> - **Aplicación**: Simplifica análisis de sistemas complejos

---

## 📚 Referencias y Enlaces

> [!quote] 🏷️ Sistema de Organización
> 
> ### 🔗 Notas Relacionadas
> 
> - [[Momentum Lineal y Su Conservación]]
> - [[Principios de Conservación de la Energía]]
> - [[Choques Uni-Bidimensionales]]
> - [[Rotación de Cuerpos Rígidos]]
> - [[Física Mecanica/Notas antiguas/Dinámica Rotacional/Momento de Inercia]]
> - [[Leyes de Newton]]

### 📖 Temas Avanzados
> [!summary]  Para más adelante:
> - [[Centro de Masa vs Centro de Gravedad]]
> - [[Sistemas de Referencia del Centro de Masa]]
> - [[Teorema del Eje Paralelo]]> 

tags

`#fisica` `#mecanica` `#centro-masa` `#dinamica` `#sistemas-particulas` `#momentum`