graph TD
    A[Conjunto de Vectores] --> B{¿Independientes?}
    B -->|Sí| C[Puede ser base]
    B -->|No| D[No es base]
    C --> E{¿Ortogonales?}
    E -->|Sí| F[Base Ortogonal]
    E -->|No| G[Base cualquiera]
    F --> H{¿Norma 1?}
    H -->|Sí| I[⭐ BASE ORTONORMAL]
    H -->|No| J[Solo ortogonal]
    style I fill:#e1ffe1
    style F fill:#fff4e1
    style C fill:#e1f5ff
