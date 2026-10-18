graph LR
    A[Matriz A] --> B{Transformación}
    B --> C[Vectores generales<br/>cambian dirección]
    B --> D[Vectores propios<br/>mantienen dirección]
    D --> E[Solo se escalan<br/>por λ]
    
    style A fill:#e1f5ff
    style C fill:#ffe1e1
    style D fill:#e1ffe1
    style E fill:#fff4e1
