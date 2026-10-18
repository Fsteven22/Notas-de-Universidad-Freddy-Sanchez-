graph TB
    A[Descomposición Espectral<br/>A = QΛQ^T] --> B[Potencias de matriz]
    A --> C[Función de matriz]
    A --> D[Formas cuadráticas]
    B --> E[A^n = QΛ^nQ^T]
    C --> F[f A = Qf Λ Q^T]
    D --> G[x^T Ax = y^T Λy]
    F --> H[e^A, sin A, √A...]
    style A fill:#e1f5ff
    style E fill:#e1ffe1
    style F fill:#e1ffe1
    style G fill:#e1ffe1
