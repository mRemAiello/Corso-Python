# Distribuzione Logistica
# Simile alla gaussiana ma con code più pesanti.
# PDF: f(x) = e^(-(x-mu)/s) / (s * (1 + e^(-(x-mu)/s))^2)

import numpy as np
import matplotlib.pyplot as plt

# Parametri
mu = 0      # media (posizione)
s = 1       # scala

# Genera dati dalla distribuzione logistica
dati = np.random.logistic(mu, s, size=1000)

# PDF teorica
x = np.linspace(-10, 10, 500)
z = np.exp(-(x - mu) / s)
pdf = z / (s * (1 + z) ** 2)

# Grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Istogramma
ax1.hist(dati, bins=40, density=True, color='steelblue',
         edgecolor='black', alpha=0.7)
ax1.set_title('Distribuzione Logistica (campione)')
ax1.set_xlabel('x')
ax1.set_ylabel('Densità')

# PDF teorica
ax2.plot(x, pdf, color='coral', linewidth=2)
ax2.fill_between(x, pdf, alpha=0.3, color='coral')
ax2.set_title(f'PDF Logistica (mu={mu}, s={s})')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')

plt.tight_layout()
plt.show()

# Confronto con diversi parametri di scala
plt.figure(figsize=(8, 5))
for s_val in [0.5, 1, 2]:
    z = np.exp(-(x - mu) / s_val)
    pdf = z / (s_val * (1 + z) ** 2)
    plt.plot(x, pdf, linewidth=2, label=f's={s_val}')

plt.title('Distribuzione Logistica - Confronto scale')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
