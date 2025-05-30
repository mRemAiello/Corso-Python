import numpy as np

# Slice da 1 a 5
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])


# Slice da 0 a 4
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])


# Slice da -3 a -1
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])


# Slice da 1 a 5 con step di 2
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:7:2])


# Slice array 2D
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])