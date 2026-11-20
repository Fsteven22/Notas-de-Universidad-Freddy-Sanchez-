---
dg-publish: true
---

# Peso Real vs Peso Aparente

>[!quote] _"Cuando un objeto se sumerge en un fluido, experimenta una ilusión de ligereza. Esta aparente pérdida de peso no es magia, sino la manifestación directa del principio de Arquímedes, donde las fuerzas de flotación revelan la danza invisible entre la gravedad y la densidad."_
>

> [!info]+ Definiciones Fundamentales ⚖️
> 
> ### Peso Real (W_real)
> 
> El **peso real** es la fuerza gravitacional que actúa sobre un objeto, calculada como el producto de su masa por la aceleración de la gravedad. **Este valor es constante** independientemente del medio que rodee al objeto.
> 
> **W_real = m × g**
> 
> ### Peso Aparente (W_aparente)
> 
> El **peso aparente** es el peso que percibimos o medimos cuando el objeto está sumergido en un fluido. Es el resultado de la **interacción entre el peso real y la fuerza de flotación**.
> 
> **W_aparente = W_real - F_flotación** **W_aparente = m × g - ρ_fluido × V_sumergido × g**
>

> [!note] Fundamento Físico - Principio de Arquímedes 🌊
> 
> ### Base Teórica
> 
> La diferencia entre peso real y aparente surge del **Principio de Arquímedes**:
> 
> - Todo cuerpo sumergido en un fluido experimenta una fuerza hacia arriba
> - Esta fuerza es igual al peso del fluido desplazado
> - La fuerza actúa en el centro de flotación del objeto
> 
> ### Diagrama de Fuerzas
> 
> ![[Diagramas/Peso_Real_vs_Peso_Aparente_01.svg]]
>

> [!tip] Casos y Situaciones 🔬
> 
> ### Clasificación por Densidad Relativa
> 
> |Situación|Condición|Peso Aparente|Comportamiento|
> |---|---|---|---|
> |🪨 **Objeto más denso**|ρ_objeto > ρ_fluido|W_aparente > 0|Se hunde|
> |⚖️ **Densidad igual**|ρ_objeto = ρ_fluido|W_aparente = 0|Flotación neutra|
> |🪵 **Objeto menos denso**|ρ_objeto < ρ_fluido|W_aparente < 0*|Flota en superficie|
> 
> *Nota: En flotación, solo parte del objeto está sumergido, equilibrando las fuerzas.
> 
> ### Grados de Inmersión
> 
> ![[Diagramas/Peso_Real_vs_Peso_Aparente_02.svg]]
>

> [!example] Ejemplos Prácticos y Cálculos 🧮
> 
> ### Ejemplo 1: Piedra en el Agua
> 
> **Problema:** Una piedra de 2 kg y densidad 2500 kg/m³ se sumerge completamente en agua. ¿Cuál es su peso aparente?
> 
> **Datos:**
> 
> - m = 2 kg
> - ρ_piedra = 2500 kg/m³
> - ρ_agua = 1000 kg/m³
> - g = 9.8 m/s²
> 
> **Solución:**
> 
> ```
> 1. Volumen de la piedra:
>    V = m/ρ = 2 kg / 2500 kg/m³ = 0.0008 m³
> 
> 2. Peso real:
>    W_real = m × g = 2 × 9.8 = 19.6 N
> 
> 3. Fuerza de flotación:
>    F_flotación = ρ_agua × V × g = 1000 × 0.0008 × 9.8 = 7.84 N
> 
> 4. Peso aparente:
>    W_aparente = 19.6 - 7.84 = 11.76 N
> ```
> 
> **Resultado:** La piedra "pesa" 11.76 N en el agua (40% menos que en el aire)
> 
> ### Ejemplo 2: Bloque de Madera Flotando
> 
> **Problema:** Un bloque de madera (ρ = 600 kg/m³) de 0.1 m³ flota en agua. ¿Qué fracción está sumergida?
> 
> **Solución:**
> 
> ```
> En equilibrio: W_real = F_flotación
> m × g = ρ_agua × V_sumergido × g
> ρ_madera × V_total × g = ρ_agua × V_sumergido × g
> 
> V_sumergido/V_total = ρ_madera/ρ_agua = 600/1000 = 0.6
> ```
> 
> **Resultado:** 60% del bloque está bajo el agua, 40% emerge
>
> [!abstract] Aplicaciones Prácticas 🏗️
> 
> ### En la Industria y Tecnología
> 
> - **🚢 Diseño naval**: Cálculo de desplazamiento y estabilidad
> - **🏗️ Construcción submarina**: Fuerzas en cimentaciones
> - **⚖️ Balanzas hidrostáticas**: Medición precisa de densidades
> - **🛢️ Industria petrolera**: Separación por densidad
> 
> ### En Ciencias e Investigación
> 
> ![[Diagramas/Peso_Real_vs_Peso_Aparente_03.svg]]
>

> [!warning] Factores que Afectan la Medición ⚠️
> 
> ### Variables del Fluido
> 
> - **🌡️ Temperatura**: Afecta la densidad del fluido
> - **📊 Presión**: Modifica la densidad (especialmente en gases)
> - **🧪 Composición**: Salinidad, impurezas, concentración
> - **🌀 Viscosidad**: Afecta el movimiento del objeto
> 
> ### Variables del Objeto
> 
> - **📐 Forma geométrica**: Afecta la distribución de presiones
> - **🕳️ Porosidad**: Absorción de fluido modifica el peso
> - **🌡️ Expansión térmica**: Cambios de volumen con temperatura
> - **⚗️ Reactividad**: Interacciones químicas con el fluido
> 
> ### Condiciones Experimentales
> 
> - **🏃 Movimiento relativo**: Efectos dinámicos vs estáticos
> - **📏 Precisión instrumental**: Limitaciones de medición
> - **🌊 Turbulencia**: Fluctuaciones en la fuerza de flotación
>

> [!summary]+ Fórmulas y Relaciones Clave 📊
> 
> ### Ecuaciones Fundamentales
> 
> ```
> Peso Real:           W_real = m × g
> Peso Aparente:       W_aparente = W_real - F_flotación
> Fuerza de Flotación: F_flotación = ρ_fluido × V_sumergido × g
> Ecuación General:    W_aparente = m × g - ρ_fluido × V_sumergido × g
> ```
> 
> ### Para Objetos Totalmente Sumergidos
> 
> ```
> W_aparente = W_real × (1 - ρ_fluido/ρ_objeto)
> Reducción relativa = (W_real - W_aparente)/W_real = ρ_fluido/ρ_objeto
> ```
> 
> ### Para Flotación en Equilibrio
> 
> ```
> Fracción sumergida = V_sumergido/V_total = ρ_objeto/ρ_fluido
> Fracción emergente = 1 - ρ_objeto/ρ_fluido
> ```
>
> [!brain]+ Técnica de Memorización: FLOTAR 🧠 **F** - Flotación reduce el peso aparente **L** - Líquido ejerce fuerza hacia arriba **O** - Objeto desplaza su propio volumen **T** - Todo sumergido siente menos peso **A** - Arquímedes explica la diferencia **R** - Real menos flotación igual aparente
>

> [!success] Puntos Clave para Recordar 🎯
> 
> 1. **⚖️ Peso real constante**: No cambia con el medio circundante
> 2. **🌊 Peso aparente variable**: Depende de la densidad del fluido
> 3. **📉 Siempre menor**: W_aparente ≤ W_real (en fluidos normales)
> 4. **🔄 Principio de Arquímedes**: Base física del fenómeno
> 5. **📐 Volumen sumergido**: Factor clave en el cálculo
> 6. **🎯 Flotación perfecta**: Peso aparente = 0

---

## Referencias

> [!quote] Notas Relacionadas
> 
> - [[El Principio de Arquímedes y Flotación]]
> - Obsidian/Universidad/Física Mecanica/Notas nuevas/06 - Hidrostática e hidrodinámica/Presión y Densidad
> - [[Fuerzas y Diagramas de Cuerpo Libre]]
> - [[Leyes de Newton]]

## Notas Recomendadas

> [!info] Prerrequisitos
> 
> - Obsidian/Universidad/Física Mecanica/Notas nuevas/06 - Hidrostática e hidrodinámica/Presión y Densidad
> - [[Fuerzas y Diagramas de Cuerpo Libre]]
> - [[Leyes de Newton]]
>

> [!tip] Continuación del Tema
> 
> - [[El Principio de Arquímedes y Flotación]]
> - [[Centro de Gravedad (CG)]]
> - [[Equilibrio]]

---

**Tags:** #física #hidrostática #arquímedes #flotación #peso-aparente #densidad #fuerzas #equilibrio-fluidos #principios-físicos