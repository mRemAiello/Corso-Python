import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([[1, 2, 3], [3, 4, 5]])

print(arr)
print(arr2)
print()


# Shape
print(arr.shape)
print(arr2.shape)
print()


# Reshape, cioè cambio della forma
# NB: Fattibile solo se il numero di elementi combacia perfettamente
print(arr.reshape(2, 3))
print()

# NB2: Il reshape è un array view
print(arr.reshape(2, 3).base)
print()


# Inserendo -1, è possibile far calcolare a numpy la dimensione sconosciuta
print(arr.reshape(3, -1))
print()


# "Spianare" l'array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print()

print("Flatten")
print(arr.flatten())
print()

print("Reshape")
print(arr.reshape(-1))