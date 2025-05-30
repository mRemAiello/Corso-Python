from matplotlib import pyplot as plt

plt.style.use("ggplot")

x = [1, 4, 5, 6, 7, 1, 10, 20]
y = [1, 2, 3, 4, 9, 8, 2, 4]

# Grafico standard
# plt.scatter(x, y)

# s = size dei punti
# c = colore dei punti
# marker = forma dei punti
# plt.scatter(x, y, s=100, c="green", marker="X")

# edgecolor = colore dei cerchi
# linewidth = grandezza dei cerchi esterni
# alpha = opacità dei punti
# plt.scatter(x, y, s=100, c="green", marker="o", edgecolor="purple", linewidth=30, alpha=0.5)

#
colors = [1, 4, 6, 6, 8, 8, 8, 10]
sizes = [100, 200, 300, 400, 500, 600, 700, 800]
plt.scatter(x, y, c=colors, cmap="Greens", s=sizes, marker="o", alpha=0.7)
cbar = plt.colorbar()
cbar.set_label("Intensità")

#
plt.title("Nome del grafico")
plt.show()