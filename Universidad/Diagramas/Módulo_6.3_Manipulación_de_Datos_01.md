graph TD
    A[📥 Cargar Dataset] --> B[🔍 Exploración Inicial]
    B --> C[📊 Estadísticas Descriptivas]
    C --> D{🤔 ¿Filtrado Necesario?}
    D -->|Sí| E[⚙️ Aplicar Filtros]
    D -->|No| F[🎲 GroupBy Análisis]
    E --> F
    F --> G[📈 Agregaciones]
    G --> H[📊 Visualización]
    H --> I[🧠 Interpretación]
    I --> J[📝 Conclusiones]
    style A fill:#e1f5fe
    style F fill:#f3e5f5
    style H fill:#fff3e0
    style J fill:#e8f5e8
