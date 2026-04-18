# Classificazione con Keras
#
# La classificazione è un problema di apprendimento supervisionato in cui si vuole
# assegnare un'etichetta (classe) a un dato di input.
#
# Classificazione binaria: 2 classi (es. spam/non spam, malato/sano)
#     - Layer di output: 1 neurone con attivazione sigmoid
#     - Loss: binary_crossentropy
#
# Classificazione multiclasse: N classi (es. cifre 0-9, tipi di fiori)
#     - Layer di output: N neuroni con attivazione softmax
#     - Loss: categorical_crossentropy (one-hot) o sparse_categorical_crossentropy (interi)

from keras import Sequential
from keras.layers import Dense, Dropout
from keras.datasets import mnist
from keras.utils import to_categorical
import numpy as np

# ==========================================
# Esempio: Classificazione cifre MNIST
# ==========================================

# 1. Caricamento dei dati
(X_train, y_train), (X_test, y_test) = mnist.load_data()

print(f"Dimensione training set: {X_train.shape}")  # (60000, 28, 28)
print(f"Dimensione test set: {X_test.shape}")        # (10000, 28, 28)

# 2. Pre-elaborazione
# Appiattire le immagini 28x28 in vettori di 784 elementi
X_train = X_train.reshape(-1, 784).astype('float32') / 255.0
X_test = X_test.reshape(-1, 784).astype('float32') / 255.0

# One-hot encoding delle etichette
# 3 => [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 3. Costruzione del modello
model = Sequential([
    Dense(256, activation='relu', input_shape=(784,)),
    Dropout(0.3),          # Spegne il 30% dei neuroni (evita overfitting)
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')  # 10 classi => softmax
])

model.summary()

# 4. Compilazione
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 5. Addestramento
history = model.fit(
    X_train, y_train,
    epochs=15,
    batch_size=128,
    validation_split=0.15,
    verbose=1
)

# 6. Valutazione
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nAccuratezza sul test set: {test_acc:.2%}")
print(f"Loss sul test set: {test_loss:.4f}")

# 7. Predizione su un singolo campione
campione = X_test[0:1]
predizione = model.predict(campione, verbose=0)
cifra_predetta = np.argmax(predizione)
cifra_reale = np.argmax(y_test[0])
print(f"\nCifra predetta: {cifra_predetta}")
print(f"Cifra reale: {cifra_reale}")
print(f"Confidenza: {np.max(predizione):.2%}")
