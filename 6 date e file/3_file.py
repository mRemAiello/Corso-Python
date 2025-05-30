# File handling
# r - Read: Apriamo un file per leggerlo, se non esiste si ha un errore
# a - Append: Apriamo un file per aggiungere elementi, crea il file se non esiste
# w - Write: Apre il file per scrivere, crea il file se non esiste
# x - Create: Crea il file, errore se esiste

# Se non metto il secondo parametro, di default è r
file = open("file_2.csv", "r", encoding="utf8")
print(file)

# Leggi il file (interamente)
# print(file.read())

# Leggo parte del file
# print(file.read(10))
# print(file.read(10))
# print(file.read(10))

# Leggo tutta una linea
# print(file.readline())
# print(file.readline())
# print(file.readline())

# Utilizziamo il ciclo per scorrere le righe
i = 1
for riga in file:
    if i > 1:
        elementi = riga.split(",")
        elementi[0] = elementi[0].strip().capitalize().replace("\n", "")
        elementi[1] = elementi[1].strip().capitalize().replace("\n", "")
        elementi[2] = elementi[2].strip().capitalize().replace("\n", "")
        elementi[2] = int(elementi[2])
        print(elementi)

    i = i + 1

# Chiudi il file, IMPORTANTE FARLO
file.close()

# Inseriamo elementi
file = open("testo.txt", "a")
file.write("Elaborazione 5/2024\n")
file.write("Inseriamo un testo\n")
file.close()

# Creiamo un nuovo file
# file = open("testo.txt", "x")
# file.close()

# Controllo se il file esiste
import os
print(os.path.exists("testo.txt"))