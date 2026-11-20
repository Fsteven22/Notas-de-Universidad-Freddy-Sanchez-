---
dg-publish: true
tags: [FISG1001, unidad1, fisica-mecanica, cinematica, problemas-de-encuentro]
---

# 🧮 Problemas de Encuentro 

> [!quote] _"El momento del encuentro es cuando dos historias en movimiento se vuelven una sola"_ - Física en acción

---

## 📋 Definición y Características

> [!info] 🎯 **¿Qué son los Problemas de Encuentro?** Son situaciones cinemáticas donde **dos o más móviles** que parten desde posiciones diferentes y con velocidades distintas llegan a **coincidir en el mismo punto** del espacio en el **mismo instante** de tiempo.
>
> **🔑 Condición fundamental:** $$x_1(t) = x_2(t) \quad \text{en el momento del encuentro}$$

---

## 🚗 Tipos de Problemas de Encuentro

> [!tip] 📍 **Encuentro Frontal (Convergencia)** **Situación:** Dos móviles parten desde puntos diferentes y **se dirigen uno hacia el otro**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Problemas_de_Encuentro_01.svg]]
>
> **Se lee así:** El esquema plantea el encuentro frontal: el móvil 1 parte del origen con x₁ = x₀₁ + v₁t y el móvil 2 viene de frente con x₂ = d₀ − v₂t. Al imponer x₁ = x₂ sale t = d₀/(v₁ + v₂), y la posición del cruce se obtiene sustituyendo ese tiempo.
>
> **Por qué importa:** Enseña el concepto de **velocidad relativa de cierre**: cuando dos cuerpos se acercan, la distancia se reduce a la suma de sus rapideces. Por eso el tiempo de encuentro es menor cuanto más rápidos son ambos.
>
> **Ejemplos típicos:**
>
> - 🚗 Dos autos que viajan en sentidos opuestos
> - 🚂 Trenes que parten de estaciones diferentes
> - 👥 Dos personas caminando una hacia la otra
>

> [!warning] 🏃‍♂️ **Persecución y Alcance** **Situación:** Un móvil **persigue** a otro que tiene ventaja inicial
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Problemas_de_Encuentro_02.svg]]
>
> **Se lee así:** Esta lámina cubre el caso opuesto, el alcance en el mismo sentido: el objetivo lleva ventaja d₀ y el perseguidor debe ser más rápido (v_per > v_obj) para que la distancia relativa de cierre (v_per − v_obj) acabe a cero. Si no se cumple esa desigualdad, el alcance nunca ocurre.
>
> **Por qué importa:** Marca la condición de existencia de la solución: antes de calcular el tiempo, comprueba que el perseguidor es más rápido. Un tiempo negativo es la señal de que el problema no tiene solución física.
>
> **Ejemplos típicos:**
>
> - 👮‍♂️ Policía persiguiendo a un ladrón
> - 🐆 Depredador cazando presa
> - 🚗 Auto rápido alcanzando auto lento
>

> [!note] 🔄 **Encuentro Cíclico** **Situación:** Móviles en trayectorias circulares o que se encuentran periódicamente
>
> **Ejemplos típicos:**
>
> - 🏃‍♂️ Corredores en pista circular
> - 🌍 Órbitas planetarias
> - ⏰ Manecillas del reloj

---

## 📐 Metodología de Resolución

> [!example] 🛠️ **Pasos para Resolver Problemas de Encuentro**
>
> ### Paso 1: Análisis de la Situación
>
> - **Identificar** los móviles involucrados
> - **Determinar** posiciones iniciales ($x_0$)
> - **Establecer** velocidades y aceleraciones
> - **Definir** el sistema de coordenadas
>
> ### Paso 2: Plantear las Ecuaciones de Posición
>
> Para cada móvil: $$x_i(t) = x_{0i} + v_{0i}t + \frac{1}{2}a_i t^2$$
>
> ### Paso 3: Aplicar la Condición de Encuentro
>
> $$x_1(t_{encuentro}) = x_2(t_{encuentro})$$
>
> ### Paso 4: Resolver para el Tiempo de Encuentro
>
> Despejar $t_{encuentro}$ de la ecuación resultante
>
> ### Paso 5: Calcular la Posición de Encuentro
>
> Sustituir $t_{encuentro}$ en cualquiera de las ecuaciones de posición

---

## 🧮 Casos Específicos y Fórmulas

> [!abstract] 📊 **Tabla de Casos Comunes**
>
> |Caso|Condiciones Iniciales|Fórmula del Tiempo|Posición de Encuentro|
> |---|---|---|---|
> |**Encuentro Frontal**|$x_A = 0, x_B = d$ <br> $v_A, v_B$ constantes|$t = \frac{d}{v_A + v_B}$|$x = \frac{v_A \cdot d}{v_A + v_B}$|
> |**Persecución Inicial**|$x_A = 0, x_B = d$ <br> $v_A > v_B$|$t = \frac{d}{v_A - v_B}$|$x = \frac{v_A \cdot d}{v_A - v_B}$|
> |**Persecución con Aceleración**|$x_A = 0, x_B = d$ <br> $v_{A0} < v_B, a_A > 0$|Ecuación cuadrática|Sustituir $t$ obtenido|

---

## 💡 Ejemplos Resueltos

> [!example] 🚗 **Ejemplo 1: Encuentro Frontal Clásico** **Problema:** Dos autos parten simultáneamente desde ciudades separadas 300 km. El auto A viaja a 80 km/h hacia el este, el auto B viaja a 70 km/h hacia el oeste. ¿Cuándo y dónde se encuentran?
>
> **Solución:**
>
> **Datos:**
>
> - $d = 300 \text{ km}$
> - $v_A = 80 \text{ km/h}$
> - $v_B = 70 \text{ km/h}$
>
> **Sistema de coordenadas:** Origen en la posición inicial de A
>
> - $x_A(0) = 0$, $x_B(0) = 300 \text{ km}$
>
> **Ecuaciones de posición:**
>
> - $x_A(t) = 80t$
> - $x_B(t) = 300 - 70t$
>
> **Condición de encuentro:** $$80t = 300 - 70t$$ $$150t = 300$$ $$t = 2 \text{ horas}$$
>
> **Posición de encuentro:** $$x = 80 \times 2 = 160 \text{ km}$$ (desde la ciudad A)
>
> **Respuesta:** Se encuentran a las 2 horas, a 160 km de la ciudad A.
>

> [!example] 👮‍♂️ **Ejemplo 2: Persecución con Ventaja Inicial** **Problema:** Un ladrón huye en auto a 60 km/h. Después de 15 minutos, la policía sale en persecución a 90 km/h. ¿Cuánto tiempo perseguirá la policía al ladrón?
>
> **Solución:**
>
> **Análisis:** La policía debe cubrir la ventaja inicial más la distancia que recorre el ladrón
>
> **Ventaja inicial del ladrón:** $$d_0 = 60 \times \frac{15}{60} = 15 \text{ km}$$
>
> **Ecuaciones (desde que sale la policía):**
>
> - Ladrón: $x_L(t) = 15 + 60t$
> - Policía: $x_P(t) = 90t$
>
> **Condición de alcance:** $$90t = 15 + 60t$$ $$30t = 15$$ $$t = 0.5 \text{ horas} = 30 \text{ minutos}$$
>
> **Respuesta:** La policía perseguirá al ladrón durante 30 minutos.

---

## 🎨 Representación Gráfica

> [!note] 📈 **Gráficos Posición vs Tiempo**
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Problemas_de_Encuentro_03.svg]]
>
> **Se lee así:** La gráfica x-t del encuentro muestra dos rectas cuya pendiente es la velocidad de cada móvil; el punto donde se cruzan es exactamente el instante y el lugar del encuentro. La pendiente más inclinada identifica al más rápido, y el área bajo la curva v-t da el desplazamiento de cada uno.
>
> **Por qué importa:** Traduce el álgebra a imagen: buscar el encuentro es buscar la intersección de dos rectas. Ese hábito permite detectar de un vistazo si hay solución, si es única o si los móviles nunca se cruzan.
>
> **🎯 Interpretación visual:**
>
> - **Pendiente** = velocidad del móvil
> - **Intersección** = momento y lugar del encuentro
> - **Área bajo la curva** = desplazamiento

---

## 🧠 Técnica Mnemotécnica: "PLACE"

> [!tip] 🎯 **Método PLACE para Problemas de Encuentro**
>
> **P** - **P**osiciones iniciales (definir $x_0$ para cada móvil) **L** - **L**eyes de movimiento (ecuaciones cinemáticas) **A** - **A**plicar condición de encuentro ($x_1 = x_2$) **C** - **C**alcular tiempo de encuentro **E** - **E**ncontrar posición final
>
> **🔄 Repaso con flashcards:**
>
> - Cara: Tipo de problema
> - Reverso: Fórmula clave y metodología

---

## ⚠️ Errores Comunes y Consejos

> [!warning] 🚫 **Errores Frecuentes**
>
> ### ❌ Error 1: Sistema de Coordenadas Confuso
>
> **Problema:** No definir claramente el origen y direcciones positivas **Solución:** Siempre dibujar el sistema y mantener consistencia
>
> ### ❌ Error 2: Signos Incorrectos en Velocidades
>
> **Problema:** No considerar direcciones opuestas con signos diferentes **Solución:** Velocidades en direcciones opuestas tienen signos contrarios
>
> ### ❌ Error 3: Confundir Tiempo Total con Tiempo de Persecución
>
> **Problema:** En persecución, no distinguir el tiempo que lleva ventaja **Solución:** Definir claramente el $t = 0$ para cada móvil

---

## 🔗 Referencias

> [!quote] 📚 **Notas Relacionadas**
>
> - [[Cinemática Traslacional]] - Conceptos base
> - [[Velocidad Relativa para Barcos y Aviones]] - Marcos de referencia
> - [[Cinemática Traslacional#📈 Tipos de Movimiento Traslacional]] - Con aceleración

---

## 📝 Notas Recomendadas como Prerrequisitos

> [!info] 🎓 **Conocimientos Previos Necesarios**
>
> - [[Vectores]] - Para sistemas de coordenadas
> - [[01 - Sistema de ecuaciones lineales en R2 y R3]] - Álgebra necesaria
> - Análisis Gráfico del Movimiento - Representación visual

---

#encuentros #cinemática #persecución #convergencia #movimiento-rectilíneo #problemas-tipo

**Tags:** #FISG1001 #fisica-mecanica #unidad1 #problemas-de-encuentro
