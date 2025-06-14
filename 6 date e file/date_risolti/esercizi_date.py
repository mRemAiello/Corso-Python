# Scrivi un programma che stampa la data e l'ora corrente.


# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e stampa il nome del mese corrispondente.


# Scrivi un programma che prende in input due date e calcola la differenza in giorni tra le due.


# Scrivi un programma che prende in input una data e un numero di giorni, e calcola la data che viene
# dopo quella data del numero di giorni specificato.


# Scrivi un programma che stampa tutti i giorni di un determinato mese e anno.


# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e verifica se l'anno è bisestile o meno.
# Un anno bisestile e’ identificato da un intero maggiore di 1584 che sia divisibile per 4 ma non per 100,
# oppure che sia divisibile per 400.
# Prendere in input una variabile intera che rappresenti l’anno e mediante print visualizzare
# BISESTILE se l’anno inserito è bisestile, e NON BISESTILE altrimenti.

# Scrivi un programma che prende in input due date e stampa tutte le date comprese tra le due (inclusi i bordi).


# Scrivi una funzione che prenda in input due date come oggetti datetime e
# restituisca il numero di giorni trascorsi tra di esse.


# Scrivi una funzione che prenda in input una data come oggetto datetime e
# restituisca il giorno della settimana corrispondente come stringa.


# Scrivi una funzione che prenda in input una data come oggetto datetime e
# restituisca il numero della settimana corrispondente nell'anno.




# Creare un catalogo di libri che contenga informazioni come il titolo, l'autore, l'anno di pubblicazione e la disponibilità.
# Gli utenti dovrebbero poter cercare libri nel catalogo per titolo o autore.
# Gli utenti dovrebbero poter prendere in prestito un libro, riducendo la sua disponibilità e assegnando una data di scadenza.
# Gli utenti dovrebbero poter restituire un libro, aumentando la sua disponibilità e rimuovendo la data di scadenza.
# Gli utenti dovrebbero poter visualizzare un elenco di libri disponibili e un elenco di libri attualmente in prestito.
# Gli amministratori della biblioteca dovrebbero poter aggiungere nuovi libri al catalogo e rimuoverli quando non sono più disponibili.
# Gestire i dettagli degli utenti, come il nome e il numero di tessera, per tenere traccia dei prestiti.
# Utilizzare la classe Date di Python per gestire le date di scadenza dei prestiti.
# Fornire un'interfaccia utente intuitiva per interagire con il sistema.


# Il gestore di un negozio associa a tutti i suoi Prodotti un codice a barre univoco,
# una descrizione sintetica del prodotto e il suo prezzo unitario.
# Realizzare una classe Prodotto con variabili, costruttore e funzione __str__
# Aggiungere alla classe Prodotto un metodo applicaSconto che modifica il prezzo del prodotto diminuendolo del 5%.
# Il gestore del negozio vuole fare una distinzione tra i prodotti Alimentari e quelli Non Alimentari .
# Ai prodotti Alimentari viene infatti associata una data di scadenza, mentre a quelli Non Alimentari
# il materiale principale di cui sono fatti, e se tale materiale è ricicabile o meno.
# Realizzare le sottoclassi Alimentari e NonAlimentari estendendo opportunamente la classe Prodotto.
# Modificare le due sottoclassi specializzando il metodo applicaSconto in modo che nel caso dei prodotti
# Alimentari venga applicato uno sconto del 20% se la data di scadenza è a meno di 10 giorni dalla data attuale,
# mentre nel caso dei prodotti Non Alimentari venga applicato uno sconto del 10% se il prodotto
# è composto da un materiale riciclabile (carta, vetro o plastica).
# Realizzare una classe ListaSpesa che chieda all'utente di inserire i prodotti acquistati e
# calcoli il totale della spesa applicando gli opportuni sconti se il cliente ha la tessera fedeltà.