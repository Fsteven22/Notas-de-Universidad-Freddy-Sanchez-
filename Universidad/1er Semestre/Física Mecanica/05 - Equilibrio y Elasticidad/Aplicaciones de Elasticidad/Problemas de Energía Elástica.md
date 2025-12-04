# Problemas de Energía Elástica

> [!quote] "La energía elástica es la memoria silenciosa de la materia; cada deformación guarda la historia de las fuerzas que la crearon, esperando el momento perfecto para liberarse." 🔋

> [!info]- La energía elástica representa la capacidad de un material deformado para realizar trabajo al regresar a su forma original. Este concepto es fundamental en el análisis de sistemas mecánicos, desde resortes simples hasta estructuras complejas, y constituye un puente esencial entre la mecánica de sólidos y la conservación de energía.

## 🎯 Conceptos Fundamentales

> [!info]- **Energía de Deformación Elástica** ⚡
> 
> ### Definición:
> 
> La **energía de deformación elástica (U)** es la energía almacenada en un material cuando se deforma dentro de su límite elástico, y que puede recuperarse completamente al eliminar la carga.
> 
> ### Características:
> 
> - **Naturaleza**: Energía potencial almacenada
> - **Reversibilidad**: Completamente recuperable
> - **Dependencia**: Proporcional al cuadrado de la deformación
> - **Unidades**: Julios (J), N·m, kg·m²/s²
> 
> ### Principio Fundamental:
> 
> ```
> Trabajo aplicado = Energía almacenada (región elástica)
> W = U = ∫F dx = ∫σ dε · V
> ```

> [!tip]- **Energía en Diferentes Tipos de Deformación** 🔧
> 
> ### **Tracción/Compresión Uniaxial**:
> 
> **U = ½·F·δ = ½·k·δ² = ½·σ·ε·V**
> 
> Donde:
> 
> - F: Fuerza aplicada
> - δ: Deformación total
> - k: Rigidez del elemento
> - σ: Esfuerzo uniforme
> - ε: Deformación unitaria
> - V: Volumen del elemento
> 
> ### **Flexión Pura**:
> 
> **U = M²·L/(2·E·I)**
> 
> Donde:
> 
> - M: Momento flector
> - L: Longitud del elemento
> - E: Módulo de Young
> - I: Momento de inercia
> 
> ### **Torsión**:
> 
> **U = T²·L/(2·G·J)**
> 
> Donde:
> 
> - T: Torque aplicado
> - G: Módulo de rigidez
> - J: Momento polar de inercia

> [!warning]- **Densidad de Energía de Deformación** 📊
> 
> ### Definición:
> 
> **u = U/V = ½·σ·ε = σ²/(2·E) = ½·E·ε²**
> 
> ### Interpretación Física:
> 
> - **Unidades**: J/m³, Pa
> - **Significado**: Energía almacenada por unidad de volumen
> - **Máximo**: En el límite elástico
> - **Distribución**: Varía según el campo de esfuerzos
> 
> ### Para Estado Multiaxial:
> 
> **u = ½·[σ₁·ε₁ + σ₂·ε₂ + σ₃·ε₃ + τ₁₂·γ₁₂ + τ₂₃·γ₂₃ + τ₁₃·γ₁₃]**

> [!success] 🔄 Métodos de Cálculo de Energía Elástica
> 
> ```mermaid
> graph TD
>     A[Energía Elástica] --> B[Método Directo]
>     A --> C[Método del Trabajo]
>     A --> D[Método de Integración]
>     
>     B --> E[U = ½·F·δ]
>     C --> F[W = ∫F·dx]
>     D --> G[U = ∫u·dV]
>     
>     E --> H[Resortes y Barras]
>     F --> I[Cargas Variables]
>     G --> J[Campos de Esfuerzo]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
> ```

> [!note]- **Relaciones Energéticas Fundamentales** 📐
> 
> ### Para Elementos Estructurales:
> 
> #### **Barra en Tracción/Compresión**:
> 
> ```
> U = ∫₀ᴸ (F²)/(2·E·A) dx
> 
> Para F y A constantes: U = F²·L/(2·E·A)
> ```
> 
> #### **Viga en Flexión**:
> 
> ```
> U = ∫₀ᴸ (M²)/(2·E·I) dx
> 
> Para momento constante: U = M²·L/(2·E·I)
> ```
> 
> #### **Eje en Torsión**:
> 
> ```
> U = ∫₀ᴸ (T²)/(2·G·J) dx
> 
> Para torque constante: U = T²·L/(2·G·J)
> ```
> 
> ### Energía de Resortes:
> 
> #### **Resorte Lineal**:
> 
> **U = ½·k·x²**
> 
> #### **Resorte Torsional**:
> 
> **U = ½·k_θ·θ²**

## 🎯 Estrategias de Resolución

> [!tip]- **Método EDEN (Energía-Deformación-Equilibrio-Naturaleza)** 🌱
> 
> ### **E**nergía - Identifica el tipo de energía
> 
> 1. Determina el tipo de deformación presente
> 2. Identifica si hay múltiples modos de deformación
> 3. Establece las condiciones de carga
> 
> ### **D**eformación - Analiza la geometría y cargas
> 
> 4. Calcula esfuerzos y deformaciones
> 5. Determina la distribución espacial
> 6. Verifica que se mantenga en rango elástico
> 
> ### **E**quilibrio - Aplica principios energéticos
> 
> 7. Usa el principio de conservación de energía
> 8. Aplica teoremas energéticos (Castigliano, etc.)
> 9. Considera cargas dinámicas si aplica
> 
> ### **N**aturaleza - Interpreta resultados físicos
> 
> 10. Verifica la coherencia dimensional
> 11. Compara con casos conocidos
> 12. Analiza la distribución de energía

## 📚 Problemas Tipo

> [!example]- **Problema 1: Resorte Simple** 🌀
> 
> ### Enunciado:
> 
> Un resorte con constante k = 500 N/m se comprime 8 cm desde su posición natural. Determina: a) La energía elástica almacenada b) La fuerza necesaria para esta compresión c) El trabajo realizado si se comprime 4 cm adicionales
> 
> ### Solución:
> 
> **Datos**:
> 
> - k = 500 N/m
> - x₁ = 8 cm = 0.08 m
> - x₂ = 12 cm = 0.12 m
> 
> **a) Energía almacenada inicial**: U₁ = ½·k·x₁² = ½·500·(0.08)² = 1.6 J
> 
> **b) Fuerza para compresión de 8 cm**: F = k·x₁ = 500·0.08 = 40 N
> 
> **c) Trabajo adicional**: U₂ = ½·k·x₂² = ½·500·(0.12)² = 3.6 J W_adicional = U₂ - U₁ = 3.6 - 1.6 = 2.0 J
> 
> **Verificación**: W = ∫F dx = ∫₀.₀₈^₀.₁² 500x dx = 250[x²]₀.₀₈^₀.₁² = 2.0 J ✓

> [!example]- **Problema 2: Barra en Tracción** 📏
> 
> ### Enunciado:
> 
> Una barra de acero de 2 m de longitud y 20 mm de diámetro está sometida a una fuerza de tracción de 15 kN. Si E = 200 GPa, determina: a) La energía de deformación almacenada b) La densidad de energía c) El alargamiento de la barra
> 
> ### Solución:
> 
> **Datos**:
> 
> - L = 2 m
> - d = 20 mm = 0.02 m
> - F = 15 kN = 15,000 N
> - E = 200 GPa = 200×10⁹ Pa
> 
> **Área transversal**: A = π·d²/4 = π·(0.02)²/4 = 3.14×10⁻⁴ m²
> 
> **a) Energía de deformación**: U = F²·L/(2·E·A) = (15,000)²·2/(2·200×10⁹·3.14×10⁻⁴) = 3.58 J
> 
> **b) Densidad de energía**: σ = F/A = 15,000/(3.14×10⁻⁴) = 47.8×10⁶ Pa u = σ²/(2·E) = (47.8×10⁶)²/(2·200×10⁹) = 5.72×10³ J/m³
> 
> **c) Alargamiento**: δ = F·L/(E·A) = 15,000·2/(200×10⁹·3.14×10⁻⁴) = 0.478 mm
> 
> **Verificación**: U = ½·F·δ = ½·15,000·0.478×10⁻³ = 3.58 J ✓

> [!example]- **Problema 3: Viga en Flexión** 🏗️
> 
> ### Enunciado:
> 
> Una viga simplemente apoyada de longitud L = 4 m tiene una sección rectangular de 200 mm × 300 mm. Está sometida a una carga puntual P = 20 kN en el centro. Si E = 30 GPa, calcula: a) La energía de deformación total b) La deflexión máxima usando métodos energéticos
> 
> ### Solución:
> 
> **Datos**:
> 
> - L = 4 m
> - b = 200 mm = 0.2 m
> - h = 300 mm = 0.3 m
> - P = 20 kN = 20,000 N
> - E = 30 GPa = 30×10⁹ Pa
> 
> **Momento de inercia**: I = b·h³/12 = 0.2·(0.3)³/12 = 4.5×10⁻⁴ m⁴
> 
> **Diagrama de momentos**: Para 0 ≤ x ≤ L/2: M(x) = P·x/2 Para L/2 ≤ x ≤ L: M(x) = P·(L-x)/2
> 
> **a) Energía de deformación**: U = (1/(2·E·I))·∫₀ᴸ M² dx = (2/(2·E·I))·∫₀ᴸ/² (P·x/2)² dx
> 
> U = (P²/(4·E·I))·∫₀ᴸ/² x² dx = (P²/(4·E·I))·[x³/3]₀ᴸ/²
> 
> U = (P²·L³)/(48·E·I) = (20,000)²·(4)³/(48·30×10⁹·4.5×10⁻⁴) = 395 J
> 
> **b) Deflexión máxima (Teorema de Castigliano)**: δₘₐₓ = ∂U/∂P = (P·L³)/(24·E·I) = 20,000·(4)³/(24·30×10⁹·4.5×10⁻⁴) = 39.5 mm

> [!example]- **Problema 4: Sistema de Resortes** 🔗
> 
> ### Enunciado:
> 
> Dos resortes están conectados: uno en serie (k₁ = 300 N/m) y otro en paralelo (k₂ = 200 N/m) con una masa m = 5 kg. Si el sistema se desplaza 10 cm de su posición de equilibrio, determina: a) La constante equivalente b) La energía total almacenada c) La distribución de energía en cada resorte
> 
> ### Solución:
> 
> **Datos**:
> 
> - k₁ = 300 N/m, k₂ = 200 N/m
> - m = 5 kg
> - x = 10 cm = 0.1 m
> 
> **a) Constante equivalente**: Para resortes en paralelo: k_eq = k₁ + k₂ = 300 + 200 = 500 N/m
> 
> **b) Energía total**: U_total = ½·k_eq·x² = ½·500·(0.1)² = 2.5 J
> 
> **c) Distribución de energía**:
> 
> - Fuerza total: F = k_eq·x = 500·0.1 = 50 N
> - En resorte 1: F₁ = k₁·x = 300·0.1 = 30 N → U₁ = ½·k₁·x² = 1.5 J
> - En resorte 2: F₂ = k₂·x = 200·0.1 = 20 N → U₂ = ½·k₂·x² = 1.0 J
> 
> **Verificación**: U₁ + U₂ = 1.5 + 1.0 = 2.5 J = U_total ✓

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "ELASTICO"** 🔄
> 
> **E**nergía = ½ × fuerza × desplazamiento **L**a densidad = σ²/(2E) para tracción **A**lmacenada completamente recuperable **S**iempre proporcional al cuadrado **T**rabajo igual a energía (proceso cuasiestático) **I**ntegración para distribuciones variables **C**astigliano para deflexiones **O**rden: U = ½kx² para resortes

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir energía de deformación con trabajo total** en procesos irreversibles
> 2. **No considerar todos los modos de deformación** en elementos complejos
> 3. **Usar fórmulas incorrectas** para diferentes tipos de carga
> 4. **Ignorar la distribución no uniforme** de esfuerzos
> 5. **No verificar que el material permanezca elástico** durante todo el proceso
> 6. **Confundir constantes de resortes** en serie vs paralelo
> 7. **Errores en la integración** de campos de esfuerzo variables
> 8. **No considerar efectos dinámicos** cuando corresponde

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Ingeniería Automotriz:
> 
> - Sistemas de suspensión y amortiguadores
> - Barras de torsión en chasis
> - Elementos de absorción de impacto
> 
> ### Energías Renovables:
> 
> - Almacenamiento de energía en volantes
> - Mecanismos de tensión en aerogeneradores
> - Sistemas de recuperación de energía
> 
> ### Construcción:
> 
> - Análisis de deflexiones en puentes
> - Diseño sísmico de estructuras
> - Sistemas de aislamiento de vibraciones
> 
> ### Biomecánica:
> 
> - Energía almacenada en tendones
> - Mecanismos de salto en animales
> - Prótesis con devolución de energía

## 📊 Datos de Referencia

> [!note]- **Capacidades de Almacenamiento Energético**
> 
> ### Materiales Comunes:
> 
> |Material|Densidad Energía Máx (MJ/m³)|Aplicación Típica|
> |---|---|---|
> |Acero al carbono|0.4|Resortes automotrices|
> |Aleaciones de titanio|1.0|Aplicaciones aeroespaciales|
> |Fibra de carbono|25|Elementos de alta performance|
> |Caucho natural|1.5|Amortiguadores, sellos|
> |Aleaciones con memoria|10|Actuadores, dispositivos médicos|
> 
> ### Eficiencias Típicas:
> 
> - **Resortes metálicos**: 95-98%
> - **Materiales compuestos**: 90-95%
> - **Elementos estructurales**: 85-90%
> - **Sistemas con fricción**: 70-85%

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Elasticidad]] - Fundamentos teóricos
> - [[Trabajo y Energía]] - Principios energéticos generales
> - [[Problemas de Deformación por Tensión y Compresión (Ley de Hooke)]] - Casos básicos
> - [[Principios de Conservación de la Energía]] - Aplicación en sistemas mecánicos

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Vectores]] - Para análisis de fuerzas y desplazamientos
> - [[Unidades y Magnitudes Físicas]] - Sistema de unidades
> - [[Trabajo y Energía]] - Conceptos fundamentales de energía

---

**Tags:** #energia-elastica #deformacion #elasticidad #resortes #energia-potencial #trabajo #metodos-energeticos #castigliano #vibraciones #almacenamiento-energia