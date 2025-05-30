import numpy as np

# 1 Dimensione
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Unione
arr = np.concatenate((arr1, arr2))
print(arr)
print()


# 2 Dimensione
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Unione
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
print()


# Row-Stack (H-Stack) -> Affianca gli array, colonna per colonna
arr = np.hstack((arr1, arr2))
print("H-Stack:")
print(arr)
print()

# Column Stack (V-Stack) -> Impila gli array
arr = np.vstack((arr1, arr2))
print("V-Stack:")
print(arr)
print()


# [1 2] [3 4]
# [5 6] [7 8]

#           [.....]
#     [3 7] [4 8]
# [1 5] [2 6]

# Height Stack (D-Stack) -> Combina in una nuova dimensione, lungo l'asse della profondità
arr = np.dstack((arr1, arr2))
print("D-Stack:")
print(arr)