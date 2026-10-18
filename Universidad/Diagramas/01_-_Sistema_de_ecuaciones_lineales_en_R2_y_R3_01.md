graph TD
    A[Sistema de Ecuaciones Lineales] --> B{¿Tiene solución?}
    
    B -->|NO| C[Incompatible<br/>❌ Sin solución<br/>Ecuaciones contradictorias]
    
    B -->|SÍ| D[Compatible<br/>✓ Con solución]
    
    D --> E{¿Cuántas soluciones?}
    
    E -->|UNA| F[Compatible Determinado<br/>🎯 Solución única<br/>rango A = rango AB = n]
    
    E -->|INFINITAS| G[Compatible Indeterminado<br/>∞ Infinitas soluciones<br/>rango A = rango AB < n]
    
    style A fill:#e3f2fd
    style B fill:#fff9c4
    style C fill:#ffcdd2
    style D fill:#c8e6c9
    style E fill:#fff9c4
    style F fill:#bbdefb
    style G fill:#ffe0b2
