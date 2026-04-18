# ==========================================================
# Riconoscimento generico di immagini con MobileNetV2
# ==========================================================
# A differenza del file 4_riconosci_immagine.py (che riconosce solo cifre 0-9),
# questo script può riconoscere 1000 CATEGORIE diverse: animali, oggetti,
# veicoli, cibi, strumenti, ecc.
#
# Usa MobileNetV2, un modello pre-addestrato su ImageNet (1.2 milioni di immagini).
# Non serve addestrare nulla: il modello è già pronto e scaricato automaticamente.
#
# Flusso:
#   1. L'utente seleziona un'immagine dal file explorer
#   2. L'immagine viene pre-elaborata (ridimensionata a 224x224)
#   3. MobileNetV2 analizza l'immagine e restituisce le 3 predizioni più probabili

import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions, preprocess_input
from tensorflow.keras.preprocessing import image
import numpy as np
from tkinter import Tk, filedialog
import os


# ==========================================================
# 1. Funzione per selezionare l'immagine
# ==========================================================
# Usa tkinter per aprire una finestra di dialogo del sistema operativo
# che permette all'utente di scegliere un file immagine (.jpg, .jpeg, .png).
def seleziona_immagine():
    root = Tk()
    root.withdraw()  # Nasconde la finestra principale di tkinter (mostra solo il dialog)
    file_path = filedialog.askopenfilename(
        title = "Seleziona un'immagine",
        filetypes = [("Image files", "*.jpg *.jpeg *.png")]
    )
    return file_path


# ==========================================================
# 2. Funzione di pre-elaborazione dell'immagine
# ==========================================================
# MobileNetV2 richiede immagini in un formato specifico:
#   - Dimensione: 224x224 pixel (diverso da MNIST che usa 28x28)
#   - Canali: 3 (RGB, a colori) - non scala di grigi
#   - Normalizzazione specifica di MobileNetV2 (valori tra -1 e 1)
def prepara_immagine(path):
    # Carica l'immagine e la ridimensiona a 224x224 pixel.
    # A differenza di MNIST (28x28 in scala di grigi), MobileNetV2
    # lavora con immagini a colori di dimensione maggiore.
    img = image.load_img(path, target_size = (224, 224))

    # Converte l'immagine PIL in un array NumPy di shape (224, 224, 3).
    # 3 = canali RGB (rosso, verde, blu).
    x = image.img_to_array(img)

    # Aggiunge una dimensione per il batch: da (224, 224, 3) a (1, 224, 224, 3).
    # Il modello si aspetta sempre un batch di immagini, anche se ne passiamo una sola.
    x = np.expand_dims(x, axis = 0)

    # Normalizzazione specifica per MobileNetV2.
    # Ogni modello pre-addestrato ha la sua normalizzazione:
    # MobileNetV2 scala i pixel da [0, 255] a [-1, 1].
    # È fondamentale usare la STESSA normalizzazione usata durante l'addestramento.
    x = preprocess_input(x)
    return x


# ==========================================================
# 3. Funzione principale di analisi
# ==========================================================
def analizza_immagine():
    # Apre il file explorer per selezionare un'immagine
    img_path = seleziona_immagine()

    # Controllo: l'utente potrebbe aver chiuso il dialog senza scegliere un file
    if not img_path or not os.path.exists(img_path):
        print("Nessuna immagine selezionata o file non valido.")
        return

    print(f"\n✅ Immagine selezionata: {img_path}")

    # Pre-elabora l'immagine nel formato richiesto dal modello
    x = prepara_immagine(img_path)

    # Carica il modello MobileNetV2 con i pesi pre-addestrati su ImageNet.
    # ImageNet: dataset con 1.2 milioni di immagini e 1000 categorie.
    # Al primo avvio, i pesi vengono scaricati da internet (~14 MB).
    # weights='imagenet' => usa i pesi già addestrati, il modello è pronto all'uso.
    model = MobileNetV2(weights = 'imagenet')

    print("📡 Analisi in corso...\n")

    # model.predict() esegue il forward pass e restituisce un array
    # di 1000 probabilità, una per ogni categoria di ImageNet.
    preds = model.predict(x)

    # decode_predictions() converte le probabilità in nomi leggibili.
    # top=3: restituisce solo le 3 predizioni con la probabilità più alta.
    # Ogni risultato è una tupla: (id_imagenet, nome_categoria, probabilità)
    # Es: [('n02124075', 'Egyptian_cat', 0.72), ('n02123045', 'tabby', 0.15), ...]
    results = decode_predictions(preds, top = 3)[0]

    # Stampa i risultati in formato leggibile
    print("🔍 Soggetto dell'immagine:")
    for i, (imagenet_id, label, score) in enumerate(results):
        # label.replace('_', ' '): sostituisce gli underscore con spazi
        # .capitalize(): prima lettera maiuscola
        # score:.2%: formatta la probabilità come percentuale (es. 72.35%)
        print(f"{i + 1}. {label.replace('_', ' ').capitalize()} ({score:.2%})")


# ==========================================================
# 4. Avvio del programma
# ==========================================================
# __name__ == "__main__" => il codice viene eseguito solo se questo file
# viene lanciato direttamente (non se viene importato da un altro file).
if __name__ == "__main__":
    analizza_immagine()
