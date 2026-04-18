# Visualizzazione dell'Addestramento
#
# Monitorare l'andamento dell'addestramento è fondamentale per capire se il modello:
#     - Sta imparando correttamente
#     - Soffre di overfitting (troppo adattato ai dati di training)
#     - Soffre di underfitting (non impara abbastanza)
#
# Segnali di overfitting:
#     - La loss di training scende, ma la loss di validazione sale
#     - L'accuracy di training è molto più alta di quella di validazione
#
# Segnali di underfitting:
#     - Entrambe le loss rimangono alte
#     - L'accuracy rimane bassa

import numpy as np
import matplotlib.pyplot as plt
from keras import Sequential
from keras.layers import Dense, Dropout
from keras.datasets import fashion_mnist
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping

# 1. Caricamento dataset Fashion MNIST
# 10 classi: T-shirt, Pantaloni, Maglione, Vestito, Cappotto,
#             Sandalo, Camicia, Scarpa, Borsa, Stivaletto
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

nomi_classi = ['T-shirt', 'Pantaloni', 'Maglione', 'Vestito', 'Cappotto',
               'Sandalo', 'Camicia', 'Scarpa', 'Borsa', 'Stivaletto']

X_train = X_train.reshape(-1, 784).astype('float32') / 255.0
X_test = X_test.reshape(-1, 784).astype('float32') / 255.0
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 2. Modello
model = Sequential([
    Dense(256, activation='relu', input_shape=(784,)),
    Dropout(0.3),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 3. Addestramento
early_stop = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

history = model.fit(
    X_train, y_train,
    epochs=40,
    batch_size=128,
    validation_split=0.2,
    callbacks=[early_stop],
    verbose=1
)

# 4. Grafici dell'addestramento
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Grafico Loss
ax1.plot(history.history['loss'], label='Loss Training', linewidth=2)
ax1.plot(history.history['val_loss'], label='Loss Validazione', linewidth=2)
ax1.set_title('Loss durante l\'addestramento')
ax1.set_xlabel('Epoca')
ax1.set_ylabel('Loss')
ax1.legend()
ax1.grid(True)

# Grafico Accuracy
ax2.plot(history.history['accuracy'], label='Accuracy Training', linewidth=2)
ax2.plot(history.history['val_accuracy'], label='Accuracy Validazione', linewidth=2)
ax2.set_title('Accuracy durante l\'addestramento')
ax2.set_xlabel('Epoca')
ax2.set_ylabel('Accuracy')
ax2.legend()
ax2.grid(True)

plt.suptitle('Monitoraggio Addestramento - Fashion MNIST', fontsize=14)
plt.tight_layout()
plt.show()

# 5. Matrice di confusione
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

y_pred = model.predict(X_test, verbose=0)
y_pred_classes = np.argmax(y_pred, axis=1)
y_test_classes = np.argmax(y_test, axis=1)

cm = confusion_matrix(y_test_classes, y_pred_classes)

fig, ax = plt.subplots(figsize=(10, 8))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=nomi_classi)
disp.plot(ax=ax, cmap='Blues', xticks_rotation=45)
plt.title('Matrice di Confusione - Fashion MNIST')
plt.tight_layout()
plt.show()

# 6. Predizioni con visualizzazione
fig, axes = plt.subplots(3, 5, figsize=(15, 9))
X_test_img = X_test.reshape(-1, 28, 28)

for i, ax in enumerate(axes.flat):
    ax.imshow(X_test_img[i], cmap='gray')
    predetto = nomi_classi[y_pred_classes[i]]
    reale = nomi_classi[y_test_classes[i]]
    colore = 'green' if predetto == reale else 'red'
    ax.set_title(f"P: {predetto}\nR: {reale}", color=colore, fontsize=9)
    ax.axis('off')

plt.suptitle('Predizioni del modello (verde=corretto, rosso=errato)', fontsize=13)
plt.tight_layout()
plt.show()

# 7. Valutazione finale
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nAccuratezza finale sul test set: {test_acc:.2%}")
print(f"Loss finale sul test set: {test_loss:.4f}")
