# Devo fare un piatto di pasta
def faccio_pasta():
    print("Peso la pasta")
    print("Aspetto che l'acqua bolle")
    print("Butto la pasta")
    print("Mangio la pasta")
    print("Lavo i piatti")
    print()


faccio_pasta()
faccio_pasta()
faccio_pasta()


# Pasta e sugo
def faccio_pasta_v2(sugo):
    print("Peso la pasta")
    print("Aspetto che l'acqua bolle")
    print("Butto la pasta")

    if sugo:
        print("Metto il sugo")

    print()


faccio_pasta_v2(True)
faccio_pasta_v2(False)
faccio_pasta_v2(True)


# Scelgo sugo e spaghetti
def faccio_pasta_v3(tipo_pasta="Spaghetti", sugo=False):
    if tipo_pasta == "":
        return "Inserisci un tipo di pasta"
    print("Peso la pasta")
    print("Aspetto che l'acqua bolle")
    print("Butto la pasta " + tipo_pasta)
    if sugo:
        print("Metto il sugo")
    print()

    return True


x = faccio_pasta_v3("")
y = faccio_pasta_v3("Rigatoni")
z = faccio_pasta_v3("Cannelloni", True)

print(x, y, z)