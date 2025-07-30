import numpy as np

# Esercizio 4: uso di np.where per sostituzioni
mat = np.random.randint(0, 10, size=(5, 5))
print("Matrice originale:\n", mat)

# Sostituiamo i valori > 5 con -1
sostituita = np.where(mat > 5, -1, mat)
print("Dopo np.where:\n", sostituita)
