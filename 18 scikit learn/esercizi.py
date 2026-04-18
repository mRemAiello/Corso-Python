# Esercizio 1: Dataset Iris
#
#     Carica il dataset Iris con load_iris()
#
#     Suddividi il dataset in train e test
#
#     Applica uno StandardScaler
#
#     Stampa i primi 5 valori scalati


# Esercizio 2: Dataset CSV
#
#     Importa un dataset a tua scelta (es. Titanic, Heart Disease)
#
#     Identifica le colonne numeriche e categoriche
#
#     Applica le trasformazioni appropriate (StandardScaler, LabelEncoder o OneHotEncoder)
#
#     Salva tutto in una pipeline


# Esercizio 3: KNN
#
#     Carica il dataset Iris e dividilo in train/test
#
#     Addestra un KNeighborsClassifier con K=3, K=7 e K=11
#
#     Confronta le accuratezze dei tre modelli
#
#     Quale K funziona meglio? Perche'?


# Esercizio 4: Decision Tree
#
#     Addestra un DecisionTreeClassifier sul dataset Iris
#
#     Prova con max_depth=2, max_depth=5, max_depth=None
#
#     Stampa l'importanza delle feature con feature_importances_
#
#     Qual e' la feature piu' importante? Ha senso?


# Esercizio 5: Regressione
#
#     Carica il dataset California Housing con fetch_california_housing()
#
#     Addestra una LinearRegression
#
#     Calcola MSE, RMSE, MAE e R2
#
#     Stampa i coefficienti del modello: quale feature influisce di piu'?


# Esercizio 6: Cross-Validation
#
#     Confronta LogisticRegression, KNN e DecisionTree usando cross_val_score
#
#     Usa cv=10
#
#     Stampa media e deviazione standard per ogni modello
#
#     Quale modello e' piu' stabile (std piu' bassa)?


# Esercizio 7: Confusion Matrix
#
#     Addestra un classificatore sul dataset Iris
#
#     Stampa la confusion matrix
#
#     Genera il classification_report
#
#     Ci sono classi che il modello confonde piu' spesso?


# Esercizio 8: Clustering
#
#     Applica KMeans sul dataset Iris SENZA usare le etichette (y)
#
#     Prova con n_clusters da 2 a 6
#
#     Calcola il Silhouette Score per ogni valore di K
#
#     Qual e' il numero ottimale di cluster?


# Esercizio 9: Grid Search
#
#     Crea una Pipeline con StandardScaler + SVC
#
#     Definisci una griglia con C=[0.1, 1, 10] e kernel=['linear', 'rbf']
#
#     Usa GridSearchCV con cv=5
#
#     Stampa i migliori iperparametri e l'accuratezza sul test set


# Esercizio 10: Progetto completo
#
#     Carica un dataset a scelta (Iris, California Housing, o un CSV)
#
#     Dividi in train/test
#
#     Addestra almeno 3 modelli diversi
#
#     Usa cross-validation per confrontarli
#
#     Ottimizza il migliore con GridSearchCV
#
#     Salva il modello finale con joblib
#
#     Ricaricalo e fai una predizione su dati nuovi