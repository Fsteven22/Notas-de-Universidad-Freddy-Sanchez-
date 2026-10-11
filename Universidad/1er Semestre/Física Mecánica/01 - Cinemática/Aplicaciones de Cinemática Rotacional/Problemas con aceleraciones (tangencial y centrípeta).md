---
dg-publish: true
---

# Problemas con aceleraciones (tangencial y centrípeta) 

> [!quote] "En el movimiento circular, la aceleración no solo cambia la rapidez, sino que también mantiene la curvatura del camino; entender sus componentes es dominar la danza entre velocidad y dirección." 🌀
>
> [!info] En el movimiento circular, la aceleración total se descompone en dos componentes fundamentales: la aceleración tangencial, que modifica la magnitud de la velocidad, y la aceleración centrípeta, que cambia constantemente la dirección del movimiento. Comprender estas componentes es esencial para analizar sistemas rotacionales complejos como ruedas, engranajes, satélites y máquinas rotativas.

## 🎯 Tipos de Aceleración en Movimiento Circular

> [!info] **Aceleración Tangencial (aₜ)** 🏹
> 
> ### Características Principales:
> 
> - **Dirección**: Tangente a la trayectoria circular
> - **Función**: Cambia la magnitud de la velocidad
> - **Relación**: aₜ = α × r (donde α es la aceleración angular)
> - **Unidades**: m/s²
> 
> ### Interpretación Física:
> 
> |Valor de aₜ|Significado|Efecto en la velocidad|
> |---|---|---|
> |aₜ > 0|Aceleración tangencial|Velocidad aumenta|
> |aₜ = 0|Velocidad constante|Sin cambio en magnitud|
> |aₜ < 0|Desaceleración tangencial|Velocidad disminuye|
> 
> ### Fórmulas Clave:
> 
> - aₜ = r × α
> - aₜ = dv/dt
> - α = aₜ/r
>
> [!tip] **Aceleración Centrípeta (aₓ)** 🎪
> 
> ### Características Principales:
> 
> - **Dirección**: Hacia el centro del círculo
> - **Función**: Cambia la dirección de la velocidad
> - **Magnitud**: aₓ = v²/r = ω²r
> - **Unidades**: m/s²
> 
> ### Interpretación Física:
> 
> - **Siempre presente** en movimiento circular
> - **Perpendicular** a la velocidad instantánea
> - **Responsable** de la curvatura de la trayectoria
> - **Independiente** de si la velocidad aumenta o disminuye
> 
> ### Fórmulas Equivalentes:
> 
> - aₓ = v²/r
> - aₓ = ω²r
> - aₓ = 4π²r/T²
> - aₓ = (2πr/T)²/r
>
> [!warning] **Aceleración Total (a)** ⚡
> 
> ### Características Principales:
> 
> - **Composición vectorial**: \vec{a} = aₜ⃗ + aₓ⃗
> - **Magnitud**: |a| = √(aₜ² + aₓ²)
> - **Ángulo**: θ = arctan(aₜ/aₓ)
> 
> ### Casos Especiales:
> 
> - **Movimiento circular uniforme**: aₜ = 0, a = aₓ
> - **Arranque desde reposo**: aₜ ≠ 0, aₓ = 0 (inicialmente)
> - **Movimiento general**: aₜ ≠ 0, aₓ ≠ 0
>
> [!success] 🔗 Relaciones Fundamentales
> 
> ```mermaid
> graph TD
>     A[Aceleración Angular α] -->|aₜ = α × r| B[Aceleración Tangencial aₜ]
>     C[Velocidad Angular ω] -->|aₓ = ω²r| D[Aceleración Centrípeta aₓ]
>     B --> E[Aceleración Total a]
>     D --> E
>     E -->|a = √(aₜ² + aₓ²)| F[Magnitud Total]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#e8f5e8
>     style D fill:#fff3e0
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
> ```
>
> [!note] **Relaciones Matemáticas** 📐
> 
> ### Para Aceleración Tangencial:
> 
> - **aₜ = r × α**: Relación básica con aceleración angular
> - **aₜ = dv/dt**: Derivada de velocidad tangencial
> - **v = v₀ + aₜt**: Para aceleración tangencial constante
> 
> ### Para Aceleración Centrípeta:
> 
> - **aₓ = v²/r**: Usando velocidad tangencial
> - **aₓ = ω²r**: Usando velocidad angular
> - **aₓ = vω**: Forma alternativa útil

## 🎯 Estrategias de Resolución

> [!tip] **Método CART (Circular-Análisis-Relaciones-Total)** 🧠
> 
> ### **C**ircular - Identifica el sistema
> 
> 1. Reconoce si es movimiento circular
> 2. Identifica el radio de curvatura
> 3. Determina el centro de rotación
> 
> ### **A**nálisis - Clasifica el movimiento
> 
> 4. ¿Es uniforme o acelerado?
> 5. ¿Qué componentes están presentes?
> 6. ¿Cuáles son los datos conocidos?
> 
> ### **R**elaciones - Aplica fórmulas
> 
> 7. Calcula aₜ si hay cambio en |v|
> 8. Calcula aₓ si hay curvatura
> 9. Relaciona variables angulares y lineales
> 
> ### **T**otal - Encuentra la resultante
> 
> 10. Suma vectorialmente las componentes
> 11. Calcula magnitud y dirección
> 12. Verifica coherencia física

## 📚 Problemas Tipo

> [!example] **Problema 1: Rueda que Acelera** 🚗
> 
> ### Enunciado:
> 
> Una rueda de radio 0.3 m acelera desde reposo con α = 2 rad/s². Determina las aceleraciones tangencial, centrípeta y total de un punto en el borde cuando t = 3s.
> 
> ### Solución:
> 
> **Datos**:
> 
> - r = 0.3 m, α = 2 rad/s², t = 3s, ω₀ = 0
> 
> **Paso 1: Velocidad angular** ω = ω₀ + αt = 0 + 2(3) = 6 rad/s
> 
> **Paso 2: Aceleración tangencial** aₜ = α × r = 2 × 0.3 = **0.6 m/s²**
> 
> **Paso 3: Aceleración centrípeta** aₓ = ω²r = (6)² × 0.3 = **10.8 m/s²**
> 
> **Paso 4: Aceleración total** |a| = √(aₜ² + aₓ²) = √(0.6² + 10.8²) = **10.82 m/s²**
> 
> **Ángulo**: θ = arctan(aₜ/aₓ) = arctan(0.6/10.8) = **3.18°**
>
> [!example] **Problema 2: Satélite en Órbita** 🛰️
> 
> ### Enunciado:
> 
> Un satélite orbita la Tierra a 7500 m/s en una órbita circular de radio 7000 km. Si incrementa su velocidad a razón de 0.5 m/s², encuentra las componentes de aceleración.
> 
> ### Solución:
> 
> **Datos**:
> 
> - v = 7500 m/s, r = 7×10⁶ m, dv/dt = 0.5 m/s²
> 
> **Aceleración tangencial**: aₜ = dv/dt = **0.5 m/s²**
> 
> **Aceleración centrípeta**: aₓ = v²/r = (7500)²/(7×10⁶) = **8.04 m/s²**
> 
> **Aceleración total**: |a| = √(0.5² + 8.04²) = **8.06 m/s²**
> 
> **Interpretación**: La aceleración está dominada por la componente centrípeta.
>
> [!example] **Problema 3: Punto en Disco Rotatorio** 💿
> 
> ### Enunciado:
> 
> Un disco de 20 cm de radio gira según θ(t) = 2t³ + t². Encuentra las aceleraciones de un punto en el borde en t = 2s.
> 
> ### Solución:
> 
> **Función angular**: θ(t) = 2t³ + t² **Velocidad angular**: ω(t) = dθ/dt = 6t² + 2t **Aceleración angular**: α(t) = dω/dt = 12t + 2
> 
> **En t = 2s**:
> 
> - ω = 6(4) + 2(2) = **28 rad/s**
> - α = 12(2) + 2 = **26 rad/s²**
> 
> **Aceleraciones**:
> 
> - aₜ = αr = 26 × 0.2 = **5.2 m/s²**
> - aₓ = ω²r = (28)² × 0.2 = **156.8 m/s²**
> - |a| = √(5.2² + 156.8²) = **156.9 m/s²**

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "TANC"** 🎵 **T**angencial → **A**ltera magnitud **A**ngular → **N**o cambia dirección **N**ormal (centrípeta) → **C**ambia dirección constantemente **C**entrípeta → **C**entro siempre apunta
>
> [!tip] **Regla Visual: "Reloj de Aceleraciones"** 🕐
> 
> - **12:00** → aₓ (hacia centro)
> - **3:00** → aₜ (tangencial, si acelera)
> - **Resultado** → Vector suma (manecilla resultante)

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir direcciones**: aₓ siempre hacia el centro, aₜ siempre tangencial
> 2. **Olvidar aₓ en MCU**: Incluso con velocidad constante existe aceleración centrípeta
> 3. **Sumar escalares**: Las aceleraciones son vectores, se suman vectorialmente
> 4. **Confundir α y a**: α es angular, a es lineal
> 5. **Usar fórmulas incorrectas**: aₓ = v²/r, NO v/r
> 6. **Ignorar unidades**: Verificar consistencia dimensional

## 🎯 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Transporte:
> 
> - Análisis de curvas en carreteras y vías férreas
> - Diseño de rotondas y intercambiadores
> - Sistemas de frenado en vehículos
> 
> ### Maquinaria:
> 
> - Balanceado de rotores en motores
> - Diseño de centrifugadoras
> - Análisis de vibraciones en máquinas rotativas
> 
> ### Deportes:
> 
> - Lanzamiento de martillo y disco
> - Análisis de giros en patinaje artístico
> - Biomecánica de movimientos circulares
> 
> ### Astronomía:
> 
> - Órbitas planetarias y satelitales
> - Sistemas binarios de estrellas
> - Cálculo de trayectorias espaciales

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Cinemática Rotacional]] - Fundamentos teóricos
> - [[Problemas de Engranajes, Poleas y Transmisión de Movimiento]] - Aplicaciones
> - [[Problemas con Gráficas Angulares (θ-t, ω-t, α-t)]] - Análisis gráfico
> - [[Rodadura]] - Fuerzas en rotación

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Vectores]] - Suma vectorial y componentes
> - [[Cinemática Traslacional]] - Conceptos básicos de aceleración
> - [[Unidades y Magnitudes Físicas]] - Sistema de unidades

---

**Tags:** #cinematica-rotacional #aceleracion-tangencial #aceleracion-centripeta #movimiento-circular #fisica-mecanica #problemas #vectores #dinamica-rotacional
