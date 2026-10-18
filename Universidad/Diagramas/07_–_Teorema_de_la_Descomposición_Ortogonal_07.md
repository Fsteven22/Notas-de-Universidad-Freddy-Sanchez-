flowchart TD
    A[Vector y y subespacio W] --> B{¿Base ortogonal?}
    B -->|Sí| C[Calcular coeficientes<br/>cᵢ = y·uᵢ/‖uᵢ‖²]
    B -->|No| D[Ortonormalizar base<br/>Gram-Schmidt]
    D --> C
    C --> E[\hat{y} = Σ cᵢuᵢ]
    E --> F[z = y - \hat{y}]
    F --> G[Verificar \hat{y} · z = 0]
    style C fill:#e1ffe1
    style E fill:#fff4e1
    style G fill:#e1f5ff
````

### 🔄 Usando Base Ortonormal

[!success] ⚡ Simplificación con Vectores Unitarios
**Ventaja:** Si la base es ortonormal, los cálculos se simplifican considerablemente.
