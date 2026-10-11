---
dg-publish: true
---

# 📦 Funciones Polinomiales

## 🎯 Introducción

> [!info] 💡 ¿Qué es un polinomio?
>
> $P(x)=a_nx^n+\cdots+a_0$: el grado $n$ manda (máximo $n$ raíces, $n-1$ giros). Ruffini + factor + resto cero factoriza; el líder decide los extremos en $\pm\infty$.
>
> ```mermaid
> graph LR
>     A["Grado n<br/>líder an"] --> B["Ruffini<br/>factoriza"]
>     B --> C["Raíces<br/>mult"]
>     C --> D["Extremos<br/>líder"]
>     style B fill:#e1ffe1
>     style D fill:#e1f5ff
> ```

---

## 📋 Definición Formal

> [!note] 📋 Definición — Grado, resto y multiplicidad
>
> **Grado:** mayor exponente; **líder:** $a_nx^n$ (manda en $\pm\infty$). **Resto:** $P(a)$ es el resto de dividir por $(x-a)$.
>
> **Fundamental:** $n$ raíces en $\mathbb{C}$ con multiplicidad. **Multiplicidad par:** toca; **impar:** cruza.

> [!tip] 💡 Cómo factorizar sin atascarse
>
> Prueba raíces candidatas ($\pm$ divisores del término independiente) evaluando $P(a)$ — si da cero, Ruffini y sigue con el cociente. Cuenta multiplicidades al final: las pares tocan el eje, las impares lo cruzan, y eso dibuja la gráfica casi sola.

> [!example] 🟢 Ejemplo — $x^3-2x^2-x+2$ completo
>
> $P(1)=0\therefore$ Ruffini: cociente $x^2-x-2=(x-2)(x+1)$. Factores $(x-1)(x-2)(x+1)$ (verifica producto $=P$ ✓).

---

## 📋 Tabla Comparativa: Raíces y Extremos

> [!note] 📋 Qué esperar según grado y líder
>
> | Caso | Raíces reales (máx) | Extremos |
> |---|---|---|
> | Grado par, $a_n>0$ | $n$ | $+\infty$ ambos lados |
> | Grado par, $a_n<0$ | $n$ | $-\infty$ ambos lados |
> | Grado impar, $a_n>0$ | $n$ | $-\infty$ izq, $+\infty$ der |
> | Grado impar, $a_n<0$ | $n$ | $+\infty$ izq, $-\infty$ der |
>
> **Descartes:** cambios de signo acotan positivas ($x^3-3x+2$: $2$ o $0$).

---

## ⚠️ Errores Comunes

> [!warning] ⚠️ Errores frecuentes
>
> - **Grado del producto sin sumar:** $(x-1)^2(x+2)$ es grado $3$.
> - **Multiplicidad par cruzando:** par **toca**, impar cruza.
> - **Ruffini sin verificar:** multiplica los factores al final.
> - **$P(2)$ por sustitución larga:** es el resto directo (resto $=P(a)$).

---

## 📝 Ejercicios Progresivos

### 🟢 Nivel 1 — Básico

> [!question] 📋 Ejercicios Nivel 1
>
> 1. Grado y líder de $2x^3-5x+1$, $-x^4+2$, $7$.
> 2. $P(2)$ si $P=x^3-2x+1$.
> 3. Factoriza $x^2-5x+6$ y $x^3-x$.

> [!success]- ✅ Respuestas Nivel 1
>
> **1.** $3,2$; $4,-1$; $0,7$.
>
> **2.** $5$.
>
> **3.** $(x-2)(x-3)$; $x(x-1)(x+1)$.

### 🟡 Nivel 2 — Intermedio

> [!question] 📋 Ejercicios Nivel 2
>
> 4. Ruffini completo de $x^3-2x^2-x+2$.
> 5. $x^4-5x^2+4$ con $y=x^2$.
> 6. Halla $k$ con $x=2$ raíz de $x^3+kx-6$.

> [!success]- ✅ Respuestas Nivel 2
>
> **4.** $(x-1)(x-2)(x+1)$.
>
> **5.** $(y-1)(y-4)$; raíces $\pm1,\pm2$.
>
> **6.** $8+2k-6=0\therefore k=-1$.

### 🔴 Nivel 3 — Avanzado

> [!question] 📋 Ejercicios Nivel 3
>
> 7. $(x-1)^2(x+2)$: multiplicidad y cruce/toca.
> 8. $x^5-x$: raíces reales y signo.
> 9. Divide $x^3+2x^2-5x-6$ por $(x+1)$.

> [!success]- ✅ Respuestas Nivel 3
>
> **7.** $x=1$ toca (par); $x=-2$ cruza.
>
> **8.** $0,\pm1$; signo por intervalos.
>
> **9.** Cociente $x^2+x-6$; raíces $-1,-3,2$.

---

## 🎯 Metas de Aprendizaje

> [!note] 📋 Nivel Básico
>
> - [ ] Identifico grado y coeficiente líder.
> - [ ] Evalúo con resto ($P(a)$).
> - [ ] Factorizo cuadráticas y cúbicas simples.
> - [ ] Predigo extremos por el líder.

> [!note] 📋 Nivel Intermedio
>
> - [ ] Aplico Ruffini completo.
> - [ ] Sustituyo $y=x^2$ en bicuadráticas.
> - [ ] Uso Descartes para acotar.
> - [ ] Hallo $k$ con raíces dadas.

> [!note] 📋 Nivel Avanzado
>
> - [ ] Interpreto multiplicidades gráficamente.
> - [ ] Enuncio el teorema fundamental.
> - [ ] Interpolo polinomios por puntos.
> - [ ] Divido con resto cero verificado.

---

## 📚 Referencias

> [!quote] 📖 Fuentes consultadas
>
> [1] J. Stewart, *Precálculo*, 7ma ed. — cap. 3 (polinomios).
>
> [2] A. Baldor, *Álgebra*, 2da ed., Patria — cap. de polinomios.

---

## 🔗 Conexiones

> [!quote] 🔗 Notas relacionadas
>
> - [[07 - Función cuadrática]] — grado 2 como caso.
> - [[13 - Técnicas de conteo]] — expande $(x+1)^n$.
> - [[12 - Funciones racionales]] — $P/Q$ con ceros de $P$.
> - [[12 - Inducción matemática]] — prueba $f^n$ lineal.

---

**Tags:** #funciones #polinomios #ruffini #unidad3
