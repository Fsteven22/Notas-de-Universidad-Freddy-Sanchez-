graph LR
    A[Matriz Ortogonal] --> B{det Q = ?}
    B -->|det = +1| C[🔄 Rotación]
    B -->|det = -1| D[🪞 Reflexión]
    C --> E[Preserva orientación]
    D --> F[Invierte orientación]
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style E fill:#e1ffe1
    style F fill:#fff4e1
