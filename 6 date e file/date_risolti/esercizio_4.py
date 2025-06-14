# Scrivi un programma che prende in input una data e un numero di giorni, e calcola la data che viene
# dopo quella data del numero di giorni specificato.

import datetime as dt
from datetime import timedelta

day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))
day_difference = int(input("Scrivi un numero di giorni "))

data = dt.datetime(day=day, month=month, year=year)

print(data + timedelta(days=day_difference))