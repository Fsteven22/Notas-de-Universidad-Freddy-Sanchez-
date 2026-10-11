---
dg-publish: true
---

# Sistemas de partículas (cuerdas, poleas ideales)

> [!quote] "En los sistemas de partículas conectadas, cada objeto cuenta su propia historia de fuerzas, pero todas convergen en una sinfonía de movimiento coordinado donde la tensión es el director de orquesta." 🎼
>
> [!info] Los sistemas de partículas conectadas por cuerdas y poleas ideales constituyen algunos de los problemas más elegantes y fundamentales de la mecánica clásica. Estos sistemas nos permiten analizar cómo múltiples objetos interactúan a través de fuerzas de tensión, manteniendo restricciones cinemáticas que los obligan a moverse de manera coordinada. Desde simples máquinas de Atwood hasta complejos sistemas de poleas múltiples, estos problemas integran conceptos de cinemática, dinámica y estática.

## 🎯 Componentes de los Sistemas

> [!info] **Cuerdas Ideales** 🪢
> 
> ### Características Principales:
> 
> - **Inextensible**: Longitud constante, no se estira
> - **Sin masa**: m = 0, no contribuye a la inercia del sistema
> - **Tensión uniforme**: Misma tensión en toda su longitud
> - **Sin fricción**: Desliza libremente sobre poleas
> 
> ### Propiedades Fundamentales:
> 
> |Propiedad|Consecuencia|Aplicación|
> |---|---|---|
> |Inextensibilidad|Restricción cinemática|Las aceleraciones están relacionadas|
> |Masa despreciable|Sin inercia propia|F = ma no aplica a la cuerda|
> |Tensión uniforme|Misma T en ambos extremos|Simplifica el análisis de fuerzas|
> |Flexibilidad ideal|Cambia dirección en poleas|Transmite fuerza alrededor de esquinas|
> 
> ### Restricciones Cinemáticas:
> 
> - **Sistema simple**: |a₁| = |a₂|
> - **Polea móvil**: a_carga = a_polea/2
> - **Múltiples poleas**: Relaciones geométricas específicas
>
> [!tip] **Poleas Ideales** ⚙️
> 
> ### Características Principales:
> 
> - **Sin fricción**: No hay pérdida de energía
> - **Sin masa**: Momento de inercia despreciable
> - **Radio fijo**: No se deforma bajo carga
> - **Cambio de dirección**: Redirige fuerzas sin alterarlas
> 
> ### Tipos de Poleas:
> 
> **Polea Fija**:
> 
> - Cambia dirección de la fuerza
> - No proporciona ventaja mecánica
> - T₁ = T₂ (misma tensión)
> 
> **Polea Móvil**:
> 
> - Proporciona ventaja mecánica 2:1
> - Se mueve con la carga
> - F_aplicada = Peso/2
> 
> **Sistema Compuesto**:
> 
> - Combina poleas fijas y móviles
> - Ventaja mecánica = 2ⁿ (n = número de poleas móviles)
>
> [!warning] **Sistemas de Múltiples Partículas** 🔗
> 
> ### Características del Sistema:
> 
> - **Interconexión**: Todas las masas están conectadas
> - **Movimiento coordinado**: Una sola variable independiente
> - **Fuerzas internas**: Tensiones en las cuerdas
> - **Fuerzas externas**: Pesos, fuerzas aplicadas, fricción
> 
> ### Principios Fundamentales:
> 
> 1. **Conservación de la cuerda**: Longitud total constante
> 2. **Misma aceleración**: En sistemas simples
> 3. **Tensión constante**: En cada segmento de cuerda
> 4. **Equilibrio de cada masa**: ΣF = ma para cada objeto
>
> [!success] 🔗 Análisis de Sistemas de Partículas
> 
> ```mermaid
> graph TD
>     A[Sistema de Partículas] --> B[Identificar Componentes]
>     A --> C[Establecer Restricciones]
>     A --> D[Analizar Fuerzas]
>     B --> E[Masas]
>     B --> F[Cuerdas]
>     B --> G[Poleas]
>     C --> H[Longitud de cuerda constante]
>     C --> I[Relación de aceleraciones]
>     C --> J[Dirección del movimiento]
>     D --> K[DCL para cada masa]
>     D --> L[Tensiones en cuerdas]
>     D --> M[Fuerzas externas]
>     style A fill:#e1f5fe
>     style B fill:#f3e5f5
>     style C fill:#e8f5e8
>     style D fill:#fff3e0
> ```
>
> [!note] **Relaciones Cinemáticas Fundamentales** 📐
> 
> ### Para Sistema Simple (Máquina de Atwood):
> 
> - **Restricción**: x₁ + x₂ = L (constante)
> - **Velocidades**: v₁ + v₂ = 0 → v₁ = -v₂
> - **Aceleraciones**: a₁ + a₂ = 0 → a₁ = -a₂
> 
> ### Para Polea Móvil:
> 
> - **Restricción**: 2y₁ + y₂ = L (constante)
> - **Relación**: a₂ = -2a₁
> - **Ventaja mecánica**: F = W/2
> 
> ### Para Sistema con Plano Inclinado:
> 
> - **Mismo módulo**: |a₁| = |a₂|
> - **Direcciones**: Según la geometría del sistema
> - **Coordenadas**: Consistentes con el movimiento

## 🎯 Estrategias de Resolución

> [!tip] **Método SPLICE (Sistema-Poleas-Longitud-Individuos-Coordenadas-Ecuaciones)** 🧠
> 
> ### **S**istema - Identifica el tipo de sistema
> 
> 1. Cuenta el número de masas
> 2. Identifica tipos de poleas (fijas/móviles)
> 3. Reconoce la configuración general
> 
> ### **P**oleas - Analiza las restricciones de poleas
> 
> 4. Determina cómo cambian las direcciones
> 5. Identifica ventajas mecánicas
> 6. Establece relaciones de tensión
> 
> ### **L**ongitud - Establece restricciones cinemáticas
> 
> 7. Escribe la ecuación de longitud de cuerda
> 8. Deriva para obtener relaciones de velocidad
> 9. Deriva nuevamente para aceleraciones
> 
> ### **I**ndividuos - Analiza cada masa por separado
> 
> 10. Dibuja DCL para cada objeto
> 11. Identifica todas las fuerzas actuantes
> 12. Establece sistemas de coordenadas consistentes
> 
> ### **C**oordenadas - Define direcciones positivas
> 
> 13. Elige direcciones coherentes con el movimiento
> 14. Mantén consistencia en todo el problema
> 15. Relaciona las aceleraciones según restricciones
> 
> ### **E**cuaciones - Resuelve el sistema
> 
> 16. Aplica ΣF = ma a cada masa
> 17. Usa las relaciones cinemáticas
> 18. Resuelve el sistema de ecuaciones resultante

## 📚 Problemas Tipo

> [!example] **Problema 1: Máquina de Atwood Simple** ⚖️
> 
> ### Enunciado:
> 
> Dos masas m₁ = 3 kg y m₂ = 5 kg están conectadas por una cuerda inextensible que pasa sobre una polea fija ideal. Determina: a) La aceleración del sistema b) La tensión en la cuerda
> 
> ### Solución:
> 
> **Datos**:
> 
> - m₁ = 3 kg, m₂ = 5 kg (m₂ > m₁, por tanto m₂ baja)
> 
> **Paso 1: Establecer coordenadas**
> 
> - Para m₁: positivo hacia arriba
> - Para m₂: positivo hacia abajo
> - Restricción: |a₁| = |a₂| = a
> 
> **Paso 2: Diagramas de cuerpo libre**
> 
> _Masa m₁_ (sube):
> 
> - Tensión T (↑)
> - Peso m₁g (↓)
> 
> _Masa m₂_ (baja):
> 
> - Peso m₂g (↓)
> - Tensión T (↑)
> 
> **Paso 3: Ecuaciones de movimiento**
> 
> Para m₁: T - m₁g = m₁a Para m₂: m₂g - T = m₂a
> 
> **Paso 4: Resolución**
> 
> Sumando las ecuaciones: m₂g - m₁g = (m₁ + m₂)a
> 
> a = (m₂ - m₁)g/(m₁ + m₂) = (5 - 3)(9.8)/(3 + 5) = **2.45 m/s²**
> 
> **Paso 5: Tensión** T = m₁(g + a) = 3(9.8 + 2.45) = **36.75 N**
> 
> _Verificación_: T = m₂(g - a) = 5(9.8 - 2.45) = 36.75 N ✓
>
> [!example] **Problema 2: Sistema con Polea Móvil** 🏗️
> 
> ### Enunciado:
> 
> Una carga de 100 N se levanta usando una polea móvil ideal. Determina: a) La fuerza aplicada necesaria b) La aceleración de la carga si se aplica una fuerza de 60 N
> 
> ### Solución:
> 
> **Parte a: Fuerza para equilibrio**
> 
> **Análisis de la polea móvil**:
> 
> - La carga está soportada por dos segmentos de cuerda
> - Cada segmento tiene tensión T
> - Para equilibrio: 2T = W
> 
> **Fuerza aplicada**: F = T = W/2 = 100/2 = **50 N**
> 
> **Parte b: Con fuerza de 60 N**
> 
> **Datos**: F_aplicada = 60 N, W = 100 N, m = W/g = 100/9.8 = 10.2 kg
> 
> **Restricción cinemática**:
> 
> - Si la carga sube distancia y, la cuerda aplicada baja 2y
> - Por tanto: a_carga = a_aplicada/2
> 
> **Análisis de fuerzas en la carga**: 2T - W = ma_carga
> 
> Donde T = F_aplicada = 60 N 2(60) - 100 = 10.2 × a_carga 20 = 10.2 × a_carga a_carga = **1.96 m/s²**
>
> [!example] **Problema 3: Sistema Mixto (Plano Inclinado + Polea)** 🏔️
> 
> ### Enunciado:
> 
> Una masa m₁ = 4 kg está en un plano inclinado 30° sin fricción, conectada por una cuerda sobre una polea fija a una masa colgante m₂ = 2 kg. Determina la aceleración del sistema y la tensión.
> 
> ### Solución:
> 
> **Análisis preliminar**:
> 
> - Componente de m₁ en el plano: m₁g sin 30° = 4 × 9.8 × 0.5 = 19.6 N
> - Peso de m₂: m₂g = 2 × 9.8 = 19.6 N
> 
> Como las fuerzas son iguales, verificaremos si hay movimiento.
> 
> **Paso 1: Establecer coordenadas**
> 
> - m₁: positivo hacia abajo del plano
> - m₂: positivo hacia abajo
> - Restricción: |a₁| = |a₂| = a
> 
> **Paso 2: Diagramas de cuerpo libre**
> 
> _Masa m₁_ (en plano inclinado):
> 
> - Componente del peso: m₁g sin 30° = 19.6 N (hacia abajo del plano)
> - Normal: N = m₁g cos 30° = 33.94 N (⊥ al plano)
> - Tensión: T (hacia arriba del plano)
> 
> _Masa m₂_ (colgante):
> 
> - Peso: m₂g = 19.6 N (↓)
> - Tensión: T (↑)
> 
> **Paso 3: Ecuaciones de movimiento**
> 
> Para m₁: m₁g sin 30° - T = m₁a Para m₂: m₂g - T = m₂a
> 
> **Paso 4: Resolución**
> 
> Sustituyendo valores: 19.6 - T = 4a ... (1) 19.6 - T = 2a ... (2)
> 
> Restando (1) - (2): 0 = 2a a = **0 m/s²** (sistema en equilibrio)
> 
> **Tensión**: De cualquier ecuación: T = **19.6 N**
> 
> _Interpretación_: Las fuerzas están perfectamente balanceadas, por lo que el sistema permanece en equilibrio estático o se mueve con velocidad constante.

## 🧮 Técnicas de Memorización

> [!tip] **Mnemotecnia: "SPLICE"** 🧵 **S**istema identificado **P**oleas analizadas  
> **L**ongitud de cuerda conservada **I**ndividuos con DCL **C**oordenadas consistentes **E**cuaciones resueltas
>
> [!tip] **Regla de Tensiones: "La Cadena de la Verdad"** ⛓️
> 
> - **Una cuerda = Una tensión** en toda su longitud
> - **Polea ideal = Tensión inalterada**
> - **Masa de cuerda = 0** → No aparece en ΣF = ma
> - **Restricción cinemática** → Acelereaciones relacionadas

## ⚠️ Errores Comunes

> [!warning] **Confusiones Frecuentes** ⚠️
> 
> 1. **Direcciones inconsistentes**: No mantener coherencia en los sistemas de coordenadas
> 2. **Olvidar restricciones cinemáticas**: No relacionar las aceleraciones correctamente
> 3. **Tensiones diferentes**: Asumir tensiones distintas en la misma cuerda
> 4. **Signos incorrectos**: Error en la dirección de fuerzas y aceleraciones
> 5. **Confundir masa y peso**: Especialmente en problemas con unidades mixtas
> 6. **Ignorar la geometría**: No considerar ángulos y direcciones en sistemas complejos
> 7. **Poleas con masa**: Olvidar que las poleas ideales no tienen inercia rotacional

## 🎯 Aplicaciones Prácticas

> [!info] **Ejemplos del Mundo Real** 🌍
> 
> ### Construcción:
> 
> - Grúas y sistemas de elevación
> - Polipastos para cargas pesadas
> - Sistemas de tensores en estructuras
> 
> ### Transporte:
> 
> - Funiculares y teleféricos
> - Ascensores y montacargas
> - Sistemas de tracción por cable
> 
> ### Maquinaria Industrial:
> 
> - Transmisión por correas y poleas
> - Sistemas de elevación en fábricas
> - Mecanismos de posicionamiento
> 
> ### Deportes y Recreación:
> 
> - Equipos de escalada y rapel
> - Sistemas de tirolesa
> - Aparejos en navegación a vela
> 
> ### Ingeniería Mecánica:
> 
> - Diseño de máquinas simples
> - Sistemas de ventaja mecánica
> - Mecanismos de transmisión de fuerza

## 📖 Referencias

> [!quote] **Notas Relacionadas**
> 
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Base del análisis de fuerzas
> - [[Leyes de Newton]] - Fundamentos dinámicos
> - [[Problemas de Planos Inclinados]] - Sistemas en superficies inclinadas
> - [[Trabajo y Energía]] - Métodos energéticos alternativos

## 📚 Notas Recomendadas

> [!note] **Prerrequisitos**
> 
> - [[Vectores]] - Análisis de fuerzas y direcciones
> - [[Dinámica de Traslación]] - Segunda ley de Newton
> - [[Cinemática Traslacional]] - Relaciones entre posición, velocidad y aceleración

---

**Tags:** #dinamica #sistemas-particulas #cuerdas #poleas #maquina-atwood #fisica-mecanica #problemas #tension #restricciones-cinematicas #fuerzas-conectadas
