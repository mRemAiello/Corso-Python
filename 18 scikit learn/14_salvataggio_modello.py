# ==========================================================
# Salvataggio e caricamento di modelli
# ==========================================================
# Addestrare un modello richiede tempo e risorse computazionali.
# Non ha senso ri-addestrarlo ogni volta che lo vogliamo usare!
#
# Per questo salviamo il modello su file e lo ricarichiamo quando serve.
# Ci sono due modi principali:
#
#   1. joblib (consigliato da scikit-learn)
#      - Ottimizzato per oggetti con grandi array NumPy
#      - Più veloce di pickle per modelli scikit-learn
#      - Estensione tipica: .joblib
#
#   2. pickle (modulo standard Python)
#      - Funziona con qualsiasi oggetto Python
#      - Più versatile ma meno ottimizzato per dati numerici
#      - Estensione tipica: .pkl
#
# ATTENZIONE: Non caricare MAI modelli da fonti non fidate!
# Un file pickle/joblib può contenere codice arbitrario che viene
# eseguito durante il caricamento (rischio di sicurezza).

import os
import joblib
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# ==========================================================
# 1. Addestramento del modello
# ==========================================================
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2, random_state=42
)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', LogisticRegression(max_iter=200))
])

pipeline.fit(X_train, y_train)

# Verifica accuratezza prima del salvataggio
y_pred = pipeline.predict(X_test)
acc_originale = accuracy_score(y_test, y_pred)
print(f"Accuratezza modello originale: {acc_originale * 100:.2f}%")

# ==========================================================
# 2. Salvataggio con joblib (metodo consigliato)
# ==========================================================
# joblib.dump() salva l'intero oggetto pipeline su file.
# Questo include lo scaler (con media e std) E il classificatore
# (con tutti i pesi appresi). Tutto in un unico file!
percorso_joblib = 'modello_iris.joblib'
joblib.dump(pipeline, percorso_joblib)

# Verifichiamo la dimensione del file salvato
dimensione = os.path.getsize(percorso_joblib)
print(f"\nSalvato con joblib: {percorso_joblib} ({dimensione} bytes)")

# ==========================================================
# 3. Caricamento con joblib
# ==========================================================
# joblib.load() ricrea l'oggetto identico a quello salvato.
# Possiamo usarlo subito per fare predizioni, senza ri-addestrare!
modello_caricato = joblib.load(percorso_joblib)

# Verifica che il modello caricato dia gli stessi risultati
y_pred_caricato = modello_caricato.predict(X_test)
acc_caricata = accuracy_score(y_test, y_pred_caricato)
print(f"Accuratezza modello caricato:  {acc_caricata * 100:.2f}%")
print(f"I risultati sono identici: {acc_originale == acc_caricata}")

# ==========================================================
# 4. Salvataggio con pickle (alternativa)
# ==========================================================
# pickle è il modulo standard di Python per la serializzazione.
# 'wb' = write binary (i file pickle sono binari, non testo).
percorso_pickle = 'modello_iris.pkl'
with open(percorso_pickle, 'wb') as f:
    pickle.dump(pipeline, f)

dimensione_pkl = os.path.getsize(percorso_pickle)
print(f"\nSalvato con pickle: {percorso_pickle} ({dimensione_pkl} bytes)")

# ==========================================================
# 5. Caricamento con pickle
# ==========================================================
# 'rb' = read binary
with open(percorso_pickle, 'rb') as f:
    modello_pickle = pickle.load(f)

y_pred_pickle = modello_pickle.predict(X_test)
acc_pickle = accuracy_score(y_test, y_pred_pickle)
print(f"Accuratezza modello pickle:    {acc_pickle * 100:.2f}%")

# ==========================================================
# 6. Uso pratico: predizione su nuovi dati
# ==========================================================
# Scenario reale: in un'applicazione, carichi il modello una volta
# e poi lo usi per fare predizioni su dati nuovi.
import numpy as np

print("\n" + "=" * 50)
print("Utilizzo del modello salvato:")
print("=" * 50)

nuovi_fiori = np.array([
    [5.1, 3.5, 1.4, 0.2],   # Misure tipiche di setosa
    [6.7, 3.0, 5.2, 2.3],   # Misure tipiche di virginica
    [5.9, 2.8, 4.5, 1.3],   # Misure tipiche di versicolor
])

predizioni = modello_caricato.predict(nuovi_fiori)

for i, (misure, pred) in enumerate(zip(nuovi_fiori, predizioni)):
    nome = data.target_names[pred]
    print(f"  Fiore {i+1}: {misure} => {nome}")

# ==========================================================
# 7. Pulizia dei file creati
# ==========================================================
# Rimuoviamo i file salvati per non lasciare spazzatura.
# In un progetto reale NON faresti questo!
os.remove(percorso_joblib)
os.remove(percorso_pickle)
print(f"\nFile rimossi: {percorso_joblib}, {percorso_pickle}")
