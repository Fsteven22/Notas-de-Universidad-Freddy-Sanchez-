# Problemas de Cuerpos Rígidos en Sistemas con Poleas

> [!quote] "Las poleas no solo cambian la dirección de las fuerzas; revelan la elegante danza entre la dinámica traslacional y rotacional en perfecta armonía." ⚙️

> [!info]- Los sistemas de poleas representan una aplicación fundamental de la dinámica de cuerpos rígidos, donde se combinan los movimientos de traslación y rotación. Estos problemas integran conceptos de torque, momento de inercia, y las leyes de Newton tanto para traslación como para rotación.

## 🔧 Fundamentos de Sistemas con Poleas

> [!info]- **Componentes del Sistema** ⚙️
> 
> ### Elementos Principales:
> 
> - **Polea**: Disco rígido que puede rotar alrededor de un eje fijo
> - **Cuerda/Cable**: Elemento flexible que transmite tensión
> - **Masas**: Objetos conectados al sistema mediante la cuerda
> - **Soporte**: Estructura que mantiene el eje de rotación
> 
> ### Características de las Poleas:
> 
> |Tipo de Polea|Momento de Inercia|Aplicación|
> |---|---|---|
> |Disco sólido|I = ½MR²|Poleas macizas|
> |Aro/Anillo|I = MR²|Poleas huecas|
> |Cilindro hueco|I = ½M(R₁² + R₂²)|Poleas con grosor|
> |Disco con agujero|I = ½M(R₂² + r²)|Poleas perforadas|

> [!tip]- **Condiciones de Rodadura sin Deslizamiento** 🎯
> 
> ### Relación Cinemática Fundamental:
> 
> ```
> v = ωR
> a = αR
> ```
> 
> Donde:
> 
> - **v**: velocidad lineal de la cuerda
> - **ω**: velocidad angular de la polea
> - **a**: aceleración lineal de la cuerda
> - **α**: aceleración angular de la polea
> - **R**: radio de la polea
> 
> ### Interpretación Física:
> 
> - La cuerda no resbala sobre la polea
> - Cada punto de la cuerda mantiene contacto con la polea
> - La velocidad tangencial de la polea = velocidad de la cuerda

> [!warning]- **Análisis de Fuerzas y Torques** ⚡
> 
> ### Para las Masas (Dinámica Traslacional):
> 
> **Masa colgante**:
> 
> ```
> ΣF = ma
> mg - T = ma
> ```
> 
> **Masa en plano inclinado**:
> 
> ```
> mg sin θ - T - f = ma
> ```
> 
> ### Para la Polea (Dinámica Rotacional):
> 
> ```
> Στ = Iα
> TR = Iα
> ```
> 
> ### Tensiones en la Cuerda:
> 
> - **Cuerda masiva**: T₁ ≠ T₂ (tensión variable)
> - **Cuerda ideal**: T₁ = T₂ = T (tensión constante)

> [!success] 🔗 Estrategia de Resolución
> 
> ```mermaid
> graph TD
>     A[Identificar Sistema] -->|1| B[Diagrama de Cuerpo Libre]
>     B -->|2| C[Ecuaciones de Movimiento]
>     C -->|3| D[Condiciones de Enlace]
>     D -->|4| E[Sistema de Ecuaciones]
>     E -->|5| F[Resolución Matemática]
>     F -->|6| G[Verificación Física]
>     
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#fff3e0
>     style D fill:#e8f5e8
>     style E fill:#fce4ec
>     style F fill:#f1f8e9
>     style G fill:#e0f2f1
> ```

> [!note]- **Ecuaciones de Conservación** 📐
> 
> ### Conservación de la Energía:
> 
> ```
> E₀ = Ef
> mgh₀ + ½mv₀² + ½Iω₀² = mghf + ½mvf² + ½Iωf²
> ```
> 
> ### Conservación del Momentum Angular:
> 
> Para sistemas aislados:
> 
> ```
> L₀ = Lf
> mvR + Iω = constante
> ```

## 🎯 Metodología PRADA

> [!tip]- **Método PRADA (Polea-Restricción-Análisis-Dinámica-Aplicación)** 🧠
> 
> ### **P**olea - Caracterización
> 
> 1. Identifica el tipo y geometría de la polea
> 2. Determina el momento de inercia
> 3. Establece el radio efectivo
> 
> ### **R**estricción - Condiciones de enlace
> 
> 4. Aplica la condición de no deslizamiento
> 5. Relaciona velocidades y aceleraciones
> 6. Considera restricciones geométricas
> 
> ### **A**nálisis - Fuerzas y torques
> 
> 7. Dibuja diagramas de cuerpo libre
> 8. Identifica todas las fuerzas
> 9. Calcula torques respecto al eje de rotación
> 
> ### **D**inámica - Ecuaciones de movimiento
> 
> 10. Aplica las leyes de Newton
> 11. Escribe ecuaciones de rotación
> 12. Sistema de ecuaciones simultáneas
> 
> ### **A**plicación - Resolución y verificación
> 
> 13. Resuelve el sistema de ecuaciones
> 14. Verifica coherencia física
> 15. Interpreta resultados en contexto

## 📚 Problemas Tipo

> [!example]- **Problema 1: Polea Simple con Masa Colgante** 🏗️
> 
> ### Enunciado:
> 
> Una polea de masa M = 2 kg y radio R = 0.3 m (disco sólido) tiene una cuerda inextensible que pasa por su borde. De un extremo cuelga una masa m = 1 kg. Si el sistema parte del reposo, determina: a) La aceleración de la masa b) La tensión en la cuerda c) La velocidad de la masa después de descender 2 m
> 
> ### Solución:
> 
> **Datos**:
> 
> - M = 2 kg, R = 0.3 m, m = 1 kg
> - I = ½MR² = ½(2)(0.3)² = 0.09 kg⋅m²
> 
> **Análisis de fuerzas**:
> 
> _Para la masa_:
> 
> ```
> mg - T = ma
> (1)(9.8) - T = (1)a
> 9.8 - T = a ... (1)
> ```
> 
> _Para la polea_:
> 
> ```
> τ = Iα
> TR = Iα = I(a/R)
> T(0.3) = (0.09)(a/0.3)
> T = 0.3a ... (2)
> ```
> 
> **Resolución**:
> 
> Sustituyendo (2) en (1):
> 
> ```
> 9.8 - 0.3a = a
> 9.8 = 1.3a
> a = 7.54 m/s²
> ```
> 
> ```
> T = 0.3(7.54) = 2.26 N
> ```
> 
> **Para v después de 2 m**:
> 
> ```
> v² = v₀² + 2as = 0 + 2(7.54)(2) = 30.16
> v = 5.49 m/s
> ```

> [!example]- **Problema 2: Sistema de Doble Polea** ⚙️⚙️
> 
> ### Enunciado:
> 
> Dos poleas idénticas (M = 3 kg, R = 0.4 m, discos sólidos) están conectadas por una cuerda. De la primera cuelga una masa m₁ = 2 kg y de la segunda una masa m₂ = 4 kg. Determina la aceleración del sistema y las tensiones.
> 
> ### Solución:
> 
> **Datos**:
> 
> - M = 3 kg, R = 0.4 m para ambas poleas
> - I = ½MR² = ½(3)(0.4)² = 0.24 kg⋅m² (cada polea)
> - m₁ = 2 kg, m₂ = 4 kg
> 
> **Análisis**:
> 
> Como m₂ > m₁, m₂ desciende y m₁ asciende.
> 
> _Para m₁_ (asciende):
> 
> ```
> T₁ - m₁g = m₁a
> T₁ - 19.6 = 2a ... (1)
> ```
> 
> _Para m₂_ (desciende):
> 
> ```
> m₂g - T₂ = m₂a
> 39.2 - T₂ = 4a ... (2)
> ```
> 
> _Para cada polea_:
> 
> ```
> T₁R = Iα₁ → T₁ = 0.6α₁ = 0.6(a/0.4) = 1.5a
> T₂R = Iα₂ → T₂ = 1.5a
> ```
> 
> **Sistema**:
> 
> ```
> 1.5a - 19.6 = 2a → a = -19.6/0.5 = -39.2 m/s²
> ```
> 
> Esto indica error en el análisis. Corrigiendo:
> 
> _Considerando la cuerda conectora_: El sistema actúa como uno solo:
> 
> ```
> (m₂ - m₁)g = (m₁ + m₂ + 2I/R²)a
> (4 - 2)(9.8) = (2 + 4 + 2(0.24)/(0.4)²)a
> 19.6 = (6 + 3)a = 9a
> a = 2.18 m/s²
> ```

> [!example]- **Problema 3: Polea en Plano Inclinado** 🔺
> 
> ### Enunciado:
> 
> Una polea (M = 1.5 kg, R = 0.25 m, disco sólido) está en la cima de un plano inclinado de 30°. Una cuerda pasa por la polea: un extremo tiene masa m₁ = 2 kg sobre el plano (μ = 0.2) y el otro extremo tiene masa m₂ = 3 kg colgando verticalmente. Determina la aceleración del sistema.
> 
> ### Solución:
> 
> **Datos**:
> 
> - M = 1.5 kg, R = 0.25 m
> - I = ½MR² = ½(1.5)(0.25)² = 0.047 kg⋅m²
> - m₁ = 2 kg, m₂ = 3 kg, θ = 30°, μ = 0.2
> 
> **Análisis de fuerzas**:
> 
> _Para m₁ en el plano_:
> 
> ```
> N = m₁g cos θ = (2)(9.8)(cos 30°) = 16.97 N
> f = μN = (0.2)(16.97) = 3.39 N
> 
> T₁ - m₁g sin θ - f = m₁a
> T₁ - (2)(9.8)(0.5) - 3.39 = 2a
> T₁ - 13.19 = 2a ... (1)
> ```
> 
> _Para m₂ colgante_:
> 
> ```
> m₂g - T₂ = m₂a
> 29.4 - T₂ = 3a ... (2)
> ```
> 
> _Para la polea_ (asumiendo T₁ = T₂ = T):
> 
> ```
> τ = 0 (polea ideal)
> T₁ = T₂ = T
> ```
> 
> _Considerando inercia de la polea_:
> 
> ```
> (T₂ - T₁)R = Iα
> Como T₁ ≈ T₂, consideramos T promedio
> TR = I(a/R)
> T = Ia/R² = (0.047)a/(0.25)² = 0.75a
> ```
> 
> **Sistema final**:
> 
> ```
> 0.75a - 13.19 = 2a ... (1')
> 29.4 - 0.75a = 3a ... (2')
> 
> De (2'): 29.4 = 3.75a → a = 7.84 m/s²
> ```

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "TORPE"** 🔄
> 
> **T**ensión = fuerza en la cuerda **O**mega (ω) = velocidad angular **R**adio = conecta lineal y angular **P**olea = objeto que rota **E**nlace = v = ωR (condición clave)

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Ignorar la inercia de la polea** y tratarla como ideal
> 2. **Confundir direcciones** de rotación y traslación
> 3. **No aplicar correctamente** la condición v = ωR
> 4. **Asumir tensiones iguales** cuando la polea tiene masa
> 5. **Olvidar fuerzas de fricción** en planos inclinados
> 6. **Usar momento de inercia incorrecto** para la geometría
> 7. **No considerar todas las fuerzas** en los diagramas

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Construcción e Ingeniería:
> 
> - Grúas y sistemas de elevación
> - Ascensores y montacargas
> - Sistemas de transmisión por poleas
> 
> ### Maquinaria Industrial:
> 
> - Bandas transportadoras
> - Sistemas de transmisión en fábricas
> - Maquinaria textil y de producción
> 
> ### Deportes y Recreación:
> 
> - Sistemas de poleas en gimnasios
> - Equipos de escalada y rappel
> - Mecanismos en parques de diversiones
> 
> ### Automóviles:
> 
> - Sistema de dirección asistida
> - Transmisión por correas
> - Sistemas de frenos

## 📊 Tabla de Momentos de Inercia

> [!note]- **Referencia Rápida** 📋
> 
> |Geometría|Momento de Inercia|Aplicación|
> |---|---|---|
> |Disco sólido|I = ½MR²|Poleas macizas|
> |Aro delgado|I = MR²|Poleas tipo anillo|
> |Cilindro hueco|I = ½M(R₁² + R₂²)|Poleas con grosor|
> |Esfera sólida|I = ⅖MR²|Poleas esféricas|
> |Varilla (centro)|I = 1/12ML²|Ejes de poleas|
> |Varilla (extremo)|I = ⅓ML²|Brazos de palanca|

## 🔗 Relaciones Importantes

> [!success]- **Fórmulas Clave** 📐
> 
> ### Cinemática:
> 
> ```
> v = ωR
> a = αR
> s = θR
> ```
> 
> ### Dinámica:
> 
> ```
> Στ = Iα
> τ = FR (para fuerza tangencial)
> ΣF = ma (para traslación)
> ```
> 
> ### Energía:
> 
> ```
> E_rot = ½Iω²
> E_trans = ½mv²
> E_total = E_rot + E_trans + E_pot
> ```

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Dinámica de Rotación]] - Fundamentos teóricos
> - [[Momento de Inercia]] - Cálculos detallados
> - [[Torque y Equilibrio Rotacional]] - Conceptos base
> - [[Segunda ley de Newton para Rotación]] - Ecuaciones fundamentales
> - [[Problemas de Cuerdas y Poleas ideales]] - Casos simplificados

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Leyes de Newton]] - Base de la dinámica
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Análisis de fuerzas
> - [[Vectores]] - Manejo matemático
> - [[Cinemática Rotacional]] - Movimiento angular

---

**Tags:** #dinamica #rotacion #poleas #cuerpos-rigidos #fisica-mecanica #torque #momento-inercia #tension #problemas #sistemas-mecanicos