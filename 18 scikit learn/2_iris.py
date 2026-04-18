# ==========================================================
# Dataset Iris - Il dataset più classico del Machine Learning
# ==========================================================
# Il dataset Iris contiene 150 campioni di fiori di iris, suddivisi in 3 specie:
#   - Setosa
#   - Versicolor
#   - Virginica
#
# Per ogni fiore sono state misurate 4 caratteristiche (feature):
#   - Lunghezza del sepalo (cm)
#   - Larghezza del sepalo (cm)
#   - Lunghezza del petalo (cm)
#   - Larghezza del petalo (cm)
#
# L'obiettivo è: date le 4 misure, prevedere a quale specie appartiene il fiore.
# È un problema di CLASSIFICAZIONE (l'output è una categoria, non un numero).

from sklearn.datasets import load_iris

# ==========================================================
# 1. Caricamento del dataset
# ==========================================================
# load_iris() restituisce un oggetto Bunch (simile a un dizionario) che contiene:
#   - data: array NumPy (150, 4) con le 4 feature per ogni campione
#   - target: array NumPy (150,) con le etichette (0 = setosa, 1 = versicolor, 2 = virginica)
#   - feature_names: nomi delle 4 feature
#   - target_names: nomi delle 3 specie
#
# Esempio di un campione:
#   Feature:  [5.1, 3.5, 1.4, 0.2]  => sepalo 5.1cm x 3.5cm, petalo 1.4cm x 0.2cm
#   Target:   0                       => specie "setosa"
data = load_iris()

# ==========================================================
# 2. Separazione feature (X) e target (y)
# ==========================================================
# X = le feature (input del modello): cosa il modello "vede"
#     Shape: (150, 4) => 150 fiori, 4 misurazioni ciascuno
X = data.data

# y = il target (output da prevedere): cosa il modello deve "indovinare"
#     Shape: (150,) => un'etichetta per ogni fiore (0, 1 o 2)
y = data.target

# ==========================================================
# 3. Esplorazione del dataset
# ==========================================================
# Stampa l'intero oggetto dataset (struttura, descrizione, dati)
print(data)

# Stampa i nomi delle 4 feature
# => ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
print(data.feature_names)

# Stampa i nomi delle 3 specie di iris
# => ['setosa' 'versicolor' 'virginica']
print(data.target_names)