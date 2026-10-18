mindmap
  root((Gram-Schmidt))
    Concepto
      Ortogonalización
      Normalización
      Base ortonormal
      Preserva espacio
    Algoritmo
      Clásico
      Modificado
      Proyecciones
      Normalización
    Aplicaciones
      Factorización QR
      Mínimos cuadrados
      Procesamiento señales
      Gráficos 3D
    Propiedades
      Teoremas
      Estabilidad
      Condiciones de fallo
      Complejidad O(mn²)
````


---

## 🔗 Conexión con Próximos Temas

```mermaid
graph LR
    A[Gram-Schmidt] --> B[Factorización QR]
    B --> C[Mínimos cuadrados]
    C --> D[Regresión lineal]
    
    A --> E[Espacios con<br/>producto interno]
    E --> F[Polinomios<br/>ortogonales]
    F --> G[Series de Fourier]
    
    A --> H[Valores propios]
    H --> I[Algoritmo QR]
    I --> J[Diagonalización]
    
    B --> K[SVD]
    K --> L[PCA]
    
    style A fill:#e1ffe1
    style B fill:#fff4e1
    style K fill:#e1f5ff
