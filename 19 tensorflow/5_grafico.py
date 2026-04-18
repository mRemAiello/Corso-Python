import tensorflow as tf
import matplotlib.pyplot as plt
from keras.src.datasets import mnist
from tensorflow.python.keras.utils.np_utils import to_categorical

# ==========================================================
# 1. Caricamento e pre-elaborazione dei dati
# ==========================================================
# Carichiamo il dataset MNIST (60.000 training + 10.000 test).
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Reshape: aggiungiamo il canale colore (1 = scala di grigi) e normalizziamo 0-1.
# Stessa pre-elaborazione usata in 2_tensorflow.py e 3_modello.py.
train_images = train_images.reshape(-1, 28, 28, 1).astype("float32") / 255
test_images = test_images.reshape(-1, 28, 28, 1).astype("float32") / 255

# One-hot encoding: trasforma le etichette in vettori di 10 elementi.
# Es: 5 => [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# ==========================================================
# 2. Costruzione del modello CNN
# ==========================================================
# Stessa architettura semplificata di 3_modello.py:
# un solo blocco Conv2D + MaxPooling, poi Flatten e Dense.
model = tf.keras.models.Sequential([
    # Conv2D: 32 filtri 3x3 che scorrono sull'immagine per estrarre feature (bordi, curve).
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),

    # MaxPooling: dimezza altezza e larghezza prendendo il massimo in finestre 2x2.
    tf.keras.layers.MaxPooling2D((2, 2)),

    # Flatten: appiattisce la mappa di feature 3D in un vettore 1D.
    tf.keras.layers.Flatten(),

    # Dense(64): layer fully connected che combina le feature per la classificazione.
    tf.keras.layers.Dense(64, activation='relu'),

    # Output: 10 neuroni (uno per cifra), softmax restituisce probabilità.
    tf.keras.layers.Dense(10, activation='softmax')
])

# ==========================================================
# 3. Compilazione
# ==========================================================
# optimizer='adam': aggiorna i pesi in modo adattivo.
# loss='categorical_crossentropy': misura l'errore per classificazione multiclasse.
# metrics=['accuracy']: monitora la percentuale di predizioni corrette.
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# ==========================================================
# 4. Addestramento
# ==========================================================
# epochs=10: il modello vede l'intero dataset 10 volte.
# batch_size=64: elabora 64 immagini per volta prima di aggiornare i pesi.
# validation_split=0.2: il 20% del training set viene usato per la validazione.
#
# IMPORTANTE: model.fit() restituisce un oggetto "history" che contiene
# lo storico di loss e accuracy per ogni epoca, sia su training che su validazione.
# Questo è fondamentale per creare i grafici di monitoraggio.
history = model.fit(train_images, train_labels,
                    epochs=10, batch_size=64,
                    validation_split=0.2)

# ==========================================================
# 5. Grafico della Loss (funzione di perdita)
# ==========================================================
# La LOSS misura quanto il modello "sbaglia" le predizioni.
# Valori più bassi = predizioni migliori.
#
# Cosa osservare:
#   - Entrambe le curve dovrebbero scendere col passare delle epoche.
#   - Se la loss di training scende MA quella di validazione sale,
#     il modello sta facendo OVERFITTING (memorizza i dati invece di generalizzare).
#   - Se entrambe restano alte, il modello sta facendo UNDERFITTING (non impara abbastanza).
plt.figure()
plt.plot(history.history['loss'], label='Loss Training')
plt.plot(history.history['val_loss'], label='Loss Validation')
plt.title('Loss durante l\'addestramento')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

# ==========================================================
# 6. Grafico dell'Accuracy (accuratezza)
# ==========================================================
# L'ACCURACY misura la percentuale di immagini classificate correttamente.
# Valori più alti = modello migliore (massimo = 1.0 cioè 100%).
#
# Cosa osservare:
#   - Entrambe le curve dovrebbero salire col passare delle epoche.
#   - Se l'accuracy di training è molto più alta di quella di validazione,
#     è un segnale di overfitting.
#   - L'accuracy di validazione è la metrica più importante perché indica
#     quanto il modello funzionerà su dati nuovi mai visti.
plt.figure()
plt.plot(history.history['accuracy'], label='Accuracy Training')
plt.plot(history.history['val_accuracy'], label='Accuracy Validation')
plt.title('Accuracy durante l\'addestramento')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()
