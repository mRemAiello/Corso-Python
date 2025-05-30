import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Carica i dati
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
train_images = train_images.reshape((-1, 28, 28, 1)).astype("float32") / 255
test_images = test_images.reshape((-1, 28, 28, 1)).astype("float32") / 255

# One-hot encoding
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Crea il modello
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compila il modello
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Addestra il modello
model.fit(train_images, train_labels, epochs=10, batch_size=64, validation_split=0.1)

# Valutazione finale
loss, accuracy = model.evaluate(test_images, test_labels)
print(f"Accuratezza: {accuracy:.2%}")

# Salvataggio
model.save("mnist_model.h5")
model.save('my_model.keras')

# Epoch
# Nel contesto del machine learning e del deep learning, un epoch rappresenta un intero passaggio del dataset di addestramento attraverso il modello.
# Definizione formale:
#
#     1 epoch = 1 iterazione completa su tutti i dati di training.
