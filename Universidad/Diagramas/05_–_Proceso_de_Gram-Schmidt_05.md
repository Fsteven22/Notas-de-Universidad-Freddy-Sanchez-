flowchart TD
    A[Inicio: v₁, v₂, ..., vₙ] --> B[k = 1]
    B --> C[Normalizar v₁ → u₁]
    C --> D[k = k + 1]
    D --> E{k ≤ n?}
    E -->|No| F[Fin: u₁, u₂, ..., uₙ]
    E -->|Sí| G[wₖ = vₖ]
    G --> H[Para j = 1 hasta k-1]
    H --> I[wₖ = wₖ - proyᵤⱼvₖ]
    I --> J["uₖ = wₖ/||wₖ||"]
    J --> D
    style C fill:#e1f5ff
    style I fill:#fff4e1
    style J fill:#e1ffe1
    style F fill:#e1ffe1
