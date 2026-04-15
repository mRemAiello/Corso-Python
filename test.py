import numpy as np

array = np.array([10, 20, 30, 40, 50])

estratti = np.random.choice(array, size = 3, replace = False)
print(estratti)
