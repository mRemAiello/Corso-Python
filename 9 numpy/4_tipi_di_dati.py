import numpy as np

# Referenze
# https://www.w3schools.com/python/numpy/numpy_data_types.asp

# Esempio con tipo stringa
arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)
print()


# Posso fare anche l'inverso
arr = np.array(["1", "2", "3"], dtype="i1")

print(arr)
print(arr.dtype)
print()


# Conversione
arr = arr.astype("S")

print(arr)
print(arr.dtype)