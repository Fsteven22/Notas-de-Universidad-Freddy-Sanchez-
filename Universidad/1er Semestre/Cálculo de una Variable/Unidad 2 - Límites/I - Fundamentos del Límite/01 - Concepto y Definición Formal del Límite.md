---
dg-publish: true
tags: [MATG1045, unidad2, limite, epsilon-delta, limites-laterales, limites-infinitos, limites-al-infinito, asintotas, demostraciones]
---

# 🤓 Concepto y Definición Formal del Límite

## 🎯 Introducción

> [!info] 💡 ¿Qué quiere decir "límite"?
>
> Un **límite** describe hacia dónde se dirige una función cuando la variable independiente se acerca a un valor específico, **sin necesitar llegar a ese valor**. Es observar hacia dónde camina una persona, no dónde está parada.
>
> Ese matiz es la que sostiene toda la nota: el límite no pide que la función esté definida en el punto ni que valga algo ahí. Pide que los valores de $f(x)$ se acerquen arbitrariamente a un número $L$ conforme $x$ se acerca a $a$ por el dominio.
>
> **Notación:** $\lim_{x \to a} f(x) = L$.
>
> **Ejemplo:** con $g(x)=x^2$ para $x\neq2$ y $g(2)=10$, el límite en $2$ sigue siendo $4$: el recorrido de $x$ es el mismo aunque el valor fijo sea otro.

> [!warning] ⚠️ Lo que NO es un límite
>
> - **NO hace falta** que $f(a)$ exista.
> - **NO importa** el valor de $f(a)$ si existe.
> - **NO hace falta** que $x$ llegue exactamente a $a$.
>
> Y lo que sí importa:
>
> - **SÍ importa** hacia dónde tienden los valores de $f(x)$.
> - **SÍ hace falta** que $x$ se acerque a $a$ por el dominio.
> - **SÍ debe existir** un valor al que se acercan $f(x)$, o al menos una tendencia bien definida.

> [!tip] 🔢 Aproximación por tablas de valores
>
> Cuando el límite no se resuelve por reglas, una tabla lo descubre:
>
> 1. **Crear tabla:** valores de $x$ acercándose a $a$ por ambos lados.
> 2. **Calcular:** los valores correspondientes de $f(x)$.
> 3. **Observar:** hacia qué valor tienden.
> 4. **Concluir:** ese es el límite, si existe.
>
> | $x$ acercándose a $3$ | $f(x)=2x+1$ |
> |---|---|
> | $2.9$ | $6.8$ |
> | $2.99$ | $6.98$ |
> | $2.999$ | $6.998$ |
> | $3.001$ | $7.002$ |
> | $3.01$ | $7.02$ |
> | $3.1$ | $7.2$ |
>
> **Por qué importa:** la tabla es solo una pista, nunca una prueba. En el caso de $\lim_{x \to 0} \frac{\sin x}{x}$ la tabla sugiere $1$, pero el valor se demuestra aparte.
>
> **Ejemplo:** para $\lim_{x \to 0} \frac{\sin x}{x}$ los valores van de $0.998334$ a $0.999999$ por ambos lados, con $\frac{\sin x}{x}\to 1$.

> [!info] 📝 El mismo enunciado, cinco formas
>
> Todas dicen lo mismo:
>
> - $\lim_{x \to a} f(x) = L$
> - "El límite de $f(x)$ cuando $x$ tiende a $a$ es $L$"
> - "Cuando $x$ se acerca a $a$, $f(x)$ se acerca a $L$"
> - "$f(x)$ tiende a $L$ cuando $x$ tiende a $a$"
> - "$f(x) \to L$ cuando $x \to a$"

> [!tip] 🎓 Mnemotecnia "CERCA"
>
> - **C**ercanos: los valores de $x$ están cerca de $a$.
> - **E**xacto: no hace falta llegar exactamente a $a$.
> - **R**esultado: los valores de $f(x)$ se acercan a un resultado $L$.
> - **C**onvergencia: los valores deben converger a $L$.
> - **A**proximación: es sobre aproximarse, no sobre llegar.

---

## 📋 Definiciones Formales

> [!note] 📋 Definición — Límite (sentido intuitivo)
>
> Decimos que el **límite de $f(x)$ cuando $x$ se acerca a $a$ es $L$** si los valores de $f(x)$ se acercan arbitrariamente a $L$ cuando $x$ toma valores cada vez más cercanos a $a$ y diferentes de $a$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_01.svg]]
>
> **Se lee así:** el diagrama es una cadena de cuatro rectángulos unidos por flechas, sin rombos: el primero marca el acercamiento de $x$ al punto, el segundo es el cálculo de $f(x)$, el tercero registra la aproximación de los valores y el cuarto cierra con el límite ya fijado. Al no haber decisiones, el camino es único.
>
> **Por qué importa:** la secuencia separa el movimiento de $x$ del movimiento de $f(x)$. Eso deja claro que $x$ nunca tiene que llegar al punto y que lo que importa es el valor al que se acerca la salida. Te ahorra el error de sustituir $x=a$ cuando la función no está definida ahí.
>
> **Ejemplo:** para $g(x)=x^2$ con $g(2)=10$, el límite en $2$ sigue siendo $4$: el valor fijo del punto no entra en la definición.

> [!note] 📋 Definición — Límite (formal $\varepsilon$-$\delta$)
>
> Se dice que $\lim_{x \to a} f(x) = L$ si y solo si: **para todo $\varepsilon > 0$ existe un $\delta > 0$** tal que
>
> $$\text{si } 0 < |x - a| < \delta \text{ entonces } |f(x) - L| < \varepsilon.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_03.svg]]
>
> **Se lee así:** es una cadena de pasos encadenados: querer demostrar el límite, fijar un $\varepsilon > 0$ arbitrario, encontrar un $\delta > 0$ apropiado y verificar la condición. El último paso es un rombo que pregunta si se cumple para todo $\varepsilon$, y de él salen dos flechas rotuladas: una hacia la demostración lograda y otra hacia el fallo de la afirmación.
>
> **Por qué importa:** este es el guion exacto de una demostración $\varepsilon$-$\delta$. Primero la tolerancia arbitraria y después el radio, nunca al revés. Seguirlo evita el error típico de elegir un $\delta$ que dependa de $x$ o de asumir el resultado que quieres probar.
>
> **Ejemplo:** para demostrar $\lim_{x \to 3} (2x + 1) = 7$ se toma $\varepsilon > 0$ arbitrario, se calcula $|f(x) - L| = 2|x - 3|$ y se elige $\delta = \varepsilon/2$.

> [!note] 📋 Definición — Límite por la izquierda
>
> Se dice que $\lim_{x \to a^-} f(x) = L$ si para todo $\varepsilon > 0$ existe $\delta > 0$ tal que
>
> $$\text{si } a - \delta < x < a \text{ entonces } |f(x) - L| < \varepsilon.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_09.svg]]
>
> **Se lee así:** el esquema arranca en el acercamiento por la izquierda, luego fija un $\varepsilon > 0$ y busca un $\delta > 0$; con el radio en mano toma los $x$ que cumplen $a - \delta < x < a$, comprueba que la distancia vertical de $f(x)$ a $L$ queda por debajo de $\varepsilon$ y concluye que el límite izquierdo es $L$.
>
> **Por qué importa:** solo cambia la condición sobre $x$: la banda vertical es unilateral. Es la que permite decidir si un límite existe y, sobre todo, detectar saltos, que son la diferencia entre una asíntota vertical con salto y una simple.
>
> **Ejemplo:** $\lim_{x \to 1^-} \frac{1}{x-1} = -\infty$: basta con que $x$ esté por debajo de $1$ y cercana a $1$.

> [!note] 📋 Definición — Límite por la derecha
>
> Se dice que $\lim_{x \to a^+} f(x) = L$ si para todo $\varepsilon > 0$ existe $\delta > 0$ tal que
>
> $$\text{si } a < x < a + \delta \text{ entonces } |f(x) - L| < \varepsilon.$$
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_10.svg]]
>
> **Se lee así:** el esquema es el espejo del anterior: el acercamiento es por la derecha, se fija $\varepsilon > 0$, se busca $\delta > 0$, se toman los $x$ con $a < x < a + \delta$ y se comprueba que $f(x)$ cae dentro de la banda de $\varepsilon$.
>
> **Por qué importa:** la condición sobre $x$ se escribe del lado contrario al de la izquierda. Cometer ese intercambio es el error que hace pasar por alto un límite que sí existe.
>
> **Ejemplo:** $\lim_{x \to 2^+} \frac{1}{x-2} = +\infty$: con $x$ justo a la derecha de $2$ el denominador es positivo y pequeño.

> [!note] 📋 Definición — Límite (existencia y unicidad)
>
> El límite existe cuando los dos laterales convergen al mismo número: $\lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x) = L$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_12.svg]]
>
> **Se lee así:** el esquema parte de un límite supuesto $L_1$, fija $\varepsilon$ como la mitad de la distancia entre $L_1$ y $L_2$ y hace que $f(x)$ deba estar cerca de $L_1$ y a la vez cerca de $L_2$ cerca de $a$. El rombo pregunta si las dos tolerancias son incompatibles: si lo son, la conclusión es que $L_1 = L_2$.
>
> **Por qué importa:** la unicidad no es un lujo: si existieran dos valores distintos, una misma bola de $\varepsilon$ sería imposible de cumplir. Así se justifica que buscar el límite sea razonable y que el método del emparedado no dé resultados contradictorios.
>
> **Ejemplo:** $\lim_{x \to 1} \frac{x^2-1}{x-1}$ vale $2$, no $0$ ni $3$: hay un solo valor posible, $2$.

> [!note] 📋 Definición — Límite infinito
>
> Se dice que $\lim_{x \to a} f(x) = +\infty$ si para todo $M > 0$ existe $\delta > 0$ tal que
>
> $$\text{si } 0 < |x - a| < \delta \text{ entonces } f(x) > M.$$
>
> Con $f(x) < -M$ en la desigualdad se define $\lim_{x \to a} f(x) = -\infty$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_05.svg]]
>
> **Se lee así:** el diagrama parte de que $x$ se acerca a $a$ y pasa por un rombo que separa según la tendencia de la función: hacia $+\infty$ o hacia $-\infty$. Cada rama repite la misma secuencia lógica: un $M > 0$ arbitrario, un $\delta > 0$ que lo garantiza y la desigualdad que se exige dentro de la franja; las dos vuelven a juntarse en la casilla de **asíntota vertical**.
>
> **Por qué importa:** aquí el papel del $\varepsilon$ lo juega un $M$ grande y arbitrario, y la condición es una desigualdad sin valor absoluto. Es el motivo del error más común de esta sección: escribir $f(x) > -M$ cuando el límite es $-\infty$, donde corresponde $f(x) < -M$.
>
> **Ejemplo:** para $\lim_{x \to 0^+} \frac{1}{x} = +\infty$ se elige $\delta = 1/M$ y se cumple que $0 < x < \delta$ implica $\frac{1}{x} > M$ para todo $M > 0$.

> [!note] 📋 Definición — Límite lateral infinito
>
> Se dice que $\lim_{x \to a^+} f(x) = +\infty$ si para todo $M > 0$ existe $\delta > 0$ tal que
>
> $$\text{si } a < x < a + \delta \text{ entonces } f(x) > M.$$
>
> En $\lim_{x \to a^-} f(x) = +\infty$ la condición se sustituye por $a - \delta < x < a$. Existe una asíntota vertical cuando al menos uno de los límites laterales es infinito.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_07.svg]]
>
> **Se lee así:** el esquema arranca en el acercamiento por un solo lado y pasa por un rombo sobre la dirección: por la derecha queda la condición $a < x < a + \delta$ y por la izquierda $a - \delta < x < a$. Las dos ramas se juntan en una sola exigencia, para todo $M > 0$ con $f(x) > M$ o $f(x) < -M$, y cierran en la conclusión de límite lateral infinito.
>
> **Por qué importa:** una vertical puede nacer de un solo lado. Por eso un salto con infinitos opuestos no se describe como "asíntota vertical simple" sino como vertical con salto, y porque una discontinuidad evitable no genera asíntota.
>
> **Ejemplo:** $\lim_{x \to 1^-} \frac{1}{x-1} = -\infty$ y $\lim_{x \to 1^+} \frac{1}{x-1} = +\infty$: $x=1$ es asíntota vertical aunque los laterales signen distinto.

> [!note] 📋 Definición — Límite al infinito
>
> Se dice que $\lim_{x \to +\infty} f(x) = L$ si para todo $\varepsilon > 0$ existe $N > 0$ tal que
>
> $$\text{si } x > N \text{ entonces } |f(x) - L| < \varepsilon.$$
>
> En $\lim_{x \to -\infty} f(x) = L$ la condición se sustituye por $x < -N$ con $N > 0$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_06.svg]]
>
> **Se lee así:** el esquema arranca con $x$ tendiendo a infinito y pasa por un rombo sobre la dirección, hacia $+\infty$ o hacia $-\infty$. Cada lado repite el patrón formal con un $\varepsilon > 0$ arbitrario, un $N > 0$ que lo acompaña y la condición sobre $x$ mayor que $N$ o menor que $-N$; las dos ramas concluyen en la misma casilla de **asíntota horizontal $y = L$**.
>
> **Por qué importa:** cuando $x$ se va al infinito el $\delta$ ya no sirve: ese papel lo cumple $N$, y como el límite sigue siendo finito se mantiene $\varepsilon$ como tolerancia. Evita mezclar $M$ con $N$ y muestra que la asíntota horizontal no depende del lado.
>
> **Ejemplo:** para $\lim_{x \to +\infty} \frac{2x+1}{x+3} = 2$ se simplifica la diferencia a $\frac{5}{x+3}$ y se toma como umbral $N = \max\{\frac{5}{\varepsilon} - 3,\, 1\}$, para que $x+3$ sea positivo.

> [!note] 📋 Definición — Límite infinito al infinito
>
> Se dice que $\lim_{x \to +\infty} f(x) = +\infty$ si para todo $M > 0$ existe $N > 0$ tal que
>
> $$\text{si } x > N \text{ entonces } f(x) > M.$$
>
> Las otras tres variantes se escriben cambiando $M$ por $-M$ en la conclusión, o $x > N$ por $x < -N$.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_08.svg]]
>
> **Se lee así:** el esquema arranca en $x$ creciendo sin cota y pasa por un rombo que separa las cuatro combinaciones posibles: dirección de $x$ ($+\infty$ o $-\infty$) y signo de $f(x)$ ($+\infty$ o $-\infty$). Cada rama lleva su condición de umbral, $x > N$ implica $f(x) > M$ o $f(x) < -M$, y las cuatro desembocan en la misma conclusión de límite infinito al infinito.
>
> **Por qué importa:** es la mezcla de las dos definiciones anteriores: el umbral $N$ gobierna el crecimiento de $x$ y el número $M$ gobierna el crecimiento de $f(x)$. Por eso el caso $\lim_{x \to +\infty} \frac{1}{x} = 0$ se resuelve con $\varepsilon$ y $N$, y el caso $\lim_{x \to +\infty} x^2 = +\infty$ con $M$ y $N$.
>
> **Ejemplo:** $\lim_{x \to +\infty} x^2 = +\infty$ se cumple tomando $N = \sqrt{M}$: si $x > N$ entonces $x^2 > M$.

---

## 📐 Interpretación Geométrica y Método de Demostración

> [!example] 🎨 Las dos bandas de la definición
>
> La definición $\varepsilon$-$\delta$ se traduce en:
>
> - **Banda horizontal:** $L - \varepsilon < f(x) < L + \varepsilon$
> - **Banda vertical:** $a - \delta < x < a + \delta$ (excluyendo $x = a$)
> - **Condición:** toda la función en la banda vertical debe quedar dentro de la banda horizontal
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_04.svg]]
>
> **Se lee así:** el esquema arranca en un punto, el par $(a, L)$, del que salen dos ramas paralelas: una banda horizontal de tolerancia $\varepsilon$ alrededor de $L$ y una banda vertical de alcance $\delta$ alrededor de $a$. La rama vertical exige que toda $x$ dentro de la franja cumpla la condición y la horizontal que $f(x)$ quede dentro; ambas desembocan en la misma casilla de **definición satisfecha**.
>
> **Por qué importa:** las dos bandas se cruzan en un mismo punto: la vertical te dice dónde mirar y la horizontal qué tan cerca debes quedar. Es la lectura geométrica de $0 < |x - a| < \delta$ y $|f(x) - L| < \varepsilon$, y con ella justificas el $\delta$ que eliges.
>
> **Ejemplo:** para $\lim_{x \to 2} x^2 = 4$ la banda de $\delta$ alrededor de $2$ debe ser tan angosta que toda la curva dentro de ella quede dentro de la banda de $\varepsilon$ alrededor de $4$, y el trabajo da $\delta = \min\{1, \varepsilon/5\}$.
>
> | Elemento | Significado geométrico | Representación |
> |---|---|---|
> | $\varepsilon$ | Mitad del ancho de la banda horizontal | $\pm \varepsilon$ alrededor de $L$ |
> | $\delta$ | Mitad del ancho de la banda vertical | $\pm \delta$ alrededor de $a$ |
> | $\|f(x) - L\|$ | Distancia vertical entre $f(x)$ y $L$ | Altura desde la función al límite |
> | $\|x - a\|$ | Distancia horizontal entre $x$ y $a$ | Distancia desde $x$ al punto de interés |

> [!info] 📈 Cómo se lee el límite en una gráfica
>
> En una gráfica, el límite se ve como:
>
> - **Observamos** hacia dónde apunta la función cuando nos acercamos al punto.
> - **No importa** si hay un "hueco" o un "salto" en ese punto exacto.
> - **Importa** la tendencia o la dirección de la función.
>
> ![[../../Unidad 0 - Guias y Ejercicios/Diagramas/01_-_Concepto_y_Definición_Formal_del_Límite_02.svg]]
>
> **Se lee así:** arriba está la caja con la gráfica de $f(x)$, que baja a un rombo de decisión con la pregunta central: hacia dónde apunta la curva cuando $x$ se acerca a $a$. Del rombo salen tres ramas: una a un valor concreto, otra a un crecimiento sin cota y una tercera a que no hay convergencia; cada rama baja a su propio casillero de veredicto, con el límite finito, el límite infinito o la falta de límite.
>
> **Por qué importa:** el diagrama separa de entrada tres resultados muy distintos: un valor concreto, un crecimiento sin cota o la ausencia de límite. Te evita decir "no existe" cuando la función simplemente se va a infinito y te obliga a mirar la gráfica antes de calcular.
>
> **Ejemplo:** $\lim_{x \to 0} \frac{1}{x^2} = +\infty$ da asíntota vertical, mientras que $\lim_{x \to 2} \frac{1}{x-2}$ no existe porque sus límites laterales son opuestos.

> [!note] 📚 Los cuatro casos típicos
>
> - **Función continua:** $\lim_{x \to a} f(x) = f(a)$. No tiene interrupciones y el límite coincide con el valor de la función.
> - **Función con hueco:** $\lim_{x \to a} f(x) = L$, pero $f(a)$ no existe. Hay un punto faltante en la gráfica.
> - **Función con salto:** $\lim_{x \to a} f(x)$ no existe. La función salta de un valor a otro y los límites laterales son distintos.
> - **Límite infinito:** $\lim_{x \to a} f(x) = \pm\infty$. La función crece sin límite y hay asíntota vertical.
>
> **Por qué importa:** estos cuatro casos son los que una función real puede presentar y cada uno lleva una respuesta distinta. Identificarlos antes de calcular evita el error de dar por perdido un límite que sí existe.
>
> **Ejemplo:** la función escalón $f(x) = \begin{cases} 0 & \text{si } x < 0 \\ 1 & \text{si } x \geq 0 \end{cases}$ está en el caso de salto: el límite en $0$ no existe, aunque $f(0)=1$.

> [!tip] 📝 Cómo se demuestra un límite
>
> 1. **Configuración inicial:** sea $\varepsilon > 0$ arbitrario; queremos encontrar $\delta > 0$ tal que la implicación se cumpla.
> 2. **Análisis algebraico:** partir de $|f(x) - L| < \varepsilon$ y manipular para obtener una condición en $|x - a|$.
> 3. **Elección de $\delta$:** identificar qué $\delta$ funciona, casi siempre como mínimo de varias restricciones.
> 4. **Verificación:** asumir $0 < |x - a| < \delta$ y demostrar que esto implica $|f(x) - L| < \varepsilon$.
>
> **Por qué importa:** el orden importa tanto como el cálculo: primero la tolerancia arbitraria y luego el radio. Si inviertes el orden acabas asumiendo lo que quieres probar.
>
> **Ejemplo:** en el ejemplo 2 de los ejercicios, $\lim_{x \to 2} x^2 = 4$, la restricción preliminar $|x - 2| < 1$ es lo que permite acotar $|x + 2| < 5$ y fijar $\delta = \min\{1, \varepsilon/5\}$.

> [!warning] ⚠️ Condiciones que no se pueden saltar
>
> - **$0 < |x - a|$:** excluimos $x = a$, porque no nos importa $f(a)$.
> - **$x \neq a$:** la función puede no estar definida en $a$.
> - **$\varepsilon > 0$:** solo consideramos tolerancias positivas.
> - **$\delta > 0$:** solo consideramos rangos positivos.
>
> **Por qué importa:** la desigualdad estricta del lado izquierdo es la que hace que el límite no dependa del valor de la función en el punto. Quitarla convierte la definición en un teorema de continuidad.
>
> **Ejemplo:** para $\lim_{x \to 1} \frac{x^2 - 1}{x - 1}$ la función no está definida en $1$, y aun así el límite existe y vale $2$.

> [!tip] 🎓 Mnemotecnia "ÉPSILON"
>
> - **É**lige un $\varepsilon$ arbitrario mayor que $0$.
> - **P**artes de la condición $|f(x) - L| < \varepsilon$.
> - **S**implificas algebraicamente la expresión.
> - **I**dentificas la relación con $|x - a|$.
> - **L**logras una condición de la forma $|x - a| < \text{algo}$.
> - **O**ptimizas eligiendo $\delta$ apropiado.
> - **N**avegas la verificación final.

---

## ⚠️ Errores y Trampas Frecuentes

> [!warning] 🚨 Trampas conceptuales
>
> - **Confundir límite con valor de función.** "Si $f(2) = 5$, entonces $\lim_{x \to 2} f(x) = 5$" es incorrecto: el límite puede ser distinto.
> - **Pensar que el límite requiere que la función esté definida.** "No puedo hallar el límite si la función no existe en ese punto" es incorrecto: el límite puede existir igual.
> - **Usar solo un lado.** Mirar valores desde la derecha o desde la izquierda basta para engañarse; hay que verificar ambos lados para asegurar convergencia.
>
> **Por qué importa:** los tres errores son de concepto, no de cálculo, y ninguno se detecta revisando la aritmética. Se detectan volviendo a la definición.
>
> **Ejemplo:** en $g(x)=x^2$ para $x\neq2$ y $g(2)=10$, el límite en $2$ vale $4$ y no $10$: el valor fijo es irrelevante.

> [!warning] 🚫 Errores en demostraciones $\varepsilon$-$\delta$
>
> - **$\delta$ dependiente de $x$:** el radio solo puede depender de $\varepsilon$ y de los datos del problema ($a$, $L$), nunca de la variable.
> - **Asumir el resultado:** empezar asumiendo $|f(x) - L| < \varepsilon$ no demuestra nada; hay que partir de la condición de $\delta$.
> - **No manejar casos extremos:** faltan restricciones de dominio o acotaciones temporales; usa $\min$ para combinarlas.
> - **Confundir $M$ con $N$:** $M$ es para $f(x)$, $N$ es para $x$.
> - **Signos en límites negativos:** para $-\infty$ corresponde $f(x) < -M$, no $f(x) > -M$.
> - **Invertir desigualdades:** al multiplicar por un número negativo cambia el sentido.
>
> **Por qué importa:** los primeros tres rompen la lógica de la demostración; los últimos tres la invalidan por aritmética. Revisarlos antes de dar por cerrado un ejercicio es más barato que corregirlo después.
>
> **Ejemplo:** para $\lim_{x \to 0^+} \frac{1}{x} = +\infty$, el error clásico es proponer $\delta = M$; el correcto es $\delta = 1/M$.

> [!info] 🏛️ Contexto histórico
>
> - **Bernard Bolzano (1781-1848):** primeras contribuciones sobre la idea de límite.
> - **Augustin-Louis Cauchy (1789-1857):** primera definición rigurosa de límite en su *Cours d'Analyse* (1821).
> - **Karl Weierstrass (1815-1897):** formalización $\varepsilon$-$\delta$ tal como se usa hoy.
>
> **Por qué importa:** la definición formal elimina la vaguedad de la intuición y permite demostraciones rigurosas. Es la base de la continuidad, la derivabilidad y la integrabilidad.
>
> **Ejemplo:** el concepto de convergencia de sucesiones que se usa en Cálculo 1 nace de esta formalización.

---

## ♾️ Límites Infinitos y Asíntotas

> [!note] 📋 Tabla resumen de las seis variantes
>
> | Tipo de límite | Notación | Condición | Parámetros |
> |---|---|---|---|
> | **Finito $\to$ finito** | $\lim_{x \to a} f(x) = L$ | $\|f(x) - L\| < \varepsilon$ cuando $0 < \|x - a\| < \delta$ | $\varepsilon, \delta$ |
> | **Finito $\to$ $+\infty$** | $\lim_{x \to a} f(x) = +\infty$ | $f(x) > M$ cuando $0 < \|x - a\| < \delta$ | $M, \delta$ |
> | **Finito $\to$ $-\infty$** | $\lim_{x \to a} f(x) = -\infty$ | $f(x) < -M$ cuando $0 < \|x - a\| < \delta$ | $M, \delta$ |
> | **$+\infty$ $\to$ finito** | $\lim_{x \to +\infty} f(x) = L$ | $\|f(x) - L\| < \varepsilon$ cuando $x > N$ | $\varepsilon, N$ |
> | **$-\infty$ $\to$ finito** | $\lim_{x \to -\infty} f(x) = L$ | $\|f(x) - L\| < \varepsilon$ cuando $x < -N$ | $\varepsilon, N$ |
> | **$+\infty$ $\to$ $+\infty$** | $\lim_{x \to +\infty} f(x) = +\infty$ | $f(x) > M$ cuando $x > N$ | $M, N$ |
>
> **Por qué importa:** la tabla resume en una sola página la decisión más importante de la nota: qué letra tocar según el caso. Es lo que separa una demostración bien planteada de una que se atasca.
>
> **Ejemplo:** $\lim_{x \to +\infty} \frac{2x+1}{x+3} = 2$ es la cuarta fila; $\lim_{x \to 0^+} \frac{1}{x} = +\infty$, la segunda.

> [!tip] 🎓 Método "EMDN"
>
> - **E**líge la definición correcta.
> - **M** o **N** según el tipo de límite.
> - **D**elta para límites en puntos finitos.
> - **N**úmero grande para límites al infinito.
>
> **Frase nemotécnica:** "Escojo Métodos Definidos Numéricamente".
>
> **Guía de decisión:**
>
> - Si $x \to a$ (finito) $\rightarrow$ usar $\delta$.
> - Si $x \to \pm\infty$ $\rightarrow$ usar $N$.
> - Si $f(x) \to \pm\infty$ $\rightarrow$ usar $M$.
> - Si $f(x) \to L$ (finito) $\rightarrow$ usar $\varepsilon$.

> [!success] 🎯 Cómo encontrar asíntotas: el algoritmo
>
> **Asíntotas verticales:**
>
> 1. Buscar puntos donde $f(x)$ no está definida.
> 2. Calcular los límites laterales usando las definiciones formales.
> 3. Si algún límite lateral es $\pm\infty$, hay asíntota vertical.
>
> **Asíntotas horizontales:**
>
> 4. Calcular $\lim_{x \to +\infty} f(x)$ y $\lim_{x \to -\infty} f(x)$.
> 5. Si alguno es finito, hay asíntota horizontal.
> 6. Usar las definiciones formales para demostrarlo.
>
> **Por qué importa:** el algoritmo evita la tentación de "mirar" la gráfica y adivinar. En exámenes como el de 2021 (Tema # 2, preguntas 6 a 10) la asíntota se pide encontrando el parámetro con los límites, no por inspección.
>
> **Ejemplo:** para $f(x) = \frac{2x + 3}{x - 1}$ la vertical es $x = 1$ y la horizontal $y = 2$.

> [!note] 📋 Casos especiales y situaciones particulares
>
> - **Límites laterales infinitos:** modificar la condición a $0 < x - a < \delta$ (derecha) o $0 < a - x < \delta$ (izquierda).
> - **Funciones racionales:** factorizar numerador y denominador e identificar el comportamiento dominante.
> - **Funciones con raíces:** considerar restricciones de dominio y usar propiedades de radicales.
> - **Composición de funciones:** aplicar las definiciones en cascada y verificar la continuidad en los puntos intermedios.
>
> **Por qué importa:** en los cuatro casos la definición sigue siendo la misma, pero el $\delta$ o el $N$ se eligen de forma distinta. Reconocer el patrón evita perder tiempo en demostraciones que no avanzan.
>
> **Ejemplo:** $\lim_{x \to +\infty} \frac{3x^2 + 1}{x^2 - 5} = 3$ se resuelve con el caso "$+\infty \to$ finito" y $N = \max\{3/\varepsilon, 1\}$.

---

## 📝 Ejercicios Propuestos

> [!example] 📋 Planteamiento
>
> Demostra, usando la definición formal, que $\lim_{x \to 3} (2x + 1) = 7$.
>
> > [!success]- ✅ Solución
> >
> > Sea $\varepsilon > 0$ arbitrario. Como $|(2x+1) - 7| = |2x - 6| = 2|x - 3|$, basta con exigir $2|x - 3| < \varepsilon$, es decir $|x - 3| < \varepsilon/2$. Tomamos $\delta = \varepsilon/2 > 0$.
> >
> > Si $0 < |x - 3| < \delta = \varepsilon/2$, entonces $|f(x) - 7| = 2|x - 3| < 2 \cdot \frac{\varepsilon}{2} = \varepsilon$. Como $\varepsilon$ era arbitrario, queda demostrado que el límite es $7$.

> [!example] 📋 Planteamiento
>
> Demostra, usando la definición formal, que $\lim_{x \to 2} x^2 = 4$.
>
> > [!success]- ✅ Solución
> >
> > Sea $\varepsilon > 0$ arbitrario. Como $|x^2 - 4| = |(x-2)(x+2)| = |x - 2| \cdot |x + 2|$, acotamos el segundo factor. Supongamos $|x - 2| < 1$, entonces $1 < x < 3$ y por tanto $3 < x + 2 < 5$, así que $|x + 2| < 5$.
> >
> > Con esa acotación queda $|x^2 - 4| < 5|x - 2|$, que es menor que $\varepsilon$ siempre que $|x - 2| < \varepsilon/5$. Tomamos
> >
> > $$\delta = \min\left\{1, \frac{\varepsilon}{5}\right\}.$$
> >
> > Si $0 < |x - 2| < \delta$, entonces $|x - 2| < 1$ da $|x + 2| < 5$ y $|x - 2| < \varepsilon/5$ da $|x^2 - 4| < \frac{\varepsilon}{5} \cdot 5 = \varepsilon$.

> [!example] 📋 Planteamiento
>
> Demostra, usando la definición formal, que $\lim_{x \to 1} \frac{x^2 - 1}{x - 1} = 2$.
>
> > [!success]- ✅ Solución
> >
> > Para $x \neq 1$ la función se simplifica: $\frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1} = x + 1$. Entonces
> >
> > $$|f(x) - 2| = |(x + 1) - 2| = |x - 1|.$$
> >
> > Sea $\varepsilon > 0$ arbitrario y tomemos $\delta = \varepsilon$. Si $0 < |x - 1| < \delta = \varepsilon$, entonces $|f(x) - 2| = |x - 1| < \varepsilon$.
> >
> > **Nota:** el límite existe aunque la función no esté definida en $1$: la simplificación solo se usa fuera del punto.

> [!example] 📋 Planteamiento
>
> Demostra, usando la definición formal, que $\lim_{x \to 0^+} \frac{1}{x} = +\infty$.
>
> > [!success]- ✅ Solución
> >
> > Sea $M > 0$ arbitrario. Buscamos $\delta > 0$ tal que si $0 < x < \delta$ entonces $\frac{1}{x} > M$. Para $x > 0$, la desigualdad $\frac{1}{x} > M$ es equivalente a $x < \frac{1}{M}$. Tomamos $\delta = \frac{1}{M}$.
> >
> > Si $0 < x < \delta = \frac{1}{M}$, entonces $x < \frac{1}{M}$ y, invirtiendo con signo positivo, $\frac{1}{x} > M$. Como $M$ era arbitrario, el límite es $+\infty$.

> [!example] 📋 Planteamiento
>
> Demostra, usando la definición formal, que $\lim_{x \to +\infty} \frac{2x + 1}{x + 3} = 2$.
>
> > [!success]- ✅ Solución
> >
> > Sea $\varepsilon > 0$ arbitrario. Simplificamos la diferencia:
> >
> > $$\left|\frac{2x + 1}{x + 3} - 2\right| = \left|\frac{2x + 1 - 2x - 6}{x + 3}\right| = \frac{5}{x + 3},$$
> >
> > válido para $x + 3 > 0$, es decir $x > -3$. Queremos $\frac{5}{x + 3} < \varepsilon$, que equivale a $x + 3 > \frac{5}{\varepsilon}$, es decir $x > \frac{5}{\varepsilon} - 3$. Tomamos
> >
> > $$N = \max\left\{\frac{5}{\varepsilon} - 3,\ 1\right\}.$$
> >
> > Si $x > N$, entonces $x > \frac{5}{\varepsilon} - 3$ y, como $x + 3 > 0$,
> >
> > $$\left|\frac{2x + 1}{x + 3} - 2\right| = \frac{5}{x + 3} < \varepsilon.$$

> [!example] 📋 Planteamiento
>
> Demostra, usando la definición formal, que $\lim_{x \to +\infty} x^2 = +\infty$.
>
> > [!success]- ✅ Solución
> >
> > Sea $M > 0$ arbitrario. Buscamos $N > 0$ tal que si $x > N$ entonces $x^2 > M$. Como $x > N > 0$, la condición equivale a $x > \sqrt{M}$. Tomamos $N = \sqrt{M}$.
> >
> > Si $x > N = \sqrt{M}$, entonces $x > 0$ y al elevar al cuadrado se obtiene $x^2 > M$. Como $M$ era arbitrario, el límite es $+\infty$.

> [!example] 📋 Planteamiento
>
> Demuestra que $\lim_{x \to 2} \frac{1}{x - 2}$ no existe, y enuncia el criterio que lo justifica.
>
> > [!success]- ✅ Solución
> >
> > Por la derecha, con $x = 2 + t$ y $t > 0$ pequeño, $\frac{1}{x - 2} = \frac{1}{t} \to +\infty$. Por la izquierda, con $x = 2 - t$ y $t > 0$ pequeño, $\frac{1}{x - 2} = -\frac{1}{t} \to -\infty$.
> >
> > Los dos laterales no son finitos ni coinciden: uno va a $+\infty$ y el otro a $-\infty$. Como $\lim_{x \to 2^-} f(x) \neq \lim_{x \to 2^+} f(x)$, el límite no existe.
> >
> > **Criterio general:** el límite existe si y solo si los dos laterales existen, son finitos e iguales; si los laterales divergen de forma opuesta, la función no tiene límite en ese punto.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Defino qué es un límite y en qué se diferencia del valor de una función.
> - [ ] Escribo y leo la notación $\lim_{x \to a} f(x) = L$ y la entiendo en cinco formas equivalentes.
> - [ ] Identifico los cuatro casos típicos: continua, con hueco, con salto y límite infinito.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Escribo la definición formal $\varepsilon$-$\delta$ y sé qué papel juega cada parámetro.
> - [ ] Demuestro límites simples de funciones lineales y cuadráticas con la definición formal.
> - [ ] Distinguo $M$, $N$, $\delta$ y $\varepsilon$ y aplico el método EMDN para elegir definición.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro que un límite no existe usando laterales opuestos.
> - [ ] Conecto el límite infinito y el límite al infinito con las asíntotas verticales y horizontales.
> - [ ] Identifico las trampas habituales de una demostración $\varepsilon$-$\delta$ antes de dar el resultado por bueno.

---

## 📚 Referencias

> [!quote] 📖 Fuentes y material de la casa
>
> - J. Stewart, *Cálculo* (Cengage), cap. 2: el límite y su definición formal.
> - R. Larson, *Cálculo* (Cengage), cap. 1: límites y su demostración.
> - T. Apostol, *Calculus, Vol. 1* (Wiley), cap. 3: construcción analítica del límite.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — álgebra de límites y límites directos.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — extensión unilateral del concepto.
> - [[Unidad 3 - Aplicaciones de Límites/01 - Continuidad y Límites|01 - Continuidad y Límites]] — aplicación directa de la definición.

---

## 🔁 Repaso SR (flashcards)

#flashcards/cal1-u2

> [!note] 🧠 Repasa con el plugin Spaced Repetition
>
> - ¿Qué significa $\lim_{x \to a} f(x) = L$ y qué NO exige?::Que para todo $\varepsilon > 0$ existe $\delta > 0$ tal que $0 < |x - a| < \delta$ implica $|f(x) - L| < \varepsilon$. No exige que $f$ esté definida en $a$ ni que $f(a) = L$.
> - ¿Qué papel juega $\varepsilon$ y cuál $\delta$?::$\varepsilon$ es la tolerancia sobre la salida y fija primero; $\delta$ es el radio de entrada que responde a $\varepsilon$. El orden nunca se invierte.
> - ¿Cuándo un límite lateral infinito deja de existir?::Cuando los dos laterales no existen finitos o no coinciden, por ejemplo $1/(x-2)$ en $x=2$, donde los laterales son $+\infty$ y $-\infty$.
> - ¿Cómo se escribe el límite al infinito con umbral?::Para todo $\varepsilon > 0$ existe $N > 0$ tal que si $x > N$ entonces $|f(x) - L| < \varepsilon$; en el caso infinito el papel de $\varepsilon$ lo tiene $M$.

---

## 🔗 Conexiones

> [!info] 🔗 Notas relacionadas
>
> - [[Unidad 1 - Preliminares/02 - Puntos de Acumulación|02 - Puntos de Acumulación]] — base topológica del acercamiento por el dominio.
> - [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|02 - Propiedades y Teoremas de los Límites]] — álgebra de límites y sustitución directa.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/01 - Límites Laterales|01 - Límites Laterales]] — extensión de los laterales y discontinuidades.
> - [[Unidad 2 - Límites/II - Técnicas Básicas/02 - Límites Especiales|02 - Límites Especiales]] — $\sin x / x$, $1 - \cos x / x^2$ y $(1 + x)^{1/x}$.
> - [[Unidad 2 - Límites/III - Avanzados/01 - Límites al Infinito y Sucesiones|01 - Límites al Infinito y Sucesiones]] — secuencias y convergencia.
> - [[Unidad 3 - Aplicaciones de Límites/02 - Asíntotas y Comportamiento de Funciones|02 - Asíntotas y Comportamiento de Funciones]] — asíntotas y análisis completo.
> - [[Unidad 4 - Derivadas/I - Fundamentos Teóricos/01 - Derivada y Definición Formal|01 - Derivada y Definición Formal]] — la derivada como límite de cocientes incrementales.
> - [[Unidad 6 - Integrales/IV - Integrales Impropias y Avanzadas/01 - Integrales Impropias|01 - Integrales Impropias]] — límites de integración infinitos.

---

## 🔗 Seguir estudiando

> [!info] 📚 Seguir estudiando
>
> - Continúa con [[Unidad 2 - Límites/I - Fundamentos del Límite/02 - Propiedades y Teoremas de los Límites|Propiedades y Teoremas de los Límites]] para resolver límites sin demostrarlos uno por uno.
> - Practica antes de saltar a las formas indeterminadas: sin el $\varepsilon$-$\delta$ de esta nota no hay forma de justificar que se cancela el factor que anula.
> - En cada problema, escribe qué definición usas y por qué letra ($\delta$, $N$, $M$) antes de calcular.
> - Practica las formas indeterminadas con [[Unidad 2 - Límites/III - Avanzados/02 - Formas Indeterminadas|Formas Indeterminadas]] después de dominar los límites directos.

---

**Tags:** #MATG1045 #unidad2 #limite #epsilon-delta #limites-laterales #limites-infinitos #limites-al-infinito #asintotas #demostraciones
