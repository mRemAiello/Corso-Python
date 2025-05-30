def calcola_media(lista):
    if int == type(lista):
        return "Devi darmi una lista"
    if len(lista) == 0:
        return "La lista è vuota"
    media = 0
    for numero in lista:
        media = media + numero
    media = media / len(lista)
    return media


# Media
pippo = [1, 2, 3]
risultato = calcola_media(pippo)
print(risultato)


numeri = [5, 6, 7]
risultato = calcola_media(numeri)
print(risultato)


numeri = {6, 1, 2, 4}
risultato = calcola_media(numeri)
print(risultato)