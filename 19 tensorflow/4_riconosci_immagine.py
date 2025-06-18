import numpy as np
from PIL import Image
import tensorflow as tf

# Carica il modello addestrato
model = tf.keras.models.load_model('mnist_model.h5')


def preprocess_image(image_path):
    """
    Preprocessa l'immagine per adattarla al modello MNIST.
    """
    # Carica l'immagine, converte in scala di grigi e ridimensiona a 28x28
    img = Image.open(image_path).convert('L').resize((28, 28))

    # Inverte i colori: MNIST ha sfondo nero (0) e cifre bianche (255)
    img = Image.eval(img, lambda x: 255 - x)

    # Converte l'immagine in array NumPy e normalizza i pixel
    img_array = np.array(img).astype('float32') / 255.0

    # Ridimensiona l'array per adattarlo all'input del modello
    img_array = img_array.reshape(1, 28, 28, 1)

    return img_array


def predict_digit(image_path):
    """
    Predice la cifra presente nell'immagine fornita.
    """
    processed_image = preprocess_image(image_path)
    prediction = model.predict(processed_image)
    predicted_digit = np.argmax(prediction)
    confidence = np.max(prediction)

    print(f"Predizione: {predicted_digit} con confidenza: {confidence:.2%}")


# Esempio di utilizzo
image_path = 'cifra.jpg'  # Sostituisci con il percorso della tua immagine
predict_digit(image_path)
image_path = 'cifra_2.jpg'  # Sostituisci con il percorso della tua immagine
predict_digit(image_path)
image_path = 'cifra_3.jpg'  # Sostituisci con il percorso della tua immagine
predict_digit(image_path)
image_path = 'cifra_4.jpg'  # Sostituisci con il percorso della tua immagine
predict_digit(image_path)
image_path = 'cifra_5.jpg'  # Sostituisci con il percorso della tua immagine
predict_digit(image_path)