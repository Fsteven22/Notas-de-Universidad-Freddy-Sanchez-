graph TD
    A[Semilla Inicial] --> B[Algoritmo PRNG]
    B --> C[Número Pseudoaleatorio]
    C --> D{¿Uso Seguro?}
    D -->|Sí| E[Módulo secrets]
    D -->|No| F[Módulo random]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style E fill:#ffebee
    style F fill:#e8f5e8
