---
dg-publish: true
---

# Problemas de Tiempo y Distancia Recorrida

>[!quote] _"Un viaje se compone de muchos pasos, y cada paso tiene su propio ritmo y medida"_ - Análisis del movimiento por tramos

---

## 📋 Definición y Características

> [!info] 🎯 **¿Qué son los Problemas de Tiempo y Distancia?** Son situaciones donde un móvil **viaja por diferentes tramos** con velocidades distintas, y se requiere calcular:
> 
> - **Distancia total recorrida**
> - **Tiempo total empleado**
> - **Velocidad media** del recorrido completo
> - **Datos faltantes** en algún tramo específico
> 
> **🔑 Principio fundamental:** $$d_{total} = \sum_{i=1}^{n} d_i, \quad t_{total} = \sum_{i=1}^{n} t_i, \quad \bar{v} = \frac{d_{total}}{t_{total}}$$

---

## 🛣️ Tipos de Problemas de Tiempo-Distancia

> [!tip] 📏 **Movimiento por Tramos con Datos Completos** **Situación:** Se conocen velocidad y tiempo (o distancia) de cada tramo
> 
> ```mermaid
> graph LR
>     A[Tramo 1<br/>v₁, t₁ → d₁] --> B[Tramo 2<br/>v₂, t₂ → d₂]
>     B --> C[Tramo 3<br/>v₃, t₃ → d₃]
>     C --> D[Totales<br/>Σdᵢ, Σtᵢ, v̄]
>     style D fill:#98FB98
> ```
> 
> **Ejemplos típicos:**
> 
> - 🚗 Viaje por carretera con diferentes límites de velocidad
> - 🚂 Tren con tramos urbanos y rurales
> - 🚴‍♂️ Ciclista en terreno variado (llano, subida, bajada)
> - ✈️ Vuelo con diferentes velocidades por altitud
>
> [!warning] 🧩 **Movimiento con Datos Incompletos** **Situación:** Faltan algunos datos en ciertos tramos, se deben calcular
> 
> **Casos típicos:**
> 
> - Se conoce distancia y velocidad → calcular tiempo
> - Se conoce tiempo y velocidad → calcular distancia
> - Se conoce distancia y tiempo → calcular velocidad
> - **Mixto:** Diferentes datos faltantes por tramo
> 
> **Estrategia:** Usar $d = vt$ en cada tramo para completar datos
>
> [!note] ⏱️ **Problemas de Velocidad Media** **Situación:** Calcular la velocidad promedio real del viaje completo
> 
> **⚠️ Advertencia crítica:** $$\bar{v} = \frac{d_{total}}{t_{total}} \neq \frac{v_1 + v_2 + ... + v_n}{n}$$
> 
> La velocidad media **NO es** el promedio aritmético de las velocidades
>
> [!abstract] 🔄 **Viajes de Ida y Vuelta** **Situación especial:** Recorrido del mismo trayecto a velocidades diferentes
> 
> **Casos comunes:**
> 
> - Ida rápida, vuelta lenta (o viceversa)
> - Condiciones cambiantes (tráfico, clima, combustible)
> - **Velocidad media armónica** cuando las distancias son iguales

---

## 📐 Metodología de Resolución

> [!example] 🛠️ **Pasos para Resolver Problemas de Tiempo-Distancia**
> 
> ### Paso 1: Organizar los Datos en Tabla
> 
> Crear tabla con columnas: **Tramo | Distancia | Velocidad | Tiempo**
> 
> ### Paso 2: Identificar Datos Conocidos y Faltantes
> 
> - ✅ **Conocidos:** Marcar con valores numéricos
> - ❓ **Faltantes:** Marcar para calcular
> 
> ### Paso 3: Completar Datos Faltantes por Tramo
> 
> - **Falta distancia:** $d_i = v_i \times t_i$
> - **Falta tiempo:** $t_i = \frac{d_i}{v_i}$
> - **Falta velocidad:** $v_i = \frac{d_i}{t_i}$
> 
> ### Paso 4: Calcular Totales
> 
> - **Distancia total:** $d_{total} = d_1 + d_2 + ... + d_n$
> - **Tiempo total:** $t_{total} = t_1 + t_2 + ... + t_n$
> 
> ### Paso 5: Calcular Velocidad Media
> 
> $$\bar{v} = \frac{d_{total}}{t_{total}}$$
> 
> ### Paso 6: Verificar Coherencia
> 
> - Comprobar unidades consistentes
> - Verificar que la velocidad media sea razonable

---

## 📊 Fórmulas y Relaciones Especiales

> [!abstract] 📋 **Tabla de Fórmulas por Tipo de Problema**
> 
> |Tipo de Cálculo|Fórmula|Aplicación|
> |---|---|---|
> |**Distancia por tramo**|$d_i = v_i \times t_i$|Cuando se conoce $v_i$ y $t_i$|
> |**Tiempo por tramo**|$t_i = \frac{d_i}{v_i}$|Cuando se conoce $d_i$ y $v_i$|
> |**Velocidad por tramo**|$v_i = \frac{d_i}{t_i}$|Cuando se conoce $d_i$ y $t_i$|
> |**Distancia total**|$d_{total} = \sum d_i$|Suma de todos los tramos|
> |**Tiempo total**|$t_{total} = \sum t_i$|Suma de todos los tiempos|
> |**Velocidad media**|$\bar{v} = \frac{d_{total}}{t_{total}}$|**NO** es promedio aritmético|
>
> [!note] 🔢 **Velocidad Media Armónica (Caso Especial)** **Cuándo usarla:** Cuando se recorren **distancias iguales** a velocidades diferentes
> 
> **Fórmula general:** $$\bar{v}_{armónica} = \frac{n}{\frac{1}{v_1} + \frac{1}{v_2} + ... + \frac{1}{v_n}}$$
> 
> **Para dos tramos iguales:** $$\bar{v} = \frac{2v_1 v_2}{v_1 + v_2}$$
> 
> **Ejemplo típico:** Ida y vuelta por la misma ruta

---

## 💡 Ejemplos Resueltos

> [!example] 🚗 **Ejemplo 1: Viaje Completo por Tramos** **Problema:** Un móvil viaja 2 horas a 60 km/h, luego 3 horas a 80 km/h, y finalmente 120 km a 40 km/h. Calcular: a) Distancia total, b) Tiempo total, c) Velocidad media.
> 
> **Solución:**
> 
> ### Paso 1: Organizar datos iniciales
> 
> |Tramo|Tiempo (h)|Velocidad (km/h)|Distancia (km)|
> |---|---|---|---|
> |1|2|60|?|
> |2|3|80|?|
> |3|?|40|120|
> 
> ### Paso 2: Completar datos faltantes
> 
> **Tramo 1:** $d_1 = v_1 \times t_1 = 60 \times 2 = 120$ km **Tramo 2:** $d_2 = v_2 \times t_2 = 80 \times 3 = 240$ km  
> **Tramo 3:** $t_3 = \frac{d_3}{v_3} = \frac{120}{40} = 3$ h
> 
> ### Paso 3: Tabla completa
> 
> |Tramo|Tiempo (h)|Velocidad (km/h)|Distancia (km)|
> |---|---|---|---|
> |1|2|60|120|
> |2|3|80|240|
> |3|3|40|120|
> |**TOTAL**|**8**|**—**|**480**|
> 
> ### Paso 4: Calcular velocidad media
> 
> $$\bar{v} = \frac{d_{total}}{t_{total}} = \frac{480}{8} = 60 \text{ km/h}$$
> 
> **Respuestas:**
> 
> - **a) Distancia total:** 480 km
> - **b) Tiempo total:** 8 horas
> - **c) Velocidad media:** 60 km/h
> 
> **Verificación:** Promedio aritmético = $\frac{60+80+40}{3} = 60$ km/h (coincide por casualidad)
>
> [!example] 🔄 **Ejemplo 2: Ida y Vuelta con Velocidades Diferentes** **Problema:** Un auto va de la ciudad A a la B (180 km) a 90 km/h. Al regresar por la misma ruta lo hace a 60 km/h. Calcular la velocidad media del viaje completo.
> 
> **Solución:**
> 
> ### Método 1: Tabla de tramos
> 
> **Datos:**
> 
> - Ida: $d_1 = 180$ km, $v_1 = 90$ km/h
> - Vuelta: $d_2 = 180$ km, $v_2 = 60$ km/h
> 
> **Cálculo de tiempos:**
> 
> - $t_1 = \frac{180}{90} = 2$ h
> - $t_2 = \frac{180}{60} = 3$ h
> 
> **Totales:**
> 
> - $d_{total} = 180 + 180 = 360$ km
> - $t_{total} = 2 + 3 = 5$ h
> 
> **Velocidad media:** $$\bar{v} = \frac{360}{5} = 72 \text{ km/h}$$
> 
> ### Método 2: Velocidad media armónica
> 
> Para distancias iguales: $$\bar{v} = \frac{2v_1 v_2}{v_1 + v_2} = \frac{2 \times 90 \times 60}{90 + 60} = \frac{10800}{150} = 72 \text{ km/h}$$
> 
> **Respuesta:** La velocidad media del viaje completo es 72 km/h.
> 
> **Nota:** NO es $\frac{90+60}{2} = 75$ km/h porque los tiempos son diferentes.

---

## 🎨 Representación Visual

> [!note] 📈 **Gráficos y Diagramas Útiles**
> 
> ```mermaid
> graph TB
>     subgraph "Análisis por Tramos"
>         A[Tramo 1: d₁, v₁, t₁] --> B[Tramo 2: d₂, v₂, t₂]
>         B --> C[Tramo 3: d₃, v₃, t₃]
>         C --> D[Resultados Totales]
>     end
>     subgraph "Verificaciones"
>         E[Unidades Consistentes] --> F[Datos Completos]
>         F --> G[Cálculo de v̄]
>         G --> H{¿Es razonable?}
>     end
>     style D fill:#90EE90
>     style H fill:#FFB6C1
> ```
> 
> ### Interpretación del Gráfico v-t
> 
> - **Altura de cada barra:** Velocidad del tramo
> - **Ancho de cada barra:** Tiempo del tramo
> - **Área de cada barra:** Distancia recorrida ($d = v \times t$)
> - **Área total:** Distancia total del viaje

---

## 🧠 Técnica Mnemotécnica: "TABLA"

> [!tip] 🎯 **Método TABLA para Tiempo-Distancia**
> 
> **T** - **T**abular datos por tramos (organizar información) **A** - **A**nalizar qué datos faltan en cada tramo **B** - **B**uscar los valores faltantes usando $d = vt$ **L** - **L**istar totales: $\sum d_i$ y $\sum t_i$ **A** - **A**plicar velocidad media: $\bar{v} = \frac{d_{total}}{t_{total}}$
> 
> **🔄 Regla nemotécnica:** _"Toda Aventura Bien Llevada Amerita"_
> 
> ### Verificación Rápida: "RUVT"
> 
> **R** - **R**evizar unidades (todo en km/h o m/s)  
> **U** - **U**nir distancias y tiempos totales  
> **V** - **V**elocidad media con fórmula correcta  
> **T** - **T**estetar si el resultado es lógico

---

## ⚠️ Errores Comunes y Consejos

> [!warning] 🚫 **Errores Frecuentes**
> 
> ### ❌ Error 1: Velocidad Media Incorrecta
> 
> **Problema:** Calcular $\bar{v} = \frac{v_1 + v_2 + ... + v_n}{n}$ (promedio aritmético) **Solución:** Siempre usar $\bar{v} = \frac{d_{total}}{t_{total}}$ **Ejemplo:** Si vas 1 km a 30 km/h y 1 km a 60 km/h, la velocidad media es 40 km/h, NO 45 km/h
> 
> ### ❌ Error 2: Unidades Inconsistentes
> 
> **Problema:** Mezclar km/h con m/s, horas con minutos **Solución:** Convertir todo al mismo sistema antes de calcular **Truco:** Crear columna de "Unidades" en la tabla
> 
> ### ❌ Error 3: No Completar Todos los Datos
> 
> **Problema:** Intentar calcular totales con datos faltantes **Solución:** Completar TODOS los campos de la tabla antes de sumar
> 
> ### ❌ Error 4: Confundir Distancia con Desplazamiento
> 
> **Problema:** En viajes de ida y vuelta, usar desplazamiento neto (cero) **Solución:** Usar distancia total recorrida, no desplazamiento neto

---

## 📊 Casos Especiales y Aplicaciones

> [!abstract] 🔄 **Movimiento con Paradas** **Situación:** El móvil hace paradas (tiempo parado se incluye en tiempo total)
> 
> **Consideraciones:**
> 
> - Tiempo de parada cuenta para tiempo total
> - Durante paradas: $v = 0$, pero $t \neq 0$
> - Afecta significativamente la velocidad media
> 
> **Ejemplo:** Autobús urbano con paradas frecuentes
>
> [!note] ⛽ **Problemas de Consumo Combinado** **Extensión:** Combinar tiempo-distancia con consumo de combustible
> 
> **Variables adicionales:**
> 
> - Consumo por tramo (L/100km o km/L)
> - Eficiencia en diferentes condiciones
> - Costo por tramo
> 
> **Aplicación:** Planificación de viajes largos
>
> [!tip] 🚴‍♂️ **Deportes y Rendimiento** **Aplicación:** Análisis de rendimiento atlético por segmentos
> 
> **Métricas útiles:**
> 
> - Pace (min/km) en diferentes tramos
> - Velocidad en subidas vs bajadas
> - Fatiga acumulativa (velocidad decreciente)
> 
> **Deportes típicos:** Ciclismo, maratón, triatlón

---

## 🔗 Referencias

> [!quote] 📚 **Notas Relacionadas**
> 
> - [[Cinemática Traslacional]] - Base teórica para cada tramo
> - [[Problemas de Persecución]] - Para casos con móviles múltiples
> - [[Análisis Gráfico del Movimiento]] - Representación visual


---

#tiempo-distancia #velocidad-media #tramos #movimiento-uniforme #análisis-sistemático #viajes #recorridos
