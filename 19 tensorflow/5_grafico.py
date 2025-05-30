import tensorflow as tf
import matplotlib.pyplot as plt
from keras.src.datasets import mnist
from tensorflow.python.keras.utils.np_utils import to_categorical

# 1. Caricamento dei dati
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape(-1, 28, 28, 1).astype("float32") / 255
test_images = test_images.reshape(-1, 28, 28, 1).astype("float32") / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# 2. Costruzione del modello
import tensorflow as tf

# Costruzione del modello CNN
model = tf.keras.models.Sequential([
    # Layer convoluzionale: 32 filtri 3x3, attivazione ReLU
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),

    # Layer di MaxPooling: riduce la dimensione spaziale
    tf.keras.layers.MaxPooling2D((2, 2)),

    # Flatten: da 2D a 1D per il passaggio ai layer densi
    tf.keras.layers.Flatten(),

    # Dense hidden layer: 64 neuroni con attivazione ReLU
    tf.keras.layers.Dense(64, activation='relu'),

    # Layer di output: 10 classi con attivazione Softmax
    tf.keras.layers.Dense(10, activation='softmax')
])


# 3. Compilazione
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 4. Addestramento
history = model.fit(train_images, train_labels,
                    epochs=10, batch_size=64,
                    validation_split=0.2)

# 5. Visualizzazione
plt.figure()
plt.plot(history.history['loss'], label='Loss Training')
plt.plot(history.history['val_loss'], label='Loss Validation')
plt.title('Loss durante l\'addestramento')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.grid(True)
plt.show()

plt.figure()
plt.plot(history.history['accuracy'], label='Accuracy Training')
plt.plot(history.history['val_accuracy'], label='Accuracy Validation')
plt.title('Accuracy durante l\'addestramento')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.show()
