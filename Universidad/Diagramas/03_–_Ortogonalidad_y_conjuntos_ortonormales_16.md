graph TB
    A[Ortogonalidad] --> B[QR Factorization]
    A --> C[Proyecciones]
    B --> D[Eigen-descomposición]
C --> E[Mínimos Cuadrados]
D --> F[SVD]
E --> F
F --> G[PCA]
F --> H[Compresión]
G --> I[Machine Learning]
H --> I
style A fill:#e1ffe1
style F fill:#fff4e1
style I fill:#e1f5ff
