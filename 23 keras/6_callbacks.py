# Callbacks e Salvataggio del Modello
#
# I callbacks sono funzioni che vengono eseguite durante l'addestramento
# in momenti specifici (fine epoca, fine batch, ecc.).
#
# Callbacks più usati:
#     - EarlyStopping: ferma l'addestramento se non ci sono miglioramenti
#     - ModelCheckpoint: salva il modello durante l'addestramento
#     - ReduceLROnPlateau: riduce il learning rate se la loss non migliora
#     - TensorBoard: visualizzazione avanzata dell'addestramento
#
# Salvataggio modello:
#     - model.save('modello.keras')        => salva tutto (architettura + pesi + optimizer)
#     - model.save_weights('pesi.weights.h5')  => salva solo i pesi
#     - keras.models.load_model('modello.keras') => carica il modello completo

import numpy as np
import keras
from keras import Sequential
from keras.layers import Dense, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from keras.datasets import mnist
from keras.utils import to_categorical

# 1. Preparazione dati
(X_train, y_train), (X_test, y_test) = mnist.load_data()
X_train = X_train.reshape(-1, 784).astype('float32') / 255.0
X_test = X_test.reshape(-1, 784).astype('float32') / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 2. Costruzione del modello
model = Sequential([
    Dense(256, activation='relu', input_shape=(784,)),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 3. Definizione dei callbacks

# EarlyStopping: ferma l'addestramento se val_loss non migliora per 5 epoche
early_stop = EarlyStopping(
    monitor='val_loss',       # metrica da monitorare
    patience=5,               # numero di epoche senza miglioramento prima di fermarsi
    restore_best_weights=True # ripristina i pesi migliori
)

# ModelCheckpoint: salva il modello migliore durante l'addestramento
checkpoint = ModelCheckpoint(
    'miglior_modello.keras',  # percorso di salvataggio
    monitor='val_accuracy',   # metrica da monitorare
    save_best_only=True,      # salva solo se c'è un miglioramento
    verbose=1
)

# ReduceLROnPlateau: riduce il learning rate se val_loss non migliora
reduce_lr = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,               # moltiplica il lr per 0.5
    patience=3,               # aspetta 3 epoche senza miglioramento
    min_lr=1e-6,              # learning rate minimo
    verbose=1
)

# 4. Addestramento con callbacks
history = model.fit(
    X_train, y_train,
    epochs=50,                              # massimo 50, ma EarlyStopping può fermare prima
    batch_size=128,
    validation_split=0.15,
    callbacks=[early_stop, checkpoint, reduce_lr],
    verbose=1
)

# 5. Valutazione
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nAccuratezza finale: {test_acc:.2%}")

# 6. Salvataggio e caricamento
model.save('modello_mnist.keras')
print("Modello salvato in 'modello_mnist.keras'")

# Caricamento del modello salvato
modello_caricato = keras.models.load_model('modello_mnist.keras')
loss, acc = modello_caricato.evaluate(X_test, y_test, verbose=0)
print(f"Accuratezza modello caricato: {acc:.2%}")

# 7. Salvataggio solo dei pesi
model.save_weights('pesi_mnist.weights.h5')
print("Pesi salvati in 'pesi_mnist.weights.h5'")
