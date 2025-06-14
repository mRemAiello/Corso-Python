# Scrivi un programma che legga il contenuto di un file di testo e lo stampi a schermo.

file = open("testo.txt", "r", encoding="utf8")

# print(file.read())

for riga in file:
    print(riga.replace("\n", ""))

file.close()