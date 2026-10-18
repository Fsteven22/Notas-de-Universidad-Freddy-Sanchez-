flowchart TD
    A[Base de W:<br/> v₁,...,vₖ ] --> B[Formar A = v₁...vₖ ]
    B --> C[Calcular A^T A]
    C --> D{¿Invertible?}
    D -->|No| E[❌ Vectores no<br/>independientes]
    D -->|Sí| F[Calcular A^T A ^-1]
    F --> G[Calcular A^T]
    G --> H[P = A A^T A ^-1 A^T]
    H --> I[Verificar propiedades]
    style H fill:#e1ffe1
    style I fill:#fff4e1
````

### ⚡ Optimización: Usar Base Ortonormal

[!success] 🚀 Método Eficiente
**Estrategia recomendada:**
