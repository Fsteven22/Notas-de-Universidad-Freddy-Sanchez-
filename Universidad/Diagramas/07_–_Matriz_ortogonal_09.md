graph LR
    A[Matriz Ortogonal Q] --> B{det Q = ?}
    B -->|+1| C[Rotación propia<br/>SO n ]
    B -->|-1| D[Rotación impropia<br/>reflexión]
    C --> E[Ejemplos:<br/>Rotaciones<br/>Identidad]
    D --> F[Ejemplos:<br/>Reflexiones<br/>Inversiones]
    style C fill:#e1ffe1
    style D fill:#fff4e1
