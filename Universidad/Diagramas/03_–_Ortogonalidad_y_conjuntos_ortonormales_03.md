graph LR
    A[Producto Interno] --> B{⟨u,v⟩ = ?}
    B -->|= 0| C[✅ Ortogonales<br/>Ángulo = 90°]
    B -->|> 0| D[❌ Ángulo agudo<br/>0° < θ < 90°]
    B -->|< 0| E[❌ Ángulo obtuso<br/>90° < θ < 180°]
    style C fill:#e1ffe1
    style D fill:#fff4e1
    style E fill:#ffe1e1
