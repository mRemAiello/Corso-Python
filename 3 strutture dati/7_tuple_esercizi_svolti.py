# Creare una lista di tuple, in cui ogni tupla contiene due stringhe.
# Stampare solo le tuple che hanno entrambe le stringhe di lunghezza pari.
# Fare lo stesso con quelle di lunghezza dispari.

x = [("Ciao", "Ciao2"), ("Auto", "Casa"), ("Macchina", "Calcio")]
for element in x:
    first = element[0]
    second = element[1]
    if len(first) % 2 == 0 and len(second) % 2 == 0:
        print(element)

# Creare una lista di tuple, in cui ogni tupla contiene due numeri interi.
# Stampare le tuple in cui la somma dei due numeri è pari.

x = [(2, 2), (3, 2)]
for element in x:
    first = element[0]
    second = element[1]
    if (first + second) % 2 == 0:
        print(element)