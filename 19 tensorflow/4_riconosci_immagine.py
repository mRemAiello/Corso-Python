import numpy as np
from PIL import Image
import tensorflow as tf

# ==========================================================
# 1. Caricamento del modello pre-addestrato
# ==========================================================
# Carichiamo il modello salvato nel file 3_modello.py dopo l'addestramento.
# Il file .h5 contiene: architettura della rete + pesi + stato dell'optimizer.
# In questo modo non serve ri-addestrare il modello ogni volta: lo carichiamo
# già pronto e lo usiamo direttamente per fare predizioni.
model = tf.keras.models.load_model('mnist_model.h5')


# ==========================================================
# 2. Funzione di pre-elaborazione dell'immagine
# ==========================================================
def preprocess_image(image_path):
    """Preprocessa l'immagine per adattarla al modello MNIST."""

    # Apre l'immagine dal percorso indicato.
    # .convert('L'): converte in scala di grigi (1 canale).
    #   Il modello MNIST è stato addestrato su immagini in bianco e nero,
    #   quindi anche le nostre immagini devono essere in scala di grigi.
    # .resize((28, 28)): ridimensiona a 28x28 pixel.
    #   Il modello accetta SOLO immagini di questa dimensione.
    img = Image.open(image_path).convert('L').resize((28, 28))

    # Inversione dei colori (negativo dell'immagine).
    # Le immagini MNIST hanno sfondo NERO (0) e cifra BIANCA (255).
    # Le foto normali hanno tipicamente sfondo chiaro e cifra scura,
    # quindi invertiamo: ogni pixel x diventa 255 - x.
    # Es: pixel bianco (255) diventa nero (0), pixel nero (0) diventa bianco (255).
    img = Image.eval(img, lambda x: 255 - x)

    # Conversione in array NumPy e normalizzazione.
    # I pixel passano da valori interi [0, 255] a float [0.0, 1.0],
    # esattamente come è stato fatto durante l'addestramento del modello.
    img_array = np.array(img).astype('float32') / 255.0

    # Reshape dell'array per adattarlo all'input del modello.
    # Il modello si aspetta un input 4D: (batch_size, altezza, larghezza, canali).
    # - 1: un solo campione (una sola immagine)
    # - 28, 28: dimensioni dell'immagine
    # - 1: un canale (scala di grigi)
    img_array = img_array.reshape(1, 28, 28, 1)

    return img_array


# ==========================================================
# 3. Funzione di predizione
# ==========================================================
def predict_digit(image_path):
    """Predice la cifra presente nell'immagine fornita."""

    # Pre-elabora l'immagine (scala di grigi, 28x28, normalizzata)
    processed_image = preprocess_image(image_path)

    # model.predict() esegue il forward pass sulla rete neurale.
    # Restituisce un array di 10 probabilità, una per ogni cifra (0-9).
    # Es: [0.01, 0.02, 0.01, 0.85, 0.03, 0.01, 0.02, 0.03, 0.01, 0.01]
    #      => il modello pensa che sia un "3" con l'85% di confidenza.
    prediction = model.predict(processed_image)

    # np.argmax: restituisce l'indice del valore più alto nell'array.
    # L'indice corrisponde alla cifra predetta (indice 3 => cifra "3").
    predicted_digit = np.argmax(prediction)

    # np.max: restituisce il valore più alto, cioè la probabilità
    # associata alla cifra predetta (la "confidenza" del modello).
    confidence = np.max(prediction)

    print(f"Predizione: {predicted_digit} con confidenza: {confidence:.2%}")


# ==========================================================
# 4. Esempio di utilizzo
# ==========================================================
# Testiamo il modello su diverse immagini di cifre scritte a mano.
# Le immagini devono essere nella stessa cartella dello script (o indicare il percorso completo).
image_path = 'cifra.jpg'
predict_digit(image_path)
image_path = 'cifra_2.jpg'
predict_digit(image_path)
image_path = 'cifra_3.jpg'
predict_digit(image_path)
image_path = 'cifra_4.jpg'
predict_digit(image_path)
image_path = 'cifra_5.jpg'
predict_digit(image_path)

# Nota: se la predizione non è corretta, possibili cause:
#   - L'immagine ha uno sfondo troppo complesso (non uniforme)
#   - La cifra non è centrata nell'immagine
#   - La risoluzione originale è troppo bassa o troppo alta
#   - Il contrasto tra cifra e sfondo è insufficiente