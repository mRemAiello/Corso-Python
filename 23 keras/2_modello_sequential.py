# Modello Sequential
#
# Il modello Sequential è il modo più semplice per costruire una rete neurale in Keras.
# Si tratta di una pila lineare di layer, uno dopo l'altro.
#
# Struttura tipica:
#     Input -> Layer 1 -> Layer 2 -> ... -> Output
#
# Layer principali:
#     - Dense: layer fully connected (ogni neurone è collegato a tutti i neuroni del layer precedente)
#     - Activation: funzione di attivazione (relu, sigmoid, softmax, tanh)
#     - Dropout: tecnica di regolarizzazione (spegne casualmente dei neuroni durante il training)

import numpy as np
from keras import Sequential
from keras.layers import Dense

# Creazione di un modello Sequential
model = Sequential([
    Dense(64, activation='relu', input_shape=(10,)),  # Layer di input: 10 feature
    Dense(32, activation='relu'),                      # Layer nascosto
    Dense(1)                                           # Layer di output: 1 valore
])

# Riepilogo del modello
model.summary()

# Compilazione del modello
# optimizer: algoritmo di ottimizzazione (adam, sgd, rmsprop)
# loss: funzione di perdita (mse per regressione, crossentropy per classificazione)
# metrics: metriche da monitorare durante l'addestramento
model.compile(
    optimizer='adam',
    loss='mse',
    metrics=['mae']
)

# Dati di esempio (casuali)
X_train = np.random.rand(1000, 10)
y_train = np.random.rand(1000, 1)

# Addestramento del modello
# epochs: numero di passaggi completi sul dataset
# batch_size: numero di campioni elaborati prima di aggiornare i pesi
# validation_split: percentuale di dati usata per la validazione
history = model.fit(
    X_train, y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# Predizione su nuovi dati
X_new = np.random.rand(5, 10)
predictions = model.predict(X_new)
print("\nPredizioni:")
for i, pred in enumerate(predictions):
    print(f"  Campione {i+1}: {pred[0]:.4f}")
