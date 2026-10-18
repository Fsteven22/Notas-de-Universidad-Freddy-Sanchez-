graph LR
    A[Origen] -->|u| B[Punto B]
    A -->|v| C[Punto C]
    B -->|v| D[u + v]
    A -->|u + v| D
    B -.->|"||u||"| E[Longitud u]
    C -.->|"||v||"| F[Longitud v]
    D -.->|"||u + v|| ≤ ||u|| + ||v||"| G[Desigualdad triangular]
    style A fill:#e1f5ff
    style G fill:#e1ffe1
