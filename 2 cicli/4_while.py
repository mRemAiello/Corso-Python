# Ciclo while
eta_persone = [18, 20, 22, 30, 35, 20, 40, 40]

i = 0
media = 0
while i < len(eta_persone):

    media = media + eta_persone[i]
    print("eta", eta_persone[i])
    print("media", media)
    print("i", i)
    print()

    i = i + 1

#
print("media", media / len(eta_persone))