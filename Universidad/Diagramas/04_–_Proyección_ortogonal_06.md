flowchart TD
    A[Vector v y subespacio W] --> B[Calcular proj_W v]
    B --> C[Calcular residuo:<br/>r = v - proj_W v]
    C --> D[Distancia: d = ||r||]
    B --> E[Punto más cercano<br/>en W]
    D --> F[Distancia mínima<br/>a W]
    style E fill:#e1ffe1
    style F fill:#fff4e1
