# Soluzioni con NumPy (e un tocco di pandas per presentare i risultati in tabelle)

import numpy as np
import pandas as pd

# -----------------------------
# Esercizio 1
# -----------------------------
a = np.arange(1, 11)  # 1..10
b = np.arange(1, 11)  # 1..10
print(a, b)
print("Ufunc")
print(np.add(a, b))
print(np.subtract(3 * a, b))
print(np.multiply(a, b))
print(np.divide(3 * a, b))
print()

# -----------------------------
# Esercizio 2
# -----------------------------
x = np.linspace(0, 2*np.pi, 50)  # 50 valori tra 0 e 2π
sin_x = np.sin(x)
cos_x = np.cos(x)
tan_x = np.tan(x)
print("Trigonometria")
print(np.round(sin_x, 3))
print(np.round(cos_x, 3))
print(np.round(tan_x, 3))
print()

# -----------------------------
# Esercizio 3
# -----------------------------
np.random.seed(42)  # per ripetibilità della soluzione
data = np.random.normal(loc=0.0, scale=1.0, size=100)

stats = {
    "Somma": np.sum(data),
    "Media": np.mean(data),
    "Deviazione standard (ddof=0)": np.std(data),  # popolazione
    "Varianza (ddof=0)": np.var(data)
}

stats_df = pd.DataFrame(list(stats.items()), columns=["Misura", "Valore"]).round(6)
print("Statistiche su 100 valori ~ N(0,1)")
print(stats_df)

# Mostro anche i primi 20 valori del campione per completezza
sample_df = pd.DataFrame({"data (prime 20)": data[:20]}).round(6)
print("Campione data: prime 20 osservazioni")
print(sample_df)

# Stampo un breve riepilogo anche in output testuale
print("=== Riepilogo Esercizio 3 (N=100, seed=42) ===")
for k, v in stats.items():
    print(f"{k}: {v:.6f}")
