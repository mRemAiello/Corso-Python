# Esercizi

# Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso.
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona,
# ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.



# Creare una classe Animale che abbia gli attributi “nome” e “specie”.
# Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie.
# Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.


# Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”.
# Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, ad esempio
# “Questa è una Toyota Corolla del 2017”.


# Realizzare una classe PersonalComputer (con costruttore) con le seguenti caratteristiche :
# marca, modello, tipo di processore, quantità di ram, spazio memoria HD e tipo di scheda video.
# Creare una funzione che stampi le informazioni del pc.
# Creare poi nel Main una serie di PersonalComputer variando marca, modello, ecc.



# Realizzare una classe Calcolatrice con 6 funzioni: Somma, Sottrazione, Moltiplicazione,
# Divisione, DivisioneResto e Potenza.
# Poi, nel Main, istanziare la classe ed eseguire le operazioni, mostrando i risultati delle operazioni.



# Realizzare una classe Studente e un'altra classe Insegnante. La classe Studente avrà un metodo public
# chiamato vado_in_classe, che scriverà a schermo "Sto andando in classe"
# La classe Insegnante avrà un metodo pubblico "insegna", che scriverà a schermo "Sto insegnando".
# Infine, entrambe le classi avranno un metodo pubblico imposta_eta (che prende in input un valore numerico
# intero e imposta l’età) e mostra_eta, che visualizza l'età.



# Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”.
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e
# un metodo aumenta_stipendio(x) che aumenta lo stipendio dell'x%.
# Inoltre inserire un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato,
# ad esempio “Impiegato: Marco Rossi, matricola: 12345, stipendio: 3000 Euro”.



# Crea una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.
# Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
#
#     Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
#     Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
#
# La classe dovrà avere i seguenti metodi:
#
#     Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
#     Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
#     Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
#
# Aggiungi poi la possibilità di inserire prodotti multipli (2 e una lista)



# Scrivere una classe Docente che rappresenti le seguenti informazioni relative ad un docente: nome, cognome, codice ed età, e che
# contenga il costruttore parametrizzato ed i metodi getCodice, getCognome e getEta che restituiscono
# rispettivamente il codice, il cognome e l’età del docente.
# Scrivere poi una classe Universita, che rappresenti un insieme di docenti universitari tramite una lista di tipo Docente,
# e che contenga il costruttore parametrizzato ed un
# metodo GetEtaMinima che restituisce la minima età tra i docenti universitari.
# Inserire poi nella classe Universita il metodo TrovaGiovani che restituisca il cognome del docente che ha età minima.


# Scrivete un programma per convertire la lettera di un voto scolastico nel numero corrispondente.
# Le lettere sono A, B, C, D e F, eventualmente seguite dai segni + o -. I loro valori numerici sono 4, 3, 2, 1 e 0. F+ e F- non esistono.
# Un segno + o – incrementa o decrementa il valore numerico di 0.3. Tuttavia, A+ è uguale a 4.0. Usate una classe Grade con un metodo getNumericGrade.
# Chiedere quindi voti all'utente all'ìnfinito finchè non scrive "Esci" (while)


# Realizzare 3 classi Chiave (Le chiavi possono essere meccaniche, magnetiche e con microchip) con le seguenti caratteristiche :
# descrizione, peso
# Le chiavi magnetiche sono caratterizzate dall'ampiezza, le chiavi meccaniche da un numero di dentelli.
# Sia le chiavi meccaniche che quelle magnetiche sono rappresentate dalla lunghezza.
# Inoltre, esiste un'operazione di aggiornamento per le chiavi con microchip.
# La chiave con microchip avrà un codice seriale (stringa), che verrà aggiornato dalla funzione sopra menzionata.
# Inserire, per ogni classe, una funzione che printa in maniera ordinata tutte le informazioni sulle chiavi
# Infine, inserire una funzione che verifica quale è la chiave più leggera
# Ogni chiave dovrà avere un costruttore che prenda in input tutti i parametri sopracitati.



# In questo esercizio, abbiamo definito due classi, Studente e Corso. La classe Studente rappresenta uno studente universitario
# con attributi come nome, cognome e matricola, oltre a un metodo per aggiungere corsi al suo elenco di corsi.
# Quando aggiungi un corso, inserisci anche un voto.
# Inserisci anche una funzione che faccia la media dei suoi voti.
# La classe Corso rappresenta un corso universitario con attributi come nome e codice.
# Successivamente, abbiamo creato due oggetti Studente e tre oggetti Corso e abbiamo aggiunto i corsi agli studenti.
# Infine, abbiamo stampato l'elenco dei corsi per ciascuno studente.



# In questo esempio, abbiamo definito due classi: Paziente e VisitaMedica.
# La classe Paziente rappresenta un paziente con attributi come nome, cognome, data di nascita e codice fiscale.
# Ha un metodo per aggiungere visite mediche all'elenco delle visite mediche del paziente e un metodo per elencare le visite mediche.
# La classe VisitaMedica rappresenta una visita medica con attributi come data, medico e diagnosi.
# La sua rappresentazione testuale è personalizzata tramite il metodo __str__.
# Abbiamo creato vari oggetti Paziente e VisitaMedica, aggiunto le visite mediche ai pazienti e poi stampato l'elenco delle visite mediche per ciascun paziente.



# Scrivere una classe Libro che rappresenti le seguenti informazioni relative ad un libro: titolo, autore, prezzo,
# e che contenga il costruttore parametrizzato ed
# i metodi getTitolo, getAutore e getPrezzo che restituiscono rispettivamente il titolo, l'autore e il prezzo del libro.
# Scrivere poi una classe Libreria, che rappresenti un insieme di libri tramite una lista di tipo Libro (che contenga il costruttore parametrizzato),
# ed un metodo Trova (che accetta in ingresso un autore a e intero k) e restituisce il numero di libri contenuti nella libreria aventi
# autore a e prezzo superiore a k.
# Aggiungere alla classe Libreria un metodo che accetti un autore a e restituisca i titoli di tutti i libri scritti dall’autore a.