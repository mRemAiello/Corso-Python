# Regressione con Keras
#
# La regressione è un problema di apprendimento supervisionato in cui si vuole
# prevedere un valore numerico continuo (es. prezzo, temperatura, età).
#
# Differenze rispetto alla classificazione:
#     - Layer di output: 1 neurone senza attivazione (lineare)
#     - Loss: mse (Mean Squared Error) o mae (Mean Absolute Error)
#     - Metriche: mae, mse, r2

import numpy as np
from keras import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

# ==========================================
# Esempio: Previsione del prezzo di una casa
# ==========================================

# 1. Generazione dati sintetici
#    Feature: superficie (m²), numero stanze, distanza dal centro (km), anno costruzione
np.random.seed(42)
n_campioni = 1000

superficie = np.random.uniform(30, 200, n_campioni)
stanze = np.random.randint(1, 7, n_campioni).astype(float)
distanza = np.random.uniform(0.5, 30, n_campioni)
anno = np.random.uniform(1960, 2024, n_campioni)

# Prezzo simulato (relazione lineare con un po' di rumore)
prezzo = (superficie * 2000 + stanze * 15000 - distanza * 3000 + (anno - 1960) * 500
          + np.random.normal(0, 20000, n_campioni))

# Assembliamo i dati
X = np.column_stack([superficie, stanze, distanza, anno])
y = prezzo

# 2. Normalizzazione dei dati (importante per la regressione!)
from sklearn.preprocessing import StandardScaler

scaler_X = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.reshape(-1, 1)).flatten()

# 3. Divisione train/test
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y_scaled, test_size=0.2, random_state=42
)

# 4. Costruzione del modello
model = Sequential([
    Dense(64, activation='relu', input_shape=(4,)),
    Dense(32, activation='relu'),
    Dense(16, activation='relu'),
    Dense(1)  # Output lineare per la regressione
])

model.summary()

# 5. Compilazione
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# 6. Addestramento
history = model.fit(
    X_train, y_train,
    epochs=100,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# 7. Valutazione
test_loss, test_mae = model.evaluate(X_test, y_test, verbose=0)
print(f"\nMSE sul test set: {test_loss:.4f}")
print(f"MAE sul test set: {test_mae:.4f}")

# 8. Predizione e confronto
y_pred_scaled = model.predict(X_test, verbose=0).flatten()

# Riconvertiamo ai valori originali
y_pred = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).flatten()
y_real = scaler_y.inverse_transform(y_test.reshape(-1, 1)).flatten()

print("\nConfronto predizioni vs reali (primi 5):")
for i in range(5):
    print(f"  Predetto: €{y_pred[i]:,.0f} | Reale: €{y_real[i]:,.0f}")

# 9. Grafico predizioni vs valori reali
plt.figure(figsize=(8, 6))
plt.scatter(y_real, y_pred, alpha=0.5, s=10)
plt.plot([y_real.min(), y_real.max()], [y_real.min(), y_real.max()], 'r--', linewidth=2)
plt.xlabel("Prezzo Reale (€)")
plt.ylabel("Prezzo Predetto (€)")
plt.title("Regressione - Predetto vs Reale")
plt.grid(True)
plt.tight_layout()
plt.show()
