# Obiettivo: Imparare a gestire un problema di classificazione binaria.
#
# Testo esercizio:
#
#     1️⃣ Crea un dataset:
#     X = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     Y = [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
#     (considera Y=1 se X>=4)
#
#     2️⃣ Costruisci un modello sequenziale con:
#
#         1 layer Dense con 4 neuroni (attivazione relu)
#
#         1 layer Dense finale con 1 neurone (attivazione sigmoid)
#
#     3️⃣ Compila il modello con 'binary_crossentropy'.
#     4️⃣ Allena per 300 epoche.
#     5️⃣ Verifica l'output per X=2 e X=7.

import tensorflow as tf
import numpy as np

# Dataset
X = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)
Y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1], dtype=float)

# Costruzione del modello
model = tf.keras.Sequential([
    tf.keras.layers.Dense(4, activation='relu', input_shape=[1]),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compilazione
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Addestramento
model.fit(X, Y, epochs=300, verbose=0)

# Previsioni
print("Predizione per X=2:", model.predict([2])[0][0])
print("Predizione per X=7:", model.predict([7])[0][0])