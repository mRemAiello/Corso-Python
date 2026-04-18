import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# ==========================================================
# 1. Caricamento del dataset MNIST
# ==========================================================
# MNIST contiene 70.000 immagini di cifre scritte a mano (0-9), in scala di grigi 28x28.
# load_data() le divide automaticamente in:
#   - 60.000 immagini di training (per addestrare il modello)
#   - 10.000 immagini di test (per valutare le performance su dati mai visti)
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# ==========================================================
# 2. Pre-elaborazione dei dati
# ==========================================================
# reshape(-1, 28, 28, 1): aggiunge la dimensione del canale colore.
#   -1 significa "calcola automaticamente il numero di campioni".
#   Il risultato è (60000, 28, 28, 1) => 1 canale perché le immagini sono in scala di grigi.
#   Conv2D richiede un input 4D: (campioni, altezza, larghezza, canali).
#
# astype("float32") / 255: normalizza i pixel da [0, 255] a [0.0, 1.0].
#   Valori più piccoli e uniformi permettono alla rete di imparare più velocemente.
train_images = train_images.reshape((-1, 28, 28, 1)).astype("float32") / 255
test_images = test_images.reshape((-1, 28, 28, 1)).astype("float32") / 255

# ==========================================================
# 3. One-hot encoding delle etichette
# ==========================================================
# Trasforma ogni etichetta in un vettore di 10 elementi.
# Esempio: 3 => [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
#          7 => [0, 0, 0, 0, 0, 0, 0, 1, 0, 0]
# Serve perché il layer di output ha 10 neuroni con softmax,
# e ciascuno rappresenta la probabilità di una delle 10 cifre.
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# ==========================================================
# 4. Creazione del modello (CNN semplificata)
# ==========================================================
# Rispetto al modello in 2_tensorflow.py, questa CNN è più semplice:
# ha un solo strato convoluzionale + pooling, invece di tre.
# È più veloce da addestrare, ma potenzialmente meno precisa.
model = models.Sequential([
    # Conv2D(32, (3,3)): strato convoluzionale con 32 filtri di dimensione 3x3.
    #   Ogni filtro scorre sull'immagine e impara a riconoscere un pattern (bordi, curve, ecc.).
    #   activation='relu': azzera i valori negativi, introducendo non-linearità.
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)),

    # MaxPooling2D(2,2): riduce le dimensioni prendendo il valore massimo in finestre 2x2.
    #   Dimezza altezza e larghezza => meno calcoli e maggiore robustezza.
    layers.MaxPooling2D((2,2)),

    # Flatten: appiattisce la mappa di feature 3D in un vettore 1D,
    #   necessario per passare i dati ai layer Dense (fully connected).
    layers.Flatten(),

    # Dense(64, relu): layer fully connected con 64 neuroni.
    #   Combina tutte le feature estratte dalla parte convoluzionale.
    layers.Dense(64, activation='relu'),

    # Dense(10, softmax): layer di output con 10 neuroni (uno per cifra 0-9).
    #   softmax restituisce probabilità che sommano a 1.
    #   Il neurone con il valore più alto indica la cifra predetta.
    layers.Dense(10, activation='softmax')
])

# ==========================================================
# 5. Compilazione del modello
# ==========================================================
# optimizer='adam': algoritmo che aggiorna i pesi in modo adattivo.
# loss='categorical_crossentropy': funzione di perdita per classificazione multiclasse.
#   Misura la distanza tra le predizioni e le etichette reali (più bassa = meglio).
# metrics=['accuracy']: monitoriamo la percentuale di classificazioni corrette.
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# ==========================================================
# 6. Addestramento del modello
# ==========================================================
# epochs=50: il modello vede l'intero dataset di training 50 volte.
#   Ad ogni epoca i pesi vengono aggiornati per migliorare le predizioni.
# batch_size=64: i dati vengono elaborati a gruppi di 64 immagini alla volta.
#   Il modello calcola la loss media sul batch e aggiorna i pesi una volta per batch.
# validation_split=0.1: il 10% del training set (6.000 immagini) viene riservato
#   per la validazione. Serve a monitorare l'overfitting: se la loss di validazione
#   inizia a salire mentre quella di training scende, il modello sta memorizzando
#   i dati invece di generalizzare.
model.fit(train_images, train_labels, epochs=50, batch_size=64, validation_split=0.1)

# ==========================================================
# 7. Valutazione finale sul test set
# ==========================================================
# evaluate: testa il modello sulle 10.000 immagini di test (mai viste durante il training).
#   Restituisce la loss e l'accuracy, che ci dicono quanto il modello generalizza bene.
loss, accuracy = model.evaluate(test_images, test_labels)
print(f"Accuratezza: {accuracy:.2%}")

# ==========================================================
# 8. Salvataggio del modello
# ==========================================================
# Il modello addestrato può essere salvato su disco per essere riutilizzato
# senza doverlo ri-addestrare da zero.
#
# Formato .h5 (HDF5): formato classico di Keras.
#   Salva architettura + pesi + stato dell'optimizer in un unico file.
model.save("mnist_model.h5")

# Formato .keras: nuovo formato nativo di Keras (consigliato).
#   Più efficiente e meglio supportato nelle versioni recenti.
model.save('my_model.keras')

# Per caricare il modello salvato si usa:
#   modello_caricato = tf.keras.models.load_model("mnist_model.h5")
#   modello_caricato = tf.keras.models.load_model("my_model.keras")

# ==========================================================
# Nota: cos'è un'Epoch?
# ==========================================================
# Un'epoch rappresenta un passaggio completo sull'intero dataset di training.
#
#   1 epoch = il modello ha visto TUTTE le 60.000 immagini una volta.
#   50 epoch = il modello ha visto ogni immagine 50 volte.
#
# Ad ogni epoca il modello migliora (riduce la loss), ma troppe epoche possono
# causare overfitting. Per questo si usa la validation_split per monitorare.
