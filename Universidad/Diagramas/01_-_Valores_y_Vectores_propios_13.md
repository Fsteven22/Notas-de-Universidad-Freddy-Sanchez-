flowchart TD
    A[Valores y Vectores Propios]

    A --> B[Definición]
    B --> B1[Av = λv]
    B --> B2[λ es valor propio]
    B --> B3[v es vector propio]
    B --> B4[Ecuación característica]

    A --> C[Cálculo]
    C --> C1["Calcular det(A − λI) = 0"]
    C --> C2[Resolver para λ]
    C --> C3[Encontrar v para cada λ]
    C --> C4[Normalizar vectores]

    A --> D[Diagonalización]
    D --> D1[A = P D P⁻¹]
    D --> D2[P: vectores propios]
    D --> D3[D: valores propios]
    D --> D4[Simplifica potencias de A]

    A --> E[Aplicaciones]
    E --> E1[Sistemas dinámicos]
    E --> E2[PCA]
    E --> E3[PageRank]
    E --> E4[Vibraciones]
    E --> E5[Estabilidad]

    A --> F[Propiedades]
    F --> F1[Matrices simétricas]
    F --> F2[Traza y determinante]
    F --> F3[Ortogonalidad]
    F --> F4[Multiplicidad]

