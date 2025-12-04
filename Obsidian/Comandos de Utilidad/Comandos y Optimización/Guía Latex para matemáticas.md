# 📝 Guía LaTeX para Matemáticas en Obsidian

> [!quote] 🎯 "La belleza de las matemáticas no está solo en los resultados, sino en cómo los expresamos."

---

> [!info]- ## 🚀 Conceptos Básicos
>
> ### 💡 Modos de Escritura
>
> > [!tip] 📋 **Dos formas de escribir matemáticas**
> > - **Inline (en línea)**: `$f(x) = x^2$` → Se integra con el texto.
> > - **Display (bloque)**: `$$f(x) = x^2$$` → Se centra en su propia línea.
>
> **Ejemplos:**
> - Inline: La función $f(x) = x^2$ es una parábola.
> - Display:
> ```latex
> $$f(x) = x^2$$
> ```

---

> [!info]- ## 🧮 Integrales
>
> ### 📊 Integrales Básicas
> | Tipo | Código | Resultado |
> |------|--------|-----------|
> | **Indefinida** | `\int f(x) dx` | $\int f(x) dx$ |
> | **Definida** | `\int_a^b f(x) dx` | $\int_a^b f(x) dx$ |
> | **Múltiple** | `\iint_D f(x,y) dA` | $\iint_D f(x,y) dA$ |
> | **Triple** | `\iiint_V f(x,y,z) dV` | $\iiint_V f(x,y,z) dV$ |
>
> > [!tip] 🔥 **Integrales Avanzadas**
> > ```latex
> > \oint_C \mathbf{F} \cdot d\mathbf{r}
> > ```
> > $$\oint_C \mathbf{F} \cdot d\mathbf{r}$$
> >
> > ```latex
> > \int_{-\infty}^{\infty} e^{-x^2} dx
> > ```
> > $$\int_{-\infty}^{\infty} e^{-x^2} dx$$
> >
> > ```latex
> > \int_0^1 \int_0^{\sqrt{1-x^2}} f(x,y) \, dy \, dx
> > ```
> > $$\int_0^1 \int_0^{\sqrt{1-x^2}} f(x,y) \, dy \, dx$$
>
> > [!warning] 💡 **Consejo:** Usa `\,` para separar la función de la diferencial.

---

> [!info]- ## 📈 Derivadas
>
> ### 🎯 Notaciones Estándar
> | Concepto | Código | Resultado |
> |----------|--------|-----------|
> | **Derivada simple** | `f'(x)` | $f'(x)$ |
> | **Leibniz** | `\frac{dy}{dx}` | $\frac{dy}{dx}$ |
> | **Segunda** | `f''(x)` / `\frac{d^2y}{dx^2}` | $f''(x)$ / $\frac{d^2y}{dx^2}$ |
> | **n-ésima** | `f^{(n)}(x)` / `\frac{d^n y}{dx^n}` | $f^{(n)}(x)$ / $\frac{d^n y}{dx^n}$ |
>
> > [!tip] 🌊 **Derivadas Parciales**
> > ```latex
> > \frac{\partial f}{\partial x}
> > ```
> > $$\frac{\partial f}{\partial x}$$
> >
> > ```latex
> > \frac{\partial^2 f}{\partial x^2} \quad \frac{\partial^2 f}{\partial x \partial y}
> > ```
> > $$\frac{\partial^2 f}{\partial x^2} \quad \frac{\partial^2 f}{\partial x \partial y}$$
>
> > [!example] 🎯 **Evaluación en Puntos**
> > ```latex
> > \left.\frac{dy}{dx}\right|_{x=a}
> > ```
> > $$\left.\frac{dy}{dx}\right|_{x=a}$$
> >
> > ```latex
> > \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}
> > ```
> > $$\lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

---

> [!info]- ## 🔢 Sumas y Productos
>
> ### Sigma
> ```latex
> \sum_{i=1}^{n} a_i
> ```
> $$\sum_{i=1}^{n} a_i$$
>
> ```latex
> \sum_{n=0}^{\infty} \frac{x^n}{n!}
> ```
> $$\sum_{n=0}^{\infty} \frac{x^n}{n!}$$
>
> ### Pi
> ```latex
> \prod_{i=1}^{n} a_i
> ```
> $$\prod_{i=1}^{n} a_i$$

---

> [!info]- ## 🎭 Límites
>
> ```latex
> \lim_{x \to a} f(x)
> ```
> $$\lim_{x \to a} f(x)$$
>
> ```latex
> \lim_{x \to \infty} \frac{1}{x}
> ```
> $$\lim_{x \to \infty} \frac{1}{x}$$
>
> ```latex
> \lim_{x \to a^+} f(x) \quad \lim_{x \to a^-} f(x)
> ```
> $$\lim_{x \to a^+} f(x) \quad \lim_{x \to a^-} f(x)$$

---

> [!info]- ## 🔧 Fracciones y Raíces
>
> ```latex
> \frac{a}{b}
> ```
> $$\frac{a}{b}$$
>
> ```latex
> \sqrt{x}
> ```
> $$\sqrt{x}$$
>
> ```latex
> \sqrt[n]{x}
> ```
> $$\sqrt[n]{x}$$

---

> [!info]- ## 🎪 Paréntesis y Delimitadores
>
> ```latex
> \left( \frac{a}{b} \right)
> ```
> $$\left( \frac{a}{b} \right)$$
>
> ```latex
> \left[ \frac{a}{b} \right] \quad \left\{ \frac{a}{b} \right\} \quad \left| \frac{a}{b} \right|
> ```
> $$\left[ \frac{a}{b} \right] \quad \left\{ \frac{a}{b} \right\} \quad \left| \frac{a}{b} \right|$$

---

> [!info]- ## 🎨 Símbolos Especiales
>
> | Símbolo | Código | Uso |
> |---------|--------|-----|
> | $\infty$ | `\infty` | Infinito |
> | $\partial$ | `\partial` | Derivada parcial |
> | $\nabla$ | `\nabla` | Gradiente |
> | $\Delta$ | `\Delta` | Delta |
> | $\epsilon$ | `\epsilon` | Épsilon |
> | $\to$ | `\to` | Tiende a |
> | $\in$ | `\in` | Pertenece |
> | $\subset$ | `\subset` | Subconjunto |
>
> **Letras Griegas:**
> ```latex
> \alpha, \beta, \gamma, \delta, \epsilon, \theta, \lambda, \mu, \pi, \sigma, \tau, \phi, \psi, \omega
> \Gamma, \Delta, \Theta, \Lambda, \Pi, \Sigma, \Phi, \Psi, \Omega
> ```

---

> [!info]- ## 🎯 Matrices y Vectores
>
> ```latex
> \begin{pmatrix}
> a & b \\
> c & d
> \end{pmatrix}
> ```
> $$\begin{pmatrix} a & b \\ c & d \end{pmatrix}$$
>
> ```latex
> \begin{bmatrix}
> 1 & 2 & 3 \\
> 4 & 5 & 6 \\
> 7 & 8 & 9
> \end{bmatrix}
> ```
> $$\begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$$
>
> ```latex
> \vec{v} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}
> ```
> $$\vec{v} = \begin{pmatrix} x \\ y \\ z \end{pmatrix}$$

---

> [!info]- ## 📐 Alineación de Ecuaciones
>
> ```latex
> \begin{align}
> y &= 2x^2 + 5x - 3 \\
> &= 2(1)^2 + 5(1) - 3 \\
> &= 2 + 5 - 3 \\
> &= 4
> \end{align}
> ```
> $$
> \begin{align}
> y &= 2x^2 + 5x - 3 \\
> &= 2(1)^2 + 5(1) - 3 \\
> &= 2 + 5 - 3 \\
> &= 4
> \end{align}
> $$
>
> > [!example] **Sistema de ecuaciones**
> > ```latex
> > \begin{cases}
> > 2x + y = 5 \\
> > x - y = 1
> > \end{cases}
> > ```
> > $$
> > \begin{cases}
> > 2x + y = 5 \\
> > x - y = 1
> > \end{cases}
> > $$

---

> [!tip]- ## ⚡ Espaciado y Formateo
>
> | Comando | Espacio | Ejemplo |
> |---------|---------|---------|
> | `\,` | Pequeño | $a\,b$ |
> | `\;` | Mediano | $a\;b$ |
> | `\quad` | 1 em | $a\quad b$ |
> | `\qquad` | 2 em | $a\qquad b$ |

---

> [!example]- ## 🧪 Ejemplos Completos
>
> **Teorema Fundamental del Cálculo**
> ```latex
> \frac{d}{dx}\left[\int_a^x f(t) \, dt\right] = f(x)
> ```
> $$\frac{d}{dx}\left[\int_a^x f(t) \, dt\right] = f(x)$$
>
> ```latex
> \int_a^b f(x) \, dx = F(b) - F(a) = \left[F(x)\right]_a^b
> ```
> $$\int_a^b f(x) \, dx = F(b) - F(a) = \left[F(x)\right]_a^b$$
---

> [!quote]- ## 📚 Notas Relacionadas
>
> > [!quote] 🔢 [[Comandos ASCII]]
> > Referencia de símbolos y caracteres útiles para LaTeX.
>
> > [!quote] 📄 [[Markdown]]
> > Integración de LaTeX en textos y documentos en Obsidian.
>
> > [!quote] ⌨️ [[Atajos de Teclado Universales]]
> > Combinaciones para escribir fórmulas y comandos más rápido.
>
> > [!quote] 📘 [[Atajos y Características de Obsidian]]
> > Guía general para usar de forma óptima el entorno de trabajo.

---

> [!link]- ## 🏷️ Tags
>
> #herramientas/latex  
> #matematicas/notacion  
> #obsidian/formatting  
> #calculo/sintaxis  
> #referencia/rapida
