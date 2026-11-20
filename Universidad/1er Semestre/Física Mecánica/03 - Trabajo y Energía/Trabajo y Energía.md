---
dg-publish: true
tags: [FISG1001, unidad3, fisica-mecanica, trabajo-energia, trabajo-y-energia]
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_01.svg]]
>
> **Se lee así:** Los **signos del trabajo** en `W = F d cosθ`: con `θ < 90°` el trabajo es positivo (**la energía entra al objeto**), con `θ = 90°` es cero (**la fuerza no aporta energía**) y con `θ > 90°` es negativo (**la fuerza quita energía**), siendo la fricción el caso típico con `θ = 180°`. Los ejemplos: el peso da `+mgh` al bajar y `−mgh` al subir, y la normal da cero en un movimiento horizontal constante.
>
> **Por qué importa:** El signo no es convención: dice si la fuerza acelera o frena. Por eso el peso puede hacer trabajo positivo o negativo según el sentido, mientras que la normal, al ser perpendicular, nunca aporta ni quita energía en el caso horizontal.
>

> [!info] Interpretación Física
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_02.svg]]
>
> **Se lee así:** El trabajo neto y sus equivalencias: `W neto = Σ trabajos` de cada fuerza, o directamente `(ΣF)·d` con la resultante; los trabajos **se pueden sumar en cualquier orden**, y la **energía potencial del resorte** se escribe `U = ½k(x₁² − x₂²)` porque al conservar energía el trabajo de las fuerzas conservativas se **guarda como U**. Cierra con la **verificación**: la suma de fuerzas debe dar la resultante física real.
>
> **Por qué importa:** Son tres escrituras del mismo número. La última advertencia es la comprobación de coherencia: si al sumar los trabajos individuales no sale la fuerza resultante que diste en el DCL, un signo está mal.

---

## 🛠️ Aplicación Práctica

> [!example] Casos Comunes de Trabajo
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_03.svg]]
>
> **Se lee así:** Los **casos concretos de trabajo**: fuerza constante diagonal `W = Fd cosθ`; peso `W = ±mgh`; normal **cero en horizontal** y sin componente en otro sentido; fricción cinética `W = −μNd` sobre la distancia arrastrada mientras dura el contacto; y resorte por integral `W = −½kΔ(x²)`. La regla de método: **redactar el DCL antes de asignar signos**.
>
> **Por qué importa:** Es la tabla de consulta del tema. El detalle de la fricción es el que más se olvida: la distancia que cuenta es la que el cuerpo recorre **deslizándose** sobre la superficie, no la que recorre en el espacio.

---

## 🔗 Relaciones con Otros Temas

> [!abstract] Conexiones Importantes
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_04.svg]]
>
> **Se lee así:** El modelo teórico en una lámina: el **teorema trabajo-energía** (`W total = ΔE cinética`), la **energía externa** medida por la potencia (`P = dW/dt = Fv`), las fuerzas **conservativas** que guardan `U = mgh` o `½kx²`, las **no conservativas** que quitan o agregan energía, el caso de la **cuerda** donde la **polea ideal** da `Στ = 0` y la misma tensión, y el **control de unidades** `N·m = J`.
>
> **Por qué importa:** Reúne las piezas que se combinan en un ejercicio completo: teorema para el movimiento, potencia para la velocidad, y la distinción conservativa/no conservativa para decidir si se usa la conservación de la energía. La verificación de unidades es el chequeo rápido de un resultado raro.

---

## 📈 Interpretación Gráfica

> [!tip] Gráfica Fuerza vs. Desplazamiento
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_05.svg]]
>
> **Se lee así:** La gráfica **F vs desplazamiento** leída por áreas: el **área bajo la curva** es el **trabajo**; para fuerza constante es un **rectángulo** `F·d`, para el resorte un **triángulo** `½kx²`, y para fuerza variable la **integral `∫F(x)dx`**. El signo depende de si la curva está arriba o abajo del eje, según si la fuerza va contra el movimiento. La aplicación típica es el **frenado** visto en la gráfica F-x.
>
> **Por qué importa:** Permite resolver sin integrar: en muchos problemas la gráfica ya está dada y basta medir rectángulos y triángulos. Es el mismo hábito que con v-t y a-t, aplicado ahora a la fuerza.
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_06.svg]]
>
> **Se lee así:** El ejercicio resuelto del pato y el trineo: con `F = 40 N`, `θ = 20°` y `d = 50 m`, el trabajo es `W = F d cos20° = 40 · 50 · 0,9397 ≈ 1879 J`. Como `θ < 90°` el trabajo es positivo: **la fuerza ayuda al movimiento**. La advertencia explícita es usar **cos θ y no sen θ**, porque el ángulo se mide **contra el desplazamiento**.
>
> **Por qué importa:** Es el ejemplo de control para no confundir la trigonometría: el coseno es el que proyecta la fuerza sobre la dirección del movimiento, y ese proyectado es el único que trabaja.
>
> **🔧 Solución**: $$W = Fd\cos\theta = (40 \text{ N})(50 \text{ m})\cos(20°) = 1879.38 \text{ J}$$
>
> **✅ Resultado**: W > 0 porque la fuerza ayuda al movimiento
>

> [!example] Ejercicio 2: Bloque Empujado 📦
>
> **🎯 Problema**: Bloque 10 kg empujado 2 m con F = 10 N a 30°, μ = 0.3
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_07.svg]]
>
> **Se lee así:** La primera mitad del bloque empujado: con `m = 10 kg`, `F = 10 N` a `30°` y `d = 2 m`, el trabajo del empuje es `W_F = 10 · 2 · cos30° = 17,32 J`; la normal y el peso dan **cero** por ser perpendiculares; y falta la fricción, que requiere antes la normal `N = mg − F sin30° = 98,1 − 5 = 93,1 N`, de donde `f_k = μN = 0,3 · 93,1 = 27,93 N` y `W_fricción = −55,86 J`.
>
> **Por qué importa:** Ilustra el orden obligatorio: **primero la normal, después la fricción, y solo al final el trabajo**. Y muestra que la componente vertical del empuje aligera la normal, por eso la fricción es menor de lo que daría el peso solo.
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_08.svg]]
>
> **Se lee así:** El cierre del mismo ejercicio: `W_F = 17,32 J`, `W_N = W_peso = 0`, `W_fricción = −55,86 J`, así que `W neto = 17,32 − 55,86 = −38,54 J`. Como es **menor que cero, el bloque se desacelera**, y el resultado es **coherente con el teorema trabajo-energía**.
>
> **Por qué importa:** Es la comprobación de sentido: un trabajo neto negativo significa que la velocidad disminuye, y eso debe coincidir con lo que diga la segunda ley de Newton. Si los dos métodos dan sentidos distintos, hay un signo mal calculado.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Trabajo_y_Energía_09.svg]]
>
> **Se lee así:** Errores y trucos del trabajo: entre los **errores** están usar la fuerza completa en lugar de `F cosθ`, confundir el desplazamiento con la distancia sobre la curva y olvidar el signo; entre los **trucos**, dibujar el DCL con ángulos reales, fijar un sistema de coordenadas claro y comprobar que el signo tenga sentido físico. La regla que resume todo: **solo la componente paralela a d trabaja**.
>
> **Por qué importa:** Es la checklist previa a cualquier ejercicio de trabajo. El truco del signo es el más útil: si un trabajo sale positivo pero la fuerza claramente frena, el error está en el ángulo, no en la aritmética.

---

## 🔗 Enlaces y Referencias

> [!quote] Notas relacionadas
>
> - [[Principio de energía]]
> - Teorema Trabajo-Energía Cinética
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

**Tags:** #FISG1001 #fisica-mecanica #unidad3 #trabajo-y-energia
