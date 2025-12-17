# 📊 Monotonía y Puntos Críticos

## 🎯 Definiciones Fundamentales

> [!info]- 💡 Conceptos Básicos La **monotonía** de una función describe si la función es creciente o decreciente en intervalos específicos. Los **puntos críticos** son los valores donde la función puede cambiar su comportamiento monótono.
> 
> **Importancia:**
> 
> - Permite determinar máximos y mínimos de funciones
> - Fundamental para optimización
> - Base para el análisis completo de funciones
> - Herramienta clave en problemas aplicados

### 📈 Definición de Monotonía

> [!success]- ✅ Función Creciente **Una función $f$ es creciente en un intervalo $I$ si:**
> 
> $$\text{Para todo } x_1, x_2 \in I \text{ con } x_1 < x_2 \text{, se cumple } f(x_1) \leq f(x_2)$$
> 
> **Tipos de crecimiento:**
> 
> - **Estrictamente creciente:** $f(x_1) < f(x_2)$ cuando $x_1 < x_2$
> - **Monótonamente creciente:** $f(x_1) \leq f(x_2)$ cuando $x_1 < x_2$
> 
> **Interpretación gráfica:** La función "sube" de izquierda a derecha

> [!success]- ✅ Función Decreciente **Una función $f$ es decreciente en un intervalo $I$ si:**
> 
> $$\text{Para todo } x_1, x_2 \in I \text{ con } x_1 < x_2 \text{, se cumple } f(x_1) \geq f(x_2)$$
> 
> **Tipos de decrecimiento:**
> 
> - **Estrictamente decreciente:** $f(x_1) > f(x_2)$ cuando $x_1 < x_2$
> - **Monótonamente decreciente:** $f(x_1) \geq f(x_2)$ cuando $x_1 < x_2$
> 
> **Interpretación gráfica:** La función "baja" de izquierda a derecha

### 🔍 Puntos Críticos

> [!example]- 📍 Definición de Punto Crítico **Un punto $x = c$ es un punto crítico de $f(x)$ si:**
> 
> 1. **$c$ está en el dominio de $f$**
> 2. **Una de las siguientes condiciones se cumple:**
>     - $f'(c) = 0$ (derivada igual a cero)
>     - $f'(c)$ no existe (derivada no definida)
> 
> **Tipos de puntos críticos:**
> 
> - **Máximo local:** $f(c) \geq f(x)$ para $x$ cerca de $c$
> - **Mínimo local:** $f(c) \leq f(x)$ para $x$ cerca de $c$
> - **Punto de inflexión:** Cambio en la concavidad
> - **Punto silla:** Ni máximo ni mínimo local

## 🧮 Criterio de la Primera Derivada

### 📊 Teorema Fundamental de Monotonía

> [!tip]- 🔧 Criterio de la Primera Derivada para Monotonía **Sea $f$ una función derivable en el intervalo $(a,b)$:**
> 
> - **Si $f'(x) > 0$ para todo $x \in (a,b)$** → $f$ es **estrictamente creciente** en $(a,b)$
> - **Si $f'(x) < 0$ para todo $x \in (a,b)$** → $f$ es **estrictamente decreciente** en $(a,b)$
> - **Si $f'(x) = 0$ para todo $x \in (a,b)$** → $f$ es **constante** en $(a,b)$
> 
> **Interpretación geométrica:**
> 
> - $f'(x) > 0$ → Pendiente de la tangente es positiva → Función sube
> - $f'(x) < 0$ → Pendiente de la tangente es negativa → Función baja
> - $f'(x) = 0$ → Pendiente de la tangente es cero → Función horizontal

### 🎯 Criterio para Extremos Locales

> [!example]- 🏔️ Test de la Primera Derivada para Extremos **Sea $x = c$ un punto crítico de $f$ (es decir, $f'(c) = 0$ o $f'(c)$ no existe):**
> 
> **Caso 1: Máximo local**
> 
> - $f'(x) > 0$ para $x < c$ (función creciente antes de $c$)
> - $f'(x) < 0$ para $x > c$ (función decreciente después de $c$)
> 
> **Caso 2: Mínimo local**
> 
> - $f'(x) < 0$ para $x < c$ (función decreciente antes de $c$)
> - $f'(x) > 0$ para $x > c$ (función creciente después de $c$)
> 
> **Caso 3: No es extremo**
> 
> - $f'(x)$ mantiene el mismo signo antes y después de $c$
> 
> |Comportamiento de $f'$|Antes de $c$|En $c$|Después de $c$|Conclusión|
> |---|---|---|---|---|
> |**Máximo local**|$f' > 0$|$f' = 0$|$f' < 0$|⛰️ Máximo|
> |**Mínimo local**|$f' < 0$|$f' = 0$|$f' > 0$|🏔️ Mínimo|
> |**No extremo**|$f' > 0$|$f' = 0$|$f' > 0$|➡️ Punto de inflexión|
> |**No extremo**|$f' < 0$|$f' = 0$|$f' < 0$|➡️ Punto de inflexión|

## 🔄 Metodología de Análisis

### 📋 Algoritmo Paso a Paso

> [!tip]- 🎓 Procedimiento Sistemático **Para analizar la monotonía y encontrar puntos críticos:**
> 
> **Paso 1: Encontrar la derivada**
> 
> - Calcular $f'(x)$
> 
> **Paso 2: Identificar puntos críticos**
> 
> - Resolver $f'(x) = 0$
> - Identificar donde $f'(x)$ no existe
> - Verificar que están en el dominio de $f$
> 
> **Paso 3: Crear tabla de signos**
> 
> - Dividir el dominio usando los puntos críticos
> - Evaluar el signo de $f'(x)$ en cada intervalo
> 
> **Paso 4: Determinar monotonía**
> 
> - $f'(x) > 0$ → función creciente
> - $f'(x) < 0$ → función decreciente
> 
> **Paso 5: Clasificar puntos críticos**
> 
> - Usar el criterio de la primera derivada
> - Identificar máximos y mínimos locales

### 📊 Diagrama de Flujo del Análisis

```mermaid
flowchart TD
    A[Función f(x)] --> B[Calcular f'(x)]
    B --> C[Resolver f'(x) = 0]
    C --> D[Puntos donde f'(x) no existe]
    D --> E[Lista de Puntos Críticos]
    E --> F[Crear Tabla de Signos]
    F --> G{Signo de f'(x)?}
    G -->|f' > 0| H[Función Creciente]
    G -->|f' < 0| I[Función Decreciente]
    G -->|f' = 0| J[Analizar Comportamiento]
    H --> K[¿Cambio de signo?]
    I --> K
    K -->|Sí| L[Extremo Local]
    K -->|No| M[Punto de Inflexión]
    
    style A fill:#e3f2fd
    style L fill:#e8f5e8
    style M fill:#fff3e0
    style H fill:#c8e6c9
    style I fill:#ffcdd2
```

## 🎨 Ejemplos Detallados

### 📊 Ejemplo 1: Función Polinomial Cúbica

> [!example]- 📈 Ejemplo: $f(x) = x^3 - 3x^2 - 9x + 5$
> 
> **Paso 1: Calcular la derivada** $$f'(x) = 3x^2 - 6x - 9$$
> 
> **Paso 2: Encontrar puntos críticos** $$f'(x) = 0 \Rightarrow 3x^2 - 6x - 9 = 0$$ $$x^2 - 2x - 3 = 0$$ $$(x - 3)(x + 1) = 0$$
> 
> **Puntos críticos:** $x = -1$ y $x = 3$
> 
> **Paso 3: Tabla de signos**
> 
> |Intervalo|$x < -1$|$x = -1$|$-1 < x < 3$|$x = 3$|$x > 3$|
> |---|---|---|---|---|---|
> |**Factor $(x+1)$**|$-$|$0$|$+$|$+$|$+$|
> |**Factor $(x-3)$**|$-$|$-$|$-$|$0$|$+$|
> |**$f'(x) = 3(x+1)(x-3)$**|$+$|$0$|$-$|$0$|$+$|
> |**Monotonía de $f$**|↗|MAX|↘|MIN|↗|
> 
> **Paso 4: Resultados**
> 
> - **Creciente en:** $(-\infty, -1) \cup (3, +\infty)$
> - **Decreciente en:** $(-1, 3)$
> - **Máximo local en:** $x = -1$, $f(-1) = (-1)^3 - 3(-1)^2 - 9(-1) + 5 = -1 - 3 + 9 + 5 = 10$
> - **Mínimo local en:** $x = 3$, $f(3) = 27 - 27 - 27 + 5 = -22$

### 📊 Ejemplo 2: Función Racional

> [!example]- 📉 Ejemplo: $f(x) = \frac{x^2 - 4}{x^2 + 1}$
> 
> **Paso 1: Calcular la derivada (regla del cociente)** $$f'(x) = \frac{(2x)(x^2 + 1) - (x^2 - 4)(2x)}{(x^2 + 1)^2}$$ $$= \frac{2x(x^2 + 1) - 2x(x^2 - 4)}{(x^2 + 1)^2}$$ $$= \frac{2x[(x^2 + 1) - (x^2 - 4)]}{(x^2 + 1)^2}$$ $$= \frac{2x[5]}{(x^2 + 1)^2} = \frac{10x}{(x^2 + 1)^2}$$
> 
> **Paso 2: Encontrar puntos críticos** $$f'(x) = 0 \Rightarrow \frac{10x}{(x^2 + 1)^2} = 0$$ $$10x = 0 \Rightarrow x = 0$$
> 
> **Nota:** $f'(x)$ está definida para todos los reales (denominador nunca es cero)
> 
> **Punto crítico:** $x = 0$
> 
> **Paso 3: Análisis de signos** Como $(x^2 + 1)^2 > 0$ siempre, el signo de $f'(x)$ depende solo de $10x$:
> 
> |Intervalo|$x < 0$|$x = 0$|$x > 0$|
> |---|---|---|---|
> |**Signo de $10x$**|$-$|$0$|$+$|
> |**$f'(x)$**|$-$|$0$|$+$|
> |**Monotonía de $f$**|↘|MIN|↗|
> 
> **Paso 4: Resultados**
> 
> - **Decreciente en:** $(-\infty, 0)$
> - **Creciente en:** $(0, +\infty)$
> - **Mínimo absoluto en:** $x = 0$, $f(0) = \frac{0 - 4}{0 + 1} = -4$

### 📊 Ejemplo 3: Función con Raíz

> [!example]- 🌱 Ejemplo: $f(x) = x^{2/3}(x - 5)$
> 
> **Paso 1: Expandir y derivar** $$f(x) = x^{2/3} \cdot x - 5x^{2/3} = x^{5/3} - 5x^{2/3}$$ $$f'(x) = \frac{5}{3}x^{2/3} - 5 \cdot \frac{2}{3}x^{-1/3}$$ $$= \frac{5}{3}x^{2/3} - \frac{10}{3}x^{-1/3}$$ $$= \frac{5}{3}x^{-1/3}(x - 2)$$ $$= \frac{5(x - 2)}{3x^{1/3}}$$
> 
> **Paso 2: Encontrar puntos críticos**
> 
> - $f'(x) = 0 \Rightarrow x - 2 = 0 \Rightarrow x = 2$
> - $f'(x)$ no existe cuando $x^{1/3} = 0 \Rightarrow x = 0$
> 
> **Puntos críticos:** $x = 0$ y $x = 2$
> 
> **Paso 3: Tabla de signos**
> 
> |Intervalo|$x < 0$|$x = 0$|$0 < x < 2$|$x = 2$|$x > 2$|
> |---|---|---|---|---|---|
> |**$(x-2)$**|$-$|$-$|$-$|$0$|$+$|
> |**$x^{1/3}$**|$-$|$0$|$+$|$+$|$+$|
> |**$f'(x) = \frac{5(x-2)}{3x^{1/3}}$**|$+$|∄|$-$|$0$|$+$|
> |**Monotonía de $f$**|↗|?|↘|MIN|↗|
> 
> **Paso 4: Análisis especial en $x = 0$** Como $f'(x) > 0$ para $x < 0$ y $f'(x) < 0$ para $0 < x < 2$:
> 
> - $x = 0$ es un **máximo local**
> 
> **Paso 5: Resultados**
> 
> - **Creciente en:** $(-\infty, 0) \cup (2, +\infty)$
> - **Decreciente en:** $(0, 2)$
> - **Máximo local en:** $x = 0$, $f(0) = 0$
> - **Mínimo local en:** $x = 2$, $f(2) = 2^{2/3}(2-5) = -3 \cdot 2^{2/3}$

## 🧠 Técnica de Estudio: Método "DICE"

> [!tip]- 🎓 Mnemotecnia "DICE"
> 
> **D** - **D**erivada primero **I** - **I**gualar a cero (y buscar donde no existe) **C** - **C**rear tabla de signos **E** - **E**valuar comportamiento en cada intervalo
> 
> **Frase nemotécnica:** _"Deriva, Iguala, Crea y Evalúa"_
> 
> **Checklist de verificación:**
> 
> - ✅ ¿Calculé $f'(x)$ correctamente?
> - ✅ ¿Encontré todos los puntos donde $f'(x) = 0$?
> - ✅ ¿Identifiqué donde $f'(x)$ no existe?
> - ✅ ¿Verifiqué que los puntos críticos están en el dominio?
> - ✅ ¿Hice la tabla de signos completa?
> - ✅ ¿Clasifiqué correctamente cada punto crítico?

## ⚠️ Casos Especiales y Errores Comunes

### 🚫 Errores Frecuentes

> [!warning]- 🛑 Errores Comunes en el Análisis
> 
> **Error 1: Olvidar puntos donde la derivada no existe**
> 
> - ❌ Solo buscar $f'(x) = 0$
> - ✅ También buscar donde $f'(x)$ no está definida
> 
> **Error 2: No verificar el dominio**
> 
> - ❌ Incluir puntos críticos fuera del dominio de $f$
> - ✅ Verificar que $x = c$ está en el dominio de $f$
> 
> **Error 3: Tabla de signos incompleta**
> 
> - ❌ No evaluar $f'(x)$ en todos los intervalos
> - ✅ Probar un punto en cada intervalo determinado por los puntos críticos
> 
> **Error 4: Confundir extremos locales y globales**
> 
> - ❌ Asumir que todo extremo local es global
> - ✅ Distinguir entre extremos locales y absolutos
> 
> **Error 5: Interpretación incorrecta de signos**
> 
> - ❌ $f'(x) > 0$ significa función decreciente
> - ✅ $f'(x) > 0$ significa función creciente

### 🔄 Casos Especiales

> [!note]- 🎪 Situaciones Particulares
> 
> **Caso 1: Puntos críticos en los extremos del dominio**
> 
> - El criterio de la primera derivada puede no aplicar
> - Analizar límites laterales
> 
> **Caso 2: Derivada que no cambia de signo**
> 
> - $f'(x) = (x-2)^2$ tiene un cero en $x=2$ pero no cambia de signo
> - No hay extremo local, solo un punto de inflexión horizontal
> 
> **Caso 3: Funciones no diferenciables**
> 
> - $f(x) = |x|$ no es diferenciable en $x = 0$
> - Pero $x = 0$ es un mínimo local
> - Usar definición directa de extremo local
> 
> **Caso 4: Infinitos puntos críticos**
> 
> - $f(x) = x^2\sin(1/x)$ para $x \neq 0$, $f(0) = 0$
> - Infinitos puntos críticos cerca del origen

## 📊 Aplicaciones Prácticas

### 🎯 Optimización Básica

> [!success]- 🏆 Problemas de Optimización **Los puntos críticos son fundamentales para:**
> 
> **1. Maximizar/minimizar funciones:**
> 
> - Encontrar valores extremos de utilidad, costo, beneficio
> - Optimizar formas geométricas (área máxima, perímetro mínimo)
> 
> **2. Análisis de funciones:**
> 
> - Bosquejar gráficas precisas
> - Entender comportamiento global
> 
> **3. Problemas físicos:**
> 
> - Encontrar equilibrios estables/inestables
> - Minimizar energía, maximizar eficiencia
> 
> **Ejemplo típico:** Maximizar el área de un rectángulo con perímetro fijo
> 
> - $P = 2x + 2y = 100$ (constrante)
> - $A(x) = x \cdot y = x(50-x) = 50x - x^2$
> - $A'(x) = 50 - 2x = 0 \Rightarrow x = 25$
> - Máximo en $x = 25$, $y = 25$ (cuadrado)

### 🌐 Conexiones Interdisciplinarias

> [!note]- 🔗 Aplicaciones en Otras Áreas
> 
> **Economía:**
> 
> - Maximizar beneficios, minimizar costos
> - Análisis marginal (derivadas como tasas de cambio)
> - Puntos de equilibrio en oferta y demanda
> 
> **Física:**
> 
> - Principio de mínima acción
> - Equilibrio de fuerzas (derivada = 0)
> - Trayectorias óptimas
> 
> **Biología:**
> 
> - Crecimiento poblacional óptimo
> - Minimización de energía en sistemas biológicos
> - Modelos de predador-presa
> 
> **Ingeniería:**
> 
> - Diseño óptimo de estructuras
> - Control de sistemas dinámicos
> - Optimización de recursos

## 📖 Ejercicios de Práctica Progresiva

> [!example]- 💪 Secuencia de Entrenamiento
> 
> **Nivel 1 - Funciones Polinomiales:** 🟢
> 
> - $f(x) = x^3 - 6x^2 + 9x + 1$
> - $f(x) = 2x^3 - 3x^2 - 12x + 5$
> - $f(x) = x^4 - 8x^2 + 3$
> 
> **Nivel 2 - Funciones Racionales:** 🟡
> 
> - $f(x) = \frac{x^2 + 1}{x^2 - 4}$
> - $f(x) = \frac{x}{x^2 + 1}$
> - $f(x) = \frac{2x - 1}{x^2 + x - 2}$
> 
> **Nivel 3 - Funciones con Raíces:** 🟠
> 
> - $f(x) = x^{2/3}(x + 3)$
> - $f(x) = \sqrt{x}(4 - x)$ para $x \geq 0$
> - $f(x) = x\sqrt{4 - x^2}$ para $x \in [-2, 2]$
> 
> **Nivel 4 - Funciones Trascendentes:** 🔴
> 
> - $f(x) = xe^{-x}$
> - $f(x) = x - \ln x$ para $x > 0$
> - $f(x) = \frac{\ln x}{x}$ para $x > 0$
> - $f(x) = x^2 e^{-x^2}$

## 🎨 Representación Gráfica

### 📊 Interpretación Visual

> [!note]- 👁️ Lectura Gráfica de la Monotonía **Elementos gráficos clave:**
> 
> **1. Pendiente de tangentes:**
> 
> - Tangente con pendiente positiva → $f'(x) > 0$ → función creciente
> - Tangente con pendiente negativa → $f'(x) < 0$ → función decreciente
> - Tangente horizontal → $f'(x) = 0$ → posible extremo
> 
> **2. Puntos especiales:**
> 
> - **Picos:** Máximos locales
> - **Valles:** Mínimos locales
> - **Puntos angulares:** Posible no diferenciabilidad
> 
> **3. Comportamiento global:**
> 
> - Tendencia general ascendente/descendente
> - Número y ubicación de extremos
> 
> **Conexión con la derivada:**
> 
> - Gráfica de $f$ creciente ↔ Gráfica de $f'$ por encima del eje x
> - Gráfica de $f$ decreciente ↔ Gráfica de $f'$ por debajo del eje x
> - Extremos de $f$ ↔ Ceros de $f'$

### 🔍 Análisis Comparativo: $f(x)$ vs $f'(x)$

> [!tip]- 📊 Relación entre Función y Derivada
> 
> |Comportamiento de $f(x)$|Signo de $f'(x)$|Gráfica de $f'(x)$|
> |---|---|---|
> |Creciente|$f' > 0$|Por encima del eje x|
> |Decreciente|$f' < 0$|Por debajo del eje x|
> |Máximo local|$f' = 0$|Cruza de + a -|
> |Mínimo local|$f' = 0$|Cruza de - a +|
> |Punto de inflexión|$f' = 0$|Toca el eje pero no cruza|
> |Crecimiento constante|$f' = $ constante|Línea horizontal|

## 🔗 Teoremas Importantes

### 📚 Teoremas Fundamentales

> [!quote]- 🎓 Teoremas Relacionados
> 
> **Teorema de Rolle:** Si $f$ es continua en $[a,b]$, diferenciable en $(a,b)$, y $f(a) = f(b)$, entonces existe $c \in (a,b)$ tal que $f'(c) = 0$.
> 
> **Teorema del Valor Medio:** Si $f$ es continua en $[a,b]$ y diferenciable en $(a,b)$, entonces existe $c \in (a,b)$ tal que: $$f'(c) = \frac{f(b) - f(a)}{b - a}$$
> 
> **Aplicaciones:**
> 
> - Garantizan la existencia de puntos críticos en ciertas condiciones
> - Conectan el comportamiento local con el global
> - Base teórica para el análisis de monotonía

### 🌟 Conexión con Otros Conceptos

> [!success]- 🔗 Temas Relacionados **La monotonía conecta con:**
> 
> **1. Concavidad (Segunda derivada):**
> 
> - $f''(x) > 0$ → función cóncava hacia arriba
> - $f''(x) < 0$ → función cóncava hacia abajo
> - Puntos de inflexión donde $f''(x) = 0$
> 
> **2. Límites y continuidad:**
> 
> - Comportamiento en los extremos del dominio
> - Discontinuidades y su efecto en la monotonía
> 
> **3. Integrales:**
> 
> - Teorema fundamental del cálculo
> - Áreas bajo la curva y funciones crecientes/decrecientes

## 📚 Conexiones con Otros Temas

> [!quote]- 🔗 Enlaces a Otras Notas
> 
> **Prerrequisitos:**
> 
> - [[Derivadas]] - Cálculo de la primera derivada
> - [[Reglas de Derivación]] - Técnicas de derivación
> - [[Límites]] - Comportamiento local de funciones
> - [[Continuidad]] - Base para aplicar teoremas
> 
> **Temas relacionados:**
> 
> - [[03 - Concavidad y Puntos de Inflexión]] - Segunda derivada
> - [[Gráficas de Funciones]] - Representación visual
> - [[Extremos Absolutos]] - Valores máximos/mínimos globales
> 
> **Aplicaciones:**
> 
> - [[Optimización]] - Problemas de máximos y mínimos
> - [[Análisis de Funciones]] - Estudio completo
> - [[Modelos Matemáticos]] - Aplicaciones en ciencias
> 
> **Temas avanzados:**
> 
> - [[Análisis Convexo]] - Propiedades de convexidad
> - [[Ecuaciones Diferenciales]] - Sistemas dinámicos
> - [[Cálculo de Variaciones]] - Optimización funcional

---

**Tags:** #matemáticas #cálculo #derivadas #monotonía #puntos-críticos #extremos-locales #análisis-funciones #optimización #primera-derivada #máximos-mínimos #university #calculus-fundamentals #function-analysis