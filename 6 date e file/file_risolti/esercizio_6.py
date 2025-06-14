# Scrivi un programma che chieda all’utente di inserire i valori di una tabella in formato CSV
# (valori separati da virgola), quindi scriva i valori in un file CSV.

file = open("file_2.csv", "w", encoding="utf8")

i = 0
while i < 2:

    nome = input("Scrivi un nome: ")
    cognome = input("Scrivi un cognome: ")
    eta = int(input("Scrivi un'età: "))

    stringa = "{},{},{}\n"
    stringa = stringa.format(nome, cognome, eta)

    file.write(stringa)

    i = i + 1

file.close()