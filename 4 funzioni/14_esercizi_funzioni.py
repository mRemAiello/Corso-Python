# Scrivere una funzione che riceva in ingresso un certo numero di giorni, ore, minuti e secondi (4 parametri della funzione),
# e che restituisca il numero di secondi totali.
# Si prega di osservare che un giorno ha 86400 secondi, un’ora ha 3600 secondi e un minuto ha 60 secondi.
# Chiedere i valori all'utente con la funzione input.

def calcola_sec(d, h, m, s):
    return (d*86400) + (h*3600) + (m*60) + s


# day = int(input("Dimmi i giorni: "))
day = 3
hour = 10
minutes = 20
seconds = 10
secondi_calcolati = calcola_sec(day, hour, minutes, seconds)


# Scrivere tre funzioni che, preso in ingresso un numero di secondi, restituiscano il numero di giorni, ore e minuti
# (rappresentati come float dentro un dict).

def get_days(seconds):
    return int(seconds / 86400)

def get_hours(seconds):
    return int(seconds / 3600)

def get_minutes(seconds):
    return int(seconds / 60)

def get_dict(seconds):
    dic = {}
    dic["days"] = get_days(seconds)
    dic["hours"] = get_hours(seconds)
    dic["minutes"] = get_minutes(seconds)
    return dic


print(get_days(secondi_calcolati))
print(get_hours(secondi_calcolati))
print(get_minutes(secondi_calcolati))
print(get_dict(secondi_calcolati))


# Si scriva una funzione, denominata Find, che ricerchi la presenza di un elemento in una lista di interi.
# La funzione riceve in ingresso due parametri: una lista di
# interi v[] nel quale ricercare il valore e il valore intero x che deve essere ricercato.
# La funzione deve restituire un valore intero, ed in particolare:
# Se il valore x è presente nella lista, allora la funzione restituisce l’indice della posizione alla quale si trova tale valore;
# Se il valore x è presente più volte, si restituiscano tutti gli indici dentro una lista.
# Se il valore x non è presente nella lista, si restituisca -1.


def find(lista, x):
    index = []
    i = 0
    while i < len(lista):
        if lista[i] == x:
            index.append(i)
        i = i + 1
    if len(index) == 0:
        return -1
    elif len(index) == 1:
        return index[0]
    return index


lista = [1, 2, 3, 4, 5, 1]
x1 = 1
x2 = 9
x3 = 2
print(find(lista, x1))
print(find(lista, x2))
print(find(lista, x3))




# Scrivi una funzione che prende una stringa e restituisce la stringa invertita.


def inversa_neg(stringa):
    inv = ""
    i = -1
    while i >= -len(stringa):
        inv += stringa[i]
        i -= 1
    return inv

def inversa(stringa):
    inv = ""
    i = len(stringa) - 1
    while i >= 0:
        inv += stringa[i]
        i -= 1
    return inv


stringa = "ciao"
print(inversa(stringa))
print(inversa_neg(stringa))


# Scrivi una funzione che prende una lista di parole e restituisce una lista
# contenente solo le parole che iniziano con una lettera specificata.

def get_lista_lettera(lista, lettera):
    lista_2 = []
    for element in lista:
        if element[0] == lettera:
            lista_2.append(element)
    return lista_2


lista = ["ciao", "ciao2", "casa", "pallone"]
lettera = "c"
print(get_lista_lettera(lista, lettera))


# Scrivi una funzione che prende una lista di parole e restituisce una lista
# contenente la lunghezza di ciascuna parola.

def get_lunghezza_parole(lista):
    lista_2 = []
    for element in lista:
        lista_2.append(len(element))
    return lista_2


print(get_lunghezza_parole(lista))


# Scrivi una funzione che prende una lista di parole e
# restituisce la parola più lunga (e poi più corta).

def get_parola_piu_lunga(lista):
    parola = lista[0]
    for element in lista:
        if len(element) > len(parola):
            parola = element

    lista_2 = []
    for element in lista:
        if len(element) == len(parola):
            lista_2.append(element)

    return lista_2


def get_parola_piu_corta(lista):
    parola = lista[0]
    for element in lista:
        if len(element) < len(parola):
            parola = element

    lista_2 = []
    for element in lista:
        if len(element) == len(parola):
            lista_2.append(element)

    return lista_2


print(get_parola_piu_lunga(lista))
print(get_parola_piu_corta(lista))


# Scrivi una funzione che prende una lista di parole e
# restituisce quelle lunghe oltre un certo valore (e corte oltre un certo valore).

def get_parole_oltre_lunghezza(lista, lunghezza):
    lista_2 = []
    for element in lista:
        if len(element) >= lunghezza:
            lista_2.append(element)

    return lista_2


def get_parole_meno_lunghezza(lista, lunghezza):
    lista_2 = []
    for element in lista:
        if len(element) <= lunghezza:
            lista_2.append(element)

    return lista_2


print(get_parole_oltre_lunghezza(lista, 3))
print(get_parole_meno_lunghezza(lista, 4))


# Scrivi una funzione che verifichi se una frase è palindroma.

def is_palindroma(parola):
    inv = inversa(parola)
    if parola == inv:
        return True
    return False


"""parola = input("Scrivi una frase: ")
print(is_palindroma(parola))
if is_palindroma(parola):
    print("La parola", parola, "è palindroma")
else:
    print("non è palindroma")"""


# Scrivi una funzione che prende una lista di parole e restituisce una lista
# contenente solo le parole palindrome.

def cerca_palindromi(lista):
    lista_2 = []
    for element in lista:
        if is_palindroma(element):
            lista_2.append(element)
    return tuple(lista_2)


lista = ["anna", "boh", "casa", "cane"]
print(cerca_palindromi(lista))


# Creare una funzione stampa_pari_dispari() che prende un intero e stampa a schermo "pari" se il numero e’ pari e "dispari" altrimenti.
# Creare una funzione calcola_pari_dispari() che prende un intero e restituisce la stringa "pari" se il numero e’ pari e la stringa "dispari" altrimenti.


# Creare una funzione controlla_alfanumerico() che prende una stringa e restituisce True se la stringa e’
# alfanumerica (contiene solo caratteri alfabetici o numerici) e False altrimenti.
# Per controllare se un carattere e’ alfanumerico, usare in e la stringa:: "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789".

def controlla_alfanumerico(carattere):
    if carattere in "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
        return True
    return False


carattere = "C"
print(controlla_alfanumerico(carattere))



# Creare una funzione wc() che prende una stringa e restituisce una tripla (tuple) di tre valori:
# Il primo elemento della coppia deve essere la lunghezza della stringa.
# Il secondo elemento deve essere il numero di a capo nella stringa.
# Il terzo elemento deve essere il numero di parole (separate da spazi o a capo) nella stringa.

def wc(parola):
    tripla = [len(parola)]
    conta_a_capo = 0
    for element in parola:
        if element == "\n":
            conta_a_capo += 1
    tripla.append(conta_a_capo)

    conta_parole = parola.count("\n") + 1
    conta_parole += parola.count(" ")
    tripla.append(conta_parole)

    return tuple(tripla)


parola = "Ciao\nMi\nChiamo\nMirko Aiello"
print(wc(parola))


# Creare una funzione stampa_dizionario() che prende un dizionario e stampa a schermo le coppie chiave-valore del dizionario formattate come da esempio sotto:
# dizionario = { "arginina": 0.7}
# arginina -> 70%

def stampa_dizionario(dict):
    for key, item in dict.items():
        print(key, "->", str(int(item*100)) + "%")



dict = {
    "chiave_1": 0.75,
    "chiave_2": 0.8,
    "chiave_3": 0.5
}

stampa_dizionario(dict)



# Scrivere una funzione che calcoli il fattoriale di un numero.
# Il fattoriale di un numero n è il prodotto dei primi n numeri.


def fattoriale(numero):
    fact = 1
    i = 1
    while i <= numero:
        fact = fact * i
        i += 1

    return fact


def fattoriale_ricorsivo(numero):

    if numero == 1:
        return 1

    return numero * fattoriale_ricorsivo(numero - 1)


# print(fattoriale(12))
# print(fattoriale_ricorsivo(12))


# Creare una funzione crea_lista_di_fattoriali() che prende un intero n, e restituisce una
# lista contenente tutti i fattoriali (ex. n = 4, la lista contiene il fattoriale di 1, 2, 3, 4)

def crea_lista_di_fattoriali(numero):
    lista = []
    i = 1
    while i <= numero:
        lista.append(fattoriale(i))
        i += 1

    return lista


print(crea_lista_di_fattoriali(10))