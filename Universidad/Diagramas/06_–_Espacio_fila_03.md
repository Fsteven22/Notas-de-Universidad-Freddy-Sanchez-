graph TB
    subgraph "Dominio: ℝⁿ"
        A[Row A<br/>Espacio Fila<br/>dim = r]
        B[Nul A<br/>Espacio Nulo<br/>dim = n-r]
    end
    subgraph "Codominio: ℝᵐ"
        C[Col A<br/>Espacio Columna<br/>dim = r]
        D[Nul Aᵀ<br/>Nulo Izquierdo<br/>dim = m-r]
    end
    A -->|transformación| C
    B -->|aniquilado| E[0]
    A -.ortogonal.- B
    C -.ortogonal.- D
    A -.misma dim.- C
    style A fill:#c8e6c9
    style B fill:#ffccbc
    style C fill:#bbdefb
    style D fill:#ffccbc
