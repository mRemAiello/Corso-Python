from matplotlib import pyplot as plt

x = [25, 26, 27, 28]
y = [10, 40, 20, 50]
y1 = [20, 20, 15, 80]


plt.bar(x, y1, label="Francesi", color="black", linewidth=4, linestyle="dotted")
plt.bar(x, y, label="Italiani", color="red", linewidth=2, linestyle="--")

# plt.grid()
plt.show()