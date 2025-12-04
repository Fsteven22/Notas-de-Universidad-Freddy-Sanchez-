# Problemas de Persecución

>[!quote] _"En la persecución, no importa qué tan lento vayas, siempre que no te detengas y seas más rápido que tu objetivo"_ - Física del alcance

---

## 📋 Definición y Características

> [!info]- 🎯 **¿Qué son los Problemas de Persecución?** Son situaciones cinemáticas donde un **móvil perseguidor** busca **alcanzar** a otro **móvil objetivo** que tiene una **ventaja inicial** en posición, tiempo, o ambos. El perseguidor debe tener mayor velocidad para lograr el alcance.
> 
> **🔑 Condiciones fundamentales:**
> 
> - **Ventaja inicial:** El objetivo tiene head start
> - **Velocidad superior:** $v_{perseguidor} > v_{objetivo}$
> - **Momento de alcance:** $x_{perseguidor}(t) = x_{objetivo}(t)$

---

## 🏃‍♂️ Tipos de Problemas de Persecución

> [!tip]- 🚗 **Persecución Clásica (Velocidades Constantes)** **Situación:** Ambos móviles mantienen velocidades constantes durante toda la persecución
> 
> ```mermaid
> graph LR
>     A[Objetivo con<br/>ventaja inicial] -->|v₂| C[Punto de<br/>Alcance]
>     B[Perseguidor<br/>desde origen] -->|v₁ > v₂| C
>     style C fill:#ff9999
> ```
> 
> **Ejemplos típicos:**
> 
> - 👮‍♂️ Policía persiguiendo criminal
> - 🐆 Depredador cazando presa
> - 🚗 Auto rápido alcanzando auto lento
> - 🏃‍♂️ Corredor alcanzando a otro en pista

> [!warning]- 🚀 **Persecución con Aceleración** **Situación:** El perseguidor acelera desde reposo o velocidad inicial menor
> 
> ```mermaid
> graph TB
>     subgraph "Fases de la Persecución"
>         A[Fase 1:<br/>Objetivo se aleja] --> B[Fase 2:<br/>Perseguidor iguala velocidad]
>         B --> C[Fase 3:<br/>Perseguidor alcanza]
>     end
>     style C fill:#90EE90
> ```
> 
> **Ejemplos típicos:**
> 
> - 🏎️ Auto deportivo alcanzando desde semáforo
> - ✈️ Caza interceptando bombardero
> - 🚂 Tren expreso alcanzando tren local
> - 🚴‍♂️ Ciclista acelerando para alcanzar pelotón

> [!note]- ⏰ **Persecución con Retardo Temporal** **Situación:** El perseguidor sale después que el objetivo
> 
> **Casos típicos:**
> 
> - 🚔 Policía saliendo en persecución tras recibir alerta
> - 🏃‍♂️ Atleta saliendo tarde en una carrera
> - 🚁 Helicóptero de rescate siguiendo embarcación
> 
> **Característica:** Combina ventaja espacial y temporal

> [!abstract]- 🎯 **Persecución Interceptiva** **Situación:** El perseguidor toma una ruta directa hacia donde estará el objetivo
> 
> **Aplicaciones:**
> 
> - 🚀 Misiles interceptores
> - ⚽ Portero anticipando trayectoria del balón
> - 🐕 Perro corriendo hacia donde llegará la pelota

> [!note]- 🚌 **Problemas de Alcance (Caso Especial)** **Situación:** Similar a persecución, pero el móvil más rápido **sale después** que el más lento desde el **mismo punto**
> 
> ```mermaid
> graph LR
>     A[t=0: Móvil lento sale] -->|v₁| B[t=τ: Móvil rápido sale]
>     B -->|v₂ > v₁| C[t=T: Alcance]
>     style C fill:#FFD700
> ```
> 
> **Diferencia clave con persecución:**
> 
> - **Persecución:** Ventaja **espacial** inicial
> - **Alcance:** Ventaja **temporal** inicial
> 
> **Ejemplos típicos:**
> 
> - 🚌 Bus sale de estación, auto lo alcanza después
> - 🚂 Tren local seguido por tren expreso
> - 🚴‍♂️ Ciclista alcanzado por motociclista
> 
> **Fórmula específica para alcance:** $T = \frac{v_2 \cdot \tau}{v_2 - v_1}$
> 
> donde $\tau$ = retardo temporal del móvil rápido

---

## 📐 Metodología de Resolución

> [!example]- 🛠️ **Pasos para Resolver Problemas de Persecución**
> 
> ### Paso 1: Analizar las Condiciones Iniciales
> 
> - **Posición inicial** de cada móvil: $x_{01}$, $x_{02}$
> - **Velocidad inicial** de cada móvil: $v_{01}$, $v_{02}$
> - **Aceleración** (si la hay): $a_1$, $a_2$
> - **Retardo temporal** (si existe): $\Delta t$
> 
> ### Paso 2: Establecer las Ecuaciones de Movimiento
> 
> **Para el objetivo:** $$x_2(t) = x_{02} + v_{02}t + \frac{1}{2}a_2 t^2$$
> 
> **Para el perseguidor:** $$x_1(t) = x_{01} + v_{01}t + \frac{1}{2}a_1 t^2$$
> 
> ### Paso 3: Aplicar la Condición de Alcance
> 
> $$x_1(t_{alcance}) = x_2(t_{alcance})$$
> 
> ### Paso 4: Resolver para el Tiempo de Alcance
> 
> - Si es lineal: despejar directamente
> - Si es cuadrática: usar fórmula cuadrática
> - Verificar que $t > 0$ y sea físicamente posible
> 
> ### Paso 5: Calcular Distancias y Verificaciones
> 
> - Posición donde ocurre el alcance
> - Distancia total recorrida por cada móvil
> - Verificar que $v_{perseguidor} > v_{objetivo}$ en el momento crítico

---

## 🧮 Casos Específicos y Fórmulas

> [!abstract]- 📊 **Tabla de Fórmulas para Casos Comunes**
> 
> |Tipo de Persecución|Condiciones|Tiempo de Alcance|Posición de Alcance|
> |---|---|---|---|
> |**Clásica Simple**|$v_1 > v_2$ constantes<br/>$x_1(0) = 0, x_2(0) = d$|$t = \frac{d}{v_1 - v_2}$|$x = \frac{v_1 \cdot d}{v_1 - v_2}$|
> |**Con Retardo**|Perseguidor sale $\tau$ después|$t = \frac{d + v_2\tau}{v_1 - v_2}$|$x = v_1 \left(\frac{d + v_2\tau}{v_1 - v_2}\right)$|
> |**Aceleración Uniforme**|$v_1(0) < v_2, a_1 > 0, a_2 = 0$|Ecuación cuadrática|Sustituir $t$ en ecuaciones|
> |**Ambos Aceleran**|$a_1 > a_2$|$\frac{1}{2}(a_1-a_2)t^2 + (v_1-v_2)t - d = 0$|Compleja|

---

## 💡 Análisis de Viabilidad

> [!warning]- 🚫 **¿Cuándo NO es Posible la Persecución?**
> 
> ### Condición de Imposibilidad
> 
> Si $v_{perseguidor} \leq v_{objetivo}$ de manera permanente, la persecución **nunca** se completará.
> 
> ### Casos Críticos
> 
> 1. **Velocidades iguales:** La distancia permanece constante
> 2. **Objetivo más rápido:** La distancia aumenta indefinidamente
> 3. **Aceleración insuficiente:** El perseguidor nunca supera al objetivo
> 
> ### Análisis Matemático
> 
> Para persecución con aceleración, verificar que el discriminante sea positivo: $$\Delta = b^2 - 4ac \geq 0$$
> 
> donde $at^2 + bt + c = 0$ es la ecuación de alcance.

---

## 💡 Ejemplos Resueltos

> [!example]- 🚔 **Ejemplo 1: Persecución Policial Clásica** **Problema:** Un ladrón escapa en auto a 60 km/h. Después de 10 minutos, la policía sale en persecución a 90 km/h. ¿Cuánto tiempo perseguirá la policía al ladrón y a qué distancia del punto de partida ocurrirá el alcance?
> 
> **Solución:**
> 
> **Datos:**
> 
> - Velocidad del ladrón: $v_2 = 60$ km/h
> - Velocidad de la policía: $v_1 = 90$ km/h
> - Retardo policial: $\tau = 10$ min $= \frac{1}{6}$ h
> 
> **Ventaja inicial del ladrón:** $$d = v_2 \cdot \tau = 60 \times \frac{1}{6} = 10 \text{ km}$$
> 
> **Ecuaciones de posición (desde que sale la policía):**
> 
> - Ladrón: $x_2(t) = 10 + 60t$
> - Policía: $x_1(t) = 90t$
> 
> **Condición de alcance:** $$90t = 10 + 60t$$ $$30t = 10$$ $$t = \frac{1}{3} \text{ h} = 20 \text{ minutos}$$
> 
> **Posición de alcance:** $$x = 90 \times \frac{1}{3} = 30 \text{ km}$$
> 
> **Verificación:**
> 
> - Ladrón: $x_2 = 10 + 60 \times \frac{1}{3} = 10 + 20 = 30$ km ✓
> 
> **Respuesta:** La policía perseguirá durante 20 minutos y alcanzará al ladrón a 30 km del punto de partida policial.

> [!example]- 🏎️ **Ejemplo 2: Persecución con Aceleración** **Problema:** Un auto deportivo (inicialmente en reposo) persigue a un auto que pasa por su lado a 20 m/s constante. El deportivo acelera a 4 m/s². ¿Cuándo y dónde alcanzará al auto en movimiento?
> 
> **Solución:**
> 
> **Datos:**
> 
> - Auto objetivo: $v_2 = 20$ m/s, $a_2 = 0$, $x_2(0) = 0$
> - Auto deportivo: $v_1(0) = 0$, $a_1 = 4$ m/s², $x_1(0) = 0$
> 
> **Ecuaciones de posición:**
> 
> - Auto objetivo: $x_2(t) = 20t$
> - Auto deportivo: $x_1(t) = \frac{1}{2}(4)t^2 = 2t^2$
> 
> **Condición de alcance:** $$2t^2 = 20t$$ $$2t^2 - 20t = 0$$ $$2t(t - 10) = 0$$
> 
> **Soluciones:**
> 
> - $t = 0$ (encuentro inicial, no es la persecución)
> - $t = 10$ s (momento del alcance)
> 
> **Posición de alcance:** $$x = 20 \times 10 = 200 \text{ m}$$
> 
> **Verificación deportivo:** $$x_1 = 2 \times 10^2 = 200 \text{ m}$$ ✓
> 
> **Velocidad del deportivo en el alcance:** $$v_1 = a_1 t = 4 \times 10 = 40 \text{ m/s}$$
> 
> **Respuesta:** El auto deportivo alcanzará al objetivo a los 10 segundos, a 200 m del punto de partida. En ese momento, el deportivo viajará a 40 m/s.

> [!example]- 🚌 **Ejemplo 3: Problema de Alcance** **Problema:** Un bus sale de la estación a 60 km/h. 10 minutos después sale un auto a 90 km/h desde la misma estación. ¿Cuándo alcanzará el auto al bus y a qué distancia de la estación?
> 
> **Solución:**
> 
> **Datos:**
> 
> - Bus: $v_1 = 60$ km/h, sale en $t = 0$
> - Auto: $v_2 = 90$ km/h, sale en $t = \tau = \frac{10}{60} = \frac{1}{6}$ h
> 
> **Ecuaciones de posición:**
> 
> - Bus: $x_1(t) = 60t$
> - Auto: $x_2(t) = 90(t - \frac{1}{6})$ para $t \geq \frac{1}{6}$
> 
> **Tiempo de alcance:** $T = \frac{v_2 \cdot \tau}{v_2 - v_1} = \frac{90 \times \frac{1}{6}}{90 - 60} = \frac{15}{30} = 0.5 \text{ h} = 30 \text{ min}$
> 
> **Posición de alcance:** $x = v_1 \cdot T = 60 \times 0.5 = 30 \text{ km}$
> 
> **Verificación con el auto:** $x_2 = 90 \times (0.5 - \frac{1}{6}) = 90 \times \frac{1}{3} = 30 \text{ km}$ ✓
> 
> **Respuesta:** El auto alcanzará al bus a los 30 minutos (desde que salió el bus) y a 30 km de la estación.

---

## 📊 Análisis Gráfico

> [!note]- 📈 **Gráficos Posición vs Tiempo**
> 
> ```mermaid
> graph TB
>     subgraph "Persecución Clásica"
>         A[t=0: Objetivo tiene ventaja] --> B[Las pendientes indican velocidades]
>         B --> C[Intersección = Alcance]
>     end
>     
>     subgraph "Persecución con Aceleración"
>         D[Línea recta: Movimiento uniforme] --> E[Parábola: Movimiento acelerado]
>         E --> F[Intersección: Momento de alcance]
>     end
>     
>     subgraph "Interpretación"
>         G[Pendiente = Velocidad instantánea]
>         H[Curvatura = Aceleración]
>         I[Intersección = Misma posición]
>     end
> ```
> 
> **🎯 Puntos clave en el gráfico:**
> 
> - **Pendiente mayor** = velocidad mayor
> - **Línea recta** = velocidad constante
> - **Parábola** = aceleración constante
> - **Punto de intersección** = momento y lugar del alcance

---

## 🧠 Técnica Mnemotécnica: "PERSIGO"

> [!tip]- 🎯 **Método PERSIGO para Problemas de Persecución**
> 
> **P** - **P**osiciones iniciales (ventaja del objetivo) **E** - **E**cuaciones de movimiento para ambos móviles **R** - **R**equisito fundamental: $v_{perseguidor} > v_{objetivo}$ **S** - **S**ustituir en condición de alcance: $x_1(t) = x_2(t)$ **I** - **I**gualar y resolver para tiempo **G** - **G**ráficar para visualizar (opcional pero útil) **O** - **O**btener posición final y verificar
> 
> **🔄 Regla nemotécnica:** _"Perseguir Exige Rapidez, Siempre Ir Ganando Oportunamente"_

---

## 🎪 Variantes y Casos Especiales

> [!abstract]- 🔄 **Persecución Circular** **Situación:** Móviles en pista circular, el perseguidor debe dar una vuelta completa de ventaja
> 
> **Consideraciones especiales:**
> 
> - Distancia a recorrer = ventaja inicial + circunferencia
> - Velocidad relativa constante en pista cerrada
> - Múltiples alcances posibles (cada vuelta)

> [!note]- 🎯 **Persecución Interceptiva** **Situación:** El perseguidor se dirige hacia donde estará el objetivo, no donde está
> 
> **Método:**
> 
> 1. Predecir posición futura del objetivo
> 2. Calcular tiempo de encuentro basado en distancias
> 3. Resolver sistema de ecuaciones simultáneas
> 
> **Ejemplo:** Portero atajando penal, misil interceptor

> [!warning]- ⚡ **Persecución con Cambio de Velocidad** **Situación:** Las velocidades cambian durante la persecución
> 
> **Análisis por tramos:**
> 
> - Dividir en fases con velocidades constantes
> - Aplicar continuidad en posición y tiempo
> - Sumar efectos acumulativos

---

## ⚠️ Errores Comunes y Consejos

> [!warning]- 🚫 **Errores Frecuentes**
> 
> ### ❌ Error 1: No Considerar la Ventaja Inicial
> 
> **Problema:** Asumir que ambos móviles parten del mismo punto **Solución:** Siempre identificar y cuantificar la ventaja inicial
> 
> ### ❌ Error 2: Confundir Tiempo Total con Tiempo de Persecución
> 
> **Problema:** No distinguir entre tiempo desde que sale el objetivo vs desde que sale el perseguidor **Solución:** Definir claramente el $t = 0$ de referencia
> 
> ### ❌ Error 3: No Verificar Viabilidad
> 
> **Problema:** No comprobar si la persecución es físicamente posible **Solución:** Verificar que $v_{perseguidor} > v_{objetivo}$ eventualmente
> 
> ### ❌ Error 4: Malinterpretar el Momento de "Velocidades Iguales"
> 
> **Problema:** Confundir el momento de igual velocidad con el de alcance **Solución:** El alcance ocurre cuando las **posiciones** son iguales, no las velocidades

---

## 🔬 Aplicaciones en el Mundo Real

> [!abstract]- 🌍 **Aplicaciones Prácticas**
> 
> ### 🛡️ Militar y Defensa
> 
> - **Interceptores:** Misiles anti-misil
> - **Persecución aérea:** Cazas interceptando bombarderos
> - **Naval:** Destructores persiguiendo submarinos
> 
> ### 🏃‍♂️ Deportes
> 
> - **Atletismo:** Corredores alcanzando en pista
> - **Ciclismo:** Pelotón persiguiendo escapados
> - **Automovilismo:** Adelantamientos en circuitos
> 
> ### 👮‍♂️ Seguridad Pública
> 
> - **Persecuciones policiales:** Cálculo de tiempos de alcance
> - **Rescates:** Equipos de emergencia
> - **Vigilancia:** Seguimiento de objetivos

---

## 🔗 Referencias

> [!quote]- 📚 **Notas Relacionadas**
> 
> - [[Problemas de Encuentro]] - Casos donde no hay ventaja inicial
> - [[Cinemática Traslacional]] - Ecuaciones fundamentales
> - [[Cinemática Traslacional#📈 Tipos de Movimiento Traslacional]] - Para casos con aceleración
> - [[Análisis Gráfico del Movimiento]] - Representación visual

---
#persecución #alcance #cinemática #movimiento-relativo #velocidad-superior #interceptación #análisis-temporal
