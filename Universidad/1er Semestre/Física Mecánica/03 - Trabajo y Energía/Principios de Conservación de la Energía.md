---
dg-publish: true
---

# ⚡ Principios de Conservación de la Energía

## 📋 Contexto General

> [!abstract] Concepto Central La energía total de un sistema se mantiene constante bajo la acción de fuerzas conservativas.
> 
> Este tema abarca el estudio completo de la energía en sistemas físicos, introduciendo conceptos fundamentales como energía cinética (movimiento) y energía potencial (posición). Los principios de conservación son herramientas poderosas que permiten analizar el movimiento sin usar directamente las leyes de Newton.
>
> [!info] Enfoque Principal
> 
> ```mermaid
> mindmap
>   root)⚡ Conservación Energía(
>     🏃 Energía Cinética
>       Movimiento
>       Velocidad
>     📍 Energía Potencial
>       Posición
>       Fuerzas conservativas
>     🔄 Conservación
>       Intercambio K ↔ U
>       Energía total constante
>     🔨 Trabajo
>       Transferencia energía
>       Fuerzas no conservativas
> ```

---

## 🔢 Variables Comunes del Sistema

> [!tip] Variables del Sistema
> 
> |Variable|Símbolo|Unidad|Descripción|
> |---|---|---|---|
> |Energía Cinética|$K$ o $E_k$|J|Energía de movimiento|
> |Energía Potencial|$U$ o $E_p$|J|Energía de posición|
> |Energía Mecánica|$E_{mec}$|J|$K + U$ total del sistema|
> |Trabajo|$W$|J|Transferencia de energía|
> |Masa|$m$|kg|Cantidad de materia|
> |Velocidad|$v$|m/s|Rapidez del movimiento|
> |Altura|$h$|m|Posición vertical|
> |Constante resorte|$k$|N/m|Rigidez elástica|
> |Desplazamiento|$x$|m|Distancia desde equilibrio|

---

## 🏃 Teorema de Trabajo y Energía Cinética

> [!note] Fórmulas Fundamentales
> 
> **💫 Energía Cinética** $$K = \frac{1}{2}mv^2$$
> 
> **⚡ Teorema Principal** $$W_{neto} = \Delta K = K_{final} - K_{inicial}$$
>
> [!abstract] Explicación Teórica
> 
> ```mermaid
> flowchart LR
>     A[🔨 Trabajo Neto] --> B[📈 Cambio en K]
>     B --> C[⚡ Nueva velocidad]
>     A -.-> D[Reformulación de<br/>Segunda Ley Newton]
> ```
> 
> Este teorema reformula la Segunda Ley de Newton: **el trabajo total realizado por todas las fuerzas sobre una partícula es igual al cambio en su energía cinética**.
>
> [!example] Aplicación Práctica
> 
> **🎯 Caso Típico**:
> 
> - ✅ Empujas una caja → $W > 0$ → $K$ aumenta
> - ❌ Fricción la detiene → $W < 0$ → $K$ disminuye
>
> [!info] Relación con Otros Temas
> 
> - **📐 Segunda Ley Newton**: Trabajo = Fuerza × desplazamiento
> - **⚡ Principio Energía**: Caso particular donde solo cambia $K$
>
> [!tip] Interpretación Gráfica
> 
> ```mermaid
> graph TD
>     A["📊 Gráfica F vs x"] --> B["📐 Área bajo curva"]
>     B --> C["= Trabajo realizado"]
>     C --> D["= Cambio en energía cinética"]
> ```
>
> [!example] Ejemplo: Bala que se Detiene 💥
> 
> **🎯 Problema**: Bala de 0.01 kg a 300 m/s se detiene en 0.06 m en un tronco.
> 
> ```mermaid
> sequenceDiagram
>     participant B as 💥 Bala (v₀ = 300 m/s)
>     participant T as 🌳 Tronco
>     participant F as 🛑 Reposo (v = 0)
>     B->>T: Penetra 0.06 m
>     T->>F: Fuerza de resistencia
>     Note over B,F: W_neto = ΔK
> ```
> 
> **🔧 Solución**: $$W_{neto} = \Delta K = K_{final} - K_{inicial}$$ $$-F_{prom} \cdot d = 0 - \frac{1}{2}mv_{inicial}^2$$ $$F_{prom} = \frac{1}{2}\frac{mv_{inicial}^2}{d} = \frac{1}{2}\frac{(0.01)(300)^2}{0.06} = 7500 \text{ N}$$
>
> [!summary] Síntesis 🔑 **Concepto Clave**: El trabajo neto realizado sobre un objeto es igual al cambio en su energía cinética.

---

## 🌟 Energías Conservativas y No Conservativas

> [!note] Relación Fuerza-Energía Potencial $$F_x = -\frac{dU}{dx}$$
>
> [!abstract] Explicación Teórica
> 
> ```mermaid
> graph TD
>     A[🔋 Fuerzas] --> B{🛤️ ¿Depende de trayectoria?}
>     B -->|NO| C[✅ CONSERVATIVAS]
>     B -->|SÍ| D[❌ NO CONSERVATIVAS]
>     C --> E[🌍 Gravedad<br/>🌀 Resorte<br/>⚡ Eléctrica]
>     D --> F[🔥 Fricción<br/>💨 Resistencia aire<br/>🌊 Viscosidad]
>     C --> G[📍 Definen energía potencial U]
>     D --> H[🔥 Disipan energía como calor]
> ```
>
> [!tip] Fuerzas Conservativas ✅
> 
> - **Definición**: Trabajo independiente de la trayectoria
> - **Característica**: Permiten definir energía potencial $U$
> - **Ejemplos**: Gravedad, resorte, fuerza eléctrica
>
> [!warning] Fuerzas No Conservativas ❌
> 
> - **Definición**: Trabajo depende de la trayectoria
> - **Característica**: Disipan energía como calor
> - **Ejemplos**: Fricción, resistencia del aire
>
> [!example] Ejemplos Comparativos
> 
> **🌍 Gravedad (Conservativa)**
> 
> ```mermaid
> graph TD
>     A["🏔️ Altura 10m"] --> B["🏁 Suelo"]
>     A -.-> C["Trayectoria 1:<br/>Caída libre"]
>     A -.-> D["Trayectoria 2:<br/>Zigzag"]
>     C --> E["W = mgh"]
>     D --> E
> ```
> 
> **Resultado**: Mismo trabajo independiente del camino
> 
> **🔥 Fricción (No Conservativa)**
> 
> ```mermaid
> graph LR
>     A["📦 Punto A"] --> B["📦 Punto B"]
>     A -.-> C["Camino corto<br/>W_fricción pequeño"]
>     A -.-> D["Camino largo<br/>W_fricción grande"]
> ```
> 
> **Resultado**: Más distancia = más trabajo disipado
>
> [!summary] Síntesis 🔑 **Concepto Clave**: Las fuerzas conservativas no dependen de la trayectoria y permiten definir energía potencial. Las no conservativas disipan energía.

---

## 📍 Energías Potenciales

> [!note] Fórmulas por Tipo
> 
> **🌍 Energía Potencial Gravitatoria** $$U_g = mgh$$
> 
> **🌀 Energía Potencial Elástica** $$U_e = \frac{1}{2}kx^2$$
>
> [!abstract] Explicación Teórica
> 
> ```mermaid
> flowchart TD
>     A[📍 Energía Potencial] --> B[💤 Energía "almacenada"]
>     B --> C[📍 Depende de posición/configuración]
>     C --> D[🔄 Puede convertirse en cinética]
>     D --> E[⚡ Cuando objeto se mueve]
> ```
> 
> **Definición**: Energía que posee un objeto debido a su posición o configuración respecto a una fuerza conservativa. Es energía "almacenada" con potencial de convertirse en otras formas.
>
> [!example] Aplicaciones Prácticas
> 
> **🏊 Clavadista (Gravitatoria)**
> 
> ```mermaid
> graph TD
>     A["🏊 Trampolín alto<br/>U_g = mgh<br/>K = 0"] --> B["🏊 Cayendo<br/>U_g disminuye<br/>K aumenta"]
>     B --> C["💦 Al agua<br/>U_g = 0<br/>K = máxima"]
> ```
> 
> **🎯 Resortera (Elástica)**
> 
> ```mermaid
> graph LR
>     A["🎯 Resortera estirada<br/>U_e = ½kx²<br/>K = 0"] --> B["🎯 Liberas<br/>U_e disminuye<br/>K aumenta"]
>     B --> C["🪨 Piedra volando<br/>U_e = 0<br/>K = máxima"]
> ```
>
> [!tip] Interpretación Gráfica
> 
> **📊 Gráfica U vs x**
> 
> ```mermaid
> graph TD
>     A["📈 Gráfica U vs posición"] --> B["📐 Pendiente = -F"]
>     B --> C["🎯 Mínimos = equilibrio estable"]
>     B --> D["⚡ Máximos = equilibrio inestable"]
> ```
> 
> **🎯 Puntos Clave**:
> 
> - **Equilibrio estable**: Mínimos de $U$ (pelota en valle)
> - **Equilibrio inestable**: Máximos de $U$ (pelota en cima de colina)
>
> [!summary] Síntesis 🔑 **Concepto Clave**: La energía potencial es energía almacenada debido a la posición. Existe una para cada fuerza conservativa.

---

## 🔄 Conservación de la Energía Mecánica

> [!note] Fórmula Principal
> 
> **⚖️ Conservación General** $$E_{mecánica} = K + U = \text{constante}$$
> 
> **🔄 Entre Estados** $$K_i + U_i = K_f + U_f$$
>
> [!abstract] Explicación Teórica
> 
> ```mermaid
> flowchart LR
>     A[🏃 Energía Cinética K] --> B[🔄 Intercambio]
>     C[📍 Energía Potencial U] --> B
>     B --> D[⚖️ Suma total constante<br/>E_mec = K + U]
> ```
> 
> **Principio Fundamental**: En sistemas donde solo actúan fuerzas conservativas, la energía mecánica total se conserva. La energía se transforma entre cinética y potencial, pero su suma permanece constante.
>
> [!example] Aplicación: Pelota que Cae ⚽
> 
> ```mermaid
> graph TD
>     A["⚽ Altura máxima<br/>K = 0<br/>U = máxima<br/>E = U"] --> B["⚽ Cayendo<br/>U disminuye<br/>K aumenta<br/>E = K + U"]
>     B --> C["⚽ Suelo<br/>U = 0<br/>K = máxima<br/>E = K"]
>     A -.-> D["E_total = constante"]
>     B -.-> D
>     C -.-> D
> ```
>
> [!example] Ejemplo Detallado: Resbaladilla Sin Fricción 🛝
> 
> **🎯 Problema**: Objeto masa $m$ se suelta desde reposo a altura $h$. ¿Velocidad en la base?
> 
> ```mermaid
> sequenceDiagram
>     participant I as 🏔️ Inicio (altura h)
>     participant F as 🏁 Final (altura 0)
>     I->>I: K₀ = 0, U₀ = mgh
>     I->>F: Conservación energía
>     F->>F: K_f = ½mv², U_f = 0
>     Note over I,F: mgh = ½mv²
> ```
> 
> **🔧 Solución**: $$K_{inicial} + U_{inicial} = K_{final} + U_{final}$$ $$0 + mgh = \frac{1}{2}mv^2 + 0$$ $$v = \sqrt{2gh}$$
> 
> **✨ Resultado**: La velocidad final depende solo de la altura, no de la masa ni la forma de la rampa.
>
> [!info] Casos Especiales
> 
> ```mermaid
> graph TD
>     A[🔄 Conservación Energía] --> B{🤔 ¿Solo fuerzas conservativas?}
>     B -->|SÍ| C[✅ E_mec = constante<br/>Análisis simple]
>     B -->|NO| D[❌ E_mec cambia<br/>Usar principio general]
>     C --> E[🎢 Montaña rusa<br/>🎯 Péndulo<br/>🛝 Rampa lisa]
>     D --> F[🔥 Con fricción<br/>💨 Con resistencia<br/>🔨 Con trabajo externo]
> ```
>
> [!summary] Síntesis 🔑 **Concepto Clave**: En sistemas con solo fuerzas conservativas, la energía mecánica se conserva, intercambiándose continuamente entre energía cinética y potencial.

---

## 🎯 Estrategia General de Resolución

> [!tip] Metodología de Resolución
> 
> ```mermaid
> flowchart TD
>     A[📋 Identificar sistema] --> B[🔍 Clasificar fuerzas]
>     B --> C{🤔 ¿Solo conservativas?}
>     C -->|SÍ| D[⚖️ Usar conservación<br/>K₁ + U₁ = K₂ + U₂]
>     C -->|NO| E[⚡ Usar principio general<br/>W_ext = ΔE_total]
>     D --> F[📝 Definir estados inicial/final]
>     E --> F
>     F --> G[🧮 Aplicar ecuaciones]
>     G --> H[✅ Verificar resultado]
> ```

---

## 🌟 Conexiones entre Subsecciones

> [!abstract] Mapa Conceptual
> 
> ```mermaid
> mindmap
>   root)⚡ Conservación Energía(
>     🔨 Trabajo-Energía K
>       Base teórica
>       W_neto = ΔK
>     🌟 Fuerzas Conservativas
>       Definen U
>       Independientes trayectoria
>     📍 Energías Potenciales
>       Gravitatoria: mgh
>       Elástica: ½kx²
>     🔄 Conservación E_mec
>       K + U = constante
>       Solo fuerzas conservativas
> ```

---

## 🔗 Enlaces y Referencias

> [!quote]  Notas relacionadas
> 
> - [[Trabajo y Energía]]
> - [[Leyes de Newton]]
> - [[Fuerzas y Diagramas de Cuerpo Libre]]
> - [[Principio de energía]]

---

## 📌 Resumen Ejecutivo

> [!summary] Puntos Clave Los **Principios de Conservación de la Energía** establecen que:
> 
> - 🏃 **Teorema W-K**: $W_{neto} = \Delta K$
> - 🌟 **Fuerzas conservativas**: Definen energía potencial $U$
> - 📍 **Energías potenciales**: Gravitatoria ($mgh$) y elástica ($\frac{1}{2}kx^2$)
> - 🔄 **Conservación**: $K + U =$ constante (solo fuerzas conservativas)
> 
> **🎯 Herramienta clave**: Permite resolver problemas complejos sin usar $F = ma$ directamente.
