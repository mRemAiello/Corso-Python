from matplotlib import pyplot as plt

plt.style.use("ggplot")

x = [13, 18, 18, 22, 27, 30, 35, 36, 40, 50, 51, 42, 54, 55, 40, 18, 20, 22, 24]
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Base
# plt.hist(x, bins=15)

# Impostiamo i beans
# plt.hist(x, bins=bins)

# Colori
plt.hist(x, bins=bins, color="orange", edgecolor="black")

# Piazzo una linea
plt.axvline(27, color="red", linewidth=3)

plt.title("Istogramma")
plt.show()