graph LR
    A[Base de W] --> B{¿Es ortonormal?}
    B -->|Sí| C[P = UU^T<br/>Directo]
    B -->|No| D{¿Ortonormalizar?}
    D -->|Sí| E[Gram-Schmidt<br/>luego P = UU^T]
    D -->|No| F[P = AA^TA^{-1}A^T<br/>Requiere inversa]
    C --> G[✅ Más simple<br/>✅ Más estable]
    E --> H[✅ Interpretación clara<br/>⚠️ Más pasos]
    F --> I[✅ Directo<br/>❌ Puede ser inestable]
    style C fill:#e1ffe1
    style E fill:#fff4e1
    style F fill:#ffe1e1
