import numpy as np

# 1 Dimensione
array1D = np.array([1, 2, 3])

# Dimensione 2: matrici
array2D = np.array([[1, 2, 3],
                    [4, 5, 6]])

# Dimensione 3
array3D = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Iterazione
for x in array1D:
    print(x)
print()

for x in array2D:
    for y in x:
        print(y)
print()

for x in array3D:
    for y in x:
        for z in y:
            print(z)
print()

# Oppure soluzione rapida
for x in np.nditer(array3D):
    print(x)
print()

for x in np.nditer(array3D, flags=["buffered"], op_dtypes=["S"]):
    print(x)