---
dg-publish: true
tags: [MATG1045, unidad7, volumenes-de-solidos-de-revolucion, integrales, volumenes, solidos-de-revolucion, geometria, aplicaciones-integrales, metodos-integracion, disco, arandelas, capas-cilindricas]
---

# 🌪️ Volúmenes de Sólidos de Revolución

## 🎯 Introducción

> [!info] 💡 Qué son y por qué importa
>
> Los **sólidos de revolución** son figuras tridimensionales generadas al rotar una región plana alrededor de un eje. Su volumen se calcula sumando elementos geométricos que aprovechan la simetría rotacional: discos, arandelas o capas cilíndricas.
>
> **Por qué importa:** es la primera aplicación tridimensional de la integral: convierte "rotar una región" en una suma de áreas de corte. La elección del corte (perpendicular o paralelo al eje) decide el método, y esa decisión es la mitad del ejercicio.
>
> **Ejemplo:** al rotar $y = \sqrt{x}$ alrededor del eje $x$ en $[0, 4]$, un corte perpendicular da discos de radio $\sqrt{x}$ y área $\pi x$, y el volumen sale $\pi\int_0^4 x\,dx = 8\pi$.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — el sólido de revolución y los tres métodos con su figura.
> - **Procedimiento Paso a Paso** — cómo elegir corte y método, con la tabla comparativa.
> - **Ejemplos Resueltos** — disco, arandela y capas, los tres casos canónicos.
> - **Ejercicios Propuestos** — seis plantillas, una por cada variante.
>
> **Por qué importa:** disco, arandela y capas no son tres fórmulas distintas sino tres maneras de medir el mismo sólido; el mapa empieza eligiendo el corte.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Sólido de revolución y el mapa de la región al volumen
>
> Un **sólido de revolución** se genera al rotar una región plana $R$ alrededor de un eje $L$. Cada método lo mide con un corte distinto: perpendicular al eje (discos o arandelas) o paralelo (capas cilíndricas).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Volúmenes_de_Sólidos_de_Revolución_04.svg]]
>
> **Se lee así:** una cadena horizontal en un solo sentido, sin rombos: se parte de la región plana y su eje de revolución, se hace rotar la región para obtener el sólido tridimensional, del que cuelgan dos lecturas complementarias —cortes perpendiculares al eje (discos o arandelas) y cortes paralelos (capas cilíndricas)— y ambas confluyen en integrar las áreas de corte hasta obtener el volumen total.
>
> **Por qué importa:** muestra que disco, arandela y capas no son tres fórmulas distintas sino tres maneras de medir el mismo sólido. Te obliga a elegir el corte antes que el método, que es la causa de la mayoría de los errores.
>
> **Ejemplo:** para rotar $y = \sqrt{x}$ alrededor del eje $x$, un corte perpendicular da un disco de radio $\sqrt{x}$ y área $\pi x$; para rotar alrededor de un eje vertical, un corte paralelo da una capa cilíndrica.

> [!note] 📋 Definición — Método del disco
>
> Cuando una función $f(x) \geq 0$ se rota alrededor del eje $x$, genera **discos** perpendiculares al eje de rotación:
> $$V = \pi \int_a^b [f(x)]^2\,dx$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Volúmenes_de_Sólidos_de_Revolución_01.svg]]
>
> **Se lee así:** seis rectángulos en línea recta, sin ninguna decisión: la función entra en la rotación alrededor de un eje, esa rotación genera **discos**, el disco toma como radio el valor de la función, su área resulta $\pi[f(x)]^2$ y al integrar esa área aparece el volumen. Cada caja es el eslabón siguiente, así que la fórmula se construye paso a paso.
>
> **Por qué importa:** el método del disco se entiende como una suma de círculos, no como una fórmula que sale de la nada. Así se justifica cada factor: el $\pi$ del círculo, el cuadrado del radio y el $dx$ como **grosor del disco**.
>
> **Ejemplo:** al rotar $f(x) = \sqrt{x}$ alrededor del eje $x$ en $[0, 4]$ la nota aplica el método del disco y obtiene $V = \pi \int_0^4 (\sqrt{x})^2\,dx = 8\pi$.

> [!note] 📋 Definición — Método de las arandelas
>
> Las **arandelas** se forman cuando hay una cavidad interior: al rotar una región entre dos funciones $f(x) \geq g(x) \geq 0$, el sólido tiene un hueco y el volumen es la diferencia de dos discos:
> $$V = \pi \int_a^b \left([f(x)]^2 - [g(x)]^2\right)dx$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Volúmenes_de_Sólidos_de_Revolución_02.svg]]
>
> **Se lee así:** la región entre curvas se abre en dos ramas paralelas, una que identifica la **función exterior** y otra la interior. Cada rama produce su propio radio y ambas desembocan en la misma caja central, donde el anillo se modela como la diferencia entre el área del disco grande y la del hueco. Solo entonces se integra esa diferencia para dar el volumen.
>
> **Por qué importa:** la arandela es la generalización del disco cuando hay cavidad, y su fórmula se obtiene **restando dos áreas**, no inventándola. Identificar bien qué función da el radio exterior evita el error de invertir los radios y perder el signo.
>
> **Ejemplo:** rotando la región entre $f(x) = x + 2$ y $g(x) = x^2$ alrededor del eje $x$ en $[-1, 2]$, la nota usa $V = \pi \int_{-1}^{2} [(x+2)^2 - (x^2)^2]\,dx$.

> [!note] 📋 Definición — Método de las capas cilíndricas
>
> El sólido se aproxima por **cilindros concéntricos** de grosor infinitesimal, como capas de una cebolla. Al rotar alrededor del eje $y$:
> $$V = 2\pi \int_a^b x \cdot f(x)\,dx$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Volúmenes_de_Sólidos_de_Revolución_03.svg]]
>
> **Se lee así:** la función entra en la rotación alrededor del eje $y$, que produce **cilindros concéntricos**, y desde ahí el flujo se bifurca: una rama da el radio y otra la altura. Ambas vuelven a juntarse en la caja de la circunferencia, que multiplicada por la altura da el área lateral del cilindro, y esa área lateral es la que finalmente se integra para obtener el volumen.
>
> **Por qué importa:** las capas cilíndricas son el método natural cuando se rota alrededor del eje $y$, y te ahorran despejar $x$ en función de $y$. Ver la circunferencia $2\pi x$ como la fuente del factor te evita **olvidar ese $2\pi$**, el error más común.
>
> **Ejemplo:** rotando $f(x) = x^2$ alrededor del eje $y$ en $[0, 2]$, la nota arma $V = 2\pi \int_0^2 x \cdot x^2\,dx$ y llega a $8\pi$.

---

## 🔧 Procedimiento Paso a Paso

> [!tip] 🔎 Estrategia de visualización
>
> 1. **Visualiza** la región original (boséjala con los cortes que vas a usar).
> 2. **Rota** mentalmente alrededor del eje.
> 3. **Identifica** la forma geométrica resultante: disco, arandela o capa.
> 4. **Aplica** la fórmula correspondiente con los límites correctos.
>
> **Por qué importa:** el orden fija el corte antes que la fórmula: quien salta al paso 4 sin el paso 3 elige el método al azar.

> [!tip] 📋 Tabla comparativa de métodos
>
> | Aspecto | Disco 💿 | Arandelas 🍩 | Capas cilíndricas 🥤 |
> |---|---|---|---|
> | **Geometría** | Círculos sólidos | Círculos con agujero | Cilindros huecos |
> | **Rotación típica** | Eje $x$ | Eje $x$ | Eje $y$ |
> | **Fórmula** | $\pi\int [f(x)]^2\,dx$ | $\pi\int ([f(x)]^2 - [g(x)]^2)\,dx$ | $2\pi\int x \cdot f(x)\,dx$ |
> | **Cuándo usar** | Una función, eje $x$ | Entre dos funciones | Rotación eje $y$ |
> | **Ventaja** | Más simple | Maneja cavidades | Evita invertir la función |
>
> **Por qué importa:** es la consulta de tres segundos: región contra un eje → disco; entre dos curvas → arandela; rotación alrededor de eje vertical con franjas verticales → capas.

> [!tip] 🎓 Mnemotecnia "DCA" (Disco–Capas–Arandelas)
>
> - 💿 **D**isco: "**D**iámetro al cuadrado" → $\pi [f(x)]^2$
> - 🥤 **C**apas: "**C**ircunferencia por altura" → $2\pi x \cdot f(x)$
> - 🍩 **A**randelas: "**A**fuera menos adentro" → $\pi (R^2 - r^2)$
>
> **Por qué importa:** las tres letras resumen los tres elementos de área: círculo completo, lateral de cilindro y anillo.

---

## 🧮 Ejemplos Resueltos

> [!example] 🔢 Ejemplo 1 — Disco: $f(x) = \sqrt{x}$ alrededor del eje $x$ en $[0, 4]$
>
> **Elemento:** disco de radio $f(x) = \sqrt{x}$, área $\pi (\sqrt{x})^2 = \pi x$, grosor $dx$.
>
> **Cálculo:**
> $$V = \pi \int_0^4 (\sqrt{x})^2\,dx = \pi \int_0^4 x\,dx = \pi \left[\frac{x^2}{2}\right]_0^4 = 8\pi$$
>
> **Por qué importa:** el caso más limpio del disco: el radio es la propia función y el cuadrado simplifica el integrando a $x$.

> [!example] 🔢 Ejemplo 2 — Arandelas: región entre $f(x) = x + 2$ y $g(x) = x^2$ alrededor del eje $x$ en $[-1, 2]$
>
> **Cruces:** $x + 2 = x^2 \Rightarrow x^2 - x - 2 = 0 \Rightarrow (x-2)(x+1) = 0 \Rightarrow x = -1, 2$ (los propios límites).
>
> **Radios:** exterior $R = x + 2$, interior $r = x^2$ (en $x = 0$: $2 > 0$ ✓).
>
> **Cálculo:**
> $$V = \pi \int_{-1}^2 \left[(x+2)^2 - (x^2)^2\right]dx = \pi \int_{-1}^2 (x^2 + 4x + 4 - x^4)\,dx$$
> $$= \pi \left[\frac{x^3}{3} + 2x^2 + 4x - \frac{x^5}{5}\right]_{-1}^2 = \pi \left(\frac{184}{15} + \frac{32}{15}\right) = \frac{72\pi}{5}$$
>
> **Por qué importa:** la cavidad se resta como disco completo menos disco hueco; invertir $R$ y $r$ daría volumen negativo, la señal de que el orden estaba mal.

> [!example] 🔢 Ejemplo 3 — Capas cilíndricas: $f(x) = x^2$ alrededor del eje $y$ en $[0, 2]$
>
> **Elemento:** capa de radio $x$, altura $f(x) = x^2$, circunferencia $2\pi x$, grosor $dx$.
>
> **Cálculo:**
> $$V = 2\pi \int_0^2 x \cdot x^2\,dx = 2\pi \int_0^2 x^3\,dx = 2\pi \left[\frac{x^4}{4}\right]_0^2 = 2\pi \cdot 4 = 8\pi$$
>
> **Por qué importa:** rotar alrededor del eje $y$ con cortes verticales evita despejar $x = \sqrt{y}$; el factor $2\pi x$ es la circunferencia de la capa, no un adorno.

> [!example] 🔢 Ejemplo 4 — Disco respecto a $y$: $x = y^2$ alrededor del eje $y$ en $[0, 2]$
>
> **Elemento:** corte perpendicular al eje $y$: disco de radio $x = y^2$.
>
> **Cálculo:**
> $$V = \pi \int_0^2 (y^2)^2\,dy = \pi \int_0^2 y^4\,dy = \pi \left[\frac{y^5}{5}\right]_0^2 = \frac{32\pi}{5}$$
>
> **Por qué importa:** el mismo método del disco cambia de variable con el eje: el radio siempre es la distancia de la curva al eje de rotación.

---

## ⚠️ Errores Comunes

> [!warning] 🚨 Errores frecuentes
>
> - ❌ Olvidar el $\pi$ en métodos de disco y arandelas.
> - ❌ Confundir radio interior y exterior en arandelas.
> - ❌ No considerar el $2\pi$ en capas cilíndricas.
> - ❌ Usar límites incorrectos de integración (los de $x$ cuando se integra en $y$, o los del enunciado en lugar de los cruces).
>
> **Por qué importa:** los cuatro son errores de planteamiento que no avisan con signo raro: el volumen "se ve" razonable. La verificación geométrica (cilindro $\pi r^2 h$, cono $\frac{1}{3}\pi r^2 h$, esfera $\frac{4}{3}\pi r^3$) los detecta.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Halla el volumen del sólido generado al rotar $y = x^3$ alrededor del eje $x$ en $[0, 1]$.
>
> > [!success]- ✅ Solución
> > Disco de radio $x^3$: $V = \pi \int_0^1 x^6\,dx = \pi \left[\frac{x^7}{7}\right]_0^1 = \frac{\pi}{7}$.
> > **Lección:** el radio se eleva al cuadrado en la fórmula: $(x^3)^2 = x^6$ ✓

> [!example] 📋 Planteamiento
>
> Halla el volumen al rotar la región entre $y = \sqrt{x}$ y $y = x^2$ alrededor del eje $x$.
>
> > [!success]- ✅ Solución
> > Cruces en $x = 0, 1$; exterior $R = \sqrt{x}$, interior $r = x^2$:
> > $$V = \pi \int_0^1 \left(x - x^4\right)dx = \pi \left[\frac{x^2}{2} - \frac{x^5}{5}\right]_0^1 = \pi \left(\frac{1}{2} - \frac{1}{5}\right) = \frac{3\pi}{10}$$
> > **Lección:** la arandela es disco grande menos disco chico, no la suma ✓

> [!example] 📋 Planteamiento
>
> Halla el volumen al rotar $y = \sqrt{x}$ alrededor del eje $y$ en $[0, 4]$ con capas.
>
> > [!success]- ✅ Solución
> > Capa de radio $x$ y altura $\sqrt{x}$:
> > $$V = 2\pi \int_0^4 x \cdot \sqrt{x}\,dx = 2\pi \int_0^4 x^{3/2}\,dx = 2\pi \left[\frac{2x^{5/2}}{5}\right]_0^4 = 2\pi \cdot \frac{2 \cdot 32}{5} = \frac{128\pi}{5}$$
> > **Lección:** $4^{5/2} = 32$; la capa ahorra despejar $x = y^2$ ✓

> [!example] 📋 Planteamiento
>
> Halla el volumen al rotar la región entre $x = y$ y $x = y^2$ alrededor del eje $y$.
>
> > [!success]- ✅ Solución
> > Cruces en $y = 0, 1$; exterior $R = y$, interior $r = y^2$:
> > $$V = \pi \int_0^1 (y^2 - y^4)\,dy = \pi \left[\frac{y^3}{3} - \frac{y^5}{5}\right]_0^1 = \pi \left(\frac{1}{3} - \frac{1}{5}\right) = \frac{2\pi}{15}$$
> > **Lección:** la misma arandela funciona respecto a $y$ con radios leídos en horizontal ✓

> [!example] 📋 Planteamiento
>
> Halla el volumen al rotar la región entre $y = x$ y $y = x^2$ alrededor del eje $y$ con capas.
>
> > [!success]- ✅ Solución
> > Capa de radio $x$ y altura $(x - x^2)$:
> > $$V = 2\pi \int_0^1 x(x - x^2)\,dx = 2\pi \int_0^1 (x^2 - x^3)\,dx = 2\pi \left(\frac{1}{3} - \frac{1}{4}\right) = \frac{\pi}{6}$$
> > **Lección:** la altura de la capa es la diferencia de las dos curvas, no una sola ✓

> [!example] 📋 Planteamiento
>
> Verifica con disco el volumen de la esfera de radio $2$: rota el semicírculo $y = \sqrt{4 - x^2}$ alrededor del eje $x$.
>
> > [!success]- ✅ Solución
> > $$V = \pi \int_{-2}^{2} (4 - x^2)\,dx = \pi \left[4x - \frac{x^3}{3}\right]_{-2}^{2} = \pi \left(8 - \frac{8}{3} + 8 - \frac{8}{3}\right) = \frac{32\pi}{3}$$
> > **Lección:** coincide con $\frac{4}{3}\pi r^3 = \frac{32\pi}{3}$: la fórmula del disco deriva la de la esfera ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico el elemento de volumen (disco, arandela o capa) según la región y el eje de rotación.
> - [ ] Escribo la fórmula del disco $V = \pi \int_a^b [f(x)]^2\,dx$ con el radio correcto.
> - [ ] Reconozco cuándo hay cavidad y aplico la arandela $\pi \int (R^2 - r^2)\,dx$.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Elijo corte perpendicular o paralelo al eje según qué evita invertir la función.
> - [ ] Calculo volúmenes de rotación alrededor del eje $y$ con capas $2\pi \int x f(x)\,dx$.
> - [ ] Uso los cruces de las curvas como límites de integración y verifico el orden de los radios.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo rotaciones alrededor de ejes distintos de los coordenados desplazando radios.
> - [ ] Verifico resultados contra sólidos conocidos (cilindro, cono, esfera) y contra la tabla comparativa.
> - [ ] Traduzco problemas de ingeniería (tanques, ejes, perfiles) a una integral de volumen con el método más barato.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage): aplicaciones del integral definido — volúmenes por discos, arandelas y capas cilíndricas.
> - G. Strang, *Calculus* (Wellesley-Cambridge): volúmenes de revolución y la elección del corte.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el área que se rota para generar el sólido.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/02 - Área entre Curvas|02 - Área entre Curvas]] — la región entre dos curvas que produce la arandela.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la evaluación de la integral de volumen.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — técnicas necesarias para resolver las integrales.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — aditividad y linealidad en los cálculos.
> - [[2do Semestre/Cálculo Vectorial/Cálculo Vectorial|Cálculo Vectorial]] — la extensión multivariable de estas mismas ideas.
>
> **Conexiones interdisciplinarias:** física (momentos y centros de masa con las mismas integrales), ingeniería (tanques, ejes y perfiles de revolución) y geometría analítica (visualización de las regiones).

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u7

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué es un sólido de revolución?::La región plana $R$ rotada alrededor de un eje $L$; su volumen se mide sumando elementos de corte.
> - ¿Cuál es la fórmula del disco?::$V = \pi \int_a^b [f(x)]^2\,dx$: radio $f(x)$, área $\pi [f(x)]^2$, grosor $dx$.
> - ¿Cuándo toca arandela?::Cuando la región entre dos curvas $f \geq g \geq 0$ genera una cavidad: $V = \pi \int_a^b ([f]^2 - [g]^2)\,dx$.
> - ¿Cuándo toca capas cilíndricas?::Al rotar alrededor del eje $y$ con franjas verticales: $V = 2\pi \int_a^b x \cdot f(x)\,dx$ (circunferencia $\times$ altura $\times$ grosor).
> - ¿Qué decide el método?::El corte: perpendicular al eje (disco/arandela) o paralelo (capa); elegir primero el corte evita la mitad de los errores.
> - ¿De dónde sale el $2\pi$ de las capas?::De la circunferencia $2\pi x$ de la capa cilíndrica de radio $x$.
> - ¿Cómo se verifica un volumen calculado?::Contrastándolo con sólidos conocidos: cilindro $\pi r^2 h$, cono $\frac{1}{3}\pi r^2 h$, esfera $\frac{4}{3}\pi r^3$.
> - ¿Qué pasa si se invierten los radios de la arandela?::El integrando sale negativo y el volumen también: la señal es que $R$ y $r$ están al revés.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el área que se rota para generar el sólido.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/02 - Área entre Curvas|02 - Área entre Curvas]] — la región entre dos curvas que produce la arandela.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la evaluación de la integral de volumen.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — técnicas necesarias para resolver las integrales.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — aditividad y linealidad en los cálculos.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — la otra medida de la misma región: longitud, no volumen.
>
> **Conexiones interdisciplinarias:** física (momentos y centros de masa con las mismas integrales), ingeniería (tanques, ejes, perfiles de revolución) y geometría analítica (visualización de regiones y sólidos).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 4: disco puro en $x$ y en $y$, el caso más limpio.
> - Después el 2 y el 5: arandelas y capas, los dos métodos que manejan regiones entre curvas.
> - Cierra con 3 y 6: capas que ahorran invertir la función y la verificación con la esfera.
> - Cuando lo tengas, sigue con [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/02 - Volúmenes con Ejes Arbitrarios y Casos Avanzados|02 - Volúmenes con Ejes Arbitrarios y Casos Avanzados]] y luego [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]].

---

**Tags:** #MATG1045 #unidad7 #volumenes-de-solidos-de-revolucion #integrales #volumenes #solidos-de-revolucion #geometria #aplicaciones-integrales #metodos-integracion #disco #arandelas #capas-cilindricas
