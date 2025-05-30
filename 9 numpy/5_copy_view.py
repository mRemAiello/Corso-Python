import numpy as np

# View e copy, come due fotocopie
arr = np.array([1, 2, 3])

# Copy
arr2 = arr.copy()
arr[0] = 10

print("arr:", arr)
print("arr2:", arr2)
print()


# View
# arr3 -> arr -> [10, 2, 3]
# arr2 -> [1, 2, 3]
arr3 = arr.view()
arr[1] = 10

print("arr:", arr)
print("arr2:", arr2)
print("arr3", arr3)
print()

#
arr[2] = 5
print("arr:", arr)
print("arr2:", arr2)
print("arr3", arr3)
print()

# Check
print("arr:", arr.base)
print("arr2:", arr2.base)
print("arr3", arr3.base)