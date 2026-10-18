flowchart TB
    A[Espacio ℝⁿ] --> B[Subespacio W]
    A --> C[Complemento W⊥]
    B --> D[Contiene vectores<br/>de W]
    C --> E[Contiene vectores<br/>perpendiculares a W]
    D -.->|v · w = 0| E
    style A fill:#e1f5ff
    style B fill:#e1ffe1
    style C fill:#fff4e1
