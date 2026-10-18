flowchart TD
    A[Vector u a representar] --> B[Base ortogonal<br/> v₁, v₂, ..., vₖ]
    B --> C1[Calcular ⟨u, v₁⟩/||v₁||²]
    B --> C2[Calcular ⟨u, v₂⟩/||v₂||²]
    B --> C3[Calcular ⟨u, vₖ⟩/||vₖ||²]
    C1 --> D[c₁]
    C2 --> E[c₂]
    C3 --> F[cₖ]
    D --> G[u = c₁v₁ + c₂v₂ + ... + cₖvₖ]
    E --> G
    F --> G
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style G fill:#e1ffe1
