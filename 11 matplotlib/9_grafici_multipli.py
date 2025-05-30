from matplotlib import pyplot as plt

plt.style.use("ggplot")

# Subplot
#fig, gf1 = plt.subplots()

# Crea x subplots
# Sharex condivide gli assi ed evita di ripeterli
# 1 riga 2 colonne => (gf1, gf2)
# 2 righe 2 colonne => ((gf1, gf2), (gf3, gf4))
# 1 riga 4 colonne => (gf1, gf2, gf3, gf4)
fig, (gf1, gf2, gf3, gf4) = plt.subplots(nrows=1, ncols=4, sharex=True)

x = [1, 2, 3, 4, 5, 6]
y = [3, 6, 7, 2, 5, 1]
y1 = [4, 5, 8, 10, 12, 14]

gf1.plot(x, y)
gf1.plot(x, y1)
gf1.set_title("Grafico 1")
gf1.set_xlabel("Prova")

# Plot 2
gf2.plot(x, y1)
gf2.set_title("Grafico 2")
gf2.set_xlabel("Prova 2")

# Mostro tutto
plt.show()