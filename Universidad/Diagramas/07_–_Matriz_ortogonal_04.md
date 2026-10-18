flowchart TD
    A[Matriz Q cuadrada] --> B{¿Calcular Q^T Q?}
    B -->|Sí| C[Multiplicar matrices]
    C --> D{¿Resultado = I?}
    D -->|Sí| E[✅ ES ORTOGONAL]
    D -->|No| F[❌ NO ES ORTOGONAL]
    B -->|No| G[Extraer columnas]
    G --> H[Verificar producto punto<br/>entre cada par]
    H --> I{¿Todos = 0?}
    I -->|No| F
    I -->|Sí| J[Calcular norma<br/>de cada columna]
    J --> K{¿Todas = 1?}
    K -->|Sí| E
    K -->|No| F
    style E fill:#e1ffe1
    style F fill:#ffe1e1
