---
dg-publish: true
---

# Presión Manométrica

>[!quote] *"En el mundo de la ingeniería y la física aplicada, no medimos la presión absoluta que incluye el peso invisible de toda la atmósfera. Medimos la diferencia, la presión que excede lo normal, la presión manométrica: el verdadero indicador de las fuerzas adicionales que actúan en nuestros sistemas."*
>
> [!info]+ Definición Fundamental 📏
> La **presión manométrica** (P_man) es la **diferencia entre la presión absoluta en un punto y la presión atmosférica local**. Es la presión que miden la mayoría de instrumentos de medición como manómetros, ya que toman como referencia la presión atmosférica.
> 
> **P_manométrica = P_absoluta - P_atmosférica**
> 
> **P_man = P_abs - P_atm**
> 
> Donde:
> - P_man = Presión manométrica
> - P_abs = Presión absoluta total
> - P_atm = Presión atmosférica (≈ 101,325 Pa al nivel del mar)
>
> [!note] Fundamento Teórico y Tipos de Presión 📊
> ### Clasificación de Presiones
> ```mermaid
> graph TB
>     A[Presión Absoluta<br/>P_abs = P_atm + P_man] --> B[Presión Atmosférica<br/>P_atm ≈ 101.325 kPa]
>     A --> C[Presión Manométrica<br/>P_man = P_abs - P_atm]
>     D[Casos Especiales] --> E[P_man > 0<br/>Presión Positiva<br/>Sobrepresión]
>     D --> F[P_man = 0<br/>Presión Atmosférica<br/>Sin diferencia]
>     D --> G[P_man < 0<br/>Presión Negativa<br/>Vacío Parcial]
>     H[Referencia] --> I[Vacío Absoluto<br/>P = 0 Pa<br/>Referencia teórica]
>     H --> J[Nivel del Mar<br/>P_atm = 1 atm<br/>Referencia práctica]
>     style A fill:#e8f5e8
>     style B fill:#e1f5fe
>     style C fill:#fff3e0
>     style E fill:#ffcdd2
>     style F fill:#f3e5f5
>     style G fill:#e0f2f1
> ```
> 
> ### Relaciones Fundamentales
> - **P_abs = P_atm + P_man** (cuando P_man > 0)
> - **P_abs = P_atm - |P_man|** (cuando P_man < 0, vacío)
> - **P_man = 0** significa que la presión es igual a la atmosférica
>
> [!tip] Instrumentos de Medición 🔬
> ### Tipos de Manómetros
> | Tipo | Principio | Aplicación | Rango Típico |
> |------|-----------|------------|--------------|
> | 📏 **Manómetro en U** | Altura de columna líquida | Laboratorio, precisión | 0-200 kPa |
> | ⚙️ **Manómetro Bourdon** | Deformación de tubo curvo | Industrial, robustez | 0-100 MPa |
> | 💎 **Piezoeléctrico** | Deformación cristalina | Alta precisión, dinámico | 0-1000 MPa |
> | 🌡️ **Digital** | Sensores electrónicos | Versatilidad, registro | Variable |
> 
> ### Manómetro en U - Principio
> ```mermaid
> graph TB
>     A[Recipiente con Gas<br/>Presión P_gas] --> B[Tubo en U<br/>con Mercurio]
>     B --> C[Rama Abierta<br/>Presión Atmosférica]
>     B --> D[Diferencia de Altura h]
>     E[Equilibrio de Presiones] --> F[P_gas = P_atm + ρ_Hg × g × h]
>     F --> G[P_manométrica = ρ_Hg × g × h]
>     style A fill:#fff3e0
>     style B fill:#e1f5fe
>     style C fill:#f3e5f5
>     style E fill:#e8f5e8
>     style G fill:#ffcdd2
> ```
>
> [!example] Cálculos y Ejemplos Prácticos 🧮
> ### Ejemplo 1: Manómetro en U con Mercurio
> **Problema:** Un manómetro en U conectado a un tanque muestra una diferencia de altura de mercurio de 25 cm. ¿Cuál es la presión manométrica del gas?
> 
> **Datos:**
> - h = 25 cm = 0.25 m
> - ρ_Hg = 13,600 kg/m³
> - g = 9.8 m/s²
> 
> **Solución:**
> ```
> P_manométrica = ρ_Hg × g × h
> P_man = 13,600 × 9.8 × 0.25 = 33,320 Pa = 33.32 kPa
> ```
> 
> **Resultado:** La presión manométrica es 33.32 kPa por encima de la atmosférica
> 
> ### Ejemplo 2: Presión en un Tanque
> **Problema:** Un manómetro en un tanque marca 2.5 bar. ¿Cuál es la presión absoluta si estamos al nivel del mar?
> 
> **Datos:**
> - P_man = 2.5 bar = 250 kPa
> - P_atm = 101.325 kPa (nivel del mar)
> 
> **Solución:**
> ```
> P_absoluta = P_atmosférica + P_manométrica
> P_abs = 101.325 + 250 = 351.325 kPa = 3.51 bar
> ```
> 
> ### Ejemplo 3: Vacío Parcial
> **Problema:** Un vacuómetro indica -30 kPa. ¿Cuál es la presión absoluta?
> 
> **Solución:**
> ```
> P_absoluta = P_atmosférica + P_manométrica
> P_abs = 101.325 + (-30) = 71.325 kPa
> 
> Porcentaje de vacío = |P_man|/P_atm × 100% = 30/101.325 × 100% = 29.6%
> ```
>
> [!abstract] Aplicaciones Prácticas 🏗️
> ### En Sistemas de Fluidos
> - **🚰 Sistemas de agua potable**: Control de presión en tuberías
> - **🔥 Calderas industriales**: Monitoreo de presión de vapor
> - **🚗 Neumáticos**: Presión de inflado (siempre manométrica)
> - **💨 Sistemas neumáticos**: Control de aire comprimido
> 
> ### En Procesos Industriales
> ```mermaid
> mindmap
>   root((Aplicaciones))
>     Petroquímica
>       Reactores a presión
>       Destilación
>       Transporte por ductos
>     Manufactura
>       Prensas hidráulicas
>       Moldeado por inyección
>       Control de calidad
>     Medicina
>       Respiradores artificiales
>       Cámaras hiperbáricas
>       Equipos de diálisis
>     Alimentaria
>       Esterilización
>       Envasado al vacío
>       Procesamiento HPP
> ```
> 
> ### Ventajas de la Medición Manométrica
> - **📏 Referencia práctica**: Elimina variaciones atmosféricas normales
> - **🔧 Simplicidad instrumental**: Manómetros más simples y económicos
> - **📊 Relevancia operacional**: Mide la presión "útil" del sistema
> - **⚖️ Comparación directa**: Fácil interpretación para operadores
>
> [!warning] Consideraciones y Limitaciones ⚠️
> ### Factores que Afectan la Medición
> - **🏔️ Altitud**: P_atm varía con la elevación (≈ -12 Pa/m)
> - **🌡️ Temperatura**: Afecta la densidad del fluido manométrico
> - **☁️ Condiciones meteorológicas**: Variaciones de presión atmosférica
> - **📐 Orientación**: Manómetros deben estar correctamente nivelados
> 
> ### Errores Comunes
> - **🔄 Confundir presión manométrica con absoluta**
> - **📍 No considerar la altitud del lugar**
> - **🌡️ Ignorar efectos de temperatura en el instrumento**
> - **⏱️ No calibrar periódicamente los instrumentos**
> 
> ### Precauciones de Seguridad
> - **💥 Sobrepresión**: Puede dañar equipos o causar accidentes
> - **🌪️ Vacío excesivo**: Puede colapsar recipientes no diseñados
> - **🔧 Mantenimiento**: Instrumentos requieren calibración regular
>
> [!summary]+ Fórmulas y Conversiones Clave 📊
> ### Ecuaciones Fundamentales
> ```
> Presión Manométrica:    P_man = P_abs - P_atm
> Presión Absoluta:       P_abs = P_atm + P_man
> Manómetro en U:         P_man = ρ_fluido × g × h
> Vacío Relativo:         Vacío% = |P_man|/P_atm × 100%
> ```
> 
> ### Conversiones Útiles
> ```
> 1 bar = 100 kPa = 0.1 MPa
> 1 atm = 101.325 kPa = 1.01325 bar
> 1 psi = 6.895 kPa
> 1 mmHg = 133.322 Pa
> 1 mH₂O = 9.807 kPa
> ```
> 
> ### Para Manómetros Líquidos
> ```
> Mercurio:    P_man = 133,322 × h_mm Pa
> Agua:        P_man = 9,807 × h_m Pa
> Aceite:      P_man = ρ_aceite × 9.8 × h Pa
> ```
>
> [!brain]+ Técnica de Memorización: MANÓMETRO 🧠
> **M** - Mide diferencia con atmósfera
> **A** - Atmosférica es la referencia
> **N** - Negativa indica vacío parcial
> **Ó** - Óptima para aplicaciones prácticas
> **M** - Mayor que cero es sobrepresión
> **E** - Elimina variaciones atmosféricas
> **T** - Total (absoluta) incluye atmósfera
> **R** - Relativa al nivel del mar
> **O** - Operacional y práctica medición
>
> [!success] Puntos Clave para Recordar 🎯
> 1. **📏 Referencia atmosférica**: P_man = P_abs - P_atm
> 2. **🔄 Signo importa**: Positiva (sobrepresión), negativa (vacío)
> 3. **🌍 Dependencia de altitud**: P_atm varía con elevación
> 4. **🔧 Instrumentos comunes**: Miden presión manométrica por defecto
> 5. **⚖️ Aplicación práctica**: Más útil que presión absoluta en ingeniería
> 6. **🧮 Conversión simple**: Sumar P_atm para obtener presión absoluta

---

## Referencias

> [!quote] Notas Relacionadas
> - [[Presión y Densidad]]
> - [[El Principio de Pascal]]
> - [[Principio de los Vasos Comunicantes]]
> - [[Módulo de Compresibilidad]]

## Notas Recomendadas

> [!info] Prerrequisitos
> - [[Presión y Densidad]]
> - [[Fuerzas y Diagramas de Cuerpo Libre]]
> - [[Equilibrio]]
>
> [!tip] Continuación del Tema
> - [[Viscosidad y Número de Reynolds]]
> - [[Ecuación de Continuidad y Bernoulli]]
> - [[Flujo Laminar y Ecuación de Poiseuille]]

---

**Tags:** #física #hidrostática #presión-manométrica #manómetros #instrumentación #vacío #sobrepresión #medición #ingeniería-fluidos #presión-absoluta
