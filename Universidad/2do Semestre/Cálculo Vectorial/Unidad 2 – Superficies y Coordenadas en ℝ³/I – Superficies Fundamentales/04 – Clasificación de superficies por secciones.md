# 🎭 Clasificación de Superficies por Secciones

## 🎯 Introducción a la Clasificación por Secciones

> [!info]- 💡 Cómo las Secciones Determinan el Tipo de Superficie La **clasificación de superficies por secciones** es un método sistemático donde **el patrón de las curvas obtenidas al cortar la superficie determina inequívocamente su tipo**.
> 
> **Principio fundamental:**
> 
> > "El tipo de curvas que resultan al hacer cortes paralelos revela la naturaleza de la superficie"
> 
> **¿Por qué funciona este método?**
> 
> - Cada tipo de superficie cuadrática tiene un **patrón único** de secciones
> - Las curvas obtenidas (círculos, elipses, parábolas, hipérbolas) son como "huellas dactilares"
> - La combinación de curvas en diferentes direcciones identifica la superficie
> 
> **El proceso de clasificación:**
> 
> 1. **Hacer cortes paralelos** en tres direcciones (x = k, y = k, z = k)
> 2. **Identificar el tipo de curva** en cada familia de cortes
> 3. **Observar cómo cambian** las curvas al variar k
> 4. **Comparar el patrón** con las superficies conocidas
> 5. **Clasificar** la superficie según el patrón único
> 
> **Analogía útil:**
> 
> - **Tomografía médica:** Reconstruir el órgano completo desde sus cortes
> - **Arqueología:** Identificar un objeto por sus capas estratigráficas
> - **Análisis de huellas:** Cada superficie tiene su "firma" única de secciones
> 
> **Herramientas de identificación:**
> 
> - **Tipo de curva:** círculo, elipse, parábola, hipérbola, recta, punto
> - **Crecimiento:** ¿cómo cambia el tamaño al variar k?
> - **Existencia:** ¿para qué valores de k existe la sección?
> - **Orientación:** ¿en qué dirección se orienta la curva?

## 📐 Criterios de Clasificación

### 🔍 Patrones de Identificación

> [!warning]- 🎯 Tabla de Decisión para Clasificar Superficies
> 
> **Criterio 1: Secciones horizontales (z = k)**
> 
> |Tipo de curva|Crecimiento|Superficie posible|
> |---|---|---|
> |**Elipses decrecientes**|Se achican hasta un punto|Elipsoide|
> |**Elipses crecientes**|Se agrandan desde un punto|Paraboloide elíptico|
> |**Elipses crecientes**|Se agrandan desde una elipse mínima|Hiperboloide de 1 hoja|
> |**Elipses crecientes**|Crecimiento lineal desde el origen|Cono elíptico|
> |**Hipérbolas cambiantes**|Cambian de orientación, rectas en k=0|Paraboloide hiperbólico|
> |**Hipérbolas constantes**|Todas con misma orientación|Hiperboloide de 2 hojas|
> 
> **Criterio 2: Existencia de secciones**
> 
> |Rango de existencia|Interpretación|
> |---|---|
> |**Solo \|k\| ≤ c**|Superficie cerrada (Elipsoide)|
> |**Solo k ≥ 0** o **k ≤ 0**|Paraboloide (elíptico o hiperbólico)|
> |**Todo k ∈ ℝ**|Hiperboloide de 1 hoja o Cono|
> |**Solo \|k\| ≥ a**|Hiperboloide de 2 hojas|
> 
> **Criterio 3: Secciones verticales**
> 
> |Patrón de curvas verticales|Superficie|
> |---|---|
> |**Todas elipses**|Elipsoide|
> |**Todas parábolas (misma orientación)**|Paraboloide elíptico|
> |**Parábolas opuestas**|Paraboloide hiperbólico|
> |**Todas hipérbolas**|Hiperboloide|
> |**Hipérbolas + rectas**|Cono|

### 🎯 Algoritmo de Clasificación

> [!success]- 📝 Proceso Paso a Paso
> 
> **PASO 1: Analizar secciones z = k**
> 
> ```
> ¿Qué curvas obtienes?
> 
> → ELIPSES:
>    ¿Crecen o decrecen?
>    ├─ Decrecen → Elipsoide
>    ├─ Crecen desde punto → Paraboloide elíptico
>    ├─ Crecen desde elipse mínima → Hiperboloide 1 hoja
>    └─ Crecen linealmente → Cono
> 
> → HIPÉRBOLAS:
>    ¿Cambian de orientación?
>    ├─ Sí (+ rectas en k=0) → Paraboloide hiperbólico
>    └─ No → Hiperboloide 2 hojas
> 
> → RECTAS:
>    → Cilindro o plano degenerado
> 
> → PUNTOS:
>    → Superficie degenerada
> ```
> 
> **PASO 2: Verificar con secciones verticales**
> 
> ```
> Hacer cortes x = k y y = k
> 
> → Confirmar el tipo de curva
> → Verificar simetría
> → Identificar orientación del eje
> ```
> 
> **PASO 3: Analizar dominio de existencia**
> 
> ```
> ¿Para qué valores de k existen las secciones?
> 
> → Acotado en todas direcciones → Elipsoide
> → Acotado en dos direcciones → Hiperboloide
> → Acotado en una dirección → Paraboloide
> → No acotado → Cono, cilindro o plano
> ```
> 
> **PASO 4: Clasificar definitivamente**
> 
> ```
> Combinar toda la información:
> - Tipo de curvas
> - Crecimiento/decrecimiento
> - Dominio de existencia
> - Orientación
> 
> → Identificar la superficie única que coincide
> ```

## 📊 Patrones Característicos de cada Superficie

### 🔵 Elipsoide: El Patrón de "Encogimiento"

> [!note]- 🥚 Patrón: Elipses que decrecen hasta un punto
> 
> **Ecuación:** x²/a² + y²/b² + z²/c² = 1
> 
> **Patrón de secciones z = k:**
> 
> ```
> Curva resultante: x²/a² + y²/b² = 1 - k²/c²
> 
> Análisis del patrón:
> 
> k = 0:    x²/a² + y²/b² = 1       (ELIPSE MÁXIMA)
> k = c/2:  x²/a² + y²/b² = 3/4     (elipse más pequeña)
> k = c:    x²/a² + y²/b² = 0       (PUNTO)
> k > c:    NO EXISTE                (fuera del dominio)
> 
> CARACTERÍSTICA ÚNICA:
> → Las elipses DECRECEN hasta colapsar en un punto
> → Existe un valor MÁXIMO de |k| = c
> → Crecimiento: proporcional a √(1 - k²/c²)
> ```
> 
> **Patrón de secciones verticales (y = k, x = k):**
> 
> ```
> TODAS son ELIPSES
> También decrecen desde un máximo
> 
> Ejemplo y = k:
> x²/a² + z²/c² = 1 - k²/b²
> 
> ELIPSE que existe solo para |k| ≤ b
> ```
> 
> **FIRMA DE IDENTIFICACIÓN:**
> 
> ✅ Secciones horizontales: **Elipses decrecientes**  
> ✅ Secciones verticales: **Elipses decrecientes**  
> ✅ Dominio: **Acotado en todas direcciones**  
> ✅ Existencia: **Solo |k| ≤ c (horizontal), |k| ≤ b, |k| ≤ a**
> 
> **Si ves este patrón → ELIPSOIDE**

### 🎪 Paraboloide Elíptico: El Patrón de "Expansión desde Punto"

> [!success]- 🍶 Patrón: Elipses crecientes desde un punto
> 
> **Ecuación:** z = x²/a² + y²/b²
> 
> **Patrón de secciones z = k:**
> 
> ```
> Curva resultante: x²/a² + y²/b² = k
> 
> Análisis del patrón:
> 
> k = 0:    x²/a² + y²/b² = 0       (PUNTO - vértice)
> k = 1:    x²/a² + y²/b² = 1       (elipse)
> k = 4:    x²/a² + y²/b² = 4       (elipse más grande)
> k < 0:    NO EXISTE                (paraboloide solo arriba)
> 
> CARACTERÍSTICA ÚNICA:
> → Las elipses CRECEN desde un punto (el vértice)
> → Solo existen para k ≥ 0 (un solo lado)
> → Crecimiento: proporcional a √k
> → Semiejes: a√k y b√k
> ```
> 
> **Patrón de secciones verticales (y = k, x = k):**
> 
> ```
> TODAS son PARÁBOLAS que abren hacia arriba
> 
> Ejemplo y = k:
> z = x²/a² + k²/b²
> 
> PARÁBOLA con vértice en (0, k, k²/b²)
> Todas tienen la misma forma
> ```
> 
> **FIRMA DE IDENTIFICACIÓN:**
> 
> ✅ Secciones horizontales: **Elipses crecientes desde punto**  
> ✅ Secciones verticales: **Parábolas (todas hacia arriba)**  
> ✅ Dominio: **Solo k ≥ 0** (o k ≤ 0 si abre hacia abajo)  
> ✅ Crecimiento: **Proporcional a √k**
> 
> **Si ves este patrón → PARABOLOIDE ELÍPTICO**

### 🦋 Paraboloide Hiperbólico: El Patrón de "Rotación"

> [!warning]- 🎢 Patrón: Hipérbolas que rotan, rectas en el medio
> 
> **Ecuación:** z = x²/a² - y²/b²
> 
> **Patrón de secciones z = k:**
> 
> ```
> Curva resultante: x²/a² - y²/b² = k
> 
> Análisis del patrón:
> 
> k > 0:    x²/(a²k) - y²/(b²k) = 1    (HIPÉRBOLA - eje en X)
> k = 0:    x²/a² - y²/b² = 0           (DOS RECTAS CRUZADAS)
>           x/a = ±y/b
> k < 0:    y²/(b²|k|) - x²/(a²|k|) = 1 (HIPÉRBOLA - eje en Y)
> 
> CARACTERÍSTICA ÚNICA:
> → Las hipérbolas CAMBIAN de orientación
> → Para k > 0: eje transversal en X
> → Para k < 0: eje transversal en Y
> → En k = 0: DOS RECTAS (punto silla)
> → Existe para TODO k ∈ ℝ
> ```
> 
> **Patrón de secciones verticales:**
> 
> ```
> Secciones y = k:
> z = x²/a² - k²/b²
> PARÁBOLA hacia ARRIBA
> 
> Secciones x = k:
> z = k²/a² - y²/b²
> PARÁBOLA hacia ABAJO
> 
> CARACTERÍSTICA ÚNICA:
> → Parábolas en direcciones OPUESTAS
> → Una abre arriba, otra abajo
> ```
> 
> **FIRMA DE IDENTIFICACIÓN:**
> 
> ✅ Secciones horizontales: **Hipérbolas que rotan 90°**  
> ✅ En z = 0: **DOS RECTAS CRUZADAS** (distintivo único)  
> ✅ Secciones verticales: **Parábolas opuestas**  
> ✅ Dominio: **Todo k ∈ ℝ**
> 
> **Si ves este patrón → PARABOLOIDE HIPERBÓLICO**

### 🎪 Hiperboloide de Una Hoja: El Patrón de "Cintura"

> [!info]- 🍾 Patrón: Elipses con mínimo en el centro
> 
> **Ecuación:** x²/a² + y²/b² - z²/c² = 1
> 
> **Patrón de secciones z = k:**
> 
> ```
> Curva resultante: x²/a² + y²/b² = 1 + k²/c²
> 
> Análisis del patrón:
> 
> k = 0:    x²/a² + y²/b² = 1         (ELIPSE MÍNIMA - la cintura)
> k = c:    x²/a² + y²/b² = 2         (elipse más grande)
> k = 2c:   x²/a² + y²/b² = 5         (elipse aún más grande)
> 
> CARACTERÍSTICA ÚNICA:
> → Las elipses CRECEN desde una elipse mínima (NO desde punto)
> → La elipse más pequeña está en z = 0
> → Existe para TODO k ∈ ℝ
> → Crecimiento: proporcional a √(1 + k²/c²)
> → Semiejes: a√(1+k²/c²) y b√(1+k²/c²)
> ```
> 
> **Patrón de secciones verticales:**
> 
> ```
> Secciones y = k:
> x²/a² - z²/c² = 1 - k²/b²
> 
> |k| < b:  HIPÉRBOLA (eje en X)
> k = ±b:   DOS RECTAS
> |k| > b:  HIPÉRBOLA (eje en Z)
> 
> TODAS son HIPÉRBOLAS (o rectas)
> ```
> 
> **FIRMA DE IDENTIFICACIÓN:**
> 
> ✅ Secciones horizontales: **Elipses crecientes desde elipse mínima**  
> ✅ Secciones verticales: **Hipérbolas**  
> ✅ Dominio: **Todo k ∈ ℝ** (sin gaps)  
> ✅ Tamaño mínimo: **En z = 0** (la cintura)
> 
> **Si ves este patrón → HIPERBOLOIDE DE UNA HOJA**

### 🎪 Hiperboloide de Dos Hojas: El Patrón de "Gap"

> [!warning]- 🎈 Patrón: Gap en el medio, elipses en los extremos
> 
> **Ecuación:** x²/a² - y²/b² - z²/c² = 1
> 
> **Patrón de secciones z = k:**
> 
> ```
> Curva resultante: x²/a² - y²/b² = 1 + k²/c²
> 
> Para todo k: HIPÉRBOLA con eje transversal en X
> 
> → Todas las secciones horizontales son hipérbolas
> → Todas tienen la misma orientación (eje en X)
> → NO hay cambio de orientación
> → Existen para todo k ∈ ℝ
> ```
> 
> **Patrón de secciones verticales (perpendiculares al eje):**
> 
> ```
> Secciones x = k:
> y²/b² + z²/c² = k²/a² - 1
> 
> |k| < a:  NO EXISTE                (GAP)
> k = ±a:   PUNTO (vértices)
> |k| > a:  ELIPSE
> 
> CARACTERÍSTICA ÚNICA:
> → Existe un GAP: -a < k < a
> → DOS HOJAS SEPARADAS: k ≥ a y k ≤ -a
> → Las elipses crecen desde los vértices
> ```
> 
> **FIRMA DE IDENTIFICACIÓN:**
> 
> ✅ Secciones horizontales: **Hipérbolas (sin rotar)**  
> ✅ Secciones perpendiculares: **Gap + Elipses**  
> ✅ Dominio: **Solo |k| ≥ a** (DOS hojas separadas)  
> ✅ Vértices: **En k = ±a**
> 
> **Si ves este patrón → HIPERBOLOIDE DE DOS HOJAS**

### 🎪 Cono Elíptico: El Patrón de "Crecimiento Lineal"

> [!tip]- 🍦 Patrón: Elipses con crecimiento lineal, vértice en origen
> 
> **Ecuación:** x²/a² + y²/b² = z²/c²
> 
> **Patrón de secciones z = k:**
> 
> ```
> Curva resultante: x²/a² + y²/b² = k²/c²
> 
> Análisis del patrón:
> 
> k = 0:    x²/a² + y²/b² = 0         (PUNTO en el origen)
> k ≠ 0:    x²/(a²k²/c²) + y²/(b²k²/c²) = 1
> 
> ELIPSE con semiejes:
> - a|k|/c
> - b|k|/c
> 
> CARACTERÍSTICA ÚNICA:
> → Crecimiento LINEAL con k (no √k)
> → Semiejes proporcionales a |k|
> → Pasa por el ORIGEN (k = 0 da punto)
> → Simetría perfecta: k y -k dan la misma elipse
> ```
> 
> **Patrón de secciones verticales:**
> 
> ```
> Secciones y = k (k ≠ 0):
> x²/a² - z²/c² = -k²/b²
> z²/c² - x²/a² = k²/b²
> 
> HIPÉRBOLA con eje en Z
> 
> Sección y = 0:
> x²/a² = z²/c²
> z = ±(c/a)x
> 
> DOS RECTAS que pasan por el origen
> 
> CARACTERÍSTICA ÚNICA:
> → Todas las secciones que pasan por el origen son RECTAS
> → Estas rectas son las GENERATRICES del cono
> ```
> 
> **FIRMA DE IDENTIFICACIÓN:**
> 
> ✅ Secciones horizontales: **Elipses con crecimiento lineal**  
> ✅ En z = 0: **PUNTO** (vértice en origen)  
> ✅ Secciones por el origen: **DOS RECTAS**  
> ✅ Crecimiento: **Proporcional a |k|** (no √k)
> 
> **Si ves este patrón → CONO ELÍPTICO**

## 📋 Tabla Maestra de Clasificación

> [!example]- 🎯 Guía Rápida de Identificación
> 
> |Superficie|Secciones z=k|Crecimiento|Secciones verticales|Dominio z|Característica única|
> |---|---|---|---|---|---|
> |**Elipsoide**|Elipses|**Decreciente** hasta punto|Elipses|\|k\| ≤ c|Superficie cerrada|
> |**Paraboloide elíptico**|Elipses|Desde **punto**, ∝ √k|Parábolas (misma dir.)|k ≥ 0|Un solo lado|
> |**Paraboloide hiperbólico**|Hipérbolas|**Rotan 90°**|Parábolas opuestas|Todo k|**Rectas en k=0**|
> |**Hiperboloide 1 hoja**|Elipses|Desde **elipse mín.**, ∝ √(1+k²)|Hipérbolas|Todo k|Cintura mínima|
> |**Hiperboloide 2 hojas**|Hipérbolas|No rotan|Elipses con **gap**|\|k\| ≥ a|Dos hojas separadas|
> |**Cono elíptico**|Elipses|**Lineal** ∝ \|k\||Hipérbolas + rectas|Todo k|**Punto en k=0**, crecimiento lineal|

## 🎯 Ejemplos de Clasificación Completa

> [!example]- 📝 Ejercicios Resueltos Paso a Paso
> 
> ### **Ejemplo 1: Identificar x² + 4y² + 9z² = 36**
> 
> **PASO 1: Forma estándar**
> 
> ```
> x²/36 + y²/9 + z²/4 = 1
> 
> Parámetros: a² = 36, b² = 9, c² = 4
> a = 6, b = 3, c = 2
> ```
> 
> **PASO 2: Secciones z = k**
> 
> ```
> x²/36 + y²/9 + k²/4 = 1
> x²/36 + y²/9 = 1 - k²/4
> 
> Análisis:
> - Para k = 0: x²/36 + y²/9 = 1 (elipse máxima)
> - Para k = 1: x²/36 + y²/9 = 3/4 (elipse más pequeña)
> - Para k = 2: x²/36 + y²/9 = 0 (punto)
> - Para |k| > 2: NO EXISTE
> 
> PATRÓN: Elipses DECRECIENTES
> ```
> 
> **PASO 3: Dominio**
> 
> ```
> Solo existe para |k| ≤ 2
> → Superficie ACOTADA
> ```
> 
> **PASO 4: Secciones verticales**
> 
> ```
> y = k:
> x²/36 + z²/4 = 1 - k²/9
> 
> También ELIPSES decrecientes
> Solo existen para |k| ≤ 3
> ```
> 
> **CLASIFICACIÓN:**
> 
> ✅ Elipses decrecientes  
> ✅ Acotada en todas direcciones  
> ✅ Todas las secciones son elipses
> 
> **→ ELIPSOIDE** ✓
> 
> ---
> 
> ### **Ejemplo 2: Identificar z = x² - y²**
> 
> **PASO 1: Reconocer forma**
> 
> ```
> z = x²/1 - y²/1
> 
> Parámetros: a = 1, b = 1
> ```
> 
> **PASO 2: Secciones z = k**
> 
> ```
> k = x² - y²
> x² - y² = k
> 
> Para k > 0:  x² - y² = k  → hipérbola (eje en X)
> Para k = 0:  x² - y² = 0  → x = ±y (DOS RECTAS)
> Para k < 0:  y² - x² = |k| → hipérbola (eje en Y)
> 
> PATRÓN: Hipérbolas que ROTAN 90°
> + DOS RECTAS en k = 0
> ```
> 
> **PASO 3: Dominio**
> 
> ```
> Existe para TODO k ∈ ℝ
> ```
> 
> **PASO 4: Secciones verticales**
> 
> ```
> y = k:
> z = x² - k²
> PARÁBOLA que abre ARRIBA
> 
> x = k:
> z = k² - y²
> PARÁBOLA que abre ABAJO
> 
> PATRÓN: Parábolas OPUESTAS
> ```
> 
> **CLASIFICACIÓN:**
> 
> ✅ Hipérbolas que rotan  
> ✅ DOS RECTAS en z = 0  
> ✅ Parábolas opuestas verticalmente
> 
> **→ PARABOLOIDE HIPERBÓLICO** ✓
> 
> ---
> 
> ### **Ejemplo 3: Identificar x² + y² - z² = 4**
> 
> **PASO 1: Forma estándar**
> 
> ```
> x²/4 + y²/4 - z²/4 = 1
> 
> Parámetros: a = 2, b = 2, c = 2
> (de revolución, porque a = b)
> ```
> 
> **PASO 2: Secciones z = k**
> 
> ```
> x²/4 + y²/4 = 1 + k²/4
> x² + y² = 4 + k²
> 
> CÍRCULOS con radio r = √(4 + k²)
> 
> Para k = 0: radio = 2 (círculo MÍNIMO)
> Para k = ±2: radio = √8 = 2√2
> Para k = ±4: radio = √20 = 2√5
> 
> PATRÓN: Círculos CRECIENTES desde mínimo
> Existe para TODO k
> ```
> 
> **PASO 3: Secciones verticales**
> 
> ```
> y = k:
> x²/4 - z²/4 = 1 - k²/4
> 
> |k| < 2:  hipérbola (eje en X)
> k = ±2:   DOS RECTAS
> |k| > 2:  hipérbola (eje en Z)
> 
> TODAS son HIPÉRBOLAS
> ```
> 
> **CLASIFICACIÓN:**
> 
> ✅ Círculos crecientes desde mínimo  
> ✅ Existe para todo k  
> ✅ Secciones verticales son hipérbolas  
> ✅ Tamaño mínimo en z = 0
> 
> **→ HIPERBOLOIDE DE UNA HOJA** ✓  
> (de revolución)
> 
> ---
> 
> ### **Ejemplo 4: Identificar z = 2x² + 3y²**
> 
> **PASO 1: Forma estándar**
> 
> ```
> z = x²/(1/2) + y²/(1/3)
> 
> Parámetros: a² = 1/2, b² = 1/3
> ```
> 
> **PASO 2: Secciones z = k**
> 
> ```
> k = 2x² + 3y²
> 2x² + 3y² = k
> 
> Para k > 0:
> x²/(k/2) + y²/(k/3) = 1
> 
> ELIPSE con semiejes √(k/2) y √(k/3)
> 
> Para k = 0: punto (0,0,0)
> Para k = 1: x²/(1/2) + y²/(1/3) = 1
> Para k = 4: x²/2 + y²/(4/3) = 1
> Para k < 0: NO EXISTE
> 
> PATRÓN: Elipses crecientes desde PUNTO
> Crecimiento ∝ √k
> ```
> 
> **PASO 3: Dominio**
> 
> ```
> Solo existe para k ≥ 0
> ```
> 
> **PASO 4: Secciones verticales**
> 
> ```
> y = k:
> z = 2x² + 3k²
> PARÁBOLA hacia arriba
> 
> x = k:
> z = 2k² + 3y²
> PARÁBOLA hacia arriba
> 
> TODAS las parábolas abren hacia arriba
> ```
> 
> **CLASIFICACIÓN:**
> 
> ✅ Elipses crecientes desde punto  
> ✅ Solo k ≥ 0  
> ✅ Parábolas verticales (misma orientación)  
> ✅ Crecimiento ∝ √k
> 
> **→ PARABOLOIDE ELÍPTICO** ✓
> 
> ---
> 
> ### **Ejemplo 5: Identificar 4x² - y² - z² = 4**
> 
> **PASO 1: Forma estándar**
> ````
> x²/1 - y²/4 - z²/4 = 1
> 
> Parámetros: a = 1, b = 2, c = 2
> ```
> 
> **PASO 2: Secciones z = k**
> 
> ```
> x²/1 - y²/4 - k²/4 = 1
> x²/1 - y²/4 = 1 + k²/4
> 
> Para todo k: HIPÉRBOLA con eje transversal en X
> 
> NO cambian de orientación
> Todas abren en dirección X
> ```
> 
> **PASO 3: Secciones verticales (perpendiculares al eje)**
> 
> ```
> x = k:
> y²/4 + z²/4 = k²/1 - 1
> y² + z² = 4(k² - 1)
> 
> Para |k| < 1: NO EXISTE (GAP)
> Para k = ±1: PUNTO (vértices)
> Para |k| > 1: CÍRCULO
> 
> PATRÓN: GAP + dos hojas separadas
> ```
> 
> **PASO 4: Dominio**
> 
> ```
> Solo existe para |k| ≥ 1
> DOS HOJAS: x ≥ 1 y x ≤ -1
> ```
> 
> **CLASIFICACIÓN:**
> 
> ✅ Hipérbolas (sin rotar)  
> ✅ Gap: -1 < x < 1  
> ✅ Dos hojas separadas  
> ✅ Círculos en secciones perpendiculares  
> 
> **→ HIPERBOLOIDE DE DOS HOJAS** ✓  
> (de revolución en yz)
> 
> ---
> 
> ### **Ejemplo 6: Identificar x² + y² = z²**
> 
> **PASO 1: Reconocer forma**
> 
> ```
> x²/1 + y²/1 = z²/1
> 
> Parámetros: a = 1, b = 1, c = 1
> (de revolución)
> ```
> 
> **PASO 2: Secciones z = k**
> 
> ```
> x² + y² = k²
> 
> Para k ≠ 0: CÍRCULO con radio |k|
> Para k = 0: PUNTO (vértice en origen)
> 
> PATRÓN: Círculos con crecimiento LINEAL
> Radio = |k| (no √k)
> ```
> 
> **PASO 3: Secciones verticales**
> 
> ```
> y = 0:
> x² = z²
> z = ±x
> 
> DOS RECTAS que pasan por el origen
> 
> y = k (k ≠ 0):
> x² - z² = -k²
> z² - x² = k²
> 
> HIPÉRBOLA
> ```
> 
> **CLASIFICACIÓN:**
> 
> ✅ Círculos con crecimiento lineal  
> ✅ Punto en z = 0  
> ✅ Rectas por el origen  
> ✅ Crecimiento ∝ |k| (no √k)  
> 
> **→ CONO CIRCULAR** ✓

## 🎨 Diagrama de Flujo de Clasificación

```mermaid
graph TD
    A[Analizar secciones z = k] --> B{¿Qué curvas?}
    
    B -->|Elipses| C{¿Crecen o decrecen?}
    B -->|Hipérbolas| D{¿Cambian orientación?}
    
    C -->|Decrecen| E{¿Hasta qué?}
    C -->|Crecen| F{¿Desde qué?}
    
    E -->|Hasta punto| G[ELIPSOIDE]
    
    F -->|Desde punto| H{¿Cómo crecen?}
    F -->|Desde elipse mínima| I[HIPERBOLOIDE 1 HOJA]
    
    H -->|∝ √k| J[PARABOLOIDE ELÍPTICO]
    H -->|∝ k lineal| K[CONO ELÍPTICO]
    
    D -->|Sí + rectas en k=0| L[PARABOLOIDE HIPERBÓLICO]
    D -->|No| M{¿Hay gap?}
    
    M -->|Sí| N[HIPERBOLOIDE 2 HOJAS]
    M -->|No| O{Verificar secciones verticales}
    
    style G fill:#90EE90
    style J fill:#FFD700
    style L fill:#FF6B6B
    style I fill:#87CEEB
    style N fill:#DDA0DD
    style K fill:#F0E68C
````

## 💡 Consejos de Clasificación

> [!tip]- 🎯 Trucos para Identificar Rápidamente
> 
> **Truco 1: Mira primero z = 0**
> 
> ```
> La sección z = 0 revela mucho:
> 
> → Elipse/círculo → puede ser elipsoide, paraboloide elíptico, 
>                     hiperboloide 1 hoja, cono
> → Punto → paraboloide elíptico o cono
> → Hipérbola → hiperboloide 2 hojas
> → DOS RECTAS → paraboloide hiperbólico o cono
> ```
> 
> **Truco 2: Observa el dominio**
> 
> ```
> ¿Para qué valores de k existen secciones?
> 
> → Solo k ≥ 0 o k ≤ 0 → Paraboloide
> → Solo |k| ≤ c → Elipsoide
> → Solo |k| ≥ a → Hiperboloide 2 hojas
> → Todo k → Hiperboloide 1 hoja, paraboloide hiperbólico, cono
> ```
> 
> **Truco 3: Cuenta los signos en la ecuación**
> 
> ```
> En forma x²/a² ± y²/b² ± z²/c² = d:
> 
> (+, +, +) = 1 → Elipsoide
> (+, +, +) = 0 → Punto (degenerado)
> (+, +, -) = 1 → Hiperboloide 1 hoja
> (+, -, -) = 1 → Hiperboloide 2 hojas
> (+, +, -) = 0 → Cono
> 
> Si z está solo (z = ...) → Paraboloide
> ```
> 
> **Truco 4: Tipo de crecimiento**
> 
> ```
> Elipses horizontales crecen como:
> 
> → √(1 - k²) → Elipsoide (decreciente)
> → √k → Paraboloide elíptico
> → √(1 + k²) → Hiperboloide 1 hoja
> → |k| → Cono (lineal)
> ```
> 
> **Truco 5: Secciones verticales**
> 
> ```
> → Todas elipses → Elipsoide
> → Todas parábolas (misma dir.) → Paraboloide elíptico
> → Parábolas opuestas → Paraboloide hiperbólico
> → Todas hipérbolas → Hiperboloide
> → Hipérbolas + rectas por origen → Cono
> ```

## 🔗 Conexiones con el Sistema de Notas

> [!quote]- 🌟 Enlaces Conceptuales
> 
> **Prerequisites (Prerrequisitos):**
> 
> - [[02 - Vectores en R3]] - Fundamentos vectoriales
> - [[03 - Aplicaciones geométricas básicas]] - Geometría en 3D
> - [[Cónicas]] - Círculos, elipses, parábolas, hipérbolas en 2D
> - [[Álgebra de ecuaciones cuadráticas]] - Formas canónicas
> 
> **Temas relacionados:**
> 
> - [[Coordenadas cilíndricas y esféricas]] - Sistemas alternativos
> - [[Ecuaciones de superficies]] - Representaciones
> - [[Curvas de nivel]] - Visualización 2D
> - [[Gradiente y superficies de nivel]] - Cálculo vectorial
> 
> **Aplicaciones:**
> 
> - [[Optimización en superficies]] - Máximos y mínimos
> - [[Integrales de superficie]] - Cálculo multivariable
> - [[Campos vectoriales en superficies]] - Física matemática
> - [[Geometría diferencial]] - Curvaturas
> 
> **Temas siguientes:**
> 
> - [[05 - Superficies de revolución]] - Rotación de curvas
> - [[06 - Ecuaciones paramétricas de superficies]] - Parametrización
> - [[Topología de superficies]] - Propiedades globales

---

**Tags:** #superficies #clasificación #secciones-transversales #cuadráticas #elipsoide #paraboloide #hiperboloide #cono #geometría-analítica #R3 #visualización #matemáticas #university #cálculo-multivariable