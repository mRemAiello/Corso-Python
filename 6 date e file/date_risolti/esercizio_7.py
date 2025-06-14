# Scrivi un programma che prende in input due date e stampa tutte le date comprese tra le due (inclusi i bordi).

import datetime as dt
from datetime import timedelta

day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data = dt.datetime(day=day, month=month, year=year)

day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data_2 = dt.datetime(day=day, month=month, year=year)

while not data == data_2:

    print(data.strftime("%d/%m/%Y"))
    data = data + timedelta(days=1)

print(data_2.strftime("%d/%m/%Y"))