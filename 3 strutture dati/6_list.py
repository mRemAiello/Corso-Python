# Lista semplice
prima_lista = ["Milano", "Roma", "Udine", "Venezia"]

# La lista può anche avere tipi di variabili differenti
# y = ["Milano", 5, 4.5, False]

# Printa gli elementi della lista
print(prima_lista)

# Tipo di lista
print(type(prima_lista))

# Lunghezza
print(len(prima_lista))

# Accedere agli elementi
print(prima_lista[2])
print(prima_lista[-1])

# Range di elementi (secondo elemento non incluso)
# Risultato: ["Milano", "Roma"]
print(prima_lista[:2])

# Risultato: ["Roma", "Udine", "Venezia"]
print(prima_lista[1:])

# Risultato: ["Roma, "Udine"]
print(prima_lista[1:3])

# Modifica elementi interni
prima_lista[0] = "Milano2"
print(prima_lista)
prima_lista[0:2] = ["Milano3", "Roma2", "Catania", "Roma"]
print(prima_lista)

# Inserimento di elementi
prima_lista.append("Palermo")
print(prima_lista)

#
prima_lista.insert(1, "Brescia")
print(prima_lista)

#
seconda_lista = ["Napoli", "Catania"]
prima_lista.extend(seconda_lista)
print(prima_lista)

# Sort
prima_lista.sort()
print(prima_lista)
prima_lista.reverse()
print(prima_lista)

# Rimozione di elementi
if "Milano3" in prima_lista:
    prima_lista.remove("Milano3")
print(prima_lista)

quarto_elemento = prima_lista.pop(3)
print(quarto_elemento)
print(prima_lista)

# prima_lista -> []
prima_lista.clear()

# Copiare una lista
nuova_lista = prima_lista.copy()
print(nuova_lista)

# Cancella la variabile
del nuova_lista
# Darebbe errore
# print(nuova_lista)