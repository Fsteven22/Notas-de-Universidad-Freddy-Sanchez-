---
dg-publish: true
tags: [MATG1045, unidad3, razon-de-cambio, derivada, tangente, limites, aproximacion-lineal]
---

# 📐 Límite de la Razón de Cambio

## 🎯 Introducción

> [!info] 💡 ¿Qué aparece al hacer el cambio cada vez más pequeño?
>
> La razón de cambio promedio divide el cambio de la variable dependiente entre el cambio de la variable independiente. Al reducir el intervalo hasta una longitud infinitesimal, el cociente deja de describir un tramo y pasa a describir una **dirección instantánea**: la pendiente de la tangente.
>
> Este es el puente entre límites y derivadas. La derivada no aparece como una fórmula aislada, sino como el límite de las secantes. La misma construcción sirve para calcular velocidad, aceleración, costo marginal o tasa de crecimiento.
>
> **Ejemplo:** para $f(x)=x^2$, el cociente en $a=3$ es
> $$\frac{(3+h)^2-3^2}{h}=6+h,$$
> y al tomar $h\to0$ se obtiene $f'(3)=6$.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Derivada como límite
>
> Si $f$ está definida en un entorno de $a$ y el límite
> $$f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}{h}$$
> existe y es finito, entonces $f$ es **derivable en $a$** y el límite es su derivada.
>
> Notaciones equivalentes: $f'(a)$, $\left.\frac{df}{dx}\right|_{x=a}$, $D_xf(a)$ y, para funciones de tiempo, $\dot f(a)$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límite_de_la_Razón_de_Cambio_03.svg]]
>
> **Se lee así:** el diagrama encadena punto fijo, punto móvil y cociente de la secante. El nodo central es el límite cuando $h\to0$; de él salen la pendiente de la tangente y la razón instantánea.
>
> **Por qué importa:** el diagrama muestra que la tangente es el final de un proceso de acercamiento. La derivada conserva exactamente la pendiente que emerge de las secantes.
>
> **Ejemplo:** para $f(x)=x^2$ en $a=3$, el cociente se simplifica a $6+h$ y su límite es $6$.

> [!note] 📋 Formas equivalentes del cociente incremental
>
> Si $f'(a)$ existe, las siguientes expresiones coinciden:
>
> | Forma | Límite | Uso principal |
> |---|---|---|
> | Estándar | $\displaystyle\lim_{h\to0}\frac{f(a+h)-f(a)}h$ | Derivada en un punto |
> | Variable móvil | $\displaystyle\lim_{x\to a}\frac{f(x)-f(a)}{x-a}$ | Analizar el comportamiento cerca de $a$ |
> | General | $\displaystyle\lim_{h\to0}\frac{f(x+h)-f(x)}h$ | Definir $f'(x)$ |
> | Bilateral | Límites izquierdo y derecho iguales y finitos | Verificar derivabilidad |
>
> **Por qué importa:** cambiar la parametrización del incremento no cambia el significado; permite usar el formato más conveniente.
>
> **Ejemplo:** $\lim_{x\to a}\frac{x^2-a^2}{x-a}=\lim_{x\to a}(x+a)=2a$, que coincide con $f'(a)$ para $f(x)=x^2$.

> [!note] 📋 Definición — Razón de cambio instantánea
>
> La **razón de cambio instantánea** de $y=f(x)$ respecto de $x$ en $a$ es
> $$\frac{dy}{dx}\bigg|_{x=a}=f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h.$$
> Si $f$ se mide en unidades $U_f$ y $x$ en $U_x$, la razón tiene unidades $U_f/U_x$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límite_de_la_Razón_de_Cambio_04.svg]]
>
> **Se lee así:** la izquierda separa variable independiente y dependiente; el camino central pasa de razón promedio a instantánea al reducir $\Delta x$ a cero. Las ramas inferiores traducen las unidades a velocidad, aceleración y costo marginal.
>
> **Por qué importa:** las unidades explican qué mide la derivada. No es un cambio abstracto: es “cuánto cambia $y$ por cada unidad de $x$ en ese instante”.
>
> **Ejemplo:** si $s(t)$ es posición en metros y $t$ tiempo en segundos, $s'(t)$ es velocidad en $\mathrm{m/s}$.

> [!note] 📋 Definición — Recta tangente
>
> Si $f$ es derivable en $a$, la recta tangente en $(a,f(a))$ tiene ecuación
> $$y-f(a)=f'(a)(x-a).$$
> Su forma explícita es $y=f'(a)x+[f(a)-af'(a)]$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límite_de_la_Razón_de_Cambio_05.svg]]
>
> **Se lee así:** la función derivable aporta el punto de tangencia y la pendiente. Ambos entran en la ecuación punto-pendiente, que produce la tangente; de ella salen la aproximación lineal y la recta normal.
>
> **Por qué importa:** la tangente conserva información local de la curva: posición y razón de cambio. Su pendiente también determina la normal.
>
> **Ejemplo:** para $f(x)=x^2$ en $a=2$, el punto es $(2,4)$ y la pendiente es $4$; por tanto $y-4=4(x-2)$.

> [!note] 📋 Definición — Recta normal
>
> La **recta normal** es perpendicular a la tangente en el punto de contacto. Si $f'(a)\ne0$, su pendiente es $-1/f'(a)$ y
> $$y-f(a)=-\frac1{f'(a)}(x-a).$$
> Si $f'(a)=0$, la normal es vertical $x=a$; si la tangente es vertical, la normal es horizontal $y=f(a)$.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límite_de_la_Razón_de_Cambio_05.svg]]
>
> **Se lee así:** desde la tangente sale una rama perpendicular. El diagrama identifica el caso general y el recíproco de las rectas horizontal y vertical.
>
> **Por qué importa:** las pendientes de rectas perpendiculares tienen producto $-1$, lo que conecta geometría y derivabilidad.
>
> **Ejemplo:** si la tangente en $a$ tiene pendiente $2$, la normal tiene pendiente $-1/2$ y pasa por $(a,f(a))$.

---

## 📐 Interpretación Geométrica y Física

> [!info] 📐 De la secante a la tangente
>
> Para $P=(a,f(a))$ y $Q=(a+h,f(a+h))$, la pendiente de la secante $PQ$ es
> $$m_{\mathrm{sec}}=\frac{f(a+h)-f(a)}{h}.$$
> Cuando $h\to0$, $Q\to P$ y
> $$m_{\mathrm{tan}}=\lim_{h\to0}m_{\mathrm{sec}}=f'(a).$$
>
> | Valor de $h$ | Interpretación | Recta |
> |---|---|---|
> | $h\ne0$ | Razón promedio | Secante |
> | $h\to0^+$ | Límite derecho | Tangente derecha |
> | $h\to0^-$ | Límite izquierdo | Tangente izquierda |
> | $h=0$ formal | Razón instantánea | Tangente |
>
> **Por qué importa:** la derivada es la “mejor aproximación lineal” de la función cerca del punto. La tangente no es una aproximación arbitraria: es el límite geométrico de las secantes.
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límite_de_la_Razón_de_Cambio_01.svg]]
>
> **Se lee así:** el diagrama recorre la secuencia completa —puntos $P$ y $Q$ sobre la curva, recta secante $PQ$, acercamiento de $Q$ a $P$ y conversión de la secante en tangente— y termina en $f'(a)$ como pendiente. En paralelo, la rama inferior salta de la razón de cambio promedio a la instantánea.
>
> **Por qué importa:** el diagrama hace visible que la tangente no aparece de la nada: es el estado final de un proceso de acercamiento. Si la secante no tiene un único límite, no hay derivada.
>
> **Ejemplo:** para $f(x)=x^2$ en $a=3$, la secante tiene pendiente $6+h$; cuando $h\to0$ queda la tangente de pendiente $6$.

> [!tip] 🔍 Formas indeterminadas en el cociente
>
> Al sustituir $h=0$ suele aparecer $0/0$. Para resolverlo:
>
> 1. Factorizar y cancelar el factor común.
> 2. Racionalizar cuando aparece una raíz.
> 3. Usar identidades trigonométricas.
> 4. Usar L’Hôpital solo como verificación o herramienta posterior, no como sustituto de la definición.
>
> **Ejemplo:**
> $$f'(3)=\lim_{h\to0}\frac{(3+h)^2-9}{h}=\lim_{h\to0}\frac{6h+h^2}{h}=\lim_{h\to0}(6+h)=6.$$
>
> **Mnemotecnia:** **C**ambio **D**ividido **T**iende = **CDT**; **L**ímite **D**el **C**ociente **D**iferencial = **LDCD**.

> [!warning] ❌ Casos donde no existe la derivada
>
> 1. **Esquinas:** $f(x)=|x|$ en $0$ tiene $f'_-(0)=-1$ y $f'_+(0)=1$.
> 2. **Cúspides:** $f(x)=x^{2/3}$ en $0$ tiene cociente tendente a infinito y tangente vertical.
> 3. **Discontinuidades:** derivabilidad implica continuidad, pero no al revés.
> 4. **Tangentes verticales:** $f'(a)=\pm\infty$ no es una derivada finita.
>
> **Por qué importa:** cada caso falla por una razón distinta; por eso conviene calcular los límites laterales antes de concluir.

> [!info] 📊 Razones de cambio por contexto
>
> | Campo | Dependiente | Independiente | Razón |
> |---|---|---|---|
> | Física | Posición $s(t)$ | Tiempo $t$ | Velocidad $v=s'(t)$ |
> | Física | Velocidad $v(t)$ | Tiempo $t$ | Aceleración $a=v'(t)$ |
> | Química | Concentración $C(t)$ | Tiempo $t$ | Velocidad de reacción |
> | Economía | Costo $C(x)$ | Producción $x$ | Costo marginal |
> | Biología | Población $P(t)$ | Tiempo $t$ | Tasa de crecimiento |
> | Medicina | Dosis $D(m)$ | Masa corporal $m$ | Sensibilidad |
>
> **Mnemotecnia:** **F**ísica, **Q**uímica, **E**conomía, **B**iología, **M**edicina = **FQEBM**.

> [!warning] 📈 Interpretación del signo
>
> - $f'(a)>0$: la función está creciendo y la tangente sube; por ejemplo, velocidad positiva.
> - $f'(a)<0$: la función está decreciendo y la tangente baja; por ejemplo, velocidad negativa.
> - $f'(a)=0$: tangente horizontal; puede indicar máximo, mínimo o inflexión y también un instante de reposo.
>
> **Ejemplo:** si $h(t)$ es la altura de una pelota, $h'(t)>0$ significa que sube, $h'(t)<0$ que baja y $h'(t)=0$ que está momentáneamente en el punto más alto.

---

## 🛠️ Construcción y Aplicaciones

> [!tip] 📏 Algoritmo de la recta tangente
>
> 1. Identificar el punto $(a,f(a))$.
> 2. Calcular $f'(x)$.
> 3. Evaluar $m=f'(a)$.
> 4. Aplicar $y-f(a)=f'(a)(x-a)$.
> 5. Simplificar si se solicita.
>
> **Ejemplo:** para $f(x)=x^2$ y $a=2$, el punto es $(2,4)$, $f'(2)=4$ y
> $$y-4=4(x-2)\iff y=4x-4.$$
>
> **Por qué importa:** separar punto y pendiente evita errores frecuentes al cambiar la abscisa.

> [!success] 🎨 Aplicaciones geométricas
>
> 1. **Aproximación lineal:** $f(x)\approx f(a)+f'(a)(x-a)$ cerca de $a$.
> 2. **Análisis de errores:** si $x=a+\Delta x$, entonces $\Delta f\approx f'(a)\Delta x$.
> 3. **Optimización visual:** la tangente horizontal señala candidatos a máximo o mínimo; el cambio de concavidad ayuda a localizar inflexiones.
> 4. **Diseño e ingeniería:** pendientes de rampas, trayectorias y formas aerodinámicas.
>
> **Ejemplo:** para estimar $\sqrt{4.04}$, se toma $a=4$ y $f'(4)=1/4$; así $\sqrt{4.04}\approx2+\frac{1}{4}(0.04)=2.01$.

> [!info] 🖼️ De la razón promedio a la instantánea
>
> ![[../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Límite_de_la_Razón_de_Cambio_02.svg]]
>
> **Se lee así:** desde $f(t)$ se mide el cambio total $\Delta f$ en un intervalo; el cociente produce la razón promedio y el límite $\Delta t\to0$ produce la razón instantánea. De ella salen la fórmula de la derivada, la pendiente tangencial y las unidades físicas, además de la rama de aplicaciones.
>
> **Por qué importa:** enlaza una operación medible con la geometría. La misma idea produce velocidad, aceleración o costo marginal.
>
> **Ejemplo:** si $s(t)$ se mide en metros y $t$ en segundos, $s'(t)$ queda en metros por segundo.

> [!tip] 📚 Método DELTA
>
> - **D**efinición: aplicar el límite del cociente incremental.
> - **E**valuación: calcular el límite paso a paso.
> - **L**inealización: escribir la aproximación lineal.
> - **T**angente: construir e interpretar la recta.
> - **A**plicación: relacionar con el contexto físico o real.
>
> **Mnemotecnia física:** **V**elocidad, **A**celeración, **C**recimiento, **M**arginal = **VACM**.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Calcula $f'(3)$ desde la definición para $f(x)=x^2$.
>
> > [!success]- ✅ Solución
> >
> > $$f'(3)=\lim_{h\to0}\frac{(3+h)^2-3^2}{h}=\lim_{h\to0}\frac{9+6h+h^2-9}{h}.$$
> > Para $h\ne0$,
> > $$\frac{6h+h^2}{h}=6+h,$$
> > y por tanto $f'(3)=\lim_{h\to0}(6+h)=6$.

> [!example] 📋 Planteamiento
>
> Para $f(x)=x+2/x$, calcula $f'(a)$ usando la definición y construye la recta tangente en $a=1$.
>
> > [!success]- ✅ Solución
> >
> > $$f'(1)=\lim_{h\to0}\frac{1+h+2/(1+h)-3}{h}.$$
> > Como
> > $$1+h+\frac2{1+h}-3=\frac{(1+h)^2-2(1+h)}{1+h}=\frac{h^2-h}{1+h},$$
> > el cociente para $h\ne0$ es $\frac{h-1}{1+h}$, cuyo límite es $-1$. El punto de tangencia es $(1,3)$, por lo que
> > $$y-3=-(x-1)\iff y=-x+4.$$

> [!example] 📋 Planteamiento
>
> La posición de una partícula es $s(t)=t^3-6t^2+9t$ metros. Calcula su velocidad y aceleración instantáneas en $t=2$.
>
> > [!success]- ✅ Solución
> >
> > $v(t)=s'(t)=3t^2-12t+9$, por tanto $v(2)=12-24+9=-3\ \mathrm{m/s}$. La aceleración es $a(t)=s''(t)=6t-12$, así $a(2)=0\ \mathrm{m/s^2}$. El signo negativo de $v$ indica que la partícula se mueve en dirección negativa al instante $t=2$.

> [!example] 📋 Planteamiento
>
> Determina por qué $f(x)=|x|$ no es derivable en $0$ y calcula sus rectas tangentes laterales.
>
> > [!success]- ✅ Solución
> >
> > Para $h>0$, el cociente es $h/h=1$; para $h<0$, es $(-h)/h=-1$. Los límites laterales son distintos, por lo que la derivada no existe. La rama derecha tiene tangente $y=x$ y la izquierda $y=-x$ en el origen.

> [!example] 📋 Planteamiento
>
> Usa la aproximación lineal para estimar $\sqrt{4.04}$.
>
> > [!success]- ✅ Solución
> >
> > Se toma $f(x)=\sqrt x$ y $a=4$. Entonces $f(4)=2$ y $f'(x)=1/(2\sqrt x)$, así $f'(4)=1/4$. Por tanto
> > $$\sqrt{4.04}\approx2+\frac14(4.04-4)=2+\frac{0.04}{4}=2.01.$$
> > La aproximación es especialmente precisa porque $0.04$ es pequeño y $f$ cambia poco alrededor de $4$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo la derivada como límite del cociente incremental.
> - [ ] Interpreto $f'(a)$ como pendiente y razón instantánea.
> - [ ] Calculo una derivada sencilla desde la definición.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Construyo rectas tangente y normal.
> - [ ] Interpreto el signo y las unidades de una razón de cambio.
> - [ ] Distingo casos de no derivabilidad por sus límites laterales.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> - J. Stewart, *Cálculo*, definición de derivada y razones de cambio.
> - G. B. Thomas, *Cálculo*, derivadas y aproximaciones lineales.
> - Material de cátedra de MATG1045.
> - EXA-2023-0S-CÁLCULO DE UNA VARIABLE-1-Mejora.pdf, p. 2: problemas de razones de cambio; enlace de estudio, sin incrustación.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u3

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Definición de derivada?::$f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h$, si existe y es finito.
> - ¿Interpretación geométrica?::Pendiente de la tangente en $a$.
> - ¿Interpretación física?::Razón de cambio instantánea con unidades de $y$ por unidad de $x$.
> - ¿Ecuación de la tangente?::$y-f(a)=f'(a)(x-a)$.
> - ¿Normal si la pendiente es $m$?::Pendiente $-1/m$ cuando $m\ne0$.
> - ¿Aproximación lineal?::$f(x)\approx f(a)+f'(a)(x-a)$.
> - ¿Derivabilidad implica?::Continuidad, pero continuidad no implica derivabilidad.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[01 - Continuidad y Límites]] — la derivabilidad implica continuidad.
> - [[../Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|Derivabilidad y Continuidad]] — reglas y teoremas posteriores.
> - [[../Unidad 4 - Derivadas/IV - Técnicas Avanzadas/01 - Derivadas de Orden Superior|Derivadas de Orden Superior]] — derivadas de orden superior.
> - [[../Unidad 6 - Integrales/II - Integrales Indefinidas/03 - Constante de integración|Constante de integración]] — antiderivativas y movimiento.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Continúa con [[../Unidad 4 - Derivadas/I - Fundamentos Teóricos/03 - Derivabilidad y Continuidad|Derivabilidad y Continuidad]].
> - Practica primero cocientes con factorización antes de usar reglas.
> - En cada problema, escribe unidades y da una interpretación al signo.
> - Usa [[../Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/03 - Aproximaciones Lineales y Diferenciales|Aproximaciones Lineales y Diferenciales]] para conectar la tangente con error y aproximación.

---

**Tags:** #MATG1045 #unidad3 #razon-de-cambio #derivada #limites #tangente #aproximacion-lineal #fisica-matematica
