---
dg-publish: true
tags: [FISG1001, unidad2, fisica-mecanica, dinamica, leyes-de-newton]
---

# ⚖️ Tutorial S10: Leyes de Newton

## 🧠 Contexto
> [!info] Empecemos con un: 
>
> **Enfoque Principal**: Aplicación de las tres leyes de Newton para analizar el movimiento de sistemas complejos.

> [!info] 📖 Contexto
>
> Este tutorial aborda situaciones donde es necesario aplicar las **tres leyes de Newton** de manera integrada para resolver problemas de dinámica. Se enfoca principalmente en sistemas con múltiples objetos, fuerzas complejas y diferentes superficies.

### 🎯 Sistemas de Estudio

> [!note] 🖼️ Sistemas de Estudio
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_01.svg]]
>
> **Se lee así:** Es un mapa mental que abre las tres leyes hacia los cuatro tipos de problemas donde se aplican: **planos inclinados** (con fricción, sin fricción, múltiples masas), **poleas** (sistemas conectados, cuerdas y tensiones, aceleraciones vinculadas), **sistemas conectados** (múltiples objetos, fuerzas internas, análisis independiente) y **fuerzas externas** (empuje y tracción, componentes vectoriales, equilibrio dinámico).
>
> **Por qué importa:** Convierte las leyes en un catálogo de ejercicios: no se estudia la tercera ley en abstracto, se aplica a la fuerza de reacción que hace el suelo sobre una caja. La rama en la que caes te dice qué DCL hay que hacer.

---

## 📌 Variables del Sistema

> [!info] 📊 Variables del Sistema
>
> |Variable|Símbolo|Unidad|Descripción|
> |---|---|---|---|
> |Masa|$m$|kg|Cantidad de materia|
> |Aceleración|$a$|m/s²|Cambio de velocidad|
> |Gravedad|$g$|9.8 m/s²|Aceleración gravitacional|
> |Fuerza Normal|$N$|N|Perpendicular a superficie|
> |Fricción|$f$|N|Oposición al movimiento|
> |Tensión|$T$|N|Fuerza en cuerdas/cables|
> |Peso|$W$|N|$W = mg$|
> |Coeficiente fricción|$\mu$|-|Estático ($\mu_s$) o cinético ($\mu_k$)|

---

## 📐 Formulación General

### ⚖️ Segunda Ley de Newton - Forma Vectorial

> [!info] 📌 ️ Segunda Ley de Newton - Forma Vectorial
>
> $$\sum \vec{F} = m \vec{a}$$

### 🧮 Descomposición por Ejes

#### 📏 Eje X (Horizontal)

> [!info] 📌 Eje X (Horizontal)
>
> $$\sum F_x = m a_x$$

#### 📏 Eje Y (Vertical)

> [!info] 📌 Eje Y (Vertical)
>
> $$\sum F_y = m a_y$$

### 🔥 Fuerza de Fricción

> [!info] 📌 Fuerza de Fricción
>
> $$f = \mu N$$

> [!info] 💡 Fuerza de Fricción
>
> **Donde**:
>
> - $\mu_s$: Coeficiente de fricción estática (objeto en reposo)
> - $\mu_k$: Coeficiente de fricción cinética (objeto en movimiento)

### 🎯 Las Tres Leyes Fundamentales

> [!note] 🖼️ Las Tres Leyes Fundamentales
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_02.svg]]
>
> **Se lee así:** El diagrama despliega las tres leyes con su contenido numérico: la **primera** (inercia) dice que un objeto en reposo o con velocidad constante tiene ΣF = 0; la **segunda** (F = ma) dice que la aceleración es proporcional a la fuerza neta, `a = F/m`; la **tercera** (acción-reacción) agrupa las fuerzas en pares de igual magnitud y direcciones opuestas.
>
> **Por qué importa:** Las tres son una sola idea en tres versiones: si la fuerza neta es cero no hay aceleración; si no lo es, la aceleración es la fuerza neta dividida por la masa. La tercera ley es la que impide sumar ambas fuerzas del par en el mismo DCL.

---

## 🧪 Aplicación Práctica

### 🎯 Tipos de Problemas Característicos

> [!note] 🖼️ Tipos de Problemas Característicos
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_03.svg]]
>
> **Se lee así:** Organiza los problemas típicos por tipo y da la receta de cada uno: **plano inclinado + fricción** (descomponer el peso, calcular la normal, aplicar la fricción), **polea con dos masas** (DCL independientes, vincular aceleraciones, resolver el sistema), **cajas empujadas** (componentes de fuerza, fricción resultante, aceleración neta) y **sistemas múltiples** (análisis por separado, relacionar ecuaciones, solución conjunta).
>
> **Por qué importa:** Cada receta es una lista de pasos que evita el error típico: plantear un solo DCL con todos los cuerpos. El patrón siempre es el mismo — un DCL por objeto y luego una ecuación de vinculo.

---

## 🎯 Metodología de Diagramas de Cuerpo Libre (DCL)

### 📐 Ejemplo: Bloque en Plano Inclinado

> [!note] 🖼️ Ejemplo: Bloque en Plano Inclinado
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_04.svg]]
>
> **Se lee así:** Muestra el DCL de un bloque sobre un plano inclinado de ángulo θ: las cuatro fuerzas son el peso **mg**, la normal **N**, la fricción **f** y la tensión **T**, y el peso se descompone en una componente **perpendicular mg cos θ** y otra **paralela mg sin θ**.
>
> **Por qué importa:** El diagrama separa lo que empuja de lo que frena: solo la componente paralela (mg sin θ) y la fricción compiten entre sí a lo largo del plano, mientras que la normal (fija por mg cos θ) es la que fija cuánto vale la fricción. De ahí sale `f = μN = μmg cos θ`.

### 🧮 Ecuaciones Asociadas

#### 📏 Componentes del Peso

> [!info] 📌 Componentes del Peso
>
> - **Perpendicular al plano**: $W_{\perp} = mg \cos(\theta)$
> - **Paralela al plano**: $W_{\parallel} = mg \sin(\theta)$

#### ⚖️ Equilibrio Perpendicular

> [!info] 📌 ️ Equilibrio Perpendicular
>
> $$N = mg \cos(\theta)$$

#### 🚀 Ecuación de Movimiento (Paralela)

> [!info] 📌 Ecuación de Movimiento (Paralela)
>
> $$ma = mg \sin(\theta) - f - T$$

---

## 📌 Estrategia de Resolución

> [!note] 🖼️ Estrategia de Resolución
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_05.svg]]
>
> **Se lee así:** Es el procedimiento completo en ocho pasos: **1)** identificar el sistema, **2)** hacer el DCL de cada objeto, **3)** definir los ejes coordenados, **4)** descomponer las fuerzas, **5)** aplicar ΣF = ma, **6)** relacionar las aceleraciones, **7)** resolver el sistema y **8)** verificar el resultado.
>
> **Por qué importa:** Los pasos 6 y 8 son los que casi siempre se saltan. Sin vincular las aceleraciones no se puede cerrar el sistema, y sin verificar (unidades, signos, sentido) el resultado numérico no significa nada.

---

## 🧠 Ejemplos de Aplicación

### 🚗 Ejemplo 1: Fuerza Resultante Simple

> [!info] 💡 Ejemplo 1: Fuerza Resultante Simple
>
> **🎯 Problema**: Bloque de 5 kg empujado con 30 N en superficie sin fricción.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_06.svg]]
>
> **Se lee así:** El caso más simple: un bloque de 5 kg al que se le aplica una fuerza de 30 N, y la pregunta es la aceleración. Con la segunda ley, `a = F/m = 30/5 = 6 m/s²`.
>
> **Por qué importa:** Es la segunda ley en estado puro, sin nada que confunda: fuerza conocida y masa conocida dan la aceleración. Sirve para fijar la fórmula antes de subir al caso del plano inclinado, donde la fuerza neta ya no es la fuerza aplicada.
>
> **🔧 Solución**: $$F = ma \Rightarrow a = \frac{F}{m} = \frac{30}{5} = 6 \text{ m/s}^2$$
>
> **✅ Resultado**: $a = 6 \text{ m/s}^2$

---

### 🧱 Ejemplo 2: Plano Inclinado Sin Fricción

> [!info] 💡 Ejemplo 2: Plano Inclinado Sin Fricción
>
> **🎯 Problema**: Bloque 10 kg en plano inclinado 30°, sin fricción.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_07.svg]]
>
> **Se lee así:** Un bloque de 10 kg en un plano inclinado de 30°: lo único que empuja hacia abajo es la componente paralela del peso, **mg sin θ**, y la aceleración se obtiene con `a = g sin θ`.
>
> **Por qué importa:** Muestra que en un plano inclinado sin fricción la aceleración no depende de la masa: da igual 10 kg que 1 kg, siempre `g sin θ`. La masa solo importa cuando hay fricción, porque ahí la normal (y con ella μN) crece con el peso.
>
> **🔧 Solución**:
>
> 1. **Componente paralela del peso**: $$W_{\parallel} = mg \sin(\theta) = 10 \times 9.8 \times \sin(30°) = 49 \text{ N}$$
> 2. **Segunda ley de Newton**: $$a = \frac{F}{m} = \frac{49}{10} = 4.9 \text{ m/s}^2$$
>
> **✅ Resultado**: $a = 4.9 \text{ m/s}^2$

---

### 🧲 Ejemplo 3: Sistema de Masas Conectadas

> [!info] 💡 Ejemplo 3: Sistema de Masas Conectadas
>
> **🎯 Problema**: Dos bloques conectados por cuerda y polea. $m_1 = 4$ kg (horizontal), $m_2 = 2$ kg (colgante).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_08.svg]]
>
> **Se lee así:** El sistema clásico de dos masas unidas por una cuerda y una polea: **m₁ = 4 kg** sobre la mesa, **m₂ = 2 kg** colgante. Sobre m₁ solo actúa la tensión **T**; sobre m₂ se contraponen el peso **m₂g ↓** y la tensión **T ↑**, que es la ecuación que realmente mueve el sistema.
>
> **Por qué importa:** Pone de manifiesto la asimetría: la masa colgante es la única que puede iniciar el movimiento, porque su peso no está equilibrado por nada. La aceleración del sistema sale de combinar `T = m₁a` (mesa, sin fricción) con `m₂g − T = m₂a`.
>
> **🔧 Análisis por DCL**:

#### 📦 Para $m_1$ (horizontal):

> [!info] 📌 Para $m_1$ (horizontal):
>
> $$T = m_1 a \quad \text{...(1)}$$

#### 📦 Para $m_2$ (vertical):

> [!info] 📌 Para $m_2$ (vertical):
>
> $$m_2 g - T = m_2 a \quad \text{...(2)}$$

> [!info] 💡 Para $m_2$ (vertical)
>
> **🧮 Resolución del sistema**: Sustituyendo (1) en (2): $$m_2 g - m_1 a = m_2 a$$ $$m_2 g = a(m_1 + m_2)$$ $$a = \frac{m_2 g}{m_1 + m_2} = \frac{2 \times 9.8}{4 + 2} = 3.27 \text{ m/s}^2$$
>
> **✅ Resultado**: $a = 3.27 \text{ m/s}^2$
>
> **🔗 Tensión en la cuerda**: $$T = m_1 a = 4 \times 3.27 = 13.08 \text{ N}$$

---

## 💡 Recomendaciones Clave

### ✅ Buenas Prácticas

> [!note] 🖼️ Buenas Prácticas
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_09.svg]]
>
> **Se lee así:** Resume la estrategia exitosa en cinco puntos: dibujar **siempre** el DCL, definir **ejes claros**, **descomponer** correctamente, **verificar los signos** y mantener **símbolos consistentes**.
>
> **Por qué importa:** Cada punto ataca un error concreto: los ejes mal definidos cambian el signo de un término sin que se note, y la descomposición mal hecha inventa fuerzas que no existen. Es la lista de control antes de entregar un ejercicio.

> [!info] 📌 Buenas Prácticas
>
> - **📐 DCL primero**: Nunca apliques fórmulas sin dibujar el diagrama
> - **📏 Ejes coherentes**: Define x, y de manera consistente para todo el problema
> - **🧮 Descomposición**: En planos inclinados, descompón peso correctamente
> - **🔍 Signos**: Revisa dirección de aceleración antes de asignar signos
> - **📝 Consistencia**: Usa los mismos símbolos en todo el desarrollo

### ❌ Errores Comunes a Evitar

> [!note] 🖼️ Errores Comunes a Evitar
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_10.svg]]
>
> **Se lee así:** Enumera los errores frecuentes: **no dibujar el DCL**, **confundir masa y peso**, **mal manejo de signos**, **olvidar vincular aceleraciones** y **aplicar la tercera ley en el mismo DCL**.
>
> **Por qué importa:** El quinto es el más sutil: la fuerza de reacción existe, pero vive en el DCL del otro objeto. Meterla en el mismo diagrama hace que las dos fuerzas se cancelen y el cuerpo quede sin aceleración.

---

## 🧠 Conceptos Fundamentales para Recordar

### 🎯 Principios Clave

> [!tip] 🔑 Regla de Oro
>
> Las Leyes de Newton se aplican a cada objeto por separado.

#### 📋 Puntos Esenciales:

> [!info] 📌 Puntos Esenciales:
>
> - **🎯 Análisis independiente**: Cada objeto tiene su propio DCL y ecuaciones
> - **↔️ Tercera ley**: No se aplica dentro del mismo DCL, sino entre objetos
> - **🔗 Sistemas múltiples**: Analiza cada cuerpo por separado, luego relaciona
> - **⚖️ Equilibrio**: $\sum F = 0$ para objetos en reposo o velocidad constante
> - **🚀 Aceleración**: Siempre en dirección de la fuerza neta

### 🌟 Jerarquía de Análisis

> [!note] 🖼️ Jerarquía de Análisis
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Leyes_de_Newton_11.svg]]
>
> **Se lee así:** Es el esquema general para un sistema de n cuerpos: un DCL por objeto (**DCL₁, DCL₂, DCLₙ**), una ecuación por cuerpo (**ΣF₁ = m₁a₁**, etc.), una etapa de **relacionar las aceleraciones** y, con todo eso, un **sistema de ecuaciones** cuya **solución** cierra el problema.
>
> **Por qué importa:** Muestra por qué los sistemas con varias cuerpos no se pueden resolver de un solo golpe: hacen falta tantas ecuaciones como cuerpos, y las aceleraciones no son independientes entre sí. Es la estructura mental detrás de todos los problemas de poleas y de bloques apilados.

---

## 🔗 Conexiones con Otros Temas

> [!info] 📌 Conexiones con Otros Temas
>
> - [[Trabajo y Energía]]
> - [[Principios de Conservación de la Energía]]
> - [[Fuerzas y Diagramas de Cuerpo Libre]]
> - [[Cinemática Traslacional]]

---

## 📌 Resumen Ejecutivo
> [!success] ✅ Resumen: las leyes de Newton
>
> Las **Leyes de Newton** proporcionan el framework fundamental para el análisis dinámico:
>
>- **1️⃣ Primera Ley**: Inercia → $\sum F = 0$ para equilibrio
>- **2️⃣ Segunda Ley**: Dinámica → $\sum F = ma$ para aceleración
>- **3️⃣ Tercera Ley**: Acción-reacción → Fuerzas en pares
>
>**🎯 Metodología clave**: DCL → Descomponer → Aplicar → Relacionar → Resolver
>
>¿Listo para aplicar lo aprendido? 💪✨

**Tags:** #FISG1001 #fisica-mecanica #unidad2 #leyes-de-newton
