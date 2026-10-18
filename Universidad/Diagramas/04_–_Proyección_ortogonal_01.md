graph TB
    A[Vector Original v] --> B{Proyectar sobre}
    B --> C[Vector u<br/>Proyección 1D]
    B --> D[Subespacio W<br/>Proyección nD]
    
    C --> E[Componente paralela<br/>proj_u v]
    C --> F[Componente perpendicular<br/>v - proj_u v]
    
    D --> G[Aproximación en W<br/>proj_W v]
    D --> H[Error perpendicular<br/>v - proj_W v]
    
    E --> I[v = proj + perp]
    F --> I
    
    style A fill:#e1f5ff
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style I fill:#f0e1ff
