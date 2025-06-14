# Minimo di un gruppo di numeri
x = min(1, 2, 3)
print(x)

# Vale anche per le liste
y = [1, 2, 3, 5]
print(min(y))

# Massimo
x = max(1, 2, 3)
print(x)

# Massimo di una lista
x = [1, 2, 3, 4, 5]
print(max(x))

# Valore assoluto
x = abs(-10)
print(x)

# Potenza
x = pow(4, 3)
print(x)

# Altre funzioni più complesse hanno bisogno del modulo math
import math

# Radice quadrata
x = math.sqrt(64)
print(x)

# Ceil arrotonda per eccesso, floor per difetto
x = math.ceil(50.80)
y = math.floor(50.80)
print(x, y)

# Pi greco
print(math.pi)

#
print(math.sin(1))

# Infinito
x = math.inf
print(x)

# Recap
print(dir(math))