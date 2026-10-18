mindmap
  root((Bases Ortonormales))
    Computación
      Algoritmos estables
      Menor error numérico
      Cálculos rápidos
    Geometría
      Interpretación clara
      Coordenadas = proyecciones
      Distancias preservadas
    Aplicaciones
      Procesamiento de señales
      Compresión de datos
      Gráficos por computadora
      Análisis de componentes principales
````

---

## 🔄 Proceso de Gram-Schmidt

### 🏗️ Algoritmo de Ortonormalización

[!example] 🛠️ Construcción de Bases Ortonormales
El **proceso de Gram-Schmidt** transforma cualquier base en una base ortonormal, preservando el espacio generado.
**Idea intuitiva:**
```mermaid
graph LR
    A["Base Cualquiera<br/>v₁, v₂, v₃" ] --> B["Ortogonalizar<br/>Gram-Schmidt" ]
    B --> C["Base Ortogonal<br/>w₁, w₂, w₃" ]
    C --> D[Normalizar<br/>Dividir por normas]
    D --> E[Base Ortonormal<br/>u₁, u₂, u₃]
    style A fill:#ffe1e1
    style C fill:#fff4e1
    style E fill:#e1ffe1
