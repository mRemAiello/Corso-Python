# Scrivi un programma che legga il contenuto di un file di testo e lo copi in un altro file.

file_1 = open("utente.txt", "r", encoding="utf-8")
file_2 = open("utente_2.txt", "w", encoding="utf-8")
for riga in file_1:
    file_2.write(riga)

file_1.close()
file_2.close()