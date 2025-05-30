# Esercizi


# Immagina di dover creare un'applicazione per la gestione di una biblioteca.
# L'applicazione dovrebbe consentire agli utenti di cercare libri nel catalogo, prendere in prestito libri, restituire libri
# e tenere traccia dei prestiti attivi. Inoltre, dovrebbe essere possibile aggiungere nuovi libri al catalogo e rimuoverli
# quando non sono più disponibili.
# Gli utenti dovrebbero essere in grado di visualizzare un elenco dei libri disponibili e dei libri attualmente in prestito.

# Requisiti dell'applicazione:
# Creare un catalogo di libri che contenga informazioni come il titolo, l'autore, l'anno di pubblicazione e la disponibilità.
# Gli utenti dovrebbero poter cercare libri nel catalogo per titolo o autore.
# Gli utenti dovrebbero poter prendere in prestito un libro, riducendo la sua disponibilità.
# Dopo un certo periodo di tempo, il libro dovrebbe essere restituito automaticamente e la disponibilità dovrebbe essere aggiornata.
# Gli utenti dovrebbero poter visualizzare un elenco di libri disponibili e un elenco di libri attualmente in prestito.
# Gli amministratori della biblioteca dovrebbero poter aggiungere nuovi libri al catalogo e rimuoverli quando non sono più disponibili.
# Gestire i dettagli degli utenti, come il nome e il numero di tessera, per tenere traccia dei prestiti.
# Fornire un'interfaccia utente intuitiva per interagire con il sistema.




# Creare una classe base chiamata Videogioco con le seguenti proprietà:
#   titolo (string): il titolo del videogioco.
#   genere (string): il genere del videogioco.
#   valutazione (float): il punteggio di valutazione del videogioco (da 0 a 10).
#   disponibile (bool): indica se il videogioco è disponibile per il noleggio.
#
# Creare almeno quattro sottoclassi (videogiochi specifici) ereditando dalla classe Videogioco.
# Ad esempio, si possono creare sottoclassi come Azione e Avventura.
# Ogni sottoclasse deve avere almeno una proprietà specifica e un metodo che ne gestisce la specifica funzionalità.
#
# Creare una classe LibreriaVideogiochi che gestisce l'inventario dei videogiochi disponibili e includa le seguenti funzioni:
# aggiungi_videogioco(self, videogioco): aggiunge un videogioco all'inventario.
# rimuovi_videogioco(self, titolo): rimuove un videogioco dall'inventario dato il titolo.
# trova_videogioco(self, titolo): restituisce il videogioco corrispondente al titolo fornito.
# elenco_videogiochi(self): stampa l'elenco dei videogiochi disponibili, inclusi titolo, genere, punteggio e disponibilità.
# Creare una funzione esterna calcola_media_valutazioni(libreria) che calcoli la media delle valutazioni di tutti i videogiochi presenti nella libreria.
# Creare una funzione esterna conteggio_videogiochi_per_genere(libreria) che restituisca un dizionario con il conteggio dei videogiochi per ciascun genere presente nella libreria.




# Creare una classe chiamata Cliente con le seguenti proprietà:
#   nome (string): il nome del cliente.
#   cognome (string): il cognome del cliente.
#   identificazione_fiscale (string): il numero di identificazione fiscale del cliente.
#   conti_correnti (dizionario): un dizionario che contiene i conti correnti del cliente (numero di conto come chiave e oggetto ContoCorrente come valore).
#
# Creare una classe chiamata ContoCorrente con le seguenti proprietà:
#   numero_conto (int): il numero del conto corrente.
#   saldo (float): il saldo del conto corrente.
#   proprietario (oggetto Cliente): il cliente proprietario del conto corrente.
#
# Creare una classe chiamata Banca con le seguenti proprietà:
#   nome (string): il nome della banca.
#   clienti (dizionario): un dizionario che contiene i clienti della banca (numero di identificazione fiscale come chiave e oggetto Cliente come valore).
#
# Creare una funzione crea_cliente(nome, cognome, identificazione_fiscale) che crea un nuovo cliente e lo aggiunge alla lista dei clienti della banca.
# Creare una funzione crea_conto_corrente(cliente) che crea un nuovo conto corrente per un cliente specifico e lo aggiunge ai suoi conti correnti.
# Creare una funzione deposito(conto_corrente, importo) che permette di effettuare un deposito su un conto corrente specifico.
# Creare una funzione prelievo(conto_corrente, importo) che permette di effettuare un prelievo da un conto corrente specifico.
# Creare una funzione saldo_conto(conto_corrente) che restituisce il saldo corrente di un conto corrente specifico.





#     Creare una classe base chiamata Giocatore con le seguenti proprietà:
#         nome (string): il nome del giocatore.
#         cognome (string): il cognome del giocatore.
#         numero_maglia (int): il numero di maglia del giocatore.
#         posizione (string): la posizione in campo del giocatore.
#
#     Creare almeno 4 sottoclassi (giocatori specifici) ereditando dalla classe Giocatore.
#     Ad esempio, si possono creare sottoclassi come Portiere e Attaccante. Ogni sottoclasse deve avere almeno una proprietà specifica e un metodo che ne gestisce la specifica funzionalità.
#
#     Creare una classe chiamata SquadraSportiva con le seguenti proprietà:
#         nome (string): il nome della squadra sportiva.
#         giocatori (dizionario): un dizionario che contiene i giocatori della squadra (numero di maglia come chiave e oggetto Giocatore come valore).
#
#     Creare una funzione aggiungi_giocatore(nome, cognome, numero_maglia, posizione) che crea un nuovo giocatore e lo aggiunge alla lista dei giocatori della squadra.
#     Creare una funzione rimuovi_giocatore(numero_maglia) che rimuove un giocatore dalla squadra dato il suo numero di maglia.
#     Creare una funzione elenco_giocatori() che stampa l'elenco dei giocatori della squadra, inclusi nome, cognome, numero di maglia e posizione.




# Creare una classe base chiamata FiguraGeometrica con le seguenti proprietà:
# tipo (string): il tipo di figura geometrica (ad esempio, "Cerchio" o "Quadrato").
# colore (string): il colore della figura geometrica.
# area (float): l'area della figura geometrica (inizialmente impostata a 0.0).
#
# Creare 4 sottoclassi (figure geometriche specifiche) ereditando dalla classe FiguraGeometrica.
# Ad esempio, si possono creare sottoclassi come Cerchio, Quadrato, Triangolo e Rettangolo.
# Ogni sottoclasse deve avere almeno una proprietà specifica e un metodo che calcoli l'area.
#
# Creare una classe chiamata GestoreFigure con le seguenti proprietà:
# figure (dizionario): un dizionario che contiene le figure geometriche (nome della figura come chiave e oggetto FiguraGeometrica come valore).
#
# Creare una funzione aggiungi_figura(nome, figura) che aggiunge una figura geometrica al gestore.
# Creare una funzione calcola_area_totale() che calcoli l'area totale di tutte le figure geometriche presenti nel gestore.
# Creare una funzione elenco_figure() che stampi l'elenco delle figure geometriche presenti nel gestore, inclusi nome, tipo, colore e area.










