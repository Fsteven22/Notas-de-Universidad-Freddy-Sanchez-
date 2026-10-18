graph TB
    A[Matriz Ortogonal Q] --> B[Columnas ortonormales]
    A --> C[Filas ortonormales]
    A --> D[Q^T · Q = I]
    
    B --> E[Perpendiculares<br/>entre sí]
    B --> F[Longitud unitaria]
    
    C --> E
    C --> F
    
    D --> G[Q^-1 = Q^T]
    G --> H[Fácil de invertir]
    
    style A fill:#e1f5ff
    style D fill:#e1ffe1
    style G fill:#fff4e1
