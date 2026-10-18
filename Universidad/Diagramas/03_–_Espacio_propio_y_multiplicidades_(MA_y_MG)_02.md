graph TD
    A["E_λ = Nul(A - λI)"] --> B[¿Contiene 0?]
    B -->|Sí: A0 = λ0| C[✓]
    A --> D[¿Cerrado bajo suma?]
    D -->|v₁,v₂ ∈ E_λ| E["A(v₁+v₂) = λ(v₁+v₂)?"]
    E -->|Sí| F[✓]
    A --> G[¿Cerrado bajo mult. escalar?]
    G -->|v ∈ E_λ, c ∈ ℝ| H["A(cv) = λ(cv)?"]
    H -->|Sí| I[✓]
    C --> J[E_λ es subespacio]
    F --> J
    I --> J
    style A fill:#e1f5ff
    style J fill:#e1ffe1
