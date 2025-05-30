from matplotlib import pyplot as plt
import numpy as np

file = open("snakes_count_1000.csv", "r", encoding="utf8")

file.readline()

y = [0, 0]

for riga in file:
    dati = riga.split(",")
    lunghezza = int(dati[1])
    if lunghezza >= 0 and lunghezza <= 20:
        y[0] = y[0] + 1
    if lunghezza > 21:
        y[1] = y[1] + 1


# Mostro i dati
width = 0.3

indexs = np.arange(2)
x = [">= 0, <= 20", "> 21"]

print(indexs)
print((indexs+width/2)+0.05)

#
plt.bar(indexs, y, width=width)
#plt.bar(indexs+width+0.1, y1, width=width)

# Sistemo i "tick"
plt.xticks((indexs+width/2)+0.05, labels=x)

plt.title("Grafico età / valori")
plt.xlabel("Età")
plt.ylabel("Valori")
plt.legend(["Italiani", "Inglesi"])

# SHow
plt.show()