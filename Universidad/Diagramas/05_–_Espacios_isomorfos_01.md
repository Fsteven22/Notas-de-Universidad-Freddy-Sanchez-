graph LR
    A[Espacio V] <-->|Isomorfismo T| B[Espacio W]
    
    A --> C[dim V = n]
    B --> D[dim W = n]
    
    C -.->|misma dimensión| D
    
    A --> E[Operaciones en V]
    B --> F[Operaciones en W]
    
    E -.->|se preservan| F
    
    style A fill:#e1f5ff
    style B fill:#ffe1f5
    style C fill:#e1ffe1
    style D fill:#e1ffe1
