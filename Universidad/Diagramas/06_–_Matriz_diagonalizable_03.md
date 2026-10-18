flowchart TD
    A[Analizar Matriz A] --> B[Calcular valores propios]
    B --> C{¿Todos distintos?}
    
    C -->|Sí| D[✅ Diagonalizable]
    C -->|No| E[Calcular multiplicidades]
    
    E --> F{Para cada λ:<br/>mult.geom = mult.alg?}
    
    F -->|Sí para todos| D
    F -->|No para alguno| G[❌ NO diagonalizable]
    
    style D fill:#e1ffe1
    style G fill:#ffe1e1
