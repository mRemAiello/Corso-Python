# ==========================================
# ESERCIZI KERAS
# ==========================================

# ------------------------------------------
# Esercizio 1: Regressione lineare semplice
# ------------------------------------------
# Obiettivo: Creare un modello per imparare la relazione y = 3x + 5
#
#     1. Genera 200 punti con X casuali tra 0 e 10, e Y = 3*X + 5 + rumore
#     2. Costruisci un modello Sequential con un solo layer Dense (1 neurone)
#     3. Compila con optimizer='sgd' e loss='mse'
#     4. Addestra per 100 epoche
#     5. Predici il valore per X = 15 (il risultato dovrebbe essere circa 50)
#     6. Stampa i pesi del modello e verifica che siano vicini a 3 (peso) e 5 (bias)
#        Suggerimento: model.layers[0].get_weights()


# ------------------------------------------
# Esercizio 2: Classificazione binaria
# ------------------------------------------
# Obiettivo: Classificare se uno studente supererà l'esame
#
#     1. Genera un dataset con 500 campioni e 3 feature:
#        - ore_studio (0-20), media_voti (18-30), frequenza (0-100%)
#     2. L'etichetta è 1 (promosso) se: ore_studio > 8 AND media_voti > 22
#     3. Costruisci un modello con 2 layer nascosti (32 e 16 neuroni, relu)
#        e un layer di output con sigmoid
#     4. Compila con binary_crossentropy e optimizer adam
#     5. Addestra con validation_split=0.2
#     6. Valuta l'accuratezza sul test set
#     7. Predici per uno studente con: ore_studio=12, media=25, frequenza=80


# ------------------------------------------
# Esercizio 3: Classificazione multiclasse con Fashion MNIST
# ------------------------------------------
# Obiettivo: Classificare capi di abbigliamento
#
#     1. Carica il dataset Fashion MNIST (keras.datasets.fashion_mnist)
#     2. Normalizza le immagini (0-1) e applica one-hot encoding alle etichette
#     3. Costruisci un modello con:
#        - Input: 784 neuroni (immagini 28x28 appiattite)
#        - 2 layer nascosti con Dropout
#        - Output: 10 neuroni con softmax
#     4. Usa EarlyStopping con patience=5
#     5. Addestra e visualizza i grafici di loss e accuracy
#     6. Stampa la matrice di confusione
#     Suggerimento: usa sklearn.metrics.confusion_matrix


# ------------------------------------------
# Esercizio 4: Confronto architetture
# ------------------------------------------
# Obiettivo: Confrontare le performance di modelli diversi sullo stesso dataset
#
#     1. Carica il dataset MNIST
#     2. Costruisci 3 modelli diversi:
#        a) Modello piccolo: 1 layer nascosto, 32 neuroni
#        b) Modello medio: 2 layer nascosti, 128 e 64 neuroni
#        c) Modello grande: 3 layer nascosti, 256, 128 e 64 neuroni con Dropout
#     3. Addestra tutti e 3 per 15 epoche
#     4. Confronta le accuracy sul test set
#     5. Crea un grafico a barre con le accuracy dei 3 modelli
#     Domanda: quale modello ha la migliore accuracy? Perché?


# ------------------------------------------
# Esercizio 5: Functional API - Multi-input
# ------------------------------------------
# Obiettivo: Creare un modello che predice il voto finale di uno studente
#
#     1. Input 1: dati accademici (media_voti, esami_superati, crediti) - 3 feature
#     2. Input 2: dati personali (ore_studio_settimanali, distanza_da_uni) - 2 feature
#     3. Ogni input passa per un ramo separato con 2 layer Dense
#     4. I rami vengono uniti con Concatenate
#     5. L'output è un singolo valore (regressione del voto finale)
#     6. Genera dati sintetici, addestra e valuta
#     Suggerimento: usa keras.Input() e keras.Model()


# ------------------------------------------
# Esercizio 6: Callbacks personalizzati
# ------------------------------------------
# Obiettivo: Creare un callback personalizzato che stampa un messaggio
#            ogni volta che l'accuracy supera una soglia
#
#     1. Crea una classe che eredita da keras.callbacks.Callback
#     2. Nel metodo on_epoch_end, controlla se val_accuracy > 0.95
#     3. Se sì, stampa "Obiettivo raggiunto all'epoca X!"
#     4. Usa questo callback insieme a EarlyStopping su MNIST
#     5. Addestra il modello e osserva l'output
#     Suggerimento: i log dell'epoca sono nel parametro 'logs' di on_epoch_end


# ------------------------------------------
# Esercizio 7: Salvataggio e caricamento
# ------------------------------------------
# Obiettivo: Addestrare un modello, salvarlo, caricarlo e verificare che funzioni
#
#     1. Addestra un modello su MNIST per 10 epoche
#     2. Valuta l'accuracy e salvala in una variabile
#     3. Salva il modello in formato .keras
#     4. Carica il modello salvato con keras.models.load_model()
#     5. Valuta l'accuracy del modello caricato
#     6. Verifica che le due accuracy siano identiche
#     7. Salva solo i pesi, crea un nuovo modello con la stessa architettura,
#        carica i pesi e verifica che le predizioni siano le stesse


# ------------------------------------------
# Esercizio 8: Analisi dell'overfitting
# ------------------------------------------
# Obiettivo: Dimostrare e risolvere l'overfitting
#
#     1. Carica il dataset MNIST e usa solo i primi 1000 campioni per il training
#     2. Costruisci un modello "troppo grande" (512, 256, 128 neuroni, senza Dropout)
#     3. Addestra per 50 epoche e salva la history
#     4. Costruisci un secondo modello identico MA con Dropout(0.5) dopo ogni layer
#     5. Addestra anche questo per 50 epoche
#     6. Crea un grafico con 4 curve:
#        - Training loss modello 1 vs Validation loss modello 1
#        - Training loss modello 2 vs Validation loss modello 2
#     7. Confronta: quale modello soffre di meno di overfitting?
#     Domanda: perché il Dropout aiuta a ridurre l'overfitting?


# ------------------------------------------
# Esercizio 9: Data Augmentation su CIFAR-10
# ------------------------------------------
# Obiettivo: Verificare l'impatto della data augmentation
#
#     1. Carica il dataset CIFAR-10 (usa solo i primi 5000 campioni)
#     2. Addestra un modello SENZA data augmentation per 20 epoche
#     3. Addestra lo stesso modello CON data augmentation (RandomFlip, RandomRotation)
#     4. Confronta le accuracy dei due modelli sul test set
#     5. Visualizza 10 immagini con le rispettive versioni "augmented"
#     Domanda: in quale scenario la data augmentation è più utile?


# ------------------------------------------
# Esercizio 10: Progetto completo
# ------------------------------------------
# Obiettivo: Costruire un sistema completo di classificazione
#
#     1. Scegli un dataset (es. Fashion MNIST o CIFAR-10)
#     2. Esplora i dati: dimensioni, classi, distribuzioni
#     3. Pre-elabora i dati (normalizzazione, encoding)
#     4. Costruisci almeno 2 modelli diversi
#     5. Usa callbacks (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau)
#     6. Addestra entrambi i modelli e confronta i risultati
#     7. Visualizza:
#        a) Grafici di loss e accuracy per entrambi i modelli
#        b) Matrice di confusione del modello migliore
#        c) Almeno 15 predizioni con immagine, predizione e label reale
#     8. Salva il modello migliore
#     9. Scrivi un breve commento con le conclusioni
