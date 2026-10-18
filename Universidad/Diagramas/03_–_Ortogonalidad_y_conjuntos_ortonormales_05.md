flowchart TD
    A[Calcular ⟨u,v⟩] --> B{Valor?}
    B -->|= 0| C[θ = 90°<br/>✅ ORTOGONALES]
    B -->|≠ 0| D[Calcular ||u|| y ||v||]
    D --> E[cos θ = ⟨u,v⟩ / ||u|| ||v||]
    E --> F[θ = arccos valor]
    C --> G[Relación<br/>perpendicular]
    F --> H{θ < 90°?}
    H -->|Sí| I[Ángulo agudo]
    H -->|No| J[Ángulo obtuso]
    style C fill:#e1ffe1
    style I fill:#fff4e1
    style J fill:#ffe1e1
