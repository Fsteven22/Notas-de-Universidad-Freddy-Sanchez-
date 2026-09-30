---
dg-publish: true
---

# 🧪 Práctica 4 — Funcionamiento de Fuentes Lineales

## 🎯 Introducción

> [!info] 💡 ¿Por qué esta práctica es importante?
>
> Una fuente lineal convierte la corriente alterna de la red (110 VAC) en un voltaje DC estable. Tiene **4 etapas funcionales**: transformador reductor, rectificador de onda completa, filtro capacitivo y regulador LM7805. En esta práctica identificas cada etapa y mides las formas de onda en cada punto.
>
> ```mermaid
> graph LR
>     A[110 VAC<br/>Red] --> B[Transformador<br/>110V/12V]
>     B --> C[Rectificador<br/>Puente de diodos]
>     C --> D[Filtro<br/>Capacitivo]
>     D --> E[Regulador<br/>LM7805]
>     E --> F[5 VDC<br/>Salida]
>     style A fill:#ffe1e1
>     style B fill:#e1f5ff
>     style C fill:#e1ffe1
>     style D fill:#fff4e1
>     style E fill:#f5e1ff
>     style F fill:#e1ffe1
> ```

---

## ⚠️ Seguridad

> [!danger]
> - Manipula el transformador TX 110 V/12 V **solo con supervisión del profesor**.
> - Trabaja con la fuente apagada al modificar conexiones.
> - El LM7805 se calienta — usa disipador.

---

## 🧰 Materiales

> [!note] 📦 Materiales necesarios
>
> | Material | Especificación |
> |---|---|
> | Multímetro | FLUKE 179 |
> | Generador de funciones |  |
> | Osciloscopio | GW INSTEK |
> | Diodo | 1N4007 (puente) |
> | Regulador | LM7805 con disipador |
> | Capacitores | 1000 µF, 470 µF, 1 µF |
> | Resistencia | 1 KΩ, 0.5 W |
> | Transformador | TX 110 V/12 V, 2 A |
> | Potenciómetro | 1 KΩ |
> | Cables | banana–banana |

---

## 📖 Introducción Teórica

> [!note] 🔵 Transformador reductor
>
> Reduce voltajes de 170 Vp (red) a voltajes menores. Relación:
>
> $$\frac{V_1}{V_2} = a$$
>
> Si el primario es 110 Vrms, el secundario es ~15 Vrms = ~21 Vp, usando $V_{rms} = V_p / \sqrt{2}$.
>
> [!note] 🟢 Rectificador de onda completa
>
> Con 4 diodos (puente), refleja todos los semiperiodos negativos al lado positivo. Durante semipositivos conducen D1 y D4; durante sinegativos, D2 y D3. Salida pulsante entre 0 y 21 V.
>
> [!note] 🟡 Filtro capacitivo
>
> Disminuye el rizado. A mayor capacitancia, menor $V_{pp}$ de rizado. El valor de C tiene un efecto inversamente proporcional sobre el voltaje pico a pico de la señal pulsante.
>
> [!note] 🔵 Regulador LM7805
>
> Fija la salida en **5 Vdc** a partir de un voltaje no regulado (~19.5 Vdc). Maneja hasta 1 A. Caída de tensión típica ~3 V. Si la caída es muy grande (como ~14 V en esta práctica), la carga debe ser pequeña para no dañar el integrado.

---

## ⚙️ Procedimiento S — Regulador de Voltaje Variable

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con potenciómetro y medir voltaje de salida.
> 2. Ajustar el potenciómetro en 0 KΩ, 0.2 KΩ, 0.5 KΩ, 0.7 KΩ y 1 KΩ.
> 3. Medir voltaje de salida en cada posición.
>
> [!note] 📊 Tabla 1 — Regulador variable
>
> |Ajuste del Potenciómetro|Voltaje de salida $V_o$ (V)|
> |---|---|
> |0 KΩ| |
> |0.2 KΩ| |
> |0.5 KΩ| |
> |0.7 KΩ| |
> |1 KΩ| |

---

## ⚙️ Procedimiento — Fuente Regulada con LM7805

> [!tip] 🔧 Pasos
>
> 1. Armar circuito con TX, puente de diodos, capacitor y LM7805.
> 2. Medir con CH1 del osciloscopio el voltaje del capacitor (entrada al regulador).
> 3. Con CH2 medir el voltaje en la resistencia R1 (salida regulada).
> 4. Completar la tabla.
>
> [!note] 📊 Tabla 2 — Fuente regulada
>
> |Parámetro|Valor|
> |---|---|
> |$V_{pp}$ onda rizada (antes del regulador)| |
> |Factor de rizado medido| |
> |Voltaje DC de la carga (salida)| |
>
> [!question]- ❓ Análisis
>
> - ¿Cuál es la caída de tensión típica que necesita el LM7805 para funcionar? (Consultar datasheet)
> - ¿Qué es el factor de rizado y qué efecto tiene el capacitor antes del regulador?
> - Completar tabla de reguladores:
>
> [!note] 📊 Tabla comparativa de reguladores
>
> |Regulador|Voltaje de salida|Carga máxima|
> |---|---|---|
> |LM7912| | |
> |LM7915| | |
> |LM317| | |

---

## 📝 Notas personales

> [!question]- 🤔 Mis observaciones
>
> - Diferencias teórico vs medido:
> - Errores encontrados:
> - Dudas para el informe:

---

## 📄 Informe

> Usa [[FORMATO INFORME DE PRÁCTICA.pdf]] y [[Formato Pre-prácticas.pdf]] para entregar.

## Metas de Aprendizaje

> [!note] Nivel Básico
> - [ ] Identifico las 4 etapas de una fuente lineal (transformador, rectificador, filtro, regulador) en el diagrama de bloques.
> - [ ] Uso el osciloscopio para observar la forma de onda antes y después del rectificador de onda completa.
> - [ ] Verifico que los semiperiodos negativos se reflejan al positivo gracias a los 4 diodos del puente.
>
> [!note] Nivel Intermedio
> - [ ] Mido el voltaje rizado del capacitor y calculo el factor de rizado ($V_{pp}/V_{dc}$).
> - [ ] Observo cómo el capacitor de 1000 µF reduce el rizado vs uno de 470 µF.
> - [ ] Mido la salida del LM7805 y confirmo que es estable en 5 Vdc.
>
> [!note] Nivel Avanzado
> - [ ] Explico la caída de tensión necesaria (~3 V típica) para que el LM7805 regule correctamente.
> - [ ] Diferencio entre una fuente regulada (LM7805) y no regulada (solo capacitor) midiendo ambas salidas.
> - [ ] Identifico en qué condiciones el LM7805 puede dañarse (caída de tensión excesiva sin carga adecuada).
>
> [!quote] 🔗 Conexiones
> - Teoría: [[02 - El Diodo - Unión P-N]], [[04 - Circuitos de Filtrado y Fuentes Lineales]] y [[05 - Reguladores en Fuentes Lineales]]
> - Previa: [[Práctica 3 — Diodos y Transistores]]
> - Siguiente: [[Práctica 5 — Filtros Activos]]

---

---

## 📎 Guía oficial (Garden)

![[Práctica # 4Funcionamiento de Fuentes Lineales.pdf]]
**Tags:** #practica #laboratorio #EYAG1037 #FESD #ESPOL #unidad2 #fuentesLineales #LM7805 #rectificador
