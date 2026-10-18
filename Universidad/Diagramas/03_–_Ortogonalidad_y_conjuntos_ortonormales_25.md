flowchart TD
    A["Base original<br/>v₁, v₂, ..., vₙ"] --> B["Normalizar v₁<br/>u₁ = v₁/||v₁||" ]
    B --> C[Para k = 2 hasta n]
    C --> D["Restar proyecciones<br/>wₖ = vₖ - Σ⟨vₖ,uⱼ⟩uⱼ"]
    D --> E["Normalizar<br/>uₖ = wₖ/||wₖ||"]
    E --> F{¿Terminado?}
    F -->|No| C
    F -->|Sí| G["Base ortonormal<br/>u₁, u₂, ..., uₙ"]
    style A fill:#ffe1e1
    style G fill:#e1ffe1
    style D fill:#fff4e1
    style E fill:#e1f5ff
