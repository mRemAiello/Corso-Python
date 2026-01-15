import numpy as np


print("=== INTERI ===")

# Intero a 1 byte (int8)
arr_int8 = np.array([1, 2, 3], dtype='int8')
print("int8:", arr_int8, "| itemsize:", arr_int8.itemsize, "byte")

# Intero a 2 byte (int16)
arr_int16 = np.array([1, 2, 3], dtype='int16')
print("int16:", arr_int16, "| itemsize:", arr_int16.itemsize, "byte")

# Intero standard (int32)
arr_int32 = np.array([1, 2, 3], dtype='int32')
print("int32:", arr_int32, "| itemsize:", arr_int32.itemsize, "byte")

# Intero a 64 bit
arr_int64 = np.array([1, 2, 3], dtype='int64')
print("int64:", arr_int64, "| itemsize:", arr_int64.itemsize, "byte")



print("\n=== FLOAT ===")

# Float 32-bit
arr_float32 = np.array([1.5, 2.5, 3.5, 4, 5], dtype='float32')
print("float32:", arr_float32, "| itemsize:", arr_float32.itemsize, "byte")

# Float 64-bit (default in NumPy)
arr_float64 = np.array([1.5, 2.5, 3.5, 4, 5], dtype='float64')
print("float64:", arr_float64, "| itemsize:", arr_float64.itemsize, "byte")
print("Consumo complessivo", arr_float64.nbytes)



print("\n=== BOOLEAN ===")

# Booleani
arr_bool = np.array([True, False, True], dtype='bool')
print("bool:", arr_bool, "| itemsize:", arr_bool.itemsize, "byte")



print("\n=== STRINGHE ===")

# Stringa a 1 byte per carattere
arr_str = np.array(['a', 'b', 'c'], dtype='S1')
print("S1:", arr_str, "| itemsize:", arr_str.itemsize, "byte")
print("Consumo complessivo: ", arr_str.nbytes, "bytes")

# Stringa con lunghezza massima di 4 caratteri
arr_str4 = np.array(['ciao', 'test', 'dato'], dtype='S4')
print("S4:", arr_str4, "| itemsize:", arr_str4.itemsize, "byte")
print("Consumo complessivo: ", arr_str4.nbytes, "bytes")
