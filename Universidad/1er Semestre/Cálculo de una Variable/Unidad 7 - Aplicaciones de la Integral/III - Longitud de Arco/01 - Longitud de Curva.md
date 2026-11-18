---
dg-publish: true
tags: [MATG1045, unidad7, longitud-de-curva, integrales, aplicaciones, longitud-de-arco, curvas, geometria]
---

# 📐 Longitud de Curva

## 🎯 Introducción

> [!info] 💡 Qué es y por qué importa
>
> La **longitud de curva** (o de arco) mide la distancia a lo largo de la propia curva, no en línea recta. Se calcula como la integral del elemento diferencial de arco $ds$, que suma infinitos segmentos infinitesimales de la curva.
>
> **Por qué importa:** la misma longitud sirve para cables, carreteras, costas en mapas, trayectorias de partículas y elipses que no admiten forma cerrada. Y funciona en cualquier representación de la curva: cartesiana, paramétrica, polar o vectorial en 3D.
>
> **Ejemplo:** el semicírculo $x^2 + y^2 = R^2$ con $y \geq 0$ mide $\pi R$, exactamente la mitad de la circunferencia $2\pi R$.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — la longitud de arco, el elemento $ds$ y las cuatro representaciones.
> - **Procedimiento Paso a Paso** — derivar $ds$ en cada representación y resolver la integral.
> - **Ejemplos Resueltos** — semicírculo, parábola y espiral, los tres casos canónicos.
> - **Curvas Especiales** — recta, cardioide, cicloide, catenaria y la elección del sistema.
> - **Ejercicios Propuestos** — seis plantillas, una por cada variante.
>
> **Por qué importa:** las cuatro fórmulas son la misma idea de $ds = \sqrt{(dx)^2 + (dy)^2}$ en distintos lenguajes; el mapa empieza por la definición y termina eligiendo la representación.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Longitud de arco y elemento diferencial
>
> La **longitud de arco** de una curva entre dos puntos es:
>
> - **Paramétrica** $\mathbf{r}(t) = (x(t), y(t))$, $t \in [a,b]$:
> $$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt = \int_a^b \|\mathbf{r}'(t)\|\,dt$$
> - **Elemento diferencial de arco:** $ds = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2}\,dt = \|\mathbf{r}'(t)\|\,dt$
> - **Curva rectificable:** la curva es rectificable si la integral converge (longitud finita).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Longitud_de_Curva_01.svg]]
>
> **Se lee así:** una caja inicial se abre en **cuatro ramas paralelas**, una por cada forma de escribir una curva: paramétrica, cartesiana, polar y vectorial en 3D. De cada rama cuelga una caja con la integral de longitud correspondiente. Aparte, una caja de ejemplos se enlaza con un resumen de casos concretos, para tener de referencia longitudes ya conocidas.
>
> **Por qué importa:** la misma curva puede enunciarse de cuatro maneras y cada una da una **fórmula de longitud distinta**. Elegir bien la representación es lo que separa un cálculo directo de una integral imposible.
>
> **Ejemplo:** para el arco superior del círculo $x^2 + y^2 = R^2$, la parametrización $x = R\cos t$, $y = R\sin t$ da $L = \int_0^{\pi} R\,dt = \pi R$.

> [!tip] 🔬 Fórmulas según la representación
>
> 1. **Paramétrica:** para $\mathbf{r}(t) = (x(t), y(t))$, $t \in [a,b]$:
> $$L = \int_a^b \sqrt{[x'(t)]^2 + [y'(t)]^2}\,dt$$
> 2. **Cartesiana:** para $y = f(x)$, $x \in [a,b]$:
> $$L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$$
> 3. **Polar:** para $r = f(\theta)$, $\theta \in [\alpha, \beta]$:
> $$L = \int_\alpha^\beta \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2}\,d\theta$$
> 4. **Vectorial 3D:** para $\mathbf{r}(t) = (x(t), y(t), z(t))$, $t \in [a,b]$:
> $$L = \int_a^b \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2 + \left(\frac{dz}{dt}\right)^2}\,dt = \int_a^b \|\mathbf{r}'(t)\|\,dt$$
>
> **Por qué importa:** las cuatro comparten la raíz cuadrada de la suma de cuadrados de derivadas; si la polar te sale con $r$ y $(dr/d\theta)^2$, no olvidaste nada: es la MISMA fórmula escrita con $x = r\cos\theta$, $y = r\sin\theta$.

> [!warning] ⚠️ Condiciones de validez
>
> - La función debe ser **continua** en el intervalo.
> - La derivada debe **existir** y ser **continua** (curva suave).
> - En polares, **$r$ y $dr/d\theta$ ambas**, continuo en $[\alpha, \beta]$ (o la integral se parte).
> - En paramétricas, la parametrización regular: $\mathbf{r}'(t) \neq \mathbf{0}$.
>
> **Por qué importa:** las discontinuidades de $f'(x)$ hacen diverger la integral: dividir el intervalo en los puntos de salto es obligatorio, nunca opcional.

---

## 🔧 Procedimiento Paso a Paso

> [!tip] 🔎 De $ds$ a la integral, en cuatro pasos
>
> 1. **Bosquejar** la curva: saber si el intervalo es el que pide el enunciado.
> 2. **Calcular las derivadas** de la parametrización elegida ($f'(x)$, $x'(t)$, $y'(t)$, $r'(\theta)$).
> 3. **Formar $ds$:** raíces cuadradas de suma de cuadrados; simplificar antes de integrar.
> 4. **Integrar** y verificar con un caso conocido (círculo $2\pi r$, semicírculo $\pi r$, recta $\sqrt{1+m^2}\,a$).
>
> **Por qué importa:** el paso 1 y 4 son los que se saltan y los que evitan los errores más caros: límites incorrectos y resultados que no cuadran con el sentido común geométrico.

> [!tip] 📊 Elección entre cartesiana, paramétrica y polar
>
> | Forma de la curva | Método recomendado | Cuándo usar |
> |---|---|---|
> | $y = x^n$ (polinomios) | $\int \sqrt{1 + [f'(x)]^2}\,dx$ | derivada simple |
> | $x = y^n$ | $\int \sqrt{1 + [g'(y)]^2}\,dy$ | más natural en $y$ |
> | Círculos, elipses | Paramétrica o polar | evita raíces complejas |
> | $r = f(\theta)$ | Polar | simetría radial |
> | Curvas complicadas | Paramétrica | máxima flexibilidad |
> | $y = \sqrt{\,\ldots\,}$ | A menudo paramétrica | evita derivadas complejas |
>
> **Por qué importa:** la tabla dice qué fórmula evita las integrales elípticas; elegir bien es la mitad del trabajo.

---

## 🧮 Ejemplos Resueltos

> [!example] 🔢 Ejemplo 1 — Semicírculo: $x^2 + y^2 = R^2$, $y \geq 0$
>
> **Parametrización:** $x = R\cos t$, $y = R\sin t$, $t \in [0, \pi]$.
>
> **Derivadas:** $x' = -R\sin t$, $y' = R\cos t$.
>
> **Cálculo:**
> $$ds = \sqrt{R^2\sin^2 t + R^2\cos^2 t}\,dt = R\,dt \quad\Rightarrow\quad L = \int_0^{\pi} R\,dt = \pi R$$
>
> **Por qué importa:** el caso canónico: la parametrización del círculo convierte la integral imposible en $\int_0^{\pi} R\,dt$.

> [!example] 🔢 Ejemplo 2 — Parábola: $y = x^2$ de $x = 0$ a $x = 1$
>
> **Derivada:** $f'(x) = 2x$.
>
> **Integral:** $L = \int_0^1 \sqrt{1 + 4x^2}\,dx$ — sustitución trigonométrica $2x = \tan\theta$:
> $$L = \frac{1}{2}\int_0^{\arctan 2} \sec^3\theta\,d\theta = \frac{1}{4}\left[\sec\theta\tan\theta + \ln|\sec\theta + \tan\theta|\right]_0^{\arctan 2}$$
> $$= \frac{1}{4}\left[2\sqrt{5} + \ln(2 + \sqrt{5})\right] = \frac{\sqrt{5}}{2} + \frac{1}{4}\ln(2 + \sqrt{5}) \approx 1.4789$$
>
> **Por qué importa:** la parábola es la puerta a las sustituciones trig: $\sqrt{1 + 4x^2}$ es el patrón $\sqrt{1 + u^2}$.

> [!example] 🔢 Ejemplo 3 — Espiral de Arquímedes: $r = a\theta$ de $\theta = 0$ a $\theta = 2\pi$
>
> **Derivada:** $\frac{dr}{d\theta} = a$.
>
> **Cálculo:**
> $$L = \int_0^{2\pi} \sqrt{(a\theta)^2 + a^2}\,d\theta = a\int_0^{2\pi} \sqrt{\theta^2 + 1}\,d\theta$$
> $$= a\left[\frac{\theta}{2}\sqrt{\theta^2 + 1} + \frac{1}{2}\ln\left|\theta + \sqrt{\theta^2 + 1}\right|\right]_0^{2\pi}$$
> $$= \frac{a}{2}\left[2\pi\sqrt{4\pi^2 + 1} + \ln\left(2\pi + \sqrt{4\pi^2 + 1}\right)\right] \approx 21.26\,a$$
>
> **Por qué importa:** el patrón $\sqrt{\theta^2 + 1}$ vuelve trig con $\theta = \tan\phi$; la espiral es también la verificación numérica de cualquier software.

---

## 🌟 Curvas Especiales e Integrables

> [!tip] 📋 Casos especiales que integran exacto
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Longitud_de_Curva_02.svg]]
>
> **Se lee así:** una sola caja en la parte superior se abre en **cinco ramas paralelas**, cada una una curva distinta con su longitud y su nivel de dificultad. La primera es elemental y la segunda se resuelve con la circunferencia, mientras que las tres últimas exigen un cálculo más cuidadoso.
>
> **Por qué importa:** conocer estas longitudes exactas te da un **banco de pruebas** para verificar cualquier integral de arco: si tu resultado para un círculo o un semicírculo no coincide con $2\pi r$ o $\pi r$, algo salió mal.
>
> **Ejemplo:** la cardioide $r = a(1 + \cos\theta)$ de la nota tiene longitud $8a$, mientras que la elipse $\frac{x^2}{a^2} + \frac{y^2}{b^2} = 1$ exige una integral elíptica sin forma cerrada.

> [!example] 🔢 Ejemplo 4 — Recta $y = mx + c$ de $0$ a $a$ (verificación geométrica)
>
> **Derivada:** $f'(x) = m$:
> $$L = \int_0^a \sqrt{1 + m^2}\,dx = a\sqrt{1 + m^2}$$
> **Verificación:** la distancia entre $(0, c)$ y $(a, ma + c)$ es $\sqrt{a^2 + (ma)^2} = a\sqrt{1 + m^2}$ ✓
>
> **Por qué importa:** el ejemplo más simple demuestra que la fórmula recupera Pitágoras.

> [!example] 🔢 Ejemplo 5 — Radical $y = \frac{2}{3}x^{3/2}$ de $x = 0$ a $x = 1$
>
> **Derivada:** $f'(x) = \sqrt{x}$:
> $$L = \int_0^1 \sqrt{1 + x}\,dx = \left[\frac{2(1+x)^{3/2}}{3}\right]_0^1 = \frac{2}{3}(2\sqrt{2} - 1) = \frac{4\sqrt{2} - 2}{3}$$
>
> **Por qué importa:** cuando $1 + f'(x)^2$ es un cuadrado perfecto (como $1 + x$), la integral se resuelve sin trig.

> [!example] 🔢 Ejemplo 6 — $x = \frac{y^3}{3} + \frac{1}{4y}$ en $y \in [1, 3]$
>
> **Derivada:** $\frac{dx}{dy} = y^2 - \frac{1}{4y^2}$:
> $$1 + \left(y^2 - \frac{1}{4y^2}\right)^2 = y^4 + \frac{1}{2} + \frac{1}{16y^4} = \left(y^2 + \frac{1}{4y^2}\right)^2$$
> $$L = \int_1^3 \left(y^2 + \frac{1}{4y^2}\right)dy = \left[\frac{y^3}{3} - \frac{1}{4y}\right]_1^3 = \left(9 - \frac{1}{12}\right) - \left(\frac{1}{3} - \frac{1}{4}\right) = \frac{53}{6}$$
>
> **Por qué importa:** los casos con $dy$ piden el mismo $ds$ con $dx/dy$ en vez de $dy/dx$; el cuadrado perfecto aquí evita la trig.

> [!example] 🔢 Ejemplo 7 — Cardioide $r = a(1 + \cos\theta)$
>
> **Derivada:** $\frac{dr}{d\theta} = -a\sin\theta$:
> $$r^2 + \left(\frac{dr}{d\theta}\right)^2 = a^2\left[(1 + \cos\theta)^2 + \sin^2\theta\right] = 2a^2(1 + \cos\theta) = 4a^2\cos^2\left(\frac{\theta}{2}\right)$$
> $$L = 2a\int_0^{2\pi} \left|\cos\frac{\theta}{2}\right|d\theta = 8a$$
>
> **Por qué importa:** el absoluto de $\cos(\theta/2)$ obliga a partir en $[0, \pi]$ y $[\pi, 2\pi]$; la cicloide va por el mismo camino con $\sin(t/2)$ y da $8a$.

> [!example] 🔢 Ejemplo 8 — Cicloide $x = a(t - \sin t)$, $y = a(1 - \cos t)$
>
> **Derivadas:** $x' = a(1 - \cos t)$, $y' = a\sin t$:
> $$(x')^2 + (y')^2 = 2a^2(1 - \cos t) = 4a^2\sin^2(t/2)$$
> $$L = 2a\int_0^{2\pi} \left|\sin\frac{t}{2}\right|dt = 8a$$
>
> **Por qué importa:** cicloide y cardioide comparten el truco de medio ángulo; memorizar ambas da $8a$ en los dos casos.

> [!example] 🔢 Ejemplo 9 — Catenaria $y = a\cosh\left(\frac{x}{a}\right)$ en $[-b, b]$
>
> **Derivada:** $y' = \sinh\left(\frac{x}{a}\right)$; como $\cosh^2 - \sinh^2 = 1$:
> $$L = \int_{-b}^{b} \sqrt{1 + \sinh^2\left(\frac{x}{a}\right)}\,dx = \int_{-b}^{b} \cosh\left(\frac{x}{a}\right)dx = 2a\sinh\left(\frac{b}{a}\right)$$
>
> **Por qué importa:** la catenaria es el único cable colgante realmente exacto; da la verificación de cualquier modelo de cable.

---

## 🔄 Elección del Sistema y Métodos

> [!tip] 🤔 ¿Qué sistema usar?
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Longitud_de_Curva_03.svg]]
>
> **Se lee así:** un mapa de decisión con un rombo inicial de cuatro salidas, según cómo venga escrita la curva. La rama cartesiana y la rama en $y$ tienen un segundo rombo que pregunta *si la derivada es simple*, y según eso van a la fórmula directa o a la casilla de reconsiderar la representación. Las ramas polar y paramétrica no tienen decisión intermedia: van directo a su fórmula de longitud.
>
> **Por qué importa:** elegir mal la representación te mete en **integrales elípticas** o en radicales imposibles. Con este mapa decides primero el sistema y luego la fórmula, en lugar de aplicar la de siempre y arrepentirte después.
>
> **Ejemplo:** para el arco de cicloide $x = a(t - \sin t)$, $y = a(1 - \cos t)$ con $t$ de $0$ a $2\pi$, la parametrización da $L = 8a$, como indica la nota.

> [!info] 🧮 Técnicas de integración habituales
>
> - **Sustitución trig:** $\sqrt{a^2 + x^2}$ con $x = a\tan\theta$; $\sqrt{a^2 - x^2}$ con $x = a\sin\theta$; $\sqrt{x^2 - a^2}$ con $x = a\sec\theta$.
> - **Sustitución algebraica:** simplificar radicales complejos antes de integrar.
> - **Integración por partes:** productos de funciones algebraicas y trascendentes.
> - **Métodos numéricos:** trapecio o Simpson cuando no hay forma cerrada.
>
> **Por qué importa:** la mayoría de las integrales de arco no son elementales; saber cuándo parar y usar Simpson es más útil que memorizar sustituciones.

---

## 🌍 Aplicaciones

> [!info] 🌍 Física e ingeniería
>
> - **Mecánica:** longitud de trayectoria y trabajo $W = \int_C \mathbf{F} \cdot d\mathbf{r}$.
> - **Óptica:** principio de Fermat (el camino de menor tiempo) y diseño de lentes.
> - **Ingeniería:** carreteras (curvas de transición), cables colgantes (catenarias).
> - **Cartografía:** estimación de distancias en mapas con curvas irregulares.

> [!tip] 📐 Geometría
>
> - **Perímetros y contornos** de figuras con bordes curvos.
> - **Geometría diferencial:** curvatura $\kappa = \frac{\|\mathbf{r}' \times \mathbf{r}''\|}{\|\mathbf{r}'\|^3}$ y parametrización por longitud de arco.
> - **Elemento de arco como parámetro:** toda curva regular puede reparametrizarse con $s$.
>
> **Por qué importa:** el elemento de arco $ds$ es EL parámetro geométrico: en él, la rapidez es 1 y la curvatura tiene fórmula directa.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Halla la longitud de $y = x^{3/2}$ de $x = 0$ a $x = 1$.
>
> > [!success]- ✅ Solución
> > $f'(x) = \frac{3}{2}x^{1/2}$; $L = \int_0^1 \sqrt{1 + \frac{9}{4}x}\,dx = \left[\frac{8}{27}\left(1 + \frac{9}{4}x\right)^{3/2}\right]_0^1 = \frac{13\sqrt{13} - 8}{27}$.
> > **Lección:** cuando $1 + f'^2$ es lineal, la sustitución $u = 1 + \frac{9}{4}x$ lo resuelve todo ✓

> [!example] 📋 Planteamiento
>
> Halla la longitud de $x = y^2$ de $y = 0$ a $y = 1$.
>
> > [!success]- ✅ Solución
> > $\frac{dx}{dy} = 2y$; $L = \int_0^1 \sqrt{1 + 4y^2}\,dy = \frac{\sqrt{5}}{2} + \frac{1}{4}\ln(2 + \sqrt{5}) \approx 1.4789$.
> > **Lección:** la misma integral que la parábola ejemplo 2, tras renombrar $y$ como $x$ ✓

> [!example] 📋 Planteamiento
>
> Verifica que la cardioide $r = a(1 + \cos\theta)$ tiene longitud $8a$ usando la forma polar.
>
> > [!success]- ✅ Solución
> > $\sqrt{r^2 + r'^2} = 2a\left|\cos\frac{\theta}{2}\right|$; $L = 2a\int_0^{2\pi} \left|\cos\frac{\theta}{2}\right|d\theta = 2a \cdot 4 = 8a$.
> > **Lección:** mismo resultado por polar y paramétrica: la representación no altera el área (ni el arco) ✓

> [!example] 📋 Planteamiento
>
> Halla la longitud de la catenaria $y = 2\cosh\left(\frac{x}{2}\right)$ de $x = 0$ a $x = 2$.
>
> > [!success]- ✅ Solución
> > $y' = \sinh\left(\frac{x}{2}\right)$; $L = \int_0^2 \sqrt{1 + \sinh^2\left(\frac{x}{2}\right)}\,dx = \int_0^2 \cosh\left(\frac{x}{2}\right)dx = [2\sinh(x/2)]_0^2 = 2\sinh(1) \approx 2.3504$.
> > **Lección:** la identidad $\cosh^2 - \sinh^2 = 1$ convierte el radical en $\cosh$ directo ✓

> [!example] 📋 Planteamiento
>
> Halla la longitud de la espiral logarítmica $r = e^{\theta}$ de $\theta = 0$ a $\theta = 2\pi$.
>
> > [!success]- ✅ Solución
> > $r' = e^{\theta}$; $L = \int_0^{2\pi} \sqrt{e^{2\theta} + e^{2\theta}}\,d\theta = \sqrt{2}\int_0^{2\pi} e^{\theta}\,d\theta = \sqrt{2}\left(e^{2\pi} - 1\right) \approx 753.76$.
> > **Lección:** la polar logarítmica siempre sale $\sqrt{2} \times$ (diferencia de radios extremos) ✓

> [!example] 📋 Planteamiento
>
> Halla la longitud del arco de cicloide $x = a(t - \sin t)$, $y = a(1 - \cos t)$ sólo hasta $t = \pi$.
>
> > [!success]- ✅ Solución
> > $L = 2a\int_0^{\pi} \left|\sin\frac{t}{2}\right|dt = 2a\left[-2\cos\frac{t}{2}\right]_0^{\pi} = 2a(2) = 4a$ (la mitad de la arcada completa).
> > **Lección:** simetría: la mitad del cicloide mide exactamente la mitad ($4a$ de $8a$) ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Escribo el elemento diferencial de arco $ds = \|\mathbf{r}'(t)\|\,dt$ y lo uso para cualquier representación.
> - [ ] Elijo la representación (cartesiana, paramétrica, polar, 3D) adecuada a la curva.
> - [ ] Reconozco las curvas "rectificables" y las condiciones que hacen diverger la integral.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Resuelvo integrales de arco con sustituciones trig $\sqrt{a^2 \pm x^2}$, $\sqrt{x^2 - a^2}$ y algebraicas.
> - [ ] Verifico resultados con casos conocidos (recta $a\sqrt{1+m^2}$, semicírculo $\pi R$, círculo $2\pi R$, cicloide $8a$).
> - [ ] Manejo curvas en las que $1 + f'(x)^2$ es un cuadrado perfecto sin trig.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Resuelvo cardioide y espirales de Arquímedes y logarítmicas con sus trucos de medio ángulo y de cuadrado $r^2$.
> - [ ] Uso el elemento de arco como parámetro (rapidez 1) y lo conecto con curvatura $\kappa$ y geometría diferencial.
> - [ ] Frente a integrales sin forma cerrada, decido entre simpson, trapecio o dejar el símbolo $\int$.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage): aplicaciones del integral definido — longitud de arco y la fórmula con $\sqrt{1 + f'(x)^2}$.
> - G. Strang, *Calculus* (Wellesley-Cambridge): el elemento de arco como parámetro geométrico.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — la aplicación base: área antes que longitud.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la suma de segmentos que subyace a $L$.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — evaluación de la integral de longitud.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — cuando la integral de arco puede diverger.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas|03 - Derivadas Paramétricas]] — derivadas $x'(t)$, $y'(t)$ que entran en $ds$.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/04 - Área en Coordenadas Polares y Paramétricas|04 - Área en Coordenadas Polares y Paramétricas]] — las mismas representaciones para área.
>
> **Conexiones interdisciplinarias:** mecánica (trayectorias), óptica (Fermat), ingeniería de carreteras y cables (catenarias), cartografía (curvas en mapas) y geometría diferencial (curvatura).

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u7

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la fórmula general de longitud de arco?::$L = \int_a^b \|\mathbf{r}'(t)\|\,dt = \int_a^b ds$, con $ds = \sqrt{x'(t)^2 + y'(t)^2}\,dt$.
> - ¿Cómo es la fórmula para $y = f(x)$?::$L = \int_a^b \sqrt{1 + [f'(x)]^2}\,dx$.
> - ¿Y para la forma polar $r = f(\theta)$?::$L = \int_\alpha^\beta \sqrt{r^2 + (dr/d\theta)^2}\,d\theta$.
> - ¿Qué significa que una curva sea rectificable?::Que la integral de $ds$ converge: la longitud resultante es finita.
> - ¿Cuánto mide una arcada de cicloide $x = a(t-\sin t)$?::$L = 8a$.
> - ¿Cuánto mide la cardioide $r = a(1 + \cos\theta)$?::$L = 8a$.
> - ¿Qué patrón trig resuelve $\sqrt{a^2 + x^2}$?::$x = a\tan\theta$, que sostiene $\sqrt{a^2 + x^2} = a\sec\theta$.
> - ¿Cómo verifico una curva cualquiera?::Con casos conocidos: recta $a\sqrt{1+m^2}$, semicírculo $\pi R$, círculo $2\pi R$, cicloide $8a$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el área como límite de sumas, la idea misma detrás de $ds$.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la suma de segmentos rectos que aproxima $L$.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — evaluación de la integral.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — cuando la integral puede diverger.
> - [[Unidad 4 - Derivadas/IV - Técnicas Avanzadas/03 - Derivadas Paramétricas|03 - Derivadas Paramétricas]] — derivadas $x'(t)$, $y'(t)$ de $ds$.
> - [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/01 - Volúmenes de Sólidos de Revolución|01 - Volúmenes de Sólidos de Revolución]] — girar la región para volumen (misma unidad).
>
> **Conexiones interdisciplinarias:** física (trayectorias, trabajo $W = \int_C \mathbf{F} \cdot d\mathbf{r}$), óptica (principio de Fermat), ingeniería (carreteras, cables colgantes) y cartografía (distancias en mapas).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 2: sustitución directa de $f'(x)$.
> - Después el 3 y el 6: cardioide y medio cicloide, los trucos de medio ángulo.
> - Cierra con 4 y 5: catenaria y espiral logarítmica, los casos exactos de la casa.
> - Cuando lo tengas, pasa a [[Unidad 7 - Aplicaciones de la Integral/II - Volúmenes/02 - Volúmenes con Ejes Arbitrarios y Casos Avanzados|02 - Volúmenes con Ejes Arbitrarios y Casos Avanzados]] y repasa el repertorio de integrales de la casa.

---

**Tags:** #MATG1045 #unidad7 #longitud-de-curva #integrales #aplicaciones #longitud-de-arco #curvas #geometria
