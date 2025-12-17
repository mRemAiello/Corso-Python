x = 5
print(x)

# Lista di elementi
# indici   0        1     2    3       4         5       6
lista = ["apple", "mela", 1, False, "banana", "cherry", 10.1]
print(lista)
print(lista[0])
print(lista[-1])
print(lista[5])
print(lista[x])
print(len(lista))

# Estraggo un numero a caso
import random
indice = int(random.uniform(0, len(lista)))
print(lista[indice])