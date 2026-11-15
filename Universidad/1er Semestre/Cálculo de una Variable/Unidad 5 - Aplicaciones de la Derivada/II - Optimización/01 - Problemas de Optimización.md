---
dg-publish: true
tags: [MATG1045, unidad5, optimizacion, modelado, maximos-minimos, funcion-objetivo, restricciones, economia, geometria]
---

# 🎯 Problemas de Optimización

## 🎯 Introducción

> [!info] 💡 Qué busca un problema de optimización
>
> Los **problemas de optimización** buscan encontrar el valor **máximo** o **mínimo** de una función objetivo sujeta a ciertas restricciones o condiciones. Es el destino natural de las derivadas: donde la pendiente se anula, la función deja de subir o de bajar, y ahí vive el óptimo.
>
> **Por qué importa:** esta es la parte del cálculo que más se usa fuera del aula: dimensionar cajas, minimizar material, maximizar beneficios, diseñar rutas. El cálculo es siempre el mismo; lo que cambia es el contexto que hay que modelar.
>
> **Ejemplo:** con 200 m de cerca, el rectángulo de área máxima resulta ser un cuadrado de 50 × 50 m: el modelo $A(x) = x(100-x)$ lo revela en tres líneas.

> [!warning] ⚠️ Los cuatro lugares donde buscar el óptimo
>
> 1. **Puntos críticos interiores:** $f'(x) = 0$.
> 2. **Puntos de frontera:** extremos del dominio.
> 3. **Puntos de discontinuidad:** donde $f'(x)$ no existe.
> 4. **Puntos de esquina:** en problemas con restricciones angulares.
>
> **Por qué importa:** el error más caro es evaluar solo $f'(x) = 0$ y olvidar el dominio. En problemas de optimización los extremos del intervalo suelen ser candidatos serios, y a veces son la respuesta.
>
> **Ejemplo:** si la función beneficio $B(x) = 8x - 0.03x^2 - 100$ tiene su máximo en $x \approx 133{,}33$, pero la producción debe ser entera, hay que evaluar los vecinos $133$ y $134$: el óptimo está en la frontera de la realidad, no en el cero exacto.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Función objetivo y restricción
>
> En un problema de optimización:
>
> - **Función objetivo** $f(x)$: la magnitud que se quiere maximizar o minimizar (área, costo, tiempo, beneficio).
> - **Restricción:** la condición que limita las variables (presupuesto, material disponible, volumen fijo).
> - **Óptimo:** el valor de la función objetivo en el punto candidato que la hace mayor o menor.
>
> El procedimiento MODELO recoge el ciclo completo: **M**odelado (variables y función objetivo) → **O**rganizar (restricciones y dominio) → **D**erivar → **E**cuacionar ($f'(x) = 0$) → **L**ocalizar (puntos críticos) → **O**ptimizar (verificar máximo o mínimo).
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Problemas_de_Optimización_01.svg]]
>
> **Se lee así:** es un diagrama completamente lineal: un rectángulo inicial con el problema y una cadena de diez pasos encadenados, sin decisiones ni bifurcaciones. La secuencia va de leer y comprender hasta verificar y responder, pasando por identificar variables, construir la función objetivo, colocar las restricciones, expresar el problema en una sola variable, fijar el dominio, derivar, encontrar puntos críticos y evaluar los candidatos.
>
> **Por qué importa:** fíjate en que el diagrama pone el modelado **antes** que el cálculo: si no defines variables y función objetivo, derivar no sirve de nada. La etapa de evaluar candidatos y verificar evita el error de responder con un punto crítico sin comprobar que sea el óptimo.
>
> **Ejemplo:** para el rectángulo de área máxima con 200 m de cerca recorres la cadena completa: $A(x) = x(100 - x)$, dominio $0 < x < 100$, $A'(x) = 100 - 2x = 0$ y respuesta $50 \times 50$ m.

> [!note] 📋 Definición — Criterios de verificación
>
> Una vez encontrado un candidato $x = c$, hay tres formas de confirmarlo:
>
> - **Test de la primera derivada:** $f'$ cambia de $+$ a $-$ → máximo local; de $-$ a $+$ → mínimo local.
> - **Test de la segunda derivada:** $f''(c) < 0$ → máximo; $f''(c) > 0$ → mínimo; $f''(c) = 0$ → test **inconcluso**.
> - **Evaluación directa:** comparar $f(x)$ en todos los candidatos, incluidos los bordes del dominio.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Problemas_de_Optimización_04.svg]]
>
> **Se lee así:** el esquema parte del candidato $x = c$ y abre dos vías de verificación en paralelo. La primera es el test de la primera derivada, que con el cambio de signo de $f'$ clasifica máximo, mínimo o no extremo; la segunda es el test de la segunda derivada, que decide con el signo de $f''$ y, si $f''(c) = 0$, declara el test inconcluso y deriva a comparar $f$ en todos los candidatos, bordes incluidos.
>
> **Por qué importa:** el diagrama muestra que las dos vías son equivalentes y que la tercera ruta (evaluación directa) es la red de seguridad: siempre que un test falle, se recurre a comparar valores. Así nunca te quedas sin respuesta en un examen.
>
> **Ejemplo:** $f(x) = x^4$ tiene $f'(0) = 0$ y $f''(0) = 0$: la rama del test inconcluso te lleva a evaluar $f$ en vecinos de $0$ y confirmar que es el mínimo absoluto.

---

## 📐 Problemas geométricos

> [!example] 📦 Caso clásico: rectángulo de área máxima
>
> **Enunciado:** con 200 m de cerca, hallar las dimensiones del rectángulo de área máxima.
>
> - Variables: largo $x$, ancho $y$; restricción $2x + 2y = 200$, es decir $y = 100 - x$.
> - Función objetivo: $A(x) = x(100 - x) = 100x - x^2$; dominio $0 < x < 100$.
> - $A'(x) = 100 - 2x = 0$ → $x = 50$; $A''(x) = -2 < 0$ → máximo.
> - **Respuesta:** cuadrado de 50 × 50 m.
>
> **Por qué importa:** es el problema-tipo: la restricción reduce las dos variables a una, y la derivada decide. Todos los problemas geométricos siguen este mismo esqueleto.

> [!example] 📐 Caso caja: volumen máximo
>
> **Enunciado:** de una lámina cuadrada de 12 cm de lado, cortar cuadrados en las esquinas para formar una caja. ¿Qué tamaño deben tener los cuadrados?
>
> - Variable: lado del cuadrado cortado $x$; dimensiones de la caja $(12-2x) \times (12-2x) \times x$.
> - $V(x) = x(12-2x)^2 = 144x - 48x^2 + 4x^3$; dominio $0 < x < 6$.
> - $V'(x) = 144 - 96x + 12x^2 = 12(x-2)(x-6) = 0$ → $x = 2$ (descartamos $x = 6$: da volumen cero).
> - $V''(2) = 24(2) - 96 = -48 < 0$ → máximo.
> - **Respuesta:** cortar cuadrados de 2 × 2 cm.
>
> **Por qué importa:** fíjate en descartar $x = 6$ por estar en la frontera del dominio y dar volumen cero: el criterio de dominio ahorra concluir mal.

> [!tip] 📐 Fórmulas que suelen usarse
>
> - **Áreas:** rectángulo $A = b \cdot h$; triángulo $A = \frac{1}{2}bh$; círculo $A = \pi r^2$; sector $A = \frac{1}{2}r^2\theta$.
> - **Volúmenes:** prisma $V = b \cdot a \cdot h$; cilindro $V = \pi r^2 h$; cono $V = \frac{1}{3}\pi r^2 h$; esfera $V = \frac{4}{3}\pi r^3$; pirámide $V = \frac{1}{3}(\text{área base})h$.
> - **Superficies:** distingue **superficie total** de **superficie lateral** y considera costos por unidad de área distintos.
>
> **Por qué importa:** la mitad de los errores vienen de aplicar mal la fórmula (olvidar una tapa, confundir lateral con total) antes siquiera de derivar.

---

## 📏 Problemas de distancia y ruta

> [!example] 📏 Punto más cercano a una parábola
>
> **Enunciado:** hallar el punto de $y = x^2$ más cercano a $(0, 1)$.
>
> - Punto en la parábola: $P(t, t^2)$; distancia $d(t) = \sqrt{t^2 + (t^2-1)^2}$.
> - Para no trabajar con raíz, se minimiza el cuadrado: $d^2(t) = t^4 - t^2 + 1$.
> - Derivada: $\frac{d}{dt}(d^2) = 4t^3 - 2t = 2t(2t^2 - 1) = 0$ → $t = 0$ o $t = \pm\frac{\sqrt{2}}{2}$.
> - Evaluando: $d^2(0) = 1$ y $d^2(\pm\frac{\sqrt{2}}{2}) = \frac{3}{4}$.
> - **Respuesta:** los puntos $(\pm\frac{\sqrt{2}}{2}, \frac{1}{2})$ están más cerca.
>
> **Por qué importa:** minimizar $d^2$ en vez de $d$ es un truco legítimo (ambas funciones tienen los mismos óptimos porque la raíz es creciente) que ahorra derivadas difíciles.

> [!warning] 💡 Principio de Fermat y ley de Snell
>
> - **Reflexión:** la luz toma el camino que minimiza el tiempo total; resultado: ángulo de incidencia = ángulo de reflexión.
> - **Refracción (ley de Snell):** cuando la luz cambia de medio, el tiempo mínimo exige $n_1 \operatorname{sen}(\theta_1) = n_2 \operatorname{sen}(\theta_2)$, donde $n_1, n_2$ son los índices de refracción.
>
> **Por qué importa:** la naturaleza "optimiza" sin calcular derivadas; estos principios son la razón física detrás de las ecuaciones que resuelves.

> [!info] 🖼️ Clasificación de problemas de ruta
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Problemas_de_Optimización_02.svg]]
>
> **Se lee así:** el diagrama arranca con un rombo que clasifica el tipo de medio o de trayectoria, y de él salen cuatro ramas. La rama de un solo medio termina en distancia euclídea; la de dos medios pasa por la ley de Snell hasta minimizar el tiempo total; la de obstáculos lleva al principio de reflexión; la de múltiples puntos exige combinatoria junto con optimización. Cada rama se cierra en un recuadro con la herramienta concreta.
>
> **Por qué importa:** la clasificación evita que trates como geometría simple un problema de refracción o de rutas múltiples. Te muestra que la derivada cambia de rol según el contexto: distancia, tiempo o número de caminos.
>
> **Ejemplo:** el problema de refracción, con la luz más lenta en agua que en aire, cae en la rama de dos medios y se resuelve con $n_1 \operatorname{sen}(\theta_1) = n_2 \operatorname{sen}(\theta_2)$.

---

## 💰 Aplicaciones económicas

> [!success] 💰 Maximización de beneficios
>
> - **Ingreso:** $I(x) = p(x) \cdot x$ (precio × cantidad).
> - **Costo:** $C(x)$ = costos fijos + costos variables.
> - **Beneficio:** $B(x) = I(x) - C(x)$.
> - **Condición de óptimo:** ingreso marginal = costo marginal, es decir $B'(x) = 0$.
>
> **Ejemplo:** con $C(x) = 100 + 2x + 0.01x^2$ y precio $p = 10 - 0.02x$:
>
> $$I(x) = 10x - 0.02x^2, \qquad B(x) = 8x - 0.03x^2 - 100,$$
>
> $$B'(x) = 8 - 0.06x = 0 \Rightarrow x \approx 133{,}33, \qquad B''(x) = -0.06 < 0 \Rightarrow \text{máximo}.$$
>
> Como la producción es entera, se evalúan $x = 133$ y $x = 134$: **producir 133 unidades**.

> [!example] 📦 Modelo EOQ: minimización de costos de inventario
>
> **Variables:** $D$ = demanda anual; $K$ = costo por pedido; $h$ = costo de mantener una unidad en inventario por año.
>
> $$C(x) = \frac{D}{x}K + \frac{x}{2}h, \qquad x^* = \sqrt{\frac{2DK}{h}}.$$
>
> **Por qué importa:** el primer término baja al pedir menos veces (pero sube el inventario); el segundo sube con el tamaño del pedido. La derivada equilibra los dos costos exactamente en $x^* = \sqrt{2DK/h}$, la célebre fórmula del inventario óptimo.
>
> **Tipos de costos:** fijos (no dependen de la producción), variables (proporcionales), marginales (derivada del costo total) y de inventario (almacenamiento vs. pedidos frecuentes).

> [!info] 📈 Elasticidad precio-demanda
>
> $$E = \frac{dp/dx}{p/x}$$
>
> - $|E| > 1$: demanda **elástica** (la cantidad reacciona mucho al precio).
> - $|E| < 1$: demanda **inelástica** (reacciona poco).
> - $|E| = 1$: elasticidad **unitaria**; ahí el ingreso es máximo.
>
> **Por qué importa:** el punto de elasticidad unitaria es exactamente donde $I'(x) = 0$: otro caso en el que el óptimo aparece como cero de una derivada.
>
> **Fórmula de inversión:** el valor presente neto $VPN = \sum \frac{CF_t}{(1+r)^t} - \text{inversión inicial}$; su optimización consiste en elegir la tasa o el momento óptimo de inversión.

---

## 🎨 Estrategias de modelado

> [!tip] 🧭 Identificación de variables
>
> - **Variables de decisión:** las que puedes controlar (el largo, el precio).
> - **Variables de estado:** describen el sistema (la temperatura, el inventario).
> - **Variables auxiliares:** facilitan los cálculos (como el $y = 100 - x$).
> - **Parámetros:** valores fijos del problema (los 200 m de cerca).
>
> **Errores comunes:** confundir independientes con dependientes; no identificar todas las restricciones; usar más variables de las necesarias; no definir claramente el dominio.

> [!example] 🧠 Construcción de la función objetivo
>
> 1. **Directa:** la función se deriva inmediatamente del problema.
> 2. **Por partes:** combinar componentes distintos del sistema (tapas + lateral).
> 3. **Paramétrica:** usar parámetros que luego se optimizan.
> 4. **Por analogía:** reutilizar modelos similares ya conocidos.
>
> **Por qué importa:** la función objetivo es la traducción del enunciado al cálculo; si la traducción es mala, todo lo demás sale bien pero inútil.

> [!info] 🖼️ Manejo de restricciones
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Problemas_de_Optimización_03.svg]]
>
> **Se lee así:** el centro del diagrama es un rombo que pregunta por el tipo de restricción, y de él salen tres ramas paralelas. La de igualdad lleva a la sustitución directa y termina en una función de una variable resuelta con optimización clásica; la de desigualdad pasa por los multiplicadores de Lagrange y un sistema de ecuaciones; la de sin restricciones va directo a la derivada ordinaria. Los tres caminos terminan en un extremo verificado.
>
> **Por qué importa:** elegir bien la rama ahorra trabajo: si la restricción es una igualdad, la sustitución es más rápida; si son varias o de desigualdad, Lagrange es más sistemático. También recuerda que un problema sin restricción se resuelve solo con $f'(x) = 0$.
>
> **Ejemplo:** el tanque cilíndrico con volumen $1000$ m³ fijo usa la rama de igualdad: despejas $h = 1000/(\pi r^2)$ y derivas $S(r) = 2\pi r^2 + 2000/r$.

> [!warning] ✅ Validación del modelo
>
> 1. **Coherencia dimensional:** unidades correctas en toda la ecuación.
> 2. **Casos límite:** comportamiento en situaciones extremas.
> 3. **Sentido físico:** ¿el resultado es lógicamente razonable?
> 4. **Sensibilidad:** ¿cómo cambia la solución con los parámetros?
>
> **Por qué importa:** una optimización puede salir algebraicamente impecable y ser físicamente imposible (altura negativa, precio cero). La validación es el paso que separa un modelo útil de una cuenta bonita.

> [!tip] 🎓 Mnemotecnias: OPTIMIZA y SPEC
>
> - **OPTIMIZA:** **O**bjetivo (define qué optimizar) · **P**arámetros (variables y constantes) · **T**ipo (geométrico, económico…) · **I**dentifica (restricciones) · **M**odela (función objetivo) · **I**gualación ($f'(x) = 0$) · **Z**ona (dominio válido) · **A**naliza (verifica máximo o mínimo).
> - **SPEC (verificación):** **S**entido (¿tiene sentido la respuesta?) · **P**untos críticos (¿están todos?) · **E**xtremos (¿evaluaste los bordes del dominio?) · **C**riterio (¿usaste bien el test de 1ª o 2ª derivada?).

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Con 200 m de cerca, encuentra las dimensiones del rectángulo de área máxima.
>
> > [!success]- ✅ Solución
> >
> > Restricción: $2x + 2y = 200$ → $y = 100 - x$.
> >
> > Objetivo: $A(x) = x(100 - x) = 100x - x^2$, con $0 < x < 100$.
> >
> > $A'(x) = 100 - 2x = 0$ → $x = 50$; $A''(x) = -2 < 0$ → máximo.
> >
> > Con $x = 50$: $y = 50$. **Respuesta:** cuadrado de 50 × 50 m, área $2500$ m².

> [!example] 📋 Planteamiento
>
> De una lámina cuadrada de 12 cm, corta cuadrados en las esquinas para maximizar el volumen de la caja resultante.
>
> > [!success]- ✅ Solución
> >
> > $V(x) = x(12 - 2x)^2 = 144x - 48x^2 + 4x^3$, con $0 < x < 6$.
> >
> > $V'(x) = 144 - 96x + 12x^2 = 12(x-2)(x-6) = 0$ → candidatos $x = 2$ y $x = 6$.
> >
> > $x = 6$ está en la frontera y da $V = 0$ (mínimo trivial); $V''(2) = -48 < 0$ → máximo.
> >
> > **Respuesta:** cuadrados de 2 × 2 cm; la caja mide $8 \times 8 \times 2$ cm y su volumen es $128$ cm³.

> [!example] 📋 Planteamiento
>
> Halla el punto de $y = x^2$ más cercano a $(0, 1)$.
>
> > [!success]- ✅ Solución
> >
> > Se minimiza $d^2(t) = t^2 + (t^2 - 1)^2 = t^4 - t^2 + 1$ (la raíz es creciente, así que comparte óptimos con $d$).
> >
> > $(d^2)' = 4t^3 - 2t = 2t(2t^2 - 1) = 0$ → $t = 0$ o $t = \pm\frac{\sqrt{2}}{2}$.
> >
> > $d^2(0) = 1$ y $d^2(\pm\frac{\sqrt{2}}{2}) = \frac{3}{4} < 1$.
> >
> > **Respuesta:** los puntos $(\pm\frac{\sqrt{2}}{2}, \frac{1}{2})$; la distancia mínima es $\sqrt{3}/2 \approx 0{,}866$.

> [!example] 📋 Planteamiento
>
> Una empresa tiene costos $C(x) = 100 + 2x + 0.01x^2$ y vende a precio $p = 10 - 0.02x$. ¿Cuál es la producción óptima?
>
> > [!success]- ✅ Solución
> >
> > Ingreso: $I(x) = x(10 - 0.02x) = 10x - 0.02x^2$.
> >
> > Beneficio: $B(x) = I(x) - C(x) = 8x - 0.03x^2 - 100$.
> >
> > $B'(x) = 8 - 0.06x = 0$ → $x = 8/0{,}06 \approx 133{,}33$; $B''(x) = -0{,}06 < 0$ → máximo.
> >
> > Como la producción es entera, se comparan $B(133)$ y $B(134)$.
> >
> > **Respuesta:** producir 133 unidades.

> [!example] 📋 Planteamiento
>
> Diseña una lata cilíndrica de 355 ml que minimice el material usado.
>
> > [!success]- ✅ Solución
> >
> > Restricción: $\pi r^2 h = 355$ → $h = \frac{355}{\pi r^2}$.
> >
> > Objetivo (área de tapas + lateral): $A(r) = 2\pi r^2 + 2\pi r h = 2\pi r^2 + \frac{710}{r}$, con $r > 0$.
> >
> > $A'(r) = 4\pi r - \frac{710}{r^2} = 0$ → $4\pi r^3 = 710$ → $r = \sqrt[3]{\frac{710}{4\pi}} \approx 3{,}84$ cm.
> >
> > $A''(r) = 4\pi + \frac{1420}{r^3} > 0$ → mínimo.
> >
> > Altura: $h = \frac{355}{\pi (3{,}84)^2} \approx 7{,}67$ cm (justamente $h = 2r$: la lata óptima tiene su altura igual a su diámetro).
> >
> > **Respuesta:** $r \approx 3{,}84$ cm y $h \approx 7{,}67$ cm.

> [!example] 📋 Planteamiento
>
> Un monopolista tiene demanda $p = 100 - 2x$ y costos $C(x) = 20x + 1000$. Halla el precio y la cantidad que maximizan el beneficio.
>
> > [!success]- ✅ Solución
> >
> > Ingreso: $I(x) = x(100 - 2x) = 100x - 2x^2$.
> >
> > Beneficio: $B(x) = 100x - 2x^2 - 20x - 1000 = 80x - 2x^2 - 1000$.
> >
> > $B'(x) = 80 - 4x = 0$ → $x = 20$; $B''(x) = -4 < 0$ → máximo.
> >
> > Precio: $p = 100 - 2(20) = 60$; beneficio: $B(20) = 1600 - 800 - 1000 = 600$.
> >
> > **Respuesta:** vender 20 unidades a \$60 cada una, con beneficio máximo \$600.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico la función objetivo, las restricciones y el dominio en un problema dado.
> - [ ] Resuelvo el problema clásico del rectángulo de área máxima con la metodología MODELO.
> - [ ] Verifico un candidato con el test de la primera o de la segunda derivada.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Modelo problemas geométricos de área, volumen y superficie reduciendo a una sola variable.
> - [ ] Resuelvo problemas económicos de beneficio y costo con su condición de óptimo.
> - [ ] Evalúo los extremos del dominio además de los puntos críticos interiores.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Aplico el truco de minimizar $d^2$ en problemas de distancia y justifico por qué es válido.
> - [ ] Diseño un problema completo de principio a fin y validamos el modelo con los cuatro criterios.
> - [ ] Reconozco cuándo conviene la sustitución y cuándo los multiplicadores de Lagrange.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 4: aplicaciones de la derivada a optimización.
> - R. Larson, *Cálculo* (Cengage), cap. 4: problemas de máximo y mínimo.
> - G. Strang, *Calculus* (Wellesley-Cambridge), cap. 4: optimización con ejemplos económicos.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — herramientas de análisis para evaluar candidatos.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]] — los puntos críticos que aquí se usan.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — el test de la segunda derivada.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u5

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuáles son los cuatro lugares donde puede estar el óptimo?::Puntos críticos ($f' = 0$), frontera del dominio, puntos donde $f'$ no existe y esquinas de restricciones angulares.
> - ¿Cuál es el orden de la metodología MODELO?::Modelado, organizar restricciones, derivar, ecuacionar $f'(x) = 0$, localizar críticos y optimizar (verificar).
> - ¿Qué hacer si el test de la segunda derivada da cero?::Es inconcluso: evalúa $f$ en todos los candidatos, incluidos los bordes del dominio, y compara valores.
> - ¿Por qué se minimiza $d^2$ en problemas de distancia?::Porque la raíz cuadrada es creciente: $d$ y $d^2$ tienen los mismos óptimos, y $d^2$ es un polinomio mucho más fácil de derivar.
> - ¿Cuál es la condición de óptimo en el beneficio?::Que el ingreso marginal iguale al costo marginal, es decir $B'(x) = I'(x) - C'(x) = 0$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/01 - Análisis Completo de Funciones|01 - Análisis Completo de Funciones]] — el análisis completo que alimenta los modelos.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/02 - Monotonía y Puntos Críticos|02 - Monotonía y Puntos Críticos]] — teoría de puntos críticos y extremos.
> - [[Unidad 5 - Aplicaciones de la Derivada/I - Análisis de Funciones/03 - Concavidad y Puntos de Inflexión|03 - Concavidad y Puntos de Inflexión]] — el test de la segunda derivada para clasificar.
> - [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/02 - Optimización con Restricciones|02 - Optimización con Restricciones]] — cuando la restricción no se reduce a una variable.
> - [[Unidad 5 - Aplicaciones de la Derivada/III - Razones de Cambio/02 - Razones de Cambio Relacionadas|02 - Razones de Cambio Relacionadas]] — tasas que cambian juntas en modelos dinámicos.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — el proceso inverso: del extremo al acumulado.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los dos problemas geométricos (rectángulo y caja) hasta que el modelado sea mecánico.
> - Después salta a [[Unidad 5 - Aplicaciones de la Derivada/II - Optimización/02 - Optimización con Restricciones|Optimización con Restricciones]] cuando la restricción no te deje reducir a una sola variable.
> - Aplica la plantilla estándar (datos, modelado, cálculo, verificación) en cada ejercicio: es el formato que se espera en el examen.
> - En cada problema, escribe primero **qué vas a maximizar o minimizar** y **qué te lo limita**; solo después tomes la derivada.

---

**Tags:** #MATG1045 #unidad5 #optimizacion #modelado #maximos-minimos #funcion-objetivo #restricciones #economia #geometria
