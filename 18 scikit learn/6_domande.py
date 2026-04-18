# ==========================================================
# Sistema interattivo di classificazione dei fiori Iris
# ==========================================================
# Questo script combina tutto ciò che abbiamo visto:
#   - Addestramento di un modello di ML (Pipeline + Logistic Regression)
#   - Interfaccia interattiva a menu per l'utente
#   - L'utente inserisce le misure di un fiore e il modello predice la specie
#
# È un esempio di come un modello addestrato può essere usato
# in un'applicazione pratica (anche se semplificata).

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# ==========================================================
# 1. Funzione per chiedere i dati all'utente e fare la predizione
# ==========================================================
# Questa funzione viene chiamata ogni volta che l'utente vuole classificare un fiore.
# Chiede le 4 misurazioni, le passa al modello e stampa il risultato.
def chiedi_e_predici():
    print("\nInserisci le caratteristiche del fiore da classificare:")
    try:
        # Chiede all'utente le 4 feature, le stesse usate nel dataset Iris.
        # Valori tipici di riferimento:
        #   Sepalo: lunghezza 4-8 cm, larghezza 2-4.5 cm
        #   Petalo: lunghezza 1-7 cm, larghezza 0.1-2.5 cm
        sepal_length = float(input("• Lunghezza sepalo (cm): "))
        sepal_width = float(input("• Larghezza sepalo (cm): "))
        petal_length = float(input("• Lunghezza petalo (cm): "))
        petal_width = float(input("• Larghezza petalo (cm): "))

        # Crea una lista 2D con i dati inseriti: [[5.1, 3.5, 1.4, 0.2]]
        # La doppia parentesi è necessaria perché predict() si aspetta
        # un array 2D (potrebbe ricevere più campioni contemporaneamente).
        features = [[sepal_length, sepal_width, petal_length, petal_width]]

        # La pipeline esegue automaticamente:
        #   1. StandardScaler normalizza i dati (con media/std del training set)
        #   2. LogisticRegression predice la classe (0, 1 o 2)
        prediction = pipeline.predict(features)

        # prediction[0] è un numero (0, 1 o 2).
        # target_names lo converte nel nome della specie: setosa, versicolor o virginica.
        print(f"\n🌸 Il fiore predetto è: {target_names[prediction[0]].capitalize()}\n")

    except ValueError:
        # Se l'utente inserisce un testo al posto di un numero, float() fallisce.
        print("\n❗ Errore: assicurati di inserire valori numerici validi.\n")


# ==========================================================
# 2. Caricamento e preparazione del dataset
# ==========================================================
data = load_iris()
X = data.data     # Feature: (150, 4)
y = data.target   # Target: (150,) => 0, 1, 2

# ==========================================================
# 3. Divisione train/test
# ==========================================================
# test_size=0.3: 30% per il test (45 campioni), 70% per il training (105 campioni)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ==========================================================
# 4. Pipeline: normalizzazione + classificazione
# ==========================================================
pipeline = Pipeline([
    ('scaler', StandardScaler()),                      # Normalizza le feature
    ('classifier', LogisticRegression(max_iter=200))   # Classifica
])

# ==========================================================
# 5. Addestramento del modello
# ==========================================================
# Il modello "impara" dal training set la relazione tra misure e specie.
pipeline.fit(X_train, y_train)

# ==========================================================
# 6. Valutazione automatica sul test set
# ==========================================================
# Prima di passare all'uso interattivo, verifichiamo che il modello
# funzioni bene sul test set (dati mai visti durante l'addestramento).
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza sul test set: {accuracy * 100:.2f}%\n")

# Array con i nomi delle 3 specie, usato per convertire 0/1/2 in nomi leggibili
target_names = data.target_names

# ==========================================================
# 7. Menu interattivo
# ==========================================================
# Un ciclo while infinito che mostra il menu e attende la scelta dell'utente.
# Opzione 1: chiede le misure e predice la specie
# Opzione 2: esce dal programma (break interrompe il while)
while True:
    print("=== Sistema di Classificazione Iris ===")
    print("1. Classifica un nuovo fiore")
    print("2. Esci")
    scelta = input("Seleziona un'opzione (1-2): ")

    if scelta == '1':
        chiedi_e_predici()
    elif scelta == '2':
        print("\n👋 Uscita dal programma. Arrivederci!\n")
        break
    else:
        print("\n❗ Scelta non valida. Riprova.\n")