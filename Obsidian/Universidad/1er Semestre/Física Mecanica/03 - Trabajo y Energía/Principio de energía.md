# ⚡ Principio de Energía

## 📋 Contexto

> [!abstract] Principio Fundamental La energía total de un sistema aislado se mantiene constante.
> 
> Este principio establece que en presencia de fuerzas externas (no conservativas) o interacciones con el entorno, el **trabajo neto externo** realizado sobre un sistema es igual al cambio en su **energía total**.

> [!success] Ventaja Principal 🎯 Es una herramienta poderosa para analizar el movimiento y las interacciones sin necesidad de usar las leyes de Newton directamente en cada punto.

---

## 🔢 Variables Comunes

> [!tip] Variables Principales
> 
> |Variable|Símbolo|Unidad|Descripción|
> |---|---|---|---|
> |Trabajo Externo|$W_{ext}$|J (Julios)|Energía transferida al sistema|
> |Energía Cinética|$\Delta K$|J|Cambio en energía de movimiento|
> |Energía Potencial|$\Delta U$|J|Cambio en energía de posición|
> |Energía Térmica|$\Delta E_{term}$|J|Energía disipada por fricción|
> |Masa|$m$|kg|Cantidad de materia|
> |Velocidad|$v$|m/s|Rapidez del movimiento|
> |Posición/Altura|$x, h$|m|Ubicación espacial|
> |Constante de resorte|$k$|N/m|Rigidez del resorte|

---

## 🧮 Fórmulas y Procedimientos

> [!note] Ecuación Principal - Principio de Energía General $W_{ext} = \Delta E_{total} = \Delta K + \Delta U + \Delta E_{term} + ...$

> [!info] Conservación de Energía Mecánica _Cuando no hay trabajo externo ni fricción:_ $K_{inicial} + U_{inicial} = K_{final} + U_{final}$

> [!warning] Relación Fuerza-Energía Potencial $F_x = -\frac{dU}{dx}$

> [!tip] Tipos de Energía Potencial
> 
> ```mermaid
> graph TD
>     A[🔋 Energía Potencial] --> B[🌍 Gravitatoria]
>     A --> C[🌀 Elástica]
>     B --> D["U = mgh"]
>     C --> E["U = ½kx²"]
> ```

---

## 🎯 Explicación Teórica

> [!quote] Concepto Fundamental El principio de energía funciona como una **contabilidad energética**:
> 
> ```mermaid
> flowchart LR
>     A[⚡ Energía Inicial] --> B{🔄 Transformaciones}
>     B --> C[🏃 Cinética]
>     B --> D[📍 Potencial]
>     B --> E[🔥 Térmica]
>     C --> F[⚡ Energía Final]
>     D --> F
>     E --> F
> ```
> 
> Un sistema puede tener múltiples formas de energía que se transforman entre sí. El **trabajo externo** es el mecanismo de transferencia de energía hacia o desde el sistema.

---

## 🛠️ Aplicación Práctica

> [!example] Carro en Plano Inclinado 🚗
> 
> ```mermaid
> graph LR
>     A["🚗 Inicio<br/>h = altura<br/>v = 0"] --> B["🏁 Final<br/>h = 0<br/>v = ?"]
>     A -.-> C["Sin fricción:<br/>mgh = ½mv²"]
>     A -.-> D["Con fricción:<br/>mgh = ½mv² + Q"]
> ```
> 
> **🔍 Análisis:**
> 
> - **Sin fricción**: Toda la energía potencial → energía cinética
> - **Con fricción**: Parte de la energía potencial → energía térmica (Q)

---

## 🔗 Relaciones con Otros Temas

> [!info] Conexiones Conceptuales
> 
> ```mermaid
> mindmap
>   root)⚡ Principio de Energía(
>     🔨 Trabajo-Energía Cinética
>       Caso particular
>       W_neto = ΔK
>     🌟 Fuerzas Conservativas
>       Definen U
>       Gravedad, resortes
>     💨 Fuerzas No Conservativas  
>       Fricción
>       Disipan energía
>     📐 Segunda Ley Newton
>       Formulación alternativa
>       Mismos fenómenos
> ```

---

## 📈 Interpretación Gráfica

> [!note] Gráfica Fuerza vs. Desplazamiento
> 
> ```mermaid
> graph LR
>     A["📊 F vs x"] --> B["📐 Área bajo curva"]
>     B --> C["= Trabajo realizado"]
>     C --> D{"🤔 ¿Fuerza conservativa?"}
>     D -->|Sí| E["W = -ΔU"]
>     D -->|No| F["W = energía disipada"]
> ```

---

## 🎯 Ejemplos de Aplicación

> [!example] Ejercicio 1: Bloque en Plataforma
> 
> **🎯 Problema**: Bloque de 5.0 kg, velocidad inicial 10 m/s, se detiene a los 5.0 m.
> 
> ```mermaid
> sequenceDiagram
>     participant I as 🚀 Estado Inicial
>     participant F as 🛑 Estado Final
>     I->>F: v₀ = 10 m/s → v = 0
>     Note over I,F: W_normal < 0 (contra movimiento)
>     Note over I,F: W_gravedad > 0 (favor movimiento)
>     Note over I,F: W_total = ΔK < 0
> ```

> [!success] Ejercicio 2: Caja con Resorte
> 
> **🎯 Problema**: Caja 2.0 kg a 3.0 m/s comprime un resorte.
> 
> **🔧 Solución**: Conservación de energía mecánica $\frac{1}{2}mv^2 = \frac{1}{2}kx^2$

> [!warning] Ejercicio 3: Masa en Curva Sin Fricción
> 
> **🎯 Problema**: Masa desde altura h, velocidad al final.
> 
> ```mermaid
> graph TD
>     A["🏔️ Altura h<br/>v = 0<br/>E = mgh"] --> B["🏁 Suelo<br/>h = 0<br/>E = ½mv²"]
>     A -.-> C["mgh = ½mv²"]
> ```

> [!quote] Ejercicio 4: Superficie Rugosa
> 
> **🎯 Problema**: Masa con fricción, distancia hasta detenerse.
> 
> **🔧 Análisis**: $\Delta U = W_{fricción} = \Delta E_{term}$

> [!info] Ejercicio 5: Resorte en Plano Inclinado
> 
> **🎯 Problema**: Objeto comprime resorte, velocidad en equilibrio.
> 
> **🔧 Solución**: $\frac{1}{2}kx^2 = \frac{1}{2}mv^2$

---

## 🎯 Estrategia de Resolución

> [!tip] Metodología de Resolución
> 
> ```mermaid
> flowchart TD
>     A[📋 Identificar sistema] --> B[🎯 Estados inicial/final]
>     B --> C{🤔 ¿Fuerzas externas?}
>     C -->|No| D[✅ Conservación energía]
>     C -->|Sí| E[⚡ Principio energía general]
>     D --> F[📝 Aplicar ecuaciones]
>     E --> F
>     F --> G[✨ Resolver]
> ```

---

## 💡 Tips y Trucos

> [!success] Consejos Prácticos 🎯 **Consejo Principal**: Siempre identifica primero qué tipos de energía están presentes en el sistema antes de aplicar las ecuaciones.

> [!warning] Mejores Prácticas
> 
> - **✅ Do**: Dibuja diagramas de energía para visualizar las transformaciones
> - **❌ Don't**: Olvides considerar la fricción cuando esté presente
> - **🔍 Recuerda**: El trabajo de fuerzas conservativas es independiente del camino

---

## 🔗 Enlaces y Referencias

> [!quote] Notas relacionadas
> 
> - [[Trabajo y Energía]]
> - [[Principios de Conservación de la Energía]]
> - [[Leyes de Newton]]

---

## 📌 Resumen Ejecutivo

> [!summary] Puntos Clave El **Principio de Energía** es una herramienta fundamental que permite:
> 
> - 🔄 Analizar transformaciones energéticas
> - 📊 Resolver problemas sin usar F=ma directamente
> - 🎯 Entender el comportamiento de sistemas complejos
> - ⚖️ Aplicar conservación cuando sea apropiado
> 
> **🌟 Ecuación clave**: $W_{ext} = \Delta K + \Delta U + \Delta E_{term}$