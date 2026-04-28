# Ciclo for
eta_persone = [18, 20, 22, 30, 35, 20, 40, 40]

#
eta_min = int(input("Seleziona l'età minima per la media: "))

# Facciamo la media parziale considerando un'età minima
media = 0
conta = 0
for eta in eta_persone:
    print("eta", eta)
    if eta > eta_min:
        media = media + eta
        conta = conta + 1

        print("media", media)
        print("conta", conta)
    print()

#
print("media", media / conta)