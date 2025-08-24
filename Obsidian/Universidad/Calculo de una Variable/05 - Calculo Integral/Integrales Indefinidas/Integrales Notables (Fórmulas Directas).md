# Integrales Notables (Fórmulas Directas)

> [!quote] _"Las integrales notables son los cimientos del cálculo integral. Como herramientas fundamentales, nos permiten resolver de manera directa una amplia gama de funciones sin recurrir a técnicas complejas de integración. Dominar estas fórmulas es esencial para construir el conocimiento integral más avanzado."_

> [!info]+ Concepto Fundamental 📚
> 
> ### ¿Qué son las Integrales Notables?
> 
> Las **integrales notables** o **integrales inmediatas** son aquellas que pueden resolverse directamente aplicando las **fórmulas básicas de integración**, sin necesidad de técnicas especiales como sustitución, integración por partes, o fracciones parciales.
> 
> ### Teorema Fundamental
> 
> Si $F'(x) = f(x)$, entonces: **$$\int f(x)dx = F(x) + C$$**
> 
> Donde $C$ es la **constante de integración**.
> 
> ### Principio de Linealidad
> 
> **$$\int [af(x) + bg(x)]dx = a\int f(x)dx + b\int g(x)dx$$**

> [!tip]- Integrales Algebraicas Básicas 🔢
> 
> ### 1. Integral de una Constante
> 
> **$$\int dx = x + C$$**
> 
> **Demostración:**
> 
> ```
> Si F(x) = x, entonces F'(x) = 1
> Por tanto: ∫1dx = ∫dx = x + C
> ```
> 
> ### 2. Integral de Potencias (Regla de la Potencia)
> 
> **$$\int x^n dx = \frac{x^{n+1}}{n+1} + C \quad ; \quad n \neq -1$$**
> 
> **Demostración:**
> 
> ```
> Si F(x) = x^(n+1)/(n+1), entonces:
> F'(x) = (n+1) · x^n/(n+1) = x^n
> 
> Por tanto: ∫x^n dx = x^(n+1)/(n+1) + C
> ```
> 
> **Casos Especiales:**
> 
> - $\int x dx = \frac{x^2}{2} + C$
> - $\int x^2 dx = \frac{x^3}{3} + C$
> - $\int \sqrt{x} dx = \int x^{1/2} dx = \frac{2x^{3/2}}{3} + C$
> - $\int \frac{1}{x^2} dx = \int x^{-2} dx = -\frac{1}{x} + C$
> 
> ### 3. Integral Logarítmica
> 
> **$$\int \frac{1}{x} dx = \ln|x| + C$$**
> 
> **Demostración:**
> 
> ```
> Para x > 0: d/dx[ln(x)] = 1/x
> Para x < 0: d/dx[ln(-x)] = 1/(-x) · (-1) = 1/x
> 
> En ambos casos: d/dx[ln|x|] = 1/x
> Por tanto: ∫(1/x)dx = ln|x| + C
> ```

> [!example]- Integrales Exponenciales 📈
> 
> ### 4. Integral de e^x
> 
> **$$\int e^x dx = e^x + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[e^x] = e^x
> Por tanto: ∫e^x dx = e^x + C
> ```
> 
> ### 5. Integral de Exponencial General
> 
> **$$\int a^x dx = \frac{a^x}{\ln a} + C \quad ; \quad a > 0, a \neq 1$$**
> 
> **Demostración:**
> 
> ```
> Sabemos que a^x = e^(x·ln a)
> 
> d/dx[a^x/ln a] = d/dx[e^(x·ln a)/ln a]
>                 = (1/ln a) · e^(x·ln a) · ln a
>                 = e^(x·ln a) = a^x
> 
> Por tanto: ∫a^x dx = a^x/ln a + C
> ```
> 
> **Casos Especiales:**
> 
> - $\int 2^x dx = \frac{2^x}{\ln 2} + C$
> - $\int 10^x dx = \frac{10^x}{\ln 10} + C$

> [!success]- Integrales Trigonométricas Básicas 📐
> 
> ### 6. Integral del Seno
> 
> **$$\int \sin x dx = -\cos x + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[-cos x] = -(-sen x) = sen x
> Por tanto: ∫sen x dx = -cos x + C
> ```
> 
> ### 7. Integral del Coseno
> 
> **$$\int \cos x dx = \sin x + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[sen x] = cos x
> Por tanto: ∫cos x dx = sen x + C
> ```
> 
> ### 8. Integral de la Secante al Cuadrado
> 
> **$$\int \sec^2 x dx = \tan x + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[tg x] = d/dx[sen x/cos x] = sec^2 x
> Por tanto: ∫sec^2 x dx = tg x + C
> ```
> 
> ### 9. Integral de la Cosecante al Cuadrado
> 
> **$$\int \csc^2 x dx = -\cot gx + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[-cot x] = d/dx[-cos x/sen x] = csc^2 x
> Por tanto: ∫csc^2 x dx = -cot x + C
> ```

> [!abstract]- Integrales Trigonométricas con Tangente y Cotangente 📊
> 
> ### 10. Integral del Producto Secante-Tangente
> 
> **$$\int \sec x \tan x dx = \sec x + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[sec x] = sec x · tg x
> Por tanto: ∫sec x tg x dx = sec x + C
> ```
> 
> ### 11. Integral del Producto Cosecante-Cotangente
> 
> **$$\int \csc x \cot gx dx = -\csc x + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[-csc x] = -(-csc x · cot x) = csc x · cot x
> Por tanto: ∫csc x cot x dx = -csc x + C
> ```
> 
> ### 12. Integral de la Tangente
> 
> **$$\int \tan x dx = -\ln|\cos x| + C = \ln|\sec x| + C$$**
> 
> **Demostración:**
> 
> ```
> ∫tg x dx = ∫(sen x/cos x) dx
> 
> Sea u = cos x, entonces du = -sen x dx
> ∫tg x dx = ∫(-1/u) du = -ln|u| + C = -ln|cos x| + C
> 
> Como ln|sec x| = ln|1/cos x| = -ln|cos x|:
> ∫tg x dx = ln|sec x| + C
> ```
> 
> ### 13. Integral de la Cotangente
> 
> **$$\int \cot gx dx = \ln|\sin x| + C$$**
> 
> **Demostración:**
> 
> ```
> ∫cot x dx = ∫(cos x/sen x) dx
> 
> Sea u = sen x, entonces du = cos x dx
> ∫cot x dx = ∫(1/u) du = ln|u| + C = ln|sen x| + C
> ```

> [!note]- Integrales Logarítmicas de Funciones Trigonométricas 📝
> 
> ### 14. Integral de la Secante
> 
> **$$\int \sec x dx = \ln|\sec x + \tan x| + C$$**
> 
> **Demostración:**
> 
> ```
> ∫sec x dx = ∫sec x · (sec x + tg x)/(sec x + tg x) dx
>           = ∫(sec^2 x + sec x tg x)/(sec x + tg x) dx
> 
> Sea u = sec x + tg x, entonces:
> du = (sec x tg x + sec^2 x) dx
> 
> ∫sec x dx = ∫(1/u) du = ln|u| + C = ln|sec x + tg x| + C
> ```
> 
> ### 15. Integral de la Cosecante
> 
> **$$\int \csc x dx = \ln|\csc x - \cot gx| + C$$**
> 
> **Demostración:**
> 
> ```
> ∫csc x dx = ∫csc x · (csc x - cot x)/(csc x - cot x) dx
>           = ∫(csc^2 x - csc x cot x)/(csc x - cot x) dx
> 
> Sea u = csc x - cot x, entonces:
> du = (-csc x cot x + csc^2 x) dx
> 
> ∫csc x dx = ∫(1/u) du = ln|u| + C = ln|csc x - cot x| + C
> ```

> [!tip]- Integrales que Resultan en Funciones Trigonométricas Inversas 🔄
> 
> ### 16. Integral Arcoseno
> 
> **$$\int \frac{1}{\sqrt{a^2 - x^2}} dx = \arcsin\left(\frac{x}{a}\right) + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[arcsen(x/a)] = 1/√(1-(x/a)^2) · (1/a)
>                   = (1/a)/√((a^2-x^2)/a^2)
>                   = 1/√(a^2-x^2)
> 
> Por tanto: ∫1/√(a^2-x^2) dx = arcsen(x/a) + C
> ```
> 
> ### 17. Integral Arctangente
> 
> **$$\int \frac{1}{a^2 + x^2} dx = \frac{1}{a}\arctan\left(\frac{x}{a}\right) + C$$**
> 
> **Demostración:**
> 
> ```
> d/dx[1/a · arctg(x/a)] = (1/a) · 1/(1+(x/a)^2) · (1/a)
>                        = 1/(a^2 + x^2)
> 
> Por tanto: ∫1/(a^2+x^2) dx = (1/a)arctg(x/a) + C
> ```
> 
> ### 18. Integral Arcosecante
> 
> **$$\int \frac{1}{x\sqrt{x^2 - a^2}} dx = \frac{1}{a}\arcsin\left(\frac{|x|}{a}\right) + C = \frac{1}{a}\arccos\left(\frac{a}{|x|}\right) + C$$**
> 
> **Demostración:**
> 
> ```
> Para x > a > 0:
> d/dx[1/a · arcsen(|x|/a)] = (1/a) · 1/√(1-(x/a)^2) · (1/a)
>                           = 1/(a√(a^2-x^2))
> 
> Para la forma con arccos:
> d/dx[1/a · arccos(a/|x|)] = (1/a) · (-1)/√(1-(a/x)^2) · (-a/x^2)
>                           = 1/(x√(x^2-a^2))
> ```

> [!example]- Integrales Hiperbólicas 🌊
> 
> ### 19. Integral del Seno Hiperbólico
> 
> **$$\int \senh x dx = \cosh x + C$$**
> 
> **Demostración:**
> 
> ```
> senh x = (e^x - e^(-x))/2
> d/dx[cosh x] = d/dx[(e^x + e^(-x))/2] = (e^x - e^(-x))/2 = senh x
> 
> Por tanto: ∫senh x dx = cosh x + C
> ```
> 
> ### 20. Integral del Coseno Hiperbólico
> 
> **$$\int \cosh x dx = \senh x + C$$**
> 
> **Demostración:**
> 
> ```
> cosh x = (e^x + e^(-x))/2
> d/dx[senh x] = d/dx[(e^x - e^(-x))/2] = (e^x + e^(-x))/2 = cosh x
> 
> Por tanto: ∫cosh x dx = senh x + C
> ```

> [!warning]- Casos Especiales y Observaciones Importantes ⚠️
> 
> ### Restricciones y Dominios
> 
> **1. Integral de 1/x:**
> 
> - El valor absoluto en $\ln|x|$ es crucial
> - Válida para $x \neq 0$
> - En intervalos donde $x > 0$: $\int \frac{1}{x}dx = \ln x + C$
> - En intervalos donde $x < 0$: $\int \frac{1}{x}dx = \ln(-x) + C$
> 
> **2. Integrales con radicales:**
> 
> - En $\int \frac{1}{\sqrt{a^2-x^2}}dx$: Requiere $|x| < a$
> - En $\int \frac{1}{x\sqrt{x^2-a^2}}dx$: Requiere $|x| > a$
> 
> **3. Constantes de integración:**
> 
> ```
> ∫[f(x) + g(x)]dx = ∫f(x)dx + ∫g(x)dx
>                   = F(x) + C₁ + G(x) + C₂
>                   = F(x) + G(x) + C  (donde C = C₁ + C₂)
> ```

> [!success]- Ejemplos de Aplicación Práctica 📚
> 
> ### Ejemplo 1: Combinación Lineal
> 
> **Calcular:** $\int (3x^2 - 5\sen x + 2e^x)dx$
> 
> **Solución:**
> 
> ```
> ∫(3x² - 5sen x + 2e^x)dx = 3∫x²dx - 5∫sen x dx + 2∫e^x dx
>                           = 3(x³/3) - 5(-cos x) + 2e^x + C
>                           = x³ + 5cos x + 2e^x + C
> ```
> 
> ### Ejemplo 2: Con Constantes
> 
> **Calcular:** $\int \frac{4}{x^2 + 9}dx$
> 
> **Solución:**
> 
> ```
> ∫4/(x² + 9)dx = 4∫1/(x² + 3²)dx
> 
> Usando la fórmula ∫1/(a² + x²)dx = (1/a)arctg(x/a) + C con a = 3:
> = 4 · (1/3)arctg(x/3) + C
> = (4/3)arctg(x/3) + C
> ```
> 
> ### Ejemplo 3: Potencias Especiales
> 
> **Calcular:** $\int (2\sqrt{x} - \frac{3}{x^3})dx$
> 
> **Solución:**
> 
> ```
> ∫(2√x - 3/x³)dx = ∫(2x^(1/2) - 3x^(-3))dx
>                  = 2∫x^(1/2)dx - 3∫x^(-3)dx
>                  = 2 · x^(3/2)/(3/2) - 3 · x^(-2)/(-2) + C
>                  = (4/3)x^(3/2) + (3/2)x^(-2) + C
>                  = (4/3)x√x + 3/(2x²) + C
> ```

> [!brain]+ Técnica de Memorización: INTEGRAL 🧠 **I** - Identificar el tipo de función (algebraica, trigonométrica, exponencial) **N** - Nombrar la fórmula correspondiente **T** - Transformar si es necesario (factores constantes) **E** - Evaluar usando la fórmula directa **G** - Garantizar que se incluya la constante C **R** - Revisar el resultado derivando **A** - Aplicar restricciones del dominio si existen **L** - Limpiar la expresión final

> [!summary]+ Tabla de Referencias Rápidas 📋
> 
> ### Las 20 Integrales Notables Fundamentales
![[bc93763d-46e7-4187-9f53-1bd5847dcd28 1.jpg]]
>
> _Esta tabla contiene las fórmulas directas más importantes para la integración inmediata. Cada fórmula representa una antiderivada que debe memorizarse para resolver integrales de manera eficiente._

> [!info]- Estrategias de Resolución 🎯
> 
> ### Pasos para Resolver Integrales Notables
> 
> **1. Identificación:**
> 
> - Reconocer la forma de la función
> - Clasificar: algebraica, trigonométrica, exponencial, etc.
> 
> **2. Preparación:**
> 
> - Extraer constantes multiplicativas
> - Reescribir en forma estándar si es necesario
> 
> **3. Aplicación:**
> 
> - Usar la fórmula directa correspondiente
> - No olvidar la constante de integración
> 
> **4. Verificación:**
> 
> - Derivar el resultado para comprobar
> - Verificar restricciones del dominio

> [!success]- Puntos Clave para Recordar 🎯
> 
> 1. **📝 Constante C**: Siempre incluir en integrales indefinidas
> 2. **🔍 Valor absoluto**: Crucial en $\ln|x|$ y funciones inversas
> 3. **⚠️ Dominios**: Verificar restricciones de cada fórmula
> 4. **🔄 Linealidad**: $\int [af(x) + bg(x)]dx = a\int f(x)dx + b\int g(x)dx$
> 5. **✅ Verificación**: Derivar el resultado debe dar la función original
> 6. **📐 Formas estándar**: Reconocer patrones para aplicar fórmulas correctas

---

## Referencias

> [!quote] Notas Relacionadas
> 
> - Carpeta Técnicas de Integración
> - [[Teorema Fundamental del Cálculo]]
> - Carpeta Reglas de Derivación
> - [[Funciones Trigonométricas]]

## Notas Recomendadas

> [!info] Prerrequisitos
> 
> - [[Reglas de Derivación]]
> - [[Funciones Elementales]]
> - [[Límites de Funciones]]

> [!tip] Continuación del Tema
> 
> - [[Cambio de Variable en Integrales]]
> - [[Integración por Partes]]
> - Carpeta Integrales Definidas
> - 06 - Aplicaciones - Integrales 

---

**Tags:** #matemáticas #cálculo #integrales #integrales-indefinidas #fórmulas-directas #integración #funciones-elementales #antiderivadas #cálculo-integral