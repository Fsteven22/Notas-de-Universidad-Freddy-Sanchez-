---
dg-publish: true
---

# Tensión Superficial 💧

>[!quote] *"Una gota de agua es tan perfecta como el universo. Su superficie curva revela el misterio de las fuerzas moleculares que actúan en la frontera entre dos mundos."* - Leonardo da Vinci (interpretación moderna)

---

## 📋 Conceptos Fundamentales

>[!info] 🎯 **Definición de Tensión Superficial**
>La tensión superficial es la fuerza cohesiva que actúa en la superficie de un líquido, causada por las interacciones moleculares desbalanceadas en la interfase líquido-gas. Se manifiesta como una tendencia del líquido a minimizar su área superficial.
>
>**Características principales:**
>- **Fuerza por unidad de longitud:** Se mide en N/m o dyn/cm
>- **Energía por unidad de área:** También en J/m²
>- **Origen molecular:** Fuerzas intermoleculares (Van der Waals, puentes de hidrógeno)
>- **Efecto macroscópico:** Comportamiento como "piel elástica"
>
>**Símbolo:** γ (gamma) o σ (sigma)
>**Unidades SI:** N/m = J/m²
>
>[!info] 🔬 **Origen Molecular**
>En el interior del líquido, cada molécula está rodeada por otras moléculas y las fuerzas de atracción se equilibran. En la superficie, las moléculas tienen menos vecinos, creando un desbalance de fuerzas hacia el interior del líquido.
>
>```mermaid
>graph TD
>    A[Molécula en el interior] --> B[Fuerzas balanceadas]
>    C[Molécula en la superficie] --> D[Fuerzas desbalanceadas]
>    B --> E[Σ \vec{F} = 0]
>    D --> F[Fuerza neta hacia el interior]
>    F --> G[Tendencia a minimizar área]
>    G --> H[Tensión superficial]
>    style A fill:#e1f5fe
>    style C fill:#f3e5f5
>    style H fill:#fff3e0
>```

## 🔢 Propiedades y Características

>[!tip] 📊 **Valores Típicos de Tensión Superficial**
>A 20°C en contacto con aire:
>
>| Líquido | γ (N/m) | γ (dyn/cm) |
>|---------|---------|------------|
>| **Agua** | 0.0728 | 72.8 |
>| **Mercurio** | 0.486 | 486 |
>| **Alcohol etílico** | 0.0223 | 22.3 |
>| **Glicerina** | 0.0634 | 63.4 |
>| **Aceite de oliva** | 0.0320 | 32.0 |
>| **Benceno** | 0.0289 | 28.9 |
>
>**Factores que afectan γ:**
>- **Temperatura:** γ disminuye al aumentar T
>- **Impurezas:** Surfactantes reducen γ
>- **Presión:** Efecto mínimo en líquidos
>- **Naturaleza química:** Polaridad molecular
>
>[!tip] 🌡️ **Dependencia con la Temperatura**
>La tensión superficial generalmente disminuye linealmente con la temperatura:
>$$\gamma(T) = \gamma_0 - k(T - T_0)$$
>
>Donde:
>- γ₀ = tensión superficial a temperatura de referencia T₀
>- k = constante específica del líquido (pendiente)
>
>**Para el agua:**
>$$\gamma_{agua}(T) = 0.0757 - 1.5 \times 10^{-4}(T - 0°C)$$

## ⚖️ Ecuaciones Fundamentales

>[!warning] 🧮 **Ecuaciones Básicas**
>
>**1. Definición por fuerza:**
>$$\gamma = \frac{F}{L}$$
>Donde F es la fuerza perpendicular a una línea de longitud L en la superficie
>
>**2. Definición por energía:**
>$$\gamma = \frac{dU}{dA}$$
>Donde U es la energía superficial y A el área superficial
>
>>[!warning]- 📐 **Interpretación del Factor 2 en γ = F/2L**
>
>**¿Por qué F/2L y no F/L?**
>
>La confusión surge del contexto del experimento:
>
>**Experimento de marco móvil:**
>- Un marco rectangular con un lado móvil
>- Una película de líquido se extiende en el marco
>- Al mover el lado, se crea área $$dA = L \, dx$$
>- **Pero:** la película tiene DOS superficies (superior e inferior)
>- **Área total creada:** $$dA_{total} = 2L \, dx$$
>- **Por tanto:** $$\gamma = \frac{F}{2L}$$
>
>**Casos según el contexto:**
>- **Película de jabón:** $$\gamma = \frac{F}{2L}$$ (dos superficies)
>- **Interfase simple:** $$\gamma = \frac{F}{L}$$ (una interfase)
>- **Método energético:** $$\gamma = \frac{dW}{dA}$$ (siempre válido)
>- **Burbuja esférica:** $$\Delta P = \frac{4\gamma}{R}$$
>- **Gota esférica:** $$\Delta P = \frac{2\gamma}{R}$$
>- **Superficie cilíndrica:** $$\Delta P = \frac{\gamma}{R}$$
>
>**3. Presión adicional en burbujas (Ley de Young-Laplace):**
>**4. Altura de ascenso capilar:**
$$h = \frac{2\gamma\cos\theta}{\rho g r}$$

**5. Relación trabajo-energía superficial:**
$$dW = \gamma \, dA$$
Esta es la forma más fundamental, donde el trabajo infinitesimal para crear área superficial dA es proporcional a γ.

## 📋 Fenómenos Relacionados

>[!example] 💧 **Capilaridad**
>**Definición:** Ascenso o descenso de un líquido en tubos estrechos debido a la tensión superficial y las fuerzas de adhesión/cohesión.
>
>**Ecuación de ascenso capilar:**
>$$h = \frac{2\gamma\cos\theta}{\rho g r}$$
>
>Donde:
>- h = altura de ascenso (positiva) o descenso (negativa)
>- θ = ángulo de contacto
>- ρ = densidad del líquido
>- g = aceleración gravitacional
>- r = radio del capilar
>
>**Casos especiales:**
>- **Agua en vidrio:** θ ≈ 0°, cos θ ≈ 1 (asciende)
>- **Mercurio en vidrio:** θ ≈ 140°, cos θ < 0 (desciende)
>
>[!example] 🫧 **Formación de Burbujas y Gotas**
>**Burbujas de jabón:**
>- **Una superficie:** $$\Delta P = \frac{2\gamma}{R}$$
>- **Dos superficies:** $$\Delta P = \frac{4\gamma}{R}$$
>
>**Gotas de lluvia:**
>- Forma esférica para minimizar energía superficial
>- Radio de curvatura relacionado con presión interna
>- Deformación por resistencia del aire al caer
>
>[!example] 🌊 **Ondas Capilares**
>Ondas en la superficie de líquidos donde la tensión superficial es la fuerza restauradora dominante.
>
>**Velocidad de onda capilar:**
>$$v = \sqrt{\frac{2\pi\gamma}{\rho\lambda}}$$
>
>Donde λ es la longitud de onda.

## 🧠 Técnica de Estudio: Método GOTA

>[!tip] 🎓 **Estrategia de Aprendizaje: Mnemotecnia GOTA**
>Para problemas de tensión superficial usa el método **GOTA**:
>
>**G - Geometría** identificar la forma de la superficie (esfera, cilindro, plano)
>**O - Origen** determinar si es capilaridad, burbuja, o interfase plana
>**T - Tensión** usar el valor correcto de γ para el líquido específico
>**A - Aplicar** la ecuación correspondiente según la geometría
>
>**Tabla de decisión:**
>
>| Fenómeno | Geometría | Ecuación Principal |
>|----------|-----------|-------------------|
>| **Capilaridad** | Cilindro | $$h = \frac{2\gamma\cos\theta}{\rho g r}$$ |
>| **Burbuja jabón** | Esfera | $$\Delta P = \frac{4\gamma}{R}$$ |
>| **Gota líquido** | Esfera | $$\Delta P = \frac{2\gamma}{R}$$ |
>| **Interfase plana** | Plano | $$F = \gamma L$$ |

## 🧪 Experimentos y Aplicaciones

>[!example] 🔬 **Métodos de Medición**
>
>**1. Método del anillo de Du Noüy:**
>- Medir la fuerza necesaria para desprender un anillo de la superficie
>- $$\gamma = \frac{F}{4\pi R}$$ (aproximado)
>
>**2. Método de la gota pendiente:**
>- Analizar la forma de una gota colgante
>- Usar análisis digital de imagen
>
>**3. Método del ascenso capilar:**
>- Medir altura de ascenso en tubo capilar
>- Aplicar ecuación de ascenso capilar
>
>**4. Método de la placa de Wilhelmy:**
>- Medir fuerza sobre placa parcialmente sumergida
>- $$\gamma = \frac{F}{P\cos\theta}$$ donde P es el perímetro
>
>[!example] 🏭 **Aplicaciones Industriales**
>
>**Detergentes y surfactantes:**
>- Reducen la tensión superficial del agua
>- Mejoran la capacidad de mojado y limpieza
>- $$\gamma_{solución} < \gamma_{agua}$$
>
>**Flotación de minerales:**
>- Separación de minerales por diferencias en mojabilidad
>- Control de tensión superficial con reactivos químicos
>
>**Impresión y recubrimientos:**
>- Control de esparcimiento de tintas y pinturas
>- Uniformidad de películas delgadas

## 🌿 Fenómenos Biológicos

>[!info] 🦎 **Tensión Superficial en la Naturaleza**
>
>**Insectos caminando sobre el agua:**
>- Los patinadores de agua distribuyen su peso
>- Patas hidrofóbicas no rompen la superficie
>- $$F_{tensión} > mg$$ (condición para no hundirse)
>
>**Alvéolos pulmonares:**
>- Surfactante pulmonar reduce tensión superficial
>- Previene colapso alveolar durante espiración
>- $$\gamma_{con\ surfactante} << \gamma_{agua}$$
>
>**Plantas y transporte de agua:**
>- Tensión superficial ayuda en el transporte xilemático
>- Cohesión del agua en tubos capilares microscópicos
>- Combinado con transpiración y presión de raíz

## 🧪 Problemas Resueltos

>[!example] 💡 **Problema 1: Ascenso Capilar**
>Un tubo capilar de vidrio limpio con radio interno de 0.5 mm se introduce en agua a 20°C. ¿Qué altura alcanza el agua? (γ = 0.0728 N/m, ρ = 1000 kg/m³, θ ≈ 0°)
>
>**Solución:**
>$$h = \frac{2\gamma\cos\theta}{\rho g r}$$
>
>$$h = \frac{2 \times 0.0728 \times \cos(0°)}{1000 \times 9.81 \times 0.0005}$$
>
>$$h = \frac{2 \times 0.0728 \times 1}{4.905} = \frac{0.1456}{4.905} = 0.0297 \text{ m} = 2.97 \text{ cm}$$
>
>[!example] 💡 **Problema 2: Presión en Burbuja de Jabón**
>Una burbuja de jabón tiene un diámetro de 4 cm. Si la tensión superficial del agua jabonosa es 0.025 N/m, ¿cuál es la presión manométrica dentro de la burbuja?
>
>**Solución:**
>Para burbuja de jabón (dos superficies):
>$$\Delta P = \frac{4\gamma}{R}$$
>
>Radio: $$R = \frac{d}{2} = \frac{0.04}{2} = 0.02 \text{ m}$$
>
>$$\Delta P = \frac{4 \times 0.025}{0.02} = \frac{0.1}{0.02} = 5 \text{ Pa}$$
>
>[!example] 💡 **Problema 3: Fuerza en Interfase**
>¿Qué fuerza se necesita para desprender una lámina rectangular de 5 cm × 2 cm de la superficie del agua? (γ = 0.0728 N/m)
>
>**Solución:**
>La fuerza actúa solo en el perímetro que está en contacto con la superficie:
>$$F = \gamma \times L_{perímetro}$$
>
>$$L_{perímetro} = 2 \times (0.05 + 0.02) = 2 \times 0.07 = 0.14 \text{ m}$$
>
>$$F = 0.0728 \times 0.14 = 0.0102 \text{ N} = 10.2 \text{ mN}$$

## 🔍 Referencias y Conexiones

>[!quote] 📚 **Referencias a otras notas**
>- [[Hidrostática e Hidrodinámica]] - Contexto de mecánica de fluidos
>- [[Fuerzas Intermoleculares]] - Origen microscópico del fenómeno
>- [[Termodinámica de Superficies]] - Aspectos energéticos
>- [[Ecuación de Continuidad y Bernoulli]] - Flujo con efectos superficiales
>- [[Presión y Densidad 1]] - Conceptos fundamentales relacionados

## 📖 Notas Recomendadas para Complementar

>[!info] 🎯 **Prerrequisitos y Temas Relacionados**
>
>**Prerrequisitos esenciales:**
>- [[Presión y Densidad 1]] - Conceptos fundamentales de fluidos
>- [[Fuerzas y Equilibrio]] - Para análisis de fuerzas en superficies
>- [[Geometría]] - Para cálculos de áreas y volúmenes
>- [[Trigonometría]] - Para ángulos de contacto
>
>**Temas complementarios:**
>- [[El Principio de Pascal]] - Transmisión de presión en fluidos
>- [[El Principio de Arquímedes]] - Flotación y empuje
>- [[Viscosidad]] - Otra propiedad importante de los fluidos
>- [[Termodinámica]] - Aspectos energéticos de las superficies

## 🔧 Técnicas Experimentales

>[!tip] 🛠️ **Consejos para Experimentos**
>
>**Limpieza crítica:**
>- Lavar toda la cristalería con detergente y enjuagar abundantemente
>- Evitar residuos de grasa que alteran los resultados
>- Usar agua destilada para mediciones precisas
>
>**Control de temperatura:**
>- La tensión superficial varía significativamente con T
>- Permitir equilibrio térmico antes de medir
>- Registrar temperatura ambiente
>
>**Minimizar vibraciones:**
>- Las ondas superficiales afectan las mediciones
>- Usar superficies estables y aisladas
>- Esperar que la superficie se calme

---

**Tags:** #fisica-mecanica #hidrostática #tension-superficial #capilaridad #burbujas #fuerzas-intermoleculares #fenomenos-superficiales #fluidos
