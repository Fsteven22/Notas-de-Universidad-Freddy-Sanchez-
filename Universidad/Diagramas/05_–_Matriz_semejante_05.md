graph TB
    A[Matrices Semejantes<br/>A ~ B] --> B[Invariantes]
    A --> C[Variables]
    
    B --> D[det A = det B]
    B --> E[tr A = tr B]
    B --> F[rango A = rango B]
    B --> G[Valores propios iguales]
    B --> H[p_A λ = p_B λ]
    
    C --> I[Entradas diferentes]
    C --> J[Vectores propios diferentes]
    
    style A fill:#e1f5ff
    style B fill:#e1ffe1
    style C fill:#ffe1e1
