import numpy as np

# Esercizio 1: operazioni element-wise con broadcasting
# Creiamo due array 1D di lunghezza diversa
arr_a = np.arange(3).reshape(3, 1)  # shape (3,1)
arr_b = np.arange(5)  # shape (5,)

# Somma con broadcasting -> risultato (3,5)
somma = arr_a + arr_b
print("Somma con broadcasting:")
print(somma)
print()

# Applichiamo np.log1p all'array ottenuto
log_result = np.log1p(somma)
print("np.log1p del risultato:")
print(log_result)
