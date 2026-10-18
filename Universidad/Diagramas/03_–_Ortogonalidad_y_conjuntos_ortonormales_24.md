graph TD
    A[Vector v] --> B[Base ortonormal<br/>u₁, u₂, ..., uₙ]
    B --> C1["c₁ = ⟨v, u₁⟩"]
    B --> C2["c₂ = ⟨v, u₂⟩"]
    B --> C3["cₙ = ⟨v, uₙ⟩"]
    C1 --> D["v = Σcᵢuᵢ"]
    C2 --> D
    C3 --> D
    D --> E["||v||² = Σcᵢ²<br/>(Parseval)"]
    style A fill:#e1f5ff
    style B fill:#fff4e1
    style D fill:#e1ffe1
    style E fill:#e1ffe1
````

---

## 🔄 Proceso de Gram-Schmidt

### 🎨 Algoritmo de Ortonormalización

[!example] 🛠️ Método de Gram-Schmidt
**Objetivo:** Transformar una base arbitraria {**v₁**, **v₂**, ..., **vₙ**} en una base ortonormal {**u₁**, **u₂**, ..., **uₙ**} que genere el mismo espacio.
**Algoritmo paso a paso:**
