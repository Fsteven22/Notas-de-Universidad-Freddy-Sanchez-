---
dg-publish: true
tags: [FISG1001, unidad1, cinematica, movimiento-rectilineo, mrua, caida-libre]
---

# 🚗 Cinemática Traslacional

> [!info] 📖 ¿Qué es la Cinemática Traslacional?
>
> La **cinemática traslacional** estudia el movimiento de los cuerpos en línea recta (unidimensional) o en el plano/espacio (bidimensional/tridimensional) sin considerar las causas que lo producen.
>
> **Se lee así:** describe el "cómo" del movimiento —posición, velocidad y aceleración como funciones del tiempo— sin analizar sus causas; eso corresponde a la dinámica.

---

## 🎯 Introducción

> [!info] 📋 Importancia de la Cinemática Traslacional
>
> La cinemática traslacional es la rama de la física que estudia el movimiento de los cuerpos sin considerar las fuerzas que lo originan. Es el punto de partida para entender cualquier fenómeno de movimiento en el universo.
>
> **Se lee así:** sin la cinemática no podríamos describir ni predecir el movimiento de objetos cotidianos como vehículos, planetas o proyectiles.

---

## 📋 Definiciones Formales

### 1️⃣ Posición

> [!note] 📋 Definición — Posición
>
> La **posición** es la ubicación de un objeto en el espacio respecto a un sistema de referencia.
>
> - En 1D: $x(t)$ — coordenada en una línea
> - En 2D/3D: $\vec{r}(t) = x(t)\hat{i} + y(t)\hat{j} + z(t)\hat{k}$
> - **Desplazamiento:** $\Delta x = x_f - x_i$ (cambio de posición)
> - **Distancia:** longitud total recorrida (siempre positiva)
>
> **Unidades:** metros (m), kilómetros (km), centímetros (cm)
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Traslacional_01.svg]]
>
> **Se lee así:** el diagrama ubica un punto P en el espacio mediante su vector posición $\vec{r}$ desde el origen del sistema de referencia.

### 2️⃣ Velocidad

> [!note] 📋 Definición — Velocidad
>
> La **velocidad** es la razón de cambio de la posición con respecto al tiempo.
>
> **Velocidad promedio:** $\bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_f - x_i}{t_f - t_i}$
>
> **Velocidad instantánea:** $v = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}$
>
> **Características:**
>
> - Es una cantidad vectorial (tiene magnitud y dirección)
> - **Rapidez:** magnitud de la velocidad (escalar)
> - **Unidades:** m/s, km/h, cm/s
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Traslacional_02.svg]]
>
> **Se lee así:** el diagrama clasifica el movimiento en MRU (velocidad constante) y MRUA (aceleración constante), con sus respectivas gráficas posición-tiempo y velocidad-tiempo.

### 3️⃣ Aceleración

> [!note] 📋 Definición — Aceleración
>
> La **aceleración** es la razón de cambio de la velocidad con respecto al tiempo.
>
> **Aceleración promedio:** $\bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_f - v_i}{t_f - t_i}$
>
> **Aceleración instantánea:** $a = \lim_{\Delta t \to 0} \frac{\Delta v}{\Delta t} = \frac{dv}{dt} = \frac{d^2x}{dt^2}$
>
> **Interpretación:**
>
> - $a > 0$: aceleración (aumenta velocidad)
> - $a < 0$: desaceleración (disminuye velocidad)
> - $a = 0$: velocidad constante
> - **Unidades:** m/s², km/h², cm/s²
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Traslacional_02.svg]]
>
> **Se lee así:** el diagrama muestra la progresión del movimiento: MRU, MRUA, caída libre y movimiento en plano, con sus características distintivas.

---

## 📝 Ejercicios Propuestos

> [!example] 🍎 Ejercicio 1: Caída Libre
>
> **Problema:** Un objeto cae libremente desde el reposo desde una altura de 45 m. Calcular el tiempo de caída y la velocidad al llegar al suelo.
>
> **Datos:** $h = 45$ m, $v_0 = 0$, $g = 9.8$ m/s²
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Elegir sistema de coordenadas (eje y hacia arriba, origen en el suelo).
> >
> > **Paso 2:** Aplicar ecuación de posición: $y = y_0 + v_0t - \frac{1}{2}gt^2$
> >
> > **Paso 3:** Sustituir: $0 = 45 + 0 \cdot t - \frac{1}{2}(9.8)t^2$
> >
> > **Paso 4:** Despejar $t$: $4.9t^2 = 45 \Rightarrow t = \sqrt{45/4.9} \approx 3.03$ s
> >
> > **Paso 5:** Calcular velocidad final: $v = v_0 - gt = 0 - 9.8(3.03) \approx -29.7$ m/s
> >
> > **Respuesta:** $t \approx 3.03$ s, $v \approx -29.7$ m/s (hacia abajo)

> [!example] 🚗 Ejercicio 2: Frenado de Vehículo
>
> **Problema:** Un auto viaja a 72 km/h y frena con desaceleración constante hasta detenerse en 50 m. Calcular la aceleración y el tiempo de frenado.
>
> **Datos:** $v_0 = 72$ km/h, $v = 0$, $x = 50$ m
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Convertir unidades: $72$ km/h $= 20$ m/s
> >
> > **Paso 2:** Identificar variables: $v_0 = 20$ m/s, $v = 0$, $x = 50$ m
> >
> > **Paso 3:** Elegir ecuación: $v^2 = v_0^2 + 2ax$
> >
> > **Paso 4:** Resolver para la aceleración: $0^2 = 20^2 + 2a(50) \Rightarrow 100a = -400 \Rightarrow a = -4$ m/s²
> >
> > **Paso 5:** Calcular el tiempo: $t = (v - v_0)/a = (0 - 20)/(-4) = 5$ s
> >
> > **Respuesta:** $a = -4$ m/s², $t = 5$ s

> [!example] ⚽ Ejercicio 3: Lanzamiento Vertical
>
> **Problema:** Se lanza un balón verticalmente hacia arriba con velocidad inicial de 15 m/s. Calcular la altura máxima que alcanza y el tiempo total de vuelo.
>
> **Datos:** $v_0 = 15$ m/s, $g = 9.8$ m/s²
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** En la altura máxima, la velocidad es cero: $v = 0$
> >
> > **Paso 2:** Aplicar ecuación: $v^2 = v_0^2 - 2gh_{max}$
> >
> > **Paso 3:** Despejar la altura máxima: $0 = 15^2 - 2(9.8)h_{max} \Rightarrow 19.6h_{max} = 225 \Rightarrow h_{max} \approx 11.5$ m
> >
> > **Paso 4:** Tiempo de subida: $t = v_0/g = 15/9.8 \approx 1.53$ s
> >
> > **Paso 5:** Tiempo total de vuelo: $t_{total} = 2t = 2(1.53) \approx 3.06$ s
> >
> > **Respuesta:** $h_{max} \approx 11.5$ m, $t_{total} \approx 3.06$ s

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Explico qué es la cinemática traslacional con mis propias palabras.
> - [ ] Distinguo posición, velocidad y aceleración.
> - [ ] Identifico MRU y MRUA en un problema.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico las ecuaciones de MRUA para resolver problemas de movimiento.
> - [ ] Interpreto gráficas posición-tiempo y velocidad-tiempo.
> - [ ] Resuelvo problemas de caída libre y frenado.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas que combinan varios tipos de movimiento.
> - [ ] Analizo el movimiento en 2D y 3D usando vectores posición.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - J. Serway, R. Jewett, *Física para Ciencias e Ingeniería*, cap. 2 «Movimiento en una dimensión».
> - Apuntes del curso FISG1001 «Física Mecánica», ESPOL.
> - Guías y ejercicios de la materia (`Unidad 0 - Guias y Ejercicios/`).

---

## 🔁 Repaso SR

#flashcards/fisica-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué estudia la cinemática traslacional?::El movimiento de los cuerpos sin considerar sus causas (posición, velocidad, aceleración como funciones del tiempo).
> - ¿Cuál es la diferencia entre velocidad y rapidez?::La velocidad es vectorial (tiene dirección); la rapidez es escalar (solo magnitud).
> - ¿Qué describe una gráfica x-t con pendiente constante?::Movimiento Rectilíneo Uniforme (MRU), velocidad constante.
> - ¿Qué es el desplazamiento?::El cambio de posición $\Delta x = x_f - x_i$, puede ser negativo.
> - ¿Cuál es la aceleración en caída libre?::$g = 9.8$ m/s² hacia abajo (constante).

---

## 🔗 Conexiones

> [!quote] 🌟 Continuando el Aprendizaje
>
> - **Cinemática Rotacional:** movimiento angular, analogías con el movimiento lineal.
> - **Dinámica:** causas del movimiento (leyes de Newton).
> - **Vectores:** movimiento en 2D y 3D.
> - **Trabajo y Energía:** enfoque energético del movimiento.

---

## 🔗 Seguir estudiando

> [!info] 📚 Próximos pasos y material complementario
>
> - [[Cinemática Rotacional]] — movimiento angular y sus analogías con el lineal.
> - [[Vectores]] — conceptos de función del tiempo en 2D y 3D.
> - [[Leyes de Newton]] — causas del movimiento (dinámica).
> - [[Guías y Ejercicios (Prof. Zambrano)]] — guías de taller y ejercicios resueltos de la Unidad 0.
> - Repaso: vuelve a las definiciones formales antes de los ejercicios.

**Tags:** #FISG1001 #unidad1 #cinematica #movimiento-rectilineo #mrua #caida-libre
