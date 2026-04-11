# Distribuzione Chi-Quadrato (Chi-Square)
# Somma dei quadrati di k variabili normali standard indipendenti.
# Usata nei test di ipotesi e intervalli di confidenza.

import numpy as np
import matplotlib.pyplot as plt
from math import gamma

# Parametri
gradi_liberta = [1, 2, 3, 5, 10]

# Genera dati
x = np.linspace(0.01, 20, 500)

# PDF teorica: f(x) = (x^(k/2 - 1) * e^(-x/2)) / (2^(k/2) * Gamma(k/2))
plt.figure(figsize=(10, 6))
for k in gradi_liberta:
    dati = np.random.chisquare(k, size=1000)
    pdf = (x ** (k / 2 - 1) * np.exp(-x / 2)) / (2 ** (k / 2) * gamma(k / 2))
    plt.plot(x, pdf, linewidth=2, label=f'k={k}')

plt.title('Distribuzione Chi-Quadrato')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.ylim(0, 0.5)
plt.show()

# Istogramma per k=5
k = 5
dati = np.random.chisquare(k, size=5000)
pdf = (x ** (k / 2 - 1) * np.exp(-x / 2)) / (2 ** (k / 2) * gamma(k / 2))

plt.figure(figsize=(8, 5))
plt.hist(dati, bins=50, density=True, color='steelblue',
         edgecolor='black', alpha=0.5, label='Campione')
plt.plot(x, pdf, color='red', linewidth=2, label='PDF teorica')
plt.title(f'Distribuzione Chi-Quadrato (k={k})')
plt.xlabel('x')
plt.ylabel('Densità')
plt.legend()
plt.grid(True)
plt.show()
