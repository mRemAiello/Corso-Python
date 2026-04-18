# ==========================================================
# Grid Search - Ottimizzazione degli iperparametri
# ==========================================================
# Ogni modello di ML ha degli IPERPARAMETRI: valori che NOI scegliamo
# prima dell'addestramento e che influenzano le prestazioni.
#
# Esempi di iperparametri:
#   - KNN: n_neighbors (quanti vicini guardare?)
#   - Decision Tree: max_depth (quanto profondo può essere l'albero?)
#   - Logistic Regression: C (quanto regolarizzare?)
#   - SVM: C e kernel (lineare? RBF? polinomiale?)
#
# Come scegliere i valori migliori?
# GridSearchCV prova TUTTE le combinazioni possibili e trova la migliore!
#
# Funzionamento:
#   1. Definiamo una "griglia" di valori da provare per ogni iperparametro
#   2. GridSearchCV prova ogni combinazione
#   3. Per ogni combinazione fa Cross-Validation
#   4. Restituisce la combinazione con il punteggio migliore
#
# Esempio: se proviamo K=[1,3,5,7] con metric=['euclidean','manhattan']
#          GridSearchCV prova 4 * 2 = 8 combinazioni!

from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# ==========================================================
# 1. Caricamento e preparazione dati
# ==========================================================
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

# ==========================================================
# 2. Grid Search su KNN
# ==========================================================
print("Grid Search su KNN")
print("=" * 55)

# Pipeline: prima normalizza, poi classifica
pipeline_knn = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier())
])

# Definiamo la griglia di iperparametri da provare.
# I nomi devono seguire il formato: "nome_step__parametro"
# 'knn__n_neighbors' => parametro n_neighbors dello step 'knn'
param_grid_knn = {
    'knn__n_neighbors': [1, 3, 5, 7, 9, 11, 13, 15],
    'knn__weights': ['uniform', 'distance'],
    # 'uniform': tutti i vicini contano uguale
    # 'distance': i vicini più vicini contano di più
    'knn__metric': ['euclidean', 'manhattan']
    # 'euclidean': distanza "in linea d'aria"
    # 'manhattan': distanza "a blocchi" (come in una griglia stradale)
}

# Totale combinazioni: 8 * 2 * 2 = 32 combinazioni, ognuna con 5-fold CV!
# Quindi 32 * 5 = 160 addestramenti totali.
grid_search_knn = GridSearchCV(
    pipeline_knn,
    param_grid_knn,
    cv=5,                  # 5-Fold Cross-Validation
    scoring='accuracy',    # Metrica da ottimizzare
    n_jobs=-1,             # Usa tutti i core del processore (parallelizza!)
    verbose=0              # 0=silenzioso, 1=progresso, 2=dettagliato
)

grid_search_knn.fit(X_train, y_train)

# ==========================================================
# 3. Risultati KNN
# ==========================================================
print(f"\n  Migliori iperparametri: {grid_search_knn.best_params_}")
print(f"  Miglior score (CV):    {grid_search_knn.best_score_ * 100:.2f}%")

# Valutiamo sul test set (dati MAI visti durante la ricerca).
y_pred_knn = grid_search_knn.predict(X_test)
acc_knn = accuracy_score(y_test, y_pred_knn)
print(f"  Accuratezza test set:  {acc_knn * 100:.2f}%")

# ==========================================================
# 4. Grid Search su SVM (Support Vector Machine)
# ==========================================================
print("\n\nGrid Search su SVM")
print("=" * 55)

pipeline_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

# La SVM ha due iperparametri principali:
#   C:      controlla il trade-off tra margine ampio e errori di classificazione.
#           C grande => pochi errori sul training (rischio overfitting)
#           C piccolo => margine più ampio (più tollerante agli errori)
#   kernel: la funzione che trasforma i dati in uno spazio di dimensione superiore.
#           'linear' => per dati linearmente separabili
#           'rbf' => per dati non linearmente separabili (il più usato)
#           'poly' => separazione polinomiale
param_grid_svm = {
    'svm__C': [0.01, 0.1, 1, 10, 100],
    'svm__kernel': ['linear', 'rbf', 'poly'],
    'svm__gamma': ['scale', 'auto']
    # gamma: "raggio di influenza" di ogni campione (solo per rbf e poly)
}

grid_search_svm = GridSearchCV(
    pipeline_svm,
    param_grid_svm,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)

grid_search_svm.fit(X_train, y_train)

# ==========================================================
# 5. Risultati SVM
# ==========================================================
print(f"\n  Migliori iperparametri: {grid_search_svm.best_params_}")
print(f"  Miglior score (CV):    {grid_search_svm.best_score_ * 100:.2f}%")

y_pred_svm = grid_search_svm.predict(X_test)
acc_svm = accuracy_score(y_test, y_pred_svm)
print(f"  Accuratezza test set:  {acc_svm * 100:.2f}%")

# ==========================================================
# 6. Top 5 combinazioni per SVM
# ==========================================================
# GridSearchCV salva TUTTI i risultati in cv_results_.
# Possiamo analizzarli per vedere le migliori combinazioni.
import pandas as pd

results = pd.DataFrame(grid_search_svm.cv_results_)
# Ordiniamo per rank (1 = migliore)
top5 = results.nsmallest(5, 'rank_test_score')[
    ['params', 'mean_test_score', 'std_test_score', 'rank_test_score']
]

print("\n\nTop 5 combinazioni SVM:")
print("-" * 70)
for _, row in top5.iterrows():
    print(f"  #{int(row['rank_test_score'])} "
          f"Score: {row['mean_test_score']*100:.2f}% "
          f"(+/-{row['std_test_score']*100:.2f}%) "
          f"Params: {row['params']}")

# ==========================================================
# 7. Confronto finale
# ==========================================================
print("\n\nConfronto modelli ottimizzati:")
print("=" * 45)
print(f"  KNN ottimizzato: {acc_knn * 100:.2f}%")
print(f"  SVM ottimizzato: {acc_svm * 100:.2f}%")

vincitore = "KNN" if acc_knn > acc_svm else "SVM" if acc_svm > acc_knn else "Pareggio"
print(f"\n  Vincitore: {vincitore}")
