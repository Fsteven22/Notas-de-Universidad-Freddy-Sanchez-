graph LR
    A["A m x n<br/>B n x p"] --> B["AB<br/>m x p"]
    B --> C{"Conmuta?"}
    C -->|Casi nunca| D["AB distinto BA"]
    style B fill:#e1ffe1
    style D fill:#ffe1e1
