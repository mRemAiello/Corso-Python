# Distribuzione di Rayleigh
# Modella la distanza dall'origine di un punto con coordinate
# gaussiane indipendenti. Usata in telecomunicazioni e fisica.
# PDF: f(x) = (x / sigma^2) * e^(-x^2 / (2*sigma^2))

import numpy as np
import matplotlib.pyplot as plt

# Parametri
sigma = 1   # parametro di scala

# Genera dati dalla distribuzione di Rayleigh
dati = np.random.rayleigh(sigma, size=5000)

# PDF teorica
x = np.linspace(0, 6, 500)
pdf = (x / sigma**2) * np.exp(-x**2 / (2 * sigma**2))

# Grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Istogramma e PDF sovrapposti
ax1.hist(dati, bins=50, density=True, color='steelblue',
         edgecolor='black', alpha=0.5, label='Campione')
ax1.plot(x, pdf, color='red', linewidth=2, label='PDF teorica')
ax1.set_title(f'Distribuzione di Rayleigh (sigma={sigma})')
ax1.set_xlabel('x')
ax1.set_ylabel('Densità')
ax1.legend()

# Confronto con diversi valori di sigma
for s in [0.5, 1, 2, 3]:
    pdf_s = (x / s**2) * np.exp(-x**2 / (2 * s**2))
    ax2.plot(x, pdf_s, linewidth=2, label=f'sigma={s}')

ax2.set_title('Rayleigh - Confronto parametri')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
