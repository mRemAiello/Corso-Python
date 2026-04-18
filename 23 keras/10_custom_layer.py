# Layer Personalizzati e Custom Training
#
# Keras permette di creare layer personalizzati ereditando da keras.layers.Layer.
# Questo è utile quando i layer standard non coprono le proprie esigenze.
#
# Struttura di un layer personalizzato:
#     - __init__: definizione dei parametri
#     - build: creazione dei pesi (viene chiamato automaticamente al primo utilizzo)
#     - call: logica del layer (forward pass)
#
# Custom Training Loop:
#     Invece di usare model.fit(), si può scrivere un ciclo di addestramento manuale
#     per avere pieno controllo su ogni step.

import numpy as np
import keras
from keras import Model, Input
from keras.layers import Dense, Layer
import tensorflow as tf

# ==========================================
# Esempio 1: Layer personalizzato - Dense semplificato
# ==========================================

class MioDense(Layer):
    """Layer Dense personalizzato con bias opzionale."""

    def __init__(self, unita, usa_bias=True, **kwargs):
        super().__init__(**kwargs)
        self.unita = unita
        self.usa_bias = usa_bias

    def build(self, input_shape):
        # Creazione del peso W (matrice dei pesi)
        self.w = self.add_weight(
            shape=(input_shape[-1], self.unita),
            initializer='glorot_uniform',
            trainable=True,
            name='peso'
        )
        if self.usa_bias:
            self.b = self.add_weight(
                shape=(self.unita,),
                initializer='zeros',
                trainable=True,
                name='bias'
            )

    def call(self, inputs):
        output = tf.matmul(inputs, self.w)
        if self.usa_bias:
            output = output + self.b
        return tf.nn.relu(output)


# Utilizzo del layer personalizzato
inputs = Input(shape=(10,))
x = MioDense(32, name='mio_layer_1')(inputs)
x = MioDense(16, name='mio_layer_2')(x)
outputs = Dense(1)(x)

model = Model(inputs, outputs, name='modello_custom')
model.summary()

# ==========================================
# Esempio 2: Custom Training Loop
# ==========================================

# Dataset di esempio
np.random.seed(42)
X_train = np.random.rand(1000, 10).astype('float32')
y_train = (np.sum(X_train, axis=1) > 5).astype('float32')

# Modello semplice
model_custom = keras.Sequential([
    Dense(32, activation='relu', input_shape=(10,)),
    Dense(16, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Optimizer e loss
optimizer = keras.optimizers.Adam(learning_rate=0.001)
loss_fn = keras.losses.BinaryCrossentropy()

# Dataset TensorFlow per il batching
dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
dataset = dataset.shuffle(1000).batch(32)

# Training loop personalizzato
epochs = 10
for epoch in range(epochs):
    epoch_loss = 0.0
    num_batches = 0

    for X_batch, y_batch in dataset:
        # GradientTape registra le operazioni per calcolare i gradienti
        with tf.GradientTape() as tape:
            predictions = model_custom(X_batch, training=True)
            loss = loss_fn(y_batch, predictions)

        # Calcolo dei gradienti
        gradients = tape.gradient(loss, model_custom.trainable_variables)

        # Aggiornamento dei pesi
        optimizer.apply_gradients(zip(gradients, model_custom.trainable_variables))

        epoch_loss += loss.numpy()
        num_batches += 1

    avg_loss = epoch_loss / num_batches
    print(f"Epoca {epoch+1}/{epochs} - Loss media: {avg_loss:.4f}")

# Valutazione finale
predictions = model_custom.predict(X_train[:10], verbose=0)
print("\nPredizioni (prime 10):")
for i, pred in enumerate(predictions):
    print(f"  Campione {i+1}: {pred[0]:.4f} (reale: {y_train[i]:.0f})")
