# Creare un programma che, dati due interi che rappresentano rispettivamento il
# tasso di propagazione di un virus (quante nuove persone ogni giorno si ammalano
# per ogni persona già ammalata) e
# la quantità di persone di una popolazione, dica quanti giorni sono necessari
# perché sia ammalata almeno la metà della popolazione considerando che all’inizio ci sia una sola persona ammalata.

tasso_propagazione = 6
popolazione = 1000000
malati = 1
giorni = 0

print("-- MALATI --")
while malati <= popolazione / 2:

    malati = malati + (malati * tasso_propagazione)
    giorni = giorni + 1

    print("Giorno", giorni, "ci sono", malati, "malati")



# Dato un numero intero che rappresenta un numero di ammalati e un numero intero che rappresenta la
# percentuale di ammalati che ogni giorno guarisce, calcolare quanti giorni
# sono necessari affinché il numero di ammalati sia minore di 100.

percentuale_guarigioni = 35
giorni = 0

print()
print("-- GUARITI --")
while malati >= 100:

    guariti = int(malati * percentuale_guarigioni / 100)
    malati = malati - guariti
    giorni = giorni + 1

    print("Giorno", giorni, "sono guariti", guariti, "e ci sono", malati, "malati")