flowchart TD
    A[Matriz A<br/>n×n] --> B[Restar λI<br/>de A]
    B --> C[A - λI<br/>matriz con λ]
    C --> D[Calcular<br/>determinante]
    D --> E[Expandir<br/>expresión]
    E --> F["p(λ)<br/>polinomio de grado n"]
    style A fill:#e1f5ff
    style C fill:#fff4e1
    style F fill:#e1ffe1
