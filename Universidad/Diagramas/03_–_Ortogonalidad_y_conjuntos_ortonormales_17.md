graph TB
    A[Vectores en ℝⁿ] --> B{¿Producto interno cero?}
    B -->|Sí| C[Vectores Ortogonales]
    B -->|No| D[Vectores Oblicuos]
    C --> E{¿Norma = 1?}
    E -->|Sí| F[Vectores Ortonormales]
    E -->|No| G[Ortogonales no normalizados]
    F --> H[Base Ortonormal]
    
    style C fill:#e1ffe1
    style F fill:#e1f5ff
    style H fill:#fff4e1
