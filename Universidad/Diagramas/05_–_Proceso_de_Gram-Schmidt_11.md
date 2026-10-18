graph TD
    A[Vectores de entrada] --> B{¿Linealmente<br/>independientes?}
    B -->|No| C[❌ GS FALLA]
    B -->|Sí| D{¿Bien<br/>condicionados?}
    D -->|No| E[⚠️ Problemas<br/>numéricos]
    D -->|Sí| F[✓ GS funciona]
    C --> G[wₖ = 0 en algún paso]
    E --> H[Pérdida de<br/>ortogonalidad]
    style C fill:#ffe1e1
    style E fill:#fff4cc
    style F fill:#e1ffe1
