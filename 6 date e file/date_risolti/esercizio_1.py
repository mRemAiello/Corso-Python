# Scrivi un programma che stampa la data e l'ora corrente.

import datetime as dt
from datetime import timedelta


def convert_date_to_string(value):
    if value <= 9:
        return "0" + str(value)
    return str(value)


# Metodo con format
stringa = "{}/{}/{} {}:{}"

data_corrente = dt.datetime.now()
day = convert_date_to_string(data_corrente.day)
month = convert_date_to_string(data_corrente.month)
minutes = convert_date_to_string(data_corrente.minute)
hour = convert_date_to_string(data_corrente.hour)
stringa = stringa.format(day, month, data_corrente.year, hour, minutes)

print(stringa)


# Metodo 2: strftime
print(data_corrente.strftime("%d/%m/%Y %H:%M"))