flowchart TD
    A[Columnas de A] --> B[Primera columna a₁]
    B --> C[Normalizar:<br/>q₁ = a₁/‖a₁‖]
    C --> D[Segunda columna a₂]
    D --> E[Restar proyección:<br/>v₂ = a₂ - a₂·q₁q₁]
    E --> F[Normalizar:<br/>q₂ = v₂/‖v₂‖]
    F --> G[Tercera columna a₃]
    G --> H[Restar proyecciones:<br/>v₃ = a₃ - a₃·q₁q₁ - a₃·q₂q₂]
    H --> I[Normalizar:<br/>q₃ = v₃/‖v₃‖]
    I --> J[Continuar...]
    style C fill:#e1ffe1
    style F fill:#e1ffe1
    style I fill:#e1ffe1
