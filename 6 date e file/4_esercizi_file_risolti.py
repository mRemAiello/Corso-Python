# Scrivi un programma che legga il contenuto di un file di testo e lo stampi a schermo.


"""file = open("testo.txt", "r", encoding="utf8")

# print(file.read())

for riga in file:
    print(riga.replace("\n", ""))

file.close()"""


# Scrivi un programma che chieda all’utente di inserire una stringa, quindi scriva la stringa in un file di testo.

"""stringa = input("Scrivi un testo: ")
file = open("utente.txt", "a", encoding="utf8")
file.write(stringa + "\n")
file.close()"""



# Scrivi un programma che legga il contenuto di un file di testo e lo copi in un altro file.

"""file_1 = open("utente.txt", "r", encoding="utf-8")
file_2 = open("utente_2.txt", "w", encoding="utf-8")
for riga in file_1:
    file_2.write(riga)

file_1.close()
file_2.close()"""


# Scrivi un programma che conti le righe di un file di testo.

"""file = open("studenti.txt", "r", encoding="utf8")
righe = 0
for riga in file:
    righe = righe + 1

file.close()
print(righe)"""


# Esempio
"""file = open("file.csv", "r", encoding="utf-8")
file_lista = []
for riga in file:

    riga_split = riga.split(";")
    username = riga_split[0].replace("\n", "").strip()
    print(username)

file.close()"""




# Scrivi un programma che legga il contenuto di un file CSV (valori separati da virgola) e lo stampi a schermo in forma di tabella.

"""file = open("file.csv", "r", encoding="utf-8")
for riga in file:
    riga_split = riga.split(";")
    for element in riga_split:
        print(element.replace("\n", "").strip(), end=" ")
    print()

file.close()"""


# Scrivi un programma che chieda all’utente di inserire i valori di una tabella in formato CSV (valori separati da virgola),
# quindi scriva i valori in un file CSV.

"""file = open("file_2.csv", "w", encoding="utf8")

i = 0
while i < 2:

    nome = input("Scrivi un nome: ")
    cognome = input("Scrivi un cognome: ")
    eta = int(input("Scrivi un'età: "))

    stringa = "{},{},{}\n"
    stringa = stringa.format(nome, cognome, eta)

    file.write(stringa)

    i = i + 1

file.close()"""

# Scrivi un programma che legga il contenuto di un file di testo e lo copi in un altro file, invertendo l’ordine delle righe.

"""file_1 = open("utente.txt", "r", encoding="utf-8")
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
file_2.close()"""