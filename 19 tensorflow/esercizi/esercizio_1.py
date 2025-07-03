# Obiettivo: Creare un modello lineare per prevedere un valore numerico.
#
# Testo esercizio:
#
#     1️⃣ Genera dei dati di esempio:
#     X = [1, 2, 3, 4, 5]
#     Y = [2, 4, 6, 8, 10]
#
#     2️⃣ Costruisci un modello Sequential con un solo layer Dense (un neurone).
#     3️⃣ Compila il modello con la funzione di perdita MSE e un ottimizzatore SGD.
#     4️⃣ Allena il modello per almeno 200 epoche.
#     5️⃣ Stampa la previsione per X = 6.
#
#     Suggerimento: il risultato dovrebbe avvicinarsi a 12.


import tensorflow as tf
import numpy as np

# Dati di addestramento
X = np.array([1, 2, 3, 4, 5], dtype=float)
Y = np.array([2, 4, 6, 8, 10], dtype=float)

# Costruzione del modello
model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

# Compilazione
model.compile(optimizer='sgd', loss='mean_squared_error')

# Addestramento
model.fit(X, Y, epochs=200, verbose=0)

# Previsione
prediction = model.predict([6])
print("Predizione per X=6:", prediction[0])
