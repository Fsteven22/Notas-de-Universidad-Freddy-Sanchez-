flowchart TD
    A[Inicio] --> B[Calcular p λ = det A-λI]
    B --> C[Encontrar raíces λ₁, ..., λₖ]
    C --> D[Para cada λᵢ]
    D --> E[Resolver A-λᵢI v = 0]
    E --> F[Base de E_λᵢ]
    F --> G{¿Más valores propios?}
    G -->|Sí| D
    G -->|No| H{∑ dim E_λᵢ = n?}
    H -->|No| I[❌ NO diagonalizable]
    H -->|Sí| J[Formar P con vectores propios]
    J --> K[Formar D con valores propios]
    K --> L[✅ A = PDP⁻¹]
    
    style A fill:#e1f5ff
    style L fill:#e1ffe1
    style I fill:#ffe1e1
