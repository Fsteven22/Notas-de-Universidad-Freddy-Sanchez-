flowchart LR
    A["Conjunto Ortogonal<br/>v₁, v₂, ..., vₖ"] --> B["Calcular normas<br/>||v₁||, ||v₂||, ..., ||vₖ||" ]
    B --> C["Normalizar cada vector<br/>uᵢ = vᵢ/||vᵢ||"]
    C --> D[Conjunto Ortonormal<br/>u₁, u₂, ..., uₖ]
    D --> E[Verificar:<br/>⟨uᵢ,uⱼ⟩ = δᵢⱼ]
    style A fill:#fff4e1
    style D fill:#e1ffe1
    style E fill:#e1f5ff
