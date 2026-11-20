---
dg-publish: true
tags: [FISG1001, unidad4, fisica-mecanica, impulso, momentum-lineal-y-su-conservacion]
---

# 🎯 Momentum Lineal y su Conservación

## 🧠 Contexto Fundamental

> [!info] 📖 Definición General El **momentum lineal** (o cantidad de movimiento) es una propiedad vectorial fundamental que describe la "inercia en movimiento" de un objeto. Representa la tendencia de un cuerpo en movimiento a mantener su estado de movimiento, siendo directamente proporcional tanto a su masa como a su velocidad.
>
> [!important] 🏛️ Principio de Conservación El **principio de conservación del momentum** es una de las leyes de conservación más fundamentales de la física, aplicable desde partículas subatómicas hasta sistemas galácticos. Es esencial para analizar colisiones, explosiones y cualquier interacción entre cuerpos.

> [!note] 🖼️ Contexto Fundamental
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Momentum_Lineal_y_Su_Conservación_01.svg]]
>
> **Se lee así:** El diagrama arranca del **momentum individual** `p = mv`, lo suma en el **momentum total** del sistema `P = Σpᵢ` y pregunta **¿`F_ext = 0`?**: si se cumple, el **momentum se conserva** (`P_inicial = P_final`); si no, **cambia** (`ΔP = J_ext`). Los ejemplos de aplicación son **colisiones**, **propulsión** y **deportes**.
>
> **Por qué importa:** Es la condición de uso de toda la unidad. Nótese que la pregunta es sobre las fuerzas **externas** al sistema: si el sistema se elige mal (por ejemplo, incluyendo la pared que empuja), la conservación no parece cumplirse.

---

# 📐 PARTE I: Momentum Lineal

## 📊 Variables y Definiciones

> [!tip] 🔢 Tabla de Variables Fundamentales
>
> |Símbolo|Magnitud|Unidad SI|Tipo|Descripción|
> |---|---|---|---|---|
> |**\vec{p}**|Momentum lineal|kg·m/s|Vectorial|Cantidad de movimiento|
> |**m**|Masa|kg|Escalar|Medida de inercia|
> |**\vec{v}**|Velocidad|m/s|Vectorial|Rapidez y dirección|
> |**\vec{F}**|Fuerza|N|Vectorial|Agente de cambio|
> |**\vec{J}**|Impulso|N·s|Vectorial|Cambio de momentum|
> |**K**|Energía cinética|J|Escalar|Energía de movimiento|

## 🧮 Fórmula Fundamental

### 📐 Definición Básica

> [!note] 📝 Momentum de una Partícula $$\vec{p} = m\vec{v}$$
>
> **Características principales:**
>
> - **Magnitud**: |p| = mv (para velocidades no relativistas)
> - **Dirección**: Idéntica a la velocidad
> - **Dependencia**: Directamente proporcional a masa y velocidad

## 🎯 Propiedades del Momentum

### 📈 Análisis Vectorial

> [!note] 🖼️ Análisis Vectorial
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Momentum_Lineal_y_Su_Conservación_02.svg]]
>
> **Se lee así:** El momentum en una sola lámina: su **magnitud** es `p = mv`, su **dirección** es la de la velocidad y su **sentido** el del movimiento, con **componentes** `px, py, pz`. De él se deriva el **impulso** `J = Δp`, la **energía cinética** `K = p²/2m` y la **fuerza** `F = dp/dt`.
>
> **Por qué importa:** La identidad `K = p²/2m` es la que más se olvida y la más útil: en un choque donde el momentum está fijado, la energía cinética depende solo de la masa. Y `F = dp/dt` es la forma general de la segunda ley de Newton, que cubre masas variables como en los cohetes.

> [!example] 🔍 Análisis en 2D **Para un objeto moviéndose en el plano:**
>
> - **Componente x**: px = mvx
> - **Componente y**: py = mvy
> - **Magnitud total**: |p| = √(px² + py²)
> - **Ángulo**: θ = arctan(py/px)

### 🔄 Relaciones con Otras Magnitudes

> [!info] 🔗 Conexiones Fundamentales
>
> **Con la energía cinética:** $$K = \frac{p^2}{2m} = \frac{mv^2}{2}$$
>
> **Con la fuerza (Segunda Ley de Newton):** $$\vec{F} = \frac{d\vec{p}}{dt} = m\frac{d\vec{v}}{dt} = m\vec{a}$$

---

# ⚖️ PARTE II: Conservación del Momentum

## 🏛️ Principio Fundamental

### 📐 Enunciado de la Ley

> [!warning] ⚠️ Ley de Conservación del Momentum **Condición necesaria:** La fuerza externa neta sobre el sistema debe ser **cero**: $$\sum \vec{F}_{ext} = 0$$
>
> **Consecuencia directa:** El momentum total del sistema se **conserva**: $$\vec{P}_{inicial} = \vec{P}_{final}$$
>
> **Para sistema de n partículas:** $$\sum_{i=1}^{n} \vec{p}_{i,inicial} = \sum_{i=1}^{n} \vec{p}_{i,final}$$

## 🔍 Sistema de Partículas

### 🎯 Análisis de Fuerzas

> [!note] 🖼️ Análisis de Fuerzas
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Momentum_Lineal_y_Su_Conservación_03.svg]]
>
> **Se lee así:** El argumento completo de la conservación: en un **sistema de n partículas** el **momentum total** es `P = Σpᵢ`; las **fuerzas internas** **se cancelan en pares** por la **tercera ley de Newton** y **no afectan** `P_total`; solo las **fuerzas externas** deciden, con la pregunta **¿`ΣF_ext = 0`?** —si sí, **P se conserva**; si no, `P` cambia según `dP/dt = ΣF_ext`.
>
> **Por qué importa:** Es la demostración del porqué: la conservación no es una regla empírica, es una consecuencia directa de la tercera ley. Eso explica por qué vale en colisiones, donde las fuerzas de contacto son enormes pero internas al sistema.

> [!info] 📖 Fuerzas Internas vs Externas
>
> **🔄 Fuerzas internas:**
>
> - Actúan entre partículas del sistema
> - Se cancelan por la Tercera Ley de Newton
> - **No cambian** el momentum total del sistema
>
> **🌍 Fuerzas externas:**
>
> - Actúan desde fuera del sistema
> - **Pueden cambiar** el momentum total
> - Su suma vectorial determina si se conserva

## 🎯 Condiciones de Aplicación

### ✅ Cuándo se Conserva el Momentum

> [!success] ✅ Sistemas Aplicables
>
> **🔒 Sistemas completamente aislados:**
>
> - Sin fuerzas externas (ΣF_ext = 0)
> - Colisiones en tiempo muy corto
> - Explosiones internas
> - Sistemas en el espacio profundo
>
> **⚖️ Sistemas con fuerzas externas despreciables:**
>
> - Colisiones rápidas (gravedad despreciable en tiempo corto)
> - Superficies sin fricción
> - Fuerzas externas << fuerzas internas durante la interacción

### ❌ Limitaciones del Principio

> [!warning] ⚠️ Cuándo NO se Conserva
>
> **Presencia de fuerzas externas significativas:**
>
> - 🌍 Gravedad no compensada
> - 🔥 Fricción considerable
> - ⚡ Fuerzas electromagnéticas externas
> - 💨 Resistencia del aire importante
> - 🌊 Fuerzas de fluidos

---

## 🛠️ Aplicaciones Fundamentales

### 💥 Tipos de Colisiones

#### 🔗 Colisión Perfectamente Inelástica

> [!note] 🖼️ Colisión Perfectamente Inelástica
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Momentum_Lineal_y_Su_Conservación_04.svg]]
>
> **Se lee así:** La colisión perfectamente inelástica en tres pasos: **antes** `m₁v₁ + m₂v₂`, la colisión donde **se unen**, y **después** `(m₁+m₂)v_f`. El resultado: **se conserva el momentum** y **se pierde energía cinética**.
>
> **Por qué importa:** Es la plantilla más corta de la unidad: una sola ecuación, `m₁v₁ + m₂v₂ = (m₁+m₂)v_f`, que da directamente la velocidad final. Y marca la asimetría central — el momentum nunca se pierde, la energía sí.

> [!example] 🔍 Fórmula para Choque Inelástico **Objetos que se unen tras la colisión:** $$m_1\vec{v}_{1i} + m_2\vec{v}_{2i} = (m_1 + m_2)\vec{v}_f$$
>
> **Velocidad final del sistema:** $$\vec{v}_f = \frac{m_1\vec{v}_{1i} + m_2\vec{v}_{2i}}{m_1 + m_2}$$

#### ⚾ Colisión Perfectamente Elástica

> [!tip] 💡 Doble Conservación **Se conservan ambas magnitudes:**
>
> - **Momentum**: m₁v₁ᵢ + m₂v₂ᵢ = m₁v₁f + m₂v₂f
> - **Energía cinética**: ½m₁v₁ᵢ² + ½m₂v₂ᵢ² = ½m₁v₁f² + ½m₂v₂f²
>
> **Velocidades finales (caso 1D):** $$v_{1f} = \frac{(m_1-m_2)v_{1i} + 2m_2v_{2i}}{m_1+m_2}$$ $$v_{2f} = \frac{(m_2-m_1)v_{2i} + 2m_1v_{1i}}{m_1+m_2}$$

### 🚀 Explosiones y Retroceso

> [!example] 🔍 Principio de Retroceso **Sistema inicialmente en reposo:** $$\vec{P}_{inicial} = 0$$ $$\vec{P}_{final} = \sum m_i\vec{v}_i = 0$$
>
> **Aplicaciones prácticas:**
>
> - 🔫 Disparos de armas de fuego
> - 🚀 Propulsión de cohetes
> - ⚛️ Fisión nuclear
> - 🌟 Desintegración radiactiva

> [!note] 🖼️ Explosiones y Retroceso
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Momentum_Lineal_y_Su_Conservación_05.svg]]
>
> **Se lee así:** El balance de un cohete: el **estado inicial** es cohete + combustible con `P_inicial = 0`; después, la **expulsión de gases** (`m_gas × v_gas`) y el **cohete acelerado** (`m_cohete × v_cohete`) deben cumplir `p_gas + p_cohete = 0`.
>
> **Por qué importa:** Explica por qué un cohete puede acelerar en el vacío: no empuja contra el aire, empuja contra sus propios gases. Como el momentum total arranca en cero, la velocidad del gas expulsado en un sentido obliga al cohete a ir en el opuesto.

---

## 📊 Análisis Gráfico

### 📈 Interpretación de Gráficas

#### 🎯 Momentum vs Velocidad (masa constante)

> [!info] 📊 Relación Lineal **Características del gráfico:**
>
> - **Pendiente** = masa del objeto (m)
> - **Línea recta** que pasa por el origen
> - **Proporcionalidad directa** entre p y v

#### ⏱️ Momentum vs Tiempo

> [!tip] 💡 Interpretación de la Pendiente **Significado físico:** $$\frac{dp}{dt} = F_{neta}$$
>
> **Casos especiales:**
>
> - **Pendiente = 0**: Momentum constante → F_neta = 0
> - **Pendiente > 0**: Fuerza neta en dirección positiva
> - **Pendiente < 0**: Fuerza neta en dirección negativa

---

## 🧪 Ejercicios Resueltos

### 🚂 Problema 1: Colisión Tren-Vagón

> [!example] 🔍 Choque Perfectamente Inelástico **Datos:**
>
> - Tren: m₁ = 10,000 kg, v₁ᵢ = 2.5 m/s
> - Vagón: m₂ = 5,000 kg, v₂ᵢ = 0 m/s (en reposo)
> - Después del choque se acoplan
>
> **Encontrar:** Velocidad final del sistema acoplado

> [!info] 📌 Problema 1: Colisión Tren-Vagón
>
> **Solución:**

> [!success] ✅ Paso a Paso
>
> **1. Aplicar conservación del momentum:** $$m_1v_{1i} + m_2v_{2i} = (m_1 + m_2)v_f$$
>
> **2. Sustituir valores conocidos:** $$10,000 \times 2.5 + 5,000 \times 0 = (10,000 + 5,000)v_f$$ $$25,000 = 15,000 \times v_f$$
>
> **3. Resolver para velocidad final:** $$v_f = \frac{25,000}{15,000} = 1.67 \text{ m/s}$$
>

> [!note] 📝 Análisis Energético **Energía cinética inicial:** $$K_i = \frac{1}{2}(10,000)(2.5)^2 = 31,250 \text{ J}$$
>
> **Energía cinética final:** $$K_f = \frac{1}{2}(15,000)(1.67)^2 = 20,917 \text{ J}$$
>
> **Energía perdida:** $$\Delta K = 31,250 - 20,917 = 10,333 \text{ J}$$
>
> _Esta energía se convierte en calor, sonido y deformación_

### 🧊 Problema 2: Hombre en Hielo

> [!example] 🔍 Sistema con Momentum Inicial Cero **Datos:**
>
> - Hombre: m₁ = 80 kg, inicialmente en reposo
> - Pelota: m₂ = 0.2 kg, lanzada a v₂f = 10 m/s
> - Superficie sin fricción (sistema aislado)
>
> **Encontrar:** Velocidad del hombre tras lanzar la pelota

> [!info] 📌 Problema 2: Hombre en Hielo
>
> **Solución:**

> [!success] ✅ Aplicación del Principio
>
> **1. Momentum inicial del sistema:** $$P_{inicial} = 0 \text{ (ambos en reposo)}$$
>
> **2. Conservación del momentum:** $$P_{inicial} = P_{final}$$ $$0 = m_1v_{1f} + m_2v_{2f}$$
>
> **3. Despejar velocidad del hombre:** $$v_{1f} = -\frac{m_2v_{2f}}{m_1} = -\frac{0.2 \times 10}{80} = -0.025 \text{ m/s}$$
>

> [!tip] 💡 Interpretación Física
>
> - **Signo negativo**: Movimiento en dirección opuesta a la pelota
> - **Magnitud pequeña**: Gran diferencia de masas → pequeña velocidad del objeto pesado
> - **Principio general**: En explosiones, objetos ligeros adquieren mayor velocidad

---

## 🔄 Casos Especiales

### ⚖️ Centro de Masa y Momentum

> [!info] 📖 Relación Fundamental **Momentum del sistema completo:** $$\vec{P}_{total} = M_{total}\vec{v}_{CM}$$
>
> **Donde:**
>
> - M_total = Σmᵢ (masa total del sistema)
> - \vec{v}_CM es la velocidad del centro de masa
>
> **Implicación importante:** Si se conserva el momentum → El centro de masa se mueve con velocidad constante

### 🌌 Momentum en Diferentes Escalas

> [!note] 🖼️ Momentum en Diferentes Escalas
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Momentum_Lineal_y_Su_Conservación_06.svg]]
>
> **Se lee así:** El mapa mental de aplicaciones en tres escalas: la **microscópica** (colisiones moleculares, teoría cinética de los gases, dispersión de partículas, física cuántica), la **cotidiana** (deportes con pelotas, colisiones de vehículos, armas de fuego, maquinaria) y la **astronómica** (órbitas planetarias, choques de asteroides, formación de sistemas, galaxias interactuando).
>
> **Por qué importa:** Muestra que la misma ley `P = constante` gobierna desde el choque de dos moléculas hasta la colisión de galaxias: cambian las masas y las velocidades, no el principio.

---

## 💡 Estrategias y Tips Avanzados

> [!tip] 🎯 Metodología Sistemática
>
> **Pasos de resolución:**
>
> 1. 🔍 **Definir el sistema** y sus límites claramente
> 2. 🌍 **Identificar fuerzas externas** significativas
> 3. ✅ **Verificar condiciones** de conservación
> 4. 📊 **Aplicar conservación** por componentes (x, y, z)
> 5. 🧮 **Resolver sistema** de ecuaciones
> 6. ✅ **Verificar resultados** física y matemáticamente
>

> [!success] ✅ Estrategias Efectivas
>
> - **Diagramas**: Usar esquemas de antes/después para visualizar
> - **Componentes**: Separar en x, y, z para casos multidimensionales
> - **Unidades**: Verificar consistencia en todos los cálculos
> - **Casos límite**: Comprobar con masas muy diferentes o velocidades extremas
> - **Simetría**: Aprovechar simetrías del problema cuando existan
>

> [!warning] ❌ Errores Frecuentes
>
> - Confundir momentum con energía cinética
> - Olvidar el carácter **vectorial** del momentum
> - No verificar si el sistema está **realmente aislado**
> - Mezclar diferentes **marcos de referencia**
> - Ignorar componentes en direcciones perpendiculares

---

## 🔗 Conexiones Conceptuales

> [!note] 🖼️ Conexiones Conceptuales
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Momentum_Lineal_y_Su_Conservación_07.svg]]
>
> **Se lee así:** El mapa de la unidad con su alcance: el **impulso** con el teorema `J = Δp`, las **fuerzas de contacto** y el **análisis temporal** con gráficas F vs t; las **leyes de Newton** (2ª como `F = dp/dt`, 3ª en las fuerzas internas, 1ª como caso especial); las **conservaciones** (energía, momento angular, simetrías de Noether, invariancias); y la **mecánica avanzada** (momentum relativista, Lagrangiana, Hamiltoniana, teoría de campos).
>
> **Por qué importa:** Sitúa el momentum dentro de la física completa: las conservaciones no son trucos aislados, se derivan de simetrías. Esa es la conexión que se estudia en cursos posteriores y la que explica por qué el momentum es tan central.

---

## 🔗 Referencias y Enlaces

> [!quote] 📚 Notas Relacionadas
>
> ### Conceptos Fundamentales
>
> - [[Impulso Lineal]] - Cambio de momentum por fuerzas externas
> - [[Leyes de Newton]] - F = dp/dt como formulación general
> - [[Trabajo y Energía]] - Complemento energético al análisis dinámico
>
> ### Aplicaciones Directas
>
> - [[Choques Uni-Bidimensionales]] - Aplicación práctica principal del principio
> - [[Centro de masa (CM)]] - Movimiento del punto representativo del sistema
> - Dinámica de Sistemas - Análisis de múltiples partículas
>
> ### Conceptos Relacionados
>
> - [[Momentum Angular]] - Análogo rotacional del Momentum lineal
> - [[Principios de Conservación de la Energía]] - Principio complementario
> - Dinámica de Fluidos - Momentum en medios continuos
>
> ### Temas Avanzados
>
> - Mecánica Lagrangiana - Formulación generalizada
> - Relatividad Especial - Momentum a altas velocidades
> - Mecánica Cuántica - Momentum en escala microscópica
> - Teoría de Campos - Momentum en sistemas continuos

---

## 📋 Síntesis Integral

> [!summary] 📊 Conceptos Esenciales
>
> **🎯 Momentum Lineal:**
>
> - **Definición**: \vec{p} = m\vec{v} (inercia en movimiento)
> - **Naturaleza**: Magnitud vectorial fundamental
> - **Significado**: Describe la cantidad de movimiento de un objeto
>
> **⚖️ Principio de Conservación:**
>
> - **Condición**: Σ \vec{F}_ext = 0 (sistema aislado)
> - **Enunciado**: \vec{P}_inicial = \vec{P}_final
> - **Aplicabilidad**: Universal, desde partículas hasta galaxias
>
> **🔗 Relaciones Fundamentales:**
>
> - **Con impulso**: \vec{J} = Δ\vec{p} (teorema impulso-momentum)
> - **Con fuerzas**: \vec{F} = d\vec{p}/dt (Segunda Ley de Newton)
> - **Con energía**: K = p²/(2m) (relación energía-momentum)
>
> **🛠️ Aplicaciones Principales:**
>
> - Análisis de colisiones (elásticas e inelásticas)
> - Sistemas de propulsión y retroceso
> - Explosiones y fragmentaciones
> - Interacciones en física de partículas

---

_Tags: #física #mecánica #momentum #conservación #dinámica #colisiones #sistemas_

**Tags:** #FISG1001 #fisica-mecanica #unidad4 #momentum-lineal-y-su-conservacion
