# 🤖 Sesgo y Gobernanza Algorítmica

## 🎯 Introducción

> [!info]- 💡 ¿Son los algoritmos neutrales?
> 
> Existe una creencia generalizada de que las matemáticas y los algoritmos son objetivos por naturaleza — que una máquina no puede ser racista, sexista o injusta. Esta idea es un **mito**.
> 
> Los algoritmos son diseñados por personas, entrenados con datos generados por personas, y desplegados en contextos sociales con historia. Todo eso introduce **sesgo**.
> 
> ```mermaid
> graph TD
>     A["Algoritmo"] --> B["¿De dónde viene el sesgo?"]
>     B --> C["Datos de entrenamiento"]
>     B --> D["Diseño del código"]
>     B --> E["Definición del problema"]
>     C --> C1["Datos históricos discriminatorios"]
>     C --> C2["Subrepresentación de grupos"]
>     D --> D1["Variables proxy discriminatorias"]
>     D --> D2["Métricas de éxito mal definidas"]
>     E --> E1["Quién define qué es un 'buen' resultado"]
> 
>     style A fill:#e1f5ff
>     style B fill:#ffe1e1
>     style C fill:#fff4e1
>     style D fill:#e1ffe1
>     style E fill:#f5e1ff
> ```

---

## ⚠️ Sesgo Algorítmico

> [!note]- 🔍 ¿Qué es el sesgo algorítmico?
> 
> El **sesgo algorítmico** es un error sistemático en un sistema computacional que produce resultados injustos, inequitativos o discriminatorios hacia ciertos grupos de personas.
> 
> A diferencia de un error aleatorio, el sesgo es **consistente y direccional** — siempre perjudica a los mismos grupos.
> 
> |Tipo de sesgo|Origen|Ejemplo|
> |---|---|---|
> |**Sesgo en los datos**|Los datos de entrenamiento reflejan desigualdades históricas|Un sistema entrenado con datos de contratación histórica aprende a discriminar mujeres si históricamente fueron menos contratadas|
> |**Sesgo de representación**|Ciertos grupos están subrepresentados en los datos|Un reconocedor facial entrenado mayormente con rostros de piel clara falla con piel oscura|
> |**Sesgo de proxy**|Se usan variables aparentemente neutras que correlacionan con raza o género|El código postal como variable de riesgo crediticio puede discriminar minorías étnicas|
> |**Sesgo de retroalimentación**|El sistema produce resultados sesgados que generan nuevos datos sesgados|Un algoritmo policial predice crimen en zonas ya vigiladas, generando más arrestos ahí, confirmando su propia predicción|

---

## 🧪 Casos de Estudio Históricos

> [!example]- 🤖 Tay — El chatbot racista de Microsoft (2016)
> 
> **Microsoft** lanzó **Tay**, un chatbot de IA en Twitter diseñado para aprender de las conversaciones con usuarios y simular el lenguaje de una joven de 19 años.
> 
> En menos de **24 horas**, usuarios coordinados en 4chan y Reddit lograron que Tay comenzara a publicar mensajes racistas, antisemitas y misóginos — simplemente alimentándolo con ese tipo de contenido de forma repetida.
> 
> |Dato|Detalle|
> |---|---|
> |**Plataforma**|Twitter|
> |**Lanzamiento**|23 de marzo de 2016|
> |**Tiempo hasta el problema**|Menos de 24 horas|
> |**Causa**|Sin filtros ni moderación en los datos de aprendizaje en tiempo real|
> |**Resultado**|Microsoft retiró Tay y lo desconectó|
> 
> > ⚠️ **Lección**: Un sistema de IA sin control sobre la calidad de sus datos de entrada puede ser manipulado activamente. El sesgo no siempre es accidental — puede ser inducido.

> [!example]- 🏥 St. George's Hospital — Sesgo en admisiones médicas (1970s–1988)
> 
> El **Hospital St. George's** en Londres usó un algoritmo computarizado para preseleccionar candidatos a su escuela de medicina desde los años 70 hasta **1988**, cuando fue descubierto y auditado.
> 
> El sistema había sido entrenado con decisiones históricas de admisión tomadas por humanos. Como resultado, **aprendió a discriminar** automáticamente:
> 
> - Penalizaba a candidatos con nombres de origen no europeo (presumiendo etnia)
> - Penalizaba a candidatos de género femenino
> 
> |Dato|Detalle|
> |---|---|
> |**Institución**|St. George's Hospital Medical School, Londres|
> |**Período**|~1979–1988|
> |**Descubrimiento**|Investigadores notaron patrones estadísticos anómalos|
> |**Causa**|Algoritmo entrenado con decisiones humanas históricamente sesgadas|
> |**Impacto**|Cientos de candidatos rechazados injustamente durante años|
> 
> > 💡 Este es uno de los primeros casos documentados de **discriminación algorítmica institucionalizada** — el sistema automatizó y escondió el sesgo humano, dándole apariencia de objetividad.

> [!example]- 📷 Reconocimiento facial — Google y Facebook (2015–2019)
> 
> Múltiples sistemas de reconocimiento facial desplegados por empresas tecnológicas mostraron tasas de error significativamente más altas en personas de piel oscura, especialmente mujeres negras.
> 
> **Casos documentados:**
> 
> |Empresa / Sistema|Problema|Año|
> |---|---|---|
> |**Google Photos**|Etiquetó automáticamente a personas negras como "gorilas"|2015|
> |**Facebook**|Tasa de error de reconocimiento facial 3x mayor en mujeres negras vs hombres blancos|2019|
> |**Amazon Rekognition**|Identificó erróneamente a 28 congresistas estadounidenses como criminales; mayoría de errores en personas no blancas|2018|
> |**MIT Media Lab (estudio)**|Tasa de error en clasificación de género: 0.8% en hombres de piel clara, 34.7% en mujeres de piel oscura|2018|
> 
> **Causa común**: Conjuntos de entrenamiento compuestos mayoritariamente por rostros de personas blancas de género masculino.

> [!example]- 💬 Sesgos de género en Procesamiento de Lenguaje Natural
> 
> Los modelos de lenguaje entrenados con texto humano absorben y amplifican los estereotipos de género presentes en ese texto.
> 
> **Ejemplos documentados:**
> 
> |Sistema|Sesgo observado|
> |---|---|
> |**Word2Vec (Google)**|Las asociaciones vectoriales colocaban "hombre" cerca de "ingeniero" y "mujer" cerca de "ama de casa"|
> |**Traductores automáticos**|Al traducir desde idiomas sin género gramatical (turco, húngaro), asignaban género masculino a profesiones de alto estatus y femenino a roles de cuidado|
> |**Sistemas de contratación (Amazon, 2018)**|Un sistema de selección de CVs desarrollado internamente penalizaba CVs que contenían la palabra "mujeres" (ej. "capitana del equipo femenino de debate")|
> 
> > 💡 Amazon descartó su sistema de contratación con IA en 2018 al descubrir estos sesgos — otro ejemplo de cómo el problema puede estar oculto hasta una auditoría explícita.

---

## 🏛️ Gobernanza Algorítmica

> [!important]- ⚖️ ¿Qué es la Gobernanza Algorítmica?
> 
> La **gobernanza algorítmica** es el conjunto de mecanismos — legales, técnicos, institucionales y éticos — para asegurar que los algoritmos que afectan a personas sean **transparentes, auditables, justos y responsables**.
> 
> El objetivo es que la automatización no elimine la rendición de cuentas: si un sistema toma una decisión que perjudica a alguien, debe haber un responsable humano identificable.
> 
> ```mermaid
> graph TD
>     G["Gobernanza Algorítmica"] --> T["Transparencia"]
>     G --> A["Auditoría"]
>     G --> R["Rendición de cuentas"]
>     G --> H["Factor humano"]
>     G --> L["Marco legal"]
> 
>     T --> T1["Explicabilidad de decisiones"]
>     T --> T2["Acceso al código y datos"]
>     A --> A1["Revisión independiente"]
>     A --> A2["Detección de sesgos"]
>     R --> R1["Responsable identificable"]
>     R --> R2["Derecho a recurrir"]
>     H --> H1["Humano en el loop"]
>     H --> H2["Revisión de casos límite"]
>     L --> L1["GDPR — Europa"]
>     L --> L2["Leyes de IA emergentes"]
> 
>     style G fill:#e1f5ff
>     style T fill:#e1ffe1
>     style A fill:#fff4e1
>     style R fill:#ffe1f5
>     style H fill:#f5e1ff
>     style L fill:#ffe1e1
> ```

> [!note]- 🔧 Principios de la Gobernanza Algorítmica
> 
> |Principio|Descripción|Ejemplo de aplicación|
> |---|---|---|
> |**Transparencia**|Los afectados por una decisión algorítmica deben poder entender cómo se tomó|Un banco debe explicar por qué un algoritmo rechazó un crédito|
> |**Explicabilidad**|El sistema debe poder justificar sus decisiones en términos comprensibles para humanos no técnicos|"Tu solicitud fue rechazada por historial de pagos" — no solo un número de riesgo|
> |**Auditabilidad**|Los algoritmos deben poder ser revisados por terceros independientes para detectar sesgos o errores|Auditores externos con acceso al código y los datos de entrenamiento|
> |**Rendición de cuentas**|Siempre debe haber un responsable humano o institucional identificable por las decisiones del sistema|No es aceptable decir "fue el algoritmo" para evadir responsabilidad|
> |**Factor humano**|En decisiones de alto impacto (salud, justicia, empleo), debe haber revisión humana obligatoria|Un juez, no solo un algoritmo, debe sentenciar a una persona|
> |**No discriminación**|Los sistemas no deben producir resultados sistemáticamente peores para grupos protegidos|Revisión estadística de tasas de error por género, etnia, edad|

> [!warning]- ⚖️ Marco legal y regulación emergente
> 
> |Regulación|Ámbito|Qué establece|
> |---|---|---|
> |**GDPR (2018)**|Unión Europea|Derecho a no ser sujeto de decisiones automatizadas con efectos significativos sin revisión humana|
> |**AI Act (2024)**|Unión Europea|Clasifica sistemas de IA por nivel de riesgo; los de alto riesgo (salud, justicia, empleo) requieren auditoría, transparencia y supervisión humana|
> |**Executive Order on AI (2023)**|EE.UU.|Mandato federal para evaluación de seguridad y sesgo en IA usada por agencias gubernamentales|
> |**Ley Orgánica de Protección de Datos**|Ecuador|Marco base de protección de datos personales, base para futura regulación de IA|
> 
> > 💡 Ecuador aún no tiene legislación específica sobre gobernanza algorítmica — es un campo en construcción en América Latina.

---

## 🔁 Sesgo y Gobernanza — La conexión

> [!summary]- 🔗 ¿Por qué la gobernanza es la respuesta al sesgo?
> 
> |Sin gobernanza|Con gobernanza|
> |---|---|
> |El sesgo se descubre tarde o nunca|Auditorías periódicas detectan sesgos antes de daño masivo|
> |No hay responsable del daño|Hay un responsable legal e institucional identificable|
> |Los afectados no tienen recurso|Existe derecho a impugnar decisiones automatizadas|
> |El algoritmo opera como caja negra|Transparencia permite revisión y mejora continua|
> |La IA reemplaza el juicio humano|La IA asiste al juicio humano sin eliminarlo|

---

**Tags:** #computacion-y-sociedad #unidad2 #sesgo-algoritmico #gobernanza-algorítmica #IA #etica #ESPOL