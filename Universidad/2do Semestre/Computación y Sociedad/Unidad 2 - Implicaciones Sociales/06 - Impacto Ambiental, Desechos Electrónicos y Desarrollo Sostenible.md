# 🌱 Impacto Ambiental, Desechos Electrónicos y Desarrollo Sostenible

## 🎯 Introducción

> [!info]- 💡 La huella ecológica de la tecnología
> 
> Cada dispositivo electrónico que usamos tiene un ciclo de vida con impacto ambiental en todas sus etapas: fabricación, uso y descarte. La tecnología que conecta al mundo también genera una de las corrientes de residuos de más rápido crecimiento en la historia.
> 
> ```mermaid
> graph LR
>     A["Ciclo de vida<br>de un dispositivo"] --> B["Fabricación"]
>     A --> C["Uso"]
>     A --> D["Descarte"]
>     B --> B1["Extracción de minerales<br>Emisiones de CO2<br>Agua utilizada"]
>     C --> C1["Consumo eléctrico<br>Calor generado<br>Actualizaciones forzadas"]
>     D --> D1["E-waste<br>Metales tóxicos<br>Exportación de residuos"]
> 
>     style A fill:#e1f5ff
>     style B fill:#ffe1e1
>     style C fill:#fff4e1
>     style D fill:#ffe1e1
> ```

---

## 🗑️ Chatarra Electrónica — E-waste

> [!warning]- 📊 Estadísticas alarmantes
> 
> Los **desechos electrónicos** (_e-waste_) son la corriente de residuos de más rápido crecimiento a nivel mundial. Incluyen todo dispositivo eléctrico o electrónico descartado: teléfonos, computadoras, televisores, electrodomésticos, baterías.
> 
> |Dato|Cifra|
> |---|---|
> |**Residuos generados globalmente (2019)**|~53.6 millones de toneladas métricas|
> |**Proyección para 2030**|~74 millones de toneladas métricas|
> |**Porcentaje reciclado formalmente**|Solo ~17% se gestiona de forma documentada|
> |**Valor económico de los materiales**|Estimado en $57 mil millones USD anuales desperdiciados|
> 
> > ⚠️ El resto — más del 80% — termina en vertederos, incineradoras o es exportado informalmente hacia países en desarrollo.

> [!note]- 📱 Composición de un teléfono móvil descartado
> 
> Un teléfono promedio contiene materiales tanto valiosos como peligrosos:
> 
> |Material|Porcentaje aproximado|Característica|
> |---|---|---|
> |**Plásticos**|~45%|Reciclable pero de baja pureza|
> |**Cobre y otros metales base**|~20%|Alto valor de recuperación|
> |**Vidrio y cerámica**|~20%|Reciclable con procesos específicos|
> |**Metales preciosos** (oro, plata, paladio)|~5%|Muy alto valor — 1 tonelada de teléfonos tiene más oro que 1 tonelada de mineral aurífero|
> |**No especificado / compuestos**|~10%|Mezcla de adhesivos, soldaduras y materiales difíciles de separar|
> 
> > 💡 El 10% no especificado refleja la complejidad real de la composición — los fabricantes no divulgan todos los materiales, lo que dificulta el reciclaje eficiente.

> [!danger]- ☠️ Componentes peligrosos
> 
> Muchos dispositivos electrónicos contienen **metales pesados y sustancias tóxicas** que, al ser descartados de forma inadecuada, contaminan suelo, agua y aire:
> 
> |Sustancia|Presente en|Efecto en la salud|
> |---|---|---|
> |**Plomo (Pb)**|Soldaduras, pantallas CRT|Daño neurológico, especialmente en niños|
> |**Mercurio (Hg)**|Pantallas LCD, interruptores|Daño renal y neurológico, bioacumulable en peces|
> |**Cadmio (Cd)**|Baterías recargables, circuitos|Daño renal, carcinógeno|
> |**Cromo hexavalente**|Recubrimientos metálicos|Carcinógeno, daño al ADN|
> |**Retardantes de llama bromados**|Carcasas plásticas, placas|Disruptores endocrinos, tóxicos al incinerar|

> [!warning]- 🚢 El flujo global de e-waste
> 
> Una fracción importante de los desechos electrónicos generados en países desarrollados es **exportada hacia Asia y América Latina**, muchas veces de forma ilegal o bajo etiquetas engañosas como "donaciones" o "equipos usados".
> 
> ```mermaid
> graph LR
>     A["Países desarrollados<br>EE.UU · Europa · Japón"] -->|"Exportación formal<br>e informal"| B["Asia<br>China · India · Ghana"]
>     A -->|"Flujo regional"| C["América Latina<br>Ecuador · Perú · Brasil"]
>     B --> D["Desmantelamiento<br>informal"]
>     C --> D
>     D --> E["Exposición tóxica<br>en trabajadores"]
>     D --> F["Contaminación de<br>suelo y agua"]
> 
>     style A fill:#e1f5ff
>     style D fill:#ffe1e1
>     style E fill:#ffe1e1
>     style F fill:#ffe1e1
> ```
> 
> > ⚠️ El Convenio de Basilea (1989) prohíbe la exportación de residuos peligrosos a países en desarrollo, pero su cumplimiento es limitado.

---

## ♻️ Green ICT — Tecnología Verde

> [!note]- 🌿 ¿Qué es Green ICT?
> 
> **Green ICT** (Tecnologías de la Información y Comunicación Verdes) es el enfoque que busca minimizar el impacto ambiental de la tecnología a lo largo de todo su ciclo de vida — desde el diseño hasta el descarte.
> 
> |Estrategia|Descripción|
> |---|---|
> |**Eficiencia energética**|Diseñar hardware y software que consuma menos electricidad — procesadores más eficientes, modos de bajo consumo|
> |**Energías renovables en data centers**|Usar energía solar, eólica o hidroeléctrica para alimentar los servidores que sostienen internet|
> |**Videoconferencias en lugar de viajes**|Reducir emisiones de CO2 asociadas a viajes de negocios mediante reuniones virtuales|
> |**Reparación en lugar de sustitución**|Extender la vida útil de los dispositivos — repararlos en vez de descartarlos al primer fallo|
> |**Diseño para el desmontaje**|Fabricar equipos que puedan desarmarse fácilmente para recuperar materiales al final de su vida|

> [!important]- 🔄 Economía Circular aplicada a la tecnología
> 
> El modelo tradicional es **lineal**: extraer → fabricar → usar → descartar. La **Economía Circular** propone cerrar ese ciclo:
> 
> ```mermaid
> graph TD
>     A["Diseño sostenible"] --> B["Fabricación<br>responsable"]
>     B --> C["Uso prolongado"]
>     C --> D["Reparación<br>y reutilización"]
>     D --> C
>     C --> E["Reciclaje<br>de materiales"]
>     E --> A
>     C -->|"modelo lineal"| F["🗑️ Vertedero"]
> 
>     style A fill:#e1ffe1
>     style B fill:#e1ffe1
>     style C fill:#e1f5ff
>     style D fill:#e1ffe1
>     style E fill:#e1ffe1
>     style F fill:#ffe1e1
> ```
> 
> **Principios clave:**
> 
> |Principio|Aplicación en tecnología|
> |---|---|
> |**Reducir**|Comprar solo lo necesario, evitar la obsolescencia programada|
> |**Reutilizar**|Donar equipos funcionales, mercado de segunda mano|
> |**Reparar**|Talleres de reparación, derecho a reparar (_Right to Repair_)|
> |**Reciclar**|Entregar en puntos de acopio certificados para recuperar materiales|

> [!tip]- 🇪🇨 Iniciativas en Ecuador
> 
> Ecuador cuenta con programas concretos para la gestión de e-waste:
> 
> |Iniciativa|Descripción|
> |---|---|
> |**Puntos de reciclaje Claro**|Acopio de celulares, accesorios y baterías en tiendas a nivel nacional|
> |**Puntos de reciclaje Movistar**|Recepción de dispositivos móviles en desuso para gestión responsable|
> |**"Ponte Pilas — RecoPila"**|Programa del Ministerio del Ambiente para recolección de pilas y baterías usadas en escuelas, municipios y puntos fijos|
> |**REEE Ecuador**|Marco regulatorio del Ministerio del Ambiente para la gestión de Residuos de Equipos Eléctricos y Electrónicos|
> 
> > 💡 La participación ciudadana es clave — llevar dispositivos a estos puntos en vez de botarlos a la basura común marca una diferencia real.

---

## 🌍 Desarrollo Sostenible

> [!important]- 📖 Definición y origen
> 
> El **Desarrollo Sostenible** fue definido por la Comisión Brundtland de la ONU en 1987 como:
> 
> > _"El desarrollo que satisface las necesidades del presente sin comprometer la capacidad de las generaciones futuras para satisfacer sus propias necesidades."_
> 
> Se apoya en tres pilares interdependientes:
> 
> ```mermaid
> graph TD
>     DS["Desarrollo Sostenible"] --> EC["🌱 Ambiental"]
>     DS --> SO["🤝 Social"]
>     DS --> EC2["💰 Económico"]
>     EC --- SO
>     SO --- EC2
>     EC2 --- EC
>     EC --> EC1["Proteger ecosistemas<br>Reducir emisiones<br>Gestionar residuos"]
>     SO --> SO1["Equidad<br>Salud<br>Educación"]
>     EC2 --> EC3["Crecimiento<br>Empleo<br>Innovación"]
> 
>     style DS fill:#e1f5ff
>     style EC fill:#e1ffe1
>     style SO fill:#fff4e1
>     style EC2 fill:#f5e1ff
> ```

> [!note]- 🎯 Los 17 Objetivos de Desarrollo Sostenible (ODS) — ONU 2030
> 
> En 2015, la ONU aprobó la **Agenda 2030** con 17 ODS como hoja de ruta global para erradicar la pobreza, proteger el planeta y garantizar prosperidad para todos.
> 
> |#|Objetivo|Relación con la tecnología|
> |---|---|---|
> |**1**|Fin de la pobreza|Acceso digital como herramienta de inclusión económica|
> |**2**|Hambre cero|Agricultura de precisión, cadenas de suministro optimizadas|
> |**3**|Salud y bienestar|Telemedicina, registros médicos digitales, diagnóstico con IA|
> |**4**|Educación de calidad|MOOCs, plataformas de aprendizaje, reducción de brecha educativa|
> |**5**|Igualdad de género|Combatir sesgos algorítmicos, acceso igualitario a tecnología|
> |**7**|Energía asequible y no contaminante|Eficiencia energética en hardware, energías renovables en data centers|
> |**9**|Industria, innovación e infraestructura|Internet como infraestructura crítica, innovación tecnológica|
> |**10**|Reducción de desigualdades|Reducir brecha digital entre países y dentro de ellos|
> |**11**|Ciudades sostenibles|Smart cities, transporte eficiente, gestión inteligente de recursos|
> |**12**|Producción y consumo responsables|Economía circular, reducción de e-waste, diseño sostenible|
> |**13**|Acción por el clima|Reducir huella de carbono del sector TIC|
> |**17**|Alianzas para los objetivos|Cooperación internacional en estándares de reciclaje y gobernanza digital|
> 
> > 💡 Los ODS más directamente relacionados con el impacto de la tecnología son el **12** (producción responsable) y el **13** (acción climática) — pero prácticamente todos tienen una dimensión digital.

---

## 📋 Trabajos Grupales

> [!tip]- 👥 Pautas para las tareas grupales de la unidad
> 
> Al finalizar esta unidad se deben realizar dos trabajos en grupo:
> 
> **Trabajo 1 — Análisis de brecha digital de un país** Investigar y presentar la situación de acceso y uso de tecnología en un país asignado, considerando:
> 
> - Indicadores de conectividad (acceso a internet, dispositivos por hogar)
> - Factores socioeconómicos que determinan la brecha
> - Políticas públicas existentes o propuestas para reducirla
> - Comparación con estándares regionales o globales
> 
> **Trabajo 2 — Caso de estudio sobre sesgo algorítmico** Investigar un caso real de sesgo algorítmico en un sector específico (salud, justicia, empleo, crédito, etc.), analizando:
> 
> - Descripción del sistema y su contexto de uso
> - Tipo de sesgo identificado y su origen (datos, diseño, proxy)
> - Impacto documentado en los afectados
> - Medidas correctivas tomadas o propuestas de gobernanza

---

**Tags:** #computacion-y-sociedad #unidad2 #e-waste #desechos-electronicos #green-ict #desarrollo-sostenible #ODS #economia-circular #Ecuador #ESPOL