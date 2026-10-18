graph LR
    A[Base Arbitraria] --> B{Método?}
    B -->|Gram-Schmidt| C[Ortonormalizar<br/>luego proyectar]
    B -->|Ecuaciones normales| D[Resolver AᵀAx=Aᵀv]
    C --> E[+ Interpretación geométrica<br/>+ Estable numéricamente<br/>- Más pasos]
    D --> F[+ Directo<br/>+ Matricial<br/>- Puede ser inestable]
    style C fill:#e1ffe1
    style D fill:#fff4e1
