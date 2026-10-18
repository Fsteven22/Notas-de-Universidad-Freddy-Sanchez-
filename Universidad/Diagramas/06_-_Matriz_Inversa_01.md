graph LR
    A["A<br/>n x n"] --> B{"det distinto 0?"}
    B -->|Sí| C["Existe inversa<br/>AA-1=I"]
    B -->|No| D["Singular<br/>sin inversa"]
    style C fill:#e1ffe1
    style D fill:#ffe1e1
