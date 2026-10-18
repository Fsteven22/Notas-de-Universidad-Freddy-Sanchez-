graph TD
    A[Gram-Schmidt Clásico] --> B[v₂ - proy₁ - proy₂ - ...]
    A --> C[Todas las proyecciones<br/>sobre vectores originales]
    C --> D[⚠️ Acumula errores]
    E[Gram-Schmidt Modificado] --> F[v₂ - proy₁]
    F --> G[Actualizar v₂]
    G --> H[v₃ - proy₁']
    H --> I[Actualizar v₃]
    I --> J[✓ Reduce errores]
    style D fill:#ffe1e1
    style J fill:#e1ffe1
````
**Ejemplo de diferencia numérica:**
