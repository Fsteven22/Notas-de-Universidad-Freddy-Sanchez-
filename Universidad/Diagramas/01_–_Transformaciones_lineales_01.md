graph LR
    A[V<br/>dim = n] --> B[Ker T<br/>dim = k]
    A --> C[complemento<br/>dim = n-k]
    C --> D[Im T<br/>dim = n-k]
    B -.mapea a.- E[0]
    C -.isomorfismo.- D
    style A fill:#e1f5ff
    style B fill:#ffccbc
    style C fill:#c8e6c9
    style D fill:#c8e6c9
