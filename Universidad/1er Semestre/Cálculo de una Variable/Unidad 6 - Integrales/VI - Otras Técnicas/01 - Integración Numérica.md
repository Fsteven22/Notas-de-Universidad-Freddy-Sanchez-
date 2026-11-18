---
dg-publish: true
tags: [MATG1045, unidad6, integracion-numerica, integrales, metodos-numericos, trapecio, simpson, error-numerico]
---

# 💻 Integración Numérica

## 🎯 Introducción

> [!info] 💡 Qué es y por qué importa
>
> La **integración numérica** aproxima el valor de integrales definidas $\int_a^b f(x)\,dx$ cuando no es posible —o práctico— encontrar una antiderivada analítica. Todos los métodos se basan en la misma idea: aproximar $f(x)$ por funciones más simples (constantes, rectas, parábolas) cuyas integrales sí se calculan exactas.
>
> **Por qué importa:** muchas funciones sin antiderivada elemental ($e^{-x^2}$, $\frac{\sin x}{x}$) solo se manejan con métodos numéricos; también es la vía cuando los datos son tabulados (mediciones, sensores) o cuando se quiere verificar un resultado analítico.
>
> **Ejemplo:** $\int_0^2 x^2\,dx = \frac{8}{3}$; con $n = 4$ subintervalos, Simpson la reproduce **exactamente**, y el punto medio la aproxima a $2.625$.

> [!tip] 🗺️ El mapa de la nota
>
> - **Definiciones Formales** — la suma de Riemann como base común.
> - **Procedimiento Paso a Paso** — rectángulos, trapecio, Simpson y sus fórmulas de error.
> - **Comparación de Métodos** — orden de precisión, costos y los casos donde difieren.
> - **Ejemplos Resueltos** — diez casos, del rectángulo al trabajo con datos tabulados.
> - **Ejercicios Propuestos** — seis plantillas, incluida la aproximación a $\frac{1}{x}$ y a $e^{-x^2}$.
>
> **Por qué importa:** la tabla de decisión del final (TRAPEZ) dice cuándo usar cada método; el mapa empieza por la suma de Riemann, de la que todo lo demás se deriva cambiando solo el polinomio por tramo.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Suma de Riemann como base común
>
> Todos los métodos numéricos son casos particulares de la definición de la integral como límite de sumas de Riemann:
> $$\int_a^b f(x)\,dx = \lim_{n \to \infty} \sum_{i=1}^n f(x_i^*)\,\Delta x$$
>
> Los métodos se diferencian en **cómo se elige el punto de muestra** $x_i^*$ y **qué polinomio se usa en cada tramo**. Todos tienen la misma estructura: $h = \frac{b-a}{n}$ y $x_i = a + ih$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Integración_Numérica_01.svg]]
>
> **Se lee así:** el diagrama avanza en línea recta hasta un rombo, la única decisión del recorrido: *¿con qué aproximo $f(x)$?*. De ese rombo salen tres ramas —constante, lineal y cuadrática— que llevan a la regla del rectángulo, la del trapecio y la de Simpson, y cada una desemboca en una caja final que resume el tipo de área que se está sumando.
>
> **Por qué importa:** este es el mapa de los métodos numéricos: todos nacen de la suma de Riemann y solo cambian en cómo se elige el punto de muestra y qué polinomio se usa en cada tramo; por eso Simpson da menos error que el trapecio con el mismo $n$.
>
> **Ejemplo:** para aproximar $\int_0^2 x^2\,dx$ con $n = 4$ en la nota, tomas la rama cuadrática —Simpson— y obtienes $\frac{8}{3}$ exacto.

> [!warning] ⚠️ ¿Cuándo usar integración numérica?
>
> 1. **Funciones sin antiderivada elemental:** $\int_0^1 e^{-x^2}\,dx$, $\int_0^\pi \frac{\sin x}{x}\,dx$.
> 2. **Datos experimentales:** valores de $f(x)$ en puntos discretos (tabla).
> 3. **Funciones muy complejas:** antiderivada existe pero es inmanejable.
> 4. **Verificación:** confirmar cálculos analíticos.
> 5. **Ingeniería:** rapidez sobre precisión exacta, o validación antes de publicar.
>
> **Por qué importa:** la lista de situaciones es un filtro: si un método analítico es viable (integración directa, tablas), usarlo; la numérica es para cuando la otra no puede.

---

## 🔧 Procedimiento Paso a Paso

> [!tip] 🔲 Regla del Rectángulo
>
> Aproxima $f(x)$ por una **constante** en cada subintervalo:
>
> - **Punto izquierdo:** $L_n = h\left[f(x_0) + f(x_1) + \cdots + f(x_{n-1})\right]$
> - **Punto derecho:** $R_n = h\left[f(x_1) + f(x_2) + \cdots + f(x_n)\right]$
> - **Punto medio:** $M_n = h\left[f\big(a + \tfrac{h}{2}\big) + f\big(a + \tfrac{3h}{2}\big) + \cdots + f\big(a + \tfrac{(2n-1)h}{2}\big)\right]$
>
> **Error (si $f''$ es continua):** $|E_M| \leq \frac{(b-a)^3}{24n^2}\max|f''(x)|$; $|E_{L,R}| \leq \frac{(b-a)^2}{2n}\max|f'(x)|$.
>
> **Por qué importa:** el punto medio es de orden $O(h^2)$ —el doble de preciso que los extremos— con el mismo número de evaluaciones.

> [!tip] 🔺 Regla del Trapecio
>
> Aproxima $f(x)$ por **segmentos lineales** (trapecios) entre puntos consecutivos:
> $$T_n = \frac{h}{2}\left[f(x_0) + 2f(x_1) + 2f(x_2) + \cdots + 2f(x_{n-1}) + f(x_n)\right]$$
> o en compacta: $T_n = \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1} f(x_i)\right]$
>
> **Error (si $f''$ es continua):** $|E_T| \leq \frac{(b-a)^3}{12n^2}\max|f''(x)|$.
>
> **Por qué importa:** orden $O(h^2)$; exacto para funciones lineales; históricamente el primer método implementado con calculadora.

> [!tip] 🌊 Regla de Simpson (1/3)
>
> Aproxima $f(x)$ por **parábolas** en cada par de subintervalos; requiere $n$ par:
> $$S_n = \frac{h}{3}\left[f(x_0) + 4f(x_1) + 2f(x_2) + 4f(x_3) + \cdots + 2f(x_{n-2}) + 4f(x_{n-1}) + f(x_n)\right]$$
>
> Patrón de coeficientes: $1, 4, 2, 4, 2, \ldots, 2, 4, 1$.
>
> **Error (si $f^{(4)}$ es continua):** $|E_S| \leq \frac{(b-a)^5}{180n^4}\max|f^{(4)}(x)|$.
>
> **Por qué importa:** orden $O(h^4)$ —exactísimo para muchas funciones con $n$ pequeño—; exacto para polinomios de grado $\leq 3$; el método estrella de la asignatura.

> [!tip] 🎓 Mnemotecnia TRAPEZ
>
> - **T** — Tipo de método (rectángulo → trapecio → Simpson).
> - **R** — Resolver intervalos: $h = \frac{b-a}{n}$, puntos $x_i = a + ih$; verificar $n$ par para Simpson.
> - **A** — Aplicar la fórmula con los coeficientes correctos ($1,2,\ldots,2,1$ trapecio; $1,4,2,\ldots,4,1$ Simpson).
> - **P** — Precisión: estimar el error con las fórmulas teóricas; duplicar $n$ como control.
> - **E** — Error experimental: comparar con valor exacto si se conoce.
> - **Z** — Zona de validez: comprobar continuidad de las derivadas requeridas e intervalos sin singularidades.
>
> **Por qué importa:** las seis letras son el procedimiento completo de cualquier aproximación; saltarse la **Z** produce estimaciones que parecen converger.

---

## 📊 Comparación de Métodos

> [!tip] 📋 Tabla comparativa
>
> | Método | Aproximación | Orden de error | Exacto para | Coeficientes |
> |---|---|---|---|---|
> | Rectángulo (extremos) | constante | $O(h)$ | constantes | $1, 1, 1, \ldots$ |
> | Rectángulo (punto medio) | constante | $O(h^2)$ | constantes | $1, 1, 1, \ldots$ |
> | Trapecio | lineal | $O(h^2)$ | lineales | $\frac{1}{2}, 1, 1, \ldots, 1, \frac{1}{2}$ |
> | Simpson 1/3 | cuadrática | $O(h^4)$ | cúbicas | $1, 4, 2, 4, \ldots, 4, 1$ |
>
> **Por qué importa:** es la regla para decidir: si basta con $O(h^2)$ y los datos son tabulados, trapecio; si hay fórmula exacta o $n$ par, Simpson; si solo se tienen tres puntos, Simpson 3/8.

> [!info] 🧮 Métodos avanzados
>
> - **Simpson 3/8** (para $n$ múltiplo de 3): $S_{3/8} = \frac{3h}{8}\left[f(x_0) + 3f(x_1) + 3f(x_2) + 2f(x_3) + \cdots + f(x_n)\right]$, con el mismo orden que Simpson 1/3.
> - **Cuadratura de Gauss–Legendre:** puntos y pesos óptimos; $n$ puntos integran exacto polinomios de grado $2n-1$.
> - **Cuadratura adaptativa:** calcula con $n$ y $2n$ puntos y estima el error por la diferencia; repite hasta bajar de la tolerancia.
>
> **Por qué importa:** son la puerta a los sistemas profesionales; la 1/3 y el trapecio son las que se usan en el curso y en el examen.

---

## 🧮 Ejemplos Resueltos

> [!example] 🔢 Ejemplo 1 — Rectángulo para $\int_0^2 x^2\,dx$, $n = 4$
>
> **Datos:** $h = 0.5$; puntos $0, 0.5, 1, 1.5, 2$.
>
> **Punto izquierdo:** $L_4 = 0.5\left[0 + 0.25 + 1 + 2.25\right] = 1.75$
>
> **Punto derecho:** $R_4 = 0.5\left[0.25 + 1 + 2.25 + 4\right] = 3.75$
>
> **Punto medio:** $M_4 = 0.5\left[0.0625 + 0.5625 + 1.5625 + 3.0625\right] = 2.625$
>
> **Exacto:** $\frac{8}{3} \approx 2.667$. Errores: $|E_{L_4}| \approx 0.92$, $|E_{R_4}| \approx 1.08$, $|E_{M_4}| \approx 0.042$.
>
> **Por qué importa:** el punto medio gana a los extremos por un orden de magnitud; esta comparación es el porqué de las fórmulas de error.

> [!example] 🔢 Ejemplo 2 — Trapecio para $\int_0^2 x^2\,dx$, $n = 4$
>
> $$T_4 = \frac{0.5}{2}\left[0 + 2(0.25) + 2(1) + 2(2.25) + 4\right] = 0.25 \times 11 = 2.75$$
>
> **Error:** $|2.75 - 2.667| = 0.083$. Exacto para funciones lineales; mejor que extremos, peor que punto medio y Simpson.
>
> **Por qué importa:** el trapecio es el puente natural: necesita los mismos puntos que el rectángulo pero con los coeficientes $\frac{1}{2}$.

> [!example] 🔢 Ejemplo 3 — Simpson 1/3 para $\int_0^2 x^2\,dx$, $n = 4$
>
> $$S_4 = \frac{0.5}{3}\left[0 + 4(0.25) + 2(1) + 4(2.25) + 4\right] = \frac{0.5 \times 16}{3} = \frac{8}{3}$$
>
> **¡Resultado exacto!** — Simpson es exacto para polinomios de grado $\leq 3$.
>
> **Por qué importa:** el único método de la tabla que no acumula error en polinomios bajos; el resto se equivoca aunque sea por poco.

> [!example] 🔢 Ejemplo 4 — $\int_1^2 \frac{1}{x}\,dx$ con $n = 4$ vs. Simpson
>
> **Trapecio:** $T_4 = \frac{0.25}{2}\left[1 + 2\left(\frac45 + \frac23 + \frac47\right) + \frac12\right] = 0.6970$
>
> **Simpson:** $S_4 = \frac{0.25}{3}\left[1 + 4(0.8) + 2(0.6667) + 4(0.5714) + 0.5\right] = 0.6933$
>
> **Exacto:** $\ln 2 \approx 0.6931$. Errores: trapecio $\approx 0.0039$, Simpson $\approx 0.0001$.
>
> **Por qué importa:** con la misma información ($5$ puntos), Simpson quintuplica la precisión; es la regla para elegir método con tabla.

> [!example] 🔢 Ejemplo 5 — Datos tabulados: trabajo $W = \int_0^2 F(x)\,dx$
>
> **Datos:** $F(0) = 10$, $F(0.5) = 15$, $F(1) = 25$, $F(1.5) = 30$, $F(2) = 20$ N.
>
> - **Trapecio:** $W = \frac{0.5}{2}\left[10 + 2(15 + 25 + 30) + 20\right] = 0.25 \times 170 = 42.5$ J
> - **Simpson:** $W = \frac{0.5}{3}\left[10 + 4(15) + 2(25) + 4(30) + 20\right] = \frac{0.5 \times 260}{3} \approx 43.33$ J
>
> **Por qué importa:** con datos tabulados no hay fórmula que valga: los trapecios (o Simpson) **son** el método.

> [!example] 🔢 Ejemplo 6 — Sin antiderivada elemental: $\int_0^1 e^{-x^2}\,dx$
>
> **Problema:** no existe antiderivada elemental (función error de Gauss).
>
> **Con $n = 8$:** $\displaystyle\int_0^1 e^{-x^2}\,dx \approx 0.7468241$ (valor con diez decimales).
>
> **Por qué importa:** los coeficientes $1,4,2,4,\ldots,4,1$ están diseñados para acumular precisión justo cuando la fórmula no existe.

---

## ⚠️ Errores Comunes y Limitaciones

> [!warning] 🚨 Errores frecuentes
>
> 1. **Número de intervalos incorrecto:**
>    - ❌ usar $n$ impar con Simpson
>    - ✅ verificar que $n$ es par para Simpson 1/3
> 2. **Coeficientes mal aplicados:**
>    - ❌ usar coeficientes del trapecio en Simpson
>    - ✅ memorizar patrones: trapecio $(1, 2, \ldots, 2, 1)$, Simpson $(1, 4, 2, 4, \ldots, 4, 1)$
> 3. **Estimación de error inadecuada:**
>    - ❌ usar las fórmulas de error sin verificar condiciones
>    - ✅ comprobar continuidad de las derivadas ($f''$, $f^{(4)}$) requeridas
> 4. **Elección incorrecta de método:**
>    - ❌ usar rectángulo cuando se necesita precisión alta
>    - ✅ elegir según balance precisión/costo
> 5. **Singularidades:**
>    - ❌ aplicar métodos estándar a $\int_0^1 \frac{dx}{\sqrt{x}}$ (la derivada explota en $x = 0$)
>    - ✅ transformar la variable o usar técnicas especiales
>
> **Por qué importa:** los cinco son errores de planteamiento, no de aritmética; la tabla comparativa del apartado anterior es su antídoto.

> [!warning] ⚠️ Cuándo fallan los métodos estándar
>
> - **Singularidades:** $\int_0^1 \frac{dx}{\sqrt{x}}$ (transformar $x = t^2$).
> - **Oscilaciones rápidas:** necesitan $n$ grande o métodos adaptativos.
> - **Intervalos infinitos:** transformar la variable o truncar.
> - **Discontinuidades:** tratar cada tramo por separado.

> [!info] 🌀 Ejemplo oscilante: $\int_0^{2\pi} x\sin(10x)\,dx$
>
> **Desafío:** la función oscila 10 veces en el intervalo; se requiere $n \geq 100$ con Simpson.
>
> **Resultado:** $-\frac{\pi}{5} \approx -0.628$ (valor exacto por partes).
>
> **Lección:** en funciones oscilantes, aumentar $n$ hasta que el control de convergencia se estabilice.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Aproxima $\int_0^1 \frac{1}{x+1}\,dx$ con $n = 4$ usando trapecio y Simpson.
>
> > [!success]- ✅ Solución
> > $h = 0.25$; $f = 1, \tfrac45, \tfrac23, \tfrac47, \tfrac12$.
> > $$T_4 = 0.125\left(1 + 2\left(0.8 + 0.6667 + 0.5714\right) + 0.5\right) = 0.6970$$
> > $$S_4 = \frac{0.25}{3}\left(1 + 4(0.8) + 2(0.6667) + 4(0.5714) + 0.5\right) = 0.6933$$
> > Exacto: $\ln 2 \approx 0.6931$.
> > **Lección:** con $5$ puntos, Simpson duplica la precisión del trapecio ✓

> [!example] 📋 Planteamiento
>
> Aproxima $\int_0^2 e^{x^2}\,dx$ con Simpson y $n = 4$, y estima el error.
>
> > [!success]- ✅ Solución
> > $h = 0.5$:
> > $$S_4 = \frac{0.5}{3}\left[f(0) + 4f(0.5) + 2f(1) + 4f(1.5) + f(2)\right] \approx 23.37$$
> > Control con $n = 8$ (misma tabla, el doble de puntos) y comparar; $|S_8 - S_4|$ estima el error.
> > **Lección:** ante duda, duplicar $n$ vale más que cualquier fórmula de error con $\max|f^{(4)}|$ difícil de acotar ✓

> [!example] 📋 Planteamiento
>
> Aproxima con Simpson el área bajo $f(x) = \sqrt{x}$ en $[0, 4]$ con $n = 4$; compara con $\frac{16}{3}$.
>
> > [!success]- ✅ Solución
> > $h = 1$; $f(0) = 0$, $f(1) = 1$, $f(2) = \sqrt2$, $f(3) = \sqrt3$, $f(4) = 2$:
> > $$S_4 = \frac{1}{3}\left(0 + 4(1) + 2\sqrt2 + 4\sqrt3 + 2\right) = \frac{6 + 2\sqrt2 + 4\sqrt3}{3} \approx 5.259$$
> > Exacto: $\int_0^4 \sqrt{x}\,dx = \frac{2}{3} \cdot 8 = \frac{16}{3} \approx 5.333$. Error $\approx 0.074$.
> > **Lección:** Simpson no es exacto aquí ($f^{(4)}$ diverge en $x = 0$), pero con $n$ mayor el error baja rápido ✓

> [!example] 📋 Planteamiento
>
> Una fuerza medida cada $0.5$ m toma valores $10, 15, 25, 30, 20$ N. Calcula el trabajo con trapecio y con Simpson.
>
> > [!success]- ✅ Solución
> > Trapecio: $W = 0.25\left[10 + 2(15 + 25 + 30) + 20\right] = 42.5$ J.
> > Simpson: $W = \frac{0.5}{3}\left[10 + 4(15) + 2(25) + 4(30) + 20\right] = \frac{260}{6} \approx 43.33$ J.
> > **Lección:** dos métodos "razonables" difieren en $1.9\%$; el dato de precisión manda la elección ✓

> [!example] 📋 Planteamiento
>
> Decide qué método usar para $\int_0^1 e^{-x^2}\,dx$ y calcula con Simpson $n = 2$.
>
> > [!success]- ✅ Solución
> > No existe antiderivada: numérica. $h = 0.5$:
> > $$S_2 = \frac{0.5}{3}\left[f(0) + 4f(0.5) + f(1)\right] = \frac{0.5}{3}\left(1 + 4e^{-0.25} + e^{-1}\right) \approx 0.7472$$
> > Exacto: $0.7468$.
> > **Lección:** con 3 puntos, Simpson ya da 3 cifras; el método estratificado siempre gana a los extremos ✓

> [!example] 📋 Planteamiento
>
> ¿Por qué Simpson fue exacto en el ejemplo del $x^2$ y no en el de $\sqrt{x}$?
>
> > [!success]- ✅ Solución
> > Simpson es exacto para polinomios de grado $\leq 3$. $x^2$ es un polinomio de grado 2 → exacto. $\sqrt{x}$ no es un polinomio (tampoco un $C^4$ en $[0, 4]$: $f^{(4)}$ diverge en $0$) → el error teórico con $f^{(4)}$ continua no aplica en $[0, 4]$ y la aproximación solo se mejora duplicando $n$ (o integrando directamente).
> > **Lección:** la fórmula de error tiene condiciones; si no se cumplen, la duplicación de $n$ es el control ✓

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Planteo la suma de Riemann y reconozco los métodos como casos particulares según el polinomio por tramo.
> - [ ] Calculo aproximaciones con rectángulo (izquierdo, derecho y punto medio) para $n$ dado.
> - [ ] Reconozco las situaciones donde la integración numérica es la única vía (sin antiderivada elemental, datos tabulados).

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico trapecio y Simpson 1/3 con los coeficientes correctos y verifico $n$ par para Simpson.
> - [ ] Estimo el error con las fórmulas $|E_T| \leq \frac{(b-a)^3}{12n^2}M$ y $|E_S| \leq \frac{(b-a)^5}{180n^4}M$, comprobando la continuidad de $f''$ o $f^{(4)}$.
> - [ ] Comparo métodos con la tabla de decisión ($O(h)$ vs $O(h^2)$ vs $O(h^4)$) según la precisión requerida.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Uso control de convergencia duplicando $n$ cuando no puedo acotar $\max|f^{(4)}|$.
> - [ ] Manejo casos especiales: oscilación rápida (aumentar $n$), singularidades (transformar variable) y datos tabulados.
> - [ ] Reconozco Simpson 3/8, cuadratura de Gauss y cuadratura adaptativa como extensiones naturales.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 7.7: estrategias para la integración y métodos numéricos.
> - G. Strang, *Calculus* (Wellesley-Cambridge): sumas de Riemann y trapecios compuestos.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la definición que origina todos los métodos.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la comparación con los métodos exactos.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — cuándo optar por lo analítico antes que lo numérico.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/03 - Teoremas de Comparación y Desigualdades|03 - Teoremas de Comparación y Desigualdades]] — estimación de errores e ideas afines.
> - [[Unidad 6 - Integrales/VI - Otras Técnicas/02 - Integrales en Coordenadas Polares|02 - Integrales en Coordenadas Polares]] — la otra técnica avanzada de la unidad.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/02 - Área entre Curvas|02 - Área entre Curvas]] — las integrales tabuladas aparecen como áreas entre curvas y se integran con estos métodos.
>
> **Conexiones interdisciplinarias:** programación (implementación de algoritmos), estadística (datos experimentales), ingeniería (integración de perfiles de fuerza y presión) y análisis de señales (muestreo).

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Cuál es la base común de todo método numérico?::La suma de Riemann: $\int_a^b f\,dx = \lim_{n\to\infty} \sum f(x_i^*)\Delta x$; los métodos difieren en cómo eligen $x_i^*$ y el polinomio por tramo.
> - ¿Cómo es la regla del trapecio?::$T_n = \frac{h}{2}\left[f(a) + f(b) + 2\sum_{i=1}^{n-1} f(x_i)\right]$; orden $O(h^2)$.
> - ¿Cómo es la regla de Simpson 1/3?::$S_n = \frac{h}{3}[f(x_0) + 4f(x_1) + 2f(x_2) + \cdots + 4f(x_{n-1}) + f(x_n)]$; requiere $n$ par; orden $O(h^4)$.
> - ¿Para qué polinomios es exacto Simpson?::Para polinomios de grado $\leq 3$.
> - ¿Qué diferencia hay entre punto medio y extremos?::El punto medio es $O(h^2)$ con el mismo costo; los extremos son solo $O(h)$.
> - ¿Cuándo usar integración numérica?::Sin antiderivada elemental ($e^{-x^2}$), con datos tabulados, o para verificar un resultado analítico.
> - ¿Cómo se verifica que la aproximación convergiendo?::Duplicar $n$ y comparar ambas aproximaciones; la diferencia acota el error.
> - ¿Qué pasa en funciones oscilantes?::Exigen $n$ mucho mayor; mejor el punto medio y Simpson adaptativo.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — base teórica de todos los métodos numéricos.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la comparación con los métodos exactos.
> - [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]] — cuándo usar analítico vs. numérico.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/03 - Teoremas de Comparación y Desigualdades|03 - Teoremas de Comparación y Desigualdades]] — estimación de errores y validación.
> - [[Unidad 6 - Integrales/VI - Otras Técnicas/02 - Integrales en Coordenadas Polares|02 - Integrales en Coordenadas Polares]] — la otra técnica avanzada de la unidad.
> - [[Unidad 7 - Aplicaciones de la Integral/III - Longitud de Arco/01 - Longitud de Curva|01 - Longitud de Curva]] — donde estas técnicas numéricas resuelven integrales sin forma cerrada.
>
> **Conexiones interdisciplinarias:** programación (implementación de algoritmos de integración), estadística y análisis de datos (mediciones discretas), ingeniería (integración de fuerzas y presión en perfiles) y análisis de señales (muestreo y cuadratura).

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1 y 4: trapecio y Simpson contra el valor exacto con $\ln 2$.
> - Después el 3 y el 5: $\sqrt{x}$ y $e^{-x^2}$, los dos casos sin forma cerrada ni $C^4$.
> - Cierra con 2 y 6: control de convergencia y elección razonada del método.
> - Cuando lo tengas, sigue con [[Unidad 6 - Integrales/VI - Otras Técnicas/02 - Integrales en Coordenadas Polares|02 - Integrales en Coordenadas Polares]], la otra técnica avanzada, y repasa [[Unidad 6 - Integrales/III - Integrales Definidas/01 - Métodos de Integración Definida|01 - Métodos de Integración Definida]].

---

**Tags:** #MATG1045 #unidad6 #integracion-numerica #integrales #metodos-numericos #trapecio #simpson #error-numerico
