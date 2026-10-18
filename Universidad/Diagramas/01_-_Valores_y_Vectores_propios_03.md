graph LR
    A[Vector v] -->|Multiplicar por A| B{¿Es vector propio?}
    B -->|No| C[Av cambia<br/>dirección y magnitud]
    B -->|Sí| D[Av = λv<br/>solo escala]
    D --> E[λ > 1: estira]
    D --> F[0 < λ < 1: contrae]
    D --> G[λ < 0: invierte]
    style C fill:#ffe1e1
    style D fill:#e1ffe1
    style E fill:#ccffcc
    style F fill:#fff4cc
    style G fill:#ffcccc
