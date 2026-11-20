---
dg-publish: true
tags: [FISG1001, unidad3, fisica-mecanica, trabajo-energia, diagramas-de-energia]
---

# 📊 Diagramas de Energía

## 🧠 Contexto Fundamental

> [!info] 📖 Definición Los **diagramas de energía** son herramientas gráficas que permiten analizar el movimiento de un objeto en sistemas donde solo actúan **fuerzas conservativas**. Al graficar la energía potencial en función de la posición, podemos determinar de manera intuitiva el movimiento, energía cinética, puntos de retorno y posiciones de equilibrio.
>
> [!success] **Aplicaciones principales:**
>
>- 🎯 Análisis de movimiento oscilatorio
>- 🚀 Predicción de trayectorias
>- ⚖️ Identificación de puntos de equilibrio
>- 🔄 Estudio de sistemas conservativos

---

## 📊 Variables y Magnitudes Físicas

### 🔢 Variables Fundamentales

> [!tip] Variables Fundamentales
>
>| Símbolo | Magnitud | Unidad SI | Descripción |
>|---------|----------|-----------|-------------|
>| U | Energía Potencial | J (Joule) | Energía almacenada en el sistema |
>| E | Energía Total | J | Suma constante: E = K + U |
>| K | Energía Cinética | J | Energía de movimiento |
>| x | Posición | m | Coordenada espacial |
>| F_x | Fuerza | N | Fuerza en dirección x |

### ⚡ Relaciones Energéticas

> [!note] 🖼️ Relaciones Energéticas
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Diagramas_de_Energía_01.svg]]
>
> **Se lee así:** El diagrama monta la aritmética de la energía total: **E = K + U**, y de ahí salen dos lecturas — la energía cinética es lo que queda al restar (`K = E − U`) y la fuerza asociada es el **gradiente negativo** del potencial (`F_x = −dU/dx`).
>
> **Por qué importa:** Son las dos operaciones opuestas que se usan todo el tiempo: para pasar de U a K se resta, y para pasar de U a la fuerza se deriva con signo cambiado. Si la fuerza sale negativa, la energía potencial está creciendo en esa dirección.

---

## 🧮 Fórmulas Fundamentales

### 📐 Ecuaciones Clave

> [!note] 📝 Conservación de Energía Mecánica **Energía total mecánica:** $$E = K + U = \text{constante}$$
>

> [!tip] 💡 Energía Cinética desde el Diagrama **Energía cinética:** $$K = E - U$$ _La energía cinética es la distancia vertical entre la línea de energía total y la curva de energía potencial_
>

> [!warning] ⚠️ Relación Fuerza-Potencial **Fuerza conservativa:** $$F_x = -\frac{dU}{dx}$$ _La fuerza es el **negativo** de la pendiente de la curva de energía potencial_

---

## 📈 Interpretación del Diagrama

### 🎨 Elementos Visuales

> [!note] 🖼️ Elementos Visuales
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Diagramas_de_Energía_02.svg]]
>
> **Se lee así:** La lectura gráfica del problema: en el eje **Y** va la energía (E, U, K) y en el **X** la posición; la **curva U(x)** es la energía potencial, la **línea E** es la energía total y **horizontal** (se conserva), y la **distancia vertical** entre ellas en cada punto es la energía cinética `K = E − U`.
>
> **Por qué importa:** Es la herramienta visual más útil de la unidad: donde la curva U toca la línea E, K llega a cero y el objeto se detiene; donde la curva está lejos por abajo, el objeto va rápido. Y como E es horizontal, se ve de un vistazo si el movimiento es posible o no en cada región.

### 🔍 Regiones de Movimiento

> [!info] 📖 Condición de Movimiento El objeto **solo puede moverse** en regiones donde: $$E \geq U(x)$$
>
> **Razón:** La energía cinética no puede ser negativa: $K = E - U ≥ 0$

---

## 🎯 Puntos Críticos del Sistema

### 🔄 Puntos de Retorno

> [!tip] 💡 Identificación de Puntos de Retorno **Definición:** Puntos donde $E = U(x)$
>
> **Características:**
>
> - Energía cinética = 0 ($K = 0$)
> - Velocidad = 0 ($v = 0$)
> - El objeto **invierte** su dirección de movimiento

> [!note] 🖼️ Puntos de Retorno
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Diagramas_de_Energía_03.svg]]
>
> **Se lee así:** El ciclo de un cuerpo en un pozo de potencial: **se acerca**, llega al **punto de retorno** donde `v = 0` y `K = 0` (toda la energía es potencial), y después **se aleja** en la dirección opuesta.
>
> **Por qué importa:** Fija el concepto de punto de retorno: el objeto nunca pasa de ahí porque no le alcanza energía cinética. Es la misma idea que la altura máxima de un tiro vertical, solo que dibujada sobre la curva U(x).

### ⚖️ Puntos de Equilibrio

> [!note] 🖼️ ️ Puntos de Equilibrio
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Diagramas_de_Energía_04.svg]]
>
> **Se lee así:** Los tres tipos de **puntos de equilibrio** (donde `F_x = 0`): el **estable**, correspondiente a los **mínimos locales** (`d²U/dx² > 0`, «valles»); el **inestable**, a los **máximos locales** (`d²U/dx² < 0`, «picos»); y el **neutro**, a las **regiones planas** (`d²U/dx² = 0`, «mesetas»).
>
> **Por qué importa:** Convierte la segunda derivada en una intuición: si empujas un objeto en un valle, la fuerza lo devuelve; en un pico, la fuerza lo aleja más. Es el criterio que aparece en oscilaciones, en la estabilidad de las órbitas y en cualquier problema con un potencial dado.

#### 🏔️ Equilibrio Estable

> [!success] ✅ Características
>
> - Ubicación: **Mínimos** de U(x)
> - Comportamiento: Fuerza restauradora
> - Si se desplaza → regresa al equilibrio
> - Ejemplo: Pelota en el fondo de un valle

#### ⛰️ Equilibrio Inestable

> [!danger] 🚨 Características
>
> - Ubicación: **Máximos** de U(x)
> - Comportamiento: Fuerza expulsora
> - Si se desplaza → se aleja del equilibrio
> - Ejemplo: Pelota en la cima de una colina

#### 🏞️ Equilibrio Neutro

> [!note] 📝 Características
>
> - Ubicación: **Regiones planas** de U(x)
> - Comportamiento: Sin fuerza neta
> - Si se desplaza → permanece en nueva posición
> - Ejemplo: Pelota en superficie horizontal

---

## 🔗 Conexiones Conceptuales

> [!note] 🖼️ Conexiones Conceptuales
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Diagramas_de_Energía_05.svg]]
>
> **Se lee así:** El mapa mental conecta los cuatro bloques: el **trabajo de las fuerzas conservativas** (define la energía potencial y su trabajo no depende del camino), la **conservación de la energía** (línea horizontal E y el principio fundamental), el **movimiento oscilatorio** (análisis de oscilaciones, período y amplitud) y la **dinámica de partículas** (predicción de trayectorias y análisis de fuerzas).
>
> **Por qué importa:** Ubica la gráfica U(x) dentro del curso: el trabajo conservativo es lo que permite dibujar la curva, la curva permite leer K, y de ahí sale el análisis de oscilaciones de la unidad de elasticidad.

---

## 🧪 Ejemplos Prácticos Resueltos

### 📈 Ejercicio 1: Identificación de Equilibrios

> [!example] 🔍 Análisis de Gráfica U(x) **Problema:** Dada una gráfica de U(x), identificar puntos de equilibrio
>
> **Método:**
>
> 1. Localizar puntos donde `dU/dx = 0`
> 2. Clasificar según la segunda derivada:
>     - $d²U/dx² > 0$ → Estable 🏔️
>     - $d²U/dx² < 0$ → Inestable ⛰️
>     - $d²U/dx² = 0$ → Neutro 🏞️

### 🎯 Ejercicio 2: Análisis de Movimiento

> [!example] 🔍 Puntos de Retorno y Fuerza **Dado:** Gráfica U(x) con línea de energía total E
>
> **Encontrar:**
>
> - **Puntos de retorno:** Intersecciones $E = U(x)$
> - **Dirección de fuerza:** $F_x = -dU/dx$
>     - Pendiente negativa → Fuerza positiva (→)
>     - Pendiente positiva → Fuerza negativa (←)

### 🚀 Ejercicio 3: Predicción de Trayectoria

> [!example] 🔍 Movimiento de Partícula **Análisis para energía total específica:**
>
> **Resultados:**
>
> - **Velocidad máxima:** En puntos más bajos de U(x)
> - **Velocidad cero:** En puntos de retorno
> - **Región permitida:** Donde E ≥ U(x)
> - **Tipo de movimiento:** Oscilatorio entre puntos de retorno

---

## 💡Tips y Trucos

> [!tip] 💡 Consejos Prácticos **🎯 Análisis Sistemático:**
>
> - Siempre identifica primero los puntos de equilibrio
> - Dibuja la línea de energía total antes de analizar
> - La energía cinética es proporcional al "espacio libre" entre $E$ y $U(x)$
>
> **✅ Hacer:**
>
> - Verificar que $E ≥ U$ en toda la región de movimiento
> - Usar la pendiente para determinar dirección de fuerzas
> - Relacionar valles con movimiento oscilatorio
>
> **❌ Evitar:**
>
> - Confundir puntos de equilibrio con puntos de retorno
> - Olvidar el signo negativo en $F_x = -dU/dx$
> - Ignorar las restricciones energéticas del movimiento

---

## 🔄 Relación con Otros Temas

> [!quote] 📝 Vínculos Conceptuales
>
> - [[Trabajo y Energía]] - Fundamento teórico
> - [[Principios de Conservación de la Energía]] - Condición de aplicabilidad
> - [[Leyes de Newton]] - Aplicación práctica

---

## 📋 Síntesis de Información

> [!summary] 📋 Puntos Clave **🎨 Elementos del Diagrama:**
>
> - Gráfica de U(x) vs. x
> - Línea horizontal de energía total E
>
> **⚡ Relaciones Fundamentales:**
>
> - Fuerza: $F_x = -dU/dx$` (negativo de la pendiente)
> - Energía cinética: $K = E - U$ (distancia vertical)
>
> **🎯 Características del Movimiento:**
>
> - Movimiento limitado a regiones donde $E ≥ U$
> - Puntos de retorno donde $E = U$
> - Equilibrio estable en valles, inestable en picos


**Tags:** #FISG1001 #fisica-mecanica #unidad3 #diagramas-de-energia
