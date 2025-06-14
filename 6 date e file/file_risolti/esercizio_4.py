# Scrivi un programma che conti le righe di un file di testo.

file = open("studenti.txt", "r", encoding="utf8")
righe = 0
for riga in file:
    righe = righe + 1

file.close()
print(righe)