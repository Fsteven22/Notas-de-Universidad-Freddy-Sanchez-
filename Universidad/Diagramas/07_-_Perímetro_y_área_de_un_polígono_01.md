graph LR
    A["Polígono"] --> B{"Datos?"}
    B -->|Regular| C["P=na<br/>A=P·ap/2"]
    B -->|Vértices| D["Shoelace"]
    B -->|Retícula| E["Pick"]
    style C fill:#e1ffe1
    style E fill:#e1f5ff
