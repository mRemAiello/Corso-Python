# Esempio 1: while senza lista
# Conto alla rovescia di un timer.
secondi = 5

while secondi > 0:
    print("Mancano", secondi, "secondi")
    secondi = secondi - 1

print("Tempo scaduto")


# Esempio 2: while con lista
eta_persone = [18, 20, 22, 30, 35, 20, 40, 40]

i = 0
media = 0
while i < len(eta_persone):
    media = media + eta_persone[i]
    print("eta", eta_persone[i])
    print("somma parziale", media)
    print("indice", i)
    print()
    i = i + 1

print("elementi letti", i)
print("media", media / len(eta_persone))