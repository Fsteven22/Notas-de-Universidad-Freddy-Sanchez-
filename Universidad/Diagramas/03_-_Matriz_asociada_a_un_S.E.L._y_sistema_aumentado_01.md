graph TB
    A[Sistema de Ecuaciones Lineales] --> B[Forma Escalar]
    A --> C[Forma Matricial]
    A --> D[Forma Vectorial]
    
    B --> E[Ecuaciones individuales]
    C --> F[Matriz de coeficientes A]
    C --> G[Matriz aumentada A|b]
    D --> H[Combinación lineal]
    
    F --> I[Ax = b]
    G --> I
    H --> I
    
    style A fill:#e1f5ff
    style I fill:#e1ffe1
