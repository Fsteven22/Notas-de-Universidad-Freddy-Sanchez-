flowchart LR
    A[Señal original s] --> B[Matriz P<br/>bajas frecuencias]
    B --> C[s_bajo = Ps]
    A --> D[Matriz I-P<br/>altas frecuencias]
    D --> E[s_alto = I-P s]
    C --> F[Señal filtrada]
    E --> G[Ruido eliminado]
    style C fill:#e1ffe1
    style E fill:#fff4e1
