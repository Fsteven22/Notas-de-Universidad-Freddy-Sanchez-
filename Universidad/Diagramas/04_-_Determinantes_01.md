graph LR
    A["Matriz<br/>cuadrada A"] --> B["det(A)<br/>escalar"]
    B --> C{"det = 0?"}
    C -->|Sí| D["Singular<br/>sin inversa"]
    C -->|No| E["Regular<br/>existe A-1"]
    style A fill:#fff4e1
    style C fill:#e1ffe1
    style E fill:#e1f5ff
