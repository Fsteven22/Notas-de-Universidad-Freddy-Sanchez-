flowchart TD
    A[Base arbitraria<br/> v₁, v₂, ..., vₖ ] --> B[Tomar v₁]
    B --> C[Normalizar: q₁ = v₁/‖v₁‖]
    C --> D[Tomar v₂]
    D --> E[Restar proyección<br/>sobre q₁]
    E --> F[Normalizar: q₂]
    F --> G[Tomar v₃]
    G --> H[Restar proyecciones<br/>sobre q₁, q₂]
    H --> I[Normalizar: q₃]
    I --> J[Continuar...]
    J --> K[Base ortonormal<br/> q₁, q₂, ..., qₖ ]
    style A fill:#ffe1e1
    style K fill:#e1ffe1
