import numpy as np

# Esercizio 5: aggregazioni lungo assi diversi
mat = np.random.randint(0, 100, size=(4, 6))
print("Matrice:\n", mat)

somma_righe = mat.sum(axis=1)
somma_colonne = mat.sum(axis=0)
somma_totale = mat.sum()

print("Somma per righe:", somma_righe)
print("Somma per colonne:", somma_colonne)
print("Somma totale:", somma_totale)
