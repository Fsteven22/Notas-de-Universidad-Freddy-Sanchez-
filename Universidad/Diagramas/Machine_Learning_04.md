graph TD
    A[📊 Métricas de Clasificación] --> B[🎯 Accuracy]
    A --> C[🔍 Precision]
    A --> D[📈 Recall]
    A --> E[⚖️ F1-Score]
    A --> F[📈 ROC-AUC]
    
    B --> G[Casos correctos / Total casos]
    C --> H[VP / VP + FP]
    D --> I[VP / VP + FN]
    E --> J[2 × Precision × Recall / Precision + Recall]
    F --> K[Área bajo curva ROC]
    
    style A fill:#e8f5e8
    style B fill:#bbdefb
    style C fill:#fff3e0
    style D fill:#f3e5f5
    style E fill:#e1f5fe
    style F fill:#fce4ec
