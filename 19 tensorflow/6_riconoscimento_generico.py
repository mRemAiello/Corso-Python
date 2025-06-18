import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from tkinter import Tk, filedialog
import os


# Funzione per selezionare l'immagine
def seleziona_immagine():
    root = Tk()
    root.withdraw()  # Nasconde la finestra principale
    file_path = filedialog.askopenfilename(
        title = "Seleziona un'immagine",
        filetypes = [("Image files", "*.jpg *.jpeg *.png")]
    )
    return file_path


# Carica immagine e prepara per il modello
def prepara_immagine(path):
    img = image.load_img(path, target_size = (224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)
    x = preprocess_input(x)
    return x


# Funzione principale
def analizza_immagine():
    img_path = seleziona_immagine()

    if not img_path or not os.path.exists(img_path):
        print("Nessuna immagine selezionata o file non valido.")
        return

    print(f"\n✅ Immagine selezionata: {img_path}")

    x = prepara_immagine(img_path)
    model = MobileNetV2(weights = 'imagenet')

    print("📡 Analisi in corso...\n")
    preds = model.predict(x)
    results = decode_predictions(preds, top = 3)[0]

    print("🔍 Soggetto dell'immagine:")
    for i, (imagenet_id, label, score) in enumerate(results):
        print(f"{i + 1}. {label.replace('_', ' ').capitalize()} ({score:.2%})")


# Avvia il programma
if __name__ == "__main__":
    analizza_immagine()
