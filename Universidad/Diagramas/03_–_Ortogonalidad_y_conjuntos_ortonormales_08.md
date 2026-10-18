flowchart TD
    A[Vector v] --> B["Calcular norma<br/>||v|| = √⟨v,v⟩"]
    B --> C{"||v|| = 0?"}
    C -->|Sí| D["❌ Error<br/>No se puede normalizar"]
    C -->|No| E["Dividir cada componente<br/>û = v/||v||"]
    E --> F["Verificar: ||û|| = 1"]
    F --> G[✅ Vector normalizado]
    style D fill:#ffe1e1
    style G fill:#e1ffe1
