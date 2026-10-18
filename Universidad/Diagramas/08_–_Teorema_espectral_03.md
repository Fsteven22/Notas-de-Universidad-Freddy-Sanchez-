graph TB
    A[Matriz Simétrica A] --> B[Define transformación]
    B --> C[En coordenadas estándar:<br/>mezcla componentes]
    A --> D[Cambio a base de<br/>vectores propios]
    D --> E[En nuevas coordenadas:<br/>solo escalado]
    E --> F[Eje i se escala por λᵢ]
    F --> G[Sin rotación ni mezcla]
    style A fill:#e1f5ff
    style E fill:#e1ffe1
    style G fill:#fff4e1
