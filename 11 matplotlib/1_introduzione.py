from matplotlib import pyplot as plt
import numpy as np

x = [25, 26, 27, 28]
y = [10, 40, 20, 50]

#
# plt.plot(x, y)


# Plot multipli
y1 = [20, 20, 15, 80]
# plt.plot(x, y1)
# plt.show()


# Personalizzare
"""plt.title("Grafico età / valori")
plt.xlabel("Età")
plt.ylabel("Valori")
plt.legend(["Italiani", "Inglesi"])
plt.grid()
plt.show()"""


# Impostazioni avanzate
# plt.plot(x, y)
# plt.plot(x, y1)
plt.plot(x, y, label="Italiani", color="red", linewidth=2, linestyle="-", marker="o")
plt.plot(x, y1, label="Inglesi", color="black", linewidth=4, linestyle="dotted")
plt.title("Grafico età / valori")
plt.xlabel("Età")
plt.ylabel("Valori")
plt.legend(["Italiani", "Inglesi"])


# Stili
print(plt.style.available)
plt.style.use("dark_background")
plt.grid()
plt.show()


# Documentazione consigliata
# https://www.w3schools.com/python/matplotlib_intro.asp