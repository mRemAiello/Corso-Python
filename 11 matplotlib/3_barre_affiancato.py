import numpy as np
from matplotlib import pyplot as plt

width = 0.3

# valori -> [0 1 2 3]
indexs = np.arange(4)
y = [10, 40, 20, 50]
y1 = [20, 20, 15, 80]

#
# 0 -> 10
# 1 -> 40
plt.bar(indexs, y, width=width)


# valori -> [0.4 1.4 2.4 3.4]
# 0.4 -> 20
# 1.4 -> 20
plt.bar(indexs+width+0.1, y1, width=width, color="red")


# Sistemo i "tick"
# valori -> [0.2 1.2 2.2 3.2]
x = ["25", "26", "27", "28"]
plt.xticks((indexs+width/2)+0.05, labels=x)


#
y2 = [0, 20, 40, 60, 80]
yindexs = ["0", "20", "40", "60", "80"]
plt.yticks(y2, labels=yindexs)


#
plt.title("Grafico età / valori")
plt.xlabel("Età")
plt.ylabel("Valori")
plt.legend(["Italiani", "Inglesi"])


# Show
plt.show()