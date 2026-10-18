flowchart TD
    A[Problema de Proyección] --> B{¿Sobre qué proyectar?}
    B -->|Vector u| C[Proyección 1D]
    B -->|Subespacio W| D[Proyección nD]
    
    C --> E{¿u es unitario?}
    E -->|Sí| F[proj = ⟨v,u⟩u]
    E -->|No| G["proj = ⟨v,u⟩/||u||² · u"]
    
    D --> H{¿Base de W?}
    H -->|Ortonormal| I[proj = Σ⟨v,uᵢ⟩uᵢ]
    H -->|Ortogonal| J["proj = Σ⟨v,uᵢ⟩/||uᵢ||² · uᵢ"]
    H -->|Arbitraria| K{¿Ortonormalizar?}
    
    K -->|Sí| L[Gram-Schmidt<br/>luego usar I o J]
    K -->|No| M["Usar P = AA^TA^{-1}A^T"]
    
    style F fill:#e1ffe1
    style I fill:#e1ffe1
    style J fill:#fff4e1
    style L fill:#e1f5ff
    style M fill:#ffe1e1
