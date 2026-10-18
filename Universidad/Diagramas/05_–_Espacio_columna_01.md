graph TD
    A[Matriz A: 3×2] --> B[Col A es subespacio de ℝ³]
    B --> C{Rango de A}
    C -->|rank = 2| D[Plano por el origen]
    C -->|rank = 1| E[Recta por el origen]
    C -->|rank = 0| F[Solo el origen]
    D --> G[2 columnas LI]
    E --> H[Columnas paralelas]
    F --> I[Matriz cero]
    style B fill:#e1f5ff
    style D fill:#c8e6c9
    style E fill:#fff9c4
    style F fill:#ffccbc
