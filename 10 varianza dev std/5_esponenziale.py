import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import t


def exp_0_5(x):
    # Lamba
    lmb = 0.5
    if x > 0:
        return lmb * np.e ** (-lmb * x)
    return 0


def exp_1(x):
    # Lamba
    lmb = 1
    if x > 0:
        return lmb * np.e ** (-lmb * x)
    return 0


def exp_1_5(x):
    # Lamba
    lmb = 1.5
    if x > 0:
        return lmb * np.e ** (-lmb * x)
    return 0


# UFunc della funzione esponenziale
f_exp_0_5 = np.frompyfunc(exp_0_5, 1, 1)
f_exp_1 = np.frompyfunc(exp_1, 1, 1)
f_exp_1_5 = np.frompyfunc(exp_1_5, 1, 1)


#
x = np.arange(0.1, 5, 0.1)
y = f_exp_0_5(x)
y1 = f_exp_1(x)
y2 = f_exp_1_5(x)


plt.plot(x, y, label="F. Exp lamba 0.5")
plt.plot(x, y1, label="F. Exp lamba 1")
plt.plot(x, y2, label="F. Exp lamba 1.5")

plt.title("Distribuzione esponenziale")
plt.legend(["F. Exp lamba 0.5", "F. Exp lamba 1", "F. Exp lamba 1.5"])

#
plt.grid()
plt.show()