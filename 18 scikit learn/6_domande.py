from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


# Funzione per interrogare l'utente
def chiedi_e_predici():
    print("\nInserisci le caratteristiche del fiore da classificare:")
    try:
        sepal_length = float(input("• Lunghezza sepalo (cm): "))
        sepal_width = float(input("• Larghezza sepalo (cm): "))
        petal_length = float(input("• Lunghezza petalo (cm): "))
        petal_width = float(input("• Larghezza petalo (cm): "))

        # Prepara il dato per la predizione
        features = [[sepal_length, sepal_width, petal_length, petal_width]]

        # Predizione
        prediction = pipeline.predict(features)

        # Stampa il risultato
        print(f"\n🌸 Il fiore predetto è: {target_names[prediction[0]].capitalize()}\n")

    except ValueError:
        print("\n❗ Errore: assicurati di inserire valori numerici validi.\n")



# Caricamento dataset
data = load_iris()
X = data.data
y = data.target

# Suddivisione in train e test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Pipeline con scaler e modello di classificazione
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=200))
])

# Addestramento del modello
pipeline.fit(X_train, y_train)

# Predizione sul test set
y_pred = pipeline.predict(X_test)

# Calcolo dell'accuratezza
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza sul test set: {accuracy * 100:.2f}%\n")

# Dizionario per convertire l'indice predetto in nome del fiore
target_names = data.target_names


# Avvio del menu
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