# =============================================================================
# ESERCIZI SULLE TUPLE
# =============================================================================


# --- SEZIONE 1: Creazione e modifica ---

# 1. Creare una tupla vuota e assegnarla a una variabile.
#    Verificare il suo tipo con type() e la sua lunghezza con len().

# 2. Creare una tupla contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".
#    Aggiungere l'elemento "pesca", poi rimuovere ogni occorrenza di "mela" dalla tupla.
#    Stampare la tupla risultante.

# 3. Partendo dalla tupla dell'esercizio precedente, aggiungere "ananas".
#    Verificare se "ananas" è presente nella tupla, stampare un messaggio appropriato,
#    quindi rimuoverlo e stampare la tupla finale.

# 4. Creare una tupla contenente cinque elementi di tipi diversi
#    (es. intero, float, stringa, booleano, None).
#    Stampare il tipo di ciascun elemento con un ciclo.

# 5. Date due tuple di numeri interi, creare una terza tupla che sia la loro concatenazione.
#    Poi creare una quarta tupla contenente solo gli elementi in comune tra le prime due.


# --- SEZIONE 2: Accesso, slicing e unpacking ---

# 6. Data la tupla (10, 20, 30, 40, 50, 60, 70, 80, 90, 100):
#    - Stampare il primo e l'ultimo elemento usando gli indici.
#    - Stampare gli elementi dal terzo al sesto (inclusi) usando lo slicing.
#    - Stampare gli elementi in ordine inverso usando lo slicing.
#    - Stampare un elemento ogni due usando lo slicing.

# 7. Data la tupla ("nome", "cognome", "età", "città"),
#    effettuare l'unpacking in quattro variabili e stamparle.
#    Poi, data una tupla di lunghezza sconosciuta, usare l'unpacking con * per
#    separare il primo elemento, l'ultimo e tutti quelli in mezzo.

# 8. Data una tupla annidata come ((1, 2), (3, 4), (5, 6)),
#    accedere a ciascun elemento interno e stamparli tutti su una riga.


# --- SEZIONE 3: Iterazione e filtraggio ---

# 9.  Creare una tupla con i numeri interi da 1 a 10.
#     Con un ciclo for, estrarre i numeri pari in una nuova tupla e i dispari in un'altra.
#     Ripetere l'esercizio usando un ciclo while.
#     Infine, fare lo stesso con un unico ciclo che popoli entrambe le tuple.

# 10. Data una tupla di stringhe, creare due nuove tuple:
#     una con le stringhe di lunghezza pari e una con quelle di lunghezza dispari.
#     Usare sia for che while.

# 11. Data una tupla di numeri (inclusi negativi e zero),
#     creare tre tuple separate: una con i positivi, una con i negativi, una con gli zeri.

# 12. Data una tupla con elementi ripetuti, creare una nuova tupla
#     contenente solo gli elementi unici (senza duplicati), mantenendo l'ordine originale.


# --- SEZIONE 4: Ricerca e ordinamento ---

# 13. Data una tupla di stringhe, riordinarla in ordine alfabetico.
#     Implementare l'ordinamento usando un ciclo for e poi con un ciclo while.
#     Stampare la tupla originale e quella ordinata.

# 14. Data una tupla di numeri, trovare il valore massimo e il minimo
#     senza usare le funzioni built-in max() e min(), ma scorrendo la tupla con un ciclo.

# 15. Data una tupla di parole, contare quante volte appare una parola specifica
#     senza usare il metodo count(). Usare sia for che while.

# 16. Data una tupla di numeri interi, verificare se è ordinata in modo crescente.
#     Stampare True o False.


# --- SEZIONE 5: Liste di tuple ---

# 17. Creare una lista di tuple in cui ogni tupla contiene due stringhe.
#     Stampare solo le tuple in cui entrambe le stringhe hanno lunghezza pari.
#     Fare lo stesso per quelle con entrambe le stringhe di lunghezza dispari.

# 18. Creare una lista di tuple in cui ogni tupla contiene due stringhe.
#     Stampare le tuple in cui entrambe le stringhe iniziano con la lettera 'a'.
#     Poi stampare quelle in cui almeno una stringa inizia con 'a'.

# 19. Creare una lista di tuple in cui ogni tupla contiene due numeri interi.
#     Stampare le tuple in cui la somma dei due numeri è pari.
#     Stampare poi le tuple ordinate in base alla somma dei loro elementi (crescente).

# 20. Creare una lista di tuple (nome, voto) con almeno 5 studenti.
#     Stampare il nome dello studente con il voto più alto e quello con il più basso.
#     Stampare poi la media dei voti.


# --- SEZIONE 6: Esercizi avanzati ---

# 21. Data una tupla di tuple di numeri, calcolare la somma di ogni tupla interna
#     e creare una nuova tupla contenente tutte queste somme.

# 22. Scrivere un programma che, data una tupla di numeri,
#     restituisca una nuova tupla con gli stessi elementi ma senza ripetizioni e ordinata.

# 23. Date due tuple della stessa lunghezza, creare una lista di tuple
#     abbinando gli elementi in posizione corrispondente (come zip).
#     Implementarlo senza usare zip().

# 24. Data una frase come stringa, creare una tupla con tutte le parole uniche
#     che appaiono più di una volta, in ordine alfabetico.