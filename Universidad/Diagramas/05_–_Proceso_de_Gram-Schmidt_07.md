flowchart LR
    A[Matriz A<br/>columnas = v₁, v₂, v₃] --> B[Gram-Schmidt]
    B --> C[Matriz Q<br/>columnas = u₁, u₂, u₃]
    B --> D[Matriz R<br/>coeficientes]
    C --> E[A = QR]
    D --> E
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style E fill:#e1f5ff
