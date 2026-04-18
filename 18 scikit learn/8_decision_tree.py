# ==========================================================
# Decision Tree - Albero decisionale
# ==========================================================
# Un Decision Tree è un modello che prende decisioni attraverso
# una serie di domande binarie (sì/no) sulle feature.
#
# Esempio di come ragiona un albero per classificare un fiore Iris:
#   - "La lunghezza del petalo è < 2.5 cm?" => Sì => Setosa
#   - "La larghezza del petalo è < 1.75 cm?" => Sì => Versicolor
#   - Altrimenti => Virginica
#
# Vantaggi:
#   - Facilissimo da interpretare (si può visualizzare l'albero!)
#   - Non richiede normalizzazione delle feature
#   - Gestisce sia dati numerici che categorici
#
# Svantaggi:
#   - Tende all'overfitting (memorizza il training set)
#   - Instabile: piccole variazioni nei dati cambiano molto l'albero
#   - Può creare alberi troppo profondi e complessi
#
# Per limitare l'overfitting si usano parametri come:
#   - max_depth: profondità massima dell'albero
#   - min_samples_split: minimo numero di campioni per creare un ramo
#   - min_samples_leaf: minimo numero di campioni in ogni foglia

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.metrics import accuracy_score

# ==========================================================
# 1. Caricamento e divisione del dataset
# ==========================================================
data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==========================================================
# 2. Creazione dell'albero decisionale
# ==========================================================
# max_depth=3 limita la profondità dell'albero a 3 livelli.
# Senza questo parametro, l'albero crescerebbe fino a classificare
# perfettamente tutti i campioni del training set (overfitting).
tree = DecisionTreeClassifier(max_depth=3, random_state=42)

# ==========================================================
# 3. Addestramento
# ==========================================================
# L'albero analizza il training set e trova le "domande" migliori
# da fare sulle feature per separare le classi.
# Il criterio di default è "gini" (impurità di Gini), che misura
# quanto un nodo è "puro" (contiene una sola classe).
tree.fit(X_train, y_train)

# ==========================================================
# 4. Predizione e valutazione
# ==========================================================
y_pred = tree.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza Decision Tree: {accuracy * 100:.2f}%")

# ==========================================================
# 5. Visualizzazione testuale dell'albero
# ==========================================================
# export_text() mostra l'albero in formato leggibile.
# Ogni riga è una "domanda" che l'albero fa per classificare un campione.
# "class:" indica la predizione finale in quella foglia.
print("\nStruttura dell'albero decisionale:")
print("=" * 50)
tree_rules = export_text(tree, feature_names=data.feature_names)
print(tree_rules)

# ==========================================================
# 6. Importanza delle feature
# ==========================================================
# L'albero ci dice quali feature sono più utili per la classificazione.
# feature_importances_ restituisce un valore tra 0 e 1 per ogni feature.
# Più è alto, più quella feature è importante per le decisioni.
print("Importanza delle feature:")
print("-" * 40)
for nome, importanza in zip(data.feature_names, tree.feature_importances_):
    barra = "█" * int(importanza * 30)  # Barra grafica proporzionale
    print(f"  {nome:20s} => {importanza:.4f} {barra}")

# ==========================================================
# 7. Confronto: albero libero vs albero limitato
# ==========================================================
# Un albero senza limiti tende all'overfitting (memorizza il training set).
# Un albero troppo limitato rischia l'underfitting (troppo semplice).
print("\nConfronto profondità dell'albero:")
print("-" * 45)

for depth in [1, 2, 3, 5, 10, None]:
    dt = DecisionTreeClassifier(max_depth=depth, random_state=42)
    dt.fit(X_train, y_train)

    acc_train = accuracy_score(y_train, dt.predict(X_train))
    acc_test = accuracy_score(y_test, dt.predict(X_test))

    depth_str = f"{depth:2d}" if depth else "∞ "
    print(f"  max_depth={depth_str}  =>  Train: {acc_train*100:.1f}%  |  Test: {acc_test*100:.1f}%")

# Se la differenza tra train e test è grande => overfitting!
# Se entrambi sono bassi => underfitting!
