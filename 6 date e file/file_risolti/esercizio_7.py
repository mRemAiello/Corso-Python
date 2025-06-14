# Scrivi un programma che legga il contenuto di un file di testo e lo copi in un altro file,
# invertendo l’ordine delle righe.

file_1 = open("utente.txt", "r", encoding="utf-8")
file_2 = open("utente_2.txt", "w", encoding="utf-8")
file_lista = []
for riga in file_1:
    file_lista.append(riga.replace("\n", ""))

i = -1
while i >= -len(file_lista):

    file_2.write(file_lista[i])
    file_2.write("\n")
    i = i - 1

file_1.close()
file_2.close()