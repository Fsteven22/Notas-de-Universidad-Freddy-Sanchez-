# 🔄 Operaciones en un Espacio Vectorial

## 🌟 Concepto Fundamental

> [!info]- Definición Intuitiva **Las operaciones en un espacio vectorial son las reglas algebraicas que gobiernan cómo se combinan vectores entre sí (suma) y con escalares (multiplicación por escalar). Estas operaciones deben satisfacer propiedades específicas (axiomas) que garantizan una estructura coherente y permiten manipulaciones algebraicas predecibles. Las propiedades fundamentales incluyen conmutatividad, asociatividad, existencia de elementos neutros e inversos, y leyes distributivas.**
> 
> **Características clave:**
> 
> - **Dos operaciones fundamentales:** Suma de vectores y multiplicación por escalar
> - **Propiedades estructurales:** 10 axiomas que definen el espacio vectorial
> - **Universalidad:** Mismas propiedades en todos los espacios vectoriales
> - **Cerradura:** Operaciones que mantienen elementos dentro del espacio
> - **Consistencia:** Reglas que permiten manipulación algebraica confiable

### 📖 Contexto Histórico

> [!note]- Desarrollo Histórico **Precursores conceptuales (1600-1800):**
> 
> - **Descartes (1637):** Álgebra de coordenadas
>     - Operaciones componente a componente (implícitas)
> - **Euler (1750s):** Manipulación de vectores
>     - Suma y resta de "líneas dirigidas"
> - **Argand, Wessel (1806):** Números complejos
>     - Operaciones geométricas en el plano
>     - Suma como composición de desplazamientos
> 
> **Formalización de operaciones (1800-1850):**
> 
> - **Möbius (1827):** _Der barycentrische Calcul_
>     - Combinaciones lineales formales
>     - Coordenadas baricéntricas
> - **Grassmann (1844):** _Ausdehnungslehre_
>     - Sistema axiomático de operaciones
>     - Álgebra exterior (productos de vectores)
>     - Poco comprendido en su época
> - **Hamilton (1843):** Cuaterniones
>     - Operaciones no conmutativas
>     - Suma asociativa y conmutativa
>     - Multiplicación más compleja
> 
> **Axiomatización (1850-1900):**
> 
> - **Cayley (1858):** Álgebra de matrices
>     - Operaciones matriciales formales
>     - Suma y producto por escalar
> - **Dedekind, Weber (1880s):** Álgebra abstracta
>     - Estructuras algebraicas generales
> - **Peano (1888):** Axiomas de espacios vectoriales
>     - Formalización definitiva de propiedades
>     - 10 axiomas fundamentales
>     - Primer tratamiento completamente abstracto
> 
> **Consolidación moderna (1900-presente):**
> 
> - **Hilbert (1900s):** Espacios de dimensión infinita
>     - Extensión de operaciones a contextos generales
> - **Banach (1920s):** Espacios normados
>     - Operaciones con topología
> - **Von Neumann (1930s):** Mecánica cuántica
>     - Operaciones en espacios de Hilbert
>     - Aplicaciones físicas
> - **Bourbaki (1940s-1960s):** Estructuras matemáticas
>     - Sistematización rigurosa
>     - Álgebra lineal moderna
> - **Era computacional (1950-presente):**
>     - Implementación numérica de operaciones
>     - Álgebra lineal computacional
>     - Complejidad algorítmica

## 📐 Las Dos Operaciones Fundamentales

> [!important]- Definiciones Formales **1. SUMA DE VECTORES**
> 
> ```
> Operación binaria interna:
> + : V × V → V
> (u⃗, v⃗) ↦ u⃗ + v⃗
> 
> Características:
> • Binaria: toma dos vectores
> • Interna: resultado es vector en V (cerradura)
> • Notación infija: u⃗ + v⃗ (operador entre argumentos)
> 
> Interpretación geométrica (ℝⁿ):
> "Regla del paralelogramo"
> - Colocar origen de v⃗ en extremo de u⃗
> - Suma: vector del origen inicial al extremo final
> 
> O equivalentemente:
> "Regla del triángulo"
> - Sumar componente a componente
> 
> Ejemplo en ℝ²:
> (3, 2) + (1, 4) = (3+1, 2+4) = (4, 6)
> ```
> 
> **2. MULTIPLICACIÓN POR ESCALAR**
> 
> ```
> Operación externa:
> · : F × V → V
> (α, v⃗) ↦ α·v⃗  o  αv⃗
> 
> Características:
> • Externa: mezcla elementos de F (campo) y V
> • Escala: cambia "longitud" pero no "dirección"
> • Notación: αv⃗ (escalar primero, usual)
> 
> Interpretación geométrica:
> α > 0: estira o comprime en misma dirección
> α < 0: estira/comprime e invierte dirección
> α = 0: produce vector cero
> |α| = 1: preserva longitud (±1 invierte)
> 
> Ejemplo en ℝ²:
> 3(2, 1) = (6, 3)
> -2(1, 4) = (-2, -8)
> 0(5, 3) = (0, 0)
> ```
> 
> **Notación y convenciones:**
> 
> ```
> Suma:
> • u⃗ + v⃗ (estándar)
> • Conmutativa: orden no importa
> • Asociativa: agrupación no importa
> 
> Multiplicación por escalar:
> • αv⃗ o α·v⃗ (punto usualmente omitido)
> • No conmutativa con suma de escalares y vectores
> • Distributiva respecto a ambas sumas
> 
> Precedencia:
> αv⃗ + w⃗ = (αv⃗) + w⃗  (multiplicación primero)
> 
> Combinaciones lineales:
> α₁v⃗₁ + α₂v⃗₂ + ... + αₙv⃗ₙ
> = (α₁v⃗₁) + (α₂v⃗₂) + ... + (αₙv⃗ₙ)
> ```

## 🎯 Axiomas de la Suma de Vectores

> [!success]- Propiedades de la Suma (A1-A5) **A1. CERRADURA (Clausura)**
> 
> ```
> ∀u⃗, v⃗ ∈ V : u⃗ + v⃗ ∈ V
> 
> Significado:
> Sumar dos vectores produce otro vector del mismo espacio
> 
> Verificación en ejemplos:
> 
> ℝⁿ: (x₁,...,xₙ) + (y₁,...,yₙ) = (x₁+y₁,...,xₙ+yₙ) ∈ ℝⁿ ✓
> 
> Mₘₓₙ: [Aᵢⱼ] + [Bᵢⱼ] = [Aᵢⱼ + Bᵢⱼ] ∈ Mₘₓₙ ✓
> 
> Pₙ: (a₀+...+aₙxⁿ) + (b₀+...+bₙxⁿ) 
>     = (a₀+b₀)+...+(aₙ+bₙ)xⁿ ∈ Pₙ ✓
> 
> Contraejemplo (NO espacio vectorial):
> Conjunto {(x,y) ∈ ℝ² : x,y > 0} (primer cuadrante)
> (1,1) + (2,2) = (3,3) ∈ conjunto ✓
> Pero: no tiene vector cero → falla A3
> ```
> 
> **A2. ASOCIATIVIDAD**
> 
> ```
> ∀u⃗, v⃗, w⃗ ∈ V : (u⃗ + v⃗) + w⃗ = u⃗ + (v⃗ + w⃗)
> 
> Significado:
> El orden de agrupación no importa
> Podemos escribir u⃗ + v⃗ + w⃗ sin ambigüedad
> 
> Consecuencia:
> Permite sumar múltiples vectores sin paréntesis
> v⃗₁ + v⃗₂ + v⃗₃ + ... + v⃗ₙ está bien definido
> 
> Verificación en ℝⁿ:
> Componente i:
> ((u + v) + w)ᵢ = (u + v)ᵢ + wᵢ 
>                = (uᵢ + vᵢ) + wᵢ
>                = uᵢ + (vᵢ + wᵢ)    (asociatividad en ℝ)
>                = uᵢ + (v + w)ᵢ
>                = (u + (v + w))ᵢ ✓
> 
> Ejemplo numérico en ℝ²:
> u⃗ = (1,2), v⃗ = (3,4), w⃗ = (5,6)
> 
> (u⃗ + v⃗) + w⃗ = (4,6) + (5,6) = (9,12)
> u⃗ + (v⃗ + w⃗) = (1,2) + (8,10) = (9,12) ✓
> ```
> 
> **A3. ELEMENTO NEUTRO (Identidad aditiva)**
> 
> ```
> ∃0⃗ ∈ V : ∀v⃗ ∈ V, v⃗ + 0⃗ = 0⃗ + v⃗ = v⃗
> 
> Significado:
> Existe un vector "cero" que no cambia otros vectores al sumar
> 
> Notación:
> • 0⃗ : vector cero (negrita o flecha para distinguir)
> • 0 : escalar cero (del campo F)
> • Contexto usualmente aclara
> 
> Forma del vector cero en cada espacio:
> 
> ℝⁿ: 0⃗ = (0, 0, ..., 0)
> 
> Mₘₓₙ: 0⃗ = [0] (matriz cero, todas entradas 0)
> 
> Pₙ: 0⃗ = polinomio cero = 0 (todos coeficientes 0)
> 
> C[a,b]: 0⃗ = función cero: f(x) = 0 ∀x ∈ [a,b]
> 
> Unicidad del vector cero:
> Supongamos dos neutros 0⃗ y 0⃗'
> 0⃗' = 0⃗' + 0⃗ = 0⃗ + 0⃗' = 0⃗
> (primera igualdad: 0⃗ es neutro)
> (segunda: conmutatividad)
> (tercera: 0⃗' es neutro)
> ∴ El vector cero es único
> ```
> 
> **A4. ELEMENTO INVERSO (Opuesto aditivo)**
> 
> ```
> ∀v⃗ ∈ V, ∃(-v⃗) ∈ V : v⃗ + (-v⃗) = (-v⃗) + v⃗ = 0⃗
> 
> Significado:
> Cada vector tiene un "opuesto" que suma a cero
> 
> Notación:
> • -v⃗ : opuesto de v⃗ (inverso aditivo)
> • También llamado "negativo" de v⃗
> 
> Forma del opuesto en cada espacio:
> 
> ℝⁿ: -(x₁,...,xₙ) = (-x₁,...,-xₙ)
>     Cambio de signo componente a componente
> 
> Mₘₓₙ: -[Aᵢⱼ] = [-Aᵢⱼ]
>       Cambio de signo entrada por entrada
> 
> Pₙ: -(a₀ + a₁x + ... + aₙxⁿ) 
>     = -a₀ - a₁x - ... - aₙxⁿ
> 
> Funciones: -f donde (-f)(x) = -f(x)
> 
> Unicidad del opuesto:
> Supongamos v⃗ + u⃗ = 0⃗ y v⃗ + w⃗ = 0⃗
> u⃗ = u⃗ + 0⃗ = u⃗ + (v⃗ + w⃗) = (u⃗ + v⃗) + w⃗ = 0⃗ + w⃗ = w⃗
> ∴ El opuesto es único
> 
> Relación con multiplicación por escalar:
> Teorema: -v⃗ = (-1)v⃗
> (se demuestra usando axiomas M)
> ```
> 
> **A5. CONMUTATIVIDAD**
> 
> ```
> ∀u⃗, v⃗ ∈ V : u⃗ + v⃗ = v⃗ + u⃗
> 
> Significado:
> El orden de los sumandos no importa
> 
> Consecuencia:
> Podemos reordenar sumas libremente
> v⃗₁ + v⃗₂ + v⃗₃ = v⃗₃ + v⃗₁ + v⃗₂ = ...
> 
> Verificación en ℝⁿ:
> (u + v)ᵢ = uᵢ + vᵢ = vᵢ + uᵢ = (v + u)ᵢ
> (por conmutatividad en ℝ)
> 
> Interpretación geométrica:
> Paralelogramo: dos caminos al mismo punto
> u⃗ → v⃗  equivale a  v⃗ → u⃗
> 
> Ejemplo numérico:
> (2,3) + (1,5) = (3,8) = (1,5) + (2,3) ✓
> 
> Nota importante:
> Espacios vectoriales son siempre conmutativos
> (algunas álgebras no lo son, ej: matrices con producto)
> ```

## 🔢 Axiomas de la Multiplicación por Escalar

> [!important]- Propiedades del Producto (M1-M5) **M1. CERRADURA BAJO MULTIPLICACIÓN**
> 
> ```
> ∀α ∈ F, ∀v⃗ ∈ V : αv⃗ ∈ V
> 
> Significado:
> Multiplicar un vector por un escalar produce vector en V
> 
> Verificación en ejemplos:
> 
> ℝⁿ: α(x₁,...,xₙ) = (αx₁,...,αxₙ) ∈ ℝⁿ ✓
> 
> Pₙ: α(a₀+...+aₙxⁿ) = (αa₀)+...+(αaₙ)xⁿ ∈ Pₙ ✓
>     Grado no aumenta
> 
> Mₘₓₙ: α[Aᵢⱼ] = [αAᵢⱼ] ∈ Mₘₓₙ ✓
> 
> Contraejemplo (NO cerrado):
> W = {(x,y) ∈ ℝ² : x,y ∈ ℤ} (puntos con coordenadas enteras)
> (1/2)(2,2) = (1,1) ∈ W ✓
> Pero: (1/2)(1,1) = (1/2, 1/2) ∉ W ✗
> → No es espacio vectorial sobre ℝ
> ```
> 
> **M2. DISTRIBUTIVIDAD I (Respecto a suma de vectores)**
> 
> ```
> ∀α ∈ F, ∀u⃗, v⃗ ∈ V : α(u⃗ + v⃗) = αu⃗ + αv⃗
> 
> Significado:
> Multiplicar suma por escalar = suma de multiplicaciones
> 
> Verificación en ℝⁿ:
> α(u + v) = α(u₁+v₁,...,uₙ+vₙ)
>          = (α(u₁+v₁),...,α(uₙ+vₙ))
>          = (αu₁+αv₁,...,αuₙ+αvₙ)    (distributividad en ℝ)
>          = (αu₁,...,αuₙ) + (αv₁,...,αvₙ)
>          = αu + αv ✓
> 
> Ejemplo numérico:
> 3((1,2) + (4,5)) = 3(5,7) = (15,21)
> 3(1,2) + 3(4,5) = (3,6) + (12,15) = (15,21) ✓
> 
> Aplicación:
> Factorización de expresiones vectoriales
> 2v⃗ + 2w⃗ = 2(v⃗ + w⃗)
> ```
> 
> **M3. DISTRIBUTIVIDAD II (Respecto a suma de escalares)**
> 
> ```
> ∀α, β ∈ F, ∀v⃗ ∈ V : (α + β)v⃗ = αv⃗ + βv⃗
> 
> Significado:
> Suma de escalares distribuye sobre vector
> 
> Verificación en ℝⁿ:
> (α + β)v = ((α+β)v₁,...,(α+β)vₙ)
>          = (αv₁+βv₁,...,αvₙ+βvₙ)    (distributividad en ℝ)
>          = (αv₁,...,αvₙ) + (βv₁,...,βvₙ)
>          = αv + βv ✓
> 
> Ejemplo numérico:
> (2 + 3)(1,4) = 5(1,4) = (5,20)
> 2(1,4) + 3(1,4) = (2,8) + (3,12) = (5,20) ✓
> 
> Aplicación:
> Simplificación de expresiones
> 3v⃗ + 5v⃗ = (3+5)v⃗ = 8v⃗
> ```
> 
> **M4. ASOCIATIVIDAD MIXTA**
> 
> ```
> ∀α, β ∈ F, ∀v⃗ ∈ V : α(βv⃗) = (αβ)v⃗
> 
> Significado:
> Multiplicar sucesivamente por escalares = multiplicar por producto
> 
> Verificación en ℝⁿ:
> α(βv) = α(βv₁,...,βvₙ)
>       = (α(βv₁),...,α(βvₙ))
>       = ((αβ)v₁,...,(αβ)vₙ)    (asociatividad en ℝ)
>       = (αβ)v ✓
> 
> Ejemplo numérico:
> 2(3(1,5)) = 2(3,15) = (6,30)
> (2·3)(1,5) = 6(1,5) = (6,30) ✓
> 
> Consecuencia:
> Podemos escribir αβv⃗ sin ambigüedad
> No necesitamos paréntesis
> 
> Potencias (notación informal):
> 2v⃗ + 2v⃗ = 2·2v⃗ = 4v⃗  (NO v⃗²)
> Nota: v⃗² no tiene sentido (no hay producto de vectores aquí)
> ```
> 
> **M5. ELEMENTO NEUTRO MULTIPLICATIVO**
> 
> ```
> ∀v⃗ ∈ V : 1·v⃗ = v⃗
> 
> donde 1 es la identidad multiplicativa del campo F
> 
> Significado:
> Multiplicar por 1 no cambia el vector
> 
> Verificación en ℝⁿ:
> 1·v = 1·(v₁,...,vₙ) = (1·v₁,...,1·vₙ) = (v₁,...,vₙ) = v ✓
> 
> Ejemplo:
> 1·(2,3,4) = (2,3,4) ✓
> 
> Importancia:
> Conecta estructura multiplicativa del campo con vectores
> Garantiza que escalares actúan "naturalmente"
> 
> Nota:
> El 1 es del campo F (ℝ o ℂ usualmente)
> No confundir con vector (1,0,0) en ℝ³
> ```

## 🧮 Propiedades Derivadas

> [!note]- Consecuencias de los Axiomas **TEOREMA 1: Unicidad del vector cero**
> 
> ```
> Enunciado:
> El vector cero es único
> 
> Demostración:
> Supongamos que 0⃗ y 0⃗' son ambos vectores cero
> 
> Como 0⃗ es neutro: 0⃗' = 0⃗' + 0⃗    ... (1)
> Como 0⃗' es neutro: 0⃗' + 0⃗ = 0⃗    ... (2)
> Por conmutatividad: 0⃗ + 0⃗' = 0⃗   ... (3)
> 
> De (1) y (2): 0⃗' = 0⃗
> 
> ∴ Solo hay un vector cero ∎
> ```
> 
> **TEOREMA 2: Unicidad del inverso aditivo**
> 
> ```
> Enunciado:
> Para cada v⃗ ∈ V, su opuesto -v⃗ es único
> 
> Demostración:
> Supongamos u⃗ y w⃗ son ambos opuestos de v⃗
> Es decir: v⃗ + u⃗ = 0⃗ y v⃗ + w⃗ = 0⃗
> 
> u⃗ = u⃗ + 0⃗                (A3: neutro)
>    = u⃗ + (v⃗ + w⃗)         (hipótesis)
>    = (u⃗ + v⃗) + w⃗         (A2: asociatividad)
>    = (v⃗ + u⃗) + w⃗         (A5: conmutatividad)
>    = 0⃗ + w⃗                (hipótesis)
>    = w⃗                     (A3: neutro)
> 
> ∴ u⃗ = w⃗, el opuesto es único ∎
> ```
> 
> **TEOREMA 3: Producto por cero escalar**
> 
> ```
> Enunciado:
> ∀v⃗ ∈ V : 0·v⃗ = 0⃗
> 
> donde 0 es el escalar cero y 0⃗ es el vector cero
> 
> Demostración:
> 0·v⃗ = (0 + 0)·v⃗           (0 = 0+0 en el campo)
>      = 0·v⃗ + 0·v⃗          (M3: distributividad II)
> 
> Sumando -(0·v⃗) a ambos lados:
> 0·v⃗ + (-(0·v⃗)) = (0·v⃗ + 0·v⃗) + (-(0·v⃗))
> 0⃗ = 0·v⃗ + (0·v⃗ + (-(0·v⃗)))    (A2: asociatividad)
> 0⃗ = 0·v⃗ + 0⃗                    (A4: inverso)
> 0⃗ = 0·v⃗                         (A3: neutro)
> 
> ∴ 0·v⃗ = 0⃗ ∎
> ```
> 
> **TEOREMA 4: Producto de escalar por vector cero**
> 
> ```
> Enunciado:
> ∀α ∈ F : α·0⃗ = 0⃗
> 
> Demostración:
> α·0⃗ = α·(0⃗ + 0⃗)          (A3: 0⃗ + 0⃗ = 0⃗)
>      = α·0⃗ + α·0⃗          (M2: distributividad I)
> 
> Sumando -(α·0⃗) a ambos lados:
> α·0⃗ + (-(α·0⃗)) = (α·0⃗ + α·0⃗) + (-(α·0⃗))
> 0⃗ = α·0⃗ + (α·0⃗ + (-(α·0⃗)))
> 0⃗ = α·0⃗ + 0⃗
> 0⃗ = α·0⃗
> 
> ∴ α·0⃗ = 0⃗ ∎
> ```
> 
> **TEOREMA 5: Producto por -1**
> 
> ```
> Enunciado:
> ∀v⃗ ∈ V : (-1)·v⃗ = -v⃗
> 
> Demostración:
> v⃗ + (-1)·v⃗ = 1·v⃗ + (-1)·v⃗      (M5: neutro)
>             = (1 + (-1))·v⃗       (M3: distributividad II)
>             = 0·v⃗                (1 + (-1) = 0 en campo)
>             = 0⃗                  (Teorema 3)
> 
> Por tanto, (-1)·v⃗ es el opuesto de v⃗
> Por unicidad del opuesto: (-1)·v⃗ = -v⃗
> 
> ∴ (-1)·v⃗ = -v⃗ ∎
> 
> Consecuencia:
> El opuesto se puede calcular multiplicando por -1
> ```
> 
> **TEOREMA 6: Ley de cancelación**
> 
> ```
> Enunciado:
> Si αv⃗ = 0⃗, entonces α = 0 o v⃗ = 0⃗
> 
> Demostración (contrapositiva):
> Supongamos α ≠ 0
> Entonces existe α⁻¹ en el campo F
> 
> αv⃗ = 0⃗
> α⁻¹(αv⃗) = α⁻¹·0⃗
> (α⁻¹α)v⃗ = 0⃗            (M4: asociatividad)
> 1·v⃗ = 0⃗                (α⁻¹α = 1 en campo)
> v⃗ = 0⃗                   (M5: neutro)
> 
> ∴ Si α ≠ 0 y αv⃗ = 0⃗, entonces v⃗ = 0⃗ ∎
> ```
> 
> **TEOREMA 7: Cancelación aditiva**
> 
> ```
> Enunciado:
> Si u⃗ + v⃗ = u⃗ + w⃗, entonces v⃗ = w⃗
> 
> Demostración:
> u⃗ + v⃗ = u⃗ + w⃗                    (hipótesis)
> (-u⃗) + (u⃗ + v⃗) = (-u⃗) + (u⃗ + w⃗)  (sumar -u⃗)
> ((-u⃗) + u⃗) + v⃗ = ((-u⃗) + u⃗) + w⃗  (A2: asociatividad)
> 0⃗ + v⃗ = 0⃗ + w⃗                    (A4: inverso)
> v⃗ = w⃗                              (A3: neutro)
> 
> ∴ Podemos "cancelar" u⃗ de ambos lados ∎
> ```
>TEOREMA 8: Opuesto de una suma**
>
> ```
> Enunciado:
> ∀u⃗, v⃗ ∈ V : -(u⃗ + v⃗) = (-u⃗) + (-v⃗)
> 
> Demostración:
> Debemos mostrar que (-u⃗) + (-v⃗) es el opuesto de u⃗ + v⃗
> 
> (u⃗ + v⃗) + [(-u⃗) + (-v⃗)]
> = u⃗ + [v⃗ + ((-u⃗) + (-v⃗))]      (A2: asociatividad)
> = u⃗ + [(v⃗ + (-u⃗)) + (-v⃗)]      (A2)
> = u⃗ + [((-u⃗) + v⃗) + (-v⃗)]      (A5: conmutatividad)
> = u⃗ + [(-u⃗) + (v⃗ + (-v⃗))]      (A2)
> = u⃗ + [(-u⃗) + 0⃗]                (A4: inverso)
> = u⃗ + (-u⃗)                       (A3: neutro)
> = 0⃗                               (A4: inverso)
> 
> Por unicidad del opuesto:
> -(u⃗ + v⃗) = (-u⃗) + (-v⃗) ∎
> 
> Notación práctica:
> -(u⃗ + v⃗) = -u⃗ - v⃗
> ```
> 
> **TEOREMA 9: Opuesto del opuesto**
> 
> ```
> Enunciado:
> ∀v⃗ ∈ V : -(-v⃗) = v⃗
> 
> Demostración:
> Por definición, -v⃗ es el opuesto de v⃗
> Es decir: v⃗ + (-v⃗) = 0⃗
> 
> Esto también se puede escribir:
> (-v⃗) + v⃗ = 0⃗                    (A5: conmutatividad)
> 
> Por tanto, v⃗ es el opuesto de (-v⃗)
> Por unicidad del opuesto: v⃗ = -(-v⃗)
> 
> ∴ -(-v⃗) = v⃗ ∎
> 
> Interpretación geométrica:
> Invertir dirección dos veces = dirección original
> ```
> 
> **TEOREMA 10: Distributividad del opuesto**
> 
> ```
> Enunciado:
> ∀α ∈ F, ∀v⃗ ∈ V : (-α)v⃗ = -(αv⃗) = α(-v⃗)
> 
> Demostración parte 1: (-α)v⃗ = -(αv⃗)
> 
> αv⃗ + (-α)v⃗ = (α + (-α))v⃗        (M3: distributividad II)
>             = 0·v⃗                (campo: α + (-α) = 0)
>             = 0⃗                  (Teorema 3)
> 
> Por tanto, (-α)v⃗ es opuesto de αv⃗
> ∴ (-α)v⃗ = -(αv⃗)
> 
> Demostración parte 2: α(-v⃗) = -(αv⃗)
> 
> αv⃗ + α(-v⃗) = α(v⃗ + (-v⃗))       (M2: distributividad I)
>             = α·0⃗                (A4: inverso)
>             = 0⃗                  (Teorema 4)
> 
> Por tanto, α(-v⃗) es opuesto de αv⃗
> ∴ α(-v⃗) = -(αv⃗)
> 
> Combinando: (-α)v⃗ = -(αv⃗) = α(-v⃗) ∎
> ```

## 🎨 Operación Derivada: Resta de Vectores

> [!tip]- Resta como Operación Secundaria **Definición:**
> 
> ```
> La resta NO es un axioma, se define en términos de suma e inverso:
> 
> u⃗ - v⃗ := u⃗ + (-v⃗)
> 
> Léase: "u menos v es u más el opuesto de v"
> 
> Notación alternativa:
> u⃗ - v⃗ ≡ u⃗ + (-1)v⃗
> 
> No es operación fundamental:
> Se reduce a operaciones primitivas (suma y producto por -1)
> ```
> 
> **Propiedades de la resta:**
> 
> ```
> P1) NO es conmutativa:
>     u⃗ - v⃗ ≠ v⃗ - u⃗ en general
>     
>     De hecho: u⃗ - v⃗ = -(v⃗ - u⃗)
>     
>     Ejemplo en ℝ²:
>     (3,2) - (1,1) = (2,1)
>     (1,1) - (3,2) = (-2,-1) ≠ (2,1)
> 
> P2) NO es asociativa:
>     (u⃗ - v⃗) - w⃗ ≠ u⃗ - (v⃗ - w⃗) en general
>     
>     Expandiendo:
>     (u⃗ - v⃗) - w⃗ = u⃗ + (-v⃗) + (-w⃗) = u⃗ - v⃗ - w⃗
>     u⃗ - (v⃗ - w⃗) = u⃗ + (-(v⃗ - w⃗)) = u⃗ + (-v⃗ + w⃗) = u⃗ - v⃗ + w⃗
>     
>     Ejemplo en ℝ:
>     (5 - 3) - 2 = 2 - 2 = 0
>     5 - (3 - 2) = 5 - 1 = 4 ≠ 0
> 
> P3) Elemento neutro (derecho):
>     v⃗ - 0⃗ = v⃗ + (-0⃗) = v⃗ + 0⃗ = v⃗
>     
>     Pero: 0⃗ - v⃗ = -v⃗ ≠ v⃗ (en general)
> 
> P4) Auto-resta:
>     v⃗ - v⃗ = v⃗ + (-v⃗) = 0⃗
>     
>     Todo vector menos sí mismo es cero
> 
> P5) Distributividad con escalares:
>     α(u⃗ - v⃗) = αu⃗ - αv⃗
>     
>     Demostración:
>     α(u⃗ - v⃗) = α(u⃗ + (-v⃗))
>               = αu⃗ + α(-v⃗)      (M2)
>               = αu⃗ + (-(αv⃗))    (Teorema 10)
>               = αu⃗ - αv⃗
> ```
> 
> **Interpretación geométrica:**
> 
> ```
> En ℝⁿ, la resta u⃗ - v⃗ representa:
> 
> 1. Vector desplazamiento de v⃗ a u⃗
>    "Qué hay que sumar a v⃗ para llegar a u⃗"
> 
> 2. Si u⃗ y v⃗ son puntos:
>    u⃗ - v⃗ = vector que apunta de v⃗ hacia u⃗
> 
> Visualización:
>       u⃗
>      /|
>     / | u⃗-v⃗
>    /  |
>   /   |
>  v⃗----+
> 
> Construcción:
> - Colocar origen de u⃗ y v⃗ en mismo punto
> - u⃗ - v⃗ va de punta de v⃗ a punta de u⃗
> 
> Ejemplo en ℝ²:
> u⃗ = (5, 3), v⃗ = (2, 1)
> u⃗ - v⃗ = (3, 2)
> 
> Vector de (2,1) a (5,3) es efectivamente (3,2)
> ```

## 🧩 Ejemplos de Verificación de Axiomas

> [!example]- Verificación Completa **Ejemplo 1: Matrices 2×2**
> 
> ```
> V = M₂ₓ₂(ℝ) = {[a b] : a,b,c,d ∈ ℝ}
>                 [c d]
> 
> Suma: [a₁ b₁] + [a₂ b₂] = [a₁+a₂  b₁+b₂]
>       [c₁ d₁]   [c₂ d₂]   [c₁+c₂  d₁+d₂]
> 
> Producto: α[a b] = [αa  αb]
>            [c d]   [αc  αd]
> 
> VERIFICACIÓN DE AXIOMAS:
> 
> (A1) Cerradura suma: ✓ (entradas son sumas de reales)
> 
> (A2) Asociatividad:
>      ((A+B)+C)ᵢⱼ = (A+B)ᵢⱼ + Cᵢⱼ
>                  = (Aᵢⱼ + Bᵢⱼ) + Cᵢⱼ
>                  = Aᵢⱼ + (Bᵢⱼ + Cᵢⱼ)    (asociat. en ℝ)
>                  = Aᵢⱼ + (B+C)ᵢⱼ
>                  = (A+(B+C))ᵢⱼ ✓
> 
> (A3) Neutro: 0⃗ = [0 0] ✓
>                  [0 0]
> 
> (A4) Inverso: -[a b] = [-a -b] ✓
>               [c d]   [-c -d]
> 
> (A5) Conmutatividad:
>      (A+B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ = Bᵢⱼ + Aᵢⱼ = (B+A)ᵢⱼ ✓
> 
> (M1) Cerradura producto: ✓
> 
> (M2) Distributividad I:
>      (α(A+B))ᵢⱼ = α(A+B)ᵢⱼ = α(Aᵢⱼ+Bᵢⱼ)
>                 = αAᵢⱼ + αBᵢⱼ        (distrib. en ℝ)
>                 = (αA)ᵢⱼ + (αB)ᵢⱼ
>                 = (αA + αB)ᵢⱼ ✓
> 
> (M3) Distributividad II:
>      ((α+β)A)ᵢⱼ = (α+β)Aᵢⱼ
>                 = αAᵢⱼ + βAᵢⱼ        (distrib. en ℝ)
>                 = (αA)ᵢⱼ + (βA)ᵢⱼ
>                 = (αA + βA)ᵢⱼ ✓
> 
> (M4) Asociatividad:
>      (α(βA))ᵢⱼ = α(βA)ᵢⱼ = α(βAᵢⱼ)
>                = (αβ)Aᵢⱼ             (asociat. en ℝ)
>                = ((αβ)A)ᵢⱼ ✓
> 
> (M5) Neutro: 1·[a b] = [a b] ✓
>               [c d]   [c d]
> 
> ∴ M₂ₓ₂(ℝ) es espacio vectorial sobre ℝ ∎
> ```
> 
> **Ejemplo 2: Polinomios de grado ≤ 2**
> 
> ```
> V = P₂(ℝ) = {a₀ + a₁x + a₂x² : a₀,a₁,a₂ ∈ ℝ}
> 
> Suma: (a₀+a₁x+a₂x²) + (b₀+b₁x+b₂x²)
>     = (a₀+b₀) + (a₁+b₁)x + (a₂+b₂)x²
> 
> Producto: α(a₀+a₁x+a₂x²) = (αa₀) + (αa₁)x + (αa₂)x²
> 
> VERIFICACIÓN (selección):
> 
> (A1) Cerradura:
>      Grado de suma ≤ max(deg p, deg q) ≤ 2 ✓
> 
> (A3) Neutro: 0⃗ = 0 + 0x + 0x² = polinomio cero ✓
> 
> (A4) Inverso: -(a₀+a₁x+a₂x²) = -a₀ - a₁x - a₂x² ✓
> 
> (M1) Cerradura:
>      Grado de αp ≤ deg p ≤ 2 ✓
>      (multiplicar por escalar no aumenta grado)
> 
> Todas las propiedades se heredan de ℝ
> operando sobre coeficientes
> 
> ∴ P₂(ℝ) es espacio vectorial sobre ℝ ∎
> ```
> 
> **Contraejemplo: NO es espacio vectorial**
> 
> ```
> W = {(x, y) ∈ ℝ² : xy = 0} (ejes coordenados)
> 
> Con operaciones usuales de ℝ²
> 
> FALLA CERRADURA BAJO SUMA:
> 
> (1, 0) ∈ W  ✓  (1·0 = 0)
> (0, 1) ∈ W  ✓  (0·1 = 0)
> 
> Pero: (1, 0) + (0, 1) = (1, 1) ∉ W
> Porque: 1·1 = 1 ≠ 0
> 
> ∴ W NO es espacio vectorial (falla A1) ✗
> 
> Interpretación geométrica:
> Unión de ejes x e y
> Suma de vectores "sale" de los ejes
> ```

## 📊 Tabla Resumen de Axiomas

> [!important]- Referencia Rápida
> 
> ```
> ╔═══════════════════════════════════════════════════════════════╗
> ║                   AXIOMAS DE ESPACIO VECTORIAL                ║
> ╠═══════════════════════════════════════════════════════════════╣
> ║ SUMA DE VECTORES                                              ║
> ╟───────────────────────────────────────────────────────────────╢
> ║ (A1) Cerradura       │ u⃗ + v⃗ ∈ V                            ║
> ║ (A2) Asociatividad   │ (u⃗+v⃗)+w⃗ = u⃗+(v⃗+w⃗)                  ║
> ║ (A3) Neutro          │ ∃0⃗: v⃗+0⃗ = v⃗                         ║
> ║ (A4) Inverso         │ ∃(-v⃗): v⃗+(-v⃗) = 0⃗                   ║
> ║ (A5) Conmutatividad  │ u⃗ + v⃗ = v⃗ + u⃗                       ║
> ╟───────────────────────────────────────────────────────────────╢
> ║ MULTIPLICACIÓN POR ESCALAR                                    ║
> ╟───────────────────────────────────────────────────────────────╢
> ║ (M1) Cerradura       │ αv⃗ ∈ V                                ║
> ║ (M2) Distributiva I  │ α(u⃗+v⃗) = αu⃗+αv⃗                      ║
> ║ (M3) Distributiva II │ (α+β)v⃗ = αv⃗+βv⃗                      ║
> ║ (M4) Asociatividad   │ α(βv⃗) = (αβ)v⃗                        ║
> ║ (M5) Neutro          │ 1·v⃗ = v⃗                              ║
> ╚═══════════════════════════════════════════════════════════════╝
> 
> PROPIEDADES DERIVADAS:
> • 0·v⃗ = 0⃗
> • α·0⃗ = 0⃗
> • (-1)v⃗ = -v⃗
> • -(u⃗+v⃗) = -u⃗ + (-v⃗)
> • -(-v⃗) = v⃗
> • αv⃗ = 0⃗ ⟹ α=0 o v⃗=0⃗
> • Unicidad de 0⃗ y -v⃗
> ```

## ⚠️ Errores Comunes

> [!warning]- Malentendidos Frecuentes **1. "Conmutatividad en multiplicación por escalar"**
> 
> ```
> ✗ FALSO: v⃗α ≠ αv⃗ en general
> 
> La multiplicación por escalar es EXTERNA:
> F × V → V
> 
> αv⃗ está definido (escalar × vector)
> v⃗α NO está definido (vector × escalar)
> 
> Notación: SIEMPRE αv⃗ (escalar primero)
> 
> Excepción: En algunos contextos (física)
> se escribe v⃗α por conveniencia, pero
> se entiende como αv⃗
> ```
> 
> **2. "0 y 0⃗ son lo mismo"**
> 
> ```
> ✗ FALSO
> 
> 0: escalar cero (elemento de F)
> 0⃗: vector cero (elemento de V)
> 
> Son objetos diferentes en estructuras diferentes
> 
> Correcto:
> • 0 + 0 = 0 (suma de escalares)
> • 0⃗ + 0⃗ = 0⃗ (suma de vectores)
> • 0·v⃗ = 0⃗ (producto → vector)
> 
> Incorrecto:
> • 0 + 0⃗ (no tiene sentido, tipos diferentes)
> ```
> 
> **3. "La resta es conmutativa"**
> 
> ```
> ✗ FALSO
> 
> u⃗ - v⃗ ≠ v⃗ - u⃗ en general
> 
> De hecho: u⃗ - v⃗ = -(v⃗ - u⃗)
> 
> Ejemplo:
> (5,0) - (2,0) = (3,0)
> (2,0) - (5,0) = (-3,0) ≠ (3,0)
> ```
> 
> **4. "αv⃗ = 0⃗ implica α = 0"**
> 
> ```
> ✗ FALSO (incompleto)
> 
> Correcto: αv⃗ = 0⃗ ⟹ α = 0 O v⃗ = 0⃗
> 
> Contraejemplos:
> • 5·0⃗ = 0⃗ pero 5 ≠ 0
> • 0·v⃗ = 0⃗ pero v⃗ ≠ 0⃗ (si v⃗ cualquiera)
> 
> Solo si sabemos que uno NO es cero,
> podemos concluir que el otro SÍ lo es
> ```
> 
> **5. "Todo conjunto con suma es espacio vectorial"**
> 
> ```
> ✗ FALSO
> 
> Contraejemplo:
> ℤⁿ = {(x₁,...,xₙ) : xᵢ ∈ ℤ} con suma usual
> 
> Problema: NO cerrado bajo multiplicación por ℝ
> (1/2)(2,2) = (1,1) ∈ ℤ² ✓
> (1/2)(1,1) = (1/2, 1/2) ∉ ℤ² ✗
> 
> No es espacio vectorial sobre ℝ
> (Sí sobre ℤ, pero ℤ no es campo)
> ```
> 
> **6. "Asociatividad implica conmutatividad"**
> 
> ```
> ✗ FALSO
> 
> Son propiedades independientes
> 
> Ejemplo: Multiplicación de matrices
> • Asociativa: (AB)C = A(BC) ✓
> • NO conmutativa: AB ≠ BA en general ✗
> 
> En espacios vectoriales:
> • Suma es asociativa Y conmutativa
> • Ambas son axiomas independientes
> ```
> 
> **7. "(-v⃗) significa 'negativo de v⃗'"**
> 
> ```
> ⚠️ CUIDADO con terminología
> 
> -v⃗ es el "opuesto" o "inverso aditivo"
> 
> "Negativo" puede confundir:
> Si v⃗ = (1,2), entonces -v⃗ = (-1,-2)
> 
> Las componentes cambian de signo, pero
> conceptualmente es "el vector que sumado
> a v⃗ da 0⃗"
> 
> Mejor: "opuesto de v⃗" o "menos v⃗"
> ```

## 🔗 Conexiones con Otros Temas

> [!quote]- Enlaces Conceptuales **Fundamentos previos:**
> 
> - [[Álgebra abstracta]] - Grupos, anillos, campos
> - [[Teoría de conjuntos]] - Operaciones binarias
> - [[Lógica matemática]] - Axiomas y demostraciones
> 
> **Temas relacionados:**
> 
> - [[09 - Vectores en espacios vectoriales]] - Estructura general
> - [[01 - Subespacios Vectoriales]] - Herencia de operaciones
> - [[Transformaciones lineales]] - Preservación de operaciones
> - [[Producto interno]] - Operación adicional
> 
> **Aplicaciones posteriores:**
> 
> - [[Álgebra lineal numérica]] - Implementación computacional
> - [[Análisis funcional]] - Espacios infinito-dimensionales
> - [[Geometría diferencial]] - Espacios tangentes
> - [[Mecánica cuántica]] - Superposición de estados
> - [[Teoría de control]] - Sistemas lineales

## 📚 Recursos Adicionales

> [!note]- Herramientas y Referencias **Software para manipulación:**
> 
> - **MATLAB/Octave:** Operaciones vectoriales y matriciales
> - **Python (NumPy):** numpy.add(), numpy.multiply()
> - **Mathematica:** Operaciones simbólicas
> - **SageMath:** Álgebra abstracta
> 
> **Visualización:**
> 
> - **GeoGebra:** Visualizar suma y producto en ℝ² y ℝ³
> - **3Blue1Brown:** Videos sobre operaciones lineales
> - **Desmos:** Visualización 2D interactiva
> 
> **Tutoriales:**
> 
> - [Khan Academy - Vector Spaces](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces)
> - [MIT OCW - Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06-linear-algebra-spring-2010/)
> - [3Blue1Brown - Essence of Linear Algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)

## 📖 Bibliografía Esencial

> [!tip]- Lecturas Recomendadas **Nivel introductorio:**
> 
> - **Kolman, B., & Hill, D.** (2006). _Álgebra Lineal_. Pearson.
>     - Cap. 4.1-4.2: Espacios vectoriales y propiedades
> - **Lay, D. C.** (2016). _Álgebra Lineal y sus Aplicaciones_. Pearson.
>     - Cap. 4.1: Espacios vectoriales y subespacios
> 
> **Nivel intermedio:**
> 
> - **Anton, H.** (2014). _Álgebra Lineal Elemental_. Wiley.
>     - Cap. 5.1: Axiomas de espacios vectoriales
> - **Strang, G.** (2016). _Introduction to Linear Algebra_. Wellesley-Cambridge.
>     - Enfoque geométrico de operaciones
> 
> **Nivel avanzado:**
> 
> - **Axler, S.** (2015). _Linear Algebra Done Right_. Springer.
>     - Cap. 1: Espacios vectoriales
>     - Tratamiento abstracto y riguroso
> - **Hoffman, K., & Kunze, R.** (1971). _Linear Algebra_. Pearson.
>     - Enfoque axiomático profundo

---

**Tags:** #operaciones-vectoriales #axiomas #suma-vectores #multiplicacion-escalar #espacios-vectoriales #propiedades-algebraicas #cerradura #asociatividad #conmutatividad #neutro #inverso #distributividad #algebra-lineal #estructuras-algebraicas
