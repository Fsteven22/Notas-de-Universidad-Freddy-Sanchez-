---
dg-publish: true
---

# 🔁 Sucesiones

## 🎯 Introducción

> [!info] 💡 ¿Qué es una sucesión?
>
> $(a_n)$ con fórmula o recurrencia: aritmética ($+d$), geométrica ($\times r$), Fibonacci ($F_{n}=F_{n-1}+F_{n-2}$). Monótona + acotada $\therefore$ converge; el límite de la recurrencia sale del punto fijo.
>
> ```mermaid
> graph LR
>     A["Fórmula<br/>a(n)"] --> B["Arit/geom<br/>d,r"]
>     B --> C["Recurre<br/>Fibonacci"]
>     C --> D["Límite<br/>punto fijo"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[15-sucesion.png]]

> [!tip] 💡 Visual — Convergencia monótona
>
> $a_1=1$, $a_{n+1}=\sqrt{2+a_n}$ sube acotada por $2$: el punto fijo $L=\sqrt{2+L}\therefore L=2$ es el techo que nunca cruza.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Tipos y convergencia
>
> **Aritmética:** $a_n=a_1+(n-1)d$, $S_n=n(a_1+a_n)/2$. **Geométrica:** $a_n=a_1r^{n-1}$, $S_n=a_1(r^n-1)/(r-1)$.
>
> **Converge:** $\forall\varepsilon>0\;\exists N\;|a_n-L|<\varepsilon$. **Teorema:** monótona + acotada $\therefore$ converge.

> [!tip] 💡 Cómo hallar límites de recurrencias
>
> Prueba acotación por inducción y monotonía comparando $a_{n+1}$ con $a_n$; luego pasa al límite en la recurrencia ($L=\sqrt{2+L}\therefore L=2$, descarta $L=-1$). Para racionales divide por la mayor potencia; para $(1+1/n)^n$ reconoce $e$.

> [!example] 🟢 Ejemplo — $a_1=1$, $a_{n+1}=\sqrt{2+a_n}$
>
> $a_n<2$ por inducción ($\sqrt{2+2}=2$); creciente ($a_2=\sqrt3>1$); $L=\sqrt{2+L}\therefore L=2$ (verifica $2=\sqrt4$ ✓).

---

## 📋 Tabla Comparativa: Sucesiones

> [!note] 📋 Qué fórmula usar y cuándo
>
> | Tipo | Término | Suma/límite |
> |---|---|---|
> | Aritmética | $a_1+(n-1)d$ | $S_5=5(2+14)/2=40$ ($a_1=2,d=3$) |
> | Geométrica | $a_1r^{n-1}$ | $a_6=64$ ($a_1=1,r=2$) |
> | Fibonacci | $F_n=F_{n-1}+F_{n-2}$ | $0,1,1,2,3,5,8,13$ |
> | $1/n$ | Acotada, no monótona | $\to0$ ($N>1/\varepsilon$) |
> | $(-1)^n$ | Oscilante | Diverge ($1$ vs $-1$) |
>
> **Encaje:** $0\le n!/n^n\le1/n\therefore\to0$.

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Índice $0$ vs $1$:** $a_1=2,d=3\therefore a_5=14$ (cuenta desde $1$).
> - **Acotada $\therefore$ converge:** falta monótona ($(-1)^n$ diverge).
> - **$L=-1$ aceptado:** en $\sqrt{\cdot}$ descarta negativos.
> - **$(1+1/n)^n\to1$:** es $e$ ($2.59,2.70$ en $n=10,100$).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Términos $2n+1$ ($n=1..4$) y $(-1)^n$ ($n=1..5$).
> 2. Aritmética $a_1=2,d=3$: $a_5$, $S_5$.
> 3. Fibonacci $F_0..F_7$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $3,5,7,9$; $-1,1,-1,1,-1$.
>
> **2.** $14$; $40$.
>
> **3.** $0,1,1,2,3,5,8,13$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $\lim(3n+1)/(2n-1)$ dividiendo por $n$.
> 5. $a_1=1$, $a_{n+1}=\sqrt{2+a_n}$: límite.
> 6. $n!/n^n\to0$ por encaje.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $3/2$.
>
> **5.** $2$ (acotada + creciente).
>
> **6.** Entre $0$ y $1/n$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. Prueba $n^{1/n}\to1$ con binomio.
> 8. Newton $x_{n+1}=(x_n+2/x_n)/2\to\sqrt2$.
> 9. Subsucesiones de $(-1)^n$ y divergencia.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $h_n\to0$ (acota con $n(n-1)h_n^2/2$).
>
> **8.** Punto fijo $L=2/L$.
>
> **9.** $1$ y $-1$ distintos $\therefore$ diverge.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Genero términos desde fórmulas.
> - [ ] Aplico $a_n,S_n$ aritméticas.
> - [ ] Aplico $a_n$ geométricas.
> - [ ] Decido acotación y monotonía.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Pruebo límites con $\varepsilon$.
> - [ ] Divido por mayor potencia.
> - [ ] Resuelvo puntos fijos.
> - [ ] Reconozco $e$ numéricamente.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Demuestro $n^{1/n}\to1$.
> - [ ] Analizo Newton hacia $\sqrt2$.
> - [ ] Uso subsucesiones para divergir.
> - [ ] Pruebo Cesàro con promedios.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] R. Grimaldi, *Matemática Discreta*, Pearson — cap. de sucesiones.
>
> [2] J. Stewart, *Cálculo*, 7ma ed. — cap. de sucesiones.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[12 - Inducción matemática]] — prueba acotación/monotonía.
> - [[13 - Técnicas de conteo]] — acota $n^{1/n}$.
> - [[01 - Conjuntos Numéricos]] — decimales como límites de parciales.
> - [[13 - Funciones exponenciales]] — $e$ como límite.

---

**Tags:** #números-reales #sucesiones #límites #unidad2
