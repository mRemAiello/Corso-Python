from matplotlib import pyplot as plt
import numpy as np

plt.style.use("ggplot")

x = np.array([27, 28, 29, 30, 31, 32])
y = np.array([80, 150, 170, 130, 140, 190])

media = 125

plt.plot(x, y)

# Coloro base
# plt.fill_between(x, y, alpha=0.2)

# Imposto una media
# plt.fill_between(x, y, media, alpha=0.2)

# Con condizione
# plt.fill_between(x, y, media, where=(y > 150), alpha=0.2, interpolate=True)

plt.title("Nome del grafico")
plt.show()