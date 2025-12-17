# Cinemática Rotacional 🌀

>[!quote] _"El movimiento circular es la manifestación más elegante de la simetría en la naturaleza - desde las galaxias hasta los electrones, todo gira siguiendo las mismas leyes fundamentales."_ - Richard Feynman

---

## 📋 Conceptos Fundamentales

> [!info]- 🎯 **Definición de Cinemática Rotacional** La cinemática rotacional estudia el movimiento de rotación de los cuerpos rígidos sin considerar las causas que producen dicho movimiento. Se enfoca en describir cómo cambian las variables angulares con respecto al tiempo.
> 
> **Características principales:**
> 
> - Movimiento en torno a un eje fijo
> - Todos los puntos del objeto describen circunferencias concéntricas
> - Las variables son angulares (θ, ω, α)

## 🔢 Variables Cinemáticas Angulares

> [!tip]- 📐 **Posición Angular (θ)** **Definición:** Ángulo medido desde una línea de referencia hasta la posición del objeto.
> 
> **Unidades:**
> 
> - Radianes (rad) - Sistema Internacional
> - Grados (°) - Sistema sexagesimal
> - Revoluciones (rev)
> 
> **Conversiones importantes:**
> 
> |Radianes|Grados|Revoluciones|
> |---|---|---|
> |2π rad|360°|1 rev|
> |π rad|180°|0.5 rev|
> |1 rad|57.3°|0.159 rev|

> [!tip]- ⚡ **Velocidad Angular (ω)** **Definición:** Razón de cambio de la posición angular con respecto al tiempo.
> 
> $$\omega = \frac{d\theta}{dt}$$
> 
> **Unidades:** rad/s, rev/min (rpm)
> 
> **Características:**
> 
> - Vector perpendicular al plano de rotación
> - Dirección dada por la regla de la mano derecha
> - En movimiento uniforme: $\omega = \frac{\theta}{t}$

> [!tip]- 🚀 **Aceleración Angular (α)** **Definición:** Razón de cambio de la velocidad angular con respecto al tiempo.
> 
> $$\alpha = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$$
> 
> **Unidades:** rad/s²
> 
> **Interpretación:**
> 
> - α > 0: Aceleración angular positiva
> - α < 0: Desaceleración angular
> - α = 0: Velocidad angular constante

## 📊 Ecuaciones de la Cinemática Rotacional

> [!warning]- 🧮 **Ecuaciones para Aceleración Angular Constante** Estas ecuaciones son análogas a las de la cinemática lineal:
> 
> |Ecuación|Fórmula|Variables|
> |---|---|---|
> |**Velocidad angular**|$\omega = \omega_0 + \alpha t$|No incluye θ|
> |**Posición angular**|$\theta = \omega_0 t + \frac{1}{2}\alpha t^2$|No incluye ω|
> |**Velocidad-posición**|$\omega^2 = \omega_0^2 + 2\alpha\theta$|No incluye t|
> |**Posición promedio**|$\theta = \frac{(\omega_0 + \omega)t}{2}$|No incluye α|
> 
> **Donde:**
> 
> - $\omega_0$ = velocidad angular inicial
> - $\omega$ = velocidad angular final
> - $\alpha$ = aceleración angular
> - $t$ = tiempo
> - $\theta$ = desplazamiento angular

## 🔄 Relación entre Variables Lineales y Angulares

> [!info]- 🔗 **Correspondencias Fundamentales** Para un punto a distancia **r** del eje de rotación:
> 
> ```mermaid
> graph TD
>    A[Variables Angulares] --> B[Variables Lineales]
>    C[θ posición angular] --> D[s = rθ arco recorrido]
>    E[ω velocidad angular] --> F[v = rω velocidad tangencial]
>    G[α aceleración angular] --> H[at = rα aceleración tangencial]
>    
>    style A fill:#e1f5fe
>    style B fill:#f3e5f5
>    style C fill:#fff3e0
>    style D fill:#fff3e0
>    style E fill:#e8f5e8
>    style F fill:#e8f5e8
>    style G fill:#fce4ec
>    style H fill:#fce4ec
> ```
> 
> **Importante:** También existe aceleración centrípeta: $a_c = \frac{v^2}{r} = \omega^2 r$

## 🧠 Técnica de Estudio: Método de Analogías

> [!tip]- 🎓 **Estrategia de Aprendizaje: Analogías Lineales-Angulares** **Paso 1:** Memoriza las correspondencias usando la mnemotecnia **"ROTO"**:
> 
> - **R**otación → **R**adio multiplica
> - **O**mega → **O**rbital (velocidad)
> - **T**heta → **T**rayectoria (posición)
> - **O**mega punto → **O**scilación (aceleración)
> 
> **Paso 2:** Usa esta tabla de correspondencias:
> 
> |Lineal|Angular|Relación|
> |---|---|---|
> |s|θ|s = rθ|
> |v|ω|v = rω|
> |a|α|a = rα|
> |m|I|Masa ↔ Momento de inercia|
> 
> **Paso 3:** Practica convirtiendo problemas lineales a angulares y viceversa.

## 📋 Tipos de Movimiento Circular

> [!info]- 🔄 **Clasificación del Movimiento Circular**
> 
> **1. Movimiento Circular Uniforme (MCU)**
> 
> - ω = constante
> - α = 0
> - θ = ωt
> 
> **2. Movimiento Circular Uniformemente Acelerado (MCUA)**
> 
> - α = constante ≠ 0
> - Se aplican todas las ecuaciones cinemáticas
> 
> **3. Movimiento Circular Variable**
> 
> - α ≠ constante
> - Requiere cálculo diferencial/integral

## 🧪 Ejemplos Prácticos

> [!example]- 💡 **Problema Resuelto** Una rueda gira con velocidad angular inicial de 10 rad/s y experimenta una aceleración angular de -2 rad/s² durante 3 segundos.
> 
> **Encontrar:** Velocidad angular final y ángulo recorrido
> 
> **Solución:**
> 
> 1. **Velocidad angular final:** $\omega = \omega_0 + \alpha t = 10 + (-2)(3) = 4 \text{ rad/s}$
>     
> 2. **Ángulo recorrido:** $\theta = \omega_0 t + \frac{1}{2}\alpha t^2 = 10(3) + \frac{1}{2}(-2)(3)^2 = 30 - 9 = 21 \text{ rad}$
>     

## 🔍 Referencias y Conexiones

> [!quote]- 📚 **Referencias a otras notas**
> 
> - [[Cinemática Traslacional]] - Base conceptual para analogías
> - [[Momento de Inercia]] - Extensión hacia dinámica rotacional
> - [[Torque y Equilibrio Rotacional]] - Causas del movimiento angular
> - [[Segunda ley de Newton para Rotación]] - Dinámica del movimiento circular

## 📖 Notas Recomendadas para Complementar

> [!info]- 🎯 **Prerrequisitos y Temas Relacionados**
> 
> **Prerrequisitos esenciales:**
> 
> - [[Vectores]] - Para comprender direcciones angulares
> - [[Funciones Trigonométricas]] - Para resolver componentes
> - [[01 - Derivada y Definición Formal]] - Para definiciones de ω y α
> 
> **Temas complementarios:**
> 
> - [[Momentum Angular]] - Conservación en sistemas rotacionales
> - [[Energía de Rotación]] - Aspectos energéticos del movimiento
> - [[Rodadura]] - Combinación de traslación y rotación

---

**Tags:** #fisica-mecanica #cinematica #movimiento-circular #rotacion #ecuaciones-cinematicas #analogias-lineales-angulares