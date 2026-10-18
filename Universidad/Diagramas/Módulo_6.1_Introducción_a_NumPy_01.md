graph TD
    A[🐍 Python Lists] -->|❌ Lento| B[⚡ NumPy Arrays]
    B -->|🏗️ Crear| C[np.array, np.zeros, np.ones]
    B -->|🔢 Tipos| D[int32, float64, bool]
    B -->|⚡ Operaciones| E[+, -, *, /, ufuncs]
    B -->|📊 Agregación| F[sum, mean, max, min]
    B -->|🎲 Random| G[rand, randn, randint, choice]
    
    style A fill:#ff6b6b
    style B fill:#4ecdc4
    style C fill:#45b7d1
    style D fill:#96ceb4
    style E fill:#ffeaa7
    style F fill:#dda0dd
    style G fill:#98d8c8
