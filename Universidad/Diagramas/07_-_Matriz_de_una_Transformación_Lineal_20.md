flowchart TD
    A[Transformación T] --> B{¿Qué hacer?}
    
    B -->|Representar| C[Aplicar T a base]
    C --> D[Escribir columnas]
    D --> E["Matriz [T]"]
    
    B -->|Aplicar| F["Multiplicar [T]·v"]
    
    B -->|Componer| G["Multiplicar [S][T]"]
    G --> H[Orden: derecha a izq]
    
    B -->|Invertir| I{det ≠ 0?}
    I -->|Sí| J["Calcular [T]⁻¹"]
    I -->|No| K[No invertible]
    
    B -->|Cambiar base| L["Calcular P⁻¹[T]P"]
    L --> M[¿Diagonal?]
    M -->|Sí| N[✅ Base de eigenvectores]
    
    style E fill:#e1ffe1
    style J fill:#e1ffe1
    style K fill:#ffe1e1
    style N fill:#e1ffe1
