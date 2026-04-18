# ==========================================================
# Dataset CSV - Caricamento di un dataset reale (Titanic)
# ==========================================================
# A differenza di Iris (già incluso in Scikit-Learn), qui carichiamo
# un dataset esterno da un file CSV: il famoso dataset del Titanic.
#
# Obiettivo: prevedere se un passeggero è SOPRAVVISSUTO al naufragio
# in base alle sue caratteristiche (età, sesso, classe, ecc.).
# È un problema di CLASSIFICAZIONE BINARIA (sopravvissuto: sì=1 / no=0).

import pandas as pd

# ==========================================================
# 1. Caricamento del dataset da file CSV
# ==========================================================
# read_csv() legge il file e lo trasforma in un DataFrame Pandas.
# Ogni riga è un passeggero, ogni colonna è una caratteristica.
# Colonne tipiche del Titanic: PassengerId, Pclass, Name, Sex, Age,
#                               SibSp, Parch, Ticket, Fare, Cabin, Embarked, Survived
df = pd.read_csv('dataset.csv')

# ==========================================================
# 2. Separazione tra feature (X) e target (y)
# ==========================================================
# X = le feature (input): tutte le informazioni sul passeggero.
#   drop() rimuove le colonne che NON devono essere feature:
#   - 'Survived': è il target (ciò che vogliamo prevedere), non un input
#   - 'Cabin': ha troppi valori mancanti (NaN), quindi la scartiamo
#   axis=1 indica che stiamo eliminando COLONNE (axis=0 sarebbe per le righe)
#
# Esempio di una riga di X:
#   PassengerId=1, Pclass=3, Name="Braund", Sex="male", Age=22, Fare=7.25, ...
X = df.drop(['Survived', 'Cabin'], axis=1)

# y = il target (output): ciò che il modello deve prevedere.
#   0 = non sopravvissuto, 1 = sopravvissuto
y = df['Survived']

# ==========================================================
# 3. Esplorazione dei dati
# ==========================================================
# head(5): mostra le prime 5 righe del DataFrame.
# Utile per verificare che i dati siano stati caricati correttamente
# e capire la struttura delle feature.
print(X.head(5))
print()
# Mostra i primi 5 valori del target (0 o 1)
print(y.head(5))