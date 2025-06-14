# Scrivi una funzione che prenda in input una data come oggetto datetime e
# restituisca il numero della settimana corrispondente nell'anno.

import datetime as dt

date_1 = dt.datetime(day=22, month=9, year=2024)
date_2 = dt.datetime(day=1, month=1, year=date_1.year)
delta = date_2 - date_1
days = int(delta.days)
if days < 0:
    days = -days
days = int(((days / 7) + 1))
print(days)