graph LR
    subgraph "Matriz 3×4"
        A[A]
    end
    subgraph "Espacio Fila"
        B[Row A ⊆ ℝ⁴]
        B1[dim ≤ 3]
        B --> B1
    end
    subgraph "Espacio Columna"
        C[Col A ⊆ ℝ³]
        C1[dim ≤ 3]
        C --> C1
    end
    A --> B
    A --> C
    B1 -.misma dim.- C1
    style B fill:#c8e6c9
    style C fill:#bbdefb
    style B1 fill:#fff9c4
    style C1 fill:#fff9c4
