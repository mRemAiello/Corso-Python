import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 4, 4, 7, 8])

# arr == 4 -> [False False False True False False True True False False]
arrInd = np.where(arr == 4)
arrCount = arrInd[0].tolist()
print(arrInd, len(arrCount))
print()

# Esempio con pari
arrInd = np.where(arr % 2 == 0)
print(arrInd)
print()

# Ordino
arr = np.array([[1, 2, 3], [5, 4, 6], [4, 4, 7]])
arrSort = np.sort(arr)
print(arrSort)
print()

# Filtraggio statico
arr = np.array([1, 2, 3, 4])
filtro = [False, False, False, True]
arrayFilt = arr[filtro]
print(arrayFilt)
print()


# Filtraggio "veloce"
# arr = [1 2 3 4]
# filtro = [False True False True]
# filtro2 = [False False True True]
filtro = arr % 2 == 0
filtro2 = arr > 2

# filtro + filtro2 =
# Somma tra booleani è False+False=False, False+True=True, True+True=True
# [False True True True]

# np.all fa una cosa diversa dalla somma tra booleani
filtro3 = np.all([filtro, filtro2], axis=0)
print(filtro, filtro2, filtro3)

# Infine ottengo i risultati
arrayFilt = arr[filtro3]
print(arrayFilt)
print()