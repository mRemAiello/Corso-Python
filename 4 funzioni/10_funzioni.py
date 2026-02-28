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
def faccio_pasta_v2(pippo):
    print("Peso la pasta")
    print("Aspetto che l'acqua bolle")
    print("Butto la pasta")

    if pippo:
        print("Metto il sugo")

    print()


sugo = True
# sugo True -> faccio_pasta_v2(True) -> pippo = True
faccio_pasta_v2(sugo)
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


# Lancio con tipo_pasta "Spaghetti", sugo False
x = faccio_pasta_v3()
# Lancio con tipo_pasta "", sugo False
y = faccio_pasta_v3("")
# Lancio con tipo_pasta "Rigatoni", sugo False
z = faccio_pasta_v3("Rigatoni")
# Lancio con tipo_pasta "Cannelloni", sugo True
t = faccio_pasta_v3("Cannelloni", True)

print("Risultato 1", x)
print("Risultato 2", y)
print("Risultato 3", z)
print("Risultato 4", t)