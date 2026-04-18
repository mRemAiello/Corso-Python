import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# ==========================================================
# 1. Caricamento del dataset MNIST
# ==========================================================
# MNIST è un dataset di 70.000 immagini di cifre scritte a mano (0-9).
# Ogni immagine è in scala di grigi, di dimensione 28x28 pixel.
# Il dataset viene automaticamente diviso in:
#   - train: 60.000 immagini per l'addestramento
#   - test: 10.000 immagini per la valutazione finale
# train_images/test_images => le immagini (pixel)
# train_labels/test_labels => le etichette (la cifra rappresentata: 0, 1, 2, ..., 9)
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# ==========================================================
# 2. Pre-elaborazione dei dati
# ==========================================================
# reshape: le immagini originali hanno shape (60000, 28, 28).
#   Aggiungiamo una dimensione per il canale colore => (60000, 28, 28, 1)
#   perché Conv2D si aspetta un input 4D: (campioni, altezza, larghezza, canali).
#   1 canale = scala di grigi (3 canali sarebbero per immagini RGB a colori).
#
# astype("float32") / 255: i pixel originali vanno da 0 a 255.
#   Dividendo per 255 normalizziamo i valori tra 0.0 e 1.0.
#   Questo aiuta la rete neurale a convergere più velocemente durante l'addestramento.
train_images = train_images.reshape((60000, 28, 28, 1)).astype("float32") / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype("float32") / 255

# to_categorical: converte le etichette in formato one-hot encoding.
# Esempio: la cifra 3 diventa [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
# Questo è necessario perché il layer di output usa softmax con 10 neuroni,
# dove ogni neurone rappresenta la probabilità di una cifra.
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# ==========================================================
# 3. Creazione del modello (CNN - Rete Neurale Convoluzionale)
# ==========================================================
# Sequential: i layer vengono impilati uno dopo l'altro in sequenza.
model = models.Sequential([
    # Conv2D(32, (3,3)): primo strato convoluzionale.
    #   - 32 filtri (il modello impara 32 pattern diversi come bordi, curve, angoli)
    #   - Kernel 3x3: ogni filtro analizza una finestra di 3x3 pixel alla volta
    #   - activation='relu': attivazione ReLU, azzera i valori negativi (introduce non-linearità)
    #   - input_shape=(28, 28, 1): dimensione dell'immagine in input
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),

    # MaxPooling2D(2,2): riduce la dimensione spaziale della mappa di feature.
    #   Prende il valore massimo in ogni finestra 2x2, dimezzando altezza e larghezza.
    #   Questo riduce i calcoli e rende il modello più robusto a piccole traslazioni.
    layers.MaxPooling2D((2, 2)),

    # Secondo strato convoluzionale con 64 filtri.
    #   Impara pattern più complessi combinando quelli trovati dal primo strato.
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    # Terzo strato convoluzionale con 64 filtri.
    #   Cattura pattern ancora più astratti e di alto livello.
    layers.Conv2D(64, (3, 3), activation='relu'),

    # Flatten: trasforma la mappa di feature 3D in un vettore 1D.
    #   Necessario per passare i dati ai layer Dense (fully connected).
    layers.Flatten(),

    # Dense(64): layer fully connected con 64 neuroni.
    #   Ogni neurone è collegato a tutti gli output del Flatten.
    #   Combina le feature estratte dalla parte convoluzionale per la classificazione.
    layers.Dense(64, activation='relu'),

    # Dense(10, softmax): layer di output con 10 neuroni (uno per ogni cifra 0-9).
    #   softmax: converte gli output in probabilità che sommano a 1.
    #   Es: [0.01, 0.02, 0.05, 0.85, 0.01, ...] => il modello pensa che sia un "3"
    layers.Dense(10, activation='softmax')
])

# ==========================================================
# 4. Compilazione del modello
# ==========================================================
# optimizer='adam': algoritmo di ottimizzazione Adam.
#   Aggiorna i pesi della rete in modo adattivo, combinando i vantaggi di
#   SGD con momentum e RMSProp. È il più usato per la sua efficacia generale.
#
# loss='categorical_crossentropy': funzione di perdita per classificazione multiclasse.
#   Misura quanto le predizioni del modello si discostano dalle etichette reali.
#   Più la loss è bassa, più il modello è accurato.
#
# metrics=['accuracy']: metrica monitorata durante l'addestramento.
#   Percentuale di immagini classificate correttamente.
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# ==========================================================
# 5. Addestramento del modello
# ==========================================================
# epochs=100: il modello passa 100 volte sull'intero dataset di training.
#   Ad ogni epoca i pesi vengono aggiornati per ridurre la loss.
#
# batch_size=64: i dati vengono elaborati in gruppi di 64 immagini alla volta.
#   Invece di aggiornare i pesi dopo ogni singola immagine, si fa una media
#   su 64 campioni => addestramento più stabile e veloce.
#
# validation_split=0.1: il 10% dei dati di training viene usato come validazione.
#   Serve per monitorare se il modello sta generalizzando bene o sta facendo overfitting
#   (ovvero impara "a memoria" i dati di training senza saper generalizzare).
model.fit(train_images, train_labels, epochs=100, batch_size=64, validation_split=0.1)

# ==========================================================
# 6. Valutazione sul test set
# ==========================================================
# evaluate: testa il modello su dati MAI visti durante l'addestramento.
#   Restituisce la loss e l'accuracy sul test set.
#   Questo ci dice quanto il modello è capace di generalizzare su dati nuovi.
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Accuratezza sul test set: {test_acc:.2%}")