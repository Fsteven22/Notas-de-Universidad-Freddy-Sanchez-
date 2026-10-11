---
dg-publish: true
---

# Problemas de Trabajo

> [!quote] "El trabajo es la medida del cambio; cada fuerza que actúa sobre un desplazamiento cuenta una historia de energía transferida." 💪
>
> [!info] El trabajo es una magnitud escalar que representa la transferencia de energía cuando una fuerza actúa sobre un objeto que se desplaza. Comprender cómo calcular el trabajo en diferentes situaciones es fundamental para analizar sistemas mecánicos y aplicar el teorema trabajo-energía.

## ⚡ Fundamentos del Trabajo

> [!info] **Definición General de Trabajo** 💼
> 
> ### Concepto Fundamental:
> 
> **W = \vec{F} · \vec{d} = Fd cos θ**
> 
> - **W**: Trabajo realizado (Joules)
> - **F**: Magnitud de la fuerza (N)
> - **d**: Magnitud del desplazamiento (m)
> - **θ**: Ángulo entre fuerza y desplazamiento
> 
> ### Características del Trabajo:
> 
> |Condición|Trabajo|Interpretación|
> |---|---|---|
> |θ = 0°|W = Fd|Fuerza en dirección del movimiento|
> |θ = 90°|W = 0|Fuerza perpendicular al movimiento|
> |θ = 180°|W = -Fd|Fuerza opuesta al movimiento|
> |0° < θ < 90°|W > 0|Trabajo positivo (motor)|
> |90° < θ < 180°|W < 0|Trabajo negativo (resistivo)|
>
> [!tip] **Teorema Trabajo-Energía** ⚖️
> 
> ### Relación Fundamental:
> 
> **W_total = ΔE_cinética = ½mv²_f - ½mv²_i**
> 
> ### Implicaciones:
> 
> - **W_total > 0**: El objeto acelera
> - **W_total < 0**: El objeto desacelera
> - **W_total = 0**: Velocidad constante
> - **W_neto = Σ W_individual**: Suma de todos los trabajos
>
> [!success] 🔗 Clasificación de Problemas
> 
> ```mermaid
> graph TD
>     A[Problemas de Trabajo] --> B[Fuerzas Constantes]
>     A --> C[Fuerzas Variables]
>     B --> B1[Fuerza Única]
>     B --> B2[Múltiples Fuerzas]
>     B --> B3[Planos Inclinados]
>     B --> B4[Fricción]
>     C --> C1[Resortes: F = -kx]
>     C --> C2[Gravitación: F ∝ 1/r²]
>     C --> C3["Funciones Generales: F(x)"]
>     C --> C4[Integrales Definidas]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
> ```

## 🔧 Trabajo con Fuerzas Constantes

> [!info] **Características de Fuerzas Constantes** ⭐
> 
> ### Definición:
> 
> Una fuerza es **constante** cuando su magnitud y dirección no cambian durante el desplazamiento.
> 
> ### Fórmula Básica:
> 
> **W = \vec{F} · \vec{d} = Fd cos θ**
> 
> ### Casos Comunes:
> 
> - **Peso**: W = mgh (movimiento vertical)
> - **Fricción**: W = -μmg·d (superficie horizontal)
> - **Fuerza aplicada**: W = F·d·cos θ
> - **Tensión en cuerda**: W = T·d·cos θ
>
> [!tip] **Estrategia para Fuerzas Constantes** 🎯
> 
> ### Método "FADE":
> 
> **F**uerza - Identifica todas las fuerzas actuantes **A**ngulo - Determina θ entre cada fuerza y desplazamiento  
> **D**esplazamiento - Calcula la distancia recorrida **E**valuación - Aplica W = Fd cos θ para cada fuerza
>
> [!example] **Problema 1: Trabajo con Múltiples Fuerzas** 🚛
> 
> ### Enunciado:
> 
> Un bloque de 10 kg se arrastra 5 m sobre una superficie horizontal con μ = 0.3, aplicando una fuerza de 80 N a 37° sobre la horizontal. Calcula: a) El trabajo de cada fuerza b) El trabajo total c) La velocidad final si partió del reposo
> 
> ### Solución:
> 
> **Datos**: m = 10 kg, d = 5 m, μ = 0.3, F = 80 N, θ = 37°
> 
> **Fuerzas actuantes**:
> 
> - Peso: W = mg = 98 N (vertical hacia abajo)
> - Normal: N = mg - F sen 37° = 98 - 48 = 50 N
> - Fricción: f = μN = 0.3 × 50 = 15 N (opuesta al movimiento)
> - Aplicada: F = 80 N a 37°
> 
> **a) Trabajo de cada fuerza**:
> 
> - W_peso = mg·d·cos 90° = 0 J (⊥ al desplazamiento)
> - W_normal = N·d·cos 90° = 0 J (⊥ al desplazamiento)
> - W_fricción = f·d·cos 180° = 15×5×(-1) = **-75 J**
> - W_aplicada = F·d·cos 37° = 80×5×0.8 = **320 J**
> 
> **b) Trabajo total**: W_total = 0 + 0 + (-75) + 320 = **245 J**
> 
> **c) Velocidad final**: W_total = ½mv²_f - 0 245 = ½(10)v²_f **v_f = 7 m/s**
>
> [!example] **Problema 2: Plano Inclinado** 🏔️
> 
> ### Enunciado:
> 
> Un objeto de 5 kg se desliza 10 m hacia abajo por un plano inclinado de 30° con μ = 0.2. Determina: a) El trabajo del peso b) El trabajo de la fricción c) El trabajo total d) La aceleración del objeto
> 
> ### Solución:
> 
> **Datos**: m = 5 kg, d = 10 m, θ = 30°, μ = 0.2, g = 9.8 m/s²
> 
> **Análisis de fuerzas**:
> 
> - Componente del peso paralela: mg sen 30° = 5×9.8×0.5 = 24.5 N
> - Normal: N = mg cos 30° = 5×9.8×0.866 = 42.4 N
> - Fricción: f = μN = 0.2×42.4 = 8.48 N (hacia arriba)
> 
> **a) Trabajo del peso**: W_peso = (mg sen 30°)·d = 24.5×10 = **245 J**
> 
> **b) Trabajo de la fricción**: W_fricción = -f·d = -8.48×10 = **-84.8 J**
> 
> **c) Trabajo total**: W_total = 245 + (-84.8) = **160.2 J**
> 
> **d) Aceleración**: F_neta = mg sen 30° - f = 24.5 - 8.48 = 16.02 N **a = F_neta/m = 16.02/5 = 3.2 m/s²**
>
> [!example] **Problema 3: Sistema de Poleas** 🔗
> 
> ### Enunciado:
> 
> En un sistema de polea fija, una persona eleva un objeto de 20 kg una altura de 3 m aplicando una fuerza de 250 N. Si el proceso toma 5 s, calcula: a) El trabajo realizado por la persona b) El trabajo realizado por el peso c) La potencia desarrollada
> 
> ### Solución:
> 
> **Datos**: m = 20 kg, h = 3 m, F_persona = 250 N, t = 5 s
> 
> **a) Trabajo de la persona**: La persona jala la cuerda la misma distancia que sube el objeto W_persona = F_persona × h = 250 × 3 = **750 J**
> 
> **b) Trabajo del peso**: El peso se opone al movimiento hacia arriba W_peso = -mgh = -20×9.8×3 = **-588 J**
> 
> **c) Potencia desarrollada**: P = W_persona/t = 750/5 = **150 W**
> 
> **Verificación**: El trabajo neto (750-588 = 162 J) se convierte en energía cinética del objeto.

## 📈 Trabajo con Fuerzas Variables

> [!warning] **Características de Fuerzas Variables** 📊
> 
> ### Definición:
> 
> Una fuerza es **variable** cuando su magnitud y/o dirección cambia durante el desplazamiento.
> 
> ### Fórmula Integral:
> 
> **W = ∫\vec{F} · d\vec{r} = ∫F(x) dx** (en una dimensión)
> 
> ### Interpretación Gráfica:
> 
> El trabajo es el **área bajo la curva** F vs x
> 
> ### Casos Frecuentes:
> 
> - **Resortes**: F = -kx → W = ½kx²
> - **Gravitación**: F = GMm/r² → W = GMm(1/r₁ - 1/r₂)
> - **Resistencia del aire**: F ∝ v² → Requiere integración
>
> [!tip] **Estrategia para Fuerzas Variables** 🧮
> 
> ### Método "VIGA":
> 
> **V**ariable - Identifica la función F(x) **I**ntegral - Plantea ∫F(x) dx entre límites **G**ráfica - Visualiza como área bajo curva  
> **A**plicación - Evalúa la integral definida
>
> [!example] **Problema 4: Trabajo con Resorte** 🔗
> 
> ### Enunciado:
> 
> Un resorte con constante k = 400 N/m se comprime desde su longitud natural hasta 0.25 m de compresión. Luego se comprime hasta 0.4 m adicionales. Calcula: a) El trabajo para la primera compresión b) El trabajo para la segunda compresión c) El trabajo total
> 
> ### Solución:
> 
> **Datos**: k = 400 N/m, x₁ = 0.25 m, x₂ = 0.25 + 0.4 = 0.65 m
> 
> **Fuerza del resorte**: F(x) = -kx (signo negativo porque se opone) **Fuerza aplicada**: F_aplicada(x) = +kx (para comprimir)
> 
> **a) Trabajo primera compresión (0 → 0.25 m)**: W₁ = ∫₀^{0.25} kx dx = k∫₀^{0.25} x dx = k[x²/2]₀^{0.25} W₁ = 400 × (0.25)²/2 = 400 × 0.03125 = **12.5 J**
> 
> **b) Trabajo segunda compresión (0.25 → 0.65 m)**: W₂ = ∫₀.₂₅^{0.65} kx dx = k[x²/2]₀.₂₅^{0.65} W₂ = 400/2 × [(0.65)² - (0.25)²] = 200 × [0.4225 - 0.0625] W₂ = 200 × 0.36 = **72 J**
> 
> **c) Trabajo total**: W_total = W₁ + W₂ = 12.5 + 72 = **84.5 J**
> 
> **Verificación**: W_total = ½k(0.65)² = ½×400×0.4225 = **84.5 J** ✓
>
> [!example] **Problema 5: Fuerza Dependiente de la Posición** 📐
> 
> ### Enunciado:
> 
> Una partícula se mueve bajo la acción de una fuerza F(x) = 2x² + 3x (en Newtons) desde x = 1 m hasta x = 4 m. Calcula: a) El trabajo realizado b) Si la masa es 0.5 kg y parte del reposo, ¿cuál es su velocidad final?
> 
> ### Solución:
> 
> **Datos**: F(x) = 2x² + 3x N, x₁ = 1 m, x₂ = 4 m, m = 0.5 kg
> 
> **a) Trabajo realizado**: W = ∫₁⁴ F(x) dx = ∫₁⁴ (2x² + 3x) dx W = ∫₁⁴ 2x² dx + ∫₁⁴ 3x dx W = [2x³/3]₁⁴ + [3x²/2]₁⁴ W = (2/3)[4³ - 1³] + (3/2)[4² - 1²] W = (2/3)[64 - 1] + (3/2)[16 - 1] W = (2/3)(63) + (3/2)(15) W = 42 + 22.5 = **64.5 J**
> 
> **b) Velocidad final**: Por teorema trabajo-energía: W = ½mv²_f - 0 64.5 = ½(0.5)v²_f v²_f = 64.5/0.25 = 258 **v_f = 16.1 m/s**
>
> [!example] **Problema 6: Trabajo Gravitatorio** 🌍
> 
> ### Enunciado:
> 
> Un satélite de 1000 kg se mueve desde una órbita de radio R = 7×10⁶ m hasta 2R = 1.4×10⁷ m desde el centro de la Tierra. Calcula el trabajo realizado contra la gravedad. (G = 6.67×10⁻¹¹ N⋅m²/kg², M_T = 6×10²⁴ kg)
> 
> ### Solución:
> 
> **Datos**: m = 1000 kg, r₁ = 7×10⁶ m, r₂ = 1.4×10⁷ m
> 
> **Fuerza gravitatoria**: F(r) = -GMm/r²
> 
> **Trabajo contra la gravedad**: W = -∫ᵣ₁^ᵣ₂ F(r) dr = ∫ᵣ₁^ᵣ₂ GMm/r² dr W = GMm ∫ᵣ₁^ᵣ₂ r⁻² dr = GMm[-r⁻¹]ᵣ₁^ᵣ₂ W = GMm[-1/r₂ - (-1/r₁)] = GMm(1/r₁ - 1/r₂)
> 
> **Sustituyendo valores**: W = (6.67×10⁻¹¹)(6×10²⁴)(1000)[1/(7×10⁶) - 1/(1.4×10⁷)] W = 4×10¹⁷[1.43×10⁻⁷ - 7.14×10⁻⁸] W = 4×10¹⁷ × 7.16×10⁻⁸ **W = 2.86×10¹⁰ J = 28.6 GJ**

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "TRABAJO"** 📝
> 
> **T**ransferencia - El trabajo transfiere energía **R**ecorrido - Debe haber desplazamiento  
> **A**ngulo - cos θ determina la componente efectiva **B**ajo la curva - Área en gráfico F vs x **A**plicada - Solo la componente en dirección del movimiento **J**oules - Unidad de energía y trabajo **O**posición - Trabajo negativo cuando F opone el movimiento
>
> [!tip] **Fórmulas Clave** 🔑
> 
> ### Fuerzas Constantes:
> 
> - **General**: W = Fd cos θ
> - **Peso**: W = mgh (vertical)
> - **Fricción**: W = -μmgd (horizontal)
> 
> ### Fuerzas Variables:
> 
> - **Resorte**: W = ½k(x₂² - x₁²)
> - **Gravitación**: W = GMm(1/r₁ - 1/r₂)
> - **General**: W = ∫F(x) dx

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir fuerza con trabajo**: W ≠ F (el trabajo incluye desplazamiento)
> 2. **Olvidar el ángulo**: No aplicar cos θ entre fuerza y desplazamiento
> 3. **Signo del trabajo**: No considerar si la fuerza ayuda u opone el movimiento
> 4. **Distancia vs desplazamiento**: Usar la distancia correcta según la fuerza
> 5. **Fuerzas perpendiculares**: Asumir que hacen trabajo cuando W = 0
> 6. **Integración incorrecta**: Errores en límites o evaluación de integrales
> 7. **Unidades inconsistentes**: Mezclar N⋅m con otros sistemas de unidades

## 🎯 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Ingeniería Mecánica:
> 
> - Cálculo de potencia en motores
> - Diseño de sistemas de transmisión
> - Análisis de eficiencia energética
> 
> ### Construcción:
> 
> - Trabajo de grúas y montacargas
> - Cálculo de energía en demoliciones
> - Sistemas de poleas y aparejos
> 
> ### Deportes:
> 
> - Análisis biomecánico del rendimiento
> - Cálculo de energía en saltos y lanzamientos
> - Optimización de técnicas deportivas
> 
> ### Tecnología:
> 
> - Almacenamiento en baterías y resortes
> - Sistemas de propulsión espacial
> - Mecanismos de precisión

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Trabajo y Energía]] - Conceptos fundamentales
> - [[Principio de energía]] - Base teórica
> - [[Potencia y Gradiente de Potencial]] - Extensiones del concepto
> - [[Problemas de Conservación de Energía Mecánica]] - Aplicaciones complementarias

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Vectores]] - Para producto escalar y componentes
> - [[Leyes de Newton]] - Análisis de fuerzas
> - [[Cinemática Traslacional]] - Conceptos de desplazamiento
> - [[Unidades y Magnitudes Físicas]] - Sistema internacional

---

**Tags:** #trabajo #energia #fuerzas-constantes #fuerzas-variables #integral #trabajo-energia #fisica-mecanica #potencia #resortes #gravitacion
