# 🎯 Rodadura

> [!abstract] 📋 Resumen General La **rodadura** es el movimiento combinado de traslación y rotación de un objeto rígido. Se puede analizar mediante dos enfoques complementarios: el **método dinámico** (aplicando las leyes de Newton) y el **método energético** (usando conservación de energía). Ambos métodos requieren la condición fundamental de rodadura sin deslizar.

---

## 🔍 Conceptos Fundamentales

> [!info] 💡 Definición Base La **rodadura** es el movimiento de un objeto rígido que gira mientras su centro de masa se traslada. En una **rodadura sin deslizar**, el punto del objeto en contacto con la superficie está instantáneamente en reposo.

> [!note] ⚖️ Condición Universal de Rodadura Sin Deslizar $$v_{CM} = \omega R \quad \text{y} \quad a_{CM} = \alpha R$$

> [!warning] ⚠️ Punto Clave Esta condición cinemática es **fundamental** para ambos métodos y conecta los movimientos lineal y rotacional.

---

> [!note] 📊 Variables Comunes
> 
> |Variable|Símbolo|Descripción|
> |---|---|---|
> |Masa|$M$|Masa del objeto que rueda|
> |Radio|$R$|Radio del objeto|
> |Momento de inercia|$I$|Momento de inercia respecto al CM|
> |Velocidad lineal CM|$v_{CM}$|Velocidad del centro de masa|
> |Velocidad angular|$\omega$|Velocidad de rotación|
> |Aceleración lineal CM|$a_{CM}$|Aceleración del centro de masa|
> |Aceleración angular|$\alpha$|Aceleración de rotación|
> |Fuerza de fricción|$f_s$|Fuerza en el punto de contacto|
> |Altura|$h$|Altura del centro de masa|

---

# 🔧 Método Dinámico

> [!tip] 🎯 Cuándo Usar el Método Dinámico
> 
> - Cuando necesitas encontrar **fuerzas** (especialmente fricción)
> - Cuando requieres calcular **aceleraciones**
> - Para análisis detallado de todas las fuerzas actuantes

> [!note] ⚖️ Sistema de Ecuaciones Fundamentales
> 
> ### 1️⃣ Segunda Ley de Newton (Lineal)
> 
> $$\sum F_{ext} = M\vec{a}_{CM}$$
> 
> ### 2️⃣ Segunda Ley de Newton (Rotacional)
> 
> $$\sum \tau_{ext} = I\alpha$$
> 
> ### 3️⃣ Condición de Rodadura Sin Deslizar
> 
> $$a_{CM} = \alpha R$$

> [!info] 🔄 Proceso de Resolución (Método Dinámico)
> 
> ```mermaid
> flowchart TD
>    A[🎯 Problema de Rodadura] --> B[📐 Diagrama de Cuerpo Libre]
>    B --> C[⚖️ Segunda Ley Newton Lineal]
>    B --> D[🔄 Segunda Ley Newton Rotacional]
>    C --> E[📝 Sistema de Ecuaciones]
>    D --> E
>    E --> F[🔗 Aplicar Condición: a = αR]
>    F --> G[🧮 Resolver Sistema]
>    G --> H[✅ Obtener a, f, etc.]
>    
>    style A fill:#e1f5fe
>    style H fill:#c8e6c9
>    style F fill:#fff3e0
> ```

## 🎲 Ejemplos Método Dinámico

> [!example] 🔵 Ejemplo 1: Disco con Fuerza Aplicada
> 
> **📋 Problema:** Un disco de masa $M$ y radio $R$ rueda sin deslizar debido a una fuerza constante $F$. Encontrar la aceleración y la fuerza de fricción.
> 
> **🔧 Solución paso a paso:**
> 
> 1. **Dinámica lineal:** $F - f_s = Ma_{CM}$
> 2. **Dinámica rotacional:** $f_s R = I\alpha = \frac{1}{2}MR^2\alpha$
> 3. **Rodadura sin deslizar:** $a_{CM} = \alpha R$
> 
> **📊 Resultado:**
> 
> - Aceleración: $a_{CM} = \frac{2F}{3M}$
> - Fricción: $f_s = \frac{F}{3}$

> [!example] 🔺 Ejemplo 2: Cilindro en Plano Inclinado
> 
> **📋 Problema:** Un cilindro rueda por un plano inclinado de ángulo $\theta$. Encontrar la aceleración del centro de masa.
> 
> **🔧 Solución:**
> 
> 1. **Componente gravitacional:** $Mg\sin\theta - f_s = Ma_{CM}$
> 2. **Torque de fricción:** $f_s R = I\alpha$
> 3. **Condición de rodadura:** $a_{CM} = \alpha R$
> 
> **📊 Resultado:** $$a_{CM} = \frac{g\sin\theta}{1+\frac{I}{MR^2}}$$

---

# ⚡ Método Energético

> [!tip] 🎯 Cuándo Usar el Método Energético
> 
> - Cuando solo necesitas **velocidades finales** o **alturas**
> - Para **comparar diferentes objetos** rodando
> - Cuando las fuerzas no conservativas **no realizan trabajo**
> - Para resolver problemas de manera **más directa**

> [!note] 🔋 Ecuaciones Fundamentales
> 
> ### Energía Cinética Total de Rodadura
> 
> $$K_{total} = K_{trasl} + K_{rot} = \frac{1}{2}Mv_{CM}^2 + \frac{1}{2}I\omega^2$$
> 
> ### Condición de Rodadura (Energético)
> 
> $$v_{CM} = \omega R$$
> 
> ### Principio de Conservación
> 
> $$E_{inicial} = E_{final}$$ $$K_{total,i} + U_{g,i} = K_{total,f} + U_{g,f}$$

> [!info] 🔄 Proceso de Resolución (Método Energético)
> 
> ```mermaid
> flowchart TD
>    A[🎯 Problema de Rodadura] --> B[⚡ Identificar Estados Inicial y Final]
>    B --> C[📊 Calcular Energías Iniciales]
>    B --> D[📊 Calcular Energías Finales]
>    C --> E[⚖️ Aplicar Conservación de Energía]
>    D --> E
>    E --> F[🔗 Usar Condición: v = ωR]
>    F --> G[🧮 Resolver para Incógnita]
>    G --> H[✅ Obtener v, h, etc.]
>    
>    style A fill:#e1f5fe
>    style H fill:#c8e6c9
>    style F fill:#fff3e0
> ```

## 🎲 Ejemplos Método Energético

> [!example] 🔵 Ejemplo 1: Cilindro Rodando por Plano Inclinado
> 
> **📋 Problema:** Un cilindro de masa $M$ y radio $R$ parte del reposo y rueda por un plano inclinado de altura $h$. ¿Cuál es la velocidad de su centro de masa en la base?
> 
> **🔧 Solución:**
> 
> 1. **Energía inicial:** $E_i = U_g = Mgh$
> 2. **Energía final:** $E_f = K_{total} = \frac{1}{2}Mv_{CM}^2 + \frac{1}{2}I\omega^2$
> 3. **Condición de rodadura:** $\omega = v_{CM}/R$
> 4. **Conservación:** $Mgh = \frac{1}{2}Mv_{CM}^2 + \frac{1}{2}I\left(\frac{v_{CM}}{R}\right)^2$
> 
> **📊 Resultado:** $$v_{CM} = \sqrt{\frac{2gh}{1+\frac{I}{MR^2}}}$$

> [!example] 🏁 Ejemplo 2: Carrera de Objetos
> 
> **📋 Problema:** Un disco y un aro con la misma masa y radio se sueltan desde la misma altura. ¿Cuál llega primero?
> 
> **🔧 Análisis:**
> 
> |Objeto|Momento de Inercia|Velocidad Final|
> |---|---|---|
> |Disco|$I = \frac{1}{2}MR^2$|$v = \sqrt{\frac{4gh}{3}}$|
> |Aro|$I = MR^2$|$v = \sqrt{gh}$|
> 
> **📊 Resultado:** El disco llega primero (mayor velocidad final)

---

## 📈 Distribución de Energía Cinética

> [!info] 🔋 Análisis Energético La fracción de energía que se convierte en rotación depende del momento de inercia:
> 
> ```mermaid
> pie title Energía Cinética en Rodadura
>    "Esfera: 71% traslación, 29% rotación" : 71
>    "Cilindro: 67% traslación, 33% rotación" : 67
>    "Aro: 50% traslación, 50% rotación" : 50
> ```

> [!note] 📊 Comparación de Velocidades Finales
> 
> Para la misma altura $h$:
> 
> $$v_{esfera} > v_{cilindro} > v_{aro}$$

---

> [!summary] ⚖️ Comparación de Métodos
> 
> |Aspecto|Método Dinámico|Método Energético|
> |---|---|---|
> |**🎯 Objetivo**|Fuerzas y aceleraciones|Velocidades y alturas|
> |**📝 Ecuaciones**|3 ecuaciones simultáneas|1 ecuación de conservación|
> |**🔧 Complejidad**|Mayor (sistema de ecuaciones)|Menor (más directo)|
> |**📊 Información**|Detalles del movimiento|Resultado final|
> |**⚡ Aplicación**|Análisis completo|Resultados rápidos|

> [!tip] 🎯 Estrategia de Selección **Usa método dinámico** cuando necesites fuerzas o aceleraciones
> 
> **Usa método energético** cuando solo necesites velocidades finales

---

> [!info] 🔗 Conexiones Conceptuales
> 
> ```mermaid
> mindmap
>  root((🎯 Rodadura))
>    🔧 Método Dinámico
>      ⚖️ Segunda Ley Newton
>        Lineal
>        Rotacional
>      🔄 Análisis de Fuerzas
>        Fricción estática
>        Peso
>        Normales
>      📊 Resultados
>        Aceleraciones
>        Fuerzas
>    ⚡ Método Energético
>      🔋 Conservación Energía
>        Cinética traslacional
>        Cinética rotacional
>        Potencial gravitatoria
>      📈 Comparaciones
>        Diferentes formas
>        Velocidades finales
>      📊 Resultados
>        Velocidades
>        Alturas
>    🔗 Conceptos Comunes
>      Condición rodadura
>      Momento de inercia
>      Fricción estática
> ```

---

## 📚 Referencias y Enlaces

> [!quote] 🔗 Links a Otras Notas
> 
> - > [[Dinámica Lineal]] - Segunda Ley de Newton
>     
> - > [[Dinámica Rotacional]] - Torque y momento de inercia
>     
> - > [[Cinemática Rotacional]] - Relaciones angulares
>     
> - > [[Física Mecanica/Notas antiguas/Dinámica Rotacional/Momento de Inercia]] - Valores para diferentes formas
>     
> - > [[Fricción Estática]] - Fuerza clave en rodadura
>     
> - > [[Conservación de Energía]] - Fundamento del método energético
>     
> - > [[Diagramas de Cuerpo Libre]] - Análisis de fuerzas
>     
> - > [[Trabajo y Energía]] - Conceptos energéticos
>     
> - > [[Energía Cinética]] - Traslacional y rotacional
>     

> [!quote] 📖 Material de Referencia
> 
> - > Tutorial: S25 Rodadura método dinámico.pdf
>     
> - > Tutorial: S26 Rodadura método energético.pdf
>     
> - > Libro de texto: Capítulo de Dinámica Rotacional
>     
> - > Problemas resueltos: Colección de ejercicios
>     

---

> [!note] 🏷️ Tags #física #mecánica #dinámica #rotación #rodadura #newton #torque #fricción #energía-cinética #método-dinámico #método-energético #conservación-energía #plano-inclinado #momento-inercia #velocidad-angular