import datetime as dt
from datetime import timedelta

# Data Corrente
data_corrente = dt.datetime.now()
print(data_corrente)

# Data stabilita dal programmatore
# datetime(year, month, day, hour..)
# datetime(2025, 9, 11, 20, 30)
data_personalizzata = dt.datetime(day=11, month=9, year=2025, hour=20, minute=30)
print(data_personalizzata)

# Operazioni con le date
delta = timedelta(days=10, minutes=1, weeks=1)

# data + timedelta => data
print(data_corrente + delta)
print(data_corrente - delta)

# data_1 - data_2 => timedelta
print(data_personalizzata - data_corrente)

# data_1 == data_2 => True/False
# Puoi anche fare data_1 >=, >, <, <= data_2
print(data_corrente == data_personalizzata)

data_di_uscita = data_personalizzata - data_corrente
print(data_di_uscita.days, "giorni al mio compleanno.")

# Formatta la stringa per renderla leggibile
# https://www.w3schools.com/python/python_datetime.asp
print(data_corrente.strftime("Data Corrente: %d-%m-%Y %H:%M"))
print(data_personalizzata.strftime("Data Personalizzata: %d-%m-%Y %I:%M %p"))
print(data_personalizzata.strftime("Data Locale: %c"))