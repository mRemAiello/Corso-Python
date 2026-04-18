# Data Augmentation
#
# La data augmentation è una tecnica per aumentare artificialmente la quantità
# di dati di training applicando trasformazioni casuali alle immagini:
#     - Rotazione
#     - Ribaltamento orizzontale/verticale (flip)
#     - Zoom
#     - Traslazione
#     - Variazione di luminosità
#
# Vantaggi:
#     - Riduce l'overfitting
#     - Migliora la generalizzazione del modello
#     - Non richiede nuovi dati reali
#
# In Keras si può fare con:
#     - Layer di preprocessing (consigliato, integrato nel modello)
#     - ImageDataGenerator (approccio classico)

import numpy as np
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import (Dense, Flatten, Dropout,
                          RandomFlip, RandomRotation, RandomZoom, Rescaling)
from keras.datasets import cifar10

# 1. Caricamento del dataset CIFAR-10
# 10 classi: aereo, auto, uccello, gatto, cervo, cane, rana, cavallo, nave, camion
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

nomi_classi = ['Aereo', 'Auto', 'Uccello', 'Gatto', 'Cervo',
               'Cane', 'Rana', 'Cavallo', 'Nave', 'Camion']

print(f"Training set: {X_train.shape}")   # (50000, 32, 32, 3)
print(f"Test set: {X_test.shape}")         # (10000, 32, 32, 3)

# 2. Visualizzazione di alcune immagini originali
fig, axes = plt.subplots(2, 5, figsize=(12, 5))
for i, ax in enumerate(axes.flat):
    ax.imshow(X_train[i])
    ax.set_title(nomi_classi[y_train[i][0]])
    ax.axis('off')
plt.suptitle("Immagini originali CIFAR-10")
plt.tight_layout()
plt.show()

# 3. Definizione dei layer di data augmentation
data_augmentation = Sequential([
    RandomFlip("horizontal"),                # Ribaltamento orizzontale casuale
    RandomRotation(0.1),                     # Rotazione fino a ±10%
    RandomZoom(0.1),                         # Zoom fino a ±10%
], name='data_augmentation')

# 4. Modello con data augmentation integrata
model = Sequential([
    # Pre-processing
    Rescaling(1./255, input_shape=(32, 32, 3)),  # Normalizzazione 0-1

    # Data augmentation (attiva solo durante il training)
    data_augmentation,

    # Rete neurale
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.4),
    Dense(256, activation='relu'),
    Dropout(0.3),
    Dense(10, activation='softmax')
])

model.summary()

# 5. Compilazione e addestramento
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=64,
    validation_split=0.2,
    verbose=1
)

# 6. Valutazione
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nAccuratezza sul test set: {test_acc:.2%}")

# 7. Visualizzazione effetto data augmentation su una singola immagine
img = X_train[0:1]  # Prima immagine
fig, axes = plt.subplots(2, 4, figsize=(12, 6))
axes[0, 0].imshow(img[0])
axes[0, 0].set_title("Originale")
axes[0, 0].axis('off')

for i, ax in enumerate(axes.flat[1:]):
    augmented = data_augmentation(img.astype('float32'))
    ax.imshow(augmented[0].numpy().astype('uint8'))
    ax.set_title(f"Augmented {i+1}")
    ax.axis('off')

plt.suptitle("Effetto Data Augmentation")
plt.tight_layout()
plt.show()
