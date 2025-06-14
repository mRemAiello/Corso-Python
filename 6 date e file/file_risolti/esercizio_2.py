# Scrivi un programma che chieda all’utente di inserire una stringa, quindi scriva la stringa in un file di testo.

stringa = input("Scrivi un testo: ")
file = open("utente.txt", "a", encoding="utf8")
file.write(stringa + "\n")
file.close()