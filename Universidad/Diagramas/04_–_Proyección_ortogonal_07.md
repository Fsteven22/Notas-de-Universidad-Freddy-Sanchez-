graph TD
    A[Vector v fuera de W] --> B[Buscar w ∈ W<br/>más cercano]
    B --> C{¿Cuál w minimiza ||v-w||?}
    C --> D[Cualquier otro w<br/>Mayor distancia]
    C --> E[proj_W v<br/>Mínima distancia]
    E --> F[Distancia:<br/>||perp_W v||]
    D --> G[Distancia:<br/>> ||perp_W v||]
    style E fill:#e1ffe1
    style F fill:#e1ffe1
    style D fill:#ffe1e1
    style G fill:#ffe1e1
