# Distribuzione Binomiale
# Modella il numero di successi in n prove indipendenti,
# ciascuna con probabilità di successo p.

import numpy as np
import matplotlib.pyplot as plt

# Parametri
n = 10      # numero di prove
p = 0.5     # probabilità di successo

# Genera dati dalla distribuzione binomiale
dati = np.random.binomial(n, p, size=1000)

# Valori possibili (da 0 a n)
valori = np.arange(0, n + 1)

# Calcola la probabilità teorica: P(X=k) = C(n,k) * p^k * (1-p)^(n-k)
from math import comb
prob_teorica = [comb(n, k) * p**k * (1 - p)**(n - k) for k in valori]

# Grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Istogramma dei dati generati
ax1.hist(dati, bins=np.arange(-0.5, n + 1.5, 1), density=True,
         color='steelblue', edgecolor='black', alpha=0.7)
ax1.set_title('Distribuzione Binomiale (campione)')
ax1.set_xlabel('Numero di successi')
ax1.set_ylabel('Frequenza relativa')

# Distribuzione teorica
ax2.bar(valori, prob_teorica, color='coral', edgecolor='black', alpha=0.7)
ax2.set_title(f'Distribuzione Binomiale teorica (n={n}, p={p})')
ax2.set_xlabel('Numero di successi')
ax2.set_ylabel('Probabilità')

plt.tight_layout()
plt.show()

# Confronto tra diversi valori di p
fig, ax = plt.subplots(figsize=(8, 5))
for p_val in [0.2, 0.5, 0.8]:
    prob = [comb(n, k) * p_val**k * (1 - p_val)**(n - k) for k in valori]
    ax.plot(valori, prob, marker='o', label=f'p={p_val}')

ax.set_title(f'Distribuzione Binomiale (n={n})')
ax.set_xlabel('k')
ax.set_ylabel('P(X=k)')
ax.legend()
ax.grid(True)
plt.show()
