import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

# Array Split
# [1 2] [3 4] [5] [6]
arr2 = np.array_split(arr, 4)
print(arr2)
print()

# Split
arr2 = np.split(arr, 3)
print(arr2)
print()

# 2D
# [1 2]
# [3 4]
# [5 6]
arr = np.array([[1, 2], [3, 4], [5, 6]])
arr2 = np.split(arr, 3)
print(arr2)
print()