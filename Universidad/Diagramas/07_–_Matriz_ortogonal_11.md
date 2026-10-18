graph TB
    A[Datos originales<br/>X correlacionados] --> B[Aplicar PCA<br/>Calcular Q ortogonal]
    B --> C[Datos transformados<br/>Y = X Q]
    D[Propiedades de Q] --> E[✅ Vectores ortogonales]
    D --> F[✅ Preserva distancias]
    D --> G[✅ Maximiza varianza]
    C --> H[Componentes<br/>independientes]
    style B fill:#e1ffe1
    style C fill:#fff4e1
