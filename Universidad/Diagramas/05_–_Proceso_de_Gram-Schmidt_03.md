graph LR
    A[v₁] -->|Normalizar| B[u₁ = v₁/||v₁||]
    C[v₂] -->|Proyección| D[proyᵤ₁v₂]
    C -->|Restar| E[v₂' = v₂ - proyᵤ₁v₂]
    E -->|Normalizar| F[u₂ = v₂'/||v₂'||]
    B --> G[✓ ||u₁|| = 1]
    F --> H[✓ ||u₂|| = 1]
    F --> I[✓ u₁ ⊥ u₂]
    style G fill:#e1ffe1
    style H fill:#e1ffe1
    style I fill:#e1ffe1
