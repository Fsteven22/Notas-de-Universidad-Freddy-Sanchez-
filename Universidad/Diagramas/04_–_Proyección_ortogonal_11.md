flowchart TD
    A["Proyección Ortogonal"]

    A --> B["Proyección sobre Vector"]
    B --> B1["Fórmula: <v,u> / ||u||^2 · u"]
    B --> B2["Propiedades"]
    B2 --> B21["Linealidad"]
    B2 --> B22["Idempotencia"]
    B --> B3["Descomposición"]
    B3 --> B31["Paralela"]
    B3 --> B32["Perpendicular"]

    A --> C["Proyección sobre Subespacio"]
    C --> C1["Base ortogonal"]
    C1 --> C11["Σ <v,u_i> / ||u_i||^2 · u_i"]
    C --> C2["Base ortonormal"]
    C2 --> C21["Σ <v,u_i> · u_i"]
    C --> C3["Base arbitraria"]
    C3 --> C31["A (A^T A)^-1 A^T"]

    A --> D["Matrices de Proyección"]
    D --> D1["Construcción"]
    D1 --> D11["P = U U^T"]
    D --> D2["Propiedades"]
    D2 --> D21["P^2 = P"]
    D2 --> D22["P^T = P"]
    D2 --> D23["Autovalores {0,1}"]

    A --> E["Aplicaciones"]
    E --> E1["Mínimos cuadrados"]
    E1 --> E11["A^T A \hat{x} = A^T b"]
    E --> E2["Distancias"]
    E2 --> E21["||v - proj_W(v)||"]
    E --> E3["Regresión lineal"]
    E --> E4["Filtrado de señales"]

    A --> F["Complemento Ortogonal"]
    F --> F1["Definición"]
    F1 --> F11["<v,w> = 0"]
    F --> F2["Propiedades"]
    F2 --> F21["V = W ⊕ W_perp"]
    F2 --> F22["dim(W) + dim(W_perp) = dim(V)"]

