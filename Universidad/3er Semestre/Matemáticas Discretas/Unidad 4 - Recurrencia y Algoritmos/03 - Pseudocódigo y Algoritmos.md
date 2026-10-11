---
dg-publish: true
---
# 💻 Pseudocódigo y Algoritmos

## 🎯 Introducción

> [!info] 💡 ¿Por qué usar seudocódigo?
> 
> El **seudocódigo** describe algoritmos con una sintaxis parecida a la de un lenguaje de programación, pero sin las reglas estrictas de ninguno en particular. Aunque el lenguaje común a veces basta para describir un algoritmo, se prefiere el seudocódigo por su **precisión, estructura y universalidad**: no depende de un lenguaje de programación específico, así que cualquiera con base en programación puede leerlo.
> 
> - Esta nota cubre la **sintaxis básica** (asignación, `if`, `while`, `for`, funciones) y la noción formal de **algoritmo**.
> - Se conecta con [[04 - Análisis de Algoritmos I - Fundamentos y Funciones Matemáticas]] y [[05 - Análisis de Algoritmos II - Pseudocódigo y Tiempo Real]], donde estos mismos algoritmos se analizan para obtener sus cotas asintóticas.
> 
> ```mermaid
> graph TD
>     A[Pseudocódigo y Algoritmos] --> B[Sintaxis básica asignación, if, comentarios]
>     A --> C[Concepto de Algoritmo]
>     A --> D[Funciones y return]
>     A --> E[Estructuras de control: while, for]
>     A --> F[Ejemplos clásicos]
> ```

---

## 🔵 Elementos Básicos del Seudocódigo

> [!note] 🔵 Asignación (`=`) vs. Igualdad (`==`)
> 
> El signo `=` denota el **operador de asignación**. En seudocódigo,
> 
> $$x = y$$
> 
> significa "copia el valor de $y$ en $x$" — el valor de $y$ **no cambia** al ejecutar esto. Para comparar dos valores se usa en cambio `==` (igual a).
> 
> **Operadores disponibles:**
> 
> |Tipo|Operadores|
> |---|---|
> |Aritméticos|$+,\ -,\ *,\ /$|
> |Relacionales|$==$ (igual a), $\neq$ (no igual a), $<, >, \leq, \geq$|
> |Lógicos|$\land$ (y), $\lor$ (o), $\neg$ (no)|

> [!example] 🟢 Ejemplo — diferencia entre `=` y `==`
> 
> Sea $x=5$, $y=10$, $z=15$. Para el segmento:
> 
> ```
> if (y == x)
>     z = x
> y = z
> ```
> 
> Como $y==x$ es **falso**, `z = x` no se ejecuta. Luego `y = z` sí se ejecuta, y $y$ pasa a valer $15$. Al final: $x=5$, y ambas $y$ y $z$ valen $15$.

> [!note] 🔵 La instrucción `if` / `if-else`
> 
> ```
> if (condición)
>     acción
> ```
> 
> Si la condición es verdadera se ejecuta la acción y el control pasa a la siguiente instrucción; si es falsa, la acción se omite. La forma `if-else` añade una rama alternativa:
> 
> ```
> if (condición)
>     acción1
> else
>     acción2
> ```
> 
> Si la acción tiene varias instrucciones, se encierran entre llaves `{ }`. Los comentarios se escriben con `//` y se extienden hasta el final de la línea — **no se ejecutan**, solo documentan el código.

> [!example] 🟢 Ejemplo — `if-else` con múltiples instrucciones
> 
> Sea $x=5$, $y=10$, $z=15$. Para:
> 
> ```
> if (y ≠ x)
>     y = x
> else
>     z = x
> a = z
> ```
> 
> Como $y\neq x$ es cierto, se ejecuta `y = x` ($y$ pasa a $5$); `z = x` no se ejecuta. Luego `a = z` se ejecuta y $a$ queda en $15$. Al final: $x=y=5$, y $a=z=15$.

---

## 🟢 ¿Qué es un Algoritmo?

> [!note] 🟢 Definición
> 
> Un **algoritmo** es un método paso a paso para resolver un problema, generalmente pensado para ser ejecutado por una computadora.
> 
> **Características típicas:**
> 
> |Característica|Significado|
> |---|---|
> |**Entrada**|Recibe datos de entrada|
> |**Salida**|Produce una salida|
> |**Precisión**|Los pasos están establecidos con precisión|
> |**Determinismo**|Cada resultado intermedio depende únicamente de la entrada y de los pasos anteriores|
> |**Carácter finito**|Termina tras un número finito de instrucciones|
> |**Corrección**|La salida producida es correcta — resuelve el problema sin errores|
> |**Generalidad**|Se aplica a un [[04 - Cardinalidad y Leyes de Cardinalidad|Cardinalidad]] de entradas, no a un solo caso|

> [!example] 🟢 Ejemplo — máximo de tres números (con rastreo)
> 
> **Algoritmo** (encuentra el máximo entre $a$, $b$, $c$):
> 
> 1. $grande = a$
> 2. Si $b > grande$, entonces $grande = b$
> 3. Si $c > grande$, entonces $grande = c$
> 
> **Rastreo** con $a=1,\ b=5,\ c=3$:
> 
> |Línea|Acción|Valor de `grande`|
> |---|---|---|
> |1|`grande = a`|1|
> |2|$5>1$ es verdadero → `grande = b`|5|
> |3|$3>5$ es falso → sin cambio|5|
> 
> Al final, `grande = 5`, el mayor entre $a, b, c$.

---

## 🟡 Funciones en Seudocódigo

> [!note] 🟡 Sintaxis de una [[01 - Funciones|función]]
> 
> ```
> nombre_función(parámetros separados por comas) {
>     código para realizar cálculos
> }
> ```
> 
> - `return x` termina la función y regresa el valor de $x$ a quien la invocó.
> - `return` (sin valor) simplemente termina la función.
> - Si no hay instrucción `return`, la función termina justo antes de la llave de cierre.

> [!example] 🟢 Ejemplo — máximo y mínimo de tres números en seudocódigo
> 
> ```
> Entrada: a, b, c
> Salida: x (el mayor de a, b y c)
> max1(a, b, c){
>     x = a
>     if (b > x)        // si b es mayor que x, se actualiza x
>         x = b
>     if (c > x)        // si c es mayor que x, se actualiza x
>         x = c
> }
> ```
> 
> El mínimo es análogo, solo invirtiendo las comparaciones:
> 
> ```
> Entrada: a, b, c
> Salida: x (el menor de a, b y c)
> menor(a, b, c){
>     x = a
>     if (b < x)
>         x = b
>     if (c < x)
>         x = c
>     return x
> }
> ```

---

## 🔴 Estructuras de Control: `while` y `for`

> [!note] 🔴 El ciclo `while`
> 
> ```
> while (condición)
>     acción
> ```
> 
> Mientras la condición sea verdadera, se ejecuta la acción y la secuencia se repite; en cuanto la condición se vuelve falsa, el control pasa a la instrucción siguiente.

> [!example] 🟢 Ejemplo — máximo de una [[04 - Sucesiones y Cadenas|sucesión]] con `while`
> 
> ```
> Entrada: s, n
> Salida: grande (el mayor valor en la sucesión s)
> grande = s1
> i = 2
> while (i ≤ n){
>     if (si > grande)
>         grande = si
>     i = i + 1
> }
> ```
> 
> La idea: recorrer toda la sucesión guardando en `grande` el valor más alto encontrado hasta el momento.

> [!note] 🔴 El ciclo `for`
> 
> ```
> for var = inicio to límite
>     acción
> ```
> 
> La acción se ejecuta una vez por cada valor de `var` desde `inicio` hasta `límite`. El mismo algoritmo de arriba, reescrito con `for`:
> 
> ```
> Entrada: s, n
> Salida: grande (el mayor valor en la sucesión s)
> grande = s1
> for i = 2 to n
>     if (si > grande)
>         grande = si
> ```

---

## 🎓 Ejemplos Avanzados: [[02 - Cuantificadores|Cuantificadores]] Lógicos

> [!example] 🟢 Valor lógico de $\forall x: P(x)$
> 
> Sea $P$ una función proposicional cuyo dominio de discurso son $d_1,\dots,d_n$:
> 
> ```
> Entrada: d1, ..., dn
> Salida: valor lógico
> for i = 1 to n
>     if (¬P(di))
>         return falsa
> return verdadera
> ```

> [!question] 📋 Ejercicios propuestos (mismos que en clase)
> 
> **1.** Diseñe un algoritmo que determine el valor lógico de $\exists x: P(x)$.
> 
> **2.** Para $P(x,y)$ con dominio los pares $(d_i,d_j)$, ya vimos el algoritmo de doble ciclo para $\forall x,\forall y: P(x,y)$:
> 
> ```
> for i = 1 to n
>     for j = 1 to n
>         if (¬P(di, dj))
>             return falsa
> return verdadera
> ```
> 
> Diseñe algoritmos análogos para $\forall x,\exists y: P(x,y)$ y para $\exists x,\forall y: P(x,y)$.
> 
> > [!tip]- 💡 Pista
> > 
> > Para $\exists x: P(x)$, basta con invertir la lógica del algoritmo de $\forall$: buscar un $d_i$ que sí cumpla $P(d_i)$ y regresar verdadero apenas se encuentre uno; si se recorre todo sin éxito, regresar falso. Para $\forall x,\exists y$ y $\exists x,\forall y$, la clave está en **dónde** se anida la búsqueda de "al menos uno" dentro del ciclo de "todos".

---

## 🧮 Otros Algoritmos Clásicos

> [!example] 🟢 Prueba de primalidad
> 
> Determina si $n>1$ es primo o compuesto. Si es compuesto, regresa un divisor $d$ con $2\leq d\leq\sqrt{n}$; si es primo, regresa $0$.
> 
> ```
> Entrada: n
> Salida: d o 0
> primalidad(n){
>     for d = 2 to ⌊√n⌋
>         if (n mod d == 0)
>             return d
>     return 0
> }
> ```

> [!example] 🟢 Conversión de base $b$ a decimal
> 
> Convierte la cadena $c = c_n c_{n-1}\cdots c_1 c_0$ (dígitos en base $b$) a su valor decimal.
> 
> ```
> Entrada: c, n, b
> Salida: val_dec
> base_b_a_dec(c, n, b){
>     val_dec = 0
>     potencia = 1
>     for i = 0 to n{
>         val_dec = val_dec + ci * potencia
>         potencia = potencia * b
>     }
>     return val_dec
> }
> ```

![[ChatGPT Image 18 ago 2026, 20_24_30.png]]

---

## 🔗 Conexiones

> [!note] 📋 Temas relacionados
> 
> - [[04 - Análisis de Algoritmos I - Fundamentos y Funciones Matemáticas]] — cómo obtener cotas asintóticas a partir de una fórmula ya dada.
> - [[05 - Análisis de Algoritmos II - Pseudocódigo y Tiempo Real]] — cómo obtener esas mismas cotas contando operaciones directamente sobre este seudocódigo, incluyendo los algoritmos recursivos.

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
> 
> [1] E. Pineda, _Pseudocódigo y Algoritmos_, clase MATG1051, ESPOL, jul. 2026.
> 
> [2] K. H. Rosen, _Discrete Mathematics and Its Applications_, 8th ed. New York, USA: McGraw-Hill, 2019, pp. 173–184.

---


## Metas de Aprendizaje

> [!note] Nivel Básico
> - [ ] Leo y escribo pseudocódigo para algoritmos secuenciales.
> - [ ] Identifico estructuras de control (if, while, for, repeat).
> - [ ] Trazeo la ejecución de un algoritmo paso a paso.

> [!note] Nivel Intermedio
> - [ ] Diseño algoritmos que resuelven problemas de búsqueda y ordenamiento.
> - [ ] Identifico recursión en pseudocódigo y la expreso como recurrencia.
> - [ ] Comparo algoritmos iterativos vs recursivos para el mismo problema.

> [!note] Nivel Avanzado
> - [ ] Diseño algoritmos divide y vencerás y expreso su recurrencia.
> - [ ] Analizo la corrección de algoritmos usando invariantes.
> - [ ] Optimizo algoritmos eliminando llamadas recursivas innecesarias.

**Tags:** #pseudocodigo #algoritmos #estructurasdecontrol #MATG1051 #unidad4 #ESPOL
