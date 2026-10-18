flowchart TD
    A[Inicio Demostración] --> B[Existencia]
    A --> C[Unicidad]
    B --> D[Definir \hat{y} usando<br/>base ortogonal]
    D --> E[Definir z = y - \hat{y}]
    E --> F[Probar \hat{y} ∈ W]
    E --> G[Probar z ∈ W⊥]
    F --> H[Existencia probada ✅]
    G --> H
    C --> I[Suponer dos<br/>descomposiciones]
    I --> J[Restar ecuaciones]
    J --> K[Mostrar diferencia<br/>en W ∩ W⊥]
    K --> L[W ∩ W⊥ = 0]
    L --> M[Unicidad probada ✅]
    style H fill:#e1ffe1
    style M fill:#e1ffe1
