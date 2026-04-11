import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

# Parametri della distribuzione t di Student
df = 25  # Gradi di libertà

# Genera i dati per l'asse x
x = np.linspace(-4, 4, 1000)

# Calcola i valori della distribuzione t di Student
y = t.pdf(x, 5)
y1 = t.pdf(x, 20)
y2 = t.pdf(x, 40)

# Crea il grafico
plt.plot(x, y, label=f't-Student (df={5})')
plt.plot(x, y1, label=f't-Student (df={10})')
plt.plot(x, y2, label=f't-Student (df={15})')

# Aggiungi titoli e etichette
plt.title('Distribuzione t di Student')
plt.xlabel('x')
plt.ylabel('Densità di probabilità')

# Mostra la legenda
plt.legend()

# Mostra il grafico
plt.grid(True)
plt.show()