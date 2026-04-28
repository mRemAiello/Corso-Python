# Far inserire una serie numerica di interi fermandosi quando o la somma di due numeri consecutivi è pari
# a 10 o quando un numero è uguale al precedente del precedente nella serie numerica

"""ter_numero = int(input("Scrivi un numero: "))
penultimo_numero = int(input("Scrivi un numero: "))
ultimo_numero = int(input("Scrivi un numero: "))

while not penultimo_numero + ultimo_numero == 10 and not ultimo_numero == ter_numero:
    numero = int(input("Scrivi un numero: "))

    ter_numero = penultimo_numero
    penultimo_numero = ultimo_numero
    ultimo_numero = numero"""


# Variante con lista
lista = [0, 0, 0]
lista[-3] = int(input("Scrivi un numero: "))
lista[-2] = int(input("Scrivi un numero: "))
lista[-1] = int(input("Scrivi un numero: "))

while not lista[-2] + lista[-1] == 10 and not lista[-1] == lista[-3]:
    numero = int(input("Scrivi un numero: "))

    lista[-3] = lista[-2]
    lista[-2] = lista[-1]
    lista[-1] = numero