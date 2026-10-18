graph TD
    A[Sistema de Ecuaciones Lineales] --> B[Escribir matriz ampliada AB]
    B --> C[Aplicar eliminación de Gauss]
    C --> D[Obtener forma escalonada]
    D --> E{¿Hay fila<br/>0 0 ... 0  k<br/>con k ≠ 0?}
    
    E -->|Sí| F[Sistema INCOMPATIBLE<br/>Sin solución]
    E -->|No| G[Calcular rangos]
    
    G --> H{¿rang A =<br/>rang AB?}
    H -->|No| F
    H -->|Sí| I{¿rang A = n?<br/>n = núm. incógnitas}
    
    I -->|Sí| J[Sistema COMPATIBLE<br/>DETERMINADO<br/>Solución única]
    I -->|No| K[Sistema COMPATIBLE<br/>INDETERMINADO<br/>Infinitas soluciones]
    
    J --> L[Sustitución regresiva]
    K --> M[Expresar en forma paramétrica<br/>Variables libres = n - rang A]
    
    L --> N[Solución: x₁, x₂, ..., xₙ]
    M --> O[Solución: f s, t, ...]
    
    style A fill:#e3f2fd
    style F fill:#ffcdd2
    style J fill:#c8e6c9
    style K fill:#fff9c4
    style N fill:#a5d6a7
    style O fill:#ffe082
