import numpy as np


# Def
def add_five(x):
    if x % 2 == 0:
        return x + 5, x + 6
    else:
        return x, x + 2


# Esempio di utilizzo:
# arr -> [1 2 3 4 5 6]
# arr2 -> [1 7 3 9 5 11]

# Con questo codice la registro come ufunc di numpy, evitando errori
# Es. utilizzando una lista normale otterrei un errore
# variabile -> add_five -> variabile(4)
u_func_five = np.frompyfunc(add_five, 1, 2)


# Utilizzo ufunc
arr = np.array([1, 2, 3, 4, 5, 6, 7])
arr2 = np.array([7, 8, 9, 10])
print(u_func_five(arr))
print(u_func_five(arr2))
print()

# Carrellata di ufunc
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Primo esempio: add
# Altre: subtract, divide, multiply, power, mod
# [1 6] -> [7]
# [2 7] -> [9]
arr = np.add(arr1, arr2)
print(arr)
print()

# Ceil / floor
arr = np.ceil([4.567, 5.42])
print(arr)
print()