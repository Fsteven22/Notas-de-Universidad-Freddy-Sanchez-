---
dg-publish: true
---

# Problemas de Torque (τ = F · d)

> [!quote] "El torque es la llave maestra que abre las puertas del movimiento rotacional; donde la fuerza encuentra su brazo de palanca, nace la rotación." 🔑
>
> [!info] El torque o momento de fuerza es la magnitud física que describe la tendencia de una fuerza a provocar una rotación alrededor de un eje. Su comprensión es fundamental para analizar el equilibrio rotacional y la dinámica de cuerpos rígidos en movimiento angular.

## 🔧 Fundamentos del Torque

> [!info] **Definición y Conceptos Básicos** ⚙️
> 
> ### Definición Matemática:
> 
> ```
> τ = F · d · sin θ
> τ = r × F  (producto vectorial)
> ```
> 
> Donde:
> 
> - **τ**: Torque o momento de fuerza (N·m)
> - **F**: Magnitud de la fuerza aplicada (N)
> - **d** o **r**: Distancia desde el eje de rotación al punto de aplicación (m)
> - **θ**: Ángulo entre la fuerza y el brazo de palanca
> 
> ### Características del Torque:
> 
> |Aspecto|Descripción|Unidad SI|
> |---|---|---|
> |Magnitud|τ = F·d·sin θ|N·m|
> |Dirección|Perpendicular al plano de rotación|---|
> |Sentido|Horario (-) / Antihorario (+)|---|
> |Naturaleza|Magnitud vectorial|Vector|
>
> [!tip] **Regla de la Mano Derecha** 👋
> 
> ### Para determinar la dirección del torque:
> 
> 1. **Dedos**: Apuntan en la dirección del vector posición (r)
> 2. **Doblar**: Hacia la dirección de la fuerza (F)
> 3. **Pulgar**: Indica la dirección del vector torque (τ)
> 
> ### Convención de signos:
> 
> - **Positivo (+)**: Rotación antihoraria (saliendo del plano)
> - **Negativo (-)**: Rotación horaria (entrando al plano)
>
> [!warning] **Brazo de Palanca o Brazo de Momento** ⚡
> 
> ### Definición:
> 
> El brazo de palanca es la **distancia perpendicular** desde el eje de rotación hasta la línea de acción de la fuerza.
> 
> ### Cálculo:
> 
> ```
> d_efectivo = r · sin θ
> ```
> 
> ### Casos Especiales:
> 
> - **θ = 90°**: d = r (máximo torque)
> - **θ = 0°**: d = 0 (torque nulo)
> - **θ = 180°**: d = 0 (torque nulo)

## 📐 Cálculo de Brazo de Palanca

> [!example] **Fuerza Perpendicular vs. Fuerza Inclinada** 📏
> 
> ### Caso 1: Fuerza Perpendicular (θ = 90°)
> 
> ```
> τ = F · r · sin(90°) = F · r
> ```
> 
> **Ventaja**: Máximo torque para una fuerza dada
> 
> ### Caso 2: Fuerza Inclinada (θ ≠ 90°)
> 
> ```
> τ = F · r · sin θ
> ```
> 
> **Componentes de la fuerza**:
> 
> - **F_tangencial = F · sin θ**: Contribuye al torque
> - **F_radial = F · cos θ**: No contribuye al torque
> 
> ### Comparación Visual:
> 
> ```mermaid
> graph LR
>     A[Fuerza Perpendicular] -->|τ = F·r| B[Torque Máximo]
>     C[Fuerza Inclinada] -->|τ = F·r·sin θ| D[Torque Reducido]
>     style A fill:#4caf50
>     style B fill:#81c784
>     style C fill:#ff9800
>     style D fill:#ffb74d
> ```
>
> [!example] **Uso de τ = F · r · sin θ** 🔄
> 
> ### Estrategia de Resolución:
> 
> 1. **Identificar el eje de rotación**
> 2. **Medir la distancia r** desde el eje al punto de aplicación
> 3. **Determinar el ángulo θ** entre F y r
> 4. **Aplicar la fórmula** τ = F · r · sin θ
> 5. **Asignar signo** según convención
> 
> ### Métodos Alternativos:
> 
> **Método 1: Componente perpendicular**
> 
> ```
> F_perp = F · sin θ
> τ = F_perp · r
> ```
> 
> **Método 2: Brazo de palanca efectivo**
> 
> ```
> d_efectivo = r · sin θ
> τ = F · d_efectivo
> ```
>
> [!example] **Ejemplo Resuelto: Fuerza a 30° sobre palanca de 50 cm** 🔧
> 
> ### Enunciado:
> 
> Una fuerza de 20 N se aplica a 30° respecto a una palanca de 50 cm de longitud. El eje de rotación está en un extremo de la palanca. Calcule el torque producido.
> 
> ### Datos:
> 
> - F = 20 N
> - r = 50 cm = 0.5 m
> - θ = 30°
> - Eje en el extremo de la palanca
> 
> ### Solución:
> 
> **Método directo**:
> 
> ```
> τ = F · r · sin θ
> τ = 20 N × 0.5 m × sin(30°)
> τ = 20 × 0.5 × 0.5
> τ = 5 N·m
> ```
> 
> **Verificación por componentes**:
> 
> ```
> F_tangencial = F · sin θ = 20 × sin(30°) = 10 N
> τ = F_tangencial × r = 10 N × 0.5 m = 5 N·m ✓
> ```
> 
> **Interpretación**: La fuerza produce un torque de 5 N·m en sentido antihorario.

## ⚙️ Torques Múltiples

> [!tip] **Varias Fuerzas Actuando sobre el Mismo Cuerpo** 🔄
> 
> ### Principio de Superposición:
> 
> El torque neto es la **suma algebraica** de todos los torques individuales:
> 
> ```
> τ_neto = Σ τᵢ = τ₁ + τ₂ + τ₃ + ... + τₙ
> ```
> 
> ### Procedimiento:
> 
> 1. **Calcular cada torque individualmente**
> 2. **Asignar signos** según convención
> 3. **Sumar algebraicamente** todos los torques
> 4. **Interpretar el resultado**:
>     - τ_neto > 0: Rotación antihoraria
>     - τ_neto < 0: Rotación horaria
>     - τ_neto = 0: Equilibrio rotacional
>
> [!example] **Ejemplo: Barra con Dos Fuerzas en Extremos Distintos** ⚖️
> 
> ### Enunciado:
> 
> Una barra uniforme de 2 m de longitud puede rotar alrededor de un eje en su centro. Se aplican dos fuerzas:
> 
> - F₁ = 15 N perpendicular en el extremo izquierdo (hacia abajo)
> - F₂ = 10 N perpendicular en el extremo derecho (hacia arriba)
> 
> Determine el torque neto y la dirección de rotación.
> 
> ### Datos:
> 
> - Longitud total: L = 2 m
> - Eje en el centro: r₁ = r₂ = 1 m
> - F₁ = 15 N (⊥, hacia abajo, extremo izquierdo)
> - F₂ = 10 N (⊥, hacia arriba, extremo derecho)
> 
> ### Solución:
> 
> **Análisis de cada torque**:
> 
> _Torque 1 (F₁)_:
> 
> ```
> τ₁ = F₁ × r₁ × sin(90°)
> τ₁ = 15 N × 1 m × 1 = 15 N·m
> ```
> 
> Sentido: **Horario → τ₁ = -15 N·m**
> 
> _Torque 2 (F₂)_:
> 
> ```
> τ₂ = F₂ × r₂ × sin(90°)
> τ₂ = 10 N × 1 m × 1 = 10 N·m
> ```
> 
> Sentido: **Horario → τ₂ = -10 N·m**
> 
> **Torque neto**:
> 
> ```
> τ_neto = τ₁ + τ₂ = (-15) + (-10) = -25 N·m
> ```
> 
> **Interpretación**:
> 
> - Magnitud: 25 N·m
> - Dirección: **Rotación horaria**
> - El extremo izquierdo baja, el derecho sube
>
> [!example] **Problema Avanzado: Sistema de Tres Fuerzas** 🔺
> 
> ### Enunciado:
> 
> En una barra de 3 m que rota alrededor de un punto a 1 m del extremo izquierdo, se aplican:
> 
> - F₁ = 20 N a 45° en el extremo izquierdo
> - F₂ = 30 N perpendicular hacia abajo en el centro de la barra
> - F₃ = 25 N perpendicular hacia arriba en el extremo derecho
> 
> ### Datos:
> 
> - L = 3 m, eje a 1 m del extremo izquierdo
> - F₁ = 20 N, θ₁ = 45°, r₁ = 1 m
> - F₂ = 30 N, θ₂ = 90°, r₂ = 0.5 m
> - F₃ = 25 N, θ₃ = 90°, r₃ = 2 m
> 
> ### Solución:
> 
> **Torque 1**:
> 
> ```
> τ₁ = F₁ · r₁ · sin θ₁ = 20 × 1 × sin(45°)
> τ₁ = 20 × 1 × 0.707 = 14.14 N·m (antihorario) → +14.14 N·m
> ```
> 
> **Torque 2**:
> 
> ```
> τ₂ = F₂ · r₂ · sin θ₂ = 30 × 0.5 × 1
> τ₂ = 15 N·m (horario) → -15 N·m
> ```
> 
> **Torque 3**:
> 
> ```
> τ₃ = F₃ · r₃ · sin θ₃ = 25 × 2 × 1
> τ₃ = 50 N·m (horario) → -50 N·m
> ```
> 
> **Torque neto**:
> 
> ```
> τ_neto = 14.14 + (-15) + (-50) = -50.86 N·m
> ```
> 
> **Resultado**: Rotación horaria con magnitud 50.86 N·m

## ⚖️ Equilibrio de Torques (Rotacional)

> [!success] **Condición de Equilibrio Rotacional** 🎯
> 
> ### Primera Condición: Suma de Torques = 0
> 
> ```
> Σ τ = 0
> τ₁ + τ₂ + τ₃ + ... + τₙ = 0
> ```
> 
> ### Significado Físico:
> 
> - **No hay rotación angular neta**
> - **El objeto permanece en reposo rotacional** o
> - **Mantiene velocidad angular constante**
> 
> ### Estrategia de Resolución:
> 
> 1. **Elegir un eje de rotación conveniente**
> 2. **Calcular todos los torques respecto a ese eje**
> 3. **Plantear la ecuación Σ τ = 0**
> 4. **Resolver para la incógnita**
>
> [!example] **Ejemplo: Viga Horizontal Sostenida por Cable** 🏗️
> 
> ### Enunciado:
> 
> Una viga uniforme de 4 m de longitud y 50 kg de masa está sostenida horizontalmente por un cable vertical en un extremo. En el otro extremo se coloca una carga de 80 kg. Determine la tensión en el cable.
> 
> ### Datos:
> 
> - Viga: L = 4 m, m_viga = 50 kg
> - Carga: m_carga = 80 kg (en extremo libre)
> - Cable: en un extremo (punto de apoyo)
> - g = 9.8 m/s²
> 
> ### Análisis:
> 
> **Fuerzas actuantes**:
> 
> - Peso de la viga: W_viga = mg = 50 × 9.8 = 490 N (en el centro de masa)
> - Peso de la carga: W_carga = mg = 80 × 9.8 = 784 N (en el extremo)
> - Tensión del cable: T (hacia arriba, en el punto de apoyo)
> 
> **Elección del eje**: En el punto de apoyo (donde está el cable)
> 
> ### Solución:
> 
> **Cálculo de torques respecto al punto de apoyo**:
> 
> _Torque del peso de la viga_:
> 
> ```
> τ_viga = W_viga × (L/2) = 490 N × 2 m = 980 N·m (horario)
> τ_viga = -980 N·m
> ```
> 
> _Torque del peso de la carga_:
> 
> ```
> τ_carga = W_carga × L = 784 N × 4 m = 3136 N·m (horario)
> τ_carga = -3136 N·m
> ```
> 
> _Torque de la tensión_:
> 
> ```
> τ_T = T × 0 = 0 N·m (fuerza aplicada en el eje)
> ```
> 
> **Condición de equilibrio**:
> 
> ```
> Σ τ = 0
> τ_viga + τ_carga + τ_T = 0
> -980 + (-3136) + 0 = 0
> ```
> 
> Esto no es correcto. **Replanteemos el problema**:
> 
> La tensión debe equilibrar ambos pesos, no generar torque.
> 
> **Equilibrio de fuerzas verticales**:
> 
> ```
> T = W_viga + W_carga
> T = 490 + 784 = 1274 N
> ```
> 
> **Verificación con torques respecto al punto medio**:
> 
> _Torque de la tensión_:
> 
> ```
> τ_T = T × 2 m = 1274 × 2 = 2548 N·m (antihorario) → +2548 N·m
> ```
> 
> _Torque del peso de la carga_:
> 
> ```
> τ_carga = 784 × 2 = 1568 N·m (horario) → -1568 N·m
> ```
> 
> _Torque del peso de la viga_:
> 
> ```
> τ_viga = 490 × 0 = 0 N·m (en el eje)
> ```
> 
> **Verificación**:
> 
> ```
> Σ τ = 2548 + (-1568) + 0 = 980 N·m ≠ 0
> ```
> 
> **Corrección del análisis**: Necesitamos considerar un punto de apoyo adicional o replantear el problema como una viga en voladizo.
>
> [!example] **Ejemplo Corregido: Viga en Equilibrio con Dos Apoyos** ⚖️
> 
> ### Enunciado Modificado:
> 
> Una viga de 4 m y 50 kg está apoyada en dos puntos: uno en A (a 1 m del extremo izquierdo) y otro en B (a 1 m del extremo derecho). Una carga de 80 kg se coloca en el extremo izquierdo. Determine las reacciones en los apoyos.
> 
> ### Datos:
> 
> - Viga: L = 4 m, m_viga = 50 kg
> - Apoyo A: a 1 m del extremo izquierdo
> - Apoyo B: a 3 m del extremo izquierdo (1 m del derecho)
> - Carga: 80 kg en extremo izquierdo
> 
> ### Solución:
> 
> **Cálculo de torques respecto al apoyo A**:
> 
> _Torque del peso de la carga (extremo izquierdo)_:
> 
> ```
> τ_carga = 784 N × 1 m = 784 N·m (horario) → -784 N·m
> ```
> 
> _Torque del peso de la viga (centro)_:
> 
> ```
> τ_viga = 490 N × 1 m = 490 N·m (horario) → -490 N·m
> ```
> 
> _Torque de la reacción en B_:
> 
> ```
> τ_B = R_B × 2 m (antihorario) → +2R_B
> ```
> 
> **Condición de equilibrio**:
> 
> ```
> Σ τ = 0
> -784 - 490 + 2R_B = 0
> 2R_B = 1274
> R_B = 637 N
> ```
> 
> **Equilibrio vertical**:
> 
> ```
> R_A + R_B = W_carga + W_viga
> R_A + 637 = 784 + 490
> R_A = 1274 - 637 = 637 N
> ```

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "FARDS"** 🎯
> 
> **F**uerza × **A**ngulo × **R**adio = **D**irección del **S**entido
> 
> - **F**: Identifica todas las fuerzas
> - **A**: Determina ángulos correctamente
> - **R**: Mide radios desde el eje
> - **D**: Aplica regla de la mano derecha
> - **S**: Suma algebraica de torques
>
> [!tip] **Regla Nemotécnica para el Signo** ↻↺
> 
> - **"Antihorario Arriba"** → Positivo (+)
> - **"Horario Hundido"** → Negativo (-)

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir distancia total con brazo de palanca efectivo**
> 2. **No aplicar correctamente sin θ** en fuerzas inclinadas
> 3. **Errores en la convención de signos** (horario/antihorario)
> 4. **Olvidar que fuerzas radiales no generan torque**
> 5. **No elegir el eje de rotación más conveniente**
> 6. **Confundir momento de fuerza con momento de inercia**
> 7. **No considerar el peso propio del objeto** en problemas de equilibrio
> 8. **Calcular torques respecto a diferentes ejes** simultáneamente

## 🎯 Casos Especiales del Torque

> [!info] **Situaciones Particulares** 🔄
> 
> ### Torque Nulo:
> 
> - **θ = 0°**: Fuerza radial (hacia o desde el eje)
> - **θ = 180°**: Fuerza radial opuesta
> - **F = 0**: Sin fuerza aplicada
> - **r = 0**: Fuerza aplicada en el eje
> 
> ### Torque Máximo:
> 
> - **θ = 90°**: Fuerza perpendicular al radio
> - **sin θ = 1**: Condición de máxima eficiencia
> 
> ### Torques Equivalentes:
> 
> Diferentes combinaciones de F, r, y θ pueden producir el mismo torque:
> 
> ```
> τ = F₁·r₁·sin θ₁ = F₂·r₂·sin θ₂
> ```

## 📊 Tabla de Referencia Rápida

> [!note] **Fórmulas y Conversiones** 📋
> 
> |Situación|Fórmula|Observaciones|
> |---|---|---|
> |Fuerza perpendicular|τ = F·r|θ = 90°, sin θ = 1|
> |Fuerza inclinada|τ = F·r·sin θ|0° < θ < 180°|
> |Brazo efectivo|τ = F·d_eff|d_eff = r·sin θ|
> |Componente tangencial|τ = F_tang·r|F_tang = F·sin θ|
> |Equilibrio rotacional|Σ τ = 0|Condición necesaria|
> |Múltiples torques|τ_neto = Σ τᵢ|Suma algebraica|

## 🔗 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Herramientas y Maquinaria:
> 
> - **Llaves de tuercas**: Maximizar torque con brazos largos
> - **Destornilladores**: Aplicar fuerza perpendicular
> - **Grúas**: Equilibrio de cargas y contrapesos
> 
> ### Construcción:
> 
> - **Vigas en equilibrio**: Cálculo de apoyos
> - **Estructuras**: Análisis de estabilidad rotacional
> - **Puentes**: Distribución de cargas
> 
> ### Deportes:
> 
> - **Palancas corporales**: Biomecánica del movimiento
> - **Bates y raquetas**: Optimización del golpe
> - **Gimnasia**: Control del momento angular
> 
> ### Vehículos:
> 
> - **Dirección**: Torque del volante
> - **Frenos**: Momento de frenado
> - **Motor**: Torque de salida

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Dinámica de Rotación]] - Aplicación del torque en movimiento
> - [[Equilibrio]] - Condiciones de equilibrio estático
> - [[Segunda ley de Newton para Rotación]] - τ = Iα
> - [[Momento de Inercia]] - Resistencia a la rotación
> - [[Vectores]] - Producto vectorial y dirección

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Análisis de fuerzas
> - [[Leyes de Newton]] - Fundamentos dinámicos
> - [[Trigonometría]] - Cálculo de componentes
> - [[Vectores]] - Operaciones vectoriales

---

**Tags:** #torque #momento-fuerza #equilibrio-rotacional #brazo-palanca #dinamica #rotacion #fisica-mecanica #estatica #problemas #fuerzas
