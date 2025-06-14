# Scrivi un programma che prende in input due date e calcola la differenza in giorni tra le due.

import datetime as dt

day = int(input("Scrivi un giorno "))
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