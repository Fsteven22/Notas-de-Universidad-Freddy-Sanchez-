graph TD
    A[Composición] --> B{¿Conmutan?}
    B -->|Sí| C[Rotaciones alrededor<br/>del mismo eje]
    B -->|Sí| D[Escalamientos<br/>uniformes]
    B -->|No| E[Rotación + Reflexión]
    B -->|No| F[Rotación + Cizalladura]
    style C fill:#e1ffe1
    style D fill:#e1ffe1
    style E fill:#ffe1e1
    style F fill:#ffe1e1
