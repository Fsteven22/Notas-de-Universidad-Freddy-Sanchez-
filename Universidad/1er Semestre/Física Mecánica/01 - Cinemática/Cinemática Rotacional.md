---
dg-publish: true
tags: [FISG1001, unidad1, cinematica, rotacion, angular]
---

# 🌀 Cinemática Rotacional

## 🎯 Introducción

> [!info] 💡 ¿Por Qué Estudiar el Movimiento Rotacional?
>
> Todo lo que gira — ruedas, engranajes, planetas, turbinas — obedece a las mismas leyes que el movimiento lineal, pero con variables angulares. Esta nota traduce posición, velocidad y aceleración a su versión rotacional: θ, ω y α, y muestra cómo se conectan con el movimiento traslacional que ya conoces.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Rotacional_01.svg]]
>
> **Se lee así:** el diagrama muestra las tres variables angulares (θ, ω, α) y cómo se encadenan: la posición angular define la velocidad, y la velocidad define la aceleración, todo respecto a un eje fijo de rotación.
>
> **Por qué importa:** sin este puente no podrías entender máquinas, órbitas ni nada que gire. Es la base de la dinámica rotacional que viene en la próxima unidad.

---

## 📋 Definiciones Formales

### 1️⃣ Posición Angular (θ)

> [!note] 📋 Definición — Posición Angular
>
> La **posición angular** es el ángulo medido desde una línea de referencia hasta la posición del objeto en rotación, respecto a un eje fijo.
>
> - Se mide en radianes (rad), grados (°) o revoluciones (rev)
> - 2π rad = 360° = 1 rev
> - 1 rad ≈ 57.3°
> - **Sentido positivo:** antihorario (regla de la mano derecha)
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Rotacional_01.svg]]
>
> **Se lee así:** el diagrama ubica θ como el ángulo barrido desde la línea de referencia hasta el punto del objeto, medido en el plano perpendicular al eje de rotación.

### 2️⃣ Velocidad Angular (ω)

> [!note] 📋 Definición — Velocidad Angular
>
> La **velocidad angular** es la razón de cambio de la posición angular con respecto al tiempo.
>
> **Velocidad angular promedio:** $\bar{\omega} = \frac{\Delta \theta}{\Delta t} = \frac{\theta_f - \theta_i}{t_f - t_i}$
>
> **Velocidad angular instantánea:** $\omega = \lim_{\Delta t \to 0} \frac{\Delta \theta}{\Delta t} = \frac{d\theta}{dt}$
>
> - Es una cantidad vectorial (dirección perpendicular al plano de rotación)
> - **Unidades:** rad/s, rev/min (rpm)
> - En movimiento uniforme: $\omega = \frac{\theta}{t}$
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Rotacional_01.svg]]
>
> **Se lee así:** el diagrama muestra que ω es la rapidez con la que θ cambia; mayor pendiente en θ-t significa mayor velocidad angular.

### 3️⃣ Aceleración Angular (α)

> [!note] 📋 Definición — Aceleración Angular
>
> La **aceleración angular** es la razón de cambio de la velocidad angular con respecto al tiempo.
>
> **Aceleración angular promedio:** $\bar{\alpha} = \frac{\Delta \omega}{\Delta t} = \frac{\omega_f - \omega_i}{t_f - t_i}$
>
> **Aceleración angular instantánea:** $\alpha = \lim_{\Delta t \to 0} \frac{\Delta \omega}{\Delta t} = \frac{d\omega}{dt} = \frac{d^2\theta}{dt^2}$
>
> - $\alpha > 0$: aceleración angular positiva
> - $\alpha < 0$: desaceleración angular
> - $\alpha = 0$: velocidad angular constante
> - **Unidades:** rad/s²
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Rotacional_01.svg]]
>
> **Se lee así:** el diagrama muestra que α es la rapidez con la que ω cambia; cuando α es constante, se aplican las ecuaciones cinemáticas rotacionales.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Rueda que frena

> [!example] 📋 Planteamiento
>
> Una rueda gira con velocidad angular inicial de 10 rad/s y experimenta una aceleración angular de −2 rad/s² durante 3 segundos. Calcular la velocidad angular final y el ángulo recorrido.
>
> **Datos:** $\omega_0 = 10$ rad/s, $\alpha = -2$ rad/s², $t = 3$ s
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Velocidad angular final: $\omega = \omega_0 + \alpha t = 10 + (-2)(3) = 4$ rad/s
> >
> > **Paso 2:** Ángulo recorrido: $\theta = \omega_0 t + \frac{1}{2}\alpha t^2 = 10(3) + \frac{1}{2}(-2)(3)^2 = 30 - 9 = 21$ rad
> >
> > **Respuesta:** $\omega = 4$ rad/s, $\theta = 21$ rad

### ✏️ Ejercicio 2 — Disco acelerando

> [!example] 📋 Planteamiento
>
> Un disco parte del reposo y alcanza 120 rev/min en 4 segundos con aceleración angular constante. Calcular la aceleración angular y el ángulo total recorrido.
>
> **Datos:** $\omega_0 = 0$, $\omega = 120$ rev/min, $t = 4$ s
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Convertir unidades: 120 rev/min = 2 rev/s = $2 \cdot 2\pi = 4\pi$ rad/s ≈ 12.57 rad/s
> >
> > **Paso 2:** Aceleración angular: $\alpha = \frac{\omega - \omega_0}{t} = \frac{12.57 - 0}{4} \approx 3.14$ rad/s²
> >
> > **Paso 3:** Ángulo recorrido: $\theta = \frac{1}{2}\alpha t^2 = \frac{1}{2}(3.14)(4)^2 = 25.12$ rad
> >
> > **Respuesta:** $\alpha \approx 3.14$ rad/s², $\theta \approx 25.12$ rad

### ✏️ Ejercicio 3 — Relación lineal-angular

> [!example] 📋 Planteamiento
>
> Un punto del borde de una rueda de radio 0.5 m gira a 10 rad/s. Calcular la velocidad lineal del punto y su aceleración centrípeta.
>
> **Datos:** $r = 0.5$ m, $\omega = 10$ rad/s
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Velocidad lineal: $v = r\omega = 0.5 \cdot 10 = 5$ m/s
> >
> > **Paso 2:** Aceleración centrípeta: $a_c = \frac{v^2}{r} = \omega^2 r = 10^2 \cdot 0.5 = 50$ m/s²
> >
> > **Respuesta:** $v = 5$ m/s, $a_c = 50$ m/s²

### ✏️ Ejercicio 4 — Revolución completa

> [!example] 📋 Planteamiento
>
> Un ventilador gira a 1800 rev/min. ¿Cuánto tarda en dar una revolución completa y cuál es su velocidad angular en rad/s?
>
> **Datos:** $\omega = 1800$ rev/min
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Convertir a rad/s: 1800 rev/min = 30 rev/s = $30 \cdot 2\pi = 60\pi$ rad/s ≈ 188.5 rad/s
> >
> > **Paso 2:** Tiempo de una revolución: $T = \frac{1}{f} = \frac{1}{30} \approx 0.033$ s
> >
> > **Respuesta:** $\omega \approx 188.5$ rad/s, $T \approx 0.033$ s

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino posición, velocidad y aceleración angular con mis propias palabras.
> - [ ] Distinguo radianes, grados y revoluciones, y convierto entre ellas.
> - [ ] Identifico MCU y MCUA en un problema de rotación.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico las ecuaciones de cinemática rotacional con α constante.
> - [ ] Convierto entre variables lineales y angulares usando $v = r\omega$ y $a = r\alpha$.
> - [ ] Resuelvo problemas de frenado y aceleración rotacional.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas que combinan movimiento traslacional y rotacional.
> - [ ] Analizo el movimiento de cuerpos rígidos en rotación usando vectores angulares.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - J. Serway, R. Jewett, *Física para Ciencias e Ingeniería*, cap. 10 «Rotación de un cuerpo rígido alrededor de un eje fijo».
> - Apuntes del curso FISG1001 «Física Mecánica», ESPOL.
> - Diagramas de la materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

---

## 🔁 Repaso SR (flashcards)

#flashcards/fisica-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué mide la posición angular θ?::El ángulo desde una línea de referencia hasta el objeto, respecto a un eje fijo.
> - ¿Cuál es la diferencia entre velocidad y rapidez angular?::La velocidad angular es vectorial (tiene dirección); la rapidez angular es escalar.
> - ¿Qué describe una gráfica θ-t con pendiente constante?::Movimiento Circular Uniforme (MCU), velocidad angular constante.
> - ¿Qué es la aceleración angular α?::La razón de cambio de la velocidad angular con el tiempo: $\alpha = \frac{d\omega}{dt}$.
> - ¿Cómo se relacionan v y ω?::Por $v = r\omega$, donde r es el distancia al eje de rotación.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[Cinemática Traslacional]] — base lineal para las analogías angulares.
> - [[Torque y Equilibrio Rotacional]] — causas del movimiento angular (leyes de Newton rotacionales).
> - [[Momento de Inercia]] — extensión hacia dinámica rotacional.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - [[Leyes de Newton]] — fuerzas y causas del movimiento lineal.
> - [[Trabajo y Energía]] — enfoque energético del movimiento.
> - [[Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Rotacional_01.svg]] — diagrama de variables angulares para repasar visualmente.
> - Repaso: vuelve a las definiciones formales antes de los ejercicios.

---

**Tags:** #FISG1001 #unidad1 #cinematica #rotacion #angular
