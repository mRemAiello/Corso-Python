# Esempio con media
eta_persone = [18, 20, 22, 30, 35, 20, 40, 40]


# Ciclo for media
media = 0
for eta in eta_persone:
    media = media + eta
    print("eta", eta)
    print("media", media)
    print()

print("media", media / len(eta_persone))