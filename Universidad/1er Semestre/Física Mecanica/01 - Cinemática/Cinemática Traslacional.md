# Cinemática Traslacional 🚗

> [!quote] _"El movimiento es relativo, pero las leyes que lo gobiernan son absolutas. La cinemática nos enseña a describir el 'cómo' del movimiento antes de preguntarnos el 'por qué'."_ - Galileo Galilei

---

## 📋 Conceptos Fundamentales

> [!info]- 🎯 **Definición de Cinemática Traslacional** La cinemática traslacional estudia el movimiento de los cuerpos en línea recta (unidimensional) o en el plano/espacio (bidimensional/tridimensional) sin considerar las causas que producen dicho movimiento.
> 
> **Características principales:**
> 
> - Se enfoca en describir el movimiento, no en explicar sus causas
> - Variables principales: posición, velocidad y aceleración
> - El tiempo es el parámetro independiente
> - Los objetos se consideran partículas puntuales

## 🔢 Variables Cinemáticas Fundamentales

> [!tip]- 📍 **Posición (x, r)** **Definición:** Ubicación de un objeto en el espacio respecto a un sistema de referencia.
> 
> **Características:**
> 
> - En 1D: $x(t)$ - coordenada en una línea
> - En 2D/3D: $r⃗(t) = x(t)î + y(t)ĵ + z(t)k̂$
> - **Desplazamiento:** $Δx = x_f - x_i$ (cambio de posición)
> - **Distancia:** Longitud total recorrida (siempre positiva)
> 
> **Unidades:** metros (m), kilómetros (km), centímetros (cm)

> [!tip]- ⚡ **Velocidad (v)** **Definición:** Razón de cambio de la posición con respecto al tiempo.
> 
> **Velocidad promedio:** $$\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$$
> 
> **Velocidad instantánea:** $$v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$$
> 
> **Características:**
> 
> - Es una cantidad vectorial (tiene magnitud y dirección)
> - **Rapidez:** Magnitud de la velocidad (escalar)
> - Unidades: m/s, km/h, cm/s

> [!tip]- 🚀 **Aceleración (a)** **Definición:** Razón de cambio de la velocidad con respecto al tiempo.
> 
> **Aceleración promedio:** $$\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i}$$
> 
> **Aceleración instantánea:** $$a = \lim_{\Delta t \to 0} \frac{\Delta v}{\Delta t} = \frac{dv}{dt} = \frac{d^2x}{dt^2}$$
> 
> **Interpretación:**
> 
> - a > 0: Aceleración (aumenta velocidad)
> - a < 0: Desaceleración (disminuye velocidad)
> - a = 0: Velocidad constante
> - Unidades: m/s², km/h², cm/s²

## 📊 Ecuaciones de la Cinemática

> [!warning]- 🧮 **Ecuaciones para Aceleración Constante (MRUA)** Estas cinco ecuaciones describen completamente el movimiento rectilíneo uniformemente acelerado:
> 
> |Ecuación|Fórmula|Variables ausentes|
> |---|---|---|
> |**Velocidad-tiempo**|$v = v_0 + at$|No incluye x|
> |**Posición-tiempo**|$x = x_0 + v_0t + \frac{1}{2}at^2$|No incluye v|
> |**Velocidad-posición**|$v^2 = v_0^2 + 2a(x-x_0)$|No incluye t|
> |**Posición promedio**|$x = x_0 + \frac{(v_0 + v)t}{2}$|No incluye a|
> |**Posición desde reposo**|$x = x_0 + \frac{1}{2}at^2$|Para v₀ = 0|
> 
> **Variables:**
> 
> - x₀, v₀ = posición y velocidad inicial
> - x, v = posición y velocidad final
> - a = aceleración constante
> - t = tiempo

## 📈 Tipos de Movimiento Traslacional

> [!info]- 🔄 **Clasificación del Movimiento**
> 
> ```mermaid
> graph TD
>    A[Movimiento Traslacional] --> B[Rectilíneo]
>    A --> C[Curvilíneo]
>    
>    B --> D[MRU: Velocidad constante]
>    B --> E[MRUA: Aceleración constante]
>    B --> F[MRV: Aceleración variable]
>    
>    C --> G[Parabólico]
>    C --> H[Circular]
>    C --> I[Elíptico]
>    
>    D --> J[v = constante, a = 0]
>    E --> K[a = constante ≠ 0]
>    F --> L[a = fx variable]
>    
>    style A fill:#e1f5fe
>    style B fill:#f3e5f5
>    style C fill:#fff3e0
>    style D fill:#e8f5e8
>    style E fill:#fce4ec
>    style F fill:#f1f8e9
> ```

> [!tip]- 🎯 **Movimiento Rectilíneo Uniforme (MRU)** **Características:**
> 
> - Velocidad constante (a = 0)
> - La gráfica x vs t es una línea recta
> - Ecuación: x = x₀ + vt
> 
> **Ejemplos:** Tren en vía recta, luz en el vacío

> [!tip]- 🎯 **Movimiento Rectilíneo Uniformemente Acelerado (MRUA)** **Características:**
> 
> - Aceleración constante (a ≠ 0)
> - La gráfica v vs t es una línea recta
> - La gráfica x vs t es una parábola
> 
> **Ejemplos:** Caída libre, auto acelerando uniformemente

## 🧠 Técnica de Estudio: Método VEXAT

> [!tip]- 🎓 **Estrategia de Aprendizaje: Mnemotecnia VEXAT** Para resolver problemas de cinemática, usa el método **VEXAT**:
> 
> **V - Variables** conocidas e incógnitas **E - Ecuación** apropiada a usar **X - eXaminar** el tipo de movimiento **A - Aplicar** la fórmula correcta **T - Todos** los valores deben tener unidades correctas
> 
> **Tabla de decisión para elegir ecuaciones:**
> 
> |Si necesitas encontrar|Y conoces|Usa la ecuación|
> |---|---|---|
> |v|v₀, a, t|v = v₀ + at|
> |x|v₀, a, t|x = x₀ + v₀t + ½at²|
> |v|v₀, a, x|v² = v₀² + 2a(x-x₀)|
> |x|v₀, v, t|x = x₀ + (v₀+v)t/2|
> |t|v₀, v, a|t = (v-v₀)/a|

## 🧪 Casos Especiales Importantes

> [!example]- 🍎 **Caída Libre** **Definición:** Movimiento bajo la influencia exclusiva de la gravedad.
> 
> **Características:**
> 
> - Aceleración: a = g = 9.8 m/s² (hacia abajo)
> - Ecuaciones de MRUA con a = -g (si y⁺ es hacia arriba)
> - Tiempo de subida = tiempo de bajada
> - Velocidad inicial = -velocidad final (en mismo punto)
> 
> **Ecuaciones especiales:**
> 
> - Altura máxima: $h_{max} = \frac{v_0^2}{2g}$
> - Tiempo total de vuelo: $t_{total} = \frac{2v_0}{g}$
> - Tiempo para alcanzar altura h: $t = \frac{v_0 \pm \sqrt{v_0^2 - 2gh}}{g}$

> [!example]- 🚗 **Frenado de Vehículos** **Problema típico:** Un auto viaja a 72 km/h y frena con desaceleración constante hasta detenerse en 50 m.
> 
> **Solución paso a paso:**
> 
> 1. **Convertir unidades:** $72 km/h = 20 m/s$
> 2. **Identificar variables:** $v₀ = 20 m/s, v = 0, x = 50 m$
> 3. **Elegir ecuación:** $v² = v₀² + 2ax$
> 4. **Resolver:** $0² = 20² + 2a(50) → a = -4 m/s²$
> 5. **Tiempo:** $t = (v-v₀)/a = (0-20)/(-4) = 5 s$

## 📊 Interpretación de Gráficas

> [!warning]- 📈 **Análisis Gráfico del Movimiento**
> 
> **Gráfica Posición vs Tiempo (x-t):**
> 
> - Pendiente = velocidad instantánea
> - Línea recta = velocidad constante
> - Curva = aceleración presente
> - Pendiente horizontal = reposo
> 
> **Gráfica Velocidad vs Tiempo (v-t):**
> 
> - Pendiente = aceleración instantánea
> - Área bajo la curva = desplazamiento
> - Línea recta = aceleración constante
> - Línea horizontal = MRU
> 
> **Gráfica Aceleración vs Tiempo (a-t):**
> 
> - Área bajo la curva = cambio de velocidad
> - Línea horizontal = MRUA
> - a = 0 = MRU

## 🔍 Referencias y Conexiones

> [!quote]- 📚 **Referencias a otras notas**
> 
> - [[Cinemática Rotacional]] - Movimiento angular, analogías
> - [[Vectores]] - Para movimiento en 2D y 3D
> - [[01 - Derivada y Definición Formal]] - Definiciones de velocidad y aceleración
> - [[01 - Antiderivadas (Primitivas)]] - Para recuperar posición desde aceleración
> - [[Leyes de Newton]] - Causas del movimiento (dinámica)

## 📖 Notas Recomendadas para Complementar

> [!info]- 🎯 **Prerrequisitos y Temas Relacionados**
> 
> **Prerrequisitos esenciales:**
> 
> - [[Álgebra]] - Manipulación de ecuaciones
> - [[Funciones]] - Conceptos de función del tiempo
> - [[Gráficas]] - Interpretación de gráficas x-t, v-t, a-t
> - [[Vectores]] - Para movimiento bidimensional
> 
> **Temas complementarios:**
> 
> - [[Movimiento Parabólico]] - Extensión 2D
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Causas del movimiento
> - [[Trabajo y Energía]] - Enfoque energético del movimiento
> - [[Momentum Lineal y Su Conservación]] - Conservación en colisiones

## 🎮 Simulación Mental de Problemas

> [!tip]- 🧩 **Técnica de Visualización** Para cada problema, construye mentalmente:
> 
> 1. **🎬 La "película" del movimiento:**
> 
> - ¿El objeto acelera, desacelera o mantiene velocidad?
>     
> - ¿Cambia de dirección?
>     
> - ¿Cuál es el estado inicial y final?
>     
> 
> 2. **📊 Los gráficos esperados:**
> 
> - ¿Cómo se vería la gráfica x-t?
>     
> - ¿Y la gráfica v-t?
>     
> - ¿La aceleración es positiva, negativa o cero?
>     
> 
> 3. **🔢 El resultado razonable:**
> 
> - ¿El resultado tiene sentido físicamente?
> - ¿Las unidades son correctas?
> - ¿El orden de magnitud es razonable?

---

**Tags:** #fisica-mecanica #cinematica #movimiento-rectilineo #mrua #mru #caida-libre #graficas-cinematicas #ecuaciones-movimiento