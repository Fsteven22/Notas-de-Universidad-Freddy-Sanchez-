graph TD
    A[Vector v] --> B[Proyectar sobre u]
    B --> C[proj_u v<br/>Componente paralela]
    B --> D[perp_u v<br/>Componente perpendicular]
    C --> E[En dirección de u]
    D --> F[Ortogonal a u]
    E --> G[v = proj_u v + perp_u v]
    F --> G
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style G fill:#e1f5ff
