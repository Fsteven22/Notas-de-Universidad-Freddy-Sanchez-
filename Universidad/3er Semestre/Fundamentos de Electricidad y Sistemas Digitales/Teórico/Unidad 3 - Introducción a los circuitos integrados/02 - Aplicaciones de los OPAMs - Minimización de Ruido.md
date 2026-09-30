---
dg-publish: true
---
# 🔇 Aplicaciones de los OPAMs — Minimización de Ruido

## 🎯 Introducción 

> [!info] 💡 ¿Por qué el OPAM es la herramienta principal contra el ruido?
> 
> En [[06 - Ruido Electrónico e Interferencia]] viste que el ruido puede ser interno (térmico, shot, flicker) o externo (EMI acoplada). El **amplificador operacional (OPAM)** es, junto con los componentes pasivos ya vistos, la herramienta activa más versátil para combatirlo: puede aislar impedancias, rechazar señales de modo común, filtrar frecuencias no deseadas y limpiar transiciones ruidosas antes de que lleguen a una etapa digital.
> 
> Como se trata de un **circuito integrado no programable** (ver [[01 - Introducción a los Circuitos Integrados No Programables]]), su función interna es fija; lo que cambia según la aplicación es la red de resistencias/capacitores externos que lo rodean — exactamente las configuraciones que se resolvieron en la guía de ejercicios de amplificador operacional.
> 
> ```mermaid
> graph LR
>     A[Señal con ruido] --> B[Configuración OPAM<br/>adecuada]
>     B --> C[Señal limpia<br/>o rechazo de ruido]
> 
>     style A fill:#ffe1e1
>     style B fill:#e1ffe1
>     style C fill:#e1f5ff
> ```

---

## 🔌 Seguidor de Tensión (Buffer) — Aislamiento de Impedancias

> [!note] 🔌 ¿Cómo reduce ruido un simple seguidor?
> 
> El seguidor de tensión ($v_o = v_i$, ganancia unitaria) no amplifica ni filtra nada por sí mismo, pero su función es evitar que una fuente de señal de **alta impedancia** (como un sensor) se vea afectada al conectarse a una carga de **baja impedancia**. Esa caída de tensión por carga (loading effect) es, en la práctica, una fuente de distorsión y ruido de la señal original.
> 
> $$v_o = v_i$$
> 
> - Impedancia de entrada: muy alta (no carga a la fuente).
>     
> - Impedancia de salida: muy baja (puede manejar cargas exigentes sin degradarse).
>     
> 
> > 📌 Es el primer paso de acondicionamiento antes de amplificar o filtrar una señal proveniente de un sensor de alta impedancia (termopar, galga extensiométrica).

---

## ➖ Amplificador Diferencial — Rechazo de Modo Común

> [!note] ➖ El corazón del rechazo de ruido
> 
> Retomando lo anticipado en [[06 - Ruido Electrónico e Interferencia]]: si el ruido se acopla **por igual** a dos líneas de señal (modo común), un amplificador diferencial lo cancela porque solo amplifica la diferencia entre sus dos entradas.
> 
> $$v_o = \frac{R_2}{R_1}\cdot(v_2 - v_1)$$
> 
> - Toda tensión diferente entre las dos entradas se amplifica según la ganancia $R_2/R_1$.
>     
> - Toda señal **común** a ambas entradas (típicamente ruido de red, EMI) se cancela.
>     
> - Este comportamiento se cuantifica con la **razón de rechazo en modo común (CMRR)**: cuanto mayor, mejor cancela el ruido común.
>     
> 
> > 📌 Es la base de los sensores de instrumentación (termopares, galgas extensiométricas) mencionados en la guía de ejercicios, precisamente porque el ruido de la red eléctrica suele acoplarse igual a ambos cables de la señal del sensor.

---

## 🎚️ Amplificador de Instrumentación — Precisión con Alta Inmunidad

> [!note] 🎚️ Cuando un solo diferencial no basta
> 
> El amplificador diferencial simple tiene una limitación: su impedancia de entrada no es lo suficientemente alta para sensores muy sensibles, y ajustar su ganancia requiere cambiar dos resistencias a la vez. El **amplificador de instrumentación** resuelve esto con tres OPAMs:
> 
> - Dos seguidores/no inversores en la entrada (alta impedancia, ganancia ajustable con una sola resistencia).
> - Un amplificador diferencial a la salida (rechazo de modo común final).
> 
> $$V_O = \frac{R_3}{R_1}\cdot\left(1+\frac{2\cdot R_2}{R_G}\right)\cdot(V_2-V_1)$$
> 
> > 📌 Es la configuración estándar en instrumentación biomédica e industrial precisamente por su combinación de alta impedancia de entrada + alto CMRR — máxima inmunidad al ruido posible con OPAMs.

---

## 🌊 Filtros Activos — Extendiendo los Filtros Pasivos

> [!note] 🌊 Del filtro pasivo al filtro activo
> 
> En [[04 - Circuitos de Filtrado y Fuentes Lineales]] viste los filtros LPF/HPF pasivos (solo R, L, C). Combinando esas mismas redes RC con un OPAM en configuración inversora o no inversora se obtiene un **filtro activo**, con dos ventajas clave para reducir ruido:
> 
> |Ventaja del filtro activo|Efecto sobre el ruido|
> |---|---|
> |**Ganancia adicional** (no solo atenuación)|La señal útil se puede amplificar mientras se filtra el ruido fuera de banda|
> |**Baja impedancia de salida**|La etapa siguiente no carga ni degrada la respuesta del filtro|
> |**Sin bobinas**|Se evita el ruido y las pérdidas asociadas a inductores reales|
> 
> > 📌 Un integrador OPAM (visto en la guía de ejercicios) es, de hecho, un LPF activo de un polo: su respuesta atenúa las frecuencias altas — un mecanismo directo de "suavizado" de ruido de alta frecuencia sobre una señal de CD o baja frecuencia.

---

## 🔲 Comparador con Histéresis — Inmunidad en Señales Digitales

> [!note] 🔲 El problema del comparador simple frente al ruido
> 
> Un comparador ideal cambia de estado exactamente quando $v_i$ cruza un umbral. Pero si esa señal tiene ruido superpuesto cerca del umbral, el comparador puede **oscilar erráticamente** entre sus dos salidas mientras el ruido cruza el umbral varias veces.
> 
> El **comparador con histéresis** (Schmitt trigger) resuelve esto definiendo **dos umbrales distintos** (uno de subida, otro de bajada) mediante realimentación positiva, de modo que un pequeño ruido superpuesto ya no alcanza a provocar conmutaciones falsas.
> 
> ```mermaid
> graph LR
>     A["Señal ruidosa<br/>cerca del umbral"] --> B{Comparador simple}
>     A --> C{Comparador con histéresis}
>     B --> D["Salida oscila<br/>falsamente"]
>     C --> E["Salida estable<br/>una sola transición"]
> 
>     style D fill:#ffe1e1
>     style E fill:#e1ffe1
> ```
> 
> > 📌 Es la configuración recomendada siempre que una señal analógica ruidosa deba convertirse en una señal digital limpia — puente directo hacia el siguiente tema de esta unidad (555, ADC, PWM).

![[ChatGPT Image 22 jul 2026, 13_36_02.png]]

---

## 🧪 Ejercicio Práctico

> [!example]- ✏️ Ejercicio — Amplificador diferencial rechazando ruido de red
> 
> **Dato:** Un sensor entrega $v_1 = 2.000\text{ V}$ y $v_2 = 2.010\text{ V}$ (diferencia útil de 10 mV), pero ambas líneas recogen 50 mV de ruido de red idéntico (modo común). Se usa un amplificador diferencial con $R_1 = 1\text{ k}\Omega$, $R_2 = 100\text{ k}\Omega$.
> 
> |Paso|Acción|
> |---|---|
> |**1**|Señal diferencial real: $v_2-v_1 = 10\text{ mV}$ (el ruido de 50 mV es igual en ambas entradas, así que no aparece en la resta)|
> |**2**|Ganancia: $R_2/R_1 = 100\text{k}/1\text{k} = 100$|
> |**3**|$v_o = 100\times10\text{ mV} = 1\text{ V}$|
> |**4**|El ruido de modo común (50 mV en ambas líneas) **no aparece amplificado** en la salida — solo la diferencia útil de 10 mV se convierte en 1 V. Si en cambio se hubiera amplificado $v_1$ sola con un inversor de ganancia 100, el ruido de 50 mV se habría amplificado a 5 V, mucho mayor que la señal útil.|

---

## 📋 Ejercicios de la Tarea Autónoma #2 (Análisis Cuantitativo de Redes de OPAMs)

> [!info] 💡 Un tipo de ejercicio distinto: análisis de red, no solo concepto
>
> Los ejercicios anteriores de esta nota trabajan el **concepto** de cada configuración (para qué sirve frente al ruido). La Tarea Autónoma #2 exige además la **habilidad de análisis de circuitos**: aplicar $V_+\approx V_-$ e $I_+=I_-=0$ (ver diapositiva "Aspectos prácticos del Op-Amp", Sesión 12) para resolver redes de OPAMs en cascada con valores de resistencia concretos — la misma habilidad que evaluará el examen, según lo señalado en clase.
>
> [!example]- ✏️ Ejercicio 1 — Amplificador inversor con red de realimentación en T
>
> **Circuito:** $V_i$ a través de $R_1$ hacia la entrada inversora del OPAM. Realimentación en forma de **T**: $R_2$ desde la salida del nodo intermedio hasta la entrada inversora, $R_3$ del nodo intermedio a tierra, y $R_4$ del nodo intermedio hasta $V_o$.
>
> |Paso|Acción|
> |---|---|
> |**1**|Nodo inversor es tierra virtual ($V_-=0$). Toda la corriente que entra por $R_1$ ($i=V_i/R_1$) debe salir hacia el nodo intermedio $X$ a través de $R_2$ (no entra corriente al OPAM).|
> |**2**|KCL en el nodo inversor: $\dfrac{V_i}{R_1}+\dfrac{V_X}{R_2}=0 \Rightarrow V_X=-\dfrac{R_2}{R_1}V_i$|
> |**3**|KCL en el nodo intermedio $X$ (conectado a $R_2$, $R_3$ a tierra, y $R_4$ a $V_o$): $\dfrac{V_X}{R_2}+\dfrac{V_X}{R_3}+\dfrac{V_X-V_o}{R_4}=0$|
> |**4**|Despejando: $V_o = V_X\left(1+\dfrac{R_4}{R_2}+\dfrac{R_4}{R_3}\right)$|
> |**5**|Sustituyendo $V_X$ del paso 2:|
>
> $$\boxed{\dfrac{V_o}{V_i} = -\dfrac{R_2}{R_1}\left(1+\dfrac{R_4}{R_2}+\dfrac{R_4}{R_3}\right)}$$
>
> > 📌 Esta red en T logra **ganancias altas** sin necesitar una resistencia de realimentación físicamente enorme — muy usado cuando $R_2$ tendría que ser poco práctica de conseguir o generaría demasiado ruido térmico por su valor elevado.
>
> [!example]- ✏️ Ejercicio 2a — Diferencial de dos etapas (dos OPAMs)
>
> **Circuito:** Primera etapa (U1): $V_2$ a través de una resistencia $R$ hacia la entrada inversora, con realimentación $R$ (mismo valor) — inversor de ganancia unitaria. Segunda etapa (U2): suma inversora de $V_1$ (a través de $R_1$) y la salida de U1 (a través de otra $R_1$), con realimentación $R_2$.
>
> |Paso|Acción|
> |---|---|
> |**1**|Primera etapa (inversor, ganancia $-R/R=-1$): $V_{U1} = -V_2$|
> |**2**|Segunda etapa (sumador inversor con dos entradas, ambas por $R_1$, realimentación $R_2$): $V_o = -\dfrac{R_2}{R_1}(V_1+V_{U1})$|
> |**3**|Sustituyendo $V_{U1}=-V_2$: $V_o = -\dfrac{R_2}{R_1}(V_1-V_2)$|
>
> $$\boxed{V_o = \dfrac{R_2}{R_1}(V_2-V_1)}$$
>
> > 📌 Es el clásico **amplificador diferencial de dos OPAMs**: la primera etapa invierte una de las entradas para que la segunda pueda sumarlas y obtener la resta con una sola resistencia de ganancia ($R_2/R_1$) en vez de dos resistencias emparejadas como en el diferencial de un solo OPAM.
>
> [!warning] ⚠️ Ejercicio 2b — Pendiente de verificar topología
>
> El circuito de la Figura 3 (dos etapas con $V_1$ y $V_2$ conectadas cerca de las entradas no inversoras) no se pudo reconstruir con certeza a partir del archivo — las conexiones exactas de $R_2$, $R_1$ y $R_3$ en cada nodo no son legibles de forma confiable. **Antes de dar por válida cualquier fórmula, confírmame la conexión exacta** (qué resistencia va a qué pin de cada OPAM) y lo resuelvo con el mismo detalle que los demás.
>
> [!warning] ⚠️ Ejercicio 3 — Pendiente de verificar topología
>
> El circuito de tres etapas (U1:A, U1:B, U2:A) con $V_1=6\text{V}$, $V_2=11\text{V}$ y la incógnita $V_3$ tiene varias resistencias con etiquetas repetidas ($R_2$ aparece dos veces, con valores distintos posiblemente para realimentación y para polarización) que no pude distinguir con certeza en la imagen. El método general es:
>
> 1. Identificar la configuración de cada etapa (sumador inversor, inversor simple, etc.) según qué resistencias llegan a cada entrada inversora.
> 2. Resolver la salida de cada etapa en función de la anterior, igual que en el Ejercicio 2a.
> 3. Igualar la expresión final a $V_o=5.7\text{ V}$ y despejar $V_3$.
>
> **Confírmame qué resistencia conecta a qué pin** (especialmente las dos etiquetadas $R_2$, y a qué nodo llega $R_4$) y calculo el valor exacto de $V_3$.
>
> [!example]- ✏️ Ejercicio 4 — Cascada de inversor simple + sumador inversor
>
> **Circuito:** Primera etapa: $V_{s1}$ a través de $2R$ hacia la entrada inversora, realimentación $R$ — inversor de ganancia $-R/2R=-1/2$. Segunda etapa: suma inversora de la salida de la primera etapa (a través de $2R$) y $V_{s2}$ (a través de $0.5R$), con realimentación $2R$.
>
> |Paso|Acción|
> |---|---|
> |**1**|Primera etapa (inversor, ganancia $-R/2R=-0.5$): $V_{etapa1} = -0.5\,V_{s1}$|
> |**2**|Segunda etapa (sumador inversor): $V_{out} = -\dfrac{2R}{2R}V_{etapa1} - \dfrac{2R}{0.5R}V_{s2} = -V_{etapa1}-4V_{s2}$|
> |**3**|Sustituyendo $V_{etapa1}$: $V_{out} = 0.5\,V_{s1} - 4\,V_{s2}$|
> |**4**|Con $V_{s1}=5\text{ V}$, $V_{s2}=2.5\text{ V}$: $V_{out} = 0.5(5) - 4(2.5) = 2.5 - 10$|
>
> $$\boxed{V_{out} = -7.5\text{ V}}$$

---

## ✅ Metas de Aprendizaje

> [!note] 🎯 Nivel Básico
> 
> - [ ] Explico para qué sirve un seguidor de tensión frente al problema de carga (loading).
> - [ ] Explico qué significa "modo común" y por qué el amplificador diferencial lo rechaza.
> - [ ] Reconozco cuándo usar un comparador con histéresis en vez de uno simple.
>
> [!note] 🎯 Nivel Intermedio
> 
> - [ ] Calculo la salida de un amplificador diferencial dado el ruido de modo común y la señal diferencial útil.
> - [ ] Explico la ventaja de un amplificador de instrumentación (3 OPAMs) sobre un diferencial simple.
> - [ ] Relaciono el integrador OPAM con un filtro LPF activo.
>
> [!note] 🎯 Nivel Avanzado
> 
> - [ ] Diseño una cadena de acondicionamiento de señal (buffer + diferencial/instrumentación + filtro activo) para un sensor ruidoso dado.
> - [ ] Justifico la elección entre comparador simple y con histéresis según el nivel de ruido esperado en la señal de entrada.
> - [ ] Resuelvo redes de OPAMs en cascada (2 o 3 etapas) aplicando $V_+\approx V_-$ e $I_+=I_-=0$ nodo por nodo, identificando la configuración de cada etapa.

---

## 📊 Resumen Visual

```mermaid
mindmap
  root((OPAMs para<br/>Minimizacion de Ruido))
    Seguidor de tension
      Aislamiento de impedancias
    Amplificador diferencial
      Rechazo modo comun
      CMRR
    Amplificador instrumentacion
      3 OPAMs
      Alta impedancia + alto CMRR
    Filtros activos
      LPF/HPF con ganancia
      Integrador como LPF
    Comparador con histeresis
      Schmitt trigger
      Inmunidad a ruido cerca del umbral
    Analisis de redes en cascada
      Red en T
      Diferencial de 2 OPAMs
      Sumador inversor multi-etapa
```

---

> [!quote] 📖 Fuentes consultadas
> 
> [1] A. Sedra y K. Smith, _Microelectronic Circuits_, 7th ed. New York, USA: Oxford University Press, 2015 — capítulos sobre amplificadores operacionales y aplicaciones.
> 
> [2] R. L. Boylestad y L. Nashelsky, _Electrónica: Teoría de Circuitos y Dispositivos Electrónicos_, 10th ed. México: Pearson, 2009.
> 
> [3] Fco. Javier Hernández Canals, _Amplificador Operacional — Ejercicios Resueltos_ (guía de ejercicios: seguidor de tensión, amplificador diferencial, amplificador de instrumentación, comparador con histéresis).
>
> [4] Ing. Adriana Aguirre Alonso, _Tarea Autónoma #2 — Amplificadores Operacionales_, EYAG1037, FIEC-ESPOL, I PAO 2026.
>
> [!quote] 🔗 Conexiones
> 
> - [[06 - Ruido Electrónico e Interferencia]] — el concepto de rechazo de modo común anticipado ahí se desarrolla aquí con el amplificador diferencial.
> - [[04 - Circuitos de Filtrado y Fuentes Lineales]] — los filtros pasivos LPF/HPF se retoman aquí en su versión activa con OPAM.
> - [[01 - Introducción a los Circuitos Integrados No Programables]] — el OPAM como ejemplo central de CI no programable.
> - Siguiente nota: [[03 - Configuraciones Lineales Básicas del OPAM]] — inversores, sumadores y convertidores (base del PDF EjREsAmpOp).
> - Luego: [[04 - Integrador, Derivador y Circuitos No Lineales]] y [[05 - Ejercicios Resueltos y de Oposición]] — completan el PDF.
> - Después: [[06 - Aplicaciones de Integrados 555 - ADC - PWM]] — acondicionamiento con 555/ADC/PWM.

---

**Tags:** #amplificadorOperacional #minimizacionRuido #EYAG1037 #FESD #ESPOL #unidad3
