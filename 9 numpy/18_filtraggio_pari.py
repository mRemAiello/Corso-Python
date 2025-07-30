import numpy as np

# Esercizio 3: mascheramento e filtraggio avanzato
# Array 1D di numeri casuali tra 0 e 100
arr = np.random.randint(0, 101, size=20)
print("Array originale:", arr)

# Filtra elementi pari maggiori di 50
mask = (arr % 2 == 0) & (arr > 50)
filtrati = arr[mask]
print("Elementi pari > 50:", filtrati)
