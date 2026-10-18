graph LR
    A["L1, L2"] --> B{"m1 = m2?"}
    B -->|No| C["Secantes<br/>un corte"]
    B -->|Sí| D{"b1 = b2?"}
    D -->|Sí| E["Coincidentes"]
    D -->|No| F["Paralelas"]
    style C fill:#e1ffe1
    style F fill:#e1f5ff
