# Obiettivo: Imparare a salvare e ricaricare un modello addestrato.
#
# Testo esercizio:
#
#     1️⃣ Usa un modello che hai già creato (puoi riutilizzare quello dell’esercizio 2 o 3).
#     2️⃣ Salva il modello nel formato TensorFlow SavedModel.
#     3️⃣ Cancella il modello dalla memoria.
#     4️⃣ Ricarica il modello salvato.
#     5️⃣ Esegui una previsione per verificare che il modello caricato funzioni correttamente.


import tensorflow as tf
import numpy as np
import os

# Per semplicità, usiamo il modello dell’esercizio 2
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(X, Y, epochs=200, verbose=0)

# Salvare il modello
model.save("my_model")

# Cancelliamo il modello dalla memoria
del model

# Ricaricare il modello
loaded_model = tf.keras.models.load_model("my_model")

# Verifica
prediction = loaded_model.predict([6])
print("Predizione dopo il caricamento:", prediction[0][0])
