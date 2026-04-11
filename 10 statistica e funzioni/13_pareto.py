# Distribuzione di Pareto
# Modella fenomeni con la regola 80/20 (es. distribuzione della ricchezza).
# PDF: f(x) = (alpha * x_m^alpha) / x^(alpha+1)  per x >= x_m

import numpy as np
import matplotlib.pyplot as plt

# Parametri
alpha = 3   # parametro di forma
x_m = 1     # scala minima

# Genera dati dalla distribuzione di Pareto
# numpy.random.pareto genera Pareto di tipo II (Lomax), aggiungiamo x_m
dati = (np.random.pareto(alpha, size=5000) + 1) * x_m

# PDF teorica
x = np.linspace(x_m, 5, 500)
pdf = (alpha * x_m**alpha) / x**(alpha + 1)

# Grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Istogramma e PDF sovrapposti
ax1.hist(dati, bins=100, density=True, color='steelblue',
         edgecolor='black', alpha=0.5, label='Campione', range=(x_m, 5))
ax1.plot(x, pdf, color='red', linewidth=2, label='PDF teorica')
ax1.set_title(f'Distribuzione di Pareto (alpha={alpha})')
ax1.set_xlabel('x')
ax1.set_ylabel('Densità')
ax1.legend()

# Confronto con diversi valori di alpha
for a in [1, 2, 3, 5]:
    pdf_a = (a * x_m**a) / x**(a + 1)
    ax2.plot(x, pdf_a, linewidth=2, label=f'alpha={a}')

ax2.set_title('Pareto - Confronto parametri')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
