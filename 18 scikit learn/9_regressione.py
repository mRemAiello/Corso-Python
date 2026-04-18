# ==========================================================
# Regressione Lineare - Prevedere valori numerici
# ==========================================================
# Finora abbiamo visto la CLASSIFICAZIONE (prevedere una categoria).
# La REGRESSIONE è l'altro grande tipo di problema supervisionato:
# prevede un VALORE NUMERICO continuo.
#
# Esempi di regressione:
#   - Prevedere il prezzo di una casa data la superficie
#   - Prevedere la temperatura di domani
#   - Prevedere il fatturato mensile
#
# La regressione lineare cerca la "retta migliore" che passa
# attraverso i punti del dataset. La formula è:
#   y = m * x + q
# dove m è la pendenza e q è l'intercetta.
#
# Con più feature (regressione multipla):
#   y = w1*x1 + w2*x2 + ... + wn*xn + b
# dove w1, w2, ... sono i pesi e b è il bias.

import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# ==========================================================
# 1. Caricamento del dataset California Housing
# ==========================================================
# Questo dataset contiene informazioni sulle case in California.
# L'obiettivo è prevedere il PREZZO MEDIANO delle case (in centinaia di migliaia di $).
# Feature: reddito medio, età della casa, num. stanze, popolazione, ecc.
data = fetch_california_housing()
X = data.data      # (20640, 8) => 20640 campioni, 8 feature
y = data.target    # (20640,) => prezzo mediano (valore continuo!)

print(f"Dimensioni dataset: {X.shape}")
print(f"Feature disponibili: {data.feature_names}")
print(f"Target: prezzo mediano delle case (in $100k)")
print(f"Range target: {y.min():.2f} - {y.max():.2f}\n")

# ==========================================================
# 2. Divisione train/test
# ==========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================================================
# 3. Normalizzazione
# ==========================================================
# La regressione lineare è sensibile alla scala delle feature.
# Feature con valori grandi avrebbero pesi sproporzionatamente grandi.
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ==========================================================
# 4. Creazione e addestramento del modello
# ==========================================================
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# ==========================================================
# 5. Predizione
# ==========================================================
y_pred = model.predict(X_test_scaled)

# ==========================================================
# 6. Metriche di valutazione per la regressione
# ==========================================================
# Per la regressione NON si usa l'accuracy (che è per la classificazione).
# Si usano metriche che misurano "quanto sbagli" in media:
#
#   MSE  (Mean Squared Error): errore quadratico medio
#        Penalizza di più gli errori grandi (perché li eleva al quadrato).
#        Valore perfetto = 0
#
#   RMSE (Root MSE): radice dell'MSE
#        Più intuitivo perché è nella stessa unità del target.
#        Es: RMSE = 0.7 significa "in media sbaglio di $70k"
#
#   MAE  (Mean Absolute Error): errore assoluto medio
#        Più robusto agli outlier rispetto all'MSE.
#        Es: MAE = 0.5 significa "in media sbaglio di $50k"
#
#   R²   (Coefficiente di determinazione): quanto il modello "spiega" i dati
#        R² = 1.0 => perfetto
#        R² = 0.0 => il modello non è meglio della media
#        R² < 0   => il modello è peggio della media (molto male!)

mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Metriche di valutazione:")
print("-" * 40)
print(f"  MSE  = {mse:.4f}")
print(f"  RMSE = {rmse:.4f}")
print(f"  MAE  = {mae:.4f}")
print(f"  R²   = {r2:.4f}")

# ==========================================================
# 7. Analisi dei coefficienti (pesi)
# ==========================================================
# I coefficienti ci dicono l'importanza e la direzione di ogni feature.
# Positivo => al crescere della feature, il prezzo aumenta
# Negativo => al crescere della feature, il prezzo diminuisce
print("\nCoefficienti del modello:")
print("-" * 50)
for nome, peso in zip(data.feature_names, model.coef_):
    direzione = "↑" if peso > 0 else "↓"
    print(f"  {nome:12s} => {peso:+.4f} {direzione}")

# L'intercetta è il valore base quando tutte le feature sono 0.
print(f"\n  Intercetta (bias): {model.intercept_:.4f}")

# ==========================================================
# 8. Esempio di predizione singola
# ==========================================================
# Prendiamo il primo campione del test set e confrontiamo
# il prezzo reale con quello predetto dal modello.
print(f"\nEsempio di predizione:")
print(f"  Prezzo reale:    ${y_test[0] * 100:.0f}k")
print(f"  Prezzo predetto: ${y_pred[0] * 100:.0f}k")
print(f"  Errore:          ${abs(y_test[0] - y_pred[0]) * 100:.0f}k")
