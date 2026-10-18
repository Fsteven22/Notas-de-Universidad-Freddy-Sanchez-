graph TD
    A[Sistema AX = B] --> B[Formar matriz ampliada A B]
    B --> C[Aplicar Gauss para obtener FE]
    C --> D[Calcular r = rango A]
    C --> E[Calcular r' = rango A B]
    D --> F{¿r = r'?}
    E --> F
    F -->|NO| G[INCOMPATIBLE]
    G --> G1[Sin solución]
    G1 --> G2[S = ∅]
    F -->|SÍ| H[COMPATIBLE]
    H --> I{¿r = n?}
    I -->|SÍ| J[Compatible DETERMINADO]
    J --> J1[Solución ÚNICA]
    J1 --> J2[Resolver por Gauss-Jordan, Cramer, o sustitución]
    J2 --> J3[S = punto]
    I -->|NO| K[Compatible INDETERMINADO]
    K --> K1[INFINITAS soluciones]
    K1 --> K2[k = n - r parámetros]
    K2 --> K3[Obtener FER]
    K3 --> K4[Solución paramétrica: X = X₀ + t₁v₁ + ... + tₖvₖ]
    K4 --> K5[S = subespacio afín de dim k]
style A fill:#e3f2fd
style G fill:#ffebee
style J fill:#e8f5e9
style K fill:#fff3e0
style F fill:#f3e5f5
style I fill:#f3e5f5
