flowchart TD
    A["Base Arbitraria<br/>v₁, v₂, ..., vₙ"] --> B["¿Ya es ortogonal?"]
    B -->|Sí| C[Normalizar vectores]
    B -->|No| D[Aplicar Gram-Schmidt]
    
    D --> E["Obtener base ortogonal<br/>{w₁, w₂, ..., wₙ}"]
    E --> C
    
    C --> F["Base ortonormal<br/>{u₁, u₂, ..., uₙ}"]
    
    F --> G[Usar para:]
    G --> H["Calcular coordenadas<br/>cᵢ = ⟨v,uᵢ⟩"]
    G --> I["Proyectar vectores<br/>proj = Σ⟨v,uᵢ⟩uᵢ"]
    G --> J["Resolver sistemas<br/>mínimos cuadrados"]
    
    style A fill:#ffe1e1
    style E fill:#fff4e1
    style F fill:#e1ffe1
    style H fill:#e1f5ff
    style I fill:#e1f5ff
    style J fill:#e1f5ff

