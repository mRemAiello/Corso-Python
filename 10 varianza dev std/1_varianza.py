from numpy import var
import numpy as np
import statistics

data = np.random.randn(100)

# Varianza
x = var(data)

# Dev Standard
y = statistics.stdev(data)

#
print(x)
print(y)
print()

print(data)
print()

sum_data = np.sum(data)
mean_data = np.mean(data)
std_data = np.std(data)
var_data = np.var(data)

print("Somma:", sum_data)
print("Media:", mean_data)
print("Deviazione standard:", std_data)
print("Varianza:", var_data)



# Correlazione

# Media mobile

# Analisi serie storiche