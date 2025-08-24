# Problemas de Deformación por Tensión y Compresión (Ley de Hooke)

> [!quote] "Los materiales nos susurran sus secretos a través de sus deformaciones; la Ley de Hooke es nuestro intérprete para entender su lenguaje silencioso." 🔧

> [!info]- La Ley de Hooke es uno de los principios fundamentales de la mecánica de materiales y la elasticidad. Describe la relación lineal entre la fuerza aplicada a un material elástico y su deformación resultante, siendo esencial para el análisis estructural y el diseño de elementos mecánicos.

## 🏗️ Fundamentos Teóricos

> [!info]- **Ley de Hooke Básica** 🔩
> 
> ### Formulación Original:
> 
> **F = k × Δx**
> 
> - **F**: Fuerza aplicada (N)
> - **k**: Constante elástica del material (N/m)
> - **Δx**: Deformación o elongación (m)
> 
> ### Interpretación Física:
> 
> |Parámetro|Significado|Unidades SI|
> |---|---|---|
> |Fuerza (F)|Magnitud de la carga aplicada|Newton (N)|
> |Constante k|Rigidez del material|N/m|
> |Deformación (Δx)|Cambio de longitud|metros (m)|
> |Tensión (σ)|Fuerza por unidad de área|Pa (N/m²)|
> |Deformación unitaria (ε)|Cambio relativo de longitud|Adimensional|

> [!tip]- **Ley de Hooke para Materiales** 🧪
> 
> ### Formulación en Términos de Esfuerzo y Deformación:
> 
> **σ = E × ε**
> 
> - **σ = F/A**: Esfuerzo o tensión (Pa)
> - **E**: Módulo de Young (Pa)
> - **ε = ΔL/L₀**: Deformación unitaria
> 
> ### Relaciones Derivadas:
> 
> - **ΔL = (F × L₀)/(A × E)**: Cambio de longitud
> - **F = (A × E × ΔL)/L₀**: Fuerza necesaria
> - **k = (A × E)/L₀**: Constante elástica del elemento
> 
> ### Interpretación:
> 
> - **Tensión**: σ > 0 (material estirado)
> - **Compresión**: σ < 0 (material comprimido)
> - **Límite elástico**: Máximo esfuerzo sin deformación permanente
> - **Zona plástica**: Deformación permanente tras límite elástico

> [!warning]- **Tipos de Deformación** ⚡
> 
> ### Clasificación por Naturaleza:
> 
> **1. Deformación Elástica**:
> 
> - Reversible al retirar la carga
> - Sigue la Ley de Hooke
> - No hay daño estructural
> 
> **2. Deformación Plástica**:
> 
> - Irreversible
> - Excede el límite elástico
> - Cambio permanente en el material
> 
> ### Clasificación por Tipo de Carga:
> 
> - **Tracción**: Fuerzas que alejan las secciones
> - **Compresión**: Fuerzas que acercan las secciones
> - **Flexión**: Combinación de tracción y compresión
> - **Torsión**: Fuerzas de giro (requiere módulo de rigidez G)

> [!success] 🔗 Diagrama Esfuerzo-Deformación
> 
> ```mermaid
> graph LR
>     A[Zona Elástica] -->|Límite de Proporcionalidad| B[Zona de Fluencia]
>     B -->|Límite Elástico| C[Zona Plástica]
>     C -->|Esfuerzo Máximo| D[Zona de Fractura]
>     
>     A --> E[Ley de Hooke σ = E·ε]
>     B --> F[Inicio de deformación permanente]
>     C --> G[Deformación irreversible]
>     D --> H[Ruptura del material]
>     
>     style A fill:#e8f5e8
>     style B fill:#fff3cd
>     style C fill:#f8d7da
>     style D fill:#d1ecf1
> ```

> [!note]- **Propiedades Mecánicas Importantes** 📊
> 
> ### Módulos Elásticos Típicos:
> 
> |Material|Módulo de Young (GPa)|Límite Elástico (MPa)|
> |---|---|---|
> |Acero estructural|200-210|250-400|
> |Aluminio|70|70-300|
> |Concreto|20-40|3-5 (compresión)|
> |Madera (pino)|10-15|30-50|
> |Cobre|110|70-200|
> |Titanio|110-120|240-550|
> 
> ### Coeficientes de Poisson (ν):
> 
> - **Acero**: 0.27-0.30
> - **Aluminio**: 0.33
> - **Concreto**: 0.20
> - **Caucho**: ≈ 0.50

## 🎯 Estrategias de Resolución

> [!tip]- **Método DEMAT (Datos-Esfuerzo-Material-Análisis-Total)** 🧠
> 
> ### **D**atos - Identifica la información
> 
> 1. Dimensiones del elemento (L₀, A)
> 2. Propiedades del material (E, σ_y)
> 3. Cargas aplicadas (F)
> 4. Condiciones de apoyo
> 
> ### **E**sfuerzo - Calcula tensiones
> 
> 5. Determina el tipo de carga
> 6. Calcula el esfuerzo: σ = F/A
> 7. Verifica si está en zona elástica
> 
> ### **M**aterial - Propiedades mecánicas
> 
> 8. Identifica el módulo de Young
> 9. Considera factores de seguridad
> 10. Verifica limitaciones del material
> 
> ### **A**nálisis - Aplicar Ley de Hooke
> 
> 11. Calcula deformación unitaria: ε = σ/E
> 12. Determina cambio total: ΔL = ε × L₀
> 13. Analiza si cumple especificaciones
> 
> ### **T**otal - Interpretación integral
> 
> 14. Verifica coherencia física
> 15. Considera efectos secundarios
> 16. Evalúa implicaciones de diseño

## 📚 Problemas Tipo

> [!example]- **Problema 1: Deformación por Tracción** 🏗️
> 
> ### Enunciado:
> 
> Una barra de acero de 2 metros de longitud y sección transversal circular de 20 mm de diámetro se somete a una fuerza de tracción de 50 kN. Si E = 200 GPa, determina: a) El esfuerzo en la barra b) La deformación unitaria c) El alargamiento total
> 
> ### Solución:
> 
> **Datos dados**:
> 
> - L₀ = 2 m = 2000 mm
> - d = 20 mm → r = 10 mm
> - F = 50 kN = 50,000 N
> - E = 200 GPa = 200,000 MPa
> 
> **a) Esfuerzo**:
> 
> - A = πr² = π(10)² = 314.16 mm²
> - σ = F/A = 50,000 N / 314.16 mm² = 159.15 MPa
> 
> **b) Deformación unitaria**:
> 
> - ε = σ/E = 159.15 MPa / 200,000 MPa = 7.96 × 10⁻⁴
> 
> **c) Alargamiento total**:
> 
> - ΔL = ε × L₀ = 7.96 × 10⁻⁴ × 2000 mm = 1.59 mm

> [!example]- **Problema 2: Sistema de Barras en Serie** 🔗
> 
> ### Enunciado:
> 
> Dos barras están conectadas en serie: la primera de acero (E₁ = 200 GPa, L₁ = 1 m, A₁ = 400 mm²) y la segunda de aluminio (E₂ = 70 GPa, L₂ = 0.5 m, A₂ = 600 mm²). Se aplica una fuerza de 80 kN. Calcula la deformación total del sistema.
> 
> ### Solución:
> 
> **Para sistemas en serie, la fuerza es la misma en ambas barras**:
> 
> **Barra de acero**:
> 
> - σ₁ = F/A₁ = 80,000 N / 400 mm² = 200 MPa
> - ε₁ = σ₁/E₁ = 200 MPa / 200,000 MPa = 1.0 × 10⁻³
> - ΔL₁ = ε₁ × L₁ = 1.0 × 10⁻³ × 1000 mm = 1.0 mm
> 
> **Barra de aluminio**:
> 
> - σ₂ = F/A₂ = 80,000 N / 600 mm² = 133.33 MPa
> - ε₂ = σ₂/E₂ = 133.33 MPa / 70,000 MPa = 1.905 × 10⁻³
> - ΔL₂ = ε₂ × L₂ = 1.905 × 10⁻³ × 500 mm = 0.95 mm
> 
> **Deformación total**: ΔL_total = ΔL₁ + ΔL₂ = 1.0 + 0.95 = 1.95 mm

> [!example]- **Problema 3: Compresión con Factor de Seguridad** 🛡️
> 
> ### Enunciado:
> 
> Una columna de concreto de 3 m de altura y sección cuadrada de 300×300 mm soporta una carga de compresión. Si E = 25 GPa, σ_admisible = 8 MPa, y se requiere un factor de seguridad de 3, determina: a) La carga máxima permisible b) El acortamiento bajo carga máxima
> 
> ### Solución:
> 
> **Datos**:
> 
> - L₀ = 3 m = 3000 mm
> - A = 300 × 300 = 90,000 mm²
> - E = 25 GPa = 25,000 MPa
> - σ_admisible = 8 MPa, FS = 3
> 
> **a) Carga máxima permisible**:
> 
> - σ_trabajo = σ_admisible / FS = 8 MPa / 3 = 2.67 MPa
> - F_max = σ_trabajo × A = 2.67 MPa × 90,000 mm² = 240,000 N = 240 kN
> 
> **b) Acortamiento**:
> 
> - ε = σ_trabajo/E = 2.67 MPa / 25,000 MPa = 1.067 × 10⁻⁴
> - ΔL = ε × L₀ = 1.067 × 10⁻⁴ × 3000 mm = 0.32 mm

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "FEAL"** 🦅
> 
> **F**uerza dividida por **E**l **A**rea da tensión (**L**ey fundamental)
> 
> - **F**/A = σ (esfuerzo)
> - **E** × ε = σ (Ley de Hooke)
> - **A**largamiento = ε × L₀
> - **L**ímite elástico no superar

> [!info]- **Reglas Nemotécnicas Adicionales** 🎯
> 
> ### "TED-AC": **T**ensión **E**s **D**irecta, **A**largamiento es **C**onsecuencia
> 
> - Mayor tensión → Mayor deformación
> - Tracción → Alargamiento (+)
> - Compresión → Acortamiento (-)
> 
> ### "MEGA": **M**ódulo **E**s **G**rande, **A**largamiento pequeño
> 
> - E alto → Material rígido → Poca deformación
> - E bajo → Material flexible → Mucha deformación

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir esfuerzo con fuerza**: σ ≠ F (σ = F/A)
> 2. **Usar unidades inconsistentes**: Mezclar mm, m, MPa, Pa
> 3. **Olvidar el signo**: Compresión = negativo, Tracción = positivo
> 4. **Superar límite elástico**: Verificar σ < σ_y siempre
> 5. **Ignorar concentración de esfuerzos**: En cambios de sección
> 6. **Factor de seguridad mal aplicado**: FS en esfuerzo, no en carga directamente
> 7. **Confundir deformación total con unitaria**: ΔL vs ε

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Construcción:
> 
> - Diseño de columnas y vigas en edificios
> - Cálculo de cables en puentes colgantes
> - Análisis de cimentaciones bajo carga
> - Dimensionamiento de elementos de acero
> 
> ### Ingeniería Mecánica:
> 
> - Diseño de ejes y árboles de transmisión
> - Análisis de resortes y elementos elásticos
> - Cálculo de pernos y elementos de sujeción
> - Diseño de recipientes a presión
> 
> ### Aeronáutica:
> 
> - Análisis estructural de fuselajes
> - Diseño de alas y superficies de control
> - Cálculo de elementos sometidos a fatiga
> - Optimización peso-resistencia
> 
> ### Ingeniería Biomédica:
> 
> - Diseño de implantes y prótesis
> - Análisis de huesos bajo carga
> - Desarrollo de materiales biocompatibles
> - Estudios de biomecánica

## 📈 Casos Especiales

> [!note]- **Situaciones Complejas** 🔬
> 
> ### Carga Variable:
> 
> - **Carga triangular**: σ(x) = σ₀(x/L)
> - **Carga distribuida**: Integración por secciones
> - **Impacto dinámico**: Factor de amplificación
> 
> ### Efectos Térmicos:
> 
> - **Dilatación térmica**: ΔL = α·L₀·ΔT
> - **Esfuerzos térmicos**: σ = E·α·ΔT (restricción)
> - **Combinación carga-temperatura**
> 
> ### Materiales Compuestos:
> 
> - **Regla de mezclas**: E_c = E_f·V_f + E_m·V_m
> - **Análisis micromecánico**
> - **Criterios de falla específicos**

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Elasticidad]] - Fundamentos teóricos generales
> - [[Equilibrio]] - Análisis de fuerzas y momentos
> - [[Fundamentos de Física Mecánica]] - Base matemática
> - [[Aplicaciones de Equilibrio]] - Casos prácticos

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Vectores]] - Para análisis de fuerzas en 3D
> - [[Unidades y Magnitudes Físicas]] - Sistema de unidades
> - [[Conocimientos Previos a las Prácticas]] - Conceptos básicos
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Análisis de cargas

---

**Tags:** #elasticidad #ley-de-hooke #deformacion #tension #compresion #modulo-young #esfuerzo #materiales #resistencia-materiales #ingenieria-estructural