# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e verifica se l'anno è bisestile o meno.
# Un anno bisestile e’ identificato da un intero maggiore di 1584 che sia divisibile per 4 ma non per 100,
# oppure che sia divisibile per 400.
# Prendere in input una variabile intera che rappresenti l’anno e mediante print visualizzare
# BISESTILE se l’anno inserito è bisestile, e NON BISESTILE altrimenti.

import datetime as dt

year = int(input("Scrivi un anno "))
data = dt.datetime(day=1, month=1, year=year)

if data.year > 1585:

    if data.year % 4 == 0 and not data.year % 100 == 0:
        print("L'anno è bisestile.")
    elif data.year % 400 == 0:
        print("L'anno è bisestile.")
    else:
        print("L'anno non è bisestile.")

else:
    print("L'anno non è bisestile.")