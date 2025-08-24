# ⚡ Momento de Inercia

> [!info] 🎯 Definición Fundamental El momento de inercia ($I$) es la **resistencia de un objeto a cambiar su estado de movimiento rotacional**. Es el equivalente rotacional de la masa en el movimiento lineal - mientras mayor sea el momento de inercia, más difícil será acelerar o detener la rotación del objeto.

---

## 🔧 Variables y Magnitudes

> [!tip] 📏 Magnitudes Principales
> 
> - **Momento de Inercia** ($I$): Resistencia rotacional en kg⋅m²
> - **Masa** ($m$): Masa del objeto en kilogramos [kg]
> - **Distancia al eje** ($r$): Distancia perpendicular al eje de rotación [m]
> - **Torque** ($\tau$): Momento de torsión en N⋅m
> - **Aceleración angular** ($\alpha$): Cambio de velocidad angular en rad/s²

---

## 🧮 Fórmulas Fundamentales

> [!note] 📐 Ecuaciones Clave
> 
> ### Partícula Puntual
> 
> $$I = mr^2$$
> 
> ### Sistema de Partículas
> 
> $$I = \sum m_i r_i^2$$
> 
> ### Cuerpos Rígidos Estándar
> 
> - **Anillo delgado**: $I = MR^2$
> - **Disco sólido**: $I = \frac{1}{2}MR^2$
> - **Esfera sólida**: $I = \frac{2}{5}MR^2$
> - **Varilla (eje central)**: $I = \frac{1}{12}ML^2$
> 
> ### Teorema de Ejes Paralelos
> 
> $$I = I_{CM} + Md^2$$ donde $I_{CM}$ es el momento de inercia respecto al centro de masa y $d$ es la distancia entre ejes.

---

## 🎓 Marco Teórico

> [!abstract] 🧠 Conceptos Fundamentales
> 
> **Dependencia de la Distribución**: El momento de inercia no solo depende de la masa total, sino de **cómo se distribuye esa masa** respecto al eje de rotación. Masa más alejada del eje → mayor momento de inercia.
> 
> **Analogía con Masa Lineal**:
> 
> - Masa lineal → resistencia al cambio de velocidad lineal
> - Momento de inercia → resistencia al cambio de velocidad angular
> 
> **Principio Clave**: Cuanto más lejos esté la masa del eje de rotación, mayor será su contribución al momento de inercia (relación cuadrática con la distancia).

---

## 🔗 Diagrama Conceptual

> [!abstract] 📊 Mapa de Relaciones
> 
> ```mermaid
> graph TD
>    A[Objeto Rotando] --> B[Momento de Inercia I]
>    B --> C[Depende de masa: m]
>    B --> D[Depende de distribución: r²]
>    
>    E[Geometría del Objeto] --> F[Fórmulas Específicas]
>    F --> G[Anillo: MR²]
>    F --> H[Disco: ½MR²]
>    F --> I[Esfera: ⅖MR²]
>    F --> J[Varilla: 1/12 ML²]
>    
>    K[Teorema Ejes Paralelos] --> L[I = I_CM + Md²]
>    
>    B --> M[Dinámica Rotacional]
>    M --> N[τ = Iα]
>    M --> O[K_rot = ½Iω²]
> ```

---

## 🌍 Aplicaciones Prácticas

> [!example] 🎯 Casos de Estudio
> 
> ### 🧊 Patinador de Hielo
> 
> - **Brazos extendidos**: Gran momento de inercia → rotación lenta
> - **Brazos pegados**: Menor momento de inercia → rotación rápida
> - **Principio**: Conservación del momento angular ($L = I\omega = \text{constante}$)
> 
> ### 🚗 Ruedas de Automóvil
> 
> - **Distribución**: Masa concentrada en el borde (como anillo)
> - **Efecto**: Alto momento de inercia para su masa total
> - **Consecuencia**: Requiere más torque para acelerar/frenar
> 
> ### 🏌️ Bate de Béisbol
> 
> - **Eje en las manos**: Momento de inercia alto → difícil de mover
> - **Eje en el centro**: Momento de inercia menor → más fácil de girar

---

## 🔄 Metodología de Cálculo

> [!info] 🛠️ Flujo de Resolución
> 
> ```mermaid
> flowchart TD
>    A[Identificar el Sistema] --> B{¿Partícula o Cuerpo Rígido?}
>    
>    B -->|Partícula| C[Usar I = mr²]
>    B -->|Sistema de Partículas| D[Usar I = Σm_i r_i²]
>    B -->|Cuerpo Rígido| E[Identificar Geometría]
>    
>    E --> F[Aplicar Fórmula Específica]
>    F --> G{¿Eje por Centro de Masa?}
>    
>    G -->|Sí| H[Resultado Final]
>    G -->|No| I[Aplicar Teorema Ejes Paralelos]
>    I --> J[I = I_CM + Md²]
>    J --> H
>    
>    C --> H
>    D --> H
> ```

---

## 📊 Ejercicios Resueltos

> [!warning] 🧮 Problema 1: Varilla con Masas Puntuales **Enunciado**: Varilla sin masa de 1.0 m con masa de 1.0 kg en un extremo y 2.0 kg en el otro. Calcular momento de inercia respecto al centro.
> 
> > [!success] ✅ Solución **Datos**: $m_1 = 1.0\text{ kg}$, $m_2 = 2.0\text{ kg}$, $L = 1.0\text{ m}$
> > 
> > **Distancias al centro**: $r_1 = r_2 = 0.5\text{ m}$
> > 
> > **Aplicación**: $I = \sum m_i r_i^2$ $$I = (1.0)(0.5)^2 + (2.0)(0.5)^2 = 0.25 + 0.50 = 0.75\text{ kg⋅m}^2$$

> [!warning] 🧮 Problema 2: Cilindro Rodando **Enunciado**: Cilindro sólido de masa $M$ y radio $R$ rueda sobre una superficie. Calcular momento de inercia respecto al punto de contacto.
> 
> > [!success] ✅ Solución **Momento de inercia del centro**: $I_{CM} = \frac{1}{2}MR^2$
> > 
> > **Distancia entre ejes**: $d = R$
> > 
> > **Teorema de ejes paralelos**: $$I = I_{CM} + Md^2 = \frac{1}{2}MR^2 + MR^2 = \frac{3}{2}MR^2$$

---

## 🔗 Conexiones Temáticas

> [!note] 🌐 Relaciones Conceptuales
> 
> ### [[Dinámica Rotacional]]
> 
> - **Segunda Ley de Newton rotacional**: $\sum \tau = I\alpha$
> - El momento de inercia es la "masa rotacional" en esta ecuación
> 
> ### [[Energía Cinética Rotacional]]
> 
> - **Fórmula**: $K_{rot} = \frac{1}{2}I\omega^2$
> - Análoga a $K = \frac{1}{2}mv^2$ pero para rotación
> 
> ### [[Centro de Masa]]
> 
> - **Teorema de ejes paralelos** conecta momento de inercia con centro de masa
> - Permite calcular $I$ para cualquier eje conociendo $I_{CM}$
> 
> ### [[Momento Angular]]
> 
> - **Relación**: $L = I\omega$
> - **Conservación**: Explica fenómenos como el patinador girando

---

## 📈 Comparación de Geometrías

> [!tip] 📊 Tabla de Momentos de Inercia
> 
> |**Geometría**|**Momento de Inercia**|**Factor**|
> |---|---|---|
> |Partícula puntual|$mr^2$|1.00|
> |Anillo delgado|$MR^2$|1.00|
> |Disco sólido|$\frac{1}{2}MR^2$|0.50|
> |Esfera sólida|$\frac{2}{5}MR^2$|0.40|
> |Esfera hueca|$\frac{2}{3}MR^2$|0.67|
> |Varilla (centro)|$\frac{1}{12}ML^2$|0.083|
> 
> **Observación**: A mayor concentración de masa cerca del eje, menor momento de inercia.

---

## 📝 Síntesis Clave

> [!summary] 🎯 Puntos Esenciales
> 
> - **Definición**: Resistencia rotacional análoga a la masa lineal
> - **Dependencia**: Proporcional a $mr^2$ (masa × distancia²)
> - **Geometría**: Cada forma tiene su fórmula específica
> - **Teorema clave**: Ejes paralelos $I = I_{CM} + Md^2$
> - **Aplicación**: Fundamental en dinámica rotacional y energía

---

## 📚 Referencias y Enlaces

> [!quote]  🏷️ Sistema de Organización
> 
> ### 🔗 Notas Relacionadas
> 
> - [[Dinámica Rotacional]]
> - [[Momento Angular]]
> - [[Energía Cinética Rotacional]]
> - [[Centro de Masa]]
> - [[Torque y Momento de Torsión]]
> - [[Conservación del Momento Angular]]
> - [[Teorema de Ejes Paralelos]]
> 
> ### 📖 Temas Avanzados
> 
> - [[Tensor de Inercia]]
> - [[Movimientos de Rodadura]]
> - [[Giroscopios y Precesión]]
> - [[Momento de Inercia de Cuerpos Compuestos]]
### Tags

#fisica #mecanica #rotacion #momento-inercia #dinamica-rotacional #energia-cinetica