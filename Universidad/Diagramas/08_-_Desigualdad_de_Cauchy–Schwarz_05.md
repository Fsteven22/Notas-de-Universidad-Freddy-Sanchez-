flowchart TD
    A{Vectores u y v} --> B{¿Uno es cero?}
    B -->|Sí| C[Igualdad trivial<br/>0 = 0]
    B -->|No| D{¿Paralelos?}
    D -->|Sí| E[Igualdad alcanzada<br/>|⟨u,v⟩| = ||u|| ||v||]
    D -->|No| F{¿Ortogonales?}
    F -->|Sí| G[Desigualdad estricta<br/>0 < ||u|| ||v||]
    F -->|No| H[Desigualdad estricta<br/>|⟨u,v⟩| < ||u|| ||v||]
    style C fill:#e1ffe1
    style E fill:#e1ffe1
    style G fill:#fff4e1
    style H fill:#fff4e1
