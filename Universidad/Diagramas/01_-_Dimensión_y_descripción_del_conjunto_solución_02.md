graph TD
    A[Sistema Ax = b] --> B{Compatibilidad}
    B -->|rango A ≠ rango AB| C[INCOMPATIBLE]
    B -->|rango A = rango AB| D[COMPATIBLE]
    
    C --> C1[No hay solución]
    C --> C2[dim no definida]
    
    D --> E{Dimensión}
    E -->|dim = n - rango A| F[Calcular dim]
    
    F --> G{dim = 0?}
    G -->|Sí| H[Compatible Determinado]
    G -->|No| I[Compatible Indeterminado]
    
    H --> H1[Solución única]
    H --> H2[x = vector específico]
    H --> H3[Punto en ℝⁿ]
    
    I --> I1{dim = 1?}
    I1 -->|Sí| J[Recta]
    I1 -->|No| K{dim = 2?}
    K -->|Sí| L[Plano]
    K -->|No| M[Hiperplano dim k]
    
    J --> J1[x = x₀ + tv]
    L --> L1[x = x₀ + sv₁ + tv₂]
    M --> M1[x = x₀ + Σtᵢvᵢ]
    
    J1 --> N[Forma Vectorial]
    L1 --> N
    M1 --> N
    
    N --> O[x₀ + Nul A]
    O --> P[Interpretación Geométrica]
    
    style A fill:#e3f2fd
    style C fill:#ffebee
    style D fill:#e8f5e9
    style H fill:#fff9c4
    style I fill:#f3e5f5
    style N fill:#c8e6c9
    style O fill:#ffe0b2
