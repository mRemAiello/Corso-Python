# 1) Data una stringa, stampa ogni carattere con indice (while e for).
"""
stringa = "Milano"

i = 0
for lettera in stringa:
    print(i, lettera)
    i = i + 1

i = 0
while i < len(stringa):
    # print(0, stringa[0])
    # print(1, stringa[1])
    print(i, stringa[i])
    i = i + 1

print(i)"""

# 2) Conta quante volte compare una lettera scelta dall'utente in una stringa.
"""
stringa = "aaabbxccdefgaa"
lettera = "a"
conta = 0
for elemento in stringa:
    if elemento == lettera:
        conta = conta + 1

print("La lettera", lettera, "è presente", conta, "volte")

i = 0
conta = 0
while i < len(stringa):
    if stringa[i] == lettera:
        conta = conta + 1
    i = i + 1

print("La lettera", lettera, "è presente", conta, "volte")"""


# 10) Mini menu testuale con while True:
#     - opzioni: somma, media, massimo, esci
#     - il programma termina solo quando l'utente sceglie "esci"

"""comando = input("Scegli un comando (somma, media, massimo, esci): ")
while not comando == "esci":

    if comando == "somma":
        primo_numero = int(input("Scegli un numero: "))
        secondo_numero = int(input("Scegli un numero: "))
        print("La somma è", primo_numero + secondo_numero)
    elif comando == "media":
        primo_numero = int(input("Scegli un numero: "))
        secondo_numero = int(input("Scegli un numero: "))
        print("La media è", (primo_numero + secondo_numero) / 2)
    elif comando == "massimo":
        primo_numero = int(input("Scegli un numero: "))
        secondo_numero = int(input("Scegli un numero: "))
        if primo_numero > secondo_numero:
            print("Il massimo è", primo_numero)
        else:
            print("Il massimo è", secondo_numero)
    else:
        print("Comando non riconosciuto")

    comando = input("Scegli un comando (somma, media, massimo, esci): ")"""


# Deve sommare finchè l'utente non scrive 0
numero = int(input("Scegli un numero: "))
somma = 0
while not numero == 0:
    somma = somma + numero
    numero = int(input("Scegli un numero: "))

print("La somma totale è", somma)