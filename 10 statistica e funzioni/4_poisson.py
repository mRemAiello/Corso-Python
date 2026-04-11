# Distribuzione di Poisson
# Modella il numero di eventi che si verificano in un intervallo
# di tempo/spazio fissato, con tasso medio lambda.
# P(X=k) = (lambda^k * e^(-lambda)) / k!

import numpy as np
import matplotlib.pyplot as plt
from math import factorial

# Parametri
lam = 5  # lambda (tasso medio di eventi)

# Genera dati dalla distribuzione di Poisson
dati = np.random.poisson(lam, size=1000)

# Valori possibili
k_max = 20
valori = np.arange(0, k_max)

# Calcola la probabilità teorica: P(X=k) = (lambda^k * e^(-lambda)) / k!
prob_teorica = [(lam**k * np.exp(-lam)) / factorial(k) for k in valori]

# Grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Istogramma dei dati generati
ax1.hist(dati, bins=np.arange(-0.5, k_max + 0.5, 1), density=True,
         color='steelblue', edgecolor='black', alpha=0.7)
ax1.set_title(f'Distribuzione di Poisson (campione, lambda={lam})')
ax1.set_xlabel('k (numero di eventi)')
ax1.set_ylabel('Frequenza relativa')

# Distribuzione teorica
ax2.bar(valori, prob_teorica, color='coral', edgecolor='black', alpha=0.7)
ax2.set_title(f'Distribuzione di Poisson teorica (lambda={lam})')
ax2.set_xlabel('k')
ax2.set_ylabel('P(X=k)')

plt.tight_layout()
plt.show()

# Confronto tra diversi valori di lambda
plt.figure(figsize=(8, 5))
for l in [1, 3, 5, 10]:
    prob = [(l**k * np.exp(-l)) / factorial(k) for k in valori]
    plt.plot(valori, prob, marker='o', label=f'lambda={l}')

plt.title('Distribuzione di Poisson - Confronto')
plt.xlabel('k')
plt.ylabel('P(X=k)')
plt.legend()
plt.grid(True)
plt.show()