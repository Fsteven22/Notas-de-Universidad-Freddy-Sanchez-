---
dg-publish: true
tags: [FISG1001, unidad3, fisica-mecanica, trabajo-energia, principio-de-energia]
---

# ⚡ Principio de Energía

## 📋 Contexto

> [!abstract] Principio Fundamental La energía total de un sistema aislado se mantiene constante.
>
> Este principio establece que en presencia de fuerzas externas (no conservativas) o interacciones con el entorno, el **trabajo neto externo** realizado sobre un sistema es igual al cambio en su **energía total**.
>

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
>

> [!info] Conservación de Energía Mecánica _Cuando no hay trabajo externo ni fricción:_ $K_{inicial} + U_{inicial} = K_{final} + U_{final}$
>

> [!warning] Relación Fuerza-Energía Potencial $F_x = -\frac{dU}{dx}$
>

> [!tip] Tipos de Energía Potencial
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principio_de_energía_01.svg]]
>
> **Se lee así:** Las dos energías potenciales que se usan en el curso, con sus fórmulas: la **gravitatoria** `U = mgh` y la **elástica** `U = ½kx²`, ambas derivadas de fuerzas conservativas (la gravedad y la fuerza del resorte).
>
> **Por qué importa:** Son las dos que hay que tener presentes al plantear cualquier problema de conservación: si el cambio de energía es de altura, entra `mgh`; si es de deformación, entra `½kx²`; si no hay ninguno de los dos, el trabajo lo hace una fuerza no conservativa.

---

## 🎯 Explicación Teórica

> [!quote] Concepto Fundamental El principio de energía funciona como una **contabilidad energética**:
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principio_de_energía_02.svg]]
>
> **Se lee así:** El flujo de la transformación: una **energía inicial** pasa por un bloque de **transformaciones** —cinética, potencial o térmica— para convertirse en la **energía final**. Cada camino termina en el mismo resultado global.
>
> **Por qué importa:** Es el principio de conservación dibujado como un diagrama de flujo: la energía no desaparece, solo cambia de nombre. El camino térmico es el que marca la diferencia con el caso ideal, porque esa energía ya no se puede recuperar para el movimiento.
>
> Un sistema puede tener múltiples formas de energía que se transforman entre sí. El **trabajo externo** es el mecanismo de transferencia de energía hacia o desde el sistema.

---

## 🛠️ Aplicación Práctica

> [!example] Carro en Plano Inclinado 🚗
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principio_de_energía_03.svg]]
>
> **Se lee así:** El caso del auto que arranca en una altura `h` con `v = 0` y termina en el suelo con `v` desconocida: **sin fricción** la ecuación es `mgh = ½mv²`; **con fricción** aparece un término de calor `Q`, `mgh = ½mv² + Q`.
>
> **Por qué importa:** Muestra el precio de la fricción: la misma altura de partida entrega menos velocidad final porque parte de la energía se disipa. Y muestra el método: restar energía no conservativa desde el inicio en vez de intentar calcular fuerzas.
>
> **🔍 Análisis:**
>
> - **Sin fricción**: Toda la energía potencial → energía cinética
> - **Con fricción**: Parte de la energía potencial → energía térmica (Q)

---

## 🔗 Relaciones con Otros Temas

> [!info] Conexiones Conceptuales
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principio_de_energía_04.svg]]
>
> **Se lee así:** El mapa mental ubica el principio de energía dentro del aparato teórico: el **teorema trabajo-energía** (`W_neto = ΔK`) es su caso particular; las **fuerzas conservativas** definen U (gravedad, resortes); las **no conservativas** como la fricción **disipan** energía; y todo es una **formulación alternativa de la segunda ley de Newton** para los mismos fenómenos.
>
> **Por qué importa:** Aclara la jerarquía: `W_neto = ΔK` siempre vale, mientras que `E_mec = constante` solo vale cuando no hay fuerzas no conservativas. La segunda ley y la conservación de la energía son dos escrituras de la misma física.

---

## 📈 Interpretación Gráfica

> [!note] Gráfica Fuerza vs. Desplazamiento
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principio_de_energía_05.svg]]
>
> **Se lee así:** La decisión a partir de la gráfica **F vs x**: el **área bajo la curva** es el **trabajo realizado**; después hay que preguntarse si la fuerza es **conservativa**: si lo es, `W = −ΔU` (la energía se guarda como potencial); si no lo es, `W` es **energía disipada**.
>
> **Por qué importa:** Es el punto de bifurcación de todos los problemas: antes de escribir una ecuación hay que decidir si la fuerza deja un saldo de energía (conservativa) o se la lleva el calor. Esa decisión determina si se usa la conservación de la energía o el principio general con trabajo externo.

---

## 🎯 Ejemplos de Aplicación

> [!example] Ejercicio 1: Bloque en Plataforma
>
> **🎯 Problema**: Bloque de 5.0 kg, velocidad inicial 10 m/s, se detiene a los 5.0 m.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principio_de_energía_06.svg]]
>
> **Se lee así:** La secuencia de un frenado: el estado inicial va a `v₀ = 10 m/s` y el final a `v = 0`. Las notas registran que el **trabajo de la normal es negativo** (va contra el movimiento), el **trabajo de la gravedad es positivo** (favorable al movimiento) y el **trabajo total** es igual a `ΔK`, que es negativo.
>
> **Por qué importa:** Un ejemplo de signos bien usados: dos fuerzas perpendiculares al desplazamiento no aportan (normal), otra aporta, y la suma da el cambio de energía cinética. El diagrama obliga a evaluar cada trabajo por separado antes de sumar.
>

> [!success] Ejercicio 2: Caja con Resorte
>
> **🎯 Problema**: Caja 2.0 kg a 3.0 m/s comprime un resorte.
>
> **🔧 Solución**: Conservación de energía mecánica $\frac{1}{2}mv^2 = \frac{1}{2}kx^2$
>

> [!warning] Ejercicio 3: Masa en Curva Sin Fricción
>
> **🎯 Problema**: Masa desde altura h, velocidad al final.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principio_de_energía_07.svg]]
>
> **Se lee así:** La cadena del caída libre desde altura `h`: arriba `E = mgh` con `v = 0`, abajo `E = ½mv²` con `h = 0`, y de ahí la igualdad `mgh = ½mv²`.
>
> **Por qué importa:** Es el problema que más se resuelve en el curso y el que mejor ilustra el método: igualar la energía en dos estados, no seguir el movimiento. Nótese que la masa se cancela, así que todos los cuerpos caen igual sin fricción.
>

> [!quote] Ejercicio 4: Superficie Rugosa
>
> **🎯 Problema**: Masa con fricción, distancia hasta detenerse.
>
> **🔧 Análisis**: $\Delta U = W_{fricción} = \Delta E_{term}$
>

> [!info] Ejercicio 5: Resorte en Plano Inclinado
>
> **🎯 Problema**: Objeto comprime resorte, velocidad en equilibrio.
>
> **🔧 Solución**: $\frac{1}{2}kx^2 = \frac{1}{2}mv^2$

---

## 🎯 Estrategia de Resolución

> [!tip] Metodología de Resolución
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principio_de_energía_08.svg]]
>
> **Se lee así:** El procedimiento general de siete pasos: **identificar el sistema**, definir los **estados inicial y final**, preguntar si hay **fuerzas externas** —si no las hay, usar la **conservación de la energía**; si las hay, usar el **principio de energía general**—, **aplicar las ecuaciones** y **resolver**.
>
> **Por qué importa:** El paso 3 es la decisión que organiza todo el ejercicio. Y el paso 1 no es formalismo: el sistema mal delimitado es la causa más frecuente de que la energía «no se conserve», cuando en realidad la que falta está fuera del sistema elegido.

---

## 💡 Tips y Trucos

> [!success] Consejos Prácticos 🎯 **Consejo Principal**: Siempre identifica primero qué tipos de energía están presentes en el sistema antes de aplicar las ecuaciones.
>

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

**Tags:** #FISG1001 #fisica-mecanica #unidad3 #principio-de-energia
