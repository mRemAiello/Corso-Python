import numpy as np

# Differenze: la lista np è 50x più veloce della lista python
lista_np = np.array([1, 2, 3, 4, 5])
lista = [1, 2, 3, 4, 5]

print(lista)
print(lista_np)
print()

# Tipo
print(type(lista))
print(type(lista_np))
print()

# Differenza 2: moltiplico per numero, comportamenti diversi
print(lista * 5)
print(lista_np * 5)
print()

# Somma, errore
# print(lista + 5)
print(lista_np + 5)
print()

# Tipologie di array in np
# Dimensione 0: scalare
array0D = np.array(10)

# Dimensione 1: Array, Vettore, Lista
array1D = np.array([1, 2, 3])

# Dimensione 2: matrici
# 1 2 3
# 4 5 6
array2D = np.array([[1, 2, 3],
                    [4, 5, 6]])

print(array0D)
print(array1D)
print(array2D)
print()

# Dimensioni multiple senza impazzire
arrayXD = np.array([1, 2, 3], ndmin=3)
print(arrayXD)
print(arrayXD.ndim)
print()

# Range di array
arrayRange = np.arange(1, 23, 3)
print(arrayRange)
print()

# Array di 0
aZeros = np.zeros(3)
print(aZeros)
aZeros = np.zeros((3, 2))
print(aZeros)
print()

# Array di uno
aOnes = np.ones(3)
print(aOnes)
print()