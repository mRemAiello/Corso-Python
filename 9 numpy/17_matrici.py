import numpy as np

# Esercizio 2: operazioni su matrici
# Generiamo due matrici 3x3 con valori casuali tra 0 e 9
m1 = np.random.randint(0, 10, size=(3, 3))
m2 = np.random.randint(0, 10, size=(3, 3))

print("Matrice 1:\n", m1)
print("Matrice 2:\n", m2)
print()

# Prodotto matrice-matrice
prodotto = m1 @ m2
print("Prodotto matrice-matrice:\n", prodotto)
print()

# Trasposta e determinante della prima matrice
trasposta = m1.T
det = np.linalg.det(m1)
print("Trasposta di m1:\n", trasposta)
print("Determinante di m1:", det)
