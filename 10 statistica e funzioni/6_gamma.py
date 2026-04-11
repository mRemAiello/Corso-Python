import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t

k = 1
gamma = 2

x = np.arange(0, 100)
y = np.random.gamma(k, scale=gamma)

plt.plot(x, y)
plt.show()