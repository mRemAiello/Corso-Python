# Scrivi un programma che legga il contenuto di un file CSV (valori separati da virgola)
# e lo stampi a schermo in forma di tabella.

file = open("file.csv", "r", encoding="utf-8")
for riga in file:
    riga_split = riga.split(";")
    for element in riga_split:
        print(element.replace("\n", "").strip(), end=" ")
    print()

file.close()