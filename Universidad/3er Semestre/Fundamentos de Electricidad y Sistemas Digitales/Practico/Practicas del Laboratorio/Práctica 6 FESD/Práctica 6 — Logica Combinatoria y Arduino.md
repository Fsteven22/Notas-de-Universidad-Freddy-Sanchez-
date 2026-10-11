---
dg-publish: true
---

# 🧪 Práctica 6 — Control por Logica Combinatoria y Arduino

## 🎯 Introducción

> [!info] 💡 ¿Por qué esta práctica es importante?
>
> Esta práctica integra **acondicionamiento de señales**, **compuertas lógicas** y **Arduino** para controlar actuadores. Comparas la implementación con hardware puro (compuertas 74LS/74HC) vs software embebido (Arduino), y analizas las ventajas de cada enfoque.
>
> ```mermaid
> graph TD
>     A[Práctica 6] --> B[Procedimiento 1<br/>Acondicionamiento LM358]
>     A --> C[Procedimiento 2<br/>Lógica combinatoria]
>     A --> D[Procedimiento 3<br/>Arduino + sensores]
>     B --> E[Comparador con umbrales]
>     C --> F[F = A' + BC]
>     D --> G[analogRead + LEDs]
>     style A fill:#fff4e1
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#f5e1ff
> ```

---

## ⚠️ Seguridad

> [!danger]
> - No exceder **5 V** en entradas lógicas de los IC (74LS/74HC).
> - Manipula conexiones con la fuente apagada.
> - El Zener 1N4733A protege las entradas — verificar su presencia antes de energizar.

---

## 🧰 Materiales

> [!note] 📦 Materiales necesarios
>
> | Material | Especificación |
> |---|---|
> | Fuente DC |  |
> | Multímetro | FLUKE 179 |
> | Op-Amp | LM358 |
> | Compuertas | 74LS04 (NOT), 74LS08 (AND), 74HC32 (OR) |
> | Diodos | LED verde/amarillo/rojo, 1N4007, Zener 1N4733A (5.1 V) |
> | Transistores | MOSFET IRF640, 2N2222 |
> | Potenciómetros | 1 KΩ o 10 KΩ |
> | Resistencias | 220, 330, 560, 1 KΩ, 10 KΩ |
> | Motor DC | 1 unidad |
> | Arduino | Uno o Nano |

---

## 📖 Introducción Teórica

> [!note] 🔵 Acondicionamiento de señales
>
> Las familias **TTL** y **CMOS** operan a 5 V. Si el voltaje supera 5 V, se dañan los transistores internos. Si está por debajo del umbral lógico, el IC no reconoce la señal.
>
> Se usa un **Zener 1N4733A** (5.1 V) para regular y proteger las entradas lógicas, asegurando que las señales acondicionadas no sobrepasen el voltaje de operación seguro.
>
> [!note] 🟢 Compuertas lógicas
>
> |Compuerta|IC|Función|Salida|
> |---|---|---|---|
> |**NOT**|74LS04|Inversión|$A'$|
> |**AND**|74LS08|Conjunción|$A \cdot B$|
> |**OR**|74HC32|Disyunción|$A + B$|
>
> [!note] 🟡 Comparador con LM358
>
> Los potenciometros RV1 (70%) y RV3 (30%) establecen umbrales de referencia con fuente de 12 V:
> - RV1 (70%): $V_{ref} = 8.4$ V
> - RV3 (30%): $V_{ref} = 3.6$ V
>
> Las salidas se activan al cruzar estos umbrales generados por la señal central.

---

## ⚙️ Procedimiento 1 — Acondicionamiento de Señales

> [!tip] 🔧 Pasos
>
> 1. Diseñar bloque comparador con LM358.
> 2. Ajustar RV1 al 70% y RV3 al 30%.
> 3. Observar activación de salidas según la señal Vacond.
>
> [!question]- ❓ Análisis
>
> - **Función del Zener 1N4733A:** regula y fija el voltaje a máximo 5.1 V. Protege las entradas lógicas de sobrevoltaje.
> - **Voltajes de referencia:** RV1 (70%) = 8.4 V, RV3 (30%) = 3.6 V. Las salidas se activan al cruzar estos umbrales.

---

## ⚙️ Procedimiento 2 — Logica Combinatoria

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con compuertas 74LS04, 74LS08, 74HC32.
> 2. Implementar la función lógica $F = A' + (B \cdot C)$.
> 3. Verificar con tabla de verdad.
>
> [!note] 📊 Tabla de verdad
>
> |A|B|C|F|
> |---|---|---|---|
> |0|0|0|1|
> |0|0|1|1|
> |0|1|0|1|
> |0|1|1|1|
> |1|0|0|0|
> |1|0|1|0|
> |1|1|0|0|
> |1|1|1|1|
>
> [!note] 🔵 Simplificación
>
> - **SOP:** $F = A'B'C' + A'B'C + A'BC' + A'BC + ABC$
> - **POS:** $F = (A'+B+C) \cdot (A'+B+C') \cdot (A'+B'+C)$
> - **Mapa de Karnaugh:** simplificado a $F = A' + BC$

---

## ⚙️ Procedimiento 3 — Integración con Arduino

> [!tip] 🔧 Pasos
>
> 1. Conectar sensor analógico al pin A0 del Arduino.
> 2. Conectar LEDs a pines digitales 7 (rojo), 5 (amarillo), 3 (verde).
> 3. Subir código y observar comportamiento en Monitor Serial.
>
> [!note] 📐 Código Arduino
>
> ```cpp
> int rojo = 7;
> int amarillo = 5;
> int verde = 3;
> int sensor = 0;
> int valorLectura = 0;
>
> void setup() {
>   pinMode(A0, INPUT);
>   pinMode(rojo, OUTPUT);
>   pinMode(amarillo, OUTPUT);
>   pinMode(verde, OUTPUT);
>   Serial.begin(9600);
> }
>
> void loop() {
>   valorLectura = analogRead(A0);
>   Serial.println(valorLectura);
>   delay(10);
>   sensor = map(valorLectura, 0, 1023, 0, 100);
>   Serial.println(sensor);
>   if (sensor <= 30) {
>     digitalWrite(verde, LOW);
>     digitalWrite(amarillo, LOW);
>     digitalWrite(rojo, HIGH);
>   } else if (sensor > 30 && sensor < 70) {
>     digitalWrite(verde, LOW);
>     digitalWrite(amarillo, HIGH);
>     digitalWrite(rojo, LOW);
>   } else if (sensor >= 70) {
>     digitalWrite(verde, HIGH);
>     digitalWrite(amarillo, LOW);
>     digitalWrite(rojo, LOW);
>   }
> }
> ```
>
> [!question] ❓ Funciones clave de Arduino
>
> |Función|Descripción|
> |---|---|
> |`analogRead(pin)`|Lee voltaje (0–5 V) y retorna 0–1023 (ADC 10 bits)|
> |`digitalWrite(pin, value)`|Escribe HIGH (5 V) o LOW (0 V) en pin digital|
> |`Serial.begin(9600)`|Inicializa comunicación serial a 9600 baudios|
> |`Serial.println()`|Imprime datos al Monitor Serial para graficar|

---

## 📊 Contraste: Compuertas Lógicas vs Arduino

> [!success] 📊 Comparación de enfoques
>
> |Aspecto|Compuertas lógicas (HW)|Arduino (SW)|
> |---|---|---|
> |**Velocidad**|Nanosegundos (casi instantáneo)|Ciclos de reloj (ms)|
> |**Flexibilidad**|Nula — hay que recablear para cambiar lógica|Alta — solo cambiar código|
> |**Escalabilidad**|Limitada por espacio físico|Amplia (agregar funciones con código)|
> |**Costo**|Más ICs para lógica compleja|Un solo microcontrolador|

---

## 📝 Notas personales

> [!question]- 🤔 Mis observaciones
>
> - Diferencias teórico vs medido:
> - Errores encontrados:
> - Dudas para el informe:

---

## 📄 Informe

> Usa [[FORMATO INFORME DE PRÁCTICA.pdf]] y [[Formato Pre-prácticas.pdf]] para entregar. Simulaciones en Proteus.

## Metas de Aprendizaje

> [!note] Nivel Básico
> - [ ] Identifico los integrados 74LS04, 74LS08 y 74HC32 y verifico sus pines VCC y GND en el datasheet.
> - [ ] Acondiciono una señal analógica a 0–5 V usando Zener 1N4733A para proteger las entradas lógicas.
> - [ ] Implemento la función lógica $F = A' + (B \cdot C)$ con compuertas NOT, AND y OR.
>
> [!note] Nivel Intermedio
> - [ ] Verifico la tabla de verdad midiendo voltajes en las salidas de cada compuerta.
> - [ ] Uso el mapa de Karnaugh para simplificar una función booleana y la comparo con la implementación física.
> - [ ] Programo el Arduino para leer un sensor analógico con `analogRead()` y mapear el valor a un rango útil.
>
> [!note] Nivel Avanzado
> - [ ] Controlo 3 LEDs (rojo, amarillo, verde) con `digitalWrite()` según rangos del sensor.
> - [ ] Uso `Serial.println()` para enviar datos al Monitor Serial y graficar el comportamiento del sensor.
> - [ ] Comparo ventajas y desventajas de controlar con compuertas lógicas vs Arduino en una aplicación real.
>
> [!quote] 🔗 Conexiones
> - Teoría: [[01 - Introducción a la Electrónica Digital]], [[02 - Minimización de Funciones Lógicas]] y [[07 - Lógica fija y tablas de verdad]]
> - Previa: [[Práctica 5 — Filtros Activos]]
> - Equipos: [[Equipos del Laboratorio - FESD]]

---

---

## 📎 Guía oficial (Garden)

![[Practica__6_FESD.pdf]]
**Tags:** #practica #laboratorio #EYAG1037 #FESD #ESPOL #unidad4 #logica #Arduino #compuertas
