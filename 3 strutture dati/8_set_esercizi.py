# Creare un set vuoto e assegnarlo a una variabile.
# Creare un set contenente i seguenti elementi: "mela", "banana", "kiwi", "mela".
# Aggiungere l'elemento "pesca" al set precedente.
# Rimuovere l'elemento "pera" dal set precedente.


# Verificare se l'elemento "ananas" è presente nel set precedente. Se è presente lo rimuovi,
# altrimenti fai un print di avviso.


# Creare un set contenente i numeri interi da 1 a 5.
# Creare un nuovo set contenente i numeri pari del set precedente.
# Fare lo stesso con i dispari.
# Utilizzare for (unica scelta possibile).


# Crea due set, A e B, contenenti alcuni numeri interi.
# Trova l'intersezione tra A e B.
# Trova l'unione tra A e B.
# Trova la differenza tra A e B.
# Verifica se un certo elemento è presente in uno dei due set.


# Realizza un gioco di carte giocabile da soli da terminale.
# Il giocatore pesca carte da un mazzo e prova a formare coppie secondo una regola.
# Il mazzo deve essere mantenuto con un set, così da garantire che ogni carta esista una sola volta.

# Regole del gioco
# Il mazzo è composto da 52 carte: semi ♠ ♥ ♦ ♣ e valori A,2,3,4,5,6,7,8,9,10,J,Q,K.
# Il giocatore parte con 0 punti.
#
# A ogni turno:
# Il giocatore pesca 2 carte dal mazzo.
# Se le due carte hanno lo stesso valore (es. 7♥ e 7♣), guadagna +2 punti.
# Se hanno lo stesso seme (es. K♦ e 3♦), guadagna +1 punto.
# Altrimenti 0 punti.
#
# Il gioco termina quando:
# il mazzo ha meno di 2 carte, oppure
# il giocatore digita q per uscire.

# Vincoli obbligatori

# Il mazzo deve essere un set di carte univoche.
# Ogni carta deve essere rappresentata come tupla: (valore, seme).
# Esempio: ("A", "♠")
# La pesca deve rimuovere la carta dal set.
#
# Vietato usare liste per memorizzare tutto il mazzo
# (puoi usare una lista temporanea per stampare o scegliere casualmente, ma il mazzo “ufficiale” resta un set).