---
dg-publish: true
---

# 🔄 Operaciones en un Espacio Vectorial

## 🌟 Concepto Fundamental

> [!info] Definición Intuitiva **Las operaciones en un espacio vectorial son las reglas algebraicas que gobiernan cómo se combinan vectores entre sí (suma) y con escalares (multiplicación por escalar). Estas operaciones deben satisfacer propiedades específicas (axiomas) que garantizan una estructura coherente y permiten manipulaciones algebraicas predecibles. Las propiedades fundamentales incluyen conmutatividad, asociatividad, existencia de elementos neutros e inversos, y leyes distributivas.**
> 
> **Características clave:**
> 
> - **Dos operaciones fundamentales:** Suma de vectores y multiplicación por escalar
> - **Propiedades estructurales:** 10 axiomas que definen el espacio vectorial
> - **Universalidad:** Mismas propiedades en todos los espacios vectoriales
> - **Cerradura:** Operaciones que mantienen elementos dentro del espacio
> - **Consistencia:** Reglas que permiten manipulación algebraica confiable

### 📖 Contexto Histórico

> [!note] Desarrollo Histórico **Precursores conceptuales (1600-1800):**
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

> [!important] Definiciones Formales **1. SUMA DE VECTORES**
> 
> ```
> Operación binaria interna:
> + : V × V → V
> (\vec{u}, \vec{v}) ↦ \vec{u} + \vec{v}
> 
> Características:
> • Binaria: toma dos vectores
> • Interna: resultado es vector en V (cerradura)
> • Notación infija: \vec{u} + \vec{v} (operador entre argumentos)
> 
> Interpretación geométrica (ℝⁿ):
> "Regla del paralelogramo"
> - Colocar origen de \vec{v} en extremo de \vec{u}
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
> (α, \vec{v}) ↦ α·\vec{v}  o  α\vec{v}
> 
> Características:
> • Externa: mezcla elementos de F (campo) y V
> • Escala: cambia "longitud" pero no "dirección"
> • Notación: α\vec{v} (escalar primero, usual)
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
> • \vec{u} + \vec{v} (estándar)
> • Conmutativa: orden no importa
> • Asociativa: agrupación no importa
> 
> Multiplicación por escalar:
> • α\vec{v} o α·\vec{v} (punto usualmente omitido)
> • No conmutativa con suma de escalares y vectores
> • Distributiva respecto a ambas sumas
> 
> Precedencia:
> α\vec{v} + \vec{w} = (α\vec{v}) + \vec{w}  (multiplicación primero)
> 
> Combinaciones lineales:
> α₁\vec{v}₁ + α₂\vec{v}₂ + ... + αₙ\vec{v}ₙ
> = (α₁\vec{v}₁) + (α₂\vec{v}₂) + ... + (αₙ\vec{v}ₙ)
> ```

## 🎯 Axiomas de la Suma de Vectores

> [!success] Propiedades de la Suma (A1-A5) **A1. CERRADURA (Clausura)**
> 
> ```
> ∀\vec{u}, \vec{v} ∈ V : \vec{u} + \vec{v} ∈ V
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
> ∀\vec{u}, \vec{v}, \vec{w} ∈ V : (\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})
> 
> Significado:
> El orden de agrupación no importa
> Podemos escribir \vec{u} + \vec{v} + \vec{w} sin ambigüedad
> 
> Consecuencia:
> Permite sumar múltiples vectores sin paréntesis
> \vec{v}₁ + \vec{v}₂ + \vec{v}₃ + ... + \vec{v}ₙ está bien definido
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
> \vec{u} = (1,2), \vec{v} = (3,4), \vec{w} = (5,6)
> 
> (\vec{u} + \vec{v}) + \vec{w} = (4,6) + (5,6) = (9,12)
> \vec{u} + (\vec{v} + \vec{w}) = (1,2) + (8,10) = (9,12) ✓
> ```
> 
> **A3. ELEMENTO NEUTRO (Identidad aditiva)**
> 
> ```
> ∃0⃗ ∈ V : ∀\vec{v} ∈ V, \vec{v} + 0⃗ = 0⃗ + \vec{v} = \vec{v}
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
> ∀\vec{v} ∈ V, ∃(-\vec{v}) ∈ V : \vec{v} + (-\vec{v}) = (-\vec{v}) + \vec{v} = 0⃗
> 
> Significado:
> Cada vector tiene un "opuesto" que suma a cero
> 
> Notación:
> • -\vec{v} : opuesto de \vec{v} (inverso aditivo)
> • También llamado "negativo" de \vec{v}
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
> Supongamos \vec{v} + \vec{u} = 0⃗ y \vec{v} + \vec{w} = 0⃗
> \vec{u} = \vec{u} + 0⃗ = \vec{u} + (\vec{v} + \vec{w}) = (\vec{u} + \vec{v}) + \vec{w} = 0⃗ + \vec{w} = \vec{w}
> ∴ El opuesto es único
> 
> Relación con multiplicación por escalar:
> Teorema: -\vec{v} = (-1)\vec{v}
> (se demuestra usando axiomas M)
> ```
> 
> **A5. CONMUTATIVIDAD**
> 
> ```
> ∀\vec{u}, \vec{v} ∈ V : \vec{u} + \vec{v} = \vec{v} + \vec{u}
> 
> Significado:
> El orden de los sumandos no importa
> 
> Consecuencia:
> Podemos reordenar sumas libremente
> \vec{v}₁ + \vec{v}₂ + \vec{v}₃ = \vec{v}₃ + \vec{v}₁ + \vec{v}₂ = ...
> 
> Verificación en ℝⁿ:
> (u + v)ᵢ = uᵢ + vᵢ = vᵢ + uᵢ = (v + u)ᵢ
> (por conmutatividad en ℝ)
> 
> Interpretación geométrica:
> Paralelogramo: dos caminos al mismo punto
> \vec{u} → \vec{v}  equivale a  \vec{v} → \vec{u}
> 
> Ejemplo numérico:
> (2,3) + (1,5) = (3,8) = (1,5) + (2,3) ✓
> 
> Nota importante:
> Espacios vectoriales son siempre conmutativos
> (algunas álgebras no lo son, ej: matrices con producto)
> ```

## 🔢 Axiomas de la Multiplicación por Escalar

> [!important] Propiedades del Producto (M1-M5) **M1. CERRADURA BAJO MULTIPLICACIÓN**
> 
> ```
> ∀α ∈ F, ∀\vec{v} ∈ V : α\vec{v} ∈ V
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
> ∀α ∈ F, ∀\vec{u}, \vec{v} ∈ V : α(\vec{u} + \vec{v}) = α\vec{u} + α\vec{v}
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
> 2\vec{v} + 2\vec{w} = 2(\vec{v} + \vec{w})
> ```
> 
> **M3. DISTRIBUTIVIDAD II (Respecto a suma de escalares)**
> 
> ```
> ∀α, β ∈ F, ∀\vec{v} ∈ V : (α + β)\vec{v} = α\vec{v} + β\vec{v}
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
> 3\vec{v} + 5\vec{v} = (3+5)\vec{v} = 8\vec{v}
> ```
> 
> **M4. ASOCIATIVIDAD MIXTA**
> 
> ```
> ∀α, β ∈ F, ∀\vec{v} ∈ V : α(β\vec{v}) = (αβ)\vec{v}
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
> Podemos escribir αβ\vec{v} sin ambigüedad
> No necesitamos paréntesis
> 
> Potencias (notación informal):
> 2\vec{v} + 2\vec{v} = 2·2\vec{v} = 4\vec{v}  (NO \vec{v}²)
> Nota: \vec{v}² no tiene sentido (no hay producto de vectores aquí)
> ```
> 
> **M5. ELEMENTO NEUTRO MULTIPLICATIVO**
> 
> ```
> ∀\vec{v} ∈ V : 1·\vec{v} = \vec{v}
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

> [!note] Consecuencias de los Axiomas **TEOREMA 1: Unicidad del vector cero**
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
> Para cada \vec{v} ∈ V, su opuesto -\vec{v} es único
> 
> Demostración:
> Supongamos \vec{u} y \vec{w} son ambos opuestos de \vec{v}
> Es decir: \vec{v} + \vec{u} = 0⃗ y \vec{v} + \vec{w} = 0⃗
> 
> \vec{u} = \vec{u} + 0⃗                (A3: neutro)
>    = \vec{u} + (\vec{v} + \vec{w})         (hipótesis)
>    = (\vec{u} + \vec{v}) + \vec{w}         (A2: asociatividad)
>    = (\vec{v} + \vec{u}) + \vec{w}         (A5: conmutatividad)
>    = 0⃗ + \vec{w}                (hipótesis)
>    = \vec{w}                     (A3: neutro)
> 
> ∴ \vec{u} = \vec{w}, el opuesto es único ∎
> ```
> 
> **TEOREMA 3: Producto por cero escalar**
> 
> ```
> Enunciado:
> ∀\vec{v} ∈ V : 0·\vec{v} = 0⃗
> 
> donde 0 es el escalar cero y 0⃗ es el vector cero
> 
> Demostración:
> 0·\vec{v} = (0 + 0)·\vec{v}           (0 = 0+0 en el campo)
>      = 0·\vec{v} + 0·\vec{v}          (M3: distributividad II)
> 
> Sumando -(0·\vec{v}) a ambos lados:
> 0·\vec{v} + (-(0·\vec{v})) = (0·\vec{v} + 0·\vec{v}) + (-(0·\vec{v}))
> 0⃗ = 0·\vec{v} + (0·\vec{v} + (-(0·\vec{v})))    (A2: asociatividad)
> 0⃗ = 0·\vec{v} + 0⃗                    (A4: inverso)
> 0⃗ = 0·\vec{v}                         (A3: neutro)
> 
> ∴ 0·\vec{v} = 0⃗ ∎
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
> ∀\vec{v} ∈ V : (-1)·\vec{v} = -\vec{v}
> 
> Demostración:
> \vec{v} + (-1)·\vec{v} = 1·\vec{v} + (-1)·\vec{v}      (M5: neutro)
>             = (1 + (-1))·\vec{v}       (M3: distributividad II)
>             = 0·\vec{v}                (1 + (-1) = 0 en campo)
>             = 0⃗                  (Teorema 3)
> 
> Por tanto, (-1)·\vec{v} es el opuesto de \vec{v}
> Por unicidad del opuesto: (-1)·\vec{v} = -\vec{v}
> 
> ∴ (-1)·\vec{v} = -\vec{v} ∎
> 
> Consecuencia:
> El opuesto se puede calcular multiplicando por -1
> ```
> 
> **TEOREMA 6: Ley de cancelación**
> 
> ```
> Enunciado:
> Si α\vec{v} = 0⃗, entonces α = 0 o \vec{v} = 0⃗
> 
> Demostración (contrapositiva):
> Supongamos α ≠ 0
> Entonces existe α⁻¹ en el campo F
> 
> α\vec{v} = 0⃗
> α⁻¹(α\vec{v}) = α⁻¹·0⃗
> (α⁻¹α)\vec{v} = 0⃗            (M4: asociatividad)
> 1·\vec{v} = 0⃗                (α⁻¹α = 1 en campo)
> \vec{v} = 0⃗                   (M5: neutro)
> 
> ∴ Si α ≠ 0 y α\vec{v} = 0⃗, entonces \vec{v} = 0⃗ ∎
> ```
> 
> **TEOREMA 7: Cancelación aditiva**
> 
> ```
> Enunciado:
> Si \vec{u} + \vec{v} = \vec{u} + \vec{w}, entonces \vec{v} = \vec{w}
> 
> Demostración:
> \vec{u} + \vec{v} = \vec{u} + \vec{w}                    (hipótesis)
> (-\vec{u}) + (\vec{u} + \vec{v}) = (-\vec{u}) + (\vec{u} + \vec{w})  (sumar -\vec{u})
> ((-\vec{u}) + \vec{u}) + \vec{v} = ((-\vec{u}) + \vec{u}) + \vec{w}  (A2: asociatividad)
> 0⃗ + \vec{v} = 0⃗ + \vec{w}                    (A4: inverso)
> \vec{v} = \vec{w}                              (A3: neutro)
> 
> ∴ Podemos "cancelar" \vec{u} de ambos lados ∎
> ```
>TEOREMA 8: Opuesto de una suma**
>
> ```
> Enunciado:
> ∀\vec{u}, \vec{v} ∈ V : -(\vec{u} + \vec{v}) = (-\vec{u}) + (-\vec{v})
> 
> Demostración:
> Debemos mostrar que (-\vec{u}) + (-\vec{v}) es el opuesto de \vec{u} + \vec{v}
> 
> (\vec{u} + \vec{v}) + [(-\vec{u}) + (-\vec{v})]
> = \vec{u} + [\vec{v} + ((-\vec{u}) + (-\vec{v}))]      (A2: asociatividad)
> = \vec{u} + [(\vec{v} + (-\vec{u})) + (-\vec{v})]      (A2)
> = \vec{u} + [((-\vec{u}) + \vec{v}) + (-\vec{v})]      (A5: conmutatividad)
> = \vec{u} + [(-\vec{u}) + (\vec{v} + (-\vec{v}))]      (A2)
> = \vec{u} + [(-\vec{u}) + 0⃗]                (A4: inverso)
> = \vec{u} + (-\vec{u})                       (A3: neutro)
> = 0⃗                               (A4: inverso)
> 
> Por unicidad del opuesto:
> -(\vec{u} + \vec{v}) = (-\vec{u}) + (-\vec{v}) ∎
> 
> Notación práctica:
> -(\vec{u} + \vec{v}) = -\vec{u} - \vec{v}
> ```
> 
> **TEOREMA 9: Opuesto del opuesto**
> 
> ```
> Enunciado:
> ∀\vec{v} ∈ V : -(-\vec{v}) = \vec{v}
> 
> Demostración:
> Por definición, -\vec{v} es el opuesto de \vec{v}
> Es decir: \vec{v} + (-\vec{v}) = 0⃗
> 
> Esto también se puede escribir:
> (-\vec{v}) + \vec{v} = 0⃗                    (A5: conmutatividad)
> 
> Por tanto, \vec{v} es el opuesto de (-\vec{v})
> Por unicidad del opuesto: \vec{v} = -(-\vec{v})
> 
> ∴ -(-\vec{v}) = \vec{v} ∎
> 
> Interpretación geométrica:
> Invertir dirección dos veces = dirección original
> ```
> 
> **TEOREMA 10: Distributividad del opuesto**
> 
> ```
> Enunciado:
> ∀α ∈ F, ∀\vec{v} ∈ V : (-α)\vec{v} = -(α\vec{v}) = α(-\vec{v})
> 
> Demostración parte 1: (-α)\vec{v} = -(α\vec{v})
> 
> α\vec{v} + (-α)\vec{v} = (α + (-α))\vec{v}        (M3: distributividad II)
>             = 0·\vec{v}                (campo: α + (-α) = 0)
>             = 0⃗                  (Teorema 3)
> 
> Por tanto, (-α)\vec{v} es opuesto de α\vec{v}
> ∴ (-α)\vec{v} = -(α\vec{v})
> 
> Demostración parte 2: α(-\vec{v}) = -(α\vec{v})
> 
> α\vec{v} + α(-\vec{v}) = α(\vec{v} + (-\vec{v}))       (M2: distributividad I)
>             = α·0⃗                (A4: inverso)
>             = 0⃗                  (Teorema 4)
> 
> Por tanto, α(-\vec{v}) es opuesto de α\vec{v}
> ∴ α(-\vec{v}) = -(α\vec{v})
> 
> Combinando: (-α)\vec{v} = -(α\vec{v}) = α(-\vec{v}) ∎
> ```

## 🎨 Operación Derivada: Resta de Vectores

> [!tip] Resta como Operación Secundaria **Definición:**
> 
> ```
> La resta NO es un axioma, se define en términos de suma e inverso:
> 
> \vec{u} - \vec{v} := \vec{u} + (-\vec{v})
> 
> Léase: "u menos v es u más el opuesto de v"
> 
> Notación alternativa:
> \vec{u} - \vec{v} ≡ \vec{u} + (-1)\vec{v}
> 
> No es operación fundamental:
> Se reduce a operaciones primitivas (suma y producto por -1)
> ```
> 
> **Propiedades de la resta:**
> 
> ```
> P1) NO es conmutativa:
>     \vec{u} - \vec{v} ≠ \vec{v} - \vec{u} en general
>     
>     De hecho: \vec{u} - \vec{v} = -(\vec{v} - \vec{u})
>     
>     Ejemplo en ℝ²:
>     (3,2) - (1,1) = (2,1)
>     (1,1) - (3,2) = (-2,-1) ≠ (2,1)
> 
> P2) NO es asociativa:
>     (\vec{u} - \vec{v}) - \vec{w} ≠ \vec{u} - (\vec{v} - \vec{w}) en general
>     
>     Expandiendo:
>     (\vec{u} - \vec{v}) - \vec{w} = \vec{u} + (-\vec{v}) + (-\vec{w}) = \vec{u} - \vec{v} - \vec{w}
>     \vec{u} - (\vec{v} - \vec{w}) = \vec{u} + (-(\vec{v} - \vec{w})) = \vec{u} + (-\vec{v} + \vec{w}) = \vec{u} - \vec{v} + \vec{w}
>     
>     Ejemplo en ℝ:
>     (5 - 3) - 2 = 2 - 2 = 0
>     5 - (3 - 2) = 5 - 1 = 4 ≠ 0
> 
> P3) Elemento neutro (derecho):
>     \vec{v} - 0⃗ = \vec{v} + (-0⃗) = \vec{v} + 0⃗ = \vec{v}
>     
>     Pero: 0⃗ - \vec{v} = -\vec{v} ≠ \vec{v} (en general)
> 
> P4) Auto-resta:
>     \vec{v} - \vec{v} = \vec{v} + (-\vec{v}) = 0⃗
>     
>     Todo vector menos sí mismo es cero
> 
> P5) Distributividad con escalares:
>     α(\vec{u} - \vec{v}) = α\vec{u} - α\vec{v}
>     
>     Demostración:
>     α(\vec{u} - \vec{v}) = α(\vec{u} + (-\vec{v}))
>               = α\vec{u} + α(-\vec{v})      (M2)
>               = α\vec{u} + (-(α\vec{v}))    (Teorema 10)
>               = α\vec{u} - α\vec{v}
> ```
> 
> **Interpretación geométrica:**
> 
> ```
> En ℝⁿ, la resta \vec{u} - \vec{v} representa:
> 
> 1. Vector desplazamiento de \vec{v} a \vec{u}
>    "Qué hay que sumar a \vec{v} para llegar a \vec{u}"
> 
> 2. Si \vec{u} y \vec{v} son puntos:
>    \vec{u} - \vec{v} = vector que apunta de \vec{v} hacia \vec{u}
> 
> Visualización:
>       \vec{u}
>      /|
>     / | \vec{u}-\vec{v}
>    /  |
>   /   |
>  \vec{v}----+
> 
> Construcción:
> - Colocar origen de \vec{u} y \vec{v} en mismo punto
> - \vec{u} - \vec{v} va de punta de \vec{v} a punta de \vec{u}
> 
> Ejemplo en ℝ²:
> \vec{u} = (5, 3), \vec{v} = (2, 1)
> \vec{u} - \vec{v} = (3, 2)
> 
> Vector de (2,1) a (5,3) es efectivamente (3,2)
> ```

## 🧩 Ejemplos de Verificación de Axiomas

> [!example] Verificación Completa **Ejemplo 1: Matrices 2×2**
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

> [!important] Referencia Rápida
> 
> ```
> ╔═══════════════════════════════════════════════════════════════╗
> ║                   AXIOMAS DE ESPACIO VECTORIAL                ║
> ╠═══════════════════════════════════════════════════════════════╣
> ║ SUMA DE VECTORES                                              ║
> ╟───────────────────────────────────────────────────────────────╢
> ║ (A1) Cerradura       │ \vec{u} + \vec{v} ∈ V                            ║
> ║ (A2) Asociatividad   │ (\vec{u}+\vec{v})+\vec{w} = \vec{u}+(\vec{v}+\vec{w})                  ║
> ║ (A3) Neutro          │ ∃0⃗: \vec{v}+0⃗ = \vec{v}                         ║
> ║ (A4) Inverso         │ ∃(-\vec{v}): \vec{v}+(-\vec{v}) = 0⃗                   ║
> ║ (A5) Conmutatividad  │ \vec{u} + \vec{v} = \vec{v} + \vec{u}                       ║
> ╟───────────────────────────────────────────────────────────────╢
> ║ MULTIPLICACIÓN POR ESCALAR                                    ║
> ╟───────────────────────────────────────────────────────────────╢
> ║ (M1) Cerradura       │ α\vec{v} ∈ V                                ║
> ║ (M2) Distributiva I  │ α(\vec{u}+\vec{v}) = α\vec{u}+α\vec{v}                      ║
> ║ (M3) Distributiva II │ (α+β)\vec{v} = α\vec{v}+β\vec{v}                      ║
> ║ (M4) Asociatividad   │ α(β\vec{v}) = (αβ)\vec{v}                        ║
> ║ (M5) Neutro          │ 1·\vec{v} = \vec{v}                              ║
> ╚═══════════════════════════════════════════════════════════════╝
> 
> PROPIEDADES DERIVADAS:
> • 0·\vec{v} = 0⃗
> • α·0⃗ = 0⃗
> • (-1)\vec{v} = -\vec{v}
> • -(\vec{u}+\vec{v}) = -\vec{u} + (-\vec{v})
> • -(-\vec{v}) = \vec{v}
> • α\vec{v} = 0⃗ ⟹ α=0 o \vec{v}=0⃗
> • Unicidad de 0⃗ y -\vec{v}
> ```

## ⚠️ Errores Comunes

> [!warning] Malentendidos Frecuentes **1. "Conmutatividad en multiplicación por escalar"**
> 
> ```
> ✗ FALSO: \vec{v}α ≠ α\vec{v} en general
> 
> La multiplicación por escalar es EXTERNA:
> F × V → V
> 
> α\vec{v} está definido (escalar × vector)
> \vec{v}α NO está definido (vector × escalar)
> 
> Notación: SIEMPRE α\vec{v} (escalar primero)
> 
> Excepción: En algunos contextos (física)
> se escribe \vec{v}α por conveniencia, pero
> se entiende como α\vec{v}
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
> • 0·\vec{v} = 0⃗ (producto → vector)
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
> \vec{u} - \vec{v} ≠ \vec{v} - \vec{u} en general
> 
> De hecho: \vec{u} - \vec{v} = -(\vec{v} - \vec{u})
> 
> Ejemplo:
> (5,0) - (2,0) = (3,0)
> (2,0) - (5,0) = (-3,0) ≠ (3,0)
> ```
> 
> **4. "α\vec{v} = 0⃗ implica α = 0"**
> 
> ```
> ✗ FALSO (incompleto)
> 
> Correcto: α\vec{v} = 0⃗ ⟹ α = 0 O \vec{v} = 0⃗
> 
> Contraejemplos:
> • 5·0⃗ = 0⃗ pero 5 ≠ 0
> • 0·\vec{v} = 0⃗ pero \vec{v} ≠ 0⃗ (si \vec{v} cualquiera)
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
> **7. "(-\vec{v}) significa 'negativo de \vec{v}'"**
> 
> ```
> ⚠️ CUIDADO con terminología
> 
> -\vec{v} es el "opuesto" o "inverso aditivo"
> 
> "Negativo" puede confundir:
> Si \vec{v} = (1,2), entonces -\vec{v} = (-1,-2)
> 
> Las componentes cambian de signo, pero
> conceptualmente es "el vector que sumado
> a \vec{v} da 0⃗"
> 
> Mejor: "opuesto de \vec{v}" o "menos \vec{v}"
> ```

## 🔗 Conexiones con Otros Temas

> [!quote] Enlaces Conceptuales **Fundamentos previos:**
> 
> - [[Álgebra abstracta]] - Grupos, anillos, campos
> - [[Teoría de conjuntos]] - Operaciones binarias
> - [[Lógica matemática]] - Axiomas y demostraciones
> 
> **Temas relacionados:**
> 
> - [[09 - Vectores en espacios vectoriales]] - Estructura general
> - [[01 - Subespacios Vectoriales]] - Herencia de operaciones
> - [[01 – Transformaciones lineales]] - Preservación de operaciones
> - [[01 – Producto interno]] - Operación adicional
> 
> **Aplicaciones posteriores:**
> 
> - [[Álgebra lineal numérica]] - Implementación computacional
> - [[Análisis funcional]] - Espacios infinito-dimensionales
> - [[Geometría diferencial]] - Espacios tangentes
> - [[Mecánica cuántica]] - Superposición de estados
> - [[Teoría de control]] - Sistemas lineales

## 📚 Recursos Adicionales

> [!note] Herramientas y Referencias **Software para manipulación:**
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

> [!tip] Lecturas Recomendadas **Nivel introductorio:**
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
