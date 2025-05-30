# Set semplice
primo_set = {"Milano", "Roma", "Udine", "Milano"}
# y = {"Milano", 5, 4.5, False}

# x = set({"Milano", "Roma"})

# Printa gli elementi
# NB: Saranno ogni volta con un ordine casuale
print(primo_set)

# Tipo
print(type(primo_set))

# Lunghezza
print(len(primo_set))

# Accedere agli elementi NO!
# print(x[2])
# print(x[-1])

# Range di elementi (secondo elemento non incluso) NO!
# print(x[:2])
# print(x[1:])


# Per accedere agli elementi, devo fare un loop
for citta in primo_set:
    print(citta)

# Aggiunta di elementi e unione di liste
primo_set.add("Palermo")
print(primo_set)

primo_set.add("Torino")
print(primo_set)

primo_set.add("Venezia")
print(primo_set)

# Rimozione di elementi con remove e discard
# NB: Se l'elemento non esiste, con remove avremo un errore, con discard NO
if "Palermo" in primo_set:
    primo_set.remove("Palermo")
primo_set.discard("Milano")

# Rimuovo il primo elemento, essendo il set casuale, anche l'elemento rimosso sarà quello che capita
terzo_set = primo_set.pop()
print(terzo_set)

# Pulizia del set e cancellazione dello stesso in memoria
# x.clear()
# del x



# Prende il set e aggiunge y
secondo_set = {"Venezia", "Brescia", "Milano"}
# x.update(y)
print(primo_set)

# Prende x e aggiunge y MA creando un nuovo set, che quindi va inserito dentro una variabile (z)
terzo_set = primo_set.union(secondo_set)
print(primo_set)
print(terzo_set)

# Intersezioni NB: La funzione intersection non modifica nessuna delle due liste,
# intersection_update invece modifica la lista x
terzo_set = primo_set.intersection(secondo_set)
primo_set.intersection_update(secondo_set)
# Cosa succede con _update
# x -> 1, 2, 3
# y -> 2, 4, 5
# x -> 2
print(primo_set)
print(terzo_set)

# Differenze tra set
terzo_set = primo_set.symmetric_difference(secondo_set)
primo_set.symmetric_difference_update(secondo_set)
print(primo_set)
print(terzo_set)