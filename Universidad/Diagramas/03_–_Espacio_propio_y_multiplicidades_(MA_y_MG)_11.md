flowchart TD
    A[Matriz A]
    A --> B[Calcular polinomio característico]
    B --> C["Factorizar p_A(λ)"]
    C --> D[Identificar valores propios]
    D --> E[Determinar MA de cada λ]
    E --> F[Para cada valor propio λᵢ]
    F --> G[Formar A − λᵢI]
    G --> H["Resolver (A − λᵢI)v = 0"]
    H --> I[Encontrar base de E_λᵢ]
    I --> J["Calcular MG(λᵢ)"]
    J --> K{"¿MG(λᵢ) = MA(λᵢ)?"}
    K -->|Sí, todos| L[DIAGONALIZABLE]
    K -->|No| M[NO diagonalizable]
    L --> N[Formar matriz P]
    L --> O[Formar matriz D]
