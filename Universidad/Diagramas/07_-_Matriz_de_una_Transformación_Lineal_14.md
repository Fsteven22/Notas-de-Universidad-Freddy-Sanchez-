graph TD
    A[Matriz n×n] --> B{¿Simétrica?}
    B -->|Sí| C[✅ Siempre diagonalizable]
    B -->|No| D{¿n eigenvalores<br/>distintos?}
    D -->|Sí| E[✅ Diagonalizable]
    D -->|No| F[Verificar multiplicidad]
    F --> G{¿Suficientes<br/>eigenvectores?}
    G -->|Sí| H[✅ Diagonalizable]
    G -->|No| I[❌ No diagonalizable]
    style C fill:#e1ffe1
    style E fill:#e1ffe1
    style H fill:#e1ffe1
    style I fill:#ffe1e1
