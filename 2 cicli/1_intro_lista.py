x = 5
print(x)

# Lista di elementi
# indici   0        1         2          3          4         5       6
lista = ["mela", "pera", "ciliegia", "lampone", "banana", "mirtillo", "fragola"]
print(lista)
print(lista[0])
print(lista[-1])
print(lista[5])
print(lista[x])
print(len(lista))

# Estrazione di un valore a caso dentro la lista
import random

# random.uniform(0, len(lista) -> ottengo un numero tra 0 e 7 (7 non incluso) -> ex. 5.82939039
# Operazione successiva, fare l'int di quel numero -> ex. 5.82939039 diventa 5
indice = int(random.uniform(0, len(lista)))
print(lista[indice])