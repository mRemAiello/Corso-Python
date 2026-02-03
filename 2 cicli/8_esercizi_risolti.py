# Scrivere un programma che utilizzi un loop for (e while) per stampare ogni elemento di una lista.
# Scrivere un programma che utilizzi un loop while per stampare tutti i numeri da 1 a 10.
# Stampare i numeri da 10 a 1 usando un loop while.
# Stampare i numeri pari da 2 a 10 (e da 10 a 2) usando un loop while.

"""lista = [1, 2, 3, 4, 5]
for elemento in lista:
    print(elemento)

i = 0
while i < len(lista):
    print(lista[i])
    i = i + 1
    # Alternativamente: i += 1 => qua viene fatto i + 1, il risultato viene salvato dentro i

i = 1
while i <= 10:
    print("Numero:", i)
    i = i + 1"""

"""i = 10
while i >= 1:
    print("Numero:", i)
    i = i - 1"""

"""i = 1
while i <= 10:
    if i % 2 == 0:
        print("Numero pari:", i)
    i = i + 1

i = 10
while i >= 2:
    if i % 2 == 0:
        print("Numero pari:", i)
    i = i - 1"""


# Leggere un numero in input (N) e utilizzare un ciclo while per stampare i primi N (partendo da 0) numeri pari e dispari.

"""N = int(input("Scrivi un numero: "))
i = 0
while i <= N:
    if i % 2 == 0:
        print("Numero pari:", i)
    else:
        print("Numero dispari:", i)
    i = i + 1"""


# Leggere due numeri in input (N e M) e utilizzarli per stampare tutti i numeri compresi tra N e M
# utilizzando un ciclo while. Distinguere pari e dispari.

"""N = int(input("Scrivi un numero: "))
M = int(input("Scrivi un altro numero: "))
if N < M:
    i = N
    while i <= M:
        if i % 2 == 0:
            print("Numero pari:", i)
        else:
            print("Numero dispari:", i)
        i = i + 1
else:
    print("Errore! La N inserita è maggiore di M")"""


# Leggere due numeri in input (N e M) e utilizzarli per sommare tutti i numeri compresi tra N e M
# utilizzando un ciclo while.

"""N = int(input("Scrivi un numero: "))
M = int(input("Scrivi un altro numero: "))
if N < M:
    i = N
    somma = 0
    while i <= M:
        somma = somma + i
        i = i + 1
    print("La somma finale è", somma)
else:
    print("Errore! La N inserita è maggiore di M")"""

# Leggere due numeri in input (N e M) e fare la somma alterna, cioè somma i pari e sottrai i dispari.
# Farlo anche con una lista, usando il for e il while.

"""N = int(input("Scrivi un numero: "))
M = int(input("Scrivi un altro numero: "))
if N < M:
    i = N
    somma = 0
    while i <= M:
        if i % 2 == 0:
            somma = somma + i
        else:
            somma = somma - i
        i = i + 1
    print("La somma finale è", somma)
else:
    print("Errore! La N inserita è maggiore di M")"""

"""lista = [2, 5, 6, 8, 9, 10, 1, 5, 0, 2, 4]
somma = 0
for elemento in lista:
    if elemento % 2 == 0:
        somma += elemento
    else:
        somma -= elemento
print("La somma finale è", somma)

somma = 0
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        somma += lista[i]
    else:
        somma -= lista[i]
    i += 1
print("La somma finale è", somma)"""



# Scrivere un programma che utilizzi un loop for (e while) per sommare tutti i numeri in una lista.
# Adesso fare lo stesso, ma imporre che la somma non superi 20.

"""lista = [2, 5, 6, 8, 9, 10, 1, 5, 0, 2, 4, 10]
somma = 0
for elemento in lista:
    if somma + elemento <= 20:
        somma += elemento
print("La somma finale è", somma)

i = 0
somma = 0
while i < len(lista):
    if somma + lista[i] <= 20:
        somma += lista[i]
    i += 1
print("La somma finale è", somma)"""


# Scrivere un programma che utilizzi un for (e while) per calcolare la media di una lista di numeri (int e float).
# Successivamente impostare un ciclo while e chiedere man mano all'utente i numeri da utilizzare nella lista.

"""lista = [2, 5.345, 6, 12.52, 20.47, 30.554, 2, 4.24, 10]
media = 0
for elemento in lista:
    media += elemento
media /= len(lista)
print("La media finale è", media)

i = 0
media = 0
while i < len(lista):
    media += lista[i]
    i += 1
media /= len(lista)
print("La media finale è", media)"""

"""lista = [2, 5.345, 6, 12.52, 20.47, 30.554, 2, 4.24, 10]
comando = input("Vuoi inserire numeri nella lista? ")
while comando == "si":
    numero = float(input("Inserisci un numero: "))
    lista.append(numero)

    comando = input("Vuoi inserire numeri nella lista? ")

media = 0
for elemento in lista:
    media += elemento
media /= len(lista)
print("La media finale è", media)"""


# Calcolare il fattoriale di un numero intero positivo n usando un loop while.
# Poi calcola il fattoriale di ogni elemento della lista, con for e while.

# Fattoriale di n con n = 5 => 5 * 4 * 3 * 2 * 1 => 120

"""N = input("Inserisci un numero intero positivo: ")
N = int(float(N))
if N >= 0:
    fattoriale = 1
    i = 1
    while i <= N:
        fattoriale = fattoriale * i
        i = i + 1
    print("Il fattoriale di", N, "è", fattoriale)
else:
    print("Errore! Devi inserire un numero intero positivo")"""

"""lista = [1, 2, -3, 3, 4, 5, -1, 0, 6, 7, 8, -4, 9, 10]
# Qua quello che succede è:
# Passaggio 1 del for, con N = 1, si fa tutto il contenuto del while
# Passaggio 2 del for, con N = 2, si fa tutto il contenuto del while
for N in lista:
    if N >= 0:
        fattoriale = 1
        i = 1
        while i <= N:
            fattoriale = fattoriale * i
            i = i + 1
        print("Il fattoriale di", N, "è", fattoriale)
    else:
        print("Errore! Nella lista è presente un numero non intero positivo:", N)

i = 0
while i < len(lista):
    if lista[i] >= 0:
        fattoriale = 1
        j = 1
        while j <= lista[i]:
            fattoriale = fattoriale * j
            j = j + 1
        print("Il fattoriale di", lista[i], "è", fattoriale)
    else:
        print("Errore! Nella lista è presente un numero non intero positivo:", N)
    i = i + 1"""


# Calcola i quadrati di una serie di numeri dentro una lista con for e while.

"""lista = [1, 4, 5, 6, 7, 2, 2, 43, 6, 7, 89]
for elemento in lista:
    quadrato = elemento * elemento
    print("Il quadrato di", elemento, "è", quadrato)

i = 0
while i < len(lista):
    quadrato = lista[i] * lista[i]
    print("Il quadrato di", lista[i], "è", quadrato)
    i = i + 1"""


# Calcolare la potenza di un numero intero. I valori base ed esponente sono a scelta dello studente.
# Ricordiamo che un numero a elevato a n è il prodotto di a eseguito n volte.
# Poi fare il calcolo usando una lista di numeri come base e come esponente.

# Esempio: a^n => 2^3 => 2 * 2 * 2
bas = 2
exp = 3
i = 1
risultato = 1
while i <= exp:
    risultato = risultato * bas
    i = i + 1

print("La potenza tra", bas, "e", exp, "è", risultato)

#
lista_bas = [1, 2, 3, 4, 5, 6]
lista_exp = [2, 3, 3, 6, 4]

if len(lista_bas) == len(lista_exp):
    i = 0
    while i < len(lista_bas):
        bas = lista_bas[i]
        exp = lista_exp[i]
        j = 1
        risultato = 1
        while j <= exp:
            risultato = risultato * bas
            j = j + 1

        print("La potenza tra", bas, "e", exp, "è", risultato)

        i = i + 1
else:
    print("La lunghezza delle lista delle basi e degli esponenti deve coincidere")


# Esegui una somma cumulativa dei numeri inseriti dall'utente fino a quando viene inserito il numero
# 0 utilizzando un ciclo while.


# Chiedere all'utente di indovinare un numero intero casuale compreso tra 1 e 10.
# Continuare a chiedere all'utente di indovinare finché non indovina il numero corretto. Usare un loop while.


# Inserire due numeri interi da tastiera: n, val. Il programma a questo punto deve chiedere all’utente di inserire n
# valori interi e verificare quanti di questi sono maggiori, minori o uguali a val.
# E se volessi farlo con una lista?


# Scrivere un programma che stampi a video tutti i numeri compresi tra due estremi a e b letti da tastiera.
# Il programma deve dire anche quanti sono i pari, i dispari e quanti i numeri totali.


# Calcolare la somma dei cubi dei primi k numeri pari.
# Farlo anche per i dispari. Dare anche la somma totale.


# Scrivere un programma che lette da tastiera le temperature
# T di un mese (il numero di giorni del mese è letto da tastiera) determini la temperatura media,
# la temperatura minima e la temperatura massima. Farlo sia con while che con for.


# Generare un numero a caso compreso tra 1-100 e chiedere all’utente un numero fino a quando non
# è uguale a quello generato casualmente. Dire ogni volta se il numero immesso è > o < di quello
# iniziale. Indicare anche il numero di tentativi.