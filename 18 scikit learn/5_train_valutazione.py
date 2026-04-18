# ==========================================================
# Training e Valutazione - Flusso completo di Machine Learning
# ==========================================================
# Questo file mette insieme tutti i passaggi visti finora:
#   1. Caricamento dati
#   2. Divisione train/test
#   3. Pre-elaborazione (StandardScaler)
#   4. Addestramento del modello (Logistic Regression)
#   5. Predizione su dati nuovi
#   6. Valutazione delle performance (accuracy)
#
# Il tutto è gestito tramite una Pipeline, che automatizza
# normalizzazione + addestramento in un unico oggetto.

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# ==========================================================
# 1. Caricamento del dataset Iris
# ==========================================================
data = load_iris()
X = data.data     # Feature: (150, 4)
y = data.target   # Target: (150,) => 0, 1 o 2

# ==========================================================
# 2. Divisione in train e test
# ==========================================================
# test_size=0.45: il 45% dei dati va al test (circa 67 campioni),
#   il restante 55% al training (circa 83 campioni).
# Un test set più grande ci dà una valutazione più affidabile,
# ma lascia meno dati per l'addestramento.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.45, random_state=42)

# ==========================================================
# 3. Creazione della Pipeline
# ==========================================================
# La Pipeline esegue in sequenza:
#   Step 1 - 'scaler': normalizza le feature (media=0, std=1)
#   Step 2 - 'classifier': Logistic Regression, un algoritmo di classificazione.
#
# Logistic Regression:
#   Nonostante il nome, è un algoritmo di CLASSIFICAZIONE (non regressione).
#   Calcola la probabilità che un campione appartenga a ciascuna classe
#   e assegna la classe con la probabilità più alta.
#   max_iter=200: numero massimo di iterazioni per trovare la soluzione ottimale.
#   (il default è 100, ma per alcuni dataset potrebbe non bastare)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=200))
])

# ==========================================================
# 4. Addestramento del modello (fit)
# ==========================================================
# pipeline.fit() esegue in sequenza:
#   1. Lo scaler "impara" media e deviazione standard dal training set
#   2. Lo scaler normalizza X_train
#   3. Il classificatore si addestra sui dati normalizzati + le etichette y_train
#
# Il modello impara la relazione: "date queste 4 misure => questa specie"
# Usa SOLO i dati di training. Il test set non viene mai toccato.
pipeline.fit(X_train, y_train)

# ==========================================================
# 5. Predizione sul test set
# ==========================================================
# pipeline.predict() esegue in sequenza:
#   1. Lo scaler normalizza X_test (usando media/std imparate dal training!)
#   2. Il classificatore predice le etichette per ogni campione del test
#
# y_pred contiene le predizioni del modello: [0, 2, 1, 1, 0, ...]
# y_test contiene le risposte corrette:     [0, 2, 1, 2, 0, ...]
# Confrontando i due array capiamo quante predizioni sono corrette.
y_pred = pipeline.predict(X_test)

# ==========================================================
# 6. Valutazione: calcolo dell'accuratezza
# ==========================================================
# accuracy_score confronta y_test (valori reali) con y_pred (predizioni).
# Conta quante predizioni sono corrette e divide per il totale.
# Es: 64 corrette su 67 test => accuracy = 64/67 = 95.52%
#
# L'accuracy è la metrica più semplice per la classificazione,
# ma non è sempre la migliore (es. con classi sbilanciate).
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza sul test set: {accuracy * 100:.2f}%")