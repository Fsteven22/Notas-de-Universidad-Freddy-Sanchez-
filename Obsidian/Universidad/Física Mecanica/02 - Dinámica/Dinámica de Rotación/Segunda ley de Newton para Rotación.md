# ⚙️ Variante Rotacional de la Segunda Ley de Newton

> [!info] 🎯 Definición Fundamental La **variante rotacional de la Segunda Ley de Newton** es el principio fundamental que rige el movimiento de rotación. Establece que el **torque neto** que actúa sobre un objeto rígido es directamente proporcional a su **momento de inercia** y a la **aceleración angular** que produce. Es la versión rotacional de la fórmula $\sum F = ma$.

---

## 🔧 Variables y Magnitudes

> [!tip] 📏 Magnitudes Principales
> 
> - **Torque neto** ($\sum \tau$): Suma de todos los torques en N⋅m
> - **Momento de inercia** ($I$): Resistencia rotacional en kg⋅m²
> - **Aceleración angular** ($\alpha$): Cambio de velocidad angular en rad/s²
> - **Fuerza tangencial** ($F_t$): Componente tangencial de la fuerza en N
> - **Radio** ($r$): Distancia desde el eje de rotación en m
> - **Aceleración tangencial** ($a_t$): Aceleración en el borde del objeto en m/s²

---

## 🧮 Fórmulas Fundamentales

> [!note] 📐 Ecuaciones Clave
> 
> ### Ley Principal
> 
> $$\sum \tau = I\alpha$$
> 
> ### Relaciones con Movimiento Lineal
> 
> - **Torque por fuerza tangencial**: $\tau = rF_t$
> - **Aceleración angular-tangencial**: $\alpha = \frac{a_t}{r}$
> - **Velocidad angular-tangencial**: $\omega = \frac{v_t}{r}$
> 
> ### Analogía con Movimiento Lineal
> 
> |**Lineal**|**Rotacional**|
> |---|---|
> |$\sum F = ma$|$\sum \tau = I\alpha$|
> |Fuerza ($F$)|Torque ($\tau$)|
> |Masa ($m$)|Momento de inercia ($I$)|
> |Aceleración ($a$)|Aceleración angular ($\alpha$)|

---

## 🎓 Marco Teórico

> [!abstract] 🧠 Principios Fundamentales
> 
> **Relación Causa-Efecto:**
> 
> - **Causa**: Torque neto ($\sum \tau$)
> - **Efecto**: Aceleración angular ($\alpha$)
> - **Resistencia**: Momento de inercia ($I$)
> 
> **Proporcionalidad Directa:**
> 
> - Mayor torque → mayor aceleración angular
> - Mayor momento de inercia → menor aceleración angular (para mismo torque)
> 
> **Equivalencia Conceptual:** El momento de inercia es la "masa rotacional" que determina qué tan difícil es cambiar el estado de rotación de un objeto.

---

## 🔗 Diagrama Conceptual

> [!abstract] 📊 Mapa de Relaciones
> 
> ```mermaid
> graph TD
>    A[Fuerzas Aplicadas] --> B[Cálculo de Torques]
>    B --> C[Torque Neto: Suma tau]
>    
>    D[Geometría del Objeto] --> E[Momento de Inercia I]
>    
>    C --> F[Segunda Ley Rotacional]
>    E --> F
>    F --> G[Suma tau = I alpha]
>    
>    G --> H[Aceleración Angular alpha]
>    
>    H --> I[Cinemática Rotacional]
>    I --> J[Velocidad angular omega]
>    I --> K[Desplazamiento angular theta]
>    
>    L[Condiciones Iniciales] --> I
>    
>    H --> M[Movimiento Tangencial]
>    M --> N[a_t = alpha × r]
> ```

---

## 🛠️ Metodología de Resolución

> [!info] 🔄 Procedimiento Sistemático
> 
> ```mermaid
> flowchart TD
>    A[1. Identificar Fuerzas] --> B[2. Diagrama de Cuerpo Libre]
>    B --> C[3. Ubicar Eje de Rotación]
>    C --> D[4. Calcular Torques Individuales]
>    D --> E[5. Sumar Torques: Suma tau]
>    
>    F[6. Determinar Momento de Inercia I] --> G[7. Aplicar Segunda Ley]
>    E --> G
>    G --> H[Suma tau = I alpha]
>    
>    H --> I[8. Despejar alpha]
>    I --> J[9. Aplicar Cinemática Rotacional]
>    J --> K[10. Encontrar omega o theta]
> ```

---

## 🌍 Aplicaciones Prácticas

> [!example] 🎯 Casos de Estudio
> 
> ### ⚡ Volante de Inercia
> 
> - **Función**: Suavizar rotación en motores
> - **Principio**: Alto momento de inercia → resistente a cambios de velocidad angular
> - **Aplicación**: $I$ grande requiere $\tau$ grande para cambiar $\alpha$
> 
> ### 🪀 Yo-yo Desenrollándose
> 
> - **Fuerzas**: Peso del yo-yo y tensión de la cuerda
> - **Torques**: Peso no causa torque, tensión sí
> - **Resultado**: Aceleración angular controlada por la tensión
> 
> ### 🚗 Rueda Acelerando
> 
> - **Torque motor**: Aplicado en el eje
> - **Resistencia**: Momento de inercia de la rueda
> - **Efecto**: Aceleración angular proporcional al torque del motor

---

## 📊 Ejercicios Resueltos

> [!warning] 🧮 Problema 1: Péndulo Físico **Enunciado**: Un péndulo físico con momento de inercia $I$ se suelta desde un ángulo $\theta$. Encontrar la aceleración angular inicial.
> 
> > [!success] ✅ Solución **Análisis de torque**: El peso actúa a distancia $L$ del eje $$\tau = -mgL\sin\theta$$
> > 
> > **Aplicación de la Segunda Ley**: $$\sum \tau = I\alpha$$ $$-mgL\sin\theta = I\alpha$$
> > 
> > **Aceleración angular inicial**: $$\alpha = -\frac{mgL\sin\theta}{I}$$
> > 
> > El signo negativo indica rotación hacia la posición de equilibrio.

> [!warning] 🧮 Problema 2: Cilindro en Plano Inclinado **Enunciado**: Cilindro sólido de masa $M$ y radio $R$ rueda sin deslizar por un plano inclinado de ángulo $\theta$. Encontrar la aceleración del centro de masa.
> 
> > [!success] ✅ Solución **Fuerzas sobre el cilindro**:
> > 
> > - Peso: $Mg$ (hacia abajo)
> > - Normal: $N$ (perpendicular al plano)
> > - Fricción: $f$ (hacia arriba del plano)
> > 
> > **Ecuación lineal** ($\sum F = ma$): $$Mg\sin\theta - f = Ma$$
> > 
> > **Ecuación rotacional** ($\sum \tau = I\alpha$): $$fR = I\alpha = \frac{1}{2}MR^2\alpha$$
> > 
> > **Condición de rodadura**: $a = \alpha R$ $$f = \frac{1}{2}Ma$$
> > 
> > **Sustituyendo en ecuación lineal**: $$Mg\sin\theta - \frac{1}{2}Ma = Ma$$ $$Mg\sin\theta = \frac{3}{2}Ma$$
> > 
> > **Aceleración del centro de masa**: $$a = \frac{2g\sin\theta}{3}$$

---

## 📈 Análisis Gráfico

> [!tip] 📊 Gráfica Torque vs Aceleración Angular
> 
> **Relación Lineal**: Para momento de inercia constante $$\tau = I\alpha$$
> 
> **Características de la gráfica**:
> 
> - **Tipo**: Línea recta que pasa por el origen
> - **Pendiente**: Igual al momento de inercia ($I$)
> - **Intercepto**: Cero (sin torque → sin aceleración angular)
> 
> **Interpretación**:
> 
> - Pendiente mayor → mayor momento de inercia → más difícil de acelerar
> - Pendiente menor → menor momento de inercia → más fácil de acelerar

---

## 🔗 Conexiones Temáticas

> [!note] 🌐 Relaciones Conceptuales
> 
> ### [[Torque y Equilibrio Rotacional]]
> 
> - **Dependencia**: La ley requiere calcular el torque neto
> - **Relación**: $\tau$ es la causa de la aceleración angular
> 
> ### [[Momento de Inercia]]
> 
> - **Papel**: Constante de proporcionalidad en la ley
> - **Significado**: Resistencia al cambio de rotación
> 
> ### [[Cinemática Rotacional]]
> 
> - **Aplicación**: Una vez conocida $\alpha$, se calcula $\omega$ y $\theta$
> - **Ecuaciones**: $\omega = \omega_0 + \alpha t$, $\theta = \omega_0 t + \frac{1}{2}\alpha t^2$
> 
> ### [[Dinámica Lineal]]
> 
> - **Analogía directa**: $\sum F = ma$ ↔ $\sum \tau = I\alpha$
> - **Conexión**: Movimiento de traslación y rotación simultáneos
> 
> ### [[Energía Cinética Rotacional]]
> 
> - **Relación**: El trabajo rotacional $W = \tau \Delta\theta$ cambia la energía cinética
> - **Conexión**: $K_{rot} = \frac{1}{2}I\omega^2$

---

## ⚖️ Casos Especiales

> [!abstract] 🎯 Condiciones Particulares
> 
> ### Equilibrio Rotacional
> 
> **Condición**: $\sum \tau = 0$ **Resultado**: $\alpha = 0$ (velocidad angular constante)
> 
> ### Rotación Uniforme
> 
> **Condición**: $\alpha = 0$ **Implicación**: $\sum \tau = 0$ (torques balanceados)
> 
> ### Aceleración Angular Constante
> 
> **Condición**: $\sum \tau = \text{constante}$ **Resultado**: Movimiento uniformemente acelerado

---

## 📝 Síntesis Clave

> [!summary] 🎯 Puntos Esenciales
> 
> - **Ley fundamental**: $\sum \tau = I\alpha$ (equivalente rotacional de $F = ma$)
> - **Causa-efecto**: Torque neto causa aceleración angular
> - **Resistencia**: Momento de inercia determina la respuesta
> - **Metodología**: Diagrama libre → torques → momento de inercia → aplicar ley
> - **Aplicación universal**: Base de toda la dinámica rotacional

---

## 📚 Referencias y Enlaces

> [!quote]  🏷️ Sistema de Organización
> 
> 
> 
> ### 🔗 Notas Relacionadas
> 
> - [[Momento de Torsión (Torque)]]
> - [[Momento de Inercia]]
> - [[Cinemática Rotacional]]
> - [[Dinámica Lineal - Segunda Ley de Newton]]
> - [[Energía Cinética Rotacional]]
> - [[Centro de Masa]]
> - [[Equilibrio Rotacional]]
> 
> ### 📖 Temas Avanzados
> 
> - [[Movimiento de Rodadura]]
> - [[Sistemas de Múltiples Cuerpos]]
> - [[Conservación del Momento Angular]]
> - [[Análisis de Máquinas Rotativas]]
 
 ### Tags

 #fisica #mecanica #segunda-ley-newton #dinamica-rotacional #torque #momento-inercia