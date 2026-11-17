---
dg-publish: true
tags: [MATG1045, unidad6, teoremas-de-comparacion-y-desigualdades, comparacion, desigualdades, convergencia, integrales-definidas, integrales-impropias, estimacion, acotacion, analisis]
---

# ⚖️ Teorema de Comparación y Desigualdades

## 🎯 Introducción

> [!info] 💡 Qué te permiten hacer
>
> Los teoremas de comparación y desigualdades sirven para **estimar, acotar y comparar integrales definidas sin evaluarlas exactamente**: si sabes que $f(x) \leq g(x)$, entonces la integral de la menor no puede superar a la de la mayor, y con eso ya tienes un valor sin calcular. Son la base del análisis de convergencia de las **integrales impropias** y de la estimación de valores integrales en física y probabilidad.
>
> **Por qué importa:** hay integrales cuya antiderivada no existe en elementos elementales (o existe y es desagradable) y que, aun así, se pueden acotar de un vistazo. Además, los criterios de comparación de la nota `02 - Criterios de Convergencia y Divergencia` se demuestran justo con estas desigualdades.
>
> **Ejemplo:** con $\int_1^2 \frac{1}{x^2}\,dx$ y $\int_1^2 \frac{1}{x}\,dx$ basta notar que $\frac{1}{x^2} \leq \frac{1}{x}$ en $[1,2]$ para concluir $\frac{1}{2} \leq \ln 2$, sin sorpresas.

> [!tip] 🎯 Dónde aparece en la carrera
>
> - **Integrales impropias:** decidir convergencia sin integrar.
> - **Análisis de series:** el criterio integral y la comparación de series son el mismo argumento en otra ropa.
> - **Estimación numérica:** cotas para integrales que solo se resuelven por cuadratura.
> - **Fourier:** acotar coeficientes $a_n$ para probar convergencia de series.
>
> **Por qué importa:** es la herramienta que resuelve el "no puedo calcularlo, pero sé dónde está".

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Teorema de comparación para integrales definidas
>
> Si $f(x) \leq g(x)$ para todo $x \in [a,b]$ y ambas funciones son integrables en $[a,b]$, entonces:
>
> $$\int_a^b f(x)\,dx \leq \int_a^b g(x)\,dx$$
>
> **Interpretación:** la integral de la función menor es menor o igual que la integral de la función mayor.
>
> **Demostración** (el esquema completo está en la figura):
>
> 1. **Paso 1:** definir $h(x) = g(x) - f(x) \geq 0$ para todo $x \in [a,b]$.
> 2. **Paso 2:** como $h \geq 0$, su integral es no negativa: $\int_a^b h(x)\,dx \geq 0$.
> 3. **Paso 3:** por linealidad, $\int_a^b h = \int_a^b g - \int_a^b f$.
> 4. **Paso 4:** por tanto $\int_a^b g - \int_a^b f \geq 0$, es decir $\int_a^b f \leq \int_a^b g$ ✓
>
> **Variante estricta:** si $f(x) < g(x)$ salvo en un conjunto finito de puntos, entonces $\int_a^b f < \int_a^b g$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Teoremas_de_Comparación_y_Desigualdades_01.svg]]
>
> **Se lee así:** una cadena de rectángulos que arranca con el enunciado del teorema ("si $f \leq g$ en $[a,b]$, entonces $\int f \leq \int g$") y baja por cuatro pasos encadenados por flechas: la función auxiliar no negativa $h = g - f$, el hecho de que su integral es $\geq 0$, la linealidad que la descompone en $\int g - \int f$ y la desigualdad final. Del último bloque sale una caja aparte con la variante estricta.
>
> **Por qué importa:** comparar integrales no es una regla suelta: es **linealidad de la integral aplicada a una diferencia**. Entendido así, deduces tú mismo la desigualdad triangular y cualquier corolario.
>
> **Ejemplo:** con $f(x) = \frac{1}{x^2}$ y $g(x) = \frac{1}{x}$ en $[1,2]$, la cadena concluye $\int_1^2 \frac{1}{x^2}\,dx \leq \int_1^2 \frac{1}{x}\,dx$, es decir $\frac{1}{2} \leq \ln 2$.

> [!warning] ⚠️ Condiciones necesarias
>
> - Ambas funciones deben ser **integrables** en $[a,b]$ (si una de las integrales no existe, la desigualdad no dice nada).
> - La desigualdad $f(x) \leq g(x)$ debe cumplirse para **todo** $x \in [a,b]$, no solo en algunos puntos.
> - Para la variante estricta basta con que la desigualdad sea estricta salvo en un conjunto **finito** de puntos.
>
> **Por qué importa:** el 90 % de los fallos con este teorema son hipótesis incumplidas: o la desigualdad falla en una parte del intervalo, o una de las dos integrales no existe.

---

## 📐 Corolarios y acotaciones

> [!tip] 📐 Desigualdad triangular para integrales
>
> Si $f$ es integrable en $[a,b]$, entonces:
>
> $$\left|\int_a^b f(x)\,dx\right| \leq \int_a^b |f(x)|\,dx$$
>
> **Interpretación:** el valor absoluto de la integral es menor o igual que la integral del valor absoluto — el peor caso posible acota al valor real.
>
> **Por qué importa:** es el paso previo obligatorio cuando $f$ **cambia de signo**: primero acotas con $|f|$, que es positiva, y ahí sí aplicas comparación.
>
> **Ejemplo:** si $\left|\int_{-1}^{1} x^3 \sin(x^2)\,dx\right| \leq \int_{-1}^{1} |x^3|\,dx = \frac{1}{2}$, ya sabes que el valor está en $[-1/2, 1/2]$ aunque no lo calcules.

> [!info] 📏 Acotación por constantes
>
> Si $m \leq f(x) \leq M$ para todo $x \in [a,b]$, entonces:
>
> $$m(b-a) \leq \int_a^b f(x)\,dx \leq M(b-a)$$
>
> **Interpretación:** la integral está entre el área del rectángulo de altura mínima y el del rectángulo de altura máxima.
>
> **Por qué importa:** es la acotación más rápida que existe: no necesitas integrar nada, solo el rango de la función y la longitud del intervalo.
>
> **Ejemplo:** en $[0,\pi]$ vale $0 \leq x\sin x \leq \pi$, luego $0 \leq \int_0^{\pi} x\sin x\,dx \leq \pi^2 \approx 9{,}87$ (el valor exacto es $\pi$).

> [!warning] ⚡ Funciones de referencia para comparar
>
> Para estimar integrales complejas se compara con:
>
> - **Polinomios:** $x^n$, especialmente para $x$ grande o pequeño.
> - **Exponenciales:** $e^{-x}$, $e^{x}$ para comportamiento asintótico.
> - **Funciones potencia:** $\frac{1}{x^p}$ para singularidades e infinitos.
> - **Trigonométricas acotadas:** $|\sin x| \leq 1$, $|\cos x| \leq 1$.
>
> **Por qué importa:** con cuatro funciones patrón cubres casi todo: la clave está en elegir la que **domine** el comportamiento del integrando en la zona que te interesa.

---

## ⚖️ Criterios de comparación para impropias

> [!info] 📋 Criterio de comparación directa
>
> Sean $0 \leq f(x) \leq g(x)$ para $x \geq a$ (o cerca de una singularidad):
>
> - **Convergencia:** si $\int g(x)\,dx$ converge, entonces $\int f(x)\,dx$ converge.
> - **Divergencia:** si $\int f(x)\,dx$ diverge, entonces $\int g(x)\,dx$ diverge.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/03_-_Teoremas_de_Comparación_y_Desigualdades_02.svg]]
>
> **Se lee así:** un flujo que parte de la caja "criterio de comparación directa (integrales impropias)" y pasa por el supuesto $0 \leq f(x) \leq g(x)$ para $x \geq a$. De ahí salen dos ramas paralelas: la de convergencia, que termina en "la chica hereda convergencia de la grande", y la de divergencia, que cierra con "la grande hereda divergencia de la chica".
>
> **Por qué importa:** aquí la comparación se usa al revés que en las definidas: no para acotar un valor, sino para **decidir si la integral existe**. Es la herramienta para clasificar impropias sin antiderivada sencilla.
>
> **Ejemplo:** como $0 \leq \frac{1}{x^2+1} \leq \frac{1}{x^2}$ para $x \geq 1$ y $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$ converge, la rama de convergencia certifica que $\int_1^{\infty} \frac{1}{x^2+1}\,dx$ también converge.

> [!tip] 📋 Criterio de comparación en el límite
>
> Sean $f(x) \geq 0$ y $g(x) > 0$ continuas en $[a,b)$ con $b$ posiblemente infinito. Si
>
> $$\lim_{x \to b^-} \frac{f(x)}{g(x)} = L, \qquad 0 < L < \infty$$
>
> entonces $\int_a^b f$ y $\int_a^b g$ **convergen o divergen juntas**.
>
> **Casos especiales:**
>
> - Si $L = 0$ y $\int g$ **converge** → $\int f$ converge (lo pequeño está cubierto).
> - Si $L = \infty$ y $\int g$ **diverge** → $\int f$ diverge (lo grande arrastra).
> - Los demás cruces ($L = 0$ con $\int g$ divergente, o $L = \infty$ con $\int g$ convergente) **no deciden nada**.
>
> **Por qué importa:** el criterio por límite es el que más se usa en examen porque basta comparar **grados dominantes**; pero el matiz de los casos $L = 0$ y $L = \infty$ es el que separa un acierto de un error.
>
> **Ejemplo:** $\lim_{x \to \infty} \frac{(x^2+1)/(x^4+x^2+1)}{1/x^2} = 1$, así que la integral se comporta como $\int_1^{\infty} \frac{1}{x^2}\,dx$ y converge.

---

## 🧩 Cómo elegir la función de referencia

> [!info] 📋 Funciones de comparación comunes
>
> | Tipo | Función | Comportamiento | Uso principal |
> |---|---|---|---|
> | Potencias | $\frac{1}{x^p}$ | $p > 1$: converge en $[1,\infty)$ | Singularidades e infinitos |
> | Exponenciales | $e^{-ax}$ ($a > 0$) | Decae muy rápido | Colas exponenciales |
> | Logarítmicas | $\frac{1}{x \ln^p x}$ | $p > 1$: converge en $[2,\infty)$ | Decrecimientos logarítmicos |
> | Trigonométricas | $\frac{\sin x}{x^p}$ | Oscilación acotada | Integrales oscilatorias |
> | Racionales | $\frac{P(x)}{Q(x)}$ | Según los grados | Funciones racionales complejas |
>
> **Por qué importa:** cada fila es una familia con su propia regla de convergencia; identificar a qué familia pertenece tu integrando es la mitad del ejercicio.

> [!tip] 💡 Estrategias de selección
>
> **Para $x \to \infty$:**
>
> 1. Identificar el **término dominante** del numerador y del denominador.
> 2. Simplificar a la forma más básica posible.
> 3. Comparar con funciones de referencia conocidas ($\frac{1}{x^p}$, $e^{-ax}$).
>
> **Para $x \to a$ (singularidad):**
>
> 4. Analizar el **comportamiento local** cerca del punto singular.
> 5. Expandir en series si es necesario.
> 6. Comparar con $\frac{1}{(x-a)^p}$ o similar.
>
> **Para funciones oscilatorias:**
>
> 7. Usar **cotas** del tipo $|\sin x| \leq 1$, $|\cos x| \leq 1$.
> 8. Comparar con la **envolvente** de la función.
>
> **Por qué importa:** el orden importa: primero el análisis asintótico, después la elección. Elegir la función de referencia antes de mirar el integrando es el error que arruina la comparación.

---

## 🧠 Método COMPAR

> [!tip] 🎓 Mnemotecnia COMPAR
>
> **C** — **Comparar** funciones y establecer desigualdades.
> **O** — **Ordenar** las funciones (mayor, menor, igual).
> **M** — **Mayorar** o minorar según convenga.
> **P** — **Probar** convergencia/divergencia de la función de referencia.
> **A** — **Aplicar** el criterio de comparación apropiado.
> **R** — **Revisar** y verificar el resultado.
>
> **Por qué importa:** las seis letras cubren el ciclo completo del ejercicio; saltarse la P (probar primero la referencia) es lo que produce resultados sin sustento.

> [!abstract] 📋 Pasos a seguir
>
> **C — Comparar funciones:** identificar las funciones involucradas, establecer el dominio de comparación y determinar los puntos problemáticos (singularidades, infinitos).
>
> **O — Ordenar las funciones:** decidir cuál es mayor/menor, verificar la desigualdad en todo el intervalo relevante y considerar el comportamiento asintótico.
>
> **M — Mayorar o minorar:** para probar **convergencia** buscar una mayorante convergente; para probar **divergencia** buscar una minorante divergente.
>
> **P — Probar la referencia:** evaluar la integral de la función de comparación con criterios conocidos ($p$-integrales, exponenciales) y verificar su convergencia/divergencia.
>
> **A — Aplicar el criterio:** comparación directa si $0 \leq f \leq g$; comparación por límite si $\lim \frac{f}{g} = L$; deducir el resultado para la función original.
>
> **R — Revisar:** comprobar coherencia, casos límite e intuición física o geométrica.
>
> **Por qué importa:** la letra **M** es la que más se confunde: mayorar con una **divergente** no prueba nada para probar convergencia. El paso R te obliga a mirar el resultado dos veces antes de entregarlo.

---

## ⚠️ Errores comunes

> [!warning] 🚨 Los cinco fallos típicos
>
> 1. **Desigualdad en sentido incorrecto:** ❌ probar convergencia mayorando con una función divergente · ✅ probar convergencia mayorando con una función **convergente**.
> 2. **Intervalos de validez:** ❌ aplicar la desigualdad fuera del dominio donde vale · ✅ verificar la desigualdad en **todo** el intervalo de integración.
> 3. **Confundir criterios:** ❌ usar comparación directa cuando el límite es $0$ o $\infty$ · ✅ elegir el criterio según el valor del límite.
> 4. **Funciones de referencia incorrectas:** ❌ comparar $\frac{1}{x^2}$ con $\frac{1}{x}$ para probar divergencia · ✅ usar la jerarquía correcta de referencias.
> 5. **Signos de las funciones:** ❌ aplicar criterios sin verificar que $f \geq 0$ · ✅ asegurar la positividad o usar el valor absoluto.
>
> **Por qué importa:** los tres primeros son de **razonamiento** y ninguno los detecta la calculadora; se previenen siguiendo el método COMPAR paso por paso.

> [!info] ⚠️ Situaciones que requieren cuidado especial
>
> - **Funciones que cambian de signo:** aplicar primero la desigualdad triangular y comparar con $\int |f|$.
> - **Múltiples singularidades:** dividir el intervalo y analizar cada parte por separado.
> - **Comportamiento oscilatorio:** distinguir entre oscilación acotada (comparable) y no acotada (no comparable).
> - **Funciones definidas por partes:** verificar la continuidad en los puntos de transición.
>
> **Por qué importa:** son los casos donde el teorema básico "se aplica mal sin avisar": ninguna condición falla de forma ruidosa.

---

## 🌟 Aplicaciones

> [!tip] 💡 Estimación de integrales definidas
>
> Cuando no puedes evaluar $\int_a^b f(x)\,dx$ exactamente:
>
> 1. **Encontrar cotas:** $m \leq f(x) \leq M$ en $[a,b]$.
> 2. **Aplicar la desigualdad:** $m(b-a) \leq \int_a^b f \leq M(b-a)$.
> 3. **Refinar la estimación:** dividir el intervalo en trozos para cotas más precisas.
>
> **Por qué importa:** cada subdivisión mejora la cota sin integrar nada: es el germen de los métodos numéricos (rectángulos, Simpson).

> [!info] 🚀 Base para integrales impropias
>
> Los teoremas de comparación son **esenciales** para:
>
> - Determinar convergencia **sin calcular** la integral.
> - Clasificar el comportamiento asintótico del integrando.
> - Establecer criterios de convergencia uniforme.
> - Analizar series infinitas relacionadas (criterio integral).
>
> **Por qué importa:** sin estas desigualdades, los criterios de `02 - Criterios de Convergencia y Divergencia` no tendrían sobre qué apoyarse.

> [!warning] 📊 Convergencia de series de Fourier
>
> Para determinar la convergencia de los coeficientes:
>
> $$a_n = \int_{-\pi}^{\pi} f(x) \cos(nx)\,dx$$
>
> se usa comparación con $\frac{1}{n^p}$ según el comportamiento de $f(x)$.
>
> **Por qué importa:** la acotación de $a_n$ es lo que decide si la serie de Fourier converge puntualmente; ahí la desigualdad triangular y la comparación trabajan juntas.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Compara $\int_1^2 \frac{1}{x^2}\,dx$ y $\int_1^2 \frac{1}{x}\,dx$ sin calcular ambas.
>
> > [!success]- ✅ Solución
> >
> > **Análisis:** para $x \in [1,2]$ vale $x \geq 1$, luego $x^2 \geq x$ y por tanto $\frac{1}{x^2} \leq \frac{1}{x}$.
> >
> > **Teorema:** $\int_1^2 \frac{1}{x^2}\,dx \leq \int_1^2 \frac{1}{x}\,dx$.
> >
> > **Verificación numérica:** $\int_1^2 \frac{1}{x^2} = \big[-\frac{1}{x}\big]_1^2 = \frac{1}{2}$ y $\int_1^2 \frac{1}{x} = \ln 2 \approx 0{,}693$.
> >
> > **Respuesta:** $\frac{1}{2} \leq \ln 2$ ✓ (efectivamente $0{,}5 < 0{,}693$).

> [!example] 📋 Planteamiento
>
> Estima $\int_0^{\pi} x \sin x\,dx$ con acotación por constantes.
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** en $[0,\pi]$ vale $0 \leq \sin x \leq 1$ y $0 \leq x \leq \pi$, así que $0 \leq x\sin x \leq \pi$.
> >
> > **Paso 2:** acotación constante: $0 \cdot (\pi - 0) \leq \int_0^{\pi} x\sin x\,dx \leq \pi \cdot \pi$, es decir $0 \leq I \leq \pi^2 \approx 9{,}87$.
> >
> > **Verificación:** el valor exacto, por partes, es $\pi$; queda dentro de la cota.
> >
> > **Respuesta:** $0 \leq \int_0^{\pi} x\sin x\,dx \leq \pi^2$ ✓

> [!example] 📋 Planteamiento
>
> Analiza $\int_{-1}^{1} x^3 \sin(x^2)\,dx$ con la desigualdad triangular.
>
> > [!success]- ✅ Solución
> >
> > **Aplicación directa:** como $|\sin(x^2)| \leq 1$,
> > $$\left|\int_{-1}^{1} x^3 \sin(x^2)\,dx\right| \leq \int_{-1}^{1} |x^3 \sin(x^2)|\,dx \leq \int_{-1}^{1} |x^3|\,dx$$
> >
> > **Evaluación de la cota:** $\int_{-1}^{1} |x^3|\,dx = 2\int_0^1 x^3\,dx = 2 \cdot \frac{1}{4} = \frac{1}{2}$.
> >
> > **Valor exacto:** $x^3 \sin(x^2)$ es **impar** (impar × par = impar), así que la integral es $0$.
> >
> > **Respuesta:** $|0| = 0 \leq \frac{1}{2}$ — la cota es correcta y el valor sale de la simetría ✓

> [!example] 📋 Planteamiento
>
> Decide la convergencia de $\int_1^{\infty} \frac{x^2 + 1}{x^4 + x^2 + 1}\,dx$ por comparación en el límite.
>
> > [!success]- ✅ Solución
> >
> > **Paso 1:** comportamiento para $x \to \infty$: $f(x) = \frac{x^2+1}{x^4+x^2+1} \sim \frac{x^2}{x^4} = \frac{1}{x^2}$.
> >
> > **Paso 2:** con $g(x) = \frac{1}{x^2}$:
> > $$\lim_{x \to \infty} \frac{f(x)}{g(x)} = \lim_{x \to \infty} \frac{x^2(x^2+1)}{x^4+x^2+1} = 1$$
> >
> > **Paso 3:** como $0 < 1 < \infty$ y $\int_1^{\infty} \frac{1}{x^2}\,dx = 1$ converge, ambas se comportan igual.
> >
> > **Respuesta:** la integral **converge** ✓ (sin calcular su valor).

> [!example] 📋 Planteamiento
>
> Determina la convergencia de $\int_0^1 \frac{\sin x}{\sqrt{x}}\,dx$ por comparación directa.
>
> > [!success]- ✅ Solución
> >
> > **Análisis cerca de $x = 0$:** como $\sin x \sim x$ cuando $x \to 0^+$, vale $\frac{\sin x}{\sqrt{x}} \sim \frac{x}{\sqrt{x}} = \sqrt{x}$.
> >
> > **Desigualdad:** para $x \in (0,1]$, $0 \leq \sin x \leq x$ implica $0 \leq \frac{\sin x}{\sqrt{x}} \leq \sqrt{x}$.
> >
> > **Referencia:** $\int_0^1 \sqrt{x}\,dx = \int_0^1 x^{1/2}\,dx = \frac{2}{3}$ converge.
> >
> > **Respuesta:** por comparación directa, la integral **converge** ✓ (y es $\leq 2/3$).

> [!example] 📋 Planteamiento
>
> Analiza $\int_2^{\infty} \frac{1}{x \ln x}\,dx$ aplicando el método COMPAR.
>
> > [!success]- ✅ Solución
> >
> > **C — Comparar:** problema en el infinito, comportamiento $\sim \frac{1}{x \ln x}$.
> >
> > **O — Ordenar:** candidatas $\frac{1}{x}$ (divergente) y $\frac{1}{x^2}$ (convergente).
> >
> > **M — Mayorar/minorar:** para $x \geq 2$, $\ln x \geq \ln 2 > 0$, así que $\frac{1}{x\ln x} \leq \frac{1}{x \ln 2}$ — pero esa mayorante **diverge**, así que no prueba convergencia.
> >
> > **P — Probar la referencia (límite):** $\lim_{x \to \infty} \frac{1/(x\ln x)}{1/x} = \frac{1}{\ln x} \to 0$. Con $L = 0$ y $\int_2^{\infty} \frac{1}{x}$ **divergente**, el criterio **no decide**.
> >
> > **A — Aplicar el criterio correcto:** integrar directamente con $u = \ln x$:
> > $$\int_2^{\infty} \frac{1}{x \ln x}\,dx = \lim_{t \to \infty} \big[\ln(\ln x)\big]_2^t = \lim_{t \to \infty} \big(\ln(\ln t) - \ln(\ln 2)\big) = \infty$$
> >
> > **R — Revisar:** $L = 0$ con referencia divergente nunca concluye; el cálculo directo confirma la divergencia.
> >
> > **Respuesta:** la integral **diverge** ✓ — y la lección es que la comparación por límite con $L = 0$ no sirve para probar divergencia.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Aplico el teorema de comparación verificando que la desigualdad vale en todo el intervalo.
> - [ ] Uso la desigualdad triangular para acotar integrales que cambian de signo.
> - [ ] Estimo una integral con $m(b-a) \leq \int \leq M(b-a)$ sin llegar a integrar.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Elijo la función de referencia correcta según el régimen ($x \to \infty$ o $x \to a$) y la familia (potencia, exponencial, logarítmica).
> - [ ] Aplico el criterio por límite distinguiendo los casos $0 < L < \infty$, $L = 0$ y $L = \infty$, incluidos los que no deciden.
> - [ ] Decido convergencia de una impropia con comparación directa respetando el sentido de la desigualdad.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro el teorema de comparación a partir de la linealidad y la no negatividad de la integral.
> - [ ] Desarrollo el método COMPAR completo en un ejercicio con singularidades y justifico cada paso.
> - [ ] Acoto los coeficientes de una serie de Fourier con estas desigualdades para concluir convergencia.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 8.8: integrales impropias y teorema de comparación.
> - G. Strang, *Calculus* (Wellesley-Cambridge): desigualdades e integrales definidas.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — base algebraica de las desigualdades (aditividad y no negatividad).
> - [[Unidad 6 - Integrales/III - Integrales Definidas/03 - Teoremas Especiales para Integrales Definidas|03 - Teoremas Especiales para Integrales Definidas]] — acotaciones y teoremas auxiliares.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/01 - Integral de Riemann|01 - Integral de Riemann]] — la definición que hace posible la desigualdad.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/04 - Teorema Fundamental del Cálculo|04 - Teorema Fundamental del Cálculo]] — la vía de evaluación exacta cuando existe.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — la aplicación principal de estos teoremas.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u6

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué dice el teorema de comparación?::Si $f(x) \leq g(x)$ en $[a,b]$ y ambas son integrables, entonces $\int_a^b f \leq \int_a^b g$; la demostración usa $h = g - f \geq 0$ y la linealidad.
> - ¿Qué afirma la desigualdad triangular?::$\left|\int_a^b f\right| \leq \int_a^b |f|$: el valor absoluto de la integral está acotado por la integral del valor absoluto; es el paso previo cuando $f$ cambia de signo.
> - ¿Cómo acotas con constantes?::Si $m \leq f \leq M$ en $[a,b]$, entonces $m(b-a) \leq \int_a^b f \leq M(b-a)$.
> - ¿Cuándo conviene la comparación directa y cuándo la por límite?::Directa si **se ve** la desigualdad $0 \leq f \leq g$; por límite si solo se ven los grados dominantes con $\lim f/g = L \in (0,\infty)$.
> - ¿Qué cuidado tienen los casos $L = 0$ y $L = \infty$?::Solo concluyen en un sentido: $L = 0$ con $\int g$ convergente implica convergencia de $\int f$; $L = \infty$ con $\int g$ divergente implica divergencia. Los cruces restantes no deciden.
> - ¿Por qué $\int_2^{\infty} \frac{1}{x\ln x}$ no converge por límite con $1/x$?::Porque el límite es $0$ y la referencia diverge: ese cruce no concluye. Directamente, $\int \frac{1}{x\ln x} = \ln(\ln x) \to \infty$, así que diverge.
> - ¿Qué hago primero con una función que cambia de signo?::Desigualdad triangular: acotar $\left|\int f\right| \leq \int |f|$ y comparar la versión positiva.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — dónde se aplican estos teoremas para decidir convergencia.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|02 - Criterios de Convergencia y Divergencia]] — los criterios completos que estas desigualdades sostienen.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/04 - Asíntotas en Integrales Definidas|04 - Asíntotas en Integrales Definidas]] — las discontinuidades que obligan a partir el intervalo antes de comparar.
> - [[Unidad 6 - Integrales/I - Fundamentos Teóricos/02 - Propiedades de la Integral|02 - Propiedades de la Integral]] — aditividad y no negatividad, las dos hipótesis que se usan en la demostración.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — el límite con el que se decide el criterio por límite.
> - [[Unidad 7 - Aplicaciones de la Integral/I - Áreas/01 - Área bajo la Curva|01 - Área bajo la Curva]] — la interpretación geométrica de todo lo anterior.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Practica primero los ejercicios 1, 2 y 3: son las tres formas de acotar (desigualdad, constantes y valor absoluto), el esqueleto de todo lo demás.
> - Después pasa al 4 y al 5, donde entran el criterio por límite y la comparación directa en una singularidad.
> - Cierra con el 6, el caso donde la comparación **no** decide y hay que recurrir al cálculo directo.
> - Cuando lo tengas, continúa con [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/02 - Criterios de Convergencia y Divergencia|Criterios de Convergencia y Divergencia]] para ver todos estos criterios aplicados a series; como siguiente horizonte, las desigualdades clásicas (Cauchy–Schwarz, Hölder) del análisis real.

---

**Tags:** #MATG1045 #unidad6 #teoremas-de-comparacion-y-desigualdades #comparacion #desigualdades #convergencia #integrales-definidas #integrales-impropias #estimacion #acotacion #analisis
