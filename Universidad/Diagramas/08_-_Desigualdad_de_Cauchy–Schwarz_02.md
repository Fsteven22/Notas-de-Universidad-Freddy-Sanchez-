graph LR
    A[Origen] -->|u| B[Extremo u]
    A -->|v| C[Extremo v]
    B -.->|"⟨u,v⟩"| D[Proyección]
    C -.->|"||v||"| E[Longitud v]
    F["⟨u,v⟩ ≤ ||u|| ||v||"] --> G[Siempre cierto]
    style A fill:#e1f5ff
    style F fill:#e1ffe1
    style G fill:#e1ffe1
