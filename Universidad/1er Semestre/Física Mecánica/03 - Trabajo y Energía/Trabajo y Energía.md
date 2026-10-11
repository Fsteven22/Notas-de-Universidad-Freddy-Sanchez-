---
dg-publish: true
---

# 🔨 Trabajo

## 📋 Contexto

> [!abstract] Definición Fundamental El trabajo describe la **transferencia de energía** a través de la acción de una fuerza.
> 
> El trabajo se realiza cuando una **fuerza actúa sobre un objeto** y este experimenta un **desplazamiento**.
>
> [!warning] Condiciones Importantes
> 
> - ❌ **No hay trabajo sin desplazamiento**
> - ❌ **No hay trabajo si fuerza ⊥ desplazamiento**
> - ✅ **Solo la componente de fuerza paralela al desplazamiento realiza trabajo**

---

## 🔢 Variables Comunes

> [!tip] Variables del Sistema
> 
> |Variable|Símbolo|Unidad|Descripción|
> |---|---|---|---|
> |Trabajo|$W$|J (Julios)|Energía transferida|
> |Fuerza|$\vec{F}$|N (Newtons)|Agente que realiza trabajo|
> |Desplazamiento|$\vec{d}$|m (metros)|Cambio de posición|
> |Ángulo|$\theta$|° (grados)|Entre $\vec{F}$ y $\vec{d}$|
> |Masa|$m$|kg|Cantidad de materia|
> |Gravedad|$g$|9.81 m/s²|Aceleración gravitacional|
>
> [!info] Conversión de Unidades 💡 **Conversión**: $1 \text{ J} = 1 \text{ N} \cdot \text{m}$

---

## 🧮 Fórmulas y Procedimientos

> [!note] Trabajo de Fuerza Constante
> 
> **📐 Definición Escalar** $$W = Fd\cos\theta$$
> 
> **🔢 Definición Vectorial (Producto Punto)** $$W = \vec{F} \cdot \vec{d}$$
>
> [!note] Trabajo Total/Neto
> 
> **🔄 Suma de Trabajos Individuales** $$W_{neto} = \sum W_i = W_{F_1} + W_{F_2} + W_{F_3} + ...$$
> 
> **⚡ Trabajo de la Fuerza Neta** $$W_{neto} = \vec{F}_{neto} \cdot \vec{d} = (\sum \vec{F}) \cdot \vec{d}$$
>
> [!note] Trabajo de un Resorte $$W_e = \frac{1}{2}k(x_i^2 - x_f^2)$$

---

## 🎯 Explicación Teórica

> [!example] Signos del Trabajo según el Ángulo
> 
> ```mermaid
> graph TD
>     A[🔨 Trabajo] --> B{📐 Ángulo θ}
>     B -->|θ < 90°| C[✅ W > 0<br/>Fuerza ayuda al movimiento<br/>⚡ Energía AL objeto]
>     B -->|θ = 90°| D[⚪ W = 0<br/>Fuerza perpendicular<br/>🚫 Sin transferencia]
>     B -->|θ > 90°| E[❌ W < 0<br/>Fuerza opone movimiento<br/>⚡ Energía DEL objeto]
> ```
>
> [!info] Interpretación Física
> 
> ```mermaid
> flowchart LR
>     A[💪 Fuerza] --> B[📏 Componente Paralela]
>     B --> C[🔨 Realiza Trabajo]
>     A --> D[📐 Componente Perpendicular]
>     D --> E[🚫 No realiza trabajo]
> ```

---

## 🛠️ Aplicación Práctica

> [!example] Casos Comunes de Trabajo
> 
> ```mermaid
> mindmap
>   root)🔨 Trabajo(
>     🔥 Fricción
>       Siempre W < 0
>       θ = 180°
>       Se opone al movimiento
>     🌍 Gravedad (horizontal)
>       W = 0
>       θ = 90°
>       Perpendicular
>     📐 Plano Inclinado
>       Subir: W < 0
>       Bajar: W > 0
>       Depende dirección
>     📏 Normal
>       Generalmente W = 0
>       θ = 90°
>       Perpendicular al movimiento
> ```

---

## 🔗 Relaciones con Otros Temas

> [!abstract] Conexiones Importantes
> 
> ```mermaid
> graph LR
>     A[🔨 Trabajo] --> B[⚡ Principio de Energía]
>     B --> C[W = mecanismo de<br/>transferencia de energía]
>     A --> D[🏃 Teorema W-K]
>     D --> E[W_neto = ΔK]
>     A --> F[📐 Segunda Ley Newton]
>     F --> G[Formulación alternativa<br/>para resolver problemas]
> ```

---

## 📈 Interpretación Gráfica

> [!tip] Gráfica Fuerza vs. Desplazamiento
> 
> ```mermaid
> graph TD
>     A["📈 Gráfica F vs x"] --> B["📐 Área bajo la curva"]
>     B --> C["= Trabajo realizado"]
>     C --> D[🌀 Especialmente útil para<br/>fuerzas variables como resortes]
> ```
> 
> **🎯 Casos Especiales:**
> 
> - **🔧 Fuerza constante**: Área = rectángulo
> - **🌀 Resorte**: Área = triángulo
> - **📈 Fuerza variable**: Integral definida

---

## 🎯 Ejemplos de Aplicación

> [!example] Ejercicio 1: Pato Jalando Trineo 🦆
> 
> **🎯 Problema**: Pato jala trineo con 40 N a 20°, moviéndolo 50 m.
> 
> ```mermaid
> graph LR
>     A["🦆 Pato<br/>F = 40 N<br/>θ = 20°"] --> B["🛷 Trineo<br/>d = 50 m"]
>     A -.-> C["W = Fd cos θ"]
> ```
> 
> **🔧 Solución**: $$W = Fd\cos\theta = (40 \text{ N})(50 \text{ m})\cos(20°) = 1879.38 \text{ J}$$
> 
> **✅ Resultado**: W > 0 porque la fuerza ayuda al movimiento
>
> [!example] Ejercicio 2: Bloque Empujado 📦
> 
> **🎯 Problema**: Bloque 10 kg empujado 2 m con F = 10 N a 30°, μ = 0.3
> 
> ```mermaid
> sequenceDiagram
>     participant F as 💪 Fuerza Empuje
>     participant N as 📏 Normal  
>     participant G as 🌍 Gravedad
>     participant Fr as 🔥 Fricción
>     F->>F: W_F = Fd cos 30° = +17.32 J
>     N->>N: W_N = 0 J (θ = 90°)
>     G->>G: W_g = 0 J (θ = 90°)
>     Fr->>Fr: W_f = -55.86 J (θ = 180°)
>     Note over F,Fr: W_neto = -38.54 J
> ```
> 
> **🔍 Análisis Detallado:**
> 
> **1️⃣ Trabajo de la Fuerza de Empuje:** $$W_F = Fd\cos\theta = (10)(2)\cos(30°) = 17.32 \text{ J}$$ ✅ **Positivo**: ayuda al movimiento
> 
> **2️⃣ Trabajo de la Normal y Gravedad:** $$W_N = W_g = 0 \text{ J}$$ ⚪ **Cero**: fuerzas perpendiculares al desplazamiento
> 
> **3️⃣ Trabajo de la Fricción:**
> 
> Primero calculamos la fuerza normal: $$N = mg - F\sin\theta = (10)(9.81) - (10)\sin(30°) = 93.1 \text{ N}$$
> 
> Luego la fuerza de fricción: $$f_k = \mu_k N = (0.3)(93.1) = 27.93 \text{ N}$$
> 
> Finalmente el trabajo: $$W_f = f_k d\cos(180°) = (27.93)(2)(-1) = -55.86 \text{ J}$$ ❌ **Negativo**: se opone al movimiento
> 
> **4️⃣ Trabajo Neto:** $$W_{neto} = 17.32 + (-55.86) = -38.54 \text{ J}$$ 🎯 **Interpretación**: $W_neto < 0$ → El bloque se desacelera

---

## 🎯 Estrategia de Resolución

> [!tip] Metodología de Resolución
> 
> ```mermaid
> flowchart TD
>     A[📋 Identificar todas las fuerzas] --> B[📐 Determinar ángulos con desplazamiento]
>     B --> C[🔢 Calcular trabajo individual]
>     C --> D[➕ Sumar todos los trabajos]
>     D --> E[📊 Interpretar resultado]
>     E --> F{W_neto}
>     F -->|> 0| G[⚡ Objeto acelera]
>     F -->|= 0| H[↔️ Velocidad constante]  
>     F -->|< 0| I[🛑 Objeto desacelera]
> ```

---

## 💡 Tips y Casos Especiales

> [!warning] Errores Comunes
> 
> - ❌ Usar la magnitud total de fuerza en lugar de la componente
> - ❌ Confundir desplazamiento con distancia recorrida
> - ❌ Olvidar el signo del trabajo
>
> [!tip] Trucos Útiles
> 
> - ✅ Dibuja siempre un diagrama de fuerzas
> - ✅ Define un sistema de coordenadas claro
> - ✅ Verifica que los signos tengan sentido físico
>
> [!example] Casos Especiales
> 
> ```mermaid
> graph TD
>     A[🔨 Casos Especiales] --> B[🔄 Movimiento Circular]
>     A --> C[🌀 Fuerzas Variables]
>     A --> D[🎢 Trayectorias Curvas]
>     B --> E[Fuerza centrípeta W = 0]
>     C --> F[Usar integración o gráficas]
>     D --> G[Solo importa desplazamiento neto]
> ```

---

## 🔗 Enlaces y Referencias

>[!quote] Notas relacionadas
> 
> - [[Principio de energía]]
> - [[Teorema Trabajo-Energía Cinética]]
> - [[Leyes de Newton]]
> - [[Fuerzas y Diagramas de Cuerpo Libre]]

---

## 📌 Resumen Ejecutivo

> [!summary] Puntos Clave El **Trabajo** es la medida de transferencia de energía mediante fuerzas:
> 
> - 🔑 **Ecuación clave**: $W = Fd\cos\theta$
> - 📊 **Interpretación gráfica**: Área bajo curva F vs x
> - ➕ **Principio de superposición**: $W_{total} = \sum W_i$
> - 🎯 **Signo indica dirección**: Positivo ayuda, negativo opone
> 
> **🌟 Regla de oro**: Solo la componente de fuerza paralela al desplazamiento realiza trabajo.
