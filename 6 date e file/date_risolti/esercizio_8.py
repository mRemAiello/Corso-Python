# Scrivi una funzione che prenda in input due date come oggetti datetime e
# restituisca il numero di giorni trascorsi tra di esse.

import datetime as dt


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