# Problemas de Variación de Momentum en Sistemas Aislados

> [!quote] "En un sistema aislado, el momentum total permanece constante; esta conservación es la clave para resolver las colisiones más complejas." 🎯

> [!info]- Los problemas de variación de momentum en sistemas aislados constituyen el corazón del análisis de colisiones y explosiones. A través de la aplicación del principio de conservación del momentum lineal, podemos predecir y analizar el comportamiento de sistemas donde no actúan fuerzas externas netas.

## 🎯 Conceptos Fundamentales

> [!info]- **Sistema Aislado** 🔒
> 
> ### Características Principales:
> 
> - **Definición**: Sistema donde la suma de fuerzas externas es nula (ΣF_ext = 0)
> - **Conservación**: El momentum total del sistema permanece constante
> - **Ecuación**: p⃗_inicial = p⃗_final
> - **Aplicación**: Válida en colisiones, explosiones y desintegraciones
> 
> ### Condiciones del Sistema:
> 
> |Tipo de Sistema|Características|Momentum Total|Energía Cinética|
> |---|---|---|---|
> |Perfectamente aislado|ΣF_ext = 0|Se conserva|Puede cambiar|
> |Cuasi-aislado|F_ext << F_int|Aproximadamente constante|Variable|
> |Con fricción despreciable|μ ≈ 0|Se conserva|Se conserva (elástico)|
> |Con fuerzas internas únicamente|Solo F_int actúan|Constante|Variable según tipo|

> [!tip]- **Tipos de Colisiones** 💥
> 
> ### Clasificación por Conservación de Energía:
> 
> #### **Colisiones Elásticas**:
> 
> - Se conserva momentum: Σp⃗_i = Σp⃗_f
> - Se conserva energía cinética: ΣK_i = ΣK_f
> - Coeficiente de restitución: e = 1
> 
> #### **Colisiones Inelásticas**:
> 
> - Se conserva momentum: Σp⃗_i = Σp⃗_f
> - NO se conserva energía cinética: ΣK_f < ΣK_i
> - Coeficiente de restitución: 0 < e < 1
> 
> #### **Colisiones Perfectamente Inelásticas**:
> 
> - Se conserva momentum: Σp⃗_i = Σp⃗_f
> - Máxima pérdida de energía cinética
> - Los objetos quedan unidos: v⃗_f1 = v⃗_f2
> - Coeficiente de restitución: e = 0

> [!warning]- **Explosiones y Desintegraciones** 💥
> 
> ### Características:
> 
> - **Estado inicial**: Objeto en reposo o con velocidad conocida
> - **Proceso**: Fuerzas internas separan las partes
> - **Conservación**: Momentum total antes = Momentum total después
> - **Energía**: Aumenta la energía cinética total (liberación de energía interna)
> 
> ### Ecuaciones Principales:
> 
> - **Momentum inicial**: p⃗_i = m_total × v⃗_inicial
> - **Momentum final**: p⃗_f = m₁v⃗₁ + m₂v⃗₂ + ... + mₙv⃗ₙ
> - **Conservación**: p⃗_i = p⃗_f

> [!success] 🔗 Relaciones Matemáticas Fundamentales
> 
> ```mermaid
> graph TD
>     A[Sistema Aislado] -->|ΣF_ext = 0| B[Conservación de Momentum]
>     B --> C[Momentum Inicial = Momentum Final]
>     C --> D[m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f]
>     D --> E{Tipo de Colisión}
>     E -->|Elástica| F[Conserva K también]
>     E -->|Inelástica| G[No conserva K]
>     E -->|Perfectamente Inelástica| H[v₁f = v₂f]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
> ```

> [!note]- **Coeficiente de Restitución** 🔄
> 
> ### Definición:
> 
> e = -(velocidad relativa de separación)/(velocidad relativa de aproximación)
> 
> ### Fórmula:
> 
> e = -(v₂f - v₁f)/(v₂i - v₁i)
> 
> ### Interpretación:
> 
> - **e = 1**: Colisión perfectamente elástica
> - **0 < e < 1**: Colisión inelástica
> - **e = 0**: Colisión perfectamente inelástica
> - **e > 1**: Colisión "superelástica" (poco común, con aporte de energía)

## 🎯 Estrategias de Resolución

> [!tip]- **Método SICE (Sistema-Inicial-Conservación-Ecuaciones)** 🧠
> 
> ### **S**istema - Define el sistema aislado
> 
> 1. Identifica todos los objetos involucrados
> 2. Verifica que ΣF_ext = 0 o sea despreciable
> 3. Define el sistema de coordenadas
> 
> ### **I**nicial - Estado antes de la interacción
> 
> 4. Lista masas y velocidades iniciales
> 5. Calcula el momentum inicial total
> 6. Determina la energía cinética inicial (si es necesaria)
> 
> ### **C**onservación - Aplica principios
> 
> 7. Aplica conservación de momentum
> 8. Verifica si se conserva energía cinética
> 9. Considera el coeficiente de restitución si es dado
> 
> ### **E**cuaciones - Resuelve el sistema
> 
> 10. Plantea las ecuaciones necesarias
> 11. Resuelve el sistema de ecuaciones
> 12. Verifica la coherencia física de los resultados

## 📚 Problemas Tipo

> [!example]- **Problema 1: Colisión Perfectamente Inelástica** 🚗
> 
> ### Enunciado:
> 
> Un automóvil de 1200 kg que viaja a 25 m/s hacia el este colisiona con un camión de 3000 kg en reposo. Después de la colisión, ambos vehículos se mueven juntos. Encuentra: a) La velocidad final del sistema b) La energía cinética perdida
> 
> ### Solución:
> 
> **Datos**:
> 
> - m₁ = 1200 kg, v₁ᵢ = 25 m/s
> - m₂ = 3000 kg, v₂ᵢ = 0 m/s
> - Colisión perfectamente inelástica: v₁f = v₂f = vf
> 
> **a) Velocidad final**:
> 
> Conservación de momentum: m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)vf
> 
> (1200)(25) + (3000)(0) = (1200 + 3000)vf 30,000 = 4200 vf **vf = 7.14 m/s hacia el este**
> 
> **b) Energía cinética perdida**:
> 
> Kᵢ = ½m₁v₁ᵢ² = ½(1200)(25)² = 375,000 J Kf = ½(m₁ + m₂)vf² = ½(4200)(7.14)² = 107,143 J
> 
> **ΔK = Kf - Kᵢ = -267,857 J** (energía perdida)

> [!example]- **Problema 2: Colisión Elástica Unidimensional** ⚡
> 
> ### Enunciado:
> 
> Una pelota de 0.5 kg moviéndose a 8 m/s colisiona elásticamente con otra pelota de 1.0 kg inicialmente en reposo. Determina las velocidades finales de ambas pelotas.
> 
> ### Solución:
> 
> **Datos**:
> 
> - m₁ = 0.5 kg, v₁ᵢ = 8 m/s
> - m₂ = 1.0 kg, v₂ᵢ = 0 m/s
> - Colisión elástica (e = 1)
> 
> **Ecuaciones**:
> 
> Conservación de momentum: m₁v₁ᵢ = m₁v₁f + m₂v₂f 0.5(8) = 0.5v₁f + 1.0v₂f 4 = 0.5v₁f + v₂f ... (1)
> 
> Coeficiente de restitución: e = -(v₂f - v₁f)/(v₂ᵢ - v₁ᵢ) = 1 -(v₂f - v₁f)/(0 - 8) = 1 v₂f - v₁f = 8 ... (2)
> 
> **Resolución**: De (2): v₂f = v₁f + 8 Sustituyendo en (1): 4 = 0.5v₁f + v₁f + 8 -4 = 1.5v₁f **v₁f = -2.67 m/s** (rebota) **v₂f = 5.33 m/s** (se mueve hacia adelante)

> [!example]- **Problema 3: Explosión Unidimensional** 💥
> 
> ### Enunciado:
> 
> Un cohete de 1000 kg inicialmente en reposo explota en dos fragmentos. El fragmento de 600 kg se mueve hacia el norte a 50 m/s. Encuentra la velocidad del fragmento restante.
> 
> ### Solución:
> 
> **Datos**:
> 
> - m_total = 1000 kg, v_inicial = 0 m/s
> - m₁ = 600 kg, v₁f = 50 m/s (norte)
> - m₂ = 400 kg, v₂f = ?
> 
> **Conservación de momentum**:
> 
> p_inicial = p_final 0 = m₁v₁f + m₂v₂f 0 = (600)(50) + (400)v₂f -30,000 = 400v₂f **v₂f = -75 m/s** (hacia el sur)
> 
> **Verificación**: El fragmento más pequeño se mueve más rápido, lo cual es físicamente consistente.

> [!example]- **Problema 4: Colisión Bidimensional** 🎱
> 
> ### Enunciado:
> 
> Una bola de billar de 0.2 kg moviéndose a 4 m/s hacia el este colisiona con otra bola idéntica en reposo. Después de la colisión, la primera bola se mueve a 2 m/s formando 30° con su dirección original. Encuentra la velocidad y dirección de la segunda bola (colisión elástica).
> 
> ### Solución:
> 
> **Datos**:
> 
> - m₁ = m₂ = 0.2 kg
> - v₁ᵢ = 4 m/s (este), v₂ᵢ = 0
> - v₁f = 2 m/s a 30° norte del este
> - Colisión elástica
> 
> **Componentes**:
> 
> **Conservación de momentum en x**: m₁v₁ᵢ = m₁v₁f cos(30°) + m₂v₂f cos(θ) 0.2(4) = 0.2(2)(√3/2) + 0.2v₂f cos(θ) 4 = √3 + v₂f cos(θ) ... (1)
> 
> **Conservación de momentum en y**: 0 = m₁v₁f sen(30°) + m₂v₂f sen(θ) 0 = 0.2(2)(1/2) + 0.2v₂f sen(θ) v₂f sen(θ) = -1 ... (2)
> 
> **Conservación de energía cinética**: ½m₁v₁ᵢ² = ½m₁v₁f² + ½m₂v₂f² 16 = 4 + v₂f² **v₂f = 2√3 ≈ 3.46 m/s**
> 
> De (2): sen(θ) = -1/3.46 = -0.289 **θ = -16.8°** (sur del este)

## 🧮 Técnicas Avanzadas

> [!tip]- **Método del Centro de Masa** 🎯
> 
> Para sistemas complejos, el análisis desde el sistema de referencia del centro de masa simplifica los cálculos:
> 
> **Centro de masa**: r⃗_CM = (m₁r⃗₁ + m₂r⃗₂)/(m₁ + m₂) **Velocidad del CM**: v⃗_CM = (m₁v⃗₁ + m₂v⃗₂)/(m₁ + m₂)
> 
> ### Ventajas:
> 
> - En el sistema CM, el momentum total es siempre cero
> - Las colisiones elásticas son simétricas respecto al CM
> - Simplifica el análisis de colisiones bidimensionales

> [!tip]- **Análisis Energético** ⚡
> 
> ### Factor Q (Energía liberada/absorbida):
> 
> Q = Kf - Kᵢ
> 
> - **Q > 0**: Reacción exotérmica (explosión)
> - **Q = 0**: Colisión elástica
> - **Q < 0**: Colisión inelástica (energía absorbida)
> 
> ### Eficiencia de la colisión:
> 
> η = Kf/Kᵢ
> 
> - **η = 1**: Colisión perfectamente elástica
> - **η < 1**: Colisión inelástica
> - **η > 1**: Proceso explosivo

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **No verificar si el sistema es realmente aislado** antes de aplicar conservación
> 2. **Confundir momentum con energía cinética** en la conservación
> 3. **Ignorar la naturaleza vectorial del momentum** en problemas 2D
> 4. **Asumir que toda colisión es elástica** sin verificar las condiciones
> 5. **No considerar los signos** en colisiones unidimensionales
> 6. **Aplicar conservación de energía cinética** en colisiones inelásticas
> 7. **Malinterpretar el coeficiente de restitución** y sus valores límite

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Ingeniería Automotriz:
> 
> - Diseño de sistemas de seguridad (airbags, zonas de deformación)
> - Análisis de pruebas de choque
> - Optimización de estructuras para absorber impactos
> 
> ### Deportes:
> 
> - Análisis de colisiones en deportes de contacto
> - Optimización de equipos deportivos (pelotas, raquetas)
> - Biomecánica de movimientos explosivos
> 
> ### Física Nuclear:
> 
> - Análisis de reacciones nucleares
> - Detectores de partículas
> - Aceleradores de partículas
> 
> ### Astronomía:
> 
> - Colisiones de asteroides y meteoritos
> - Formación planetaria
> - Análisis de sistemas binarios

## 📖 Referencias y Notas Relacionadas

> [!quote]- **Notas Relacionadas**
> 
> - [[Momentum Lineal y Su Conservación]] - Fundamentos teóricos
> - [[Choques Uni-Bidimensionales]] - Análisis detallado de colisiones
> - [[Impulso Lineal]] - Relación entre impulso y cambio de momentum
> - [[Centro de masa (CM)]] - Análisis desde el sistema CM
> - [[Problemas de Colisiones]] - Ejercicios adicionales

## 🔧 Formulario de Consulta Rápida

> [!note]- **Ecuaciones Esenciales**
> 
> ### Conservación de Momentum:
> 
> - **General**: Σp⃗ᵢ = Σp⃗f
> - **Dos objetos**: m₁v⃗₁ᵢ + m₂v⃗₂ᵢ = m₁v⃗₁f + m₂v⃗₂f
> 
> ### Coeficiente de Restitución:
> 
> - **Definición**: e = -(v₂f - v₁f)/(v₂ᵢ - v₁ᵢ)
> - **Rango**: 0 ≤ e ≤ 1
> 
> ### Colisión Elástica (1D):
> 
> - v₁f = [(m₁-m₂)v₁ᵢ + 2m₂v₂ᵢ]/(m₁+m₂)
> - v₂f = [(m₂-m₁)v₂ᵢ + 2m₁v₁ᵢ]/(m₁+m₂)
> 
> ### Colisión Perfectamente Inelástica:
> 
> - vf = (m₁v₁ᵢ + m₂v₂ᵢ)/(m₁+m₂)

---

**Tags:** #momentum #conservacion #colisiones #sistemas-aislados #fisica-mecanica #impulso #dinamica #choques #explosiones #coeficiente-restitucion