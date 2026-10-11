---
dg-publish: true
---

# Problemas de Colisiones

> [!quote] "En las colisiones, la naturaleza conserva lo esencial mientras transforma lo superficial; cada choque es una danza de conservación y cambio." 💥
>
> [!info] Las colisiones son eventos fundamentales en la física donde dos o más cuerpos interactúan durante un tiempo muy corto, intercambiando momentum y energía. El análisis de colisiones nos permite comprender desde el comportamiento de partículas subatómicas hasta accidentes vehiculares, aplicando principios de conservación que rigen el universo.

## 🎯 Tipos de Colisiones

> [!success] **Colisiones Elásticas (1D)** ⚽
> 
> ### Características Principales:
> 
> - **Conservación de momentum lineal**: Σpᵢ = Σpf
> - **Conservación de energía cinética**: ΣKEᵢ = ΣKEf
> - **Coeficiente de restitución**: e = 1
> - **Deformación**: Temporal y completamente reversible
> 
> ### Ecuaciones Fundamentales:
> 
> **Para dos objetos (m₁, m₂)**:
> 
> ```
> Momentum: m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f
> Energía:   ½m₁v₁ᵢ² + ½m₂v₂ᵢ² = ½m₁v₁f² + ½m₂v₂f²
> ```
> 
> ### Fórmulas de Velocidades Finales:
> 
> ```
> v₁f = ((m₁-m₂)v₁ᵢ + 2m₂v₂ᵢ)/(m₁+m₂)
> 
> v₂f = ((m₂-m₁)v₂ᵢ + 2m₁v₁ᵢ)/(m₁+m₂)
> ```
> 
> ### Casos Especiales:
> 
> |Condición|Resultado|Aplicación|
> |---|---|---|
> |m₁ = m₂|Las velocidades se intercambian|Bolas de billar idénticas|
> |m₁ >> m₂, v₂ᵢ = 0|v₁f ≈ v₁ᵢ, v₂f ≈ 2v₁ᵢ|Pelota contra pared|
> |m₁ << m₂, v₂ᵢ = 0|v₁f ≈ -v₁ᵢ, v₂f ≈ 0|Rebote contra objeto masivo|
>
> [!warning] **Colisiones Inelásticas (1D)** 🚗
> 
> ### Características Principales:
> 
> - **Conservación de momentum lineal**: Σpᵢ = Σpf
> - **NO conservación de energía cinética**: ΣKEᵢ > ΣKEf
> - **Coeficiente de restitución**: 0 < e < 1
> - **Deformación**: Permanente, energía se disipa
> 
> ### Coeficiente de Restitución:
> 
> ```
> e = -(v₁f - v₂f)/(v₁ᵢ - v₂ᵢ)
> ```
> 
> ### Energía Cinética Perdida:
> 
> ```
> ΔKE = KEᵢ - KEf = ½μ(v₁ᵢ - v₂ᵢ)²(1 - e²)
> ```
> 
> Donde μ = m₁m₂/(m₁ + m₂) es la masa reducida
> 
> ### Interpretación Física:
> 
> - La energía "perdida" se convierte en calor, sonido, deformación
> - El coeficiente e caracteriza la "elasticidad" del material
> - Valores típicos: acero-acero (e ≈ 0.9), plástico-plástico (e ≈ 0.3)
>
> [!danger] **Choque Completamente Inelástico** 🔗
> 
> ### Características Principales:
> 
> - **Conservación de momentum lineal**: Σpᵢ = Σpf
> - **Máxima pérdida de energía cinética** posible
> - **Coeficiente de restitución**: e = 0
> - **Los objetos quedan unidos** tras la colisión
> 
> ### Ecuación Fundamental:
> 
> ```
> m₁v₁ᵢ + m₂v₂ᵢ = (m₁ + m₂)vf
> ```
> 
> ### Velocidad Final Común:
> 
> ```
> vf = (m₁v₁ᵢ + m₂v₂ᵢ)/(m₁ + m₂)
> ```
> 
> ### Máxima Energía Perdida:
> 
> ```
> ΔKE_max = ½μ(v₁ᵢ - v₂ᵢ)²
> ```
> 
> ### Ejemplos Comunes:
> 
> - Bala incrustándose en bloque de madera
> - Trenes acoplándose en maniobras
> - Meteorito impactando planeta
> - Accidentes vehiculares con enganche
>
> [!info] 🔄 Relaciones Entre Tipos de Colisiones
> 
> ```mermaid
> graph TD
>     A[Colisión] --> B{Coeficiente e}
>     B -->|e = 1| C[Elástica]
>     B -->|0 < e < 1| D[Inelástica]
>     B -->|e = 0| E[Completamente Inelástica]
>     C --> F[Conserva KE y p]
>     D --> G[Conserva p, pierde KE]
>     E --> H[Conserva p, máxima pérdida KE]
>     style C fill:#e8f5e8
>     style D fill:#fff3e0
>     style E fill:#ffebee
> ```

## 🎯 Estrategias de Resolución

> [!tip] **Método CIME (Conservación-Identificación-Modelado-Evaluación)** 🧠
> 
> ### **C**onservación - Identifica qué se conserva
> 
> 1. **Siempre**: Momentum lineal (si no hay fuerzas externas)
> 2. **A veces**: Energía cinética (solo en colisiones elásticas)
> 3. **Nunca**: Energía total (algo siempre se disipa)
> 
> ### **I**dentificación - Clasifica el tipo de colisión
> 
> 4. Analiza el enunciado para determinar el tipo
> 5. Busca palabras clave: "rebotan" (elástica), "se pegan" (inelástica)
> 6. Verifica si se da el coeficiente de restitución
> 
> ### **M**odelado - Establece el sistema de ecuaciones
> 
> 7. Aplica conservación de momentum
> 8. Si es elástica, añade conservación de energía
> 9. Si es inelástica, usa el coeficiente de restitución
> 
> ### **E**valuación - Resuelve y verifica
> 
> 10. Resuelve el sistema de ecuaciones
> 11. Verifica que las velocidades tengan sentido físico
> 12. Calcula energías para verificar coherencia

## 📚 Problemas Tipo

> [!example] **Problema 1: Colisión Elástica Frontal** ⚽⚾
> 
> ### Enunciado:
> 
> Una pelota de 0.2 kg moviéndose a 10 m/s choca elásticamente con otra de 0.3 kg en reposo. Determina las velocidades finales de ambas pelotas.
> 
> ### Datos:
> 
> - m₁ = 0.2 kg, v₁ᵢ = 10 m/s
> - m₂ = 0.3 kg, v₂ᵢ = 0 m/s
> - Colisión elástica (e = 1)
> 
> ### Solución:
> 
> **Conservación de momentum**:
> 
> ```
> 0.2(10) + 0.3(0) = 0.2v₁f + 0.3v₂f
> 2 = 0.2v₁f + 0.3v₂f ... (1)
> ```
> 
> **Conservación de energía**:
> 
> ```
> ½(0.2)(10)² = ½(0.2)v₁f² + ½(0.3)v₂f²
> 10 = 0.1v₁f² + 0.15v₂f² ... (2)
> ```
> 
> **Usando las fórmulas directas**:
> 
> ```
> v₁f = (0.2-0.3)(10) + 2(0.3)(0) / (0.2+0.3) = -2 m/s
> v₂f = (0.3-0.2)(0) + 2(0.2)(10) / (0.2+0.3) = 8 m/s
> ```
> 
> **Verificación**:
> 
> - Momentum: 0.2(-2) + 0.3(8) = 2 ✓
> - Energía: ½(0.2)(4) + ½(0.3)(64) = 10 J ✓
>
> [!example] **Problema 2: Colisión Inelástica** 🚗💥
> 
> ### Enunciado:
> 
> Un automóvil de 1200 kg a 20 m/s choca con otro de 1000 kg a 15 m/s en dirección opuesta. Tras el choque, el primer auto se mueve a 5 m/s. Encuentra la velocidad final del segundo auto y el coeficiente de restitución.
> 
> ### Datos:
> 
> - m₁ = 1200 kg, v₁ᵢ = +20 m/s
> - m₂ = 1000 kg, v₂ᵢ = -15 m/s
> - v₁f = +5 m/s, v₂f = ?
> 
> ### Solución:
> 
> **Conservación de momentum**:
> 
> ```
> 1200(20) + 1000(-15) = 1200(5) + 1000v₂f
> 24000 - 15000 = 6000 + 1000v₂f
> 9000 = 6000 + 1000v₂f
> v₂f = 3 m/s
> ```
> 
> **Coeficiente de restitución**:
> 
> ```
> e = -(v₁f - v₂f)/(v₁ᵢ - v₂ᵢ)
> e = -(5 - 3)/(20 - (-15)) = -2/35 ≈ 0.057
> ```
> 
> **Energía perdida**:
> 
> ```
> KEᵢ = ½(1200)(20)² + ½(1000)(15)² = 352500 J
> KEf = ½(1200)(5)² + ½(1000)(3)² = 19500 J
> ΔKE = 333000 J (94% de energía perdida)
> ```
>
> [!example] **Problema 3: Choque Completamente Inelástico** 🔫🎯
> 
> ### Enunciado:
> 
> Una bala de 20 g disparada a 400 m/s se incrusta en un bloque de madera de 2 kg inicialmente en reposo. Determina la velocidad final del sistema y la energía perdida.
> 
> ### Datos:
> 
> - m₁ = 0.02 kg, v₁ᵢ = 400 m/s
> - m₂ = 2 kg, v₂ᵢ = 0 m/s
> - Choque completamente inelástico (e = 0)
> 
> ### Solución:
> 
> **Velocidad final común**:
> 
> ```
> vf = (m₁v₁ᵢ + m₂v₂ᵢ)/(m₁ + m₂)
> vf = (0.02 × 400 + 2 × 0)/(0.02 + 2)
> vf = 8/2.02 ≈ 3.96 m/s
> ```
> 
> **Energía inicial**:
> 
> ```
> KEᵢ = ½(0.02)(400)² = 1600 J
> ```
> 
> **Energía final**:
> 
> ```
> KEf = ½(2.02)(3.96)² ≈ 15.9 J
> ```
> 
> **Energía perdida**:
> 
> ```
> ΔKE = 1600 - 15.9 ≈ 1584 J (99% perdida)
> ```
> 
> Esta energía se convierte en calor, sonido y deformación.

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "ELIPSE"** 🥚 **E**lástica → **L**a energía **I**gual **P**ermanece **S**iempre **E**xacta
> 
> **Reglas Rápidas:**
> 
> - **Elástica**: "Se conserva TODO" (momentum + energía)
> - **Inelástica**: "Se conserva MOMENTUM, se pierde energía"
> - **Completamente inelástica**: "Se PEGAN y pierden MÁS energía"

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ❌
> 
> 1. **Confundir el signo de velocidades** en colisiones frontales
> 2. **Asumir conservación de energía** en todas las colisiones
> 3. **Olvidar que e = 0** significa que los objetos quedan unidos
> 4. **Calcular mal el coeficiente de restitución** (invertir velocidades)
> 5. **No verificar** que las velocidades finales sean físicamente coherentes
> 6. **Ignorar la dirección** en problemas unidimensionales
> 7. **Confundir energía perdida con energía total** del sistema

## 🔧 Herramientas de Análisis

> [!info] **Diagramas de Análisis** 📊
> 
> ### Diagrama Antes-Después:
> 
> ```
> ANTES:    [m₁→v₁ᵢ]     [m₂→v₂ᵢ]
> COLISIÓN:        💥
> DESPUÉS:  [m₁→v₁f]     [m₂→v₂f]
> ```
> 
> ### Gráfico de Energía:
> 
> - **Eje Y**: Energía cinética
> - **Eje X**: Tipo de colisión
> - **Tendencia**: Decrece de elástica a inelástica
> 
> ### Tabla de Verificación:
> 
> |Magnitud|Inicial|Final|¿Se conserva?|
> |---|---|---|---|
> |Momentum|pᵢ|pf|✓ Siempre|
> |Energía KE|KEᵢ|KEf|Depende del tipo|
> |Energía Total|Eᵢ|Ef|✓ Siempre|

## 🎯 Aplicaciones Prácticas

> [!success] **Ejemplos del Mundo Real** 🌍
> 
> ### Seguridad Vehicular:
> 
> - Diseño de zonas de deformación en automóviles
> - Cálculo de fuerzas en accidentes de tránsito
> - Análisis forense de colisiones
> 
> ### Deportes:
> 
> - Técnicas de golpeo en béisbol y golf
> - Estrategias en billar y bowling
> - Análisis biomecánico de impactos
> 
> ### Ingeniería:
> 
> - Diseño de amortiguadores y sistemas de absorción
> - Pruebas de materiales bajo impacto
> - Simulación de colisiones en videojuegos
> 
> ### Astronomía:
> 
> - Formación de cráteres por meteoritos
> - Colisiones entre galaxias
> - Origen del sistema solar por acreción

## 🔬 Casos Especiales Avanzados

> [!note] **Situaciones Complejas** ⚡
> 
> ### Colisión con Rotación:
> 
> - Conservación de momentum angular
> - Rodadura después del impacto
> - Ejemplo: Pelota de ping-pong con efecto
> 
> ### Colisiones en Cadena:
> 
> - Múltiples objetos en fila (péndulo de Newton)
> - Propagación de ondas de choque
> - Aplicación: Cuna de Newton
> 
> ### Colisión Oblicua (2D):
> 
> - Componentes x e y del momentum
> - Ángulos de dispersión
> - Conservación vectorial

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Momentum Lineal y Su Conservación]] - Fundamentos teóricos
> - [[Centro de masa (CM)]] - Análisis de sistemas
> - [[Impulso Lineal]] - Relación fuerza-tiempo
> - [[Trabajo y Energía]] - Base energética

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Vectores]] - Para colisiones bidimensionales
> - [[Leyes de Newton]] - Fundamentos dinámicos
> - [[Principios de Conservación de la Energía]] - Conceptos energéticos

---

**Tags:** #colisiones #momentum #energia-cinetica #elastica #inelastica #conservacion #impulso #fisica-mecanica #dinamica #problemas
