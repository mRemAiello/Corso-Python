# Distribuzione Uniforme
# Tutti i valori nell'intervallo [a, b] hanno la stessa probabilità.

import numpy as np
import matplotlib.pyplot as plt

# Parametri
a = 2   # limite inferiore
b = 8   # limite superiore

# Genera dati dalla distribuzione uniforme
dati = np.random.uniform(a, b, size=1000)

# PDF teorica: f(x) = 1 / (b - a) per a <= x <= b
x = np.linspace(a - 1, b + 1, 500)
pdf = np.where((x >= a) & (x <= b), 1 / (b - a), 0)

# Grafico
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Istogramma dei dati generati
ax1.hist(dati, bins=30, density=True, color='steelblue',
         edgecolor='black', alpha=0.7)
ax1.set_title('Distribuzione Uniforme (campione)')
ax1.set_xlabel('x')
ax1.set_ylabel('Densità')

# PDF teorica
ax2.plot(x, pdf, color='coral', linewidth=2)
ax2.fill_between(x, pdf, alpha=0.3, color='coral')
ax2.set_title(f'PDF Uniforme teorica (a={a}, b={b})')
ax2.set_xlabel('x')
ax2.set_ylabel('f(x)')

plt.tight_layout()
plt.show()

# Confronto istogramma e PDF teorica sovrapposti
plt.figure(figsize=(8, 5))
plt.hist(dati, bins=30, density=True, color='steelblue',
         edgecolor='black', alpha=0.5, label='Campione')
plt.plot(x, pdf, color='red', linewidth=2, label='PDF teorica')
plt.title('Distribuzione Uniforme - Confronto')
plt.xlabel('x')
plt.ylabel('Densità')
plt.legend()
plt.grid(True)
plt.show()
