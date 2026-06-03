# 🧪 Práctica 1 — Manejo de Equipos del Laboratorio

> [!danger]- ⚠️ Riesgo Eléctrico Se trabaja con **5 VDC**. El riesgo está en la fuente DC y el generador de funciones.
> 
> - ❌ No manipular conexiones sin supervisión del profesor.
> - 🧤 Usar **guantes dieléctricos de baja tensión**.

---

## 🎯 Objetivos

> [!info]- 📌 ¿Qué vamos a lograr?
> 
> - Identificar los equipos y materiales básicos del Laboratorio de Electrónica mediante la implementación y medición en circuitos sencillos.
> - Reconocer las funcionalidades de los equipos más comunes mediante explicación técnica e implementación.

---

## 🧰 Materiales

> [!note]- 📦 ¿Qué necesitamos?
> 
> |Material|Especificación|
> |---|---|
> |Fuente DC|GW INSTEK GPS-4303|
> |Multímetro|FLUKE 179|
> |Generador de Funciones|Meterman / GW INSTEK|
> |Osciloscopio|GW INSTEK GDS-820C|
> |Tablero Universal|—|
> |Resistencia cerámica|10 Ω, 15 W|
> |Resistencia|1 kΩ|

---

## ⚙️ Procedimiento 1 — Fuente DC y Multímetro

> [!tip]- 🔧 Pasos
> 
> **Antes de empezar:** revisar cómo encender la fuente en modo dual y cómo conectar el multímetro según la variable a medir.
> 
> ---
> 
> **Paso 1 — Verificar continuidad y fusibles del multímetro**
> 
> - Poner el multímetro en modo **continuidad** (símbolo `)))`).
> - Tocar las dos puntas entre sí → debe sonar la señal acústica.
> - Verificar los **fusibles internos** con la misma función.
> 
> ---
> 
> **Paso 2 — Configurar fuente dual ±15V**
> 
> - Armar la fuente en modo **dual**: +15V y −15V.
> - Cable verde entre CH3(+) y CH1(−) → referencia (punto C).
> - Cable rojo: CH1(+) → punto A (+Vcc).
> - Cable azul: CH3(−) → punto B (−Vcc).
> - Conectar la resistencia entre A y B, con C como referencia.
> - Presionar **OUTPUT** para energizar.
> 
> ---
> 
> ![[Pasted image 20260525223659.png]]
> 
> **Paso 3 — Medir voltaje DC con el multímetro**
> 
> - Poner el multímetro en modo **V— (tensión DC)**.
> - Conectar punta roja al nodo positivo, punta negra al negativo.
> - Completar la Tabla 1:
> 
> |Punta Roja|Punta Negra|Lectura multímetro|
> |---|---|---|
> |A|B||
> |B|A||
> |A|C||
> |C|A||
> |C|B||
> |B|C||
> 
> ---
> 
> ![[Pasted image 20260525223728.png]]
> 
> **Paso 4 — Medir corriente DC**
> 
> - Cambiar el multímetro a modo **corriente DC**.
> - Conectar en **serie** con el circuito (romper la rama y poner el multímetro en medio).
> - Bornera **mA** si la corriente es menor a 400 mA, bornera **10A** si es mayor.

---

## ⚙️ Procedimiento 2 — Generador de Funciones y Osciloscopio

> [!tip]- 🔧 Pasos
> 
> **Antes de empezar:** revisar cómo configurar el generador y cómo verificar las puntas del osciloscopio.
> 
> ---
> 
> ![[Pasted image 20260525223751.png]]
> 
> **Paso 1 — Conectar el generador a la resistencia**
> 
> - Usar cable **BNC – lagarto** en el puerto de **50 Ω** del generador.
> - Lagarto rojo → terminal positiva de la resistencia.
> - Lagarto negro → referencia (GND).
> 
> ---
> 
> **Paso 2 — Conectar el osciloscopio**
> 
> - Conectar punta de prueba al **CH1** del osciloscopio.
> - Punta → terminal positiva de la resistencia.
> - Lagarto de la punta → GND del circuito.
> - Verificar la punta antes: debe mostrar señal rectangular en la ranura de prueba (bajo F1–F5).
> 
> ---
> 
> **Paso 3 — Ajustar señales y observar**
> 
> Para cada configuración ajustar en el generador y anotar lo observado en el osciloscopio:
> 
> |Tipo de onda|Frecuencia|Vpp (V)|Observaciones|
> |---|---|---|---|
> |Sinusoidal|100 Hz|10||
> |Triangular|1 kHz|5||
> |Cuadrada|10 kHz|12||
> 
> ---
> 
> **Tips para el osciloscopio:**
> 
> - Usar **AUTOSET** si la señal no se ve bien → luego ajustar manualmente si hace falta.
> - Usar **MEASURE** para leer Vpp, frecuencia, período y duty cycle automáticamente.
> - Usar **CURSOR** si necesitas medir un punto específico de la onda.
> - El botón **MATH** permite sumar o restar CH1 y CH2, o activar la FFT.

---

## 📝 Notas personales

> [!question]- 🤔 Mis observaciones de la práctica _(Espacio para agregar reflexiones, errores encontrados, diferencias entre valor teórico y medido, etc.)_

---

**Tags:** #practica #laboratorio #EYAG1037 #FESD #ESPOL #unidad1 #multimetro #osciloscopio #fuenteDC