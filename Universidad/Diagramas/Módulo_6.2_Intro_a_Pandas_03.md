graph TB
    A[📁 Archivos] --> B[📄 CSV]
    A --> C[📊 Excel]
    A --> D[🌐 JSON]
    A --> E[🔄 Otros]
    
    B --> F[pd.read_csv]
    B --> G[df.to_csv]
    
    C --> H[pd.read_excel]
    C --> I[df.to_excel]
    
    D --> J[pd.read_json]
    D --> K[df.to_json]
    
    E --> L[Parquet, SQL, HTML]
    
    style A fill:#fff3e0,stroke:#e65100,stroke-width:3px
    style B fill:#e8f5e8,stroke:#2e7d32,stroke-width:2px
    style C fill:#e3f2fd,stroke:#1565c0,stroke-width:2px
    style D fill:#fce4ec,stroke:#c2185b,stroke-width:2px
