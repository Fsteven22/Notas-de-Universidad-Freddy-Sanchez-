graph TB
    A[Teorema Espectral] --> B[Matrices Simétricas]
    A --> C[Matrices Hermitianas]
    A --> D[Operadores Normales]
    
    B --> E[Valores propios<br/>REALES]
    C --> F[Valores propios<br/>REALES]
    D --> G[Valores propios<br/>COMPLEJOS]
    
    E --> H[Vectores propios<br/>ORTOGONALES]
    F --> H
    G --> I[Vectores propios<br/>ORTONORMALES]
    
    H --> J[Diagonalización<br/>A = QΛQ^T]
    I --> J
    
    style A fill:#e1f5ff
    style J fill:#e1ffe1
