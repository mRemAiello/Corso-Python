# ==========================================================
# Confusion Matrix e Classification Report
# ==========================================================
# L'accuracy da sola non basta! Consideriamo questo scenario:
#   - Dataset con 95 email normali e 5 spam
#   - Un modello che predice SEMPRE "normale" ha accuracy del 95%!
#   - Ma non ha identificato NESSUNO spam!
#
# Per capire meglio le performance servono metriche più dettagliate.
#
# CONFUSION MATRIX (Matrice di confusione):
# È una tabella che mostra quante predizioni sono corrette e quante sbagliate.
#
#                     Predetto: Positivo   Predetto: Negativo
# Reale: Positivo         TP                    FN
# Reale: Negativo         FP                    TN
#
#   TP (True Positive):  correttamente classificato come positivo
#   TN (True Negative):  correttamente classificato come negativo
#   FP (False Positive): classificato positivo ma era negativo (falso allarme)
#   FN (False Negative): classificato negativo ma era positivo (mancata rilevazione)
#
# METRICHE DERIVATE:
#   Precision = TP / (TP + FP) => "di tutti quelli che ho detto positivi, quanti lo erano davvero?"
#   Recall    = TP / (TP + FN) => "di tutti i positivi reali, quanti ne ho trovati?"
#   F1-Score  = 2 * (Precision * Recall) / (Precision + Recall) => media armonica

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    ConfusionMatrixDisplay
)
import numpy as np

# ==========================================================
# 1. Preparazione: addestramento del modello
# ==========================================================
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.3, random_state=42
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('clf', LogisticRegression(max_iter=200))
])
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

# ==========================================================
# 2. Confusion Matrix
# ==========================================================
# Per il dataset Iris (3 classi), la matrice è 3x3.
# Ogni riga rappresenta la classe REALE, ogni colonna la classe PREDETTA.
#
# Esempio di lettura:
#   cm[0][0] = campioni che sono setosa E il modello ha detto setosa (corretto!)
#   cm[0][1] = campioni che sono setosa MA il modello ha detto versicolor (errore!)
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Versione più leggibile:
print("\nConfusion Matrix dettagliata:")
print(f"{'':15s} {'Pred Setosa':>12s} {'Pred Versic.':>12s} {'Pred Virgin.':>12s}")
print("-" * 55)
for i, nome in enumerate(data.target_names):
    riga = "  ".join(f"{cm[i][j]:10d}" for j in range(3))
    print(f"  Reale {nome:10s} {riga}")

# ==========================================================
# 3. Classification Report
# ==========================================================
# Mostra precision, recall, f1-score per OGNI classe.
# È il modo più completo per valutare un classificatore.
print("\nClassification Report:")
print("=" * 55)
report = classification_report(
    y_test, y_pred,
    target_names=data.target_names
)
print(report)

# ==========================================================
# 4. Interpretazione delle metriche
# ==========================================================
# Lettura del report:
#   precision: dei fiori predetti come X, quanti lo sono davvero?
#   recall:    dei fiori realmente X, quanti sono stati trovati?
#   f1-score:  media bilanciata tra precision e recall
#   support:   quanti campioni reali ci sono per ogni classe
#
#   accuracy:     accuratezza complessiva
#   macro avg:    media semplice delle metriche per classe
#   weighted avg: media pesata per il numero di campioni per classe

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza complessiva: {accuracy * 100:.2f}%")

# ==========================================================
# 5. Analisi degli errori
# ==========================================================
# Vediamo esattamente DOVE il modello sbaglia.
print("\nAnalisi degli errori:")
print("-" * 55)

errori = np.where(y_test != y_pred)[0]  # Indici dove la predizione è sbagliata

if len(errori) == 0:
    print("  Nessun errore! Il modello ha classificato tutto correttamente.")
else:
    print(f"  Totale errori: {len(errori)} su {len(y_test)} campioni")
    for idx in errori:
        reale = data.target_names[y_test[idx]]
        predetto = data.target_names[y_pred[idx]]
        print(f"  Campione {idx}: reale={reale}, predetto={predetto}")
        print(f"    Feature: {X_test[idx]}")
