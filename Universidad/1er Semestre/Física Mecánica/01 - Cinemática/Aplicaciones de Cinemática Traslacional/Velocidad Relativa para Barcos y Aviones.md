---
dg-publish: true
tags: [FISG1001, unidad1, cinematica, velocidad-relativa, navegacion]
---

# 🚤 Velocidad Relativa para Barcos y Aviones

## 🎯 Introducción

> [!info] 💡 ¿Por Qué la Velocidad Relativa Importa en la Navegación?
>
> Un avión no vuela solo respecto al aire: el aire se mueve respecto a la tierra. Un barco no navega solo respecto al agua: la corriente se mueve respecto a la costa. La velocidad que mide el GPS (respecto a tierra) es distinta de la que marca el velocímetro (respecto al medio). Esta nota enseña a combinar vectores de velocidad para predecir la trayectoria real de cualquier vehículo en un medio en movimiento.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Velocidad_Relativa_para_Barcos_y_Aviones_01.svg]]
>
> **Se lee así:** el diagrama muestra que la velocidad del avión respecto a tierra es la suma vectorial de su velocidad respecto al aire más la velocidad del viento respecto a tierra.

---

## 📋 Definiciones Formales

### 1️⃣ Velocidad Relativa

> [!note] 📋 Definición — Velocidad Relativa
>
> La **velocidad relativa** es la velocidad de un objeto medida respecto a otro objeto de referencia que también puede estar en movimiento. Se expresa como la diferencia vectorial entre dos velocidades absolutas.
>
> **Ecuación fundamental:** $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$
>
> Donde $\vec{v}_{AB}$ es la velocidad de A respecto a B.
>
> - Es una cantidad vectorial (tiene magnitud y dirección)
> - Siempre requiere especificar "respecto a qué" se mide
> - **Unidades:** m/s, km/h
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Velocidad_Relativa_para_Barcos_y_Aviones_01.svg]]
>
> **Se lee así:** el diagrama muestra que la velocidad resultante es la suma vectorial de la velocidad del vehículo respecto al medio y la velocidad del medio respecto a tierra.

### 2️⃣ Sistemas de Referencia

> [!note] 📋 Definición — Sistemas de Referencia
>
> Un **sistema de referencia** es el punto de vista desde el cual se mide el movimiento. En navegación se distinguen tres sistemas principales:
>
> - **Terrestre (fija):** respecto a la superficie terrestre (GPS, mapas) — símbolo $\vec{v}_g$
> - **Del medio (aire/agua):** respecto al fluido en movimiento (velocímetros) — símbolo $\vec{v}_a$ o $\vec{v}_w$
> - **Del vehículo:** respecto al vehículo en movimiento (observador interno) — símbolo $\vec{v}_v$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Velocidad_Relativa_para_Barcos_y_Aviones_02.svg]]
>
> **Se lee así:** el diagrama muestra cómo la velocidad del barco respecto al agua y la velocidad de la corriente se combinan para dar la velocidad del barco respecto a tierra.

### 3️⃣ Vector de Deriva y Rumbo de Compensación

> [!note] 📋 Definición — Deriva y Rumbo de Compensación
>
> La **deriva** es el desplazamiento lateral no deseado causado por el medio en movimiento (viento o corriente). El **rumbo de compensación** es la dirección que debe tomar el vehículo para anular la deriva y alcanzar el destino deseado.
>
> - **Deriva:** $\vec{v}_{deriva} = \vec{v}_{medio}$
> - **Ecuación de compensación:** $\vec{v}_{deseada} = \vec{v}_{vehículo/medio} + \vec{v}_{compensación}$
> - El rumbo compensado debe anular la componente lateral de la deriva
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/Velocidad_Relativa_para_Barcos_y_Aviones_03.svg]]
>
> **Se lee así:** el diagrama muestra cómo el rumbo compensado apunta contra la deriva para que la velocidad resultante lleve al vehículo directamente al destino.

---

## 📝 Ejercicios Propuestos

### ✏️ Ejercicio 1 — Avión con Viento Lateral

> [!example] 📋 Planteamiento
>
> Un avión vuela hacia el Norte a 300 km/h respecto al aire. Hay un viento del Oeste de 50 km/h. Determinar la velocidad resultante respecto a tierra (magnitud y dirección).
>
> **Datos:** $\vec{v}_{avión/aire} = 300\hat{j}$ km/h, $\vec{v}_{viento/tierra} = 50\hat{i}$ km/h
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Aplicar ecuación vectorial: $\vec{v}_{avión/tierra} = \vec{v}_{avión/aire} + \vec{v}_{viento/tierra} = 50\hat{i} + 300\hat{j}$
> >
> > **Paso 2:** Calcular magnitud: $|\vec{v}| = \sqrt{50^2 + 300^2} = \sqrt{92500} \approx 304.1$ km/h
> >
> > **Paso 3:** Calcular dirección: $\theta = \arctan(50/300) = \arctan(0.167) \approx 9.46°$
> >
> > **Respuesta:** 304.1 km/h, 9.46° al Este del Norte

### ✏️ Ejercicio 2 — Barco Cruzando Río

> [!example] 📋 Planteamiento
>
> Un barco quiere cruzar un río de 200 m de ancho perpendicularmente. La corriente fluye a 3 m/s hacia el Este. El barco navega a 5 m/s respecto al agua. ¿Qué rumbo debe seguir y cuánto tardará?
>
> **Datos:** $d = 200$ m, $\vec{v}_{corriente} = 3\hat{i}$ m/s, $|\vec{v}_{barco/agua}| = 5$ m/s
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Para cruzar perpendicularmente, cancelar la corriente: $v_{barco,x} = -3$ m/s
> >
> > **Paso 2:** Componente Norte: $v_{barco,y} = \sqrt{5^2 - 3^2} = \sqrt{16} = 4$ m/s
> >
> > **Paso 3:** Rumbo: $\theta = \arctan(-3/4) = -36.87°$ (36.87° Oeste del Norte)
> >
> > **Paso 4:** Tiempo: $t = 200 / 4 = 50$ s
> >
> > **Respuesta:** 36.87° al Oeste del Norte, 50 segundos

### ✏️ Ejercicio 3 — Rumbo de Compensación

> [!example] 📋 Planteamiento
>
> Un piloto quiere volar directamente al Norte. Hay viento del Sur a 40 km/h y el avión vuela a 200 km/h respecto al aire. ¿Qué rumbo debe tomar y cuál es su velocidad respecto a tierra?
>
> **Datos:** $\vec{v}_{viento/tierra} = -40\hat{j}$ km/h (Sur), $|\vec{v}_{avión/aire}| = 200$ km/h, destino al Norte
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** La componente Norte del avión debe superar el viento: $v_y = 200 \sin(\theta) - 40$
> >
> > **Paso 2:** Para ir directo al Norte, la componente Este debe ser cero: el avión apunta al Oeste
> >
> > **Paso 3:** $\sin(\theta) = 40/200 = 0.2$, por lo que $\theta = \arcsin(0.2) \approx 11.5°$ al Oeste del Norte
> >
> > **Paso 4:** Velocidad respecto a tierra: $v_g = 200 \cos(11.5°) - 40 \approx 196 - 40 = 156$ km/h
> >
> > **Respuesta:** Rumbo 11.5° Oeste del Norte, $v_g \approx 156$ km/h

### ✏️ Ejercicio 4 — Velocidad Relativa en 2D

> [!example] 📋 Planteamiento
>
> Un barco se desplaza a 10 km/h respecto al agua en dirección 30° al Norte del Este. Hay una corriente de 4 km/h hacia el Este. Calcular la velocidad del barco respecto a tierra.
>
> **Datos:** $|\vec{v}_{barco/agua}| = 10$ km/h, dirección 30° N de E, $\vec{v}_{corriente} = 4\hat{i}$ km/h
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** Descomponer velocidad del barco: $v_x = 10\cos(30°) = 8.66$, $v_y = 10\sin(30°) = 5$
> >
> > **Paso 2:** Sumar corriente: $v_{tierra,x} = 8.66 + 4 = 12.66$, $v_{tierra,y} = 5$
> >
> > **Paso 3:** Magnitud: $|\vec{v}_{tierra}| = \sqrt{12.66^2 + 5^2} = \sqrt{160.3 + 25} = \sqrt{185.3} \approx 13.6$ km/h
> >
> > **Paso 4:** Dirección: $\theta = \arctan(5/12.66) \approx 21.5°$ al Norte del Este
> >
> > **Respuesta:** 13.6 km/h, 21.5° al Norte del Este

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino velocidad relativa y explico por qué depende del sistema de referencia.
> - [ ] Distinguo velocidad respecto al medio vs respecto a tierra.
> - [ ] Aplico $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$ en problemas simples.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo problemas de viento lateral y corrientes cruzadas.
> - [ ] Calculo rumbos de compensación para anular la deriva.
> - [ ] Descompono vectores en componentes x, y y recombino.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo problemas de navegación con múltiples medios en movimiento.
> - [ ] Analizo trayectorias curvas debidas a deriva en 2D y 3D.

---

## 📚 Referencias

> [!quote] 📖 Fuentes Consultadas
>
> - J. Serway, R. Jewett, *Física para Ciencias e Ingeniería*, cap. 4 «Movimiento en dos y tres dimensiones».
> - Apuntes del curso FISG1001 «Física Mecánica», ESPOL.
> - Diagramas de la materia (`Unidad 0 - Guias y Ejercicios/Diagramas/`).

---

## 🔁 Repaso SR (flashcards)

#flashcards/fisica-u1

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es la velocidad relativa?::Velocidad de un objeto medida respecto a otro objeto en movimiento: $\vec{v}_{AB} = \vec{v}_A - \vec{v}_B$.
> - ¿Cuáles son los 3 sistemas de referencia en navegación?::Terrestre (tierra), del medio (aire/agua), del vehículo.
> - ¿Qué es la deriva?::Desplazamiento lateral causado por el medio en movimiento (viento o corriente).
> - ¿Cómo se calcula el rumbo de compensación?::Apuntando contra la deriva para que la velocidad resultante vaya al destino.
> - ¿Cuál es la ecuación de velocidad respecto a tierra?::$\vec{v}_{vehículo/tierra} = \vec{v}_{vehículo/medio} + \vec{v}_{medio/tierra}$.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas Relacionadas
>
> - [[Cinemática Traslacional]] — conceptos base de movimiento y vectores.
> - [[Vectores]] — operaciones vectoriales y descomposición en componentes.
> - [[Problemas de Encuentro]] — aplicación de velocidad relativa a encuentros.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - [[Problemas de Tiempo-Distancia]] — cinemática aplicada a desplazamientos.
> - [[Problemas de Persecución]] — movimiento relativo entre dos objetos.
> - [[Unidad 0 - Guias y Ejercicios/Diagramas/Velocidad_Relativa_para_Barcos_y_Aviones_04.svg]] — diagrama de representación gráfica para repasar visualmente.
> - Repaso: vuelve a las definiciones formales antes de los ejercicios.

---

**Tags:** #FISG1001 #unidad1 #cinematica #velocidad-relativa #navegacion
