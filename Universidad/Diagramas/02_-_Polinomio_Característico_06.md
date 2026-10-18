graph TD
    A[Matriz n×n] --> B{¿Tipo?}
    B -->|Diagonal| C[Leer diagonal<br/>O(n)]
    B -->|Triangular| D[Leer diagonal<br/>O(n)]
    B -->|Simétrica| E[Métodos<br/>especializados]
    B -->|Dispersa| F[Aprovechar<br/>estructura]
    B -->|Densa| G[QR o<br/>Hessenberg]
    style C fill:#e1ffe1
    style D fill:#e1ffe1
    style E fill:#fff4e1
    style G fill:#ffe1e1
