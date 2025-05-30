import numpy as np

# Tipologie di array in np
# Dimensione 0: scalare
array0D = np.array(10)
array1D = np.array([1, 2, 3])

# Dimensione 3: matrici
array2D = np.array([[1, 2, 3], [4, 5, 6]])

# Prendo l'elemento 2
print(array1D[1])

# Prendo l'elemento 5 in un array di 2 dim
# 1 2 3
# 4 5 6
print(array2D[1, 1])

# Posso anche usare i negativi
print(array2D[1, -1])