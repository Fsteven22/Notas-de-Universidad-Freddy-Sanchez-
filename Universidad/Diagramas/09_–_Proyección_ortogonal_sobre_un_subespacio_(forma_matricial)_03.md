graph TB
    A[Base de W] --> B{¿Ortonormal?}
    B -->|No| C[P = A A^T A ^-1 A^T]
    B -->|Sí| D[P = QQ^T]
    C --> E[Requiere inversión<br/>Más costoso]
    D --> F[Solo multiplicación<br/>Muy eficiente]
    E --> G[O n³ operaciones]
    F --> H[O n² operaciones]
    style D fill:#e1ffe1
    style F fill:#e1ffe1
    style C fill:#ffe1e1
