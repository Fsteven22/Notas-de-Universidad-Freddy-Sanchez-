flowchart TD
    A[Tengo vectores] --> B{¿Son ortogonales?}
    
    B -->|No| C[Aplicar Gram-Schmidt]
    B -->|Sí| D{¿Son unitarios?}
    
    C --> E[Conjunto ortogonal]
    E --> D
    
    D -->|No| F[Normalizar]
    D -->|Sí| G[Ya son ortonormales]
    
    F --> G
    
    G --> H{¿Qué necesito?}
    
    H -->|Representar vector| I[Calcular coordenadas<br/>cᵢ = ⟨v,uᵢ⟩]
    H -->|Proyectar| J[proj = Σ⟨y,uᵢ⟩uᵢ]
    H -->|Resolver sistema| K[Usar QR o ecuaciones normales]
    H -->|Cambiar base| L[Matriz con uᵢ como columnas]
    
    style B fill:#fff4e1
    style D fill:#fff4e1
    style G fill:#e1ffe1
    style I fill:#e1f5ff
    style J fill:#e1f5ff
    style K fill:#e1f5ff
    style L fill:#e1f5ff
