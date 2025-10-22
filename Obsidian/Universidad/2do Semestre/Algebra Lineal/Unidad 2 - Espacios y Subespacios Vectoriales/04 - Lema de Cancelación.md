# 🔄 Lema de Cancelación

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva **El Lema de Cancelación es una propiedad fundamental en estructuras algebraicas que permite "cancelar" o "eliminar" términos comunes en ambos lados de una ecuación bajo ciertas condiciones. En álgebra lineal, se manifiesta principalmente en espacios vectoriales y transformaciones lineales, estableciendo cuándo podemos simplificar expresiones vectoriales de manera similar a como cancelamos en aritmética.**
> 
> **Características clave:**
> 
> - **Cancelación aditiva:** Si u + v = u + w, entonces v = w
> - **Cancelación multiplicativa:** Más restrictiva, requiere invertibilidad
> - **Dependencia del contexto:** Válida en grupos, espacios vectoriales
> - **Fundamental para resolución:** Base de muchos métodos algebraicos
> - **No siempre válida:** Fallos en estructuras sin inversos
> - **Conexión con unicidad:** Garantiza soluciones únicas

### 📖 Contexto Histórico

> [!note]- Desarrollo Histórico **Antigüedad - Aritmética elemental (300 a.C.):**
> 
> - **Euclides (300 a.C.):** _Elementos_
>     - Axiomas de igualdad (Axioma de Euclides)
>     - "Si iguales se restan de iguales, los residuos son iguales"
>     - Primera formalización implícita de cancelación
>     - Aplicado a magnitudes geométricas
> 
> **Álgebra medieval (800-1600):**
> 
> - **Al-Khwarizmi (820):** _Al-jabr_
>     - Operaciones de "al-jabr" (completar) y "al-muqabala" (balancear)
>     - Cancelación de términos en ecuaciones
>     - "Lo que se hace a un lado debe hacerse al otro"
> - **Fibonacci (1202):** _Liber Abaci_
>     - Reglas de cancelación en aritmética
> 
> **Álgebra simbólica (1500-1700):**
> 
> - **Viète (1591):** _In Artem Analyticam Isagoge_
>     - Álgebra simbólica con letras
>     - Operaciones de transposición
>     - Cancelación formal
> - **Descartes (1637):** _La Géométrie_
>     - Manipulación algebraica sistemática
>     - Resolución de ecuaciones
> 
> **Álgebra abstracta (1800-1900):**
> 
> - **Gauss (1801):** _Disquisitiones Arithmeticae_
>     - Congruencias y cancelación modular
>     - Cuando la cancelación falla (con divisores de cero)
> - **Cauchy (1815):**
>     - Grupos de permutaciones
>     - Propiedad de cancelación en grupos
> - **Cayley (1854):**
>     - Teoría de grupos abstracta
>     - Axiomatización de propiedades
> - **Dedekind (1871):**
>     - Ideales y cancelación en anillos
>     - Dominios de integridad
> - **Frobenius (1878):**
>     - Álgebra de matrices
>     - Cancelación y matrices invertibles
> 
> **Álgebra lineal moderna (1900-presente):**
> 
> - **Peano (1888):** Axiomas de espacios vectoriales
>     - Cancelación como consecuencia de axiomas
> - **Steinitz (1910):** Teoría de extensiones
>     - Dominios de cancelación
> - **Emmy Noether (1921):**
>     - Teoría de anillos
>     - Clasificación de estructuras con/sin cancelación
> - **van der Waerden (1930):** _Moderne Algebra_
>     - Tratamiento sistemático
>     - Dominios de integridad y cancelación
> - **Bourbaki (1942+):**
>     - Estructuras algebraicas axiomáticas
>     - Cancelación en contexto general

## 📐 Lema de Cancelación Aditiva

> [!important]- En Grupos y Espacios Vectoriales **Enunciado formal:**
> 
> ```
> Sea (V, +) un espacio vectorial (o grupo abeliano).
> 
> Para cualesquiera vectores u, v, w ∈ V:
> 
> Si u + v = u + w, entonces v = w
> 
> Demostración:
> 1. Supongamos u + v = u + w
> 2. Existe -u (inverso aditivo de u)
> 3. Sumar -u a ambos lados:
>    (-u) + (u + v) = (-u) + (u + w)
> 4. Por asociatividad:
>    [(-u) + u] + v = [(-u) + u] + w
> 5. Por definición de inverso:
>    0 + v = 0 + w
> 6. Por identidad:
>    v = w ∎
> 
> Clave: Existencia del inverso aditivo (elemento neutro)
> ```
> 
> **Cancelación por la izquierda:**
> 
> ```
> Si v + u = w + u, entonces v = w
> 
> Demostración similar:
> 1. v + u = w + u
> 2. (v + u) + (-u) = (w + u) + (-u)
> 3. v + [u + (-u)] = w + [u + (-u)]
> 4. v + 0 = w + 0
> 5. v = w ∎
> 
> Nota: En grupos abelianos (conmutativos),
> cancelación derecha = cancelación izquierda
> ```
> 
> **Consecuencias importantes:**
> 
> ```
> 6. Unicidad del elemento neutro:
>    Si 0 y 0' son neutros, entonces 0 = 0'
>    
>    Demostración:
>    0 = 0 + 0' (0' es neutro)
>    0 + 0' = 0' (0 es neutro)
>    Por transitividad: 0 = 0' ✓
> 
> 7. Unicidad del inverso:
>    Si v + u = 0 y v + u' = 0, entonces u = u'
>    
>    Demostración:
>    v + u = v + u' (ambos = 0)
>    Por cancelación: u = u' ✓
> 
> 8. Solución única de ecuaciones:
>    La ecuación u + x = v tiene solución única
>    x = v - u = v + (-u)
>    
>    Demostración de unicidad:
>    Si u + x₁ = v y u + x₂ = v
>    entonces u + x₁ = u + x₂
>    Por cancelación: x₁ = x₂ ✓
> 
> 9. Inyectividad de traslaciones:
>    La función τᵤ(v) = u + v es inyectiva
>    
>    Si τᵤ(v₁) = τᵤ(v₂), entonces:
>    u + v₁ = u + v₂
>    Por cancelación: v₁ = v₂ ✓
> ```
> 
> **Aplicaciones en espacios vectoriales:**
> 
> ```
> Ejemplo 1: Resolver u + x = v en ℝ³
> u = (1, 2, 3), v = (4, 5, 6)
> 
> Solución:
> x = v - u = (4-1, 5-2, 6-3) = (3, 3, 3)
> 
> Verificación:
> u + x = (1,2,3) + (3,3,3) = (4,5,6) = v ✓
> 
> Unicidad garantizada por cancelación
> 
> Ejemplo 2: Simplificar (2u + v) - (2u + w)
> = 2u + v - 2u - w
> = (2u - 2u) + (v - w)
> = 0 + (v - w)
> = v - w
> 
> Cancelación implícita de 2u
> 
> Ejemplo 3: Si A + X = B (matrices)
> entonces X = B - A (única solución)
> Por cancelación matricial
> ```

## 🎯 Lema de Cancelación Multiplicativa

> [!success]- En Anillos y Cuerpos **Cancelación en cuerpos:**
> 
> ```
> Sea 𝔽 un cuerpo (ℝ, ℂ, ℚ, etc.)
> 
> Para a, b, c ∈ 𝔽 con a ≠ 0:
> 
> Si a·b = a·c, entonces b = c
> 
> Demostración:
> 1. a·b = a·c
> 2. Como a ≠ 0, existe a⁻¹ (inverso multiplicativo)
> 3. Multiplicar ambos lados por a⁻¹:
>    a⁻¹·(a·b) = a⁻¹·(a·c)
> 4. Por asociatividad:
>    (a⁻¹·a)·b = (a⁻¹·a)·c
> 5. Por definición de inverso:
>    1·b = 1·c
> 6. Por identidad:
>    b = c ∎
> 
> Condición esencial: a ≠ 0
> Sin esta condición, la cancelación FALLA
> ```
> 
> **Divisores de cero (cuando falla):**
> 
> ```
> En algunos anillos existen divisores de cero:
> elementos no nulos a, b tales que a·b = 0
> 
> Ejemplo en ℤ₆ (enteros módulo 6):
> 2·3 ≡ 0 (mod 6)
> 
> Contraejemplo de cancelación:
> 2·3 = 2·0 (ambos ≡ 0 mod 6)
> pero 3 ≠ 0
> 
> ¡Cancelación falla!
> 2 es divisor de cero en ℤ₆
> 
> En general:
> Si a es divisor de cero, NO podemos cancelar a
> 
> Ejemplo matricial:
> A = [1 0]    B = [1]    C = [2]
>     [0 0]        [0]        [0]
> 
> A·B = [1] = A·C
>       [0]
> 
> pero B ≠ C
> 
> A es singular (det(A) = 0) → no cancelable
> ```
> 
> **Dominios de integridad:**
> 
> ```
> Definición:
> Un dominio de integridad es un anillo conmutativo
> sin divisores de cero (excepto 0)
> 
> Propiedad de cancelación:
> En dominios de integridad, la cancelación
> multiplicativa es VÁLIDA para elementos no nulos
> 
> Si a·b = a·c y a ≠ 0, entonces b = c
> 
> Ejemplos de dominios de integridad:
> • ℤ (enteros)
> • ℚ, ℝ, ℂ (cuerpos)
> • ℤ[x] (polinomios con coeficientes enteros)
> • Anillo de polinomios sobre un cuerpo
> 
> Contraejemplos (NO son dominios):
> • ℤₙ con n compuesto (ej: ℤ₆, ℤ₈, ℤ₁₀)
> • Matrices n×n (tienen divisores de cero)
> • ℤ₄ (2·2 = 0)
> ```
> 
> **Cancelación en matrices:**
> 
> ```
> Para matrices A, B, C:
> 
> Si AB = AC, entonces B = C
> ⟺ A es invertible (det(A) ≠ 0)
> 
> Demostración (⟹):
> AB = AC
> A⁻¹(AB) = A⁻¹(AC)
> (A⁻¹A)B = (A⁻¹A)C
> IB = IC
> B = C ✓
> 
> Si A no es invertible:
> ¡NO podemos cancelar!
> 
> Contraejemplo:
> A = [1 0]    B = [1 0]    C = [0 0]
>     [0 0]        [0 1]        [0 0]
> 
> AB = [1 0] = AC
>      [0 0]
> 
> pero B ≠ C
> 
> Regla práctica:
> Solo cancela matrices invertibles
> ```

## 🔷 Lema de Cancelación Escalar

> [!note]- En Espacios Vectoriales **Cancelación de escalares:**
> 
> ```
> Sea V un espacio vectorial sobre 𝔽
> Sea α ∈ 𝔽 (escalar) y v, w ∈ V (vectores)
> 
> Si α·v = α·w y α ≠ 0, entonces v = w
> 
> Demostración:
> 1. α·v = α·w
> 2. Como α ≠ 0 en 𝔽, existe α⁻¹
> 3. Multiplicar por α⁻¹:
>    α⁻¹·(α·v) = α⁻¹·(α·w)
> 4. Por asociatividad escalar-vector:
>    (α⁻¹·α)·v = (α⁻¹·α)·w
> 5. Como α⁻¹·α = 1:
>    1·v = 1·w
> 6. Por identidad escalar:
>    v = w ∎
> 
> Condición necesaria: α ≠ 0
> ```
> 
> **Caso especial: α = 0:**
> 
> ```
> ¡Cuidado! Si α = 0:
> 
> 0·v = 0·w = 0 (el vector cero)
> 
> para CUALQUIER v, w ∈ V
> 
> No podemos concluir v = w
> 
> Ejemplo:
> 0·(1,2,3) = (0,0,0)
> 0·(4,5,6) = (0,0,0)
> 
> 0·(1,2,3) = 0·(4,5,6)
> pero (1,2,3) ≠ (4,5,6)
> 
> Moraleja: NUNCA cancelar escalar cero
> ```
> 
> **Aplicaciones:**
> 
> ```
> Ejemplo 1: Resolver 3x = 3b en ℝ³
> x, b ∈ ℝ³
> 
> Como 3 ≠ 0:
> x = (1/3)·3b = b
> 
> Solución única por cancelación
> 
> Ejemplo 2: Si 5u = 5v en cualquier espacio vectorial
> y 5 ≠ 0, entonces u = v
> 
> Ejemplo 3: Simplificar 2(u + v) - 2(u + w)
> = 2u + 2v - 2u - 2w
> = 2(u - u) + 2(v - w)
> = 2·0 + 2(v - w)
> = 2(v - w)
> 
> O directamente:
> 2(u + v) - 2(u + w) = 2[(u+v) - (u+w)]
> = 2[v - w]
> 
> Cancelación de u permitida por linealidad
> ```
> 
> **Combinaciones lineales:**
> 
> ```
> Si α₁v₁ + α₂v₂ = α₁w₁ + α₂w₂
> 
> NO podemos concluir directamente v₁ = w₁ y v₂ = w₂
> 
> Solo si vectores son linealmente independientes
> y coeficientes se pueden igualar término a término
> 
> Contraejemplo:
> 2(1,0) + 3(0,1) = (2,3)
> 1(2,0) + 3(0,1) = (2,3)
> 
> Misma combinación lineal,
> pero coeficientes diferentes
> 
> La cancelación requiere contexto adicional
> ```

## 📊 Tabla Comparativa

> [!tip]- Cuándo Aplica el Lema
> 
> ```
> LEMA DE CANCELACIÓN - VALIDEZ POR ESTRUCTURA
> 
> Estructura        | Aditiva | Multiplicativa | Condiciones
> ------------------|---------|----------------|-------------
> Grupo             | ✓       | —              | Siempre
> Grupo abeliano    | ✓       | —              | Siempre
> Espacio vectorial | ✓       | —              | Siempre
> Anillo            | ✓       | ✗              | Solo si sin div. cero
> Dominio integral  | ✓       | ✓              | a ≠ 0
> Cuerpo            | ✓       | ✓              | a ≠ 0
> ℤₙ (n primo)      | ✓       | ✓              | a ≠ 0
> ℤₙ (n compuesto)  | ✓       | ✗              | Divisores de cero
> Matrices n×n      | ✓       | ✗              | Solo si invertible
> Polinomios        | ✓       | ✓              | Sobre dominio
> Funciones         | ✓       | ✗              | Depende del contexto
> 
> Leyenda:
> ✓ = Válida siempre (bajo condiciones mínimas)
> ✗ = No válida en general
> — = No aplicable (no hay operación definida)
> ```

## 🧮 Problemas Resueltos

> [!example]- Ejemplos Detallados **Problema 1: Cancelación vectorial básica**
> 
> ```
> En ℝ³, resolver:
> (2, -1, 3) + x = (5, 2, -1) + x + (1, 1, 1)
> 
> SOLUCIÓN:
> 
> Lado derecho:
> (5, 2, -1) + x + (1, 1, 1) = (6, 3, 0) + x
> 
> Ecuación:
> (2, -1, 3) + x = (6, 3, 0) + x
> 
> Por cancelación de x:
> (2, -1, 3) = (6, 3, 0)
> 
> ¡Contradicción!
> 
> No hay solución (ecuación inconsistente)
> 
> Conclusión: El lema de cancelación revela
> que la ecuación es imposible
> ```
> 
> **Problema 2: Cancelación escalar**
> 
> ```
> Si 7v = 7w en un espacio vectorial V,
> demostrar que v = w
> 
> SOLUCIÓN:
> 
> Dado: 7v = 7w
> 
> Paso 1: Verificar que 7 ≠ 0 ✓
> 
> Paso 2: Multiplicar por 1/7:
> (1/7)·7v = (1/7)·7w
> 
> Paso 3: Por asociatividad:
> ((1/7)·7)v = ((1/7)·7)w
> 
> Paso 4: Simplificar:
> 1·v = 1·w
> 
> Paso 5: Por identidad:
> v = w ✓
> 
> Nota: Usamos que 7 tiene inverso (1/7)
> en el campo de escalares
> ```
> 
> **Problema 3: Cancelación que falla**
> 
> ```
> En ℤ₆, considerar:
> 2·3 ≡ 2·0 (mod 6)
> 
> ¿Podemos concluir 3 ≡ 0 (mod 6)?
> 
> SOLUCIÓN:
> 
> Verificación:
> 2·3 = 6 ≡ 0 (mod 6) ✓
> 2·0 = 0 ≡ 0 (mod 6) ✓
> 
> Entonces: 2·3 ≡ 2·0 (mod 6)
> 
> Intento de cancelar 2:
> ¿3 ≡ 0 (mod 6)?
> 
> NO, porque 3 ≢ 0 (mod 6)
> 
> Razón del fallo:
> 2 es divisor de cero en ℤ₆
> porque 2·3 ≡ 0 (mod 6)
> 
> Lección: En ℤₙ con n compuesto,
> NO podemos cancelar divisores de cero
> 
> Divisores de cero en ℤ₆: {2, 3, 4}
> ```
> 
> **Problema 4: Matrices no invertibles**
> 
> ```
> Sean:
> A = [1 0]    B = [1 2]    C = [3 4]
>     [0 0]        [0 0]        [0 0]
> 
> Verificar que AB = AC pero B ≠ C
> 
> SOLUCIÓN:
> 
> Calcular AB:
> AB = [1 0][1 2] = [1 2]
>      [0 0][0 0]   [0 0]
> 
> Calcular AC:
> AC = [1 0][3 4] = [3 4]
>      [0 0][0 0]   [0 0]
> 
> ¡Error en mi cálculo! Verifiquemos:
> 
> AB = [1·1+0·0  1·2+0·0] = [1 2]
>      [0·1+0·0  0·2+0·0]   [0 0]
> 
> AC = [1·3+0·0  1·4+0·0] = [3 4]
>      [0·3+0·0  0·4+0·0]   [0 0]
> 
> AB ≠ AC en este caso
> 
> Mejor ejemplo:
> A = [1 0]    B = [1]    C = [2]
>     [0 0]        [1]        [0]
> 
> AB = [1 0][1] = [1]
>      [0 0][1]   [0]
> 
> AC = [1 0][2] = [2]
>      [0 0][0]   [0]
> 
> Tampoco funciona. Corrección:
> 
> A = [1 1]    B = [1]    C = [0]
>     [1 1]        [0]        [1]
> 
> AB = [1 1][1] = [1]
>      [1 1][0]   [1]
> 
> AC = [1 1][0] = [1]
>      [1 1][1]   [1]
> 
> AB = AC pero B ≠ C ✓
> 
> Razón: A no es invertible (det(A) = 0)
> Las filas son proporcionales
> 
> Conclusión: NO cancelar matrices singulares
> ```
> 
> **Problema 5: Ecuación lineal**
> 
> ```
> Resolver la ecuación vectorial en ℝ²:
> 3x + (2, 1) = 3y + (5, 4)
> 
> SOLUCIÓN:
> 
> Reescribir:
> 3x - 3y = (5, 4) - (2, 1)
> 3(x - y) = (3, 3)
> 
> Por cancelación escalar (3 ≠ 0):
> x - y = (1/3)(3, 3) = (1, 1)
> 
> Por tanto:
> x = y + (1, 1)
> 
> Solución general:
> Para cualquier y ∈ ℝ²:
> x = y + (1, 1)
> 
> Ejemplo: Si y = (0, 0), entonces x = (1, 1)
> Verificar:
> 3(1,1) + (2,1) = (3,3) + (2,1) = (5,4)
> 3(0,0) + (5,4) = (0,0) + (5,4) = (5,4) ✓
> ```
> 
> **Problema 6: Independencia lineal**
> 
> ```
> Si αu + βv = αw + βv para u, v, w vectores
> y α ≠ 0, demostrar que u = w
> 
> SOLUCIÓN:
> 
> Dado: αu + βv = αw + βv
> 
> Paso 1: Restar βv de ambos lados:
> αu + βv - βv = αw + βv - βv
> αu + (βv - βv) = αw + (βv - βv)
> 
> Paso 2: Simplificar:
> αu + 0 = αw + 0
> αu = αw
> 
> Paso 3: Como α ≠ 0, cancelar:
> u = w ✓
> 
> Nota: La cancelación de βv fue por
> lema aditivo, la de α por lema escalar
> ```
> 
> **Problema 7: Sistema de ecuaciones**
> 
> ```
> Resolver el sistema usando cancelación:
> x + 2y = 5
> x + 2y = 8
> 
> SOLUCIÓN:
> 
> De las dos ecuaciones:
> x + 2y = 5
> x + 2y = 8
> 
> Por transitividad:
> 5 = 8
> 
> ¡Contradicción!
> 
> Conclusión: Sistema inconsistente
> No tiene solución
> 
> El lema de cancelación ayuda a detectar
> inconsistencias rápidamente
> 
> Si las ecuaciones fueran:
> x + 2y = 5
> x + 2y = 5
> 
> Son idénticas (infinitas soluciones)
> x = 5 - 2y para cualquier y ∈ ℝ
> ```
> 
> **Problema 8: Polinomios**
> 
> ```
> En ℝ[x], si (x-1)p(x) = (x-1)q(x),
> ¿podemos concluir p(x) = q(x)?
> 
> SOLUCIÓN:
> 
> Depende del contexto:
> 
> Como polinomios (igualdad formal):
> SÍ, si x-1 no es el polinomio cero
> 
> ℝ[x] es dominio de integridad
> (x-1) ≠ 0 (como polinomio)
> → Podemos cancelar
> → p(x) = q(x)
> 
> Como funciones (igualdad puntual):
> NO necesariamente en todo punto
> 
> Si evaluamos en x = 1:
> (1-1)p(1) = 0 = (1-1)q(1)
> 0 = 0 (¡siempre cierto!)
> 
> No podemos concluir nada sobre p(1) vs q(1)
> 
> Ejemplo:
> p(x) = x + 1, q(x) = x + 2
> 
> (x-1)(x+1) = x² - 1
> (x-1)(x+2) = x² + x - 2
> 
> Estos NO son iguales como polinomios
> 
> Pero si (x-1)p(x) = (x-1)q(x) formalmente,
> entonces p(x) = q(x) formalmente ✓
> ```

## 🔍 Generalizaciones

> [!important]- Extensiones del Concepto **Cancelación en módulos:**
> 
> ```
> Un módulo M sobre un anillo R generaliza
> espacios vectoriales
> 
> Cancelación aditiva: SIEMPRE válida
> (M es grupo abeliano bajo +)
> 
> Cancelación escalar: Depende de R
> • Si R es dominio de integridad: válida para r ≠ 0
> • Si R tiene divisores de cero: NO siempre válida
> 
> Ejemplo: ℤ-módulo (grupo abeliano)
> 2·m = 2·n en ℤ-módulo
> → m = n (2 ≠ 0 en ℤ)
> 
> Pero en ℤ₆-módulo:
> 2·m = 2·n no implica m = n
> (2 es divisor de cero en ℤ₆)
> ```
> 
> **Cancelación en categorías:**
> 
> ```
> Monomorfismos (generalizan inyectividad):
> f: A → B es monomorfismo si:
> f ∘ g = f ∘ h ⟹ g = h
> 
> "Cancelable por la izquierda"
> 
> Epimorfismos (generalizan sobreyectividad):
> f: A → B es epimorfismo si:
> g ∘ f = h ∘ f ⟹ g = h
> 
> "Cancelable por la derecha"
> 
> En Set (categoría de conjuntos):
> • Mono = inyectiva
> • Epi = sobreyectiva
> 
> En otras categorías puede diferir
> ```
> 
> **Cancelación débil:**
> 
> ```
> En algunos contextos, cancelación parcial:
> 
> Si au = av y a es regular (no divisor de cero):
> entonces u = v
> 
> Elemento regular: a es regular si ax = 0 implica x = 0
> 
> En anillos sin divisores de cero: Todos los elementos no nulos son regulares → Cancelación válida
> 
> En anillos generales: Solo elementos regulares son cancelables
> 
> ```
> 
> **Cancelación en grupos no abelianos:**
> ```
> 
> En grupos no conmutativos:
> 
> Cancelación izquierda: a·b = a·c ⟹ b = c
> 
> Cancelación derecha: b·a = c·a ⟹ b = c
> 
> Ambas VÁLIDAS pero DISTINTAS (no son equivalentes por falta de conmutatividad)
> 
> Ejemplo: Grupo de matrices invertibles GL(n, ℝ) Si AB = AC y A invertible: B = C Si BA = CA y A invertible: B = C Pero AB = AC no implica BA = CA en general
> ```

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes **1. "Siempre se puede cancelar"**
> 
> ```
> ✗ FALSO
> 
> Cancelación requiere condiciones:
> • Aditiva: Válida en grupos
> • Multiplicativa: Solo sin divisores de cero
> • Escalar: Solo si escalar ≠ 0
> 
> Contraejemplo (multiplicativo):
> En ℤ₆: 2·3 = 2·0 pero 3 ≠ 0
> ```
> 
> **2. "Cancelar antes de verificar invertibilidad"**
> 
> ```
> ✗ ERROR COMÚN
> 
> En matrices:
> AB = AC NO implica B = C
> (si A no es invertible)
> 
> Procedimiento correcto:
> 1. Verificar det(A) ≠ 0
> 2. Si es invertible, entonces cancelar
> 3. Si no, buscar otro método
> ```
> 
> **3. "Cancelar el cero"**
> 
> ```
> ✗ FALSO
> 
> 0·u = 0·v NO implica u = v
> 
> Razón: 0 no tiene inverso multiplicativo
> No cumple condición para cancelación
> 
> Ejemplo:
> 0·(1,2) = (0,0)
> 0·(3,4) = (0,0)
> pero (1,2) ≠ (3,4)
> ```
> 
> **4. "Cancelación término a término sin justificación"**
> 
> ```
> ✗ FALSO en general
> 
> Si a₁v₁ + a₂v₂ = b₁w₁ + b₂w₂
> 
> NO podemos concluir:
> a₁v₁ = b₁w₁ y a₂v₂ = b₂w₂
> 
> Solo si hay independencia lineal y estructura adecuada
> 
> Contraejemplo:
> 2·(1,0) + 1·(0,1) = (2,1)
> 1·(1,0) + 1·(1,1) = (2,1)
> 
> Mismos vectores resultantes,
> coeficientes diferentes
> ```
> 
> **5. "Cancelar en ecuaciones no lineales"**
> 
> ```
> ✗ PELIGROSO
> 
> En u² = v² no podemos cancelar u
> 
> Razón: u² = v² implica u = ±v
> (no solo u = v)
> 
> Ejemplo: (-2)² = 2² pero -2 ≠ 2
> 
> Cancelación es para operaciones lineales
> ```
> 
> **6. "Ignorar el contexto algebraico"**
> 
> ```
> ✗ ERROR FUNDAMENTAL
> 
> La validez de cancelación depende de:
> • Estructura algebraica (grupo, anillo, cuerpo)
> • Propiedades del elemento (invertible, regular)
> • Tipo de operación (suma, producto)
> 
> No es una regla universal sin contexto
> ```
> 
> **7. "Confundir cancelación con simplificación"**
> 
> ```
> ✗ CONCEPTOS DISTINTOS
> 
> Cancelación: Eliminar términos de ecuación
> (a + b = a + c ⟹ b = c)
> 
> Simplificación: Reducir expresión
> (2x + 3x = 5x)
> 
> Relacionados pero no idénticos
> ```

## 🎯 Aplicaciones Prácticas

> [!note]- Usos en Álgebra Lineal **Resolución de sistemas lineales:**
> 
> ```
> Sistema: Ax = b
> 
> Si A es invertible:
> Ax = b
> A⁻¹(Ax) = A⁻¹b  (multiplicar por A⁻¹)
> (A⁻¹A)x = A⁻¹b  (asociatividad)
> Ix = A⁻¹b        (cancelación efectiva de A)
> x = A⁻¹b         (solución única)
> 
> La cancelación de A (por invertibilidad)
> garantiza unicidad de solución
> ```
> 
> **Espacios de soluciones:**
> 
> ```
> Si Av₁ = 0 y Av₂ = 0
> entonces A(v₁ + v₂) = Av₁ + Av₂ = 0 + 0 = 0
> 
> El conjunto de soluciones forma subespacio
> (cerrado bajo suma por cancelación aditiva)
> 
> ker(A) = {v : Av = 0}
> es subespacio por propiedades de cancelación
> ```
> 
> **Independencia lineal:**
> 
> ```
> Vectores v₁, ..., vₙ son linealmente independientes
> si:
> c₁v₁ + ... + cₙvₙ = 0 ⟹ c₁ = ... = cₙ = 0
> 
> Uso de cancelación:
> Si c₁v₁ + ... + cₙvₙ = d₁v₁ + ... + dₙvₙ
> entonces (c₁-d₁)v₁ + ... + (cₙ-dₙ)vₙ = 0
> 
> Por independencia: cᵢ - dᵢ = 0 para todo i
> Por tanto: cᵢ = dᵢ para todo i
> 
> Unicidad de representación
> ```
> 
> **Transformaciones lineales:**
> 
> ```
> Si T: V → W es lineal e inyectiva:
> 
> T(u) = T(v) ⟹ u = v
> 
> Equivalentemente:
> T(u - v) = T(u) - T(v) = 0
> ⟹ u - v ∈ ker(T) = {0}
> ⟹ u - v = 0
> ⟹ u = v
> 
> La inyectividad ES una forma de cancelación
> ```
> 
> **Cambio de base:**
> 
> ```
> Si [v]ᵦ = coordenadas de v en base B
> y P es matriz de cambio de base
> 
> [v]ᵦ' = P[v]ᵦ
> 
> Como P es invertible:
> P⁻¹[v]ᵦ' = P⁻¹P[v]ᵦ
> P⁻¹[v]ᵦ' = [v]ᵦ
> 
> Cancelación de P garantiza reversibilidad
> ```

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales **Fundamentos previos:**
> 
> - [[Axiomas de espacios vectoriales]] - Propiedades básicas
> - [[Grupos y estructuras algebraicas]] - Contexto general
> - [[Operaciones binarias]] - Suma y producto
> - [[Elemento neutro e inverso]] - Requisitos para cancelación
> 
> **Temas relacionados:**
> 
> - [[Matrices invertibles]] - Cancelación matricial
> - [[Determinantes]] - Condición de invertibilidad
> - [[Núcleo de transformación]] - Inyectividad
> - [[Divisores de cero]] - Cuando falla cancelación
> 
> **Aplicaciones posteriores:**
> 
> - [[Sistemas de ecuaciones lineales]] - Resolución
> - [[Independencia lineal]] - Unicidad de coeficientes
> - [[Isomorfismos]] - Biyecciones cancelables
> - [[Teorema de rango-nulidad]] - Dimensiones
> - [[Formas canónicas]] - Simplificación de matrices

## 📋 Tabla de Resumen

> [!important]- Guía Rápida
> 
> ```
> LEMA DE CANCELACIÓN - GUÍA DE USO
> 
> CANCELACIÓN ADITIVA (u + v = u + w ⟹ v = w)
> ✓ Válida en: Grupos, espacios vectoriales, anillos
> ✓ Siempre aplicable (sin condiciones adicionales)
> ✓ Base: Existencia de inverso aditivo
> 
> CANCELACIÓN MULTIPLICATIVA (a·b = a·c ⟹ b = c)
> ✓ Válida si: a es invertible o a no es divisor de cero
> ✗ NO válida si: a es divisor de cero
> ✓ Estructuras seguras: Cuerpos, dominios de integridad
> ⚠ Peligrosas: ℤₙ compuesto, matrices singulares
> 
> CANCELACIÓN ESCALAR (α·v = α·w ⟹ v = w)
> ✓ Válida si: α ≠ 0
> ✗ NUNCA válida si α = 0
> ✓ Base: Existencia de α⁻¹ en el campo
> 
> PROCEDIMIENTO:
> 1. Identificar estructura algebraica
> 2. Verificar condiciones (invertibilidad, α ≠ 0)
> 3. Aplicar cancelación apropiada
> 4. Si falla, buscar método alternativo
> 
> SEÑALES DE PELIGRO:
> • Matrices singulares (det = 0)
> • Escalares cero
> • Anillos con divisores de cero
> • Operaciones no lineales
> ```

## 💡 Intuición Geométrica

> [!tip]- Interpretación Visual **Traslaciones (cancelación aditiva):**
> 
> ```
> En ℝ²:
> Si u + v = u + w
> 
> Geométricamente:
> "Trasladar por u" es operación reversible
> 
>     v ----+u----> u+v
>     
>     w ----+u----> u+w
> 
> Si u+v = u+w (misma posición final)
> entonces v = w (mismo punto inicial)
> 
> Traslación no cambia relaciones de igualdad
> ```
> 
> **Escalamientos (cancelación escalar):**
> 
> ```
> Si α·v = α·w con α ≠ 0
> 
> Geométricamente:
> "Escalar por α" es operación reversible
> (podemos "desescalar" por 1/α)
> 
>     v ----×α----> α·v
>     
>     w ----×α----> α·w
> 
> Si α·v = α·w (misma longitud y dirección)
> y α ≠ 0 (escala no trivial)
> entonces v = w
> 
> Pero si α = 0:
> Todos los vectores → vector cero
> Información perdida, no recuperable
> ```
> 
> **Transformaciones lineales:**
> 
> ```
> T: V → W lineal
> 
> T inyectiva ⟺ "cancelable"
> T(u) = T(v) ⟹ u = v
> 
> Geométricamente:
> T inyectiva significa que no "colapsa" vectores
> diferentes en el mismo punto
> 
> Si T no inyectiva:
> ker(T) ≠ {0}
> Hay vectores no nulos que van a cero
> No podemos "cancelar" T
> ```

## 📚 Teoremas Relacionados

> [!success]- Resultados Importantes **Teorema de cancelación en grupos:**
> 
> ```
> Sea (G, ·) un grupo.
> 
> Para a, b, c ∈ G:
> 1. a · b = a · c ⟹ b = c (cancelación izquierda)
> 2. b · a = c · a ⟹ b = c (cancelación derecha)
> 
> Demostración análoga a caso vectorial
> usando existencia de inversos
> ```
> 
> **Teorema: Inyectividad y cancelación:**
> 
> ```
> Una función f: A → B es inyectiva
> si y solo si es cancelable por la izquierda
> 
> f inyectiva ⟺ [f(a) = f(b) ⟹ a = b]
> 
> En categorías:
> f monomorfismo ⟺ f cancelable por izquierda
> ```
> 
> **Teorema: Dominios de integridad:**
> 
> ```
> En un anillo conmutativo R:
> 
> R es dominio de integridad
> ⟺ Cancelación multiplicativa válida para a ≠ 0
> ⟺ No hay divisores de cero (excepto 0)
> ```
> 
> **Proposición: Unicidad por cancelación:**
> 
> ```
> En espacio vectorial V:
> La ecuación u + x = v tiene solución única
> 
> Existencia: x = v - u
> Unicidad: Si u + x₁ = v y u + x₂ = v
>          entonces u + x₁ = u + x₂
>          por cancelación: x₁ = x₂
> ```

---

**Tags:** #lema-cancelacion #algebra-lineal #grupos #espacios-vectoriales #anillos #dominios-integridad #divisores-cero #invertibilidad #inyectividad #ecuaciones-lineales #cancelacion-aditiva #cancelacion-multiplicativa #propiedades-algebraicas
