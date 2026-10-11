---
dg-publish: true
---

# 📈 Exponenciales y Logaritmos

## 🎯 Introducción

> [!info] 💡 ¿Qué son $a^x$ y $\log_ax$?
>
> Inversas mutuas ($y=a^x\iff x=\log_ay$): la exponencial crece con asíntota $y=0$; el logaritmo crece lento con asíntota $x=0$ y dominio $(0,\infty)$. Juntas convierten productos en sumas y potencias en multiplicaciones.
>
> ```mermaid
> graph LR
>     A["a x<br/>crece"] --> B["Inversa<br/>reflejo y=x"]
>     B --> C["log x<br/>lento"]
>     C --> D["Producto<br/>suma"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

![[U3-1314-explog.png]]

> [!tip] 💡 Visual — Reflejos en $y=x$
>
> $2^x$ y $\log_2x$ se reflejan: $(1/2,-1),(1,0),(2,1),(4,2)$ del logaritmo son $(-1,1/2),(0,1),(1,2),(2,4)$ de la exponencial intercambiados.

---

## 📋 Definición Formal

> [!note] 📋 Definición — Exponencial, logaritmo y leyes
>
> **Exponencial:** $a^x$ ($a>0,a\neq1$); $\text{Dom}=\mathbb{R}$, $\text{Ran}=(0,\infty)$, asíntota $y=0$ ($y=-2$ en $3^x-2$, que la desplaza).
>
> **Logaritmo:** $\log_ax=y\iff a^y=x$ ($x>0$); $\text{Dom}=(0,\infty)$, asíntota $x=0$. **Leyes (valen en ambos mundos):** $a^ma^n=a^{m+n}$ y $\log(xy)=\log x+\log y$ (misma regla reflejada); $\log(x^n)=n\log x$; cambio $\log_bx=\ln x/\ln b$.

> [!tip] 💡 Cómo resolver en ambos sentidos
>
> Exponencial: iguala bases ($9=3^2$) y la ecuación se vuelve lineal; si no hay base común, toma logaritmos ($2^x=3^{x-1}\therefore x=\ln3/(\ln3-\ln2)$). Logaritmo: escribe el dominio **antes** de operar y pasa a exponencial. Con base $<1$ en desigualdades, **invierte** en ambos casos.

> [!example] 🟢 Ejemplo — $4^x-3\cdot2^x+2=0$ y $\log_2(x-1)<3$
>
> $y=2^x$: $y^2-3y+2=0\therefore x=0,1$. Log: dominio $x>1$, base $>1$ conserva $\therefore x<9\therefore(1,9)$ (verifica $x=2\to1<3$ ✓).

---

## 📋 Tabla Comparativa: Exp vs Log

> [!note] 📋 Qué hace cada una y por qué son espejo
>
> | Aspecto | $a^x$ ($a>1$) | $\log_ax$ ($a>1$) |
> |---|---|---|
> | Dominio | $\mathbb{R}$ | $(0,\infty)$ (intercambiado con el rango) |
> | Asíntota | $y=0$ (nunca toca) | $x=0$ (reflejo de la anterior) |
> | Ecuación tipo | $2^{x+1}=8\therefore x=2$ | $\log_2(x-1)=3\therefore x=9$ |
> | Desigualdad base $<1$ | Invierte ($(1/3)^{x-2}\le9\to x\ge0$) | Invierte ($\log_{1/2}(x+3)\ge-2\to(-3,1]$) |
>
> **Escalas:** pH $4$ si $[H^+]=10^{-4}$; $x^{\log x}=100\therefore x=10^{\pm\sqrt2}$ (porque $(\log x)^2=2$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **$2^{x+1}=2^x+1$:** es $2\cdot2^x$ (el $+1$ multiplica por la base).
> - **$\log(x+y)=\log x+\log y$:** falso (solo productos/cocientes se parten).
> - **Dominio después:** $x>0$ primero; las extrañas se descartan ahí.
> - **Base $<1$ sin invertir:** vale en exp y en log por igual.

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. $2^{x+1}=8$, $5^x=1$; $\log_28$, $\ln e^2$.
> 2. $2^x$ en $-1,0,1,2$; $\log_2x$ en $1/2,1,2,4$.
> 3. Expande $\log(2x^3)$; condensa $2\ln x+\ln y$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $x=2,0$; $3,2$.
>
> **2.** $1/2,1,2,4$; $-1,0,1,2$ (reflejo).
>
> **3.** $\log2+3\log x$; $\ln(x^2y)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. $(1/3)^{x-2}\le9$.
> 5. $4^x-3\cdot2^x+2=0$.
> 6. $\log_{1/2}(x+3)\ge-2$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $x\ge0$ (invierte).
>
> **5.** $x=0,1$.
>
> **6.** $(-3,1]$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $2^x=3^{x-1}$ con logaritmos.
> 8. $x^{\log x}=100$.
> 9. $1000$ al $5\%$ 3 años: simple vs compuesto.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $x=\ln3/(\ln3-\ln2)$.
>
> **8.** $10^{\pm\sqrt2}$.
>
> **9.** $1150$; $1157.63$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Igualo bases y evalúo $\log_a$.
> - [ ] Tabulo ambas y veo el reflejo.
> - [ ] Expando y condenso logaritmos.
> - [ ] Calculo interés simple.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Invierto con base $<1$ (ambas).
> - [ ] Sustituyo $y=a^x$ en cuadráticas.
> - [ ] Resuelvo inecuaciones con dominio.
> - [ ] Hallo asíntotas desplazadas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Paso a logaritmos sin base común.
> - [ ] Resuelvo $x^{\log x}=k$.
> - [ ] Comparo interés continuo.
> - [ ] Aplico pH y Richter.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 4 (exp y log).
>
> [2] R. D. Swokowski, *Álgebra y Trigonometría* — cap. de exp y log.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[10 - Función inversa de una función biyectiva]] — $\ln$ como inversa.
> - [[10 - Ecuaciones]] — exponenciales como ecuaciones.
> - [[06 - Funciones Especiales]] — $\sigma$ usa $e^{-x}$.
> - [[11 - Inecuaciones]] — dominios con desigualdades.

---

**Tags:** #funciones #exponencial #logaritmo #unidad3
