# Transfer Learning
#
# Il transfer learning è una tecnica che permette di riutilizzare un modello
# pre-addestrato su un grande dataset (es. ImageNet) per un nuovo compito.
#
# Vantaggi:
#     - Non serve un enorme dataset
#     - Addestramento molto più veloce
#     - Performance migliori su piccoli dataset
#
# Strategia:
#     1. Caricare un modello pre-addestrato (es. MobileNetV2, ResNet, VGG)
#     2. "Congelare" i layer del modello base (non vengono aggiornati)
#     3. Aggiungere nuovi layer per il proprio compito
#     4. Addestrare solo i nuovi layer
#     5. (Opzionale) Fine-tuning: scongelare alcuni layer e riaddestrare

import numpy as np
from keras.applications import MobileNetV2
from keras.layers import Dense, GlobalAveragePooling2D, Dropout
from keras import Model, Input
from keras.datasets import cifar10
from keras.utils import to_categorical
import tensorflow as tf

# 1. Caricamento dati
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

nomi_classi = ['Aereo', 'Auto', 'Uccello', 'Gatto', 'Cervo',
               'Cane', 'Rana', 'Cavallo', 'Nave', 'Camion']

# Pre-elaborazione
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Ridimensionamento a 96x96 (MobileNetV2 richiede almeno 32x32)
X_train_resized = tf.image.resize(X_train, (96, 96)).numpy()
X_test_resized = tf.image.resize(X_test, (96, 96)).numpy()

y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Usiamo un sottoinsieme per velocizzare l'esempio
X_train_sub = X_train_resized[:5000]
y_train_sub = y_train_cat[:5000]
X_test_sub = X_test_resized[:1000]
y_test_sub = y_test_cat[:1000]

# 2. Caricamento modello pre-addestrato
# include_top=False => esclude i layer di classificazione originali
base_model = MobileNetV2(
    weights='imagenet',        # pesi pre-addestrati su ImageNet
    include_top=False,         # senza il classificatore finale
    input_shape=(96, 96, 3)
)

# 3. Congelamento dei layer del modello base
base_model.trainable = False

print(f"Layer totali del modello base: {len(base_model.layers)}")
print(f"Layer addestrabili: {len([l for l in base_model.layers if l.trainable])}")

# 4. Costruzione del nuovo modello
inputs = Input(shape=(96, 96, 3))
x = base_model(inputs, training=False)  # training=False mantiene BatchNorm in modalità inferenza
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation='relu')(x)
x = Dropout(0.3)(x)
outputs = Dense(10, activation='softmax')(x)

model = Model(inputs, outputs, name='transfer_learning_model')
model.summary()

# 5. Compilazione
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 6. Addestramento (solo i nuovi layer)
print("\n--- Addestramento dei nuovi layer ---")
history = model.fit(
    X_train_sub, y_train_sub,
    epochs=10,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# 7. Valutazione
test_loss, test_acc = model.evaluate(X_test_sub, y_test_sub, verbose=0)
print(f"\nAccuratezza (solo nuovi layer): {test_acc:.2%}")

# 8. Fine-tuning (opzionale)
# Scongeliamo gli ultimi 20 layer del modello base
base_model.trainable = True
for layer in base_model.layers[:-20]:
    layer.trainable = False

trainable_count = len([l for l in model.layers if l.trainable])
print(f"\nLayer addestrabili dopo fine-tuning: {trainable_count}")

# Ricompilazione con learning rate più basso
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

print("\n--- Fine-tuning ---")
history_ft = model.fit(
    X_train_sub, y_train_sub,
    epochs=5,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

test_loss, test_acc = model.evaluate(X_test_sub, y_test_sub, verbose=0)
print(f"\nAccuratezza dopo fine-tuning: {test_acc:.2%}")
