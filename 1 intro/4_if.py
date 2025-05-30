import random

# IF
massimo = 15
panini = int(random.uniform(-1, massimo))
print("Panini:", panini)

# panini > 10, panini < 10, panini >= 10, panini <= 10, panini == 10

if panini > 10:
    print("Mangia il pane")

elif panini == 0:
    print("Compra il pane")

elif panini < 5:
    print("Mangia poco pane")

else:
    print("Mangia un pò di pane")


# AND
if panini < 10 and panini > 3:
    print("Non c'è abbastanza pane")


# Oppure
if panini > 10 or panini == 3:
    print("C'è abbastanza pane")


# Combinazione con parentesi
# Panini == 1 => print("Prova")
# Panini 11, 12 => print("Prova)
if (panini > 10 and panini < 13) or panini == 1:
    print("Prova")

# Se tolgo la parentesi:
# if panini > 10 and panini < 13 or panini == 1:
#

# Not
# Qua vanno bene tutti i panini <= 10
if not panini > 10:
    print("C'è abbastanza pane")



# Esercizi

# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è positivo" se il numero è maggiore di zero,
# altrimenti stampa "Il numero è negativo".
# Eseguire l'esercizio anche generando un numero random. Trasformare il numero random in int.


# Scrivere un programma che chiede all'utente di inserire due numeri e stampa "Il primo numero è maggiore"
# se il primo numero è maggiore del secondo,
# "Il secondo numero è maggiore" se il secondo numero è maggiore del primo, altrimenti stampa "I numeri sono uguali".


# Scrivere un programma che chiede all'utente di inserire un numero e stampa "Il numero è pari" se il numero è pari,
# altrimenti stampa "Il numero è dispari".


# Scrivere un programma che chiede all'utente di inserire una stringa e stampa "La stringa è vuota" se la stringa è vuota,
# altrimenti stampa "La stringa non è vuota".


# Scrivere un programma che chiede all'utente di inserire una lettera e stampa "La lettera è una vocale"
# se la lettera è una vocale (a, e, i, o, u), altrimenti stampa "La lettera non è una vocale".
# Poi inserire un controllo sul numero di lettere scritte dall'utente (deve essere una)


# Scrivere un programma che prenda in input un numero intero random.
# Stampare il valore assoluto di quel numero (il valore assoluto di un numero è il valore senza il segno, es. |-5| = 5 oppure |5| = 5).
# Per ottenere il valore positivo da un numero negativo scrivere (-numero).


# Scrivere un programma che prenda in input una variabile float che rappresenti un Celsius, da convertire in Fahrenheit ed in Kelvin.
# Se una delle due temperature (Fahr -459.67, Celsius -273.15, Kelvin -273.15) visualizzarlo a schermo in qualche modo.
# Fahrenheit = (9/5 * Celsius) + 32
# Kelvin = Celsius + 273,15


# Dato un numero intero tra 1 e 12, che rappresenta il mese corrente (farlo scegliere all'utente),
# stampare il nome del mese per esteso (“Gennaio” ... “Dicembre”).


# Un anno bisestile e’ identificato da un intero maggiore di 1584 che sia divisibile per 4 ma non per 100, oppure che sia divisibile per 400.
# Prendere in input una variabile intera che rappresenti l’anno e mediante print visualizzare BISESTILE
# se l’anno inserito è bisestile, e NON BISESTILE altrimenti.


# Dato numero un intero preso in input, mediante print visualizzare una stringa ottenuta dalla concatenazione di 3 vocali,
# ognuna estratta mediante il seguente procedimento: 'a' = 1, 'e' = 2, 'i' = 3...


# Controlla la password sottostante e se risulta con più di 11 caratteri allora stampa a video 'Password ok' altrimenti 'Password troppo corta'.
# password = 'alfabravocharly'


# Verifica se il valore assegnato alla variabile sottostante è un intero, se lo è stampa la stringa 'Si' altrimenti 'No'.
# num = 33.0

# isdigit controlla che sia un numero, in questo primo caso NON lo è
string = '123ayu456'
print(string.isdigit())

# In questo caso, invece, è un numero
string = '123456'
print(string.isdigit())


# Calcolo del Punteggio degli Esami:
# Scrivi un programma che legge il punteggio di tre esami (numero intero) da parte dell'utente.
# Il programma deve calcolare la media dei punteggi e determinare la lettera di voto
# finale basata sulla media.

# Usa le seguenti regole:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Inoltre, se un esame ha un punteggio inferiore a 50, il voto finale deve essere
# F indipendentemente dalla media.