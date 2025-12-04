# 🎯 Teoremas Fundamentales del Espacio Vectorial

## 🌟 Concepto Fundamental

> [!info]- Visión General **Los teoremas fundamentales de espacios vectoriales son consecuencias lógicas que se derivan de los axiomas básicos. Aunque parecen "obvios" intuitivamente, su demostración rigurosa es esencial para la construcción formal de la teoría. Estos teoremas establecen propiedades cruciales sobre la unicidad de elementos especiales, comportamiento del cero, cancelación y otras relaciones algebraicas.**
> 
> **Importancia:**
> 
> - **Rigor matemático:** Fundamentan la teoría formal
> - **Garantías de existencia:** Aseguran elementos únicos
> - **Propiedades operativas:** Simplifican cálculos
> - **Base para resultados avanzados:** Cimientos de teoremas más complejos
> - **Coherencia estructural:** Verifican que los axiomas no sean contradictorios

### 📖 Contexto Histórico

> [!note]- Desarrollo de la Fundamentación **Era Pre-Axiomática (1600-1850):**
> 
> - **Descartes, Newton, Leibniz:** Uso intuitivo de vectores
> - Propiedades asumidas sin demostración formal
> - Énfasis en aplicaciones geométricas y físicas
> 
> **Formalización Temprana (1850-1900):**
> 
> - **Grassmann (1844):** Primeros intentos axiomáticos
> - **Hamilton (1843):** Cuaterniones y álgebra no conmutativa
> - **Peano (1888):** Primera axiomatización explícita
>     - Lista de propiedades fundamentales
>     - Reconoce necesidad de demostrar resultados básicos
> 
> **Rigor Moderno (1900-1930):**
> 
> - **Steinitz (1910):** Teoría abstracta de espacios vectoriales
> - **Énfasis en unicidad:** Vector cero, opuestos
> - **Banach, Hilbert:** Espacios de dimensión infinita
> - **Separación clara:** Axiomas vs. Teoremas derivados
> 
> **Era Bourbaki (1940-presente):**
> 
> - **Estructura algebraica unificada**
> - **Demostraciones rigurosas obligatorias**
> - **Énfasis pedagógico:** No asumir "propiedades obvias"
> - **Estándar actual:** Todo teorema debe probarse desde axiomas

## 📐 Lista Completa de Axiomas (Recordatorio)

> [!note]- Axiomas Base **Para un espacio vectorial (V, +, ·) sobre campo 𝔽:**
> 
> **AXIOMAS DE LA SUMA:**
> 
> ```
> (A1) CLAUSURA: ∀u, v ∈ V, u + v ∈ V
> 
> (A2) CONMUTATIVA: ∀u, v ∈ V, u + v = v + u
> 
> (A3) ASOCIATIVA: ∀u, v, w ∈ V, (u + v) + w = u + (v + w)
> 
> (A4) ELEMENTO NEUTRO: ∃0 ∈ V tal que ∀v ∈ V, v + 0 = v
> 
> (A5) ELEMENTO OPUESTO: ∀v ∈ V, ∃(-v) ∈ V tal que v + (-v) = 0
> ```
> 
> **AXIOMAS DE LA MULTIPLICACIÓN ESCALAR:**
> 
> ```
> (M1) CLAUSURA: ∀c ∈ 𝔽, ∀v ∈ V, c·v ∈ V
> 
> (M2) DISTRIBUTIVA (vectores): ∀c ∈ 𝔽, ∀u, v ∈ V,
>      c·(u + v) = c·u + c·v
> 
> (M3) DISTRIBUTIVA (escalares): ∀c, d ∈ 𝔽, ∀v ∈ V,
>      (c + d)·v = c·v + d·v
> 
> (M4) ASOCIATIVA MIXTA: ∀c, d ∈ 𝔽, ∀v ∈ V,
>      c·(d·v) = (cd)·v
> 
> (M5) ELEMENTO NEUTRO: ∀v ∈ V, 1·v = v
>      (donde 1 es la unidad de 𝔽)
> ```
> 
> **Nota:** A partir de estos 10 axiomas demostraremos TODOS los teoremas siguientes.

## 🎯 Teorema 1: Unicidad del Vector Cero

> [!important]- Vector Neutro Único **Teorema:** El vector cero (elemento neutro de la suma) es único.
> 
> **Enunciado formal:**
> 
> ```
> Si 0 y 0' son vectores en V tales que:
> ∀v ∈ V, v + 0 = v
> ∀v ∈ V, v + 0' = v
> 
> Entonces: 0 = 0'
> ```
> 
> **Demostración:**
> 
> ```
> Supongamos que 0 y 0' son ambos vectores cero.
> 
> Esto significa:
> - Para todo v ∈ V: v + 0 = v    (0 es neutro)
> - Para todo v ∈ V: v + 0' = v   (0' es neutro)
> 
> Paso 1: Aplicar primera propiedad con v = 0'
> 0' + 0 = 0'                               ... (1)
> 
> Paso 2: Aplicar segunda propiedad con v = 0
> 0 + 0' = 0                                ... (2)
> 
> Paso 3: Usar conmutatividad (A2) en (1)
> 0' + 0 = 0 + 0'                           ... (3)
> 
> Paso 4: De (1), (2) y (3):
> 0' = 0' + 0 = 0 + 0' = 0
> 
> Por tanto: 0' = 0
> 
> ∎ (Fin de la demostración)
> ```
> 
> **Consecuencia:**
> 
> ```
> Podemos hablar de "EL" vector cero (no "UN" vector cero)
> 
> Notación unívoca: 0
> ```

> [!example]- Interpretación y Ejemplos **¿Por qué es importante?**
> 
> ```
> Sin este teorema, podría haber múltiples "ceros"
> Lo cual sería inconsistente:
> 
> Supongamos 0 ≠ 0' ambos neutros
> Entonces v + 0 = v y v + 0' = v para todo v
> Pero esto llevaría a contradicciones en ecuaciones
> ```
> 
> **Ejemplo en ℝ²:**
> 
> ```
> ¿Podría (0,0) y (1,1) ser ambos vectores cero?
> 
> NO, porque:
> (0,0) + (1,1) = (1,1) ≠ (0,0)
> 
> Si (1,1) fuera cero: (0,0) + (1,1) = (0,0)
> Contradicción.
> 
> Solo (0,0) es el vector cero en ℝ²
> ```
> 
> **Ejemplo en P(ℝ):**
> 
> ```
> El único polinomio neutro es p(x) = 0
> 
> No puede ser p(x) = 1 porque:
> q(x) + 1 ≠ q(x) para polinomios q no nulos
> ```

## 🎯 Teorema 2: Unicidad del Vector Opuesto

> [!important]- Inverso Aditivo Único **Teorema:** Para cada vector v ∈ V, su opuesto (inverso aditivo) es único.
> 
> **Enunciado formal:**
> 
> ```
> Si w y w' son vectores en V tales que:
> v + w = 0
> v + w' = 0
> 
> Entonces: w = w'
> ```
> 
> **Demostración:**
> 
> ```
> Supongamos v + w = 0 y v + w' = 0
> 
> Paso 1: Partir de v + w = 0
> 
> Paso 2: Sumar w' a ambos lados por la izquierda
> w' + (v + w) = w' + 0
> 
> Paso 3: Usar asociatividad (A3)
> (w' + v) + w = w' + 0
> 
> Paso 4: w' + v = 0 (por hipótesis), y w' + 0 = w' (por A4)
> 0 + w = w'
> 
> Paso 5: 0 es neutro (A4)
> w = w'
> 
> ∎
> ```
> 
> **Demostración alternativa:**
> 
> ```
> v + w = 0        ... (1)
> v + w' = 0       ... (2)
> 
> De (1) y (2):
> v + w = v + w'
> 
> Sumar -v a ambos lados por la izquierda:
> -v + (v + w) = -v + (v + w')
> 
> Por asociatividad:
> (-v + v) + w = (-v + v) + w'
> 
> Como -v + v = 0:
> 0 + w = 0 + w'
> 
> Por A4:
> w = w'
> 
> ∎
> ```
> 
> **Consecuencia:**
> 
> ```
> Para cada v existe un ÚNICO -v tal que v + (-v) = 0
> 
> Notación estándar: -v (el opuesto de v)
> ```

> [!example]- Ejemplos e Interpretación **En ℝ²:**
> 
> ```
> v = (3, -5)
> 
> Su opuesto es único: -v = (-3, 5)
> 
> No puede haber otro w ≠ (-3, 5) tal que v + w = 0
> ```
> 
> **En matrices M₂ₓ₂(ℝ):**
> 
> ```
> A = ⎡2  -1⎤
>     ⎣3   4⎦
> 
> Único opuesto: -A = ⎡-2   1⎤
>                     ⎣-3  -4⎦
> 
> A + (-A) = O (matriz cero)
> ```
> 
> **Importancia:**
> 
> ```
> Podemos definir resta sin ambigüedad:
> u - v := u + (-v)
> 
> Esta definición es coherente porque -v es único
> ```

## 🎯 Teorema 3: Producto por Escalar Cero

> [!important]- Cero Escalar Anula Cualquier Vector **Teorema:** Para todo vector v ∈ V:
> 
> ```
> 0·v = 0
> 
> (El escalar cero multiplicado por cualquier vector da el vector cero)
> ```
> 
> **Demostración:**
> 
> ```
> Sea v ∈ V cualquiera.
> 
> Paso 1: Usar que 0 = 0 + 0 en el campo 𝔽
> 0·v = (0 + 0)·v
> 
> Paso 2: Aplicar distributividad de escalares (M3)
> 0·v = 0·v + 0·v
> 
> Paso 3: Tenemos 0·v = 0·v + 0·v
> Sumar -(0·v) a ambos lados:
> 0·v + (-(0·v)) = (0·v + 0·v) + (-(0·v))
> 
> Paso 4: Lado izquierdo, por definición de opuesto:
> 0 = (0·v + 0·v) + (-(0·v))
> 
> Paso 5: Lado derecho, por asociatividad:
> 0 = 0·v + (0·v + (-(0·v)))
> 
> Paso 6: 0·v + (-(0·v)) = 0
> 0 = 0·v + 0
> 
> Paso 7: Por A4 (0 es neutro):
> 0 = 0·v
> 
> Por tanto: 0·v = 0
> 
> ∎
> ```
> 
> **Demostración más corta (usando cancelación):**
> 
> ```
> 0·v = (0 + 0)·v         (0 = 0 + 0 en 𝔽)
>     = 0·v + 0·v         (M3)
> 
> Sumando -(0·v):
> 0·v + (-(0·v)) = (0·v + 0·v) + (-(0·v))
> 0 = 0·v + (0·v + (-(0·v)))
> 0 = 0·v + 0
> 0 = 0·v
> 
> ∎
> ```

> [!example]- Ejemplos y Consecuencias **En ℝ³:**
> 
> ```
> 0·(2, -3, 5) = (0, 0, 0) = 0
> 
> El escalar 0 "anula" cualquier vector
> ```
> 
> **En polinomios:**
> 
> ```
> 0·(x² + 3x - 1) = 0 (polinomio cero)
> 
> Todos los coeficientes se vuelven cero
> ```
> 
> **En matrices:**
> 
> ```
> 0·⎡a b⎤ = ⎡0 0⎤
>   ⎣c d⎦   ⎣0 0⎦
> ```
> 
> **Advertencia común:**
> 
> ```
> ⚠️ NO confundir:
> - 0 (escalar cero en 𝔽)
> - 0 (vector cero en V)
> 
> El teorema conecta ambos: escalar 0 produce vector 0
> ```

## 🎯 Teorema 4: Producto de Vector Cero

> [!important]- Escalar por Vector Cero **Teorema:** Para todo escalar c ∈ 𝔽:
> 
> ```
> c·0 = 0
> 
> (Cualquier escalar multiplicado por el vector cero da el vector cero)
> ```
> 
> **Demostración:**
> 
> ```
> Sea c ∈ 𝔽 cualquiera.
> 
> Paso 1: Usar que 0 = 0 + 0 en V
> c·0 = c·(0 + 0)
> 
> Paso 2: Aplicar distributividad de vectores (M2)
> c·0 = c·0 + c·0
> 
> Paso 3: Tenemos c·0 = c·0 + c·0
> Sumar -(c·0) a ambos lados:
> c·0 + (-(c·0)) = (c·0 + c·0) + (-(c·0))
> 
> Paso 4: Simplificar usando opuestos y asociatividad:
> 0 = c·0 + (c·0 + (-(c·0)))
> 0 = c·0 + 0
> 0 = c·0
> 
> Por tanto: c·0 = 0
> 
> ∎
> ```

> [!example]- Ejemplos **En ℝ²:**
> 
> ```
> 5·(0, 0) = (0, 0)
> (-3)·(0, 0) = (0, 0)
> π·(0, 0) = (0, 0)
> ```
> 
> **En funciones:**
> 
> ```
> c·f_cero = f_cero
> 
> donde f_cero(x) = 0 para todo x
> 
> Cualquier múltiplo de la función cero es la función cero
> ```
> 
> **Simetría con Teorema 3:**
> 
> ```
> Teorema 3: 0·v = 0  (cero escalar)
> Teorema 4: c·0 = 0  (cero vector)
> 
> Complementarios y simétricos
> ```

## 🎯 Teorema 5: Producto por Menos Uno

> [!important]- (-1) Produce el Opuesto **Teorema:** Para todo vector v ∈ V:
> 
> ```
> (-1)·v = -v
> 
> (Multiplicar por -1 da el opuesto del vector)
> ```
> 
> **Demostración:**
> 
> ```
> Sea v ∈ V cualquiera.
> 
> Necesitamos probar que (-1)·v es el opuesto de v,
> es decir, que v + (-1)·v = 0
> 
> Paso 1: Calcular v + (-1)·v
> v + (-1)·v
> 
> Paso 2: Escribir v = 1·v (por M5)
> = 1·v + (-1)·v
> 
> Paso 3: Aplicar distributividad (M3)
> = (1 + (-1))·v
> 
> Paso 4: 1 + (-1) = 0 en el campo 𝔽
> = 0·v
> 
> Paso 5: Por Teorema 3
> = 0
> 
> Por tanto: v + (-1)·v = 0
> 
> Paso 6: Por unicidad del opuesto (Teorema 2):
> (-1)·v = -v
> 
> ∎
> ```

> [!example]- Ejemplos y Consecuencias **En ℝ³:**
> 
> ```
> v = (2, -3, 5)
> 
> (-1)·v = (-1)·(2, -3, 5)
>        = (-2, 3, -5)
>        = -v ✓
> ```
> 
> **En polinomios:**
> 
> ```
> p(x) = 3x² - 2x + 1
> 
> (-1)·p(x) = -3x² + 2x - 1 = -p(x) ✓
> ```
> 
> **Consecuencia: Definición de resta:**
> 
> ```
> u - v = u + (-v)
>       = u + (-1)·v
> 
> Justifica la notación usual de resta
> ```
> 
> **Propiedad útil:**
> 
> ```
> -(-v) = v
> 
> Demostración:
> -(-v) = (-1)·(-v)
>       = (-1)·((-1)·v)
>       = ((-1)·(-1))·v    (M4)
>       = 1·v              (en 𝔽: (-1)(-1) = 1)
>       = v                (M5)
> ```

## 🎯 Teorema 6: Propiedad del Producto Nulo

> [!important]- Ley del Cero Producto **Teorema:** Para todo c ∈ 𝔽 y v ∈ V:
> 
> ```
> c·v = 0  ⟹  c = 0  o  v = 0
> 
> (Si el producto es cero, entonces al menos uno de los factores es cero)
> ```
> 
> **Demostración:**
> 
> ```
> Supongamos c·v = 0
> 
> Demostraremos por contradicción (o casos):
> 
> CASO 1: c = 0
> Entonces la conclusión es verdadera. ✓
> 
> CASO 2: c ≠ 0
> Necesitamos probar v = 0
> 
> Como c ≠ 0, existe c⁻¹ en 𝔽 tal que c⁻¹·c = 1
> 
> Paso 1: Partir de c·v = 0
> 
> Paso 2: Multiplicar ambos lados por c⁻¹
> c⁻¹·(c·v) = c⁻¹·0
> 
> Paso 3: Lado izquierdo, usar M4
> (c⁻¹·c)·v = c⁻¹·0
> 
> Paso 4: c⁻¹·c = 1
> 1·v = c⁻¹·0
> 
> Paso 5: Por M5 (izquierda) y Teorema 4 (derecha)
> v = 0
> 
> Por tanto, si c ≠ 0, entonces v = 0. ✓
> 
> En ambos casos, c = 0 o v = 0
> 
> ∎
> ```
> 
> **Contrarrecíproca (forma equivalente):**
> 
> ```
> c ≠ 0  y  v ≠ 0  ⟹  c·v ≠ 0
> 
> Si ningún factor es cero, el producto no es cero
> ```

> [!example]- Ejemplos y Aplicaciones **Ejemplo 1:**
> 
> ```
> En ℝ²: Si 3·v = (0,0), entonces v = (0,0)
> 
> Pues 3 ≠ 0, luego v = 0 por el teorema
> ```
> 
> **Ejemplo 2: Resolver ecuación**
> 
> ```
> Encontrar v tal que 5·v = 0 en ℝ³
> 
> Por el teorema: 5 = 0 (imposible) o v = 0
> 
> Como 5 ≠ 0, necesariamente v = 0
> 
> Solución única: v = (0,0,0)
> ```
> 
> **Ejemplo 3: Independencia lineal**
> 
> ```
> ¿Son {v} linealmente independiente si v ≠ 0?
> 
> c·v = 0  y  v ≠ 0  ⟹  c = 0  (por teorema)
> 
> Sí, cualquier vector no nulo es l.i.
> ```
> 
> **Diferencia con números reales:**
> 
> ```
> En ℝ: ab = 0 ⟹ a = 0 o b = 0
> 
> En espacios vectoriales:
> c·v = 0 ⟹ c = 0 o v = 0
> 
> Propiedad análoga pero en contexto diferente
> ```

## 🎯 Teorema 7: Propiedad de Cancelación

> [!important]- Ley de Cancelación Aditiva **Teorema:** Para todo u, v, w ∈ V:
> 
> ```
> u + w = v + w  ⟹  u = v
> 
> (Podemos "cancelar" el mismo sumando de ambos lados)
> ```
> 
> **Demostración:**
> 
> ```
> Supongamos u + w = v + w
> 
> Paso 1: Sumar -w a ambos lados (por la derecha)
> (u + w) + (-w) = (v + w) + (-w)
> 
> Paso 2: Aplicar asociatividad (A3)
> u + (w + (-w)) = v + (w + (-w))
> 
> Paso 3: w + (-w) = 0 por definición de opuesto
> u + 0 = v + 0
> 
> Paso 4: Por A4 (0 es neutro)
> u = v
> 
> ∎
> ```
> 
> **Cancelación por la izquierda:**
> 
> ```
> w + u = w + v  ⟹  u = v
> 
> Demostración:
> w + u = w + v
> Por conmutatividad: u + w = v + w
> Por teorema anterior: u = v
> 
> ∎
> ```

> [!example]- Aplicaciones **Resolver ecuación:**
> 
> ```
> Resolver: v + (2, 3) = (5, 7)
> 
> Método 1 (directo):
> v = (5, 7) - (2, 3) = (3, 4)
> 
> Método 2 (cancelación):
> v + (2, 3) = (5, 7)
> 
> Sumar -(2, 3) a ambos lados:
> v + (2, 3) + (-(2, 3)) = (5, 7) + (-(2, 3))
> v + 0 = (5, 7) + (-2, -3)
> v = (3, 4)
> ```
> 
> **Unicidad de soluciones:**
> 
> ```
> Si u + w = c y v + w = c (mismo c)
> 
> Entonces: u + w = v + w
> Por cancelación: u = v
> 
> La solución de x + w = c es única
> ```

## 🎯 Teorema 8: Cancelación Multiplicativa

> [!important]- Cancelación de Escalares No Nulos **Teorema:** Para todo c ∈ 𝔽 (c ≠ 0) y u, v ∈ V:
> 
> ```
> c·u = c·v  ⟹  u = v
> 
> (Si c ≠ 0, podemos "dividir" por c)
> ```
> 
> **Demostración:**
> 
> ```
> Supongamos c·u = c·v con c ≠ 0
> 
> Paso 1: Como c ≠ 0, existe c⁻¹ en 𝔽
> 
> Paso 2: Multiplicar ambos lados por c⁻¹
> c⁻¹·(c·u) = c⁻¹·(c·v)
> 
> Paso 3: Aplicar asociatividad (M4)
> (c⁻¹·c)·u = (c⁻¹·c)·v
> 
> Paso 4: c⁻¹·c = 1
> 1·u = 1·v
> 
> Paso 5: Por M5
> u = v
> 
> ∎
> ```
> 
> **Contrarrecíproca:**
> 
> ```
> Si c ≠ 0 y u ≠ v, entonces c·u ≠ c·v
> 
> Escalares no nulos preservan desigualdad
> ```

> [!example]- Ejemplos **Ejemplo 1:**
> 
> ```
> Si 3·u = 3·v, entonces u = v
> 
> Pues 3 ≠ 0 permite cancelar
> ```
> 
> **Ejemplo 2: Resolver ecuación**
> 
> ```
> Resolver: 5·v = (10, -15, 20)
> 
> v = (1/5)·(10, -15, 20)
>   = (2, -3, 4)
> 
> Justificación formal:
> 5·v = (10, -15, 20)
> (1/5)·(5·v) = (1/5)·(10, -15, 20)
> ((1/5)·5)·v = (2, -3, 4)
> 1·v = (2, -3, 4)
> v = (2, -3, 4)
> ```
> 
> **Contraejemplo (c = 0):**
> 
> ```
> 0·u = 0·v SIEMPRE (ambos dan 0)
> 
> ¡Pero no implica u = v!
> 
> No se puede "cancelar" 0
> ```

## 🎯 Teorema 9: Distributividad del Opuesto

> [!important]- Distribución de Signo Negativo **Teorema:** Para todo u, v ∈ V:
> 
> ```
> -(u + v) = (-u) + (-v)
> 
> (El opuesto de una suma es la suma de los opuestos)
> ```
> 
> **Demostración:**
> 
> ```
> Necesitamos probar que (-u) + (-v) es el opuesto de u + v
> Es decir: (u + v) + ((-u) + (-v)) = 0
> 
> Paso 1: Calcular (u + v) + ((-u) + (-v))
> 
> Paso 2: Usar asociatividad y conmutatividad repetidamente
> = u + v + (-u) + (-v)
> = u + (-u) + v + (-v)        (reordenar)
> 
> Paso 3: Cada par vector + opuesto = 0
> = 0 + 0
> = 0
> 
> Por tanto (u + v) + ((-u) + (-v)) = 0
> 
> Paso 4: Por unicidad del opuesto:
> (-u) + (-v) es EL opuesto de u + v
> 
> Es decir: -(u + v) = (-u) + (-v)
> 
> ∎
> ```
> 
> **Usando multiplicación por -1:**
> 
> ```
> Demostración alternativa:
> 
> -(u + v) = (-1)·(u + v)           (Teorema 5)
>          = (-1)·u + (-1)·v        (M2)
>          = (-u) + (-v)            (Teorema 5)
> 
> ∎
> ```
> [!example]- Ejemplos **En ℝ²:**
> 
> ```
> u = (3, -2), v = (1, 5)
> 
> u + v = (4, 3)
> -(u + v) = -(4, 3) = (-4, -3)
> 
> -u = (-3, 2), -v = (-1, -5)
> (-u) + (-v) = (-3, 2) + (-1, -5) = (-4, -3)
> 
> Verificación: -(u + v) = (-u) + (-v) ✓
> ```
> 
> **En polinomios:**
> ```
> 
> p(x) = x² + 2x, q(x) = -x + 3
> 
> p(x) + q(x) = x² + x + 3 -(p + q)(x) = -x² - x - 3
> 
> -p(x) = -x² - 2x -q(x) = x - 3 (-p + (-q))(x) = -x² - 2x + x - 3 = -x² - x - 3 ✓
> 
> ```
> 
> **Generalización:**
> ```
> 
> -(v₁ + v₂ + ... + vₙ) = (-v₁) + (-v₂) + ... + (-vₙ)
> 
> Se puede probar por inducción usando este teorema
> ```

## 🎯 Teorema 10: Opuesto de un Múltiplo Escalar

> [!important]- Negativo de Producto Escalar **Teorema:** Para todo c ∈ 𝔽 y v ∈ V:
> 
> ```
> -(c·v) = (-c)·v = c·(-v)
> 
> (Tres formas equivalentes de negar un producto escalar)
> ```
> 
> **Demostración de -(c·v) = (-c)·v:**
> 
> ```
> Necesitamos probar que (-c)·v es el opuesto de c·v
> Es decir: (c·v) + ((-c)·v) = 0
> 
> Paso 1: Factorizar usando distributividad (M3)
> (c·v) + ((-c)·v) = (c + (-c))·v
> 
> Paso 2: c + (-c) = 0 en 𝔽
> = 0·v
> 
> Paso 3: Por Teorema 3
> = 0
> 
> Por tanto: (c·v) + ((-c)·v) = 0
> 
> Por unicidad del opuesto:
> -(c·v) = (-c)·v
> 
> ∎
> ```
> 
> **Demostración de -(c·v) = c·(-v):**
> 
> ```
> Necesitamos probar que c·(-v) es el opuesto de c·v
> Es decir: (c·v) + c·(-v) = 0
> 
> Paso 1: Factorizar usando distributividad (M2)
> (c·v) + c·(-v) = c·(v + (-v))
> 
> Paso 2: v + (-v) = 0
> = c·0
> 
> Paso 3: Por Teorema 4
> = 0
> 
> Por tanto: (c·v) + c·(-v) = 0
> 
> Por unicidad del opuesto:
> -(c·v) = c·(-v)
> 
> ∎
> ```
> 
> **Demostración de (-c)·v = c·(-v):**
> 
> ```
> Por transitividad de las dos demostraciones anteriores:
> -(c·v) = (-c)·v  y  -(c·v) = c·(-v)
> 
> Por tanto: (-c)·v = c·(-v)
> 
> ∎
> ```

> [!example]- Ejemplos y Aplicaciones **Ejemplo 1:**
> 
> ```
> c = 3, v = (2, -1, 4)
> 
> c·v = 3·(2, -1, 4) = (6, -3, 12)
> 
> Tres formas de negar:
> 
> 1. -(c·v) = -(6, -3, 12) = (-6, 3, -12)
> 
> 2. (-c)·v = (-3)·(2, -1, 4) = (-6, 3, -12)
> 
> 3. c·(-v) = 3·(-2, 1, -4) = (-6, 3, -12)
> 
> Las tres dan el mismo resultado ✓
> ```
> 
> **Ejemplo 2: Simplificación algebraica**
> 
> ```
> -(5·u) = (-5)·u = 5·(-u)
> 
> Podemos "mover" el signo negativo libremente
> ```
> 
> **Aplicación en ecuaciones:**
> 
> ```
> Resolver: -3·v = (6, -9, 12)
> 
> Método 1: Multiplicar por -1/3
> v = (-1/3)·(6, -9, 12) = (-2, 3, -4)
> 
> Método 2: Reconocer -3·v = -(3·v)
> -(3·v) = (6, -9, 12)
> 3·v = -(6, -9, 12) = (-6, 9, -12)
> v = (1/3)·(-6, 9, -12) = (-2, 3, -4)
> 
> Mismo resultado
> ```
> 
> **Propiedad útil:**
> 
> ```
> (-1)·(-v) = (-1)·((-1)·v)    (por Teorema 5)
>           = ((-1)·(-1))·v    (M4)
>           = 1·v              (en 𝔽)
>           = v                (M5)
> 
> El opuesto del opuesto es el vector original
> ```

## 🎯 Teorema 11: Resta como Suma del Opuesto

> [!important]- Definición Formal de Resta **Teorema:** Para todo u, v ∈ V, la ecuación u + x = v tiene solución única.
> 
> **Definición de resta:**
> 
> ```
> u - v := u + (-v)
> 
> La resta se define como suma del opuesto
> ```
> 
> **Teorema (reformulado):**
> 
> ```
> u - v es la solución única de la ecuación:
> v + x = u
> ```
> 
> **Demostración de existencia:**
> 
> ```
> Sea x = u + (-v) = u - v
> 
> Verificar que es solución de v + x = u:
> 
> v + x = v + (u + (-v))
>       = v + ((-v) + u)      (conmutatividad)
>       = (v + (-v)) + u      (asociatividad)
>       = 0 + u               (definición opuesto)
>       = u                   (neutro)
> 
> Por tanto x = u - v es solución ✓
> ```
> 
> **Demostración de unicidad:**
> 
> ```
> Supongamos v + x = u y v + y = u
> 
> Entonces: v + x = v + y
> 
> Por cancelación (Teorema 7): x = y
> 
> La solución es única ✓
> ```

> [!example]- Propiedades de la Resta **Propiedad 1: Resta de sí mismo**
> 
> ```
> v - v = 0
> 
> Demostración:
> v - v = v + (-v) = 0
> ```
> 
> **Propiedad 2: Resta con cero**
> 
> ```
> v - 0 = v
> 
> Demostración:
> v - 0 = v + (-0) = v + 0 = v
> 
> 0 - v = -v
> 
> Demostración:
> 0 - v = 0 + (-v) = -v
> ```
> 
> **Propiedad 3: Distributividad escalar**
> 
> ```
> c·(u - v) = c·u - c·v
> 
> Demostración:
> c·(u - v) = c·(u + (-v))
>           = c·u + c·(-v)      (M2)
>           = c·u + (-(c·v))    (Teorema 10)
>           = c·u - c·v         (definición resta)
> ```
> 
> **Propiedad 4: Opuesto de resta**
> 
> ```
> -(u - v) = v - u
> 
> Demostración:
> -(u - v) = -(u + (-v))
>          = (-u) + (-(-v))     (Teorema 9)
>          = (-u) + v           (-(-v) = v)
>          = v + (-u)           (conmutatividad)
>          = v - u
> ```

## 🎯 Teorema 12: Propiedades de Combinaciones Lineales

> [!important]- Linealidad de Operaciones **Teorema:** Para escalares c₁, c₂, ..., cₙ y vectores v₁, v₂, ..., vₙ:
> 
> **Parte A: Distributividad extendida**
> 
> ```
> c·(v₁ + v₂ + ... + vₙ) = c·v₁ + c·v₂ + ... + c·vₙ
> 
> Un escalar se distribuye sobre una suma de n vectores
> ```
> 
> **Parte B: Asociatividad extendida**
> 
> ```
> (c₁ + c₂ + ... + cₙ)·v = c₁·v + c₂·v + ... + cₙ·v
> 
> Una suma de escalares se distribuye sobre un vector
> ```
> 
> **Demostración de Parte A (por inducción):**
> 
> ```
> Base (n = 2): Axioma M2 ✓
> 
> Hipótesis inductiva: Vale para n = k
> c·(v₁ + ... + vₖ) = c·v₁ + ... + c·vₖ
> 
> Paso inductivo: Probar para n = k+1
> 
> c·(v₁ + ... + vₖ + vₖ₊₁)
> = c·((v₁ + ... + vₖ) + vₖ₊₁)
> = c·(v₁ + ... + vₖ) + c·vₖ₊₁    (M2)
> = c·v₁ + ... + c·vₖ + c·vₖ₊₁    (H.I.)
> 
> ∎
> ```
> 
> **Demostración de Parte B:**
> 
> ```
> Similar usando M3 e inducción
> ```

> [!example]- Consecuencias Importantes **Combinación lineal general:**
> 
> ```
> c₁v₁ + c₂v₂ + ... + cₙvₙ
> 
> está bien definida y satisface:
> - Asociatividad completa
> - Conmutatividad completa
> - Distributividad en ambas direcciones
> ```
> 
> **Ejemplo en ℝ³:**
> 
> ```
> 2(v₁ + v₂ + v₃) = 2v₁ + 2v₂ + 2v₃
> 
> (2 + 3 - 5)·v = 2v + 3v - 5v = 0·v = 0
> ```
> 
> **Aplicación a independencia lineal:**
> 
> ```
> c₁v₁ + c₂v₂ + ... + cₙvₙ = 0
> 
> Esta ecuación tiene significado único debido
> a las propiedades demostradas
> ```

## 📊 Tabla Resumen de Teoremas

> [!note]- Referencia Rápida
> 
> |#|Teorema|Enunciado|Importancia|
> |---|---|---|---|
> |**1**|Unicidad del cero|0 es único|Notación coherente|
> |**2**|Unicidad del opuesto|-v es único|Define resta|
> |**3**|Cero escalar|0·v = 0|Anulación|
> |**4**|Vector cero|c·0 = 0|Anulación|
> |**5**|Multiplicación por -1|(-1)·v = -v|Conecta opuesto|
> |**6**|Producto nulo|c·v = 0 ⟹ c=0 o v=0|Cancelación|
> |**7**|Cancelación aditiva|u+w = v+w ⟹ u=v|Resolver ecuaciones|
> |**8**|Cancelación multiplicativa|c·u = c·v ⟹ u=v (c≠0)|División|
> |**9**|Opuesto de suma|-(u+v) = -u + -v|Distributividad|
> |**10**|Opuesto de producto|-(c·v) = (-c)·v = c·(-v)|Flexibilidad|
> |**11**|Resta|u - v = u + (-v)|Definición|
> |**12**|Linealidad|Distributividad extendida|Combinaciones|

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes **1. "Asumir propiedades sin demostrar"**
> 
> ```
> ✗ "Es obvio que 0·v = 0"
> 
> ✓ DEBE demostrarse desde axiomas
>   No es un axioma, es un teorema
> 
> En matemática rigurosa, nada es "obvio"
> ```
> 
> **2. "Confundir cero escalar y vector cero"**
> 
> ```
> 0 (escalar en 𝔽)  vs  0 (vector en V)
> 
> ✗ Tratarlos como el mismo objeto
> 
> ✓ Son diferentes, aunque se relacionan:
>   0·v = 0 (escalar 0 produce vector 0)
> ```
> 
> **3. "Aplicar cancelación con c = 0"**
> 
> ```
> ✗ De 0·u = 0·v concluir u = v
> 
> ✓ Solo se cancela c ≠ 0
>   0·u = 0·v SIEMPRE (ambos = 0)
> ```
> 
> **4. "Asumir que u + v = 0 implica u = v = 0"**
> 
> ```
> ✗ FALSO en general
> 
> ✓ Solo implica v = -u
> 
> Ejemplo: (1,2) + (-1,-2) = 0
> pero (1,2) ≠ 0 y (-1,-2) ≠ 0
> ```
> 
> **5. "Usar división en vez de multiplicación por inverso"**
> 
> ```
> ✗ v/c (no está definido en espacios vectoriales)
> 
> ✓ (1/c)·v  o  c⁻¹·v
> 
> La división no es operación primitiva
> ```
> 
> **6. "Olvidar verificar c ≠ 0"**
> 
> ```
> De c·v = w, concluir v = (1/c)·w
> 
> ✗ Sin verificar c ≠ 0
> 
> ✓ SOLO válido si c ≠ 0
>   Si c = 0: 0·v = w solo tiene solución si w = 0
> ```

## 🎯 Ejercicios Propuestos

> [!example]- Problemas de Práctica **Nivel básico - Verificación:**
> 
> 1. Verificar Teorema 3 (0·v = 0) explícitamente en: a) v = (2, -3) en ℝ² b) v = x² + 1 en P(ℝ) c) v = ⎡1 2⎤ en M₂ₓ₂(ℝ) ⎣3 4⎦
>     
> 2. Verificar Teorema 5 ((-1)·v = -v) en: a) v = (1, -2, 3) en ℝ³ b) v = 2x - 5 en P₁(ℝ)
>     
> 3. Verificar Teorema 9 en ℝ²: u = (3, -1), v = (2, 5) Verificar: -(u + v) = (-u) + (-v)
>     
> 
> **Nivel intermedio - Demostraciones:** 4. Demostrar usando solo axiomas: a) 0 + 0 = 0 b) -0 = 0 c) -(-v) = v para todo v
> 
> 4. Demostrar que si u + v = u, entonces v = 0
>     
> 5. Demostrar que (c - d)·v = c·v - d·v
>     
> 6. Demostrar que c·(u - v) = c·u - c·v
>     
> 7. Demostrar que si c·v = v para todo v, entonces c = 1
>     
> 
> **Nivel avanzado - Aplicaciones:** 9. Resolver en espacio vectorial general: a) v + (3·v) = w para v b) 2·v - 5·u = 3·v + u para v en términos de u
> 
> 8. Demostrar: Si {v₁, v₂, ..., vₙ} es l.i. y c₁v₁ + c₂v₂ + ... + cₙvₙ = d₁v₁ + d₂v₂ + ... + dₙvₙ entonces cᵢ = dᵢ para todo i
>     
> 9. Probar que en cualquier espacio vectorial: v - u = -(u - v)
>     
> 10. Demostrar por inducción: c·(v₁ + v₂ + ... + vₙ) = c·v₁ + c·v₂ + ... + c·vₙ
>     

## 💡 Importancia y Aplicaciones

> [!example]- Por Qué Son Importantes Estos Teoremas **Fundamento teórico:**
> 
> ```
> - Base rigurosa para álgebra lineal
> - Garantizan coherencia de definiciones
> - Permiten demostraciones formales
> - Evitan contradicciones lógicas
> ```
> 
> **Simplificación de cálculos:**
> 
> ```
> - Justifican técnicas algebraicas habituales
> - Permiten "cancelar" términos con certeza
> - Autorizan manipulaciones simbólicas
> - Establecen reglas de simplificación
> ```
> 
> **Resolución de ecuaciones:**
> 
> ```
> Ecuación: a·v + b·w = c·v + d·w
> 
> Pasos justificados por teoremas:
> a·v - c·v = d·w - b·w
> (a - c)·v = (d - b)·w
> 
> Cada paso usa algún teorema demostrado
> ```
> 
> **Independencia lineal:**
> 
> ```
> Definición: c₁v₁ + ... + cₙvₙ = 0 ⟹ todos cᵢ = 0
> 
> Usa:
> - Unicidad de representación (Teorema 12)
> - Propiedad del producto nulo (Teorema 6)
> - Cancelación (Teoremas 7, 8)
> ```
> 
> **Bases y coordenadas:**
> 
> ```
> v = c₁v₁ + ... + cₙvₙ (representación única)
> 
> Unicidad garantizada por teoremas fundamentales
> Sin ellos, coordenadas serían ambiguas
> ```

## 🔗 Relación entre Teoremas

> [!note]- Dependencias Lógicas
> 
> ```
> AXIOMAS (10)
>     ↓
> Teorema 1: Unicidad del 0
> Teorema 2: Unicidad de -v
>     ↓
> Teorema 3: 0·v = 0 ────────┐
> Teorema 4: c·0 = 0         │
>     ↓                      │
> Teorema 5: (-1)·v = -v ←───┘
>     ↓
> Teorema 6: c·v = 0 ⟹ c=0 o v=0
>     ↓
> Teorema 7: Cancelación aditiva
> Teorema 8: Cancelación multiplicativa
>     ↓
> Teorema 9: -(u+v) = -u + -v
> Teorema 10: -(c·v) = (-c)·v = c·(-v)
>     ↓
> Teorema 11: Resta bien definida
>     ↓
> Teorema 12: Linealidad general
>     ↓
> TEORÍA COMPLETA DE ESPACIOS VECTORIALES
> ```

## 📚 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales **Fundamentos previos:**
> 
> - [[02.2 Axiomas]] - Concepto de sistema axiomático
> - [[Lógica Matemática]] - Demostraciones formales
> - [[Teoría de Conjuntos]] - Unicidad de elementos
> - [[Campos]] - Propiedades de escalares 𝔽
> 
> **Temas relacionados:**
> 
> - [[Espacio Vectorial]] - Definición axiomática
> - [[Subespacios]] - Heredan propiedades
> - [[Transformaciones Lineales]] - Preservan estructura
> - [[Independencia Lineal]] - Usa estos teoremas
> 
> **Aplicaciones posteriores:**
> 
> - [[Bases y Dimensión]] - Representación única
> - [[Sistemas de Ecuaciones]] - Resolución formal
> - [[Determinantes]] - Propiedades algebraicas
> - [[Espacios Normados]] - Estructura adicional
> - [[Análisis Funcional]] - Extensión infinita

## 📖 Referencias Históricas

> [!note]- Fuentes Clásicas **Textos fundamentales:**
> 
> - **Peano, G. (1888).** "Calcolo Geometrico"
>     - Primera axiomatización de espacios vectoriales
>     - Teoremas básicos enunciados explícitamente
> - **Steinitz, E. (1910).** "Algebraische Theorie der Körper"
>     - Teoría abstracta de espacios vectoriales
>     - Demostraciones rigurosas de propiedades básicas
> - **Banach, S. (1932).** "Théorie des Opérations Linéaires"
>     - Espacios normados
>     - Propiedades fundamentales en dimensión infinita
> - **Bourbaki, N. (1939-).** "Éléments de Mathématique"
>     - Tratamiento sistemático y riguroso
>     - Énfasis en fundamentos axiomáticos

## 🎓 Resumen Ejecutivo

> [!important]- Puntos Clave para Recordar **Los 12 teoremas fundamentales:**
> 
> ```
> 1. Vector cero ÚNICO
> 2. Opuesto ÚNICO para cada vector
> 3. 0·v = 0 (cero escalar anula)
> 4. c·0 = 0 (cero vector anulado)
> 5. (-1)·v = -v (menos uno = opuesto)
> 6. c·v = 0 ⟹ c=0 o v=0 (ley del producto nulo)
> 7. Cancelación aditiva
> 8. Cancelación multiplicativa (c ≠ 0)
> 9. -(u+v) = -u + -v (distributividad opuesto)
> 10. -(c·v) = (-c)·v = c·(-v) (tres formas)
> 11. Resta bien definida: u - v = u + (-v)
> 12. Linealidad de combinaciones
> ```
> 
> **Método de demostración:**
> 
> ```
> 1. Partir de axiomas
> 2. Aplicar propiedades ya demostradas
> 3. Usar álgebra elemental (del campo 𝔽)
> 4. Invocar unicidad cuando corresponda
> 5. Concluir con rigor lógico
> ```
> 
> **Importancia práctica:**
> 
> ```
> - Justifican manipulaciones algebraicas
> - Garantizan coherencia de definiciones
> - Permiten resolver ecuaciones con certeza
> - Base para teoría de independencia lineal
> - Fundamentan concepto de coordenadas
> ```
> 
> **Principio general:**
> 
> ```
> En matemática rigurosa:
> - AXIOMAS: se asumen sin demostración
> - TEOREMAS: se derivan de axiomas
> - NADA es "obvio" sin demostración
> 
> Estos teoremas parecen "obvios" pero
> requieren demostración formal desde axiomas
> ```

## 🧩 Demostración Completa Modelo

> [!example]- Ejemplo Extenso: Teorema del Producto Nulo **Teorema 6 (Detallado):** Si c·v = 0, entonces c = 0 o v = 0
> 
> **Demostración formal completa:**
> 
> ```
> DADO: c ∈ 𝔽, v ∈ V tal que c·v = 0
> DEMOSTRAR: c = 0 o v = 0
> 
> ESTRATEGIA: Demostración por casos exhaustivos
> 
> CASO 1: Supongamos c = 0
>   Entonces la conclusión "c = 0 o v = 0" es verdadera.
>   (Porque c = 0 es verdadero)
>   Este caso está completo. □
> 
> CASO 2: Supongamos c ≠ 0
>   Debemos demostrar que v = 0
>   
>   Subcaso 2.1: Existencia de c⁻¹
>     Como c ≠ 0 y 𝔽 es campo, existe c⁻¹ ∈ 𝔽
>     tal que c⁻¹·c = 1 (unidad de 𝔽)
>   
>   Subcaso 2.2: Manipulación de c·v = 0
>     Partimos de: c·v = 0             ... (hipótesis)
>     
>     Multiplicar por c⁻¹ (izquierda):
>     c⁻¹·(c·v) = c⁻¹·0                ... (1)
>     
>     Lado izquierdo, aplicar (M4) [asociatividad mixta]:
>     (c⁻¹·c)·v = c⁻¹·0
>     
>     Como c⁻¹·c = 1:
>     1·v = c⁻¹·0                      ... (2)
>     
>     Aplicar (M5) [1 es neutro] al lado izquierdo:
>     v = c⁻¹·0                        ... (3)
>     
>     Lado derecho, aplicar Teorema 4 [c·0 = 0]:
>     v = 0                            ... (4)
>   
>   Por tanto, si c ≠ 0, entonces v = 0
>   Luego "c = 0 o v = 0" es verdadero □
> 
> CONCLUSIÓN:
>   En ambos casos (c = 0 o c ≠ 0), se cumple c = 0 o v = 0
>   Como estos casos son exhaustivos y mutuamente excluyentes,
>   hemos demostrado el teorema para todo c y v.
> 
> ∎ Q.E.D. (Quod Erat Demonstrandum)
> ```
> 
> **Análisis de la demostración:**
> 
> ```
> Axiomas usados:
> - (M4) Asociatividad mixta: c·(d·v) = (cd)·v
> - (M5) Neutro multiplicativo: 1·v = v
> 
> Teoremas previos usados:
> - Teorema 4: c·0 = 0
> 
> Propiedades del campo 𝔽:
> - Existencia de inverso multiplicativo si c ≠ 0
> - Identidad c⁻¹·c = 1
> 
> Lógica:
> - Demostración por casos
> - Casos exhaustivos (c = 0 o c ≠ 0)
> ```

---

**Tags:** #espacio-vectorial #teoremas-fundamentales #axiomas #demostraciones #álgebra-lineal #rigor-matemático #unicidad #cancelación #producto-nulo #opuestos #vector-cero #fundamentos
