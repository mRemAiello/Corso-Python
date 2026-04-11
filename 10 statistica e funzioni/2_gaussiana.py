# Gaussiana

import numpy as np
import matplotlib.pyplot as plt

# Parametri della distribuzione gaussiana
media = 0  # Media
sigma = 1  # Deviazione standard

# Genera i dati per l'asse x
x = np.linspace(media - 3 * sigma, media + 3 * sigma, 1000)

print(x)
print()

# Calcola i valori della distribuzione gaussiana
print(np.pi)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - media) / sigma) ** 2)

print(y)

# Crea il grafico
plt.plot(x, y)

# Aggiungi titoli e etichette
plt.title('Distribuzione Gaussiana')
plt.xlabel('x')
plt.ylabel('Probabilità')

# Mostra il grafico
plt.grid(True)
plt.show()