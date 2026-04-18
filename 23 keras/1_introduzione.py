# Keras - Introduzione
#
# Keras è un'API di alto livello per la costruzione e l'addestramento di reti neurali.
# A partire da TensorFlow 2.x, Keras è integrato direttamente in TensorFlow (tf.keras),
# ma esiste anche come libreria standalone.
#
# Perché usare Keras?
#     - Semplicità: API intuitiva e user-friendly
#     - Modularità: i modelli sono composti da blocchi (layers, ottimizzatori, funzioni di perdita)
#     - Flessibilità: supporta sia modelli semplici (Sequential) che complessi (Functional API)
#     - Integrazione: funziona con TensorFlow, supporta GPU e TPU
#
# Concetti fondamentali:
#     - Layer: unità base di una rete neurale (Dense, Conv2D, LSTM, ecc.)
#     - Model: contenitore di layers (Sequential o Functional)
#     - Compile: configurazione dell'addestramento (optimizer, loss, metrics)
#     - Fit: addestramento del modello sui dati
#     - Evaluate: valutazione delle performance
#     - Predict: fare previsioni su nuovi dati
#
# Flusso di lavoro tipico:
#     1. Preparare i dati
#     2. Definire il modello (architettura della rete)
#     3. Compilare il modello
#     4. Addestrare il modello (fit)
#     5. Valutare il modello (evaluate)
#     6. Fare previsioni (predict)
#
# Differenza tra Keras standalone e tf.keras:
#     - tf.keras: integrato in TensorFlow, consigliato per nuovi progetti
#     - keras (standalone): versione indipendente, Keras 3 supporta anche PyTorch e JAX
#
# Installazione:
#     pip install keras tensorflow

import keras
import tensorflow as tf

print("Versione Keras:", keras.__version__)
print("Versione TensorFlow:", tf.__version__)

# Verifica disponibilità GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"GPU disponibile: {gpus}")
else:
    print("Nessuna GPU disponibile, si utilizzerà la CPU")
