graph LR
    A[Vector x] --> B[Rotar: V^T x]
    B --> C[Escalar: Σ V^T x]
    C --> D[Rotar: U Σ V^T x]
    D --> E[Resultado: Ax]
    F[Ortogonal V] -.-> B
    G[Valores singulares] -.-> C
    H[Ortogonal U] -.-> D
    style B fill:#e1ffe1
    style C fill:#fff4e1
    style D fill:#e1ffe1
