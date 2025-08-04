import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Shape
print("Shape di arr")
print(arr)
print(arr.shape)
print()


# Reshape, cioè cambio della forma
# NB: Fattibile solo se il numero di elementi combacia perfettamente
print("Array reshape")
print(arr.reshape(2, 3))
print()

# NB2: Il reshape è un array view
print("Reshape è una view")
print(arr.reshape(2, 3).base)
print()


# Inserendo -1, è possibile far calcolare a numpy la dimensione sconosciuta
print("Reshape con calcolo dimensione automatico")
print(arr.reshape(3, -1))
print()


# "Spianare" l'array
arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Array da 'spianare'")
print(arr)
print()

print("Flatten")
print(arr.flatten())
print()

print("Reshape")
print(arr.reshape(-1))