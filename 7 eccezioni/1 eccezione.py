try:

    numero = int(input("Inserisci un numero: "))


except ValueError:

    print("Errore: Devi inserire un numero valido.")
    print("Continuo con un numero default 1")
    numero = 1

#
print(f"Hai inserito il numero: {numero}")
print("Proseguo col programma")

#
print(f"Moltiplico per 2: {numero * 2}")