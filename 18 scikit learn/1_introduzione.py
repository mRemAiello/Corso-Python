# Cos'è Scikit-Learn?
#
# Scikit-Learn è una libreria Python open-source per il machine learning. Offre:
#
#       Modelli supervisionati (classificazione, regressione)
#       Supervisionati: il modello impara da dati etichettati, cioè per ogni input conosce il risultato corretto.
#
#       Modelli non supervisionati (clustering, PCA)
#       Non supervisionati: il modello lavora su dati non etichettati, cerca pattern, gruppi o riduzioni di dimensionalità.
#
#     Preprocessing e selezione delle feature
#
#     Pipeline e strumenti di validazione



# Cosa sono train e test
#
# Nel Machine Learning, quando abbiamo un dataset,
# non alleniamo il modello sull’intero dataset, perché vogliamo testare la sua capacità
# di generalizzare su dati mai visti prima.
#
# Per questo motivo, suddividiamo i dati in due (a volte tre) insiemi:
#
#     Train set (training set):
#     È l’insieme di dati usato per allenare il modello.
#     X => Sepal length, width, Petal length e width
#     Y => Setosa
#     Serve per "fargli imparare" le relazioni tra gli input (X) e l’output (y).
#
#     Test set:
#     È l’insieme di dati usato per valutare le performance del modello su nuovi dati.
#     Serve a capire se il modello ha imparato davvero o solo memorizzato (overfitting).


# fit_transform() è un metodo combinato che:
#
#     “Fitta” (fit) il trasformatore sul dataset, cioè calcola i parametri statistici necessari (es. media e deviazione standard).
#
#     “Trasforma” (transform) i dati usando quei parametri.


#  Cos'è StandardScaler
#
# StandardScaler è una classe di Scikit-Learn che standardizza le feature in modo che abbiano:
#
#     media = 0
#     deviazione standard = 1
#
# Serve per mettere tutte le feature sullo stesso ordine di grandezza,
# soprattutto quando usi modelli sensibili alle scale (es. regressione, KNN, SVM).
