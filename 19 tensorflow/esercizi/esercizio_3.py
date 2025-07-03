# Obiettivo: Usare un dataset reale per il riconoscimento di immagini.
#
# Testo esercizio:
#
#     1️⃣ Carica il dataset MNIST (tf.keras.datasets.mnist.load_data())
#     2️⃣ Normalizza i dati (dividendo i pixel per 255).
#     3️⃣ Crea un modello sequenziale con:
#
#         un layer Flatten (28x28 -> 784)
#
#         un Dense con 128 neuroni (relu)
#
#         un Dense finale con 10 neuroni (softmax)
#
#     4️⃣ Compila con 'sparse_categorical_crossentropy' come loss.
#     5️⃣ Allena per 5 epoche.
#     6️⃣ Valuta la precisione sul test set.

import tensorflow as tf

# Caricamento dataset MNIST
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# Normalizzazione
X_train = X_train / 255.0
X_test = X_test / 255.0

# Costruzione del modello
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])

# Compilazione
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Addestramento
model.fit(X_train, y_train, epochs=5)

# Valutazione
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Accuratezza sul test set:", test_acc)
