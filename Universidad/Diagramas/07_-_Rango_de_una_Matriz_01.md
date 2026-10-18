graph LR
    A["Matriz A"] --> B["Filas/cols<br/>indep"]
    B --> C["r(A)"]
    C --> D{"r = n?"}
    D -->|Sí| E["Invertible"]
    D -->|No| F["Singular"]
    style C fill:#e1ffe1
    style F fill:#ffe1e1
