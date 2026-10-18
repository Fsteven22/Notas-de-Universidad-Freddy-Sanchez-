graph LR
    A["A x = b"] --> B{"Rango A<br/>vs A|b"}
    B -->|Iguales = n| C["Única<br/>x=A-1b"]
    B -->|Iguales menor n| D["Infinitas<br/>parámetros"]
    B -->|Distintos| E["Incompatible<br/>vacío"]
    style C fill:#e1ffe1
    style E fill:#ffe1e1
