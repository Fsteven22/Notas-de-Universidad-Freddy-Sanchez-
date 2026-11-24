---
dg-publish: true
tags: [FISG1001, unidad1, cinematica, tiempo-distancia, velocidad-media]
---

# ⏱️ Problemas de Tiempo y Distancia

## 🎯 Introducción

> [!info] 💡 ¿Por Qué los Problemas de Tiempo y Distancia Son Fundamentales?
>
> Casi todo viaje real se hace por tramos: un auto cambia de velocidad al entrar a una ciudad, un ciclista sube y baja colinas, un avión varia su crucero según la altitud. Estos problemas enseñan a organizar datos incompletos, calcular distancias y tiempos totales, y sobre todo, a entender que la velocidad media **no es** el promedio aritmético de las velocidades.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Problemas_de_Tiempo-Distancia_01.svg]]
>
> **Se lee así:** el diagrama muestra cómo cada tramo de un viaje aporta su propia distancia y tiempo, y cómo se suman para obtener los totales del viaje completo.

---

## 📋 Definiciones Formales

### 1️⃣ Problemas de Tiempo y Distancia

> [!note] 📋 Definición — Problemas de Tiempo y Distancia
>
> Son situaciones donde un móvil **viaja por diferentes tramos** con velocidades distintas, y se requiere calcular la distancia total, el tiempo total y la velocidad media del recorrido completo.
>
> **Principio fundamental:** $d_{total} = \sum d_i$, $t_{total} = \sum t_i$, $\bar{v} = \frac{d_{total}}{t_{total}}$
>
> - Se resuelven tramo por tramo usando $d = v \cdot t$
> - Cada tramo puede tener datos conocidos o faltantes
> - La velocidad media del viaje **no es** el promedio de las velocidades de cada tramo
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Problemas_de_Tiempo-Distancia_01.svg]]
>
> **Se lee así:** el diagrama muestra que cada tramo tiene su propia velocidad, tiempo y distancia, y que los totales se obtienen sumando las contribuciones de cada tramo.

### 2️⃣ Velocidad Media

> [!note] 📋 Definición — Velocidad Media
>
> La **velocidad media** es la razón entre la distancia total recorrida y el tiempo total empleado. **No equivale al promedio aritmético de las velocidades** de cada tramo.
>
> **Fórmula:** $\bar{v} = \frac{d_{total}}{t_{total}}$
>
> **Velocidad media armónica:** cuando se recorren distancias iguales a velocidades diferentes, $\bar{v} = \frac{2v_1 v_2}{v_1 + v_2}$ (para dos tramos) o $\bar{v} = \frac{n}{\sum \frac{1}{v_i}}$ (para n tramos).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Problemas_de_Tiempo-Distancia_02.svg]]
>
> **Se lee así:** el diagrama muestra que la velocidad media depende de la distancia total y el tiempo total, no de un simple promedio de las velocidades individuales.

### 3️⃣ Metodología de Resolución por Tramos

> [!note] 📋 Definición — Metodología por Tramos
>
> El método sistemático para resolver problemas de tiempo-distancia consiste en: (1) organizar los datos en tabla, (2) completar los datos faltantes por tramo usando $d = v \cdot t$, (3) sumar distancias y tiempos totales, y (4) calcular la velocidad media final.
>
> **Pasos:** Tabla → Completar faltantes → Totales → Velocidad media → Verificar
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Problemas_de_Tiempo-Distancia_02.svg]]
>
> **Se lee así:** el diagrama muestra el flujo lógico: distancia y tiempo por tramo llevan a la velocidad, que se suma para obtener los totales y finalmente la velocidad media.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Viaje por Tramos

> [!example] 📋 Planteamiento
>
> Un móvil viaja 2 horas a 60 km/h, luego 3 horas a 80 km/h, y finalmente 120 km a 40 km/h. Calcular: a) distancia total, b) tiempo total, c) velocidad media.
>
> **Datos:** Tramo 1: $t_1=2$ h, $v_1=60$ km/h; Tramo 2: $t_2=3$ h, $v_2=80$ km/h; Tramo 3: $d_3=120$ km, $v_3=40$ km/h
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Tabla de tramos
> >
> > |Tramo|Tiempo (h)|Velocidad (km/h)|Distancia (km)|
> > |---|---|---|---|
> > |1|2|60|$60 \times 2 = 120$|
> > |2|3|80|$80 \times 3 = 240$|
> > |3|$120/40 = 3$|40|120|
> > |**TOTAL**|**8**|—|**480**|
> >
> > **Paso 2:** Velocidad media: $\bar{v} = 480 / 8 = 60$ km/h
> >
> > **Respuesta:** a) 480 km, b) 8 h, c) 60 km/h

### ✏️ Ejercicio 2 — Ida y Vuelta

> [!example] 📋 Planteamiento
>
> Un auto va de la ciudad A a la B (180 km) a 90 km/h y regresa por la misma ruta a 60 km/h. Calcular la velocidad media del viaje completo.
>
> **Datos:** Ida: $d_1=180$ km, $v_1=90$ km/h; Vuelta: $d_2=180$ km, $v_2=60$ km/h
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Tiempos: $t_1 = 180/90 = 2$ h, $t_2 = 180/60 = 3$ h
> >
> > **Paso 2:** Totales: $d_{total} = 360$ km, $t_{total} = 5$ h
> >
> > **Paso 3:** Velocidad media: $\bar{v} = 360/5 = 72$ km/h
> >
> > **Verificación (armónica):** $\bar{v} = \frac{2 \times 90 \times 60}{90 + 60} = 72$ km/h
> >
> > **Respuesta:** 72 km/h (NO es 75 km/h, que sería el promedio aritmético incorrecto)

### ✏️ Ejercicio 3 — Velocidad Media Armónica

> [!example] 📋 Planteamiento
>
> Un ciclista recorre 30 km a 15 km/h y otros 30 km a 10 km/h. Calcular la velocidad media del recorrido total de 60 km.
>
> **Datos:** Tramo 1: $d_1=30$ km, $v_1=15$ km/h; Tramo 2: $d_2=30$ km, $v_2=10$ km/h
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Tiempos: $t_1 = 30/15 = 2$ h, $t_2 = 30/10 = 3$ h
> >
> > **Paso 2:** Totales: $d_{total} = 60$ km, $t_{total} = 5$ h
> >
> > **Paso 3:** Velocidad media: $\bar{v} = 60/5 = 12$ km/h
> >
> > **Verificación (armónica):** $\bar{v} = \frac{2 \times 15 \times 10}{15 + 10} = \frac{300}{25} = 12$ km/h
> >
> > **Respuesta:** 12 km/h

### ✏️ Ejercicio 4 — Movimiento con Paradas

> [!example] 📋 Planteamiento
>
> Un autobús viaja 3 horas a 50 km/h, hace una parada de 30 minutos, y luego viaja 2 horas a 60 km/h. Calcular la velocidad media del viaje completo incluyendo la parada.
>
> **Datos:** Tramo 1: $t_1=3$ h, $v_1=50$ km/h; Parada: $t_p=0.5$ h; Tramo 2: $t_2=2$ h, $v_2=60$ km/h
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Distancias: $d_1 = 50 \times 3 = 150$ km, $d_2 = 60 \times 2 = 120$ km
> >
> > **Paso 2:** Tiempo total incluyendo parada: $t_{total} = 3 + 0.5 + 2 = 5.5$ h
> >
> > **Paso 3:** Distancia total: $d_{total} = 150 + 120 = 270$ km
> >
> > **Paso 4:** Velocidad media: $\bar{v} = 270 / 5.5 \approx 49.1$ km/h
> >
> > **Respuesta:** 49.1 km/h (la parada reduce significativamente la velocidad media)

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino tiempo, distancia y velocidad, y aplico $d = v \cdot t$.
> - [ ] Distinguo velocidad media de promedio aritmético de velocidades.
> - [ ] Organizo datos de un viaje en tabla por tramos.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Calculo distancia total, tiempo total y velocidad media de viajes por tramos.
> - [ ] Aplico la fórmula de velocidad media armónica para distancias iguales.
> - [ ] Resuelvo problemas con datos faltantes en algunos tramos.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas que incluyen paradas y cambios de condiciones medioambientales.
> - [ ] Analizo viajes con múltiples tramos y velocidades variables en 2D.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - J. Serway, R. Jewett, *Física para Ciencias e Ingeniería*, cap. 2 «Movimiento en una dimensión».
> - Apuntes del curso FISG1001 «Física Mecánica», ESPOL.
> - Diagramas de la materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

---

## 🔁 Repaso SR (flashcards)

#flashcards/fisica-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la fórmula de la velocidad media?::$\bar{v} = \frac{d_{total}}{t_{total}}$, distancia total dividida entre tiempo total.
> - ¿Es la velocidad media el promedio aritmético de las velocidades?::No, nunca lo es salvo coincidencia; siempre es $d_{total}/t_{total}$.
> - ¿Qué es la velocidad media armónica?::La velocidad media cuando se recorren distancias iguales a velocidades diferentes: $\frac{2v_1v_2}{v_1+v_2}$.
> - ¿Cómo se completa un dato faltante en un tramo?::Usando $d = v \cdot t$ o sus variantes: $t = d/v$, $v = d/t$.
> - ¿Cuenta el tiempo de parada en el tiempo total?::Sí, el tiempo parado cuenta para el tiempo total del viaje.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[Cinemática Traslacional]] — conceptos base de posición, velocidad y aceleración.
> - [[Velocidad Relativa para Barcos y Aviones]] — movimiento relativo en navegación.
> - [[Problemas de Persecución]] — aplicación de tiempo-distancia a móviles múltiples.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - [[Problemas de Persecución]] — dos móviles en movimiento relativo.
> - [[Problemas de Encuentro]] — puntos de encuentro entre móviles.
> - [[Unidad 0 - Guias y Ejercicios/Diagramas/Problemas_de_Tiempo-Distancia_02.svg]] — diagrama de metodología para repasar visualmente.
> - Repaso: vuelve a las definiciones formales antes de los ejercicios.

---

**Tags:** #FISG1001 #unidad1 #cinematica #tiempo-distancia #velocidad-media
