---
dg-publish: true
tags: [FISG1001, unidad3, fisica-mecanica, trabajo-energia, principios-de-conservacion-de-la-energia]
---

# ⚡ Principios de Conservación de la Energía

## 📋 Contexto General

> [!abstract] Concepto Central La energía total de un sistema se mantiene constante bajo la acción de fuerzas conservativas.
>
> Este tema abarca el estudio completo de la energía en sistemas físicos, introduciendo conceptos fundamentales como energía cinética (movimiento) y energía potencial (posición). Los principios de conservación son herramientas poderosas que permiten analizar el movimiento sin usar directamente las leyes de Newton.
>

> [!info] Enfoque Principal
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_01.svg]]
>
> **Se lee así:** El mapa mental de la unidad: la **energía cinética** ligada al movimiento y a la velocidad, la **energía potencial** a la posición y a las fuerzas conservativas, la **conservación** como intercambio K ↔ U con energía total constante, y el **trabajo** como mecanismo de transferencia para las fuerzas no conservativas.
>
> **Por qué importa:** Separa las dos formas de cambiar la energía: el intercambio interno entre K y U (que la conserva) y el trabajo externo (que la modifica). Esa distinción es exactamente la que decide qué ecuación se usa en cada problema.

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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_02.svg]]
>
> **Se lee así:** El teorema trabajo-energía en cadena: el **trabajo neto** produce el **cambio en K**, que se traduce en una **nueva velocidad**. El diagrama lo presenta como una **reformulación de la segunda ley de Newton**.
>
> **Por qué importa:** Es el puente entre las dos formas de escribir la dinámica: `F = ma` habla de fuerzas y aceleraciones, `W = ΔK` habla de fuerzas y velocidades. Cuando el problema pide velocidad y no tiempo, el segundo camino es mucho más corto.
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_03.svg]]
>
> **Se lee así:** La lectura gráfica: de la **gráfica F vs x**, el **área bajo la curva** es el **trabajo realizado**, que a su vez es el **cambio en energía cinética**.
>
> **Por qué importa:** Encadena las tres interpretaciones —gráfico, área y energía— en una sola línea. Es la forma más rápida de resolver un problema en que la fuerza varía y solo se pide la velocidad final.
>

> [!example] Ejemplo: Bala que se Detiene 💥
>
> **🎯 Problema**: Bala de 0.01 kg a 300 m/s se detiene en 0.06 m en un tronco.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_04.svg]]
>
> **Se lee así:** La secuencia del impacto: la **bala** parte con `v₀ = 300 m/s`, **penetra 0,06 m** en el **tronco** y el sistema termina en **reposo** (`v = 0`), con una fuerza de resistencia que actúa en el trayecto. La nota global es `W_neto = ΔK`.
>
> **Por qué importa:** Es el problema tipo del teorema trabajo-energía: la fuerza de resistencia es desconocida, pero el cambio de energía cinética está fijado por las velocidades, así que `W = 0 − ½mv²` da directamente la fuerza media sin integrar nada.
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_05.svg]]
>
> **Se lee así:** La clasificación por la pregunta clave: si la fuerza **no depende de la trayectoria** es **conservativa** (gravedad, resorte, eléctrica) y **define una energía potencial U**; si **depende** es **no conservativa** (fricción, resistencia del aire, viscosidad) y **disipa energía como calor**.
>
> **Por qué importa:** Es el criterio operativo, no memorístico: para saber si una fuerza conservativa basta preguntar si el trabajo entre dos puntos cambia si el camino cambia. Y la consecuencia práctica es enorme — si es conservativa, su trabajo se sustituye por un término de energía.
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_06.svg]]
>
> **Se lee así:** La prueba de la conservación: desde los **10 m** hasta el suelo hay dos **trayectorias**, la de **caída libre** y la de **zigzag**, y ambas producen el **mismo trabajo** `W = mgh`.
>
> **Por qué importa:** Demuestra empíricamente el criterio anterior: el trabajo de la gravedad es idéntico por cualquier camino, y por eso se le puede asignar un valor de energía potencial. Si el trabajo dependiera del camino, no existiría U.
>
> **Resultado**: Mismo trabajo independiente del camino
>
> **🔥 Fricción (No Conservativa)**
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_07.svg]]
>
> **Se lee así:** El contraste con la fuerza no conservativa: para ir del **punto A** al **punto B** por el **camino corto** el trabajo de fricción es **pequeño**, y por el **camino largo** es **grande**.
>
> **Por qué importa:** Es la prueba negativa: la fricción sí depende de la trayectoria, así que no tiene energía potencial asociada. Y explica por qué en la práctica el camino importa, a diferencia de la gravedad.
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_08.svg]]
>
> **Se lee así:** La definición de **energía potencial U**: es la **energía almacenada por posición o configuración**, con sus dos formas — **gravitatoria `U_g = mgh`** y **elástica `U_e = ½kx²`** —, y siempre está **definida respecto a una fuerza conservativa**.
>
> **Por qué importa:** La última frase es la condición de existencia: no se puede hablar de energía potencial de la fricción. Y el «configuración» amplía la idea más allá de la altura: un resorte estirado y un resorte comprimido guardan la misma energía aunque estén en el mismo punto.
>
> **Definición**: Energía que posee un objeto debido a su posición o configuración respecto a una fuerza conservativa. Es energía "almacenada" con potencial de convertirse en otras formas.
>

> [!example] Aplicaciones Prácticas
>
> **🏊 Clavadista (Gravitatoria)**
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_09.svg]]
>
> **Se lee así:** El intercambio en un trampolín: arriba, `U_g = mgh` y `K = 0`; **cayendo**, `U_g` disminuye mientras `K` aumenta; **al agua**, `U_g = 0` y `K` es **máxima**.
>
> **Por qué importa:** Es el ejemplo canónico del balance K ↔ U: la suma total no cambia en ningún punto de la caída, solo se mueve de una columna a la otra. Y permite ver que la velocidad máxima ocurre justo donde la altura es cero.
>
> **🎯 Resortera (Elástica)**
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_10.svg]]
>
> **Se lee así:** El mismo intercambio con un resorte: la **resortera estirada** tiene `U_e = ½kx²` y `K = 0`; al **liberarla**, `U_e` disminuye y `K` aumenta; cuando la piedra sale volando, `U_e = 0` y `K` es **máxima**.
>
> **Por qué importa:** Muestra que la conservación no distingue entre tipos de potencial: la gravedad y el resorte intercambian energía con la cinética de la misma manera. Y fija el punto de máxima velocidad: en la posición de reposo del resorte.
>

> [!tip] Interpretación Gráfica
>
> **📊 Gráfica U vs x**
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_11.svg]]
>
> **Se lee así:** La lectura de la **gráfica U vs posición**: la **pendiente es −F**, los **mínimos** corresponden al **equilibrio estable** y los **máximos** al **equilibrio inestable**.
>
> **Por qué importa:** Es la regla de derivación del potencial a fuerza, aplicada visualmente: donde la curva baja, la fuerza empuja hacia la derecha; donde sube, empuja hacia la izquierda. Y la curvatura decide si el equilibrio es recuperable.
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
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_12.svg]]
>
> **Se lee así:** El esquema minimalista de la conservación: la **energía cinética K** y la **potencial U** se **intercambian**, y su **suma total es constante** (`E_mec = K + U`).
>
> **Por qué importa:** Es la ecuación que se escribe una sola vez al principio de un ejercicio y se reutiliza en todos los puntos. Nótese que el intercambio puede ir en cualquier dirección: subir convierte K en U y bajar convierte U en K.
>
> **Principio Fundamental**: En sistemas donde solo actúan fuerzas conservativas, la energía mecánica total se conserva. La energía se transforma entre cinética y potencial, pero su suma permanece constante.
>

> [!example] Aplicación: Pelota que Cae ⚽
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_13.svg]]
>
> **Se lee así:** El caso del balón en tres estados: en la **altura máxima** `K = 0`, `U` es máxima y `E = U`; **cayendo**, `U` disminuye y `K` aumenta (`E = K + U`); en el **suelo**, `U = 0`, `K` es máxima y `E = K`. La rama derecha afirma que `E_total` es **constante** en los tres.
>
> **Por qué importa:** Fija la identidad en los extremos del vuelo: en la altura máxima toda la energía es potencial y en el suelo toda es cinética. Eso permite calcular la velocidad máxima sin conocer la trayectoria intermedia.
>

> [!example] Ejemplo Detallado: Resbaladilla Sin Fricción 🛝
>
> **🎯 Problema**: Objeto masa $m$ se suelta desde reposo a altura $h$. ¿Velocidad en la base?
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_14.svg]]
>
> **Se lee así:** La secuencia formal de la conservación: el estado **inicial** (altura h) tiene `K₀ = 0` y `U₀ = mgh`, se aplica la **conservación de la energía** y el estado **final** (altura 0) queda con `K_f = ½mv²` y `U_f = 0`, lo que produce la nota `mgh = ½mv²`.
>
> **Por qué importa:** Es la escritura paso a paso que conviene copiar en un examen: declarar los dos estados, escribir cada energía por separado y recién entonces igualar. Evita el error de igualar «alturas con velocidades» sin definir de qué energía se habla.
>
> **🔧 Solución**: $$K_{inicial} + U_{inicial} = K_{final} + U_{final}$$ $$0 + mgh = \frac{1}{2}mv^2 + 0$$ $$v = \sqrt{2gh}$$
>
> **✨ Resultado**: La velocidad final depende solo de la altura, no de la masa ni la forma de la rampa.
>

> [!info] Casos Especiales
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_15.svg]]
>
> **Se lee así:** La decisión por tipos de fuerza: si **solo hay fuerzas conservativas**, `E_mec` es **constante** y el análisis es **simple** (montaña rusa, péndulo, rampa lisa); si hay **fuerzas no conservativas**, `E_mec` **cambia** y hay que usar el **principio general** (con fricción, con resistencia del aire, con trabajo externo).
>
> **Por qué importa:** Es el semáforo del problema. Elegir mal aquí es el error más costoso: aplicar `K₁+U₁ = K₂+U₂` con fricción da un resultado incorrecto que parece razonable.
>

> [!summary] Síntesis 🔑 **Concepto Clave**: En sistemas con solo fuerzas conservativas, la energía mecánica se conserva, intercambiándose continuamente entre energía cinética y potencial.

---

## 🎯 Estrategia General de Resolución

> [!tip] Metodología de Resolución
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_16.svg]]
>
> **Se lee así:** El procedimiento completo en ocho pasos: **identificar el sistema**, **clasificar las fuerzas**, preguntar si **solo son conservativas** —si sí, usar `K₁ + U₁ = K₂ + U₂`; si no, usar el **principio general** `W_ext = ΔE_total`—, **definir los estados inicial y final**, **aplicar las ecuaciones** y **verificar el resultado**.
>
> **Por qué importa:** Es la versión ampliada del flujo de la nota anterior, con el paso de clasificación en el centro. La verificación final suele ser de sentido: la energía final no puede ser mayor que la inicial si hubo fricción.

---

## 🌟 Conexiones entre Subsecciones

> [!abstract] Mapa Conceptual
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Principios_de_Conservación_de_la_Energía_17.svg]]
>
> **Se lee así:** El mapa mental de cierre: la base teórica es el **teorema trabajo-energía** (`W_neto = ΔK`); las **fuerzas conservativas** definen U y son **independientes de la trayectoria**; las **energías potenciales** son la **gravitatoria `mgh`** y la **elástica `½kx²`**; y la **conservación de `E_mec`** (`K + U = constante`) vale **solo con fuerzas conservativas**.
>
> **Por qué importa:** Resume la unidad entera en cuatro ideas encadenadas. La advertencia final —«solo fuerzas conservativas»— es la condición que más se olvida al plantear un ejercicio con fricción.

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

**Tags:** #FISG1001 #fisica-mecanica #unidad3 #principios-de-conservacion-de-la-energia
