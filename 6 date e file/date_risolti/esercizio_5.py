# Scrivi un programma che stampa tutti i giorni di un determinato mese e anno.

import datetime as dt
from datetime import timedelta

month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data = dt.datetime(day=1, month=month, year=year)
print(data.strftime("%d/%m/%Y"))
i = 1
while i < 31:
    data_interna = data + timedelta(days=i)
    if data_interna.month == data.month:
        print(data_interna.strftime("%d/%m/%Y"))
    i = i + 1