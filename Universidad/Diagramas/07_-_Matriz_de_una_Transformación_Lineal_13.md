graph TB
    A[Matriz A] --> B{¿Diagonalizable?}
    B -->|Sí| C[Encontrar eigenvectores]
    C --> D[Formar base con ellos]
    D --> E[Matriz diagonal D]
    B -->|No| F[Mantener forma general]
    style E fill:#e1ffe1
    style F fill:#ffe1e1
