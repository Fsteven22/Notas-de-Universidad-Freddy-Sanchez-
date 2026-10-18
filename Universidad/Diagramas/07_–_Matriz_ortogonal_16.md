graph TB
    A[Conjunto de matrices<br/>ortogonales n×n] --> B[Operación: Multiplicación]
    B --> C[✅ Cerradura:<br/>Q₁Q₂ ortogonal]
    B --> D[✅ Asociatividad:<br/> Q₁ Q₂Q₃ =  Q₁Q₂ Q₃]
    B --> E[✅ Identidad:<br/>I ortogonal]
    B --> F[✅ Inversos:<br/>Q^-1 = Q^T ortogonal]
    C --> G[Grupo Ortogonal O n ]
    D --> G
    E --> G
    F --> G
    style A fill:#e1f5ff
    style G fill:#e1ffe1
