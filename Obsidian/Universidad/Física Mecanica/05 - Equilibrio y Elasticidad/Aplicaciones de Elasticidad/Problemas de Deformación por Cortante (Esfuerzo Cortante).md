# Problemas de Deformación por Cortante (Esfuerzo Cortante)

> [!quote] "El cortante es el arte sutil de la deformación: mientras la tensión estira y la compresión aprieta, el cortante desliza las capas del material como páginas de un libro que se hojea." ✂️

> [!info]- El esfuerzo cortante representa uno de los estados de carga más importantes en ingeniería, caracterizado por fuerzas que actúan paralelas a las superficies del material. A diferencia de los esfuerzos normales (tensión/compresión), el cortante produce deformaciones angulares y deslizamientos entre capas del material.

## 🔄 Fundamentos Teóricos

> [!info]- **Esfuerzo Cortante Básico** ⚡
> 
> ### Definición Fundamental:
> 
> **τ = V/A**
> 
> - **τ** (tau): Esfuerzo cortante (Pa o N/m²)
> - **V**: Fuerza cortante aplicada (N)
> - **A**: Área sobre la cual actúa el esfuerzo (m²)
> 
> ### Características del Cortante:
> 
> |Aspecto|Descripción|Unidades SI|
> |---|---|---|
> |Dirección|Paralelo a la superficie|N/m² (Pa)|
> |Deformación|Angular (γ = tan θ)|radianes|
> |Distribución|Variable según geometría|Pa|
> |Complementariedad|τxy = τyx|Pa|

> [!tip]- **Ley de Hooke para Cortante** 🔧
> 
> ### Relación Esfuerzo-Deformación:
> 
> **τ = G × γ**
> 
> - **G**: Módulo de rigidez o cortante (Pa)
> - **γ**: Deformación angular o cortante (rad)
> - **θ**: Ángulo de distorsión (pequeños ángulos: γ ≈ tan θ ≈ θ)
> 
> ### Relación con Otras Constantes Elásticas:
> 
> **G = E / [2(1 + ν)]**
> 
> - **E**: Módulo de Young
> - **ν**: Coeficiente de Poisson
> 
> ### Interpretación Geométrica:
> 
> - **γ = Δx/h**: Distorsión relativa
> - **Δx**: Desplazamiento horizontal
> - **h**: Altura del elemento

> [!warning]- **Tipos de Esfuerzo Cortante** ⚔️
> 
> ### Clasificación por Origen:
> 
> **1. Cortante Directo**:
> 
> - Provocado por fuerzas paralelas
> - Distribución uniforme (idealizada)
> - Ejemplos: pernos, remaches, soldaduras
> 
> **2. Cortante por Torsión**:
> 
> - Debido a momentos torsores
> - Distribución variable (máximo en perímetro)
> - Fórmula: τ = Tr/J
> 
> **3. Cortante por Flexión**:
> 
> - Acompaña a esfuerzos normales en vigas
> - Distribución parabólica típica
> - Fórmula: τ = VQ/(Ib)
> 
> ### Estados de Cortante:
> 
> - **Cortante puro**: Solo esfuerzos cortantes
> - **Cortante combinado**: Con esfuerzos normales
> - **Cortante máximo**: τmax = (σ1 - σ3)/2

> [!success] 🔗 Distribución de Esfuerzos Cortantes
> 
> ```mermaid
> graph TD
>     A[Cortante Directo] --> B[Distribución Uniforme]
>     A --> C[τ = V/A]
>     
>     D[Cortante por Torsión] --> E[Distribución Lineal]
>     D --> F[τmax = Tr/J en r = R]
>     
>     G[Cortante por Flexión] --> H[Distribución Parabólica]
>     G --> I[τmax en fibra neutra]
>     
>     style A fill:#e1f5fe
>     style D fill:#f3e5f5
>     style G fill:#fff3e0
> ```

> [!note]- **Propiedades de Materiales en Cortante** 📊
> 
> ### Módulos de Rigidez Típicos (G):
> 
> |Material|Módulo G (GPa)|Relación G/E|
> |---|---|---|
> |Acero estructural|80-85|≈ 0.40|
> |Aluminio|26-28|≈ 0.38|
> |Cobre|45-50|≈ 0.42|
> |Concreto|8-15|≈ 0.40|
> |Madera (paralela)|0.5-1.5|≈ 0.08|
> |Caucho|0.0003-0.003|≈ 0.33|
> 
> ### Esfuerzos Cortantes Admisibles:
> 
> |Material|τ_admisible (MPa)|Factor típico|
> |---|---|---|
> |Acero A36|140-170|≈ 0.6 × σy|
> |Aluminio 6061|85-110|≈ 0.6 × σy|
> |Madera (pino)|7-12|Variable|
> |Soldadura|110-140|≈ 0.6 × σy base|

## 🎯 Estrategias de Resolución

> [!tip]- **Método CORTA (Carga-Orientación-Rigidez-Tensión-Análisis)** 🧠
> 
> ### **C**arga - Identifica las fuerzas
> 
> 1. Localiza fuerzas cortantes aplicadas
> 2. Determina la dirección de actuación
> 3. Calcula la magnitud resultante
> 4. Identifica puntos críticos
> 
> ### **O**rientación - Analiza la geometría
> 
> 5. Define el plano de cortante
> 6. Identifica áreas efectivas
> 7. Considera la distribución del esfuerzo
> 8. Evalúa restricciones geométricas
> 
> ### **R**igidez - Propiedades del material
> 
> 9. Determina el módulo G
> 10. Considera factores de temperatura
> 11. Evalúa efectos de fatiga
> 12. Aplica factores de seguridad
> 
> ### **T**ensión - Calcula esfuerzos
> 
> 13. Aplica τ = V/A para cortante directo
> 14. Usa τ = Tr/J para torsión
> 15. Emplea τ = VQ/(Ib) para flexión
> 16. Verifica esfuerzos admisibles
> 
> ### **A**nálisis - Interpreta resultados
> 
> 17. Calcula deformaciones: γ = τ/G
> 18. Evalúa desplazamientos
> 19. Verifica criterios de diseño
> 20. Considera interacción con otros esfuerzos

## 📚 Problemas Tipo

> [!example]- **Problema 1: Cortante Directo en Perno** 🔩
> 
> ### Enunciado:
> 
> Un perno de diámetro 12 mm conecta dos placas de acero sometidas a una fuerza de tracción de 18 kN. El perno está sometido a cortante simple. Si G = 80 GPa y τ_admisible = 120 MPa, determina: a) El esfuerzo cortante actual b) El factor de seguridad c) La deformación angular
> 
> ### Solución:
> 
> **Datos dados**:
> 
> - d = 12 mm → A = π(6)² = 113.1 mm²
> - V = 18 kN = 18,000 N
> - G = 80 GPa = 80,000 MPa
> - τ_admisible = 120 MPa
> 
> **a) Esfuerzo cortante actual**:
> 
> - τ = V/A = 18,000 N / 113.1 mm² = 159.1 MPa
> 
> **b) Factor de seguridad**:
> 
> - FS = τ_admisible / τ_actual = 120 MPa / 159.1 MPa = 0.75
> - **¡PELIGRO! FS < 1** → El perno fallará
> 
> **c) Deformación angular**:
> 
> - γ = τ/G = 159.1 MPa / 80,000 MPa = 1.99 × 10⁻³ rad
> - θ = γ = 0.114° (ángulo muy pequeño)

> [!example]- **Problema 2: Torsión en Eje Circular** 🌀
> 
> ### Enunciado:
> 
> Un eje circular sólido de 50 mm de diámetro y 2 m de longitud transmite un torque de 3 kN·m. Si G = 85 GPa, determina: a) El esfuerzo cortante máximo b) El ángulo de torsión total c) El diámetro mínimo para τ_admisible = 80 MPa
> 
> ### Solución:
> 
> **Datos dados**:
> 
> - d = 50 mm → R = 25 mm
> - L = 2 m = 2000 mm
> - T = 3 kN·m = 3×10⁶ N·mm
> - G = 85 GPa = 85,000 MPa
> 
> **a) Esfuerzo cortante máximo**:
> 
> - J = πd⁴/32 = π(50)⁴/32 = 613,592 mm⁴
> - τmax = TR/J = (3×10⁶ × 25)/613,592 = 122.1 MPa
> 
> **b) Ángulo de torsión total**:
> 
> - φ = TL/(GJ) = (3×10⁶ × 2000)/(85,000 × 613,592)
> - φ = 0.115 rad = 6.58°
> 
> **c) Diámetro mínimo**:
> 
> - J_min = TR/τ_admisible = (3×10⁶ × 25)/80 = 937,500 mm⁴
> - d_min⁴ = 32J_min/π = 9,549,297 mm⁴
> - d_min = 55.4 mm

> [!example]- **Problema 3: Cortante en Viga (Flexión)** 📏
> 
> ### Enunciado:
> 
> Una viga de sección rectangular (200 mm × 300 mm, h × b) soporta una fuerza cortante de 150 kN. Determina: a) El esfuerzo cortante máximo b) La distribución del esfuerzo c) La relación τmax/τpromedio
> 
> ### Solución:
> 
> **Datos**:
> 
> - b = 200 mm, h = 300 mm
> - V = 150 kN = 150,000 N
> - I = bh³/12 = 200(300)³/12 = 450×10⁶ mm⁴
> 
> **a) Esfuerzo cortante máximo (en fibra neutra)**:
> 
> - Q = (b × h/2) × (h/4) = (200 × 150) × 75 = 2.25×10⁶ mm³
> - τmax = VQ/(Ib) = (150,000 × 2.25×10⁶)/(450×10⁶ × 200)
> - τmax = 3.75 MPa
> 
> **b) Distribución parabólica**:
> 
> - τ(y) = (V/Ib) × [bh²/8 - by²/2]
> - En bordes (y = ±h/2): τ = 0
> - En centro (y = 0): τ = τmax = 3.75 MPa
> 
> **c) Relación con esfuerzo promedio**:
> 
> - τpromedio = V/A = 150,000/(200×300) = 2.5 MPa
> - τmax/τpromedio = 3.75/2.5 = 1.5

## 🧮 Técnicas de Memorización

> [!tip]- **Mnemotecnia: "GATO"** 🐱
> 
> **G**amma es deformación angular (**G** × γ = τ) **A**rea en denominador (τ = V/**A**) **T**au es cortante (**T**orque genera τ) **O**rtogonal a la normal (esfuerzo **O**blicuo)

> [!info]- **Reglas Nemotécnicas Adicionales** 🎯
> 
> ### "PARA-TOR": **PARA**lelo al área, **TOR**que causa cortante
> 
> - Fuerza **paralela** a superficie → Cortante
> - **Torque** en eje → Cortante máximo en perímetro
> 
> ### "FLEX-MAX": **FLEX**ión tiene **MAX**imo en centro
> 
> - Cortante por flexión → τmax en fibra neutra
> - Distribución parabólica en secciones rectangulares
> 
> ### "G-MENOR": **G** siempre **MENOR** que **E**
> 
> - G ≈ 0.4E para metales
> - G = E/[2(1+ν)] → Siempre G < E

## ⚠️ Errores Comunes

> [!warning]- **Confusiones Frecuentes** ⚠️
> 
> 1. **Confundir esfuerzo cortante con normal**: τ ⊥ σ siempre
> 2. **Usar área incorrecta**: Área perpendicular vs paralela a fuerza
> 3. **Olvidar la complementariedad**: τxy = τyx en cortante puro
> 4. **Asumir distribución uniforme**: Solo válida en cortante directo idealizado
> 5. **Confundir G con E**: Módulos diferentes para diferentes deformaciones
> 6. **Ignorar concentraciones de esfuerzo**: En cambios de sección o agujeros
> 7. **Mal aplicar fórmulas de torsión**: Solo válidas para secciones circulares
> 8. **Deformación angular vs lineal**: γ (radianes) vs ε (adimensional)

## 🎯 Aplicaciones Prácticas

> [!info]- **Ejemplos del Mundo Real** 🌍
> 
> ### Elementos de Sujeción:
> 
> - Pernos y remaches en estructuras
> - Soldaduras bajo cargas cortantes
> - Pasadores en conexiones articuladas
> - Chavetas en ejes y poleas
> 
> ### Sistemas de Transmisión:
> 
> - Ejes de transmisión automotrices
> - Árboles de turbinas y motores
> - Sistemas de engranajes
> - Acoplamientos flexibles
> 
> ### Estructuras:
> 
> - Vigas sometidas a cargas transversales
> - Columnas bajo cargas excéntricas
> - Placas bajo cargas en el plano
> - Elementos de cortante en edificios sismorresistentes
> 
> ### Geotecnia:
> 
> - Resistencia al cortante de suelos
> - Estabilidad de taludes
> - Cimentaciones superficiales
> - Muros de contención

## 📈 Casos Especiales

> [!note]- **Situaciones Complejas** 🔬
> 
> ### Secciones No Circulares en Torsión:
> 
> - **Sección rectangular**: τmax = T/(αab²)
> - **Sección elíptica**: Análisis más complejo
> - **Perfiles abiertos**: Concentración en extremos
> - **Sección hueca**: Distribución en pared delgada
> 
> ### Cortante Combinado:
> 
> - **Con tensión/compresión**: Círculo de Mohr
> - **Estado biaxial**: τmax = (σ1-σ2)/2
> - **Criterios de falla**: Von Mises, Tresca
> - **Fatiga por cortante**: Amplitud alternante
> 
> ### Efectos Dinámicos:
> 
> - **Carga de impacto**: Factor de amplificación
> - **Resonancia torsional**: Frecuencias críticas
> - **Pandeo por cortante**: En placas delgadas
> - **Cortante sísmico**: Estructuras bajo sismo
> 
> ### Materiales Especiales:
> 
> - **Materiales compuestos**: Matriz vs fibra
> - **Anisotropía**: Propiedades direccionales
> - **Viscoelasticidad**: Dependencia temporal
> - **Plasticidad**: Más allá del límite elástico

## 🔬 Métodos de Análisis Avanzados

> [!tip]- **Técnicas Especializadas** 🎓
> 
> ### Análisis por Elementos Finitos:
> 
> - Distribución real de esfuerzos
> - Concentraciones en geometrías complejas
> - Interacción multifísica
> 
> ### Teoría de Torsión:
> 
> - Función de alabeo (warping)
> - Torsión restringida vs libre
> - Perfiles abiertos vs cerrados
> 
> ### Métodos Experimentales:
> 
> - Galgas extensométricas a 45°
> - Fotoelasticidad
> - Interferometría holográfica

## 📖 Referencias

> [!quote]- **Notas Relacionadas**
> 
> - [[Elasticidad]] - Fundamentos de deformación
> - [[Torque y Equilibrio Rotacional]] - Base para torsión
> - [[Segunda ley de Newton para Rotación]] - Conceptos de momento
> - [[Aplicaciones de Equilibrio]] - Análisis de fuerzas

## 📚 Notas Recomendadas

> [!note]- **Prerrequisitos**
> 
> - [[Problemas de Deformación por tensión y compresión (Ley de Hooke)]] - Conceptos base
> - [[Vectores]] - Para análisis de esfuerzos en 3D
> - [[Equilibrio]] - Balance de fuerzas y momentos
> - [[Fuerzas y Diagramas de Cuerpo Libre]] - Identificación de cargas

---

**Tags:** #elasticidad #esfuerzo-cortante #deformacion-angular #torsion #cortante-directo #modulo-rigidez #cortante-flexion #materiales #resistencia-materiales #ingenieria-mecanica