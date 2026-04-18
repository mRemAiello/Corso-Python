# ==============================================================================
# DEEP LEARNING - Introduzione Approfondita
# ==============================================================================

# ==============================================================================
# 1. Cos'è il Deep Learning?
# ==============================================================================
# Il deep learning è un sottoinsieme del machine learning che si basa su reti neurali
# artificiali composte da molti strati (da cui il termine "deep", ovvero profondo).
#
# Gerarchia:
#   Intelligenza Artificiale (AI)
#       └── Machine Learning (ML)
#               └── Deep Learning (DL)
#
# L'idea fondamentale è ispirata al cervello umano: i neuroni biologici ricevono
# segnali, li elaborano e li trasmettono ad altri neuroni. Allo stesso modo,
# i neuroni artificiali ricevono dati in input, applicano dei pesi e una funzione
# di attivazione, e producono un output.
#
# Cosa lo rende "deep" (profondo)?
#   Un modello di deep learning ha molti strati nascosti (hidden layers),
#   tipicamente da decine a centinaia. Ogni strato impara rappresentazioni
#   sempre più astratte e complesse dei dati.
#
# Esempio con un'immagine di un gatto:
#   Strato 1: rileva bordi e linee semplici
#   Strato 2: combina i bordi in forme (cerchi, angoli)
#   Strato 3: riconosce parti del corpo (orecchie, occhi, zampe)
#   Strato 4: combina le parti per riconoscere "è un gatto"

# ==============================================================================
# 2. Come funziona una rete neurale?
# ==============================================================================
# Una rete neurale è composta da:
#
#   a) Layer di input: riceve i dati grezzi (es. i pixel di un'immagine)
#
#   b) Layer nascosti (hidden layers): elaborano i dati in modo progressivo.
#      Ogni neurone in un layer:
#        - Riceve valori dal layer precedente
#        - Li moltiplica per dei "pesi" (weights)
#        - Aggiunge un valore di "bias"
#        - Applica una funzione di attivazione (es. ReLU, sigmoid)
#        - Produce un output che passa al layer successivo
#
#   c) Layer di output: produce il risultato finale
#      (es. "gatto" con 95% di probabilità)
#
# L'addestramento avviene così:
#   1. Forward pass: i dati attraversano la rete e producono una predizione
#   2. Calcolo della loss: si misura quanto la predizione è lontana dal valore reale
#   3. Backpropagation: si calcolano i gradienti (quanto ogni peso ha contribuito all'errore)
#   4. Aggiornamento pesi: l'optimizer aggiorna i pesi per ridurre l'errore
#   5. Si ripete per migliaia/milioni di volte fino a convergenza

# ==============================================================================
# 3. Tipi di reti neurali
# ==============================================================================
#
# a) Reti Dense (Fully Connected / MLP - Multi Layer Perceptron)
#    - Ogni neurone è connesso a tutti i neuroni del layer precedente
#    - Usate per: dati tabulari, classificazione semplice, regressione
#    - Esempio: prevedere il prezzo di una casa in base a superficie, posizione, ecc.
#
# b) Reti Convoluzionali (CNN - Convolutional Neural Networks)
#    - Usano filtri che scorrono sull'immagine per estrarre feature spaziali
#    - Usate per: riconoscimento immagini, video, elaborazione visiva
#    - Esempio: classificare foto di cani vs gatti, riconoscimento facciale
#
# c) Reti Ricorrenti (RNN - Recurrent Neural Networks)
#    - Hanno una "memoria" che permette di elaborare sequenze di dati
#    - Usate per: testo, serie temporali, audio
#    - Varianti: LSTM (Long Short-Term Memory), GRU (Gated Recurrent Unit)
#    - Esempio: previsione del prezzo delle azioni, traduzione automatica
#
# d) Transformer
#    - Architettura basata sul meccanismo di "attenzione" (attention)
#    - Rivoluzionari per il linguaggio naturale
#    - Esempio: GPT (ChatGPT), BERT, modelli di traduzione
#    - Usati anche per immagini (Vision Transformer - ViT)
#
# e) GAN (Generative Adversarial Networks)
#    - Due reti che competono: un generatore (crea dati falsi) e un discriminatore
#      (cerca di distinguere vero da falso)
#    - Usate per: generazione di immagini, deepfake, super-risoluzione
#    - Esempio: creare volti realistici di persone che non esistono
#
# f) Autoencoder
#    - Comprimono i dati in una rappresentazione più piccola e poi li ricostruiscono
#    - Usati per: riduzione del rumore, compressione, rilevamento anomalie
#    - Esempio: ripulire immagini sfocate o danneggiate

# ==============================================================================
# 4. Esempi pratici nel mondo reale
# ==============================================================================
#
# VISIONE ARTIFICIALE:
#   - Riconoscimento facciale: sblocco del telefono con il volto (Face ID)
#   - Classificazione immagini: Google Foto che riconosce persone e luoghi
#   - Guida autonoma: Tesla Autopilot che riconosce segnali, pedoni, veicoli
#   - Controllo qualità: fabbriche che rilevano difetti nei prodotti in tempo reale
#   - Imaging medico: rilevamento tumori nelle radiografie con accuratezza >95%
#
# ELABORAZIONE DEL LINGUAGGIO NATURALE (NLP):
#   - Chatbot e assistenti: ChatGPT, Siri, Alexa, Google Assistant
#   - Traduzione automatica: Google Translate, DeepL
#   - Analisi del sentimento: capire se una recensione è positiva o negativa
#   - Riassunto automatico: sintetizzare articoli e documenti lunghi
#   - Generazione di codice: GitHub Copilot
#
# AUDIO E VOCE:
#   - Riconoscimento vocale: trascrizione automatica di riunioni (Whisper, Google STT)
#   - Sintesi vocale: voci artificiali realistiche (text-to-speech)
#   - Riconoscimento musicale: Shazam che identifica una canzone
#
# SCIENZE E MEDICINA:
#   - Scoperta di farmaci: AlphaFold di DeepMind predice la struttura delle proteine
#   - Diagnosi mediche: rilevamento di malattie della retina, tumori al seno
#   - Genomica: analisi del DNA per prevedere predisposizioni genetiche
#
# FINANZA:
#   - Trading algoritmico: previsione dei mercati finanziari
#   - Rilevamento frodi: identificare transazioni sospette su carte di credito
#   - Credit scoring: valutare l'affidabilità di un cliente per un prestito
#
# GIOCHI E INTRATTENIMENTO:
#   - AlphaGo: ha battuto il campione mondiale di Go (gioco da tavolo)
#   - AI nei videogiochi: NPC (personaggi non giocanti) più intelligenti
#   - Generazione procedurale: creazione automatica di livelli, mondi, musiche

# ==============================================================================
# 5. Vantaggi del Deep Learning
# ==============================================================================
#
# a) Non richiede feature engineering manuale
#    Nel ML classico bisogna decidere manualmente quali caratteristiche estrarre
#    (es. per riconoscere un gatto: "ha orecchie a punta? ha i baffi?").
#    Il DL impara automaticamente le feature rilevanti dai dati grezzi.
#
# b) Performance superiori su dati complessi
#    Per immagini, audio, video e testo, il DL supera quasi sempre il ML classico.
#    In alcuni compiti supera anche le capacità umane (es. diagnosi mediche).
#
# c) Scalabilità
#    Più dati e più potenza di calcolo = performance migliori.
#    I modelli migliorano semplicemente aumentando la quantità di dati.
#
# d) Versatilità
#    La stessa architettura (es. Transformer) può essere applicata a problemi
#    molto diversi: testo, immagini, audio, proteine, codice sorgente.
#
# e) Transfer learning
#    Un modello addestrato su un compito può essere riutilizzato per un altro,
#    risparmiando tempo e risorse. Es: un modello addestrato su ImageNet
#    (milioni di immagini) può essere adattato per classificare radiografie.

# ==============================================================================
# 6. Svantaggi del Deep Learning
# ==============================================================================
#
# a) Richiede enormi quantità di dati
#    Un modello di DL tipicamente ha bisogno di migliaia o milioni di esempi.
#    Con pochi dati, il ML classico (es. Random Forest, SVM) può funzionare meglio.
#
# b) Costo computazionale elevato
#    L'addestramento richiede GPU potenti (es. NVIDIA A100, H100).
#    Addestrare GPT-4 è costato stimatamente oltre 100 milioni di dollari.
#    Anche l'inferenza (usare il modello) può essere costosa.
#
# c) "Scatola nera" (Black Box)
#    È molto difficile capire PERCHÉ il modello prende una certa decisione.
#    Questo è un problema critico in ambiti come medicina e giustizia,
#    dove serve spiegabilità (Explainable AI - XAI).
#
# d) Overfitting
#    Con troppi parametri e pochi dati, il modello "memorizza" il dataset
#    di training invece di imparare regole generali.
#    Soluzioni: Dropout, data augmentation, regolarizzazione, early stopping.
#
# e) Tempi di addestramento lunghi
#    Addestrare un modello complesso può richiedere ore, giorni o settimane,
#    anche con hardware dedicato (GPU/TPU).
#
# f) Sensibilità agli iperparametri
#    Learning rate, architettura, batch size, numero di epoche...
#    Piccole variazioni possono cambiare drasticamente le performance.
#    Trovare la configurazione ottimale richiede esperimenti ripetuti.
#
# g) Bias nei dati
#    Se i dati di training contengono pregiudizi (es. dati sbilanciati per genere
#    o etnia), il modello li apprende e li amplifica nelle sue predizioni.

# ==============================================================================
# 7. Deep Learning vs Machine Learning classico: quando usare cosa?
# ==============================================================================
#
#   Caratteristica           | ML Classico              | Deep Learning
#   -------------------------|--------------------------|---------------------------
#   Quantità di dati         | Pochi dati bastano       | Servono molti dati
#   Tipo di dati             | Dati tabulari/strutturati | Immagini, testo, audio
#   Feature engineering      | Manuale                  | Automatico
#   Interpretabilità         | Alta                     | Bassa (black box)
#   Costo computazionale     | Basso (CPU sufficiente)  | Alto (servono GPU/TPU)
#   Tempo di addestramento   | Minuti                   | Ore/giorni
#   Performance su immagini  | Limitata                 | Eccellente
#   Esempi di algoritmi      | Random Forest, SVM, KNN  | CNN, RNN, Transformer
#
# Regola pratica:
#   - Dati tabulari (CSV, database) => prova prima ML classico (Scikit-Learn)
#   - Immagini, testo, audio => vai diretto con Deep Learning (Keras/TensorFlow)
#   - Pochi dati (<1000 campioni) => ML classico o transfer learning

# ==============================================================================
# 8. Librerie e framework principali
# ==============================================================================
#
# TensorFlow (Google): framework completo per DL, include Keras come API di alto livello.
# Keras: API intuitiva e user-friendly, integrata in TensorFlow (tf.keras).
# PyTorch (Meta/Facebook): framework molto usato nella ricerca, più "pythonic".
# JAX (Google): libreria per calcolo numerico ad alte prestazioni con autograd.
# Scikit-Learn: ML classico (non deep learning), ottimo per dati tabulari.