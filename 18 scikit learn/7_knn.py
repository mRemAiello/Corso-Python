# ==========================================================
# K-Nearest Neighbors (KNN) - Classificatore basato sui vicini
# ==========================================================
# KNN è uno degli algoritmi più semplici e intuitivi del Machine Learning.
#
# Come funziona:
#   1. Riceve un nuovo dato da classificare
#   2. Cerca i K punti più vicini nel training set (i "vicini")
#   3. Assegna la classe più frequente tra quei K vicini
#
# Esempio pratico:
#   Se K=3 e i 3 vicini più vicini sono: setosa, setosa, versicolor
#   Il modello predice "setosa" (2 su 3).
#
# Vantaggi:
#   - Semplicissimo da capire
#   - Non ha una fase di "training" vera e propria (memorizza i dati)
#   - Funziona bene con pochi dati
#
# Svantaggi:
#   - Lento con dataset grandi (deve calcolare tutte le distanze)
#   - Sensibile alla scala delle feature (serve StandardScaler!)
#   - K va scelto con cura (troppo basso = rumore, troppo alto = troppo generico)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# ==========================================================
# 1. Caricamento del dataset Iris
# ==========================================================
data = load_iris()
X = data.data      # 150 campioni, 4 feature ciascuno
y = data.target    # 0=setosa, 1=versicolor, 2=virginica

# ==========================================================
# 2. Divisione train/test (80% train, 20% test)
# ==========================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================================================
# 3. Normalizzazione delle feature
# ==========================================================
# KNN calcola le DISTANZE tra i punti, quindi è fondamentale
# che tutte le feature siano sulla stessa scala.
# Senza normalizzazione, una feature con valori grandi (es. 1-1000)
# dominerebbe su una con valori piccoli (es. 0.1-2.5).
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # Calcola media/std dal train e trasforma
X_test_scaled = scaler.transform(X_test)          # Usa media/std del train per trasformare il test

# ==========================================================
# 4. Creazione del modello KNN
# ==========================================================
# n_neighbors=5 => il modello guarda i 5 punti più vicini.
# Valori comuni: 3, 5, 7 (sempre numeri dispari per evitare pareggi).
knn = KNeighborsClassifier(n_neighbors=5)

# ==========================================================
# 5. Addestramento
# ==========================================================
# In realtà KNN non "impara" nulla: memorizza tutto il training set.
# La predizione avviene calcolando le distanze al momento del predict().
knn.fit(X_train_scaled, y_train)

# ==========================================================
# 6. Predizione e valutazione
# ==========================================================
y_pred = knn.predict(X_test_scaled)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza KNN (K=5): {accuracy * 100:.2f}%")

# ==========================================================
# 7. Confronto con valori diversi di K
# ==========================================================
# Proviamo K da 1 a 15 per vedere quale dà i risultati migliori.
print("\nConfronto con diversi valori di K:")
print("-" * 35)

for k in range(1, 16):
    knn_temp = KNeighborsClassifier(n_neighbors=k)
    knn_temp.fit(X_train_scaled, y_train)
    y_pred_temp = knn_temp.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred_temp)
    print(f"  K={k:2d}  =>  Accuratezza: {acc * 100:.2f}%")

# ==========================================================
# 8. Predizione su un singolo campione
# ==========================================================
# Proviamo a classificare un fiore con misure inventate.
# ATTENZIONE: dobbiamo normalizzare anche il nuovo dato con lo stesso scaler!
import numpy as np

nuovo_fiore = np.array([[5.0, 3.4, 1.5, 0.2]])         # Misure grezze
nuovo_fiore_scaled = scaler.transform(nuovo_fiore)       # Normalizzazione
predizione = knn.predict(nuovo_fiore_scaled)              # Predizione
nome_specie = data.target_names[predizione[0]]

print(f"\nNuovo fiore {nuovo_fiore[0]} => Predizione: {nome_specie}")
