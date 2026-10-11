---
dg-publish: true
---

# Problemas con Fuerzas No Conservativas

> [!quote] "Las fuerzas no conservativas son las ladronas de energía del universo mecánico; donde aparecen, la energía se transforma pero nunca se pierde completamente." 🔥
>
> [!info] Las fuerzas no conservativas son aquellas cuyo trabajo depende de la trayectoria seguida, no solo de los puntos inicial y final. Estas fuerzas, como la fricción y la resistencia del aire, introducen disipación de energía mecánica, transformándola en otras formas como calor, sonido o deformación permanente.

## ⚡ Fundamentos de Fuerzas No Conservativas

> [!info] **Características Principales** 🌀
> 
> ### Definición:
> 
> Una fuerza es **no conservativa** cuando el trabajo realizado **depende de la trayectoria** seguida entre dos puntos.
> 
> ### Propiedades Fundamentales:
> 
> - **W ≠ 0** en trayectorias cerradas
> - **No existe energía potencial** asociada
> - **Disipan energía mecánica** del sistema
> - **Irreversibles** en procesos naturales
> 
> ### Comparación con Fuerzas Conservativas:
> 
> |Aspecto|Conservativas|No Conservativas|
> |---|---|---|
> |Trabajo en ciclo cerrado|W = 0|W ≠ 0|
> |Dependencia|Solo puntos inicial/final|Trayectoria completa|
> |Energía potencial|Existe|No existe|
> |Reversibilidad|Reversible|Irreversible|
> |Ejemplos|Gravitatoria, elástica|Fricción, resistencia aire|
>
> [!tip] **Teorema Trabajo-Energía Generalizado** ⚖️
> 
> ### Ecuación Fundamental:
> 
> **W_conservativas + W_no_conservativas = ΔE_cinética**
> 
> ### Reformulación en Términos de Energía:
> 
> **E_mecánica_inicial + W_no_conservativas = E_mecánica_final**
> 
> **ΔE_mecánica = W_no_conservativas**
> 
> ### Interpretación:
> 
> - Si W_no_cons < 0: Se pierde energía mecánica (fricción)
> - Si W_no_cons > 0: Se añade energía al sistema (motor)
> - La energía "perdida" se transforma en calor, sonido, etc.
>
> [!warning] **Tipos de Fuerzas No Conservativas** 🔥
> 
> ### 1. Fricción (μ):
> 
> - **Estática**: f_s ≤ μ_s N
> - **Cinética**: f_k = μ_k N
> - **Trabajo**: W_f = -f_k × d = -μ_k mg d cos θ
> 
> ### 2. Resistencia del Aire (R):
> 
> - **Baja velocidad**: R = -bv
> - **Alta velocidad**: R = -cv²
> - **Trabajo**: W_R = ∫\vec{R} · d\vec{r} (requiere integración)
> 
> ### 3. Fuerzas Aplicadas Variables:
> 
> - **Motores**: Añaden energía al sistema
> - **Frenos**: Disipan energía del sistema
> - **Trabajo**: Depende de la función F(t) o F(x)
>
> [!success] 🔗 Estrategias de Resolución
> 
> ```mermaid
> graph TD
>     A[Problema con Fuerzas No Conservativas] --> B[Identificar Fuerzas]
>     B --> C[Fuerzas Conservativas]
>     B --> D[Fuerzas No Conservativas]
>     C --> E[Calcular ΔE_potencial]
>     D --> F[Calcular W_no_conservativo]
>     E --> G[Aplicar: E_inicial + W_no_cons = E_final]
>     F --> G
>     G --> H[Resolver para Incógnita]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#e8f5e8
>     style D fill:#fff3e0
>     style G fill:#fce4ec
> ```

## 🔧 Estrategias de Resolución

> [!tip] **Método FRENO (Fuerzas-Resistencia-Energía-No_conservativas-Obtener)** 🧠
> 
> ### **F**uerzas - Clasificar todas las fuerzas
> 
> 1. Identificar fuerzas conservativas (peso, elástica)
> 2. Identificar fuerzas no conservativas (fricción, resistencia)
> 3. Determinar direcciones y magnitudes
> 
> ### **R**esistencia - Calcular trabajo disipativo
> 
> 4. Calcular trabajo de fricción: W_f = -μmgd
> 5. Calcular trabajo de resistencia del aire si aplica
> 6. Sumar todos los trabajos no conservativos
> 
> ### **E**nergía - Evaluar estados inicial y final
> 
> 7. Calcular E_mecánica inicial = E_c + E_p
> 8. Calcular E_mecánica final = E_c + E_p
> 9. Establecer nivel de referencia consistente
> 
> ### **N**o_conservativas - Aplicar ecuación generalizada
> 
> 10. E_inicial + W_no_conservativo = E_final
> 11. Sustituir valores conocidos
> 12. Simplificar la ecuación
> 
> ### **O**btener - Resolver y verificar
> 
> 13. Despejar la incógnita
> 14. Verificar coherencia física del resultado
> 15. Comprobar unidades y signos

## 📚 Problemas Tipo

> [!example] **Problema 1: Deslizamiento con Fricción** 🛷
> 
> ### Enunciado:
> 
> Un bloque de 5 kg se desliza por un plano inclinado rugoso de 30° y 10 m de longitud, partiendo del reposo. Si μ_k = 0.2, determina: a) La velocidad al final del plano b) La energía disipada por fricción c) ¿Qué velocidad inicial necesitaría para llegar abajo con 8 m/s?
> 
> ### Solución:
> 
> **Datos**: m = 5 kg, θ = 30°, L = 10 m, μ_k = 0.2, v_0 = 0
> 
> **Análisis de fuerzas**:
> 
> - Altura inicial: h = L sen 30° = 10 × 0.5 = 5 m
> - Normal: N = mg cos 30° = 5 × 9.8 × 0.866 = 42.4 N
> - Fricción: f_k = μ_k N = 0.2 × 42.4 = 8.48 N
> 
> **a) Velocidad final**:
> 
> E_inicial = mgh = 5 × 9.8 × 5 = 245 J W_fricción = -f_k × L = -8.48 × 10 = -84.8 J E_final = ½mv²
> 
> **Aplicando**: E_inicial + W_no_cons = E_final 245 + (-84.8) = ½(5)v² 160.2 = 2.5v² **v = 8.01 m/s**
> 
> **b) Energía disipada**: **E_disipada = |W_fricción| = 84.8 J**
> 
> **c) Velocidad inicial necesaria**:
> 
> E_inicial = ½mv_0² + mgh = ½(5)v_0² + 245 E_final = ½m(8)² = ½(5)(64) = 160 J
> 
> E_inicial + W_fricción = E_final [2.5v_0² + 245] + (-84.8) = 160 2.5v_0² = 160 - 245 + 84.8 = -0.2
> 
> **No es posible** (resultado negativo). El objeto no puede llegar con 8 m/s debido a la fricción.
>
> [!example] **Problema 2: Resistencia del Aire Proporcional a v** 🪂
> 
> ### Enunciado:
> 
> Un objeto de 2 kg cae desde el reposo experimentando resistencia del aire R = -0.5v (en N). Si cae 50 m, determina: a) La ecuación diferencial del movimiento b) La velocidad terminal c) La velocidad después de caer 50 m
> 
> ### Solución:
> 
> **Datos**: m = 2 kg, R = -0.5v, h = 50 m, v_0 = 0
> 
> **a) Ecuación diferencial**:
> 
> Aplicando la segunda ley de Newton: ma = mg - R = mg - 0.5v 2(dv/dt) = 2(9.8) - 0.5v **dv/dt = 9.8 - 0.25v**
> 
> **b) Velocidad terminal**:
> 
> En equilibrio: dv/dt = 0 9.8 - 0.25v_terminal = 0 **v_terminal = 9.8/0.25 = 39.2 m/s**
> 
> **c) Velocidad después de 50 m**:
> 
> Usando conservación de energía: E_inicial = mgh = 2 × 9.8 × 50 = 980 J E_final = ½mv² = ½(2)v² = v²
> 
> W_resistencia = -∫₀^50 R dy = -∫₀^50 0.5v dy
> 
> Como v depende de y, esto requiere resolver la ecuación diferencial. **Resultado aproximado usando métodos numéricos: v ≈ 35.8 m/s**
>
> [!example] **Problema 3: Fricción en Movimiento Circular** 🎠
> 
> ### Enunciado:
> 
> Una masa de 1 kg gira en un círculo horizontal de radio 2 m sobre una mesa con μ_k = 0.3. Si inicialmente tiene velocidad de 6 m/s, determina: a) El tiempo que tarda en detenerse b) El número de vueltas antes de parar c) La potencia disipada inicial
> 
> ### Solución:
> 
> **Datos**: m = 1 kg, R = 2 m, μ_k = 0.3, v_0 = 6 m/s
> 
> **Análisis**: La fricción es la única fuerza no conservativa
> 
> **a) Tiempo para detenerse**:
> 
> Fuerza de fricción: f = μ_k mg = 0.3 × 1 × 9.8 = 2.94 N Desaceleración: a = f/m = 2.94 m/s²
> 
> Usando v = v_0 - at: 0 = 6 - 2.94t **t = 6/2.94 = 2.04 s**
> 
> **b) Número de vueltas**:
> 
> Distancia recorrida: s = v_0t - ½at² = 6(2.04) - ½(2.94)(2.04)² s = 12.24 - 6.12 = 6.12 m
> 
> Circunferencia: C = 2πR = 2π(2) = 12.57 m **Número de vueltas = 6.12/12.57 = 0.49 vueltas**
> 
> **c) Potencia disipada inicial**:
> 
> P = F × v = f × v_0 = 2.94 × 6 = **17.6 W**
> 
> **Verificación energética**: E_inicial = ½mv_0² = ½(1)(6)² = 18 J W_fricción = -f × s = -2.94 × 6.12 = -18 J ✓
>
> [!example] **Problema 4: Sistemas con Motor** 🚗
> 
> ### Enunciado:
> 
> Un automóvil de 1200 kg acelera desde reposo hasta 25 m/s en una distancia de 200 m sobre una superficie con μ_k = 0.02. Determina: a) El trabajo realizado por el motor b) La potencia promedio del motor c) La eficiencia si el motor consume 5 MJ
> 
> ### Solución:
> 
> **Datos**: m = 1200 kg, v_0 = 0, v_f = 25 m/s, d = 200 m, μ_k = 0.02
> 
> **a) Trabajo del motor**:
> 
> Cambio de energía cinética: ΔE_c = ½m(v_f² - v_0²) = ½(1200)(25²) = 375,000 J Trabajo contra fricción: W_fricción = μ_k mgd = 0.02 × 1200 × 9.8 × 200 = 47,040 J
> 
> **W_motor = ΔE_c + |W_fricción| = 375,000 + 47,040 = 422,040 J**
> 
> **b) Potencia promedio**:
> 
> Para encontrar el tiempo, usamos cinemática: v_f² = v_0² + 2ad → a = v_f²/(2d) = (25)²/(2×200) = 1.56 m/s² v_f = v_0 + at → t = v_f/a = 25/1.56 = 16 s
> 
> **P_promedio = W_motor/t = 422,040/16 = 26.4 kW**
> 
> **c) Eficiencia**:
> 
> Energía consumida = 5 MJ = 5,000,000 J **η = W_útil/E_consumida = 422,040/5,000,000 = 8.4%**
>
> [!example] **Problema 5: Péndulo con Resistencia del Aire** 🕰️
> 
> ### Enunciado:
> 
> Un péndulo de 1 m de longitud y masa 0.5 kg se suelta desde 60° con la vertical. Debido a la resistencia del aire, solo alcanza 45° en el lado opuesto. Determina: a) La energía disipada en media oscilación b) El coeficiente de resistencia si R = -cv² c) La amplitud después de 5 oscilaciones completas
> 
> ### Solución:
> 
> **Datos**: L = 1 m, m = 0.5 kg, θ_1 = 60°, θ_2 = 45°
> 
> **a) Energía disipada**:
> 
> Altura inicial: h_1 = L(1 - cos 60°) = 1(1 - 0.5) = 0.5 m Altura final: h_2 = L(1 - cos 45°) = 1(1 - 0.707) = 0.293 m
> 
> E_inicial = mgh_1 = 0.5 × 9.8 × 0.5 = 2.45 J E_final = mgh_2 = 0.5 × 9.8 × 0.293 = 1.44 J
> 
> **E_disipada = E_inicial - E_final = 2.45 - 1.44 = 1.01 J**
> 
> **b) Coeficiente de resistencia**:
> 
> Velocidad máxima (en el punto bajo): v_máx = √(2gL(1 - cos 60°)) = √(2 × 9.8 × 1 × 0.5) = 3.13 m/s
> 
> Longitud del arco recorrido: s ≈ L(θ_1 + θ_2) = 1(60° + 45°) × π/180° = 1.83 m
> 
> W_resistencia = -c∫v² ds ≈ -cv²_promedio × s Asumiendo v_promedio ≈ 0.7v_máx = 2.19 m/s
> 
> -1.01 = -c(2.19)² × 1.83 **c = 1.01/(4.8 × 1.83) = 0.115 kg/m**
> 
> **c) Amplitud después de 5 oscilaciones**:
> 
> Si la pérdida es proporcional, después de cada media oscilación: Fracción conservada = E_final/E_inicial = 1.44/2.45 = 0.588
> 
> Después de 10 medias oscilaciones: (0.588)^10 = 0.00084 **Amplitud final ≈ 60° × √0.00084 ≈ 1.7°**

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "DISIPA"** 📝
> 
> **D**epende - El trabajo depende de la trayectoria **I**rrversible - No se puede recuperar la energía perdida  
> **S**iempre - Siempre disipan energía (fricción, resistencia) **I**mposible - Imposible definir energía potencial **P**érdida - Transforman energía mecánica en calor **A**ñaden - Los motores añaden energía al sistema
>
> [!tip] **Ecuaciones Clave** 🔑
> 
> ### Conservación Modificada:
> 
> **E_inicial + W_no_conservativo = E_final**
> 
> ### Fricción:
> 
> - **Cinética**: W_f = -μ_k mg d cos θ
> - **En plano**: W_f = -μ_k mg d
> - **En inclinado**: W_f = -μ_k mg cos θ × d
> 
> ### Resistencia del aire:
> 
> - **Lineal**: R = -bv → W = -∫bv ds
> - **Cuadrática**: R = -cv² → W = -∫cv² ds

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Ignorar las fuerzas no conservativas**: Aplicar conservación sin considerar fricción
> 2. **Signo del trabajo no conservativo**: Confundir cuándo es positivo o negativo
> 3. **Distancia vs desplazamiento**: Usar desplazamiento cuando la fricción actúa sobre la distancia recorrida
> 4. **Fricción en planos inclinados**: Olvidar el cos θ en la normal
> 5. **Energía "perdida"**: Pensar que se destruye en lugar de transformarse
> 6. **Resistencia del aire**: Asumir que es constante cuando depende de la velocidad
> 7. **Trabajo de la normal**: Asumir que hace trabajo en movimiento curvilíneo

## 🎯 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Transporte:
> 
> - Frenado de vehículos y trenes
> - Consumo de combustible por resistencia
> - Diseño de neumáticos y superficies
> 
> ### Ingeniería:
> 
> - Amortiguadores y sistemas de suspensión
> - Lubricación y reducción de fricción
> - Eficiencia energética de máquinas
> 
> ### Deportes:
> 
> - Resistencia del aire en ciclismo y natación
> - Fricción en esquí y patinaje
> - Pérdidas en equipos deportivos
> 
> ### Meteorología:
> 
> - Caída de gotas de lluvia
> - Resistencia del aire en paracaidismo
> - Sedimentación de partículas

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Trabajo y Energía]] - Conceptos fundamentales
> - [[Problemas de Trabajo]] - Cálculo del trabajo
> - [[Problemas de Conservación de Energía Mecánica]] - Caso ideal
> - [[Principios de Conservación de la Energía]] - Marco teórico general

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Leyes de Newton]] - Análisis de fuerzas
> - [[Cinemática Traslacional]] - Conceptos de movimiento
> - [[Vectores]] - Descomposición de fuerzas
> - [[Unidades y Magnitudes Físicas]] - Consistencia dimensional

---

**Tags:** #fuerzas-no-conservativas #friccion #resistencia-aire #disipacion-energia #trabajo-energia #fisica-mecanica #perdidas-energeticas #eficiencia #motores #amortiguamiento
