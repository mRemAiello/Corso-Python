# ==========================================================
# Cross-Validation - Validazione incrociata
# ==========================================================
# Finora abbiamo diviso i dati in un UNICO train/test split.
# Il problema: il risultato dipende MOLTO da come vengono divisi i dati.
# Con un split fortunato => alta accuratezza. Con uno sfortunato => bassa.
#
# La Cross-Validation risolve questo problema:
#   1. Divide il dataset in K parti uguali (chiamate "fold")
#   2. Per ogni fold:
#      - Usa quel fold come test set
#      - Usa tutti gli altri fold come training set
#      - Calcola l'accuratezza
#   3. Fa la media di tutte le accuratezze
#
# Esempio con K=5 (5-Fold Cross-Validation):
#   Fold 1: [TEST] [train] [train] [train] [train]
#   Fold 2: [train] [TEST] [train] [train] [train]
#   Fold 3: [train] [train] [TEST] [train] [train]
#   Fold 4: [train] [train] [train] [TEST] [train]
#   Fold 5: [train] [train] [train] [train] [TEST]
#
# Ogni campione viene usato ESATTAMENTE una volta come test.
# Il risultato è molto più affidabile di un singolo split.

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import numpy as np

# ==========================================================
# 1. Caricamento del dataset
# ==========================================================
data = load_iris()
X = data.data
y = data.target

# ==========================================================
# 2. Cross-Validation con Logistic Regression
# ==========================================================
# cross_val_score() fa tutto automaticamente:
#   - Divide i dati in cv=5 fold
#   - Per ogni fold: addestra, predice, calcola l'accuratezza
#   - Restituisce un array con 5 accuratezze
pipeline_lr = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=200))
])

# cv=5 significa 5-Fold Cross-Validation.
# scoring='accuracy' specifica la metrica da usare.
scores = cross_val_score(pipeline_lr, X, y, cv=5, scoring='accuracy')

print("Cross-Validation con Logistic Regression:")
print(f"  Accuratezze per fold: {scores}")
print(f"  Media:  {scores.mean() * 100:.2f}%")
print(f"  Std:    {scores.std() * 100:.2f}%")
# La deviazione standard (std) ci dice quanto i risultati variano tra i fold.
# Std bassa => il modello è stabile. Std alta => il modello è instabile.

# ==========================================================
# 3. Confronto tra diversi modelli
# ==========================================================
# La cross-validation è perfetta per CONFRONTARE modelli.
# Usiamo la stessa procedura su diversi algoritmi e vediamo quale funziona meglio.
modelli = {
    'Logistic Regression': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', LogisticRegression(max_iter=200))
    ]),
    'KNN (K=5)': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', KNeighborsClassifier(n_neighbors=5))
    ]),
    'Decision Tree': DecisionTreeClassifier(max_depth=3, random_state=42),
    'SVM (Support Vector Machine)': Pipeline([
        ('scaler', StandardScaler()),
        ('clf', SVC(kernel='rbf'))
    ]),
}

print("\n" + "=" * 55)
print("Confronto modelli con 5-Fold Cross-Validation:")
print("=" * 55)

risultati = {}
for nome, modello in modelli.items():
    scores = cross_val_score(modello, X, y, cv=5, scoring='accuracy')
    media = scores.mean()
    std = scores.std()
    risultati[nome] = media
    print(f"\n  {nome}:")
    print(f"    Fold scores: {[f'{s:.3f}' for s in scores]}")
    print(f"    Media: {media*100:.2f}% (+/- {std*100:.2f}%)")

# ==========================================================
# 4. Classifica finale
# ==========================================================
# Ordiniamo i modelli dal migliore al peggiore.
print("\n" + "=" * 55)
print("Classifica finale:")
print("=" * 55)

classifica = sorted(risultati.items(), key=lambda x: x[1], reverse=True)
for posizione, (nome, media) in enumerate(classifica, 1):
    medaglia = ["🥇", "🥈", "🥉", "  "][posizione - 1]
    print(f"  {medaglia} {posizione}. {nome}: {media*100:.2f}%")

# ==========================================================
# 5. Diversi numeri di fold
# ==========================================================
# Quanti fold usare?
#   - cv=5: il più comune, buon bilanciamento
#   - cv=10: più preciso ma più lento
#   - cv=len(X): Leave-One-Out (LOO), molto preciso ma lentissimo
print("\n\nEffetto del numero di fold (Logistic Regression):")
print("-" * 45)

for k in [3, 5, 10, 20]:
    scores = cross_val_score(pipeline_lr, X, y, cv=k, scoring='accuracy')
    print(f"  cv={k:2d}  =>  Media: {scores.mean()*100:.2f}%  Std: {scores.std()*100:.2f}%")
