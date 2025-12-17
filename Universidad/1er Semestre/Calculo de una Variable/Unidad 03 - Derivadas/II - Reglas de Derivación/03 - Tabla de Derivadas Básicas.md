# Tabla de Derivadas Básicas 

> [!quote] _"Las fórmulas de derivación son herramientas esenciales que todo estudiante de cálculo debe dominar. Esta tabla de referencia rápida complementa el estudio teórico profundo, proporcionando acceso inmediato a las fórmulas fundamentales necesarias para resolver problemas de derivación."_

> [!info]+ Propósito de esta Referencia 📚
> 
> ### Complemento a tus Estudios de Derivadas
> 
> Esta nota está diseñada como **referencia rápida** para complementar tus notas detalladas sobre:
> 
> - **Derivabilidad y Continuidad** - Conceptos teóricos fundamentales
> - **Derivadas y Definición Formal** - Demostraciones rigurosas usando límites
> - **Interpretación Geométrica de la Derivada** - Significado visual y aplicaciones
> 
> ### Notación Utilizada
> 
> - **Funciones trigonométricas**: $\sin x$, $\cos x$, $\tan x$, $\cot x$, $\sec x$, $\csc x$
> - **Operador derivada**: $D_x f(x)$ o $f'(x)$
> - **Notación de Leibniz**: $\frac{dy}{dx}$

> [!summary]+ Tabla de Derivadas Básicas 📋
> 
> ### Las 13 Fórmulas Fundamentales
> ![[Pasted image 20250824170857.png]]
> 
> _Esta tabla contiene las reglas de derivación esenciales que debes memorizar. Cada fórmula representa la derivada directa de las funciones elementales más importantes en cálculo diferencial._

> [!tip]- Fórmulas Organizadas por Categoría 🔢
> 
> ### Funciones Algebraicas
> 
> **1.** $D_x(k) = 0$ para toda constante $k \in \mathbb{R}$ **2.** $D_x(x) = 1$ **3.** $D_x(x^n) = nx^{n-1}$
> 
> ### Funciones Exponenciales
> 
> **4.** $D_x(e^x) = e^x$ **5.** $D_x(a^x) = a^x \ln a$
> 
> ### Funciones Logarítmicas
> 
> **6.** $D_x(\ln x) = \frac{1}{x}$ **7.** $D_x(\log_a x) = \frac{1}{x \ln a}$
> 
> ### Funciones Trigonométricas Básicas
> 
> **8.** $D_x(\sin x) = \cos x$ **9.** $D_x(\cos x) = -\sin x$ **10.** $D_x(\tan x) = \sec^2 x$ **11.** $D_x(\cot x) = -\csc^2 x$
> 
> ### Funciones Trigonométricas Recíprocas
> 
> **12.** $D_x(\sec x) = \sec x \tan x$ **13.** $D_x(\csc x) = -\csc x \cot x$

> [!example]- Reglas de Combinación (Referencia Rápida) ⚡
> 
> ### Reglas Fundamentales para Funciones Compuestas
> 
> **Regla de la Suma/Diferencia:** $$D_x[f(x) \pm g(x)] = f'(x) \pm g'(x)$$
> 
> **Regla del Producto:** $$D_x[f(x) \cdot g(x)] = f'(x) \cdot g(x) + f(x) \cdot g'(x)$$
> 
> **Regla del Cociente:** $$D_x\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x) \cdot g(x) - f(x) \cdot g'(x)}{[g(x)]^2}$$
> 
> **Regla de la Cadena:** $$D_x[f(g(x))] = f'(g(x)) \cdot g'(x)$$

> [!note]- Casos Especiales Importantes 📝
> 
> ### Extensiones Útiles de las Fórmulas Básicas
> 
> **Potencias con exponente negativo:**
> 
> - $D_x(x^{-n}) = -nx^{-n-1} = -\frac{n}{x^{n+1}}$
> - $D_x\left(\frac{1}{x}\right) = -\frac{1}{x^2}$
> 
> **Raíces como potencias:**
> 
> - $D_x(\sqrt{x}) = D_x(x^{1/2}) = \frac{1}{2}x^{-1/2} = \frac{1}{2\sqrt{x}}$
> - $D_x(\sqrt[n]{x}) = \frac{1}{n}x^{(1/n)-1}$
> 
> **Funciones trigonométricas con coeficientes:**
> 
> - $D_x(\sin(ax)) = a\cos(ax)$
> - $D_x(\cos(ax)) = -a\sin(ax)$
> - $D_x(\tan(ax)) = a\sec^2(ax)$

> [!success]- Ejemplos Rápidos de Aplicación 🚀
> 
> ### Casos Comunes que Aparecen Frecuentemente
> 
> **Ejemplo 1: Polinomio simple**
> 
> ```
> f(x) = 3x⁴ - 2x³ + 5x - 7
> f'(x) = 12x³ - 6x² + 5
> ```
> 
> **Ejemplo 2: Combinación exponencial-trigonométrica**
> 
> ```
> f(x) = e^x + sin x
> f'(x) = e^x + cos x
> ```
> 
> **Ejemplo 3: Producto simple**
> 
> ```
> f(x) = x² sin x
> f'(x) = 2x sin x + x² cos x  (regla del producto)
> ```

> [!brain]+ Estrategia de Memorización: TABLA 🧠 **T** - **Tipo**: Identifica la función (algebraica, exponencial, logarítmica, trigonométrica) **A** - **Aplica**: Usa la fórmula directa correspondiente **B** - **Busca**: Composición de funciones (cadena) **L** - **Linealiza**: Separa sumas y diferencias **A** - **Ajusta**: Simplifica el resultado final

> [!warning]- Conexión con tus Otras Notas 🔗
> 
> ### Cómo usar esta referencia junto con tus estudios
> 
> **📖 Para teoría profunda:** Consulta tus notas de _Derivadas y Definición Formal_
> 
> **📐 Para interpretación visual:** Revisa _Interpretación Geométrica de la Derivada_
> 
> **🔍 Para conceptos avanzados:** Estudia _Derivabilidad y Continuidad_
> 
> **⚡ Para aplicación rápida:** Usa esta tabla como referencia inmediata
> 
> ### Flujo de Estudio Recomendado
> 
> 1. **Entender el concepto** → Tus notas de definición formal
> 2. **Visualizar geométricamente** → Tu nota de interpretación geométrica
> 3. **Memorizar fórmulas** → Esta tabla de referencia
> 4. **Aplicar en problemas** → Combinando teoría con fórmulas

> [!info]- Relación con Integrales 🔄
> 
> ### Teorema Fundamental del Cálculo
> 
> **Si conoces la derivada, puedes encontrar la integral:**
> 
> ```
> Si D_x F(x) = f(x), entonces ∫f(x)dx = F(x) + C
> ```
> 
> **Ejemplos de la relación inversa:**
> 
> - $D_x(x^2) = 2x$ ↔ $\int 2x , dx = x^2 + C$
> - $D_x(\sin x) = \cos x$ ↔ $\int \cos x , dx = \sin x + C$
> - $D_x(e^x) = e^x$ ↔ $\int e^x , dx = e^x + C$

> [!success]- Puntos Clave para Recordar 🎯
> 
> 1. **📋 Referencia rápida**: Esta tabla es para consulta inmediata durante problemas
> 2. **🔗 Complemento**: Funciona mejor junto con tus notas teóricas existentes
> 3. **⚡ Memorización**: Las 13 fórmulas básicas son esenciales
> 4. **🔄 Reglas de combinación**: Producto, cociente y cadena son fundamentales
> 5. **✅ Verificación**: Siempre puedes comprobar derivando el resultado
> 6. **📐 Conexión**: Las derivadas son la base para entender las integrales

---

## Referencias

> [!quote] Notas Relacionadas
> 
> - [[03 - Derivabilidad y Continuidad]]
> - [[01 - Derivada y Definición Formal]]
> - [[02 - Interpretación Geométrica de la Derivada]]
> - [[Integrales Notables (Fórmulas Directas)]]

## Notas Recomendadas

> [!info] Tus Notas de Derivadas
> 
> - [[03 - Derivabilidad y Continuidad]] - Conceptos fundamentales
> - [[01 - Derivada y Definición Formal]] - Demostraciones rigurosas
> - [[02 - Interpretación Geométrica de la Derivada]] - Significado visual

> [!tip] Continuación del Tema
> 
> - [[Integrales Notables (Fórmulas Directas)]] - Operación inversa
> - [[01 - Problemas de Optimización]]

---

**Tags:** #matemáticas #cálculo #derivadas #fórmulas-básicas #referencia-rápida #cálculo-diferencial #tabla-derivadas