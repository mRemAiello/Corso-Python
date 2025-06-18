import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Caricamento del dataset MNIST
# Dataset => 1000 immagini, labels => "uomo, mare, costume, costume blu, cielo"
# Train_images => 844, train_labels
# test_img, test_labels => testare se azzecca la previsione
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Pre-elaborazione dei dati
train_images = train_images.reshape((60000, 28, 28, 1)).astype("float32") / 255
test_images = test_images.reshape((10000, 28, 28, 1)).astype("float32") / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

# Creazione del modello
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Compilazione del modello
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Addestramento del modello
model.fit(train_images, train_labels, epochs=100, batch_size=64, validation_split=0.1)

# Valutazione sul test set
test_loss, test_acc = model.evaluate(test_images, test_labels)
print(f"Accuratezza sul test set: {test_acc:.2%}")