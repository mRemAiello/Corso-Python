import numpy as np
from numpy import random

# Numero random
numero = random.randint(20, 100, size = 3)
print(numero)
print()


# Array
# arr = random.randint(100, size=(3))
arr = random.randint(20, 100, size=(3, 5, 2))
print("Array 3, 5, 2")
print(arr)
print()


# Scelta
arr = np.array([1, 2, 3, 4, 5, 6])
print("Estrazione numeri casuali da un np-array")
print(random.choice(arr))
print(random.choice(arr, size=5, replace=False))
print()


# Scelta con probabilità
arr = np.array([1, 2, 3, 4])
prob = np.array([0.5, 0.3, 0.19, 0.01])
print(random.choice(arr, p=prob, size=20))
print()


# Disordinare
# Shuffle disordina l'array e lo modifica
arr = [1, 2, 3, 5, 6]
random.shuffle(arr)
print(arr)
print()

# Permutation crea un nuovo array disordinato, l'originale non viene toccato
arr2 = random.permutation(arr)
print(arr2)