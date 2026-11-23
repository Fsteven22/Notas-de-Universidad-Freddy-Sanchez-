---
dg-publish: true
tags: [FISG1001, unidad1, cinematica, movimiento-rectilineo, mrua, caida-libre]
---

# 🚗 Cinemática Traslacional

> [!quote] 💡 "El movimiento es relativo, pero las leyes que lo gobiernan son absolutas."
>
> La cinemática traslacional estudia el movimiento de los cuerpos sin considerar las causas que lo producen. Describe la "cómo" del movimiento: posición, velocidad y aceleración como funciones del tiempo.

---

## 🎯 Introducción

> [!info] 📖 ¿Qué es la Cinemática Traslacional?
>
> La **cinemática traslacional** estudia el movimiento de los cuerpos en línea recta (unidimensional) o en el plano/espacio (bidimensional/tridimensional) sin considerar las causas que producen dicho movimiento.
>
> > **Se lee así:** la cinemática describe el movimiento (posición, velocidad, aceleración) como función del tiempo, sin analizar sus causas; eso corresponde a la dinámica.
>
> **Características principales:**
>
> - Se enfoca en describir el movimiento, no en explicar sus causas
> - Variables principales: posición, velocidad y aceleración
> - El tiempo es el parámetro independiente
> - Los objetos se consideran partículas puntuales

> [!note] 📋 Figura — Introducción
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Traslacional_01.svg]]
>
> **Se lee así:** el diagrama muestra la clasificación del movimiento traslacional: MRU (velocidad constante) y MRUA (aceleración constante), con sus respectivas gráficas posición-tiempo y velocidad-tiempo.

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
> > [!note] 📋 Figura — Posición
> > >
> > > ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Traslacional_01.svg]]
> > >
> > > **Se lee así:** el diagrama ubica un punto P en el espacio mediante su vector posición $\vec{r}$ desde el origen del sistema de referencia.

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
> > [!note] 📋 Figura — Velocidad
> > >
> > > ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Traslacional_02.svg]]
> > >
> > > **Se lee así:** el diagrama clasifica el movimiento en MRU (velocidad constante) y MRUA (aceleración constante), con sus respectivas gráficas posición-tiempo y velocidad-tiempo.

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
> > [!note] 📋 Figura — Aceleración
> > >
> > > ![[../Unidad 0 - Guias y Ejercicios/Diagramas/Cinemática_Traslacional_02.svg]]
> > >
> > > **Se lee así:** el diagrama muestra la progresión del movimiento: MRU, MRUA, caída libre y movimiento en plano, con sus características distintivas.

---

## 📝 Ejercicios Propuestos

> [!example] 🍎 Caída Libre
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
> - [ ] Analiza el movimiento en 2D y 3D usando vectores posición.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - J. Serway, R. Jewett, *Física para Ciencias e Ingeniería*, cap. 2 «Movimiento en una dimensión».
> - Apuntes del curso FISG1001 «Física Mecánica», ESPOL.
> - Diagramas de la materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

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

> [!info] 📚 Próximos pasos
>
> - [[Cinemática Rotacional]] — movimiento angular y sus analogías con el lineal.
> - [[Vectores]] — conceptos de función del tiempo en 2D y 3D.
> - [[Leyes de Newton]] — causas del movimiento (dinámica).
> - Repaso: vuelve a las definiciones formales antes de los ejercicios.

**Tags:** #FISG1001 #unidad1 #cinematica #movimiento-rectilineo #mrua #caida-libre
