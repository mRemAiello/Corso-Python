# ==========================================================
# Elaborazione dei dati (Preprocessing)
# ==========================================================
# Prima di addestrare un modello di ML, i dati devono essere preparati.
# I passaggi principali sono:
#   1. Divisione in train e test set
#   2. Normalizzazione/Standardizzazione delle feature
#   3. Encoding delle variabili categoriche
#   4. Pipeline per automatizzare il tutto

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline

# ==========================================================
# 1. Caricamento del dataset Iris
# ==========================================================
data = load_iris()
X = data.data     # Feature: (150, 4) => 4 misurazioni per fiore
y = data.target   # Target: (150,) => 0, 1 o 2 (specie del fiore)
print(data.feature_names)   # Nomi delle 4 feature
print(data.target_names)    # Nomi delle 3 specie


# ==========================================================
# 2. Divisione del dataset: train e test
# ==========================================================
# Non possiamo addestrare E valutare il modello sugli stessi dati,
# altrimenti non sapremmo se funziona su dati nuovi (mai visti).
#
# train_test_split() divide casualmente i dati in due insiemi:
#   - X_train, y_train: per addestrare il modello (80%)
#   - X_test, y_test: per valutare le performance (20%)
#
# test_size=0.2: il 20% dei dati va al test set (30 campioni su 150)
# random_state=42: "seme" per la casualità, garantisce che la divisione
#   sia sempre la stessa ad ogni esecuzione (utile per la riproducibilità)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verifica: le prime 5 righe del training set
print(X_train[0:5])     # 5 campioni con 4 feature ciascuno
print(y_train[0:5])     # Le etichette corrispondenti
print()

# ==========================================================
# 3. Normalizzazione (Standardizzazione)
# ==========================================================
# Le feature possono avere scale molto diverse:
#   - Lunghezza sepalo: 4.3 - 7.9 cm
#   - Larghezza petalo: 0.1 - 2.5 cm
#
# Molti algoritmi (es. SVM, KNN, reti neurali) funzionano meglio
# quando tutte le feature hanno la stessa scala.
#
# StandardScaler trasforma ogni feature in modo che abbia:
#   - Media = 0
#   - Deviazione standard = 1
# Formula: z = (x - media) / deviazione_standard
#
# fit_transform(): prima "impara" media e deviazione (fit),
#   poi trasforma i dati (transform). In un solo passaggio.
#
# Alternativa: MinMaxScaler scala i valori nell'intervallo [0, 1]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Prima della normalizzazione: [5.1, 3.5, 1.4, 0.2]
# Dopo la normalizzazione:     [-0.90, 1.01, -1.34, -1.31]  (valori centrati su 0)
print(X_scaled[0:5])
print()


# ==========================================================
# 4. Encoding (Codifica delle variabili categoriche)
# ==========================================================
# I modelli di ML lavorano solo con NUMERI, non con stringhe.
# Se il target o le feature sono categoriche (es. "setosa", "maschio"),
# bisogna convertirle in numeri.
#
# LabelEncoder: assegna un numero intero a ogni categoria.
#   "setosa" => 0, "versicolor" => 1, "virginica" => 2
#   Utile per il target (etichette).
#   Nota: nel caso di Iris, y è già numerico (0, 1, 2), quindi il
#   LabelEncoder non cambia nulla. Lo mostriamo a scopo didattico.
#
# OneHotEncoder: crea una colonna binaria per ogni categoria.
#   "setosa"     => [1, 0, 0]
#   "versicolor" => [0, 1, 0]
#   "virginica"  => [0, 0, 1]
#   Utile per le feature categoriche (evita che il modello pensi
#   che 2 > 1 > 0, come se ci fosse un ordine tra le categorie).
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)


# ==========================================================
# 5. Pipeline
# ==========================================================
# Una Pipeline raggruppa più passaggi di pre-elaborazione in un unico oggetto.
# Vantaggi:
#   - Codice più pulito e organizzato
#   - Evita errori (applica gli stessi passaggi a train e test)
#   - Si può aggiungere anche il modello (vedremo nella prossima lezione)
#
# Ogni step è una tupla ('nome', Trasformatore).
# I dati passano da uno step all'altro in sequenza:
#   Dati grezzi -> StandardScaler -> Dati normalizzati
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    # ('encoder', OneHotEncoder()),  # se necessario
    # ('model', LogisticRegression())  # nella prossima lezione
])
X_transformed = pipeline.fit_transform(X)

# Il risultato è identico a quello ottenuto con scaler.fit_transform(X)
print(X_transformed[0:5])