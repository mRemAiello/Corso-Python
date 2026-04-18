# Functional API
#
# La Functional API è un modo più flessibile di costruire modelli in Keras.
# A differenza del modello Sequential (lineare), permette di creare:
#     - Modelli con input multipli
#     - Modelli con output multipli
#     - Layer condivisi
#     - Architetture complesse (reti residuali, ecc.)
#
# Sintassi:
#     inputs = Input(shape=(...))
#     x = Layer(...)(inputs)       # Ogni layer viene "chiamato" sull'output del precedente
#     outputs = Layer(...)(x)
#     model = Model(inputs, outputs)

import numpy as np
from keras import Model, Input
from keras.layers import Dense, Concatenate

# ==========================================
# Esempio 1: Modello semplice con Functional API
# ==========================================

inputs = Input(shape=(10,), name='input_features')
x = Dense(64, activation='relu', name='hidden_1')(inputs)
x = Dense(32, activation='relu', name='hidden_2')(x)
outputs = Dense(1, name='output')(x)

model_simple = Model(inputs=inputs, outputs=outputs, name='modello_semplice')
model_simple.summary()

# ==========================================
# Esempio 2: Modello con input multipli
# ==========================================
# Scenario: prevedere il prezzo di una casa
# Input 1: dati numerici (superficie, stanze, ecc.)
# Input 2: dati sulla zona (distanza dal centro, servizi, ecc.)

input_casa = Input(shape=(3,), name='dati_casa')        # superficie, stanze, anno
input_zona = Input(shape=(2,), name='dati_zona')        # distanza centro, servizi

# Ramo per i dati della casa
x1 = Dense(32, activation='relu')(input_casa)
x1 = Dense(16, activation='relu')(x1)

# Ramo per i dati della zona
x2 = Dense(16, activation='relu')(input_zona)
x2 = Dense(8, activation='relu')(x2)

# Unione dei due rami
merged = Concatenate()([x1, x2])
x = Dense(32, activation='relu')(merged)
output_prezzo = Dense(1, name='prezzo')(x)

model_multi = Model(
    inputs=[input_casa, input_zona],
    outputs=output_prezzo,
    name='modello_multi_input'
)

model_multi.summary()

# Compilazione e addestramento
model_multi.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Dati di esempio
np.random.seed(42)
X_casa = np.random.rand(500, 3)
X_zona = np.random.rand(500, 2)
y_prezzo = np.random.rand(500, 1) * 500000

model_multi.fit(
    [X_casa, X_zona], y_prezzo,
    epochs=20,
    batch_size=32,
    validation_split=0.2,
    verbose=1
)

# ==========================================
# Esempio 3: Modello con output multipli
# ==========================================
# Scenario: classificare un'immagine e stimarne la qualità

input_img = Input(shape=(784,), name='immagine')
shared = Dense(128, activation='relu')(input_img)
shared = Dense(64, activation='relu')(shared)

# Output 1: classificazione (10 classi)
out_classe = Dense(10, activation='softmax', name='classe')(shared)

# Output 2: punteggio qualità (regressione)
out_qualita = Dense(1, name='qualita')(shared)

model_multi_out = Model(
    inputs=input_img,
    outputs=[out_classe, out_qualita],
    name='modello_multi_output'
)

model_multi_out.summary()

# Compilazione con loss e metriche diverse per ogni output
model_multi_out.compile(
    optimizer='adam',
    loss={
        'classe': 'sparse_categorical_crossentropy',
        'qualita': 'mse'
    },
    metrics={
        'classe': 'accuracy',
        'qualita': 'mae'
    }
)

print("\nModello con output multipli compilato con successo!")
