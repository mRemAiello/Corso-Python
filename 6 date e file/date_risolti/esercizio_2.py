# Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e stampa il nome del mese corrispondente.

import datetime as dt

day = int(input("Scrivi un giorno "))
month = int(input("Scrivi un mese "))
year = int(input("Scrivi un anno "))

data = dt.datetime(day=day, month=month, year=year)
print(data)
print(data.strftime("Mese: %B"))