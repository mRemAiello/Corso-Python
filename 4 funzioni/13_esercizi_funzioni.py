# Esercizi

# Si scriva una funzione, che prenda in input 2 parametri (x e y) e restituisca la somma x + y.

def somma(x, y):
    return x + y


x = 10
y = 20
print(somma(x, y))


# Sviluppare una calcolatrice, creando le funzioni Add, Subtract, Multiply, Divide e Modulo che prendono in input 2 valori (x e y)
# e restituiscono rispettivamente la somma, la sottrazione, la moltiplicazione e la divisione tra x e y.


def divide(x=0, y=0):
    if y == 0:
        return 0
    return x / y


x = 20
y = 15
print(divide(x, y))


# Scrivi una funzione che prende una lista di numeri e restituisce la somma di tutti gli elementi.

def somma(x=[]):
    s = 0
    for element in x:
        s = s + element
    return s


x = [1, 2, 3, 4]
print(somma(x))


# Scrivere una funzione che, preso in ingresso una lista, esegua una somma alterna.
# Per somma alterna si intende la somma di tutti i numeri pari della lista, e la sottrazione di tutti i numeri dispari dell’array.

def somma_alterna(lista=[]):
    s = 0
    for element in lista:
        if element % 2 == 0:
            s = s + element
        else:
            s = s - element
    return s


x = [1, 2, 3, 4]
print(somma_alterna(x))


# Scrivere due funzioni che, presa una lista, vadano a contare rispettivamente, la totalità dei numeri pari e dispari.

def conta_pari_dispari(lista=[]):
    num_pari_dispari = {"pari": 0, "dispari": 0, "totale": 0}
    for element in lista:
        if element % 2 == 0:
            num_pari_dispari["pari"] += 1
            num_pari_dispari["totale"] += 1
        else:
            num_pari_dispari["dispari"] += 1
            num_pari_dispari["totale"] += 1
    return num_pari_dispari


x = [1, 2, 3, 4]
dic = conta_pari_dispari(x)
print(dic)



# Si Scriva una funzione, chiamata find_min, che ricerchi il minimo in una lista di valori interi. Fare lo stesso col massimo.
# Usare while e for.


def find_min(lista=[]):
    min = lista[0]
    for element in lista:
        if element < min:
            min = element
    return min


def find_max(lista=[]):
    max = lista[0]
    for element in lista:
        if element > max:
            max = element
    return max


def find_min_max(lista=[]):
    min = find_min(lista)
    max = find_max(lista)
    return {"minimo": min, "massimo": max}


x = [2, 3, 4, 1, 0]
print("Minimo:", find_min(x))
print("Massimo:", find_max(x))
print("Entrambi:", find_min_max(x))



# Creare anche due funzioni che restituiscano la posizione del minimo / massimo.


# Scrivere una funzione per il calcolo della media, che prenda in input una lista e restituisca la media dei numeri.

def media(lista=[]):
    m = 0
    for element in lista:
        m = m + element
    return m / len(lista)


x = [2, 3, 5, 1, 0]
print(media(x))


# Calcolare, sempre usando una funzione, la media dei numeri pari, dispari ed entrambi.
# Restituire un dict.


def media_pari(lista=[]):
    m = 0
    n_pari = 0
    for element in lista:
        if element % 2 == 0:
            m = m + element
            n_pari += 1
    return m / n_pari


def media_dispari(lista=[]):
    m = 0
    n_dispari = 0
    for element in lista:
        if not element % 2 == 0:
            m = m + element
            n_dispari += 1
    return m / n_dispari


def media_totale(lista=[]):
    dic = {}
    dic["media"] = int(media(lista))
    dic["media_pari"] = int(media_pari(lista))
    dic["media_dispari"] = int(media_dispari(lista))
    return dic


x = [2, 3, 5, 1, 0]
print(media_totale(x))


# Sviluppare una funzione che restituisca una tupla, con all'interno di una lista i positivi, negativi o nulli.
# Ordinarli numericamente.