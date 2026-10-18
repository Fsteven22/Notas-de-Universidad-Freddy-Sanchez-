graph TB
    A[Proyección] --> B[Sobre Vector u<br/>Línea 1D]
    A --> C[Sobre Subespacio W<br/>Plano nD]
    B --> D[Fórmula: ⟨v,u⟩/||u||² · u]
    B --> E[Resultado: en span u]
    C --> F[Fórmula: Σ ⟨v,uᵢ⟩uᵢ]
    C --> G[Resultado: en W]
    D --> H[Caso especial n=1]
    F --> I[Caso general n≥1]
    style B fill:#e1ffe1
    style C fill:#fff4e1
    style H fill:#e1f5ff
    style I fill:#e1f5ff
