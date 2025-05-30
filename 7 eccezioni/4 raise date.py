import datetime

try:

    anno = int(input("Seleziona un anno: "))
    data = datetime.datetime(day=11, year=anno, month=10)

except ValueError:

    data = datetime.datetime.now()

#
print(data)