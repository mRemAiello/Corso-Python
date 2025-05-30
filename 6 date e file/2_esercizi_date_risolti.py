import datetime as dt
from datetime import timedelta

# Scrivi un programma che stampa la data e l'ora corrente.

"""def convert_date_to_string(value):
    if value <= 9:
        return "0" + str(value)
    return str(value)


data_corrente = dt.datetime.now()

# Metodo 1: format
stringa = "{}/{}/{} {}:{}"
day = convert_date_to_string(data_corrente.day)
month = convert_date_to_string(data_corrente.month)
minutes = convert_date_to_string(data_corrente.minute)
hour = convert_date_to_string(data_corrente.hour)
stringa = stringa.format(day, month, data_corrente.year, hour, minutes)

print(stringa)"""

# Metodo 2: strftime
# print(data_corrente.strftime("%d/%m/%Y %H:%M"))


# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e stampa il nome del mese corrispondente.

"""day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data = dt.datetime(day=day, month=month, year=year)
print(data.strftime("Mese: %B"))"""


# Scrivi un programma che prende in input due date e calcola la differenza in giorni tra le due.

"""day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data = dt.datetime(day=day, month=month, year=year)

day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data_2 = dt.datetime(day=day, month=month, year=year)

delta = data - data_2
if delta.days > 0:
    print(delta.days, "giorni di differenza")
else:
    print(-delta.days, "giorni di differenza")
    
    
    """



# Scrivi un programma che prende in input una data e un numero di giorni, e calcola la data che viene
# dopo quella data del numero di giorni specificato.

"""day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))
data = dt.datetime(day=day, month=month, year=year)

print(data + timedelta(days=1))"""





# Scrivi un programma che stampa tutti i giorni di un determinato mese e anno.

"""month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data = dt.datetime(day=1, month=month, year=year)
print(data.strftime("%d/%m/%Y"))
i = 1
while i < 31:
    data_interna = data + timedelta(days=i)
    if data_interna.month == data.month:
        print(data_interna.strftime("%d/%m/%Y"))
    i = i + 1"""


# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e verifica se l'anno è bisestile o meno.
# Un anno bisestile e’ identificato da un intero maggiore di 1584 che sia divisibile per 4 ma non per 100,
# oppure che sia divisibile per 400.
# Prendere in input una variabile intera che rappresenti l’anno e mediante print visualizzare
# BISESTILE se l’anno inserito è bisestile, e NON BISESTILE altrimenti.

"""year = int(input("Scrivi un anno "))
data = dt.datetime(day=1, month=1, year=year)

if data.year > 1585:
    
    if data.year % 4 == 0 and not data.year % 100 == 0:
        print("L'anno è bisestile.")
    elif data.year % 400 == 0:
        print("L'anno è bisestile.")
    else:
        print("L'anno non è bisestile.")

else:
    print("L'anno non è bisestile.")"""


# Scrivi un programma che prende in input due date e stampa tutte le date comprese tra le due (inclusi i bordi).

"""day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data = dt.datetime(day=day, month=month, year=year)

day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data_2 = dt.datetime(day=day, month=month, year=year)

while not data == data_2:

    print(data.strftime("%d/%m/%Y %H:%M"))
    data = data + timedelta(days=1)

print(data_2.strftime("%d/%m/%Y %H:%M"))"""


# Scrivi una funzione che prenda in input due date come oggetti datetime e restituisca il numero di giorni trascorsi tra di esse.

def days_between_dates(date_1, date_2):
    delta = date_1 - date_2
    if delta.days < 0:
        return -delta.days
    return delta.days


def days_between_dates_abs(date_1, date_2):
    return abs((date_1 - date_2).days)


date_1 = dt.datetime(day=22, month=10, year=2024)
date_2 = dt.datetime(day=22, month=7, year=2024)

print(days_between_dates(date_1, date_2), "giorni")
print(days_between_dates_abs(date_1, date_2), "giorni")


file = open("giorni.csv", "w", encoding="utf-8")
file.write(str(days_between_dates(date_1, date_2)) + " giorni;")
file.write(str(days_between_dates_abs(date_1, date_2)) + " giorni;")
file.close()


# Scrivi una funzione che prenda in input una data come oggetto datetime e restituisca il giorno della settimana corrispondente come stringa.

"""date_1 = dt.datetime(day=22, month=7, year=2024)
print(date_1.strftime("%A"))"""




# Scrivi una funzione che prenda in input una data come oggetto datetime e
# restituisca il numero della settimana corrispondente nell'anno.

date_1 = dt.datetime(day=22, month=7, year=2024)
date_2 = dt.datetime(day=1, month=1, year=date_1.year)
delta = date_2 - date_1
days = int(delta.days)
if days < 0:
    days = -days
days = int(((days / 7) + 1))
print(days)


# CLASSI

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
# Ai prodotti Alimentari viene infatti associata una data di scadenza, mentre a quelli Non Alimentari il materiale principale di cui sono fatti, e
# se tale materiale è ricicabile o meno.
# Realizzare le sottoclassi Alimentari e NonAlimentari estendendo opportunamente la classe Prodotto.
# Modificare le due sottoclassi dell'esercizio 2 specializzando il metodo applicaSconto in modo che nel caso dei prodotti
# Alimentari venga applicato uno sconto del 20% se la data di scadenza è a meno di 10 giorni dalla data attuale,
# mentre nel caso dei prodotti Non Alimentari venga applicato uno sconto del 10% se il prodotto è composto da un materiale riciclabile (carta, vetro o plastica).
# Realizzare una classe ListaSpesa che chieda all'utente di inserire i prodotti acquistati e
# calcoli il totale della spesa applicando gli opportuni sconti se il cliente ha la tessera fedeltà.