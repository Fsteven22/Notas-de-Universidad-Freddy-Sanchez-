graph TD
    A[Vector u] --> B[Proyección sobre v]
    A --> C[Componente ortogonal]
    B -.->|"Longitud = |⟨u,v⟩|/||v||"| D[Acotada por ||u||]
    C -.->|"≥ 0"| E[Pitágoras]
    D --> F[Cauchy-Schwarz]
    E --> F
    style A fill:#e1f5ff
    style F fill:#e1ffe1
