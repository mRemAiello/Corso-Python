# Casting

# Cosa succede
# "5" => 5
x = "5"
# Inverso diventa 5.1 => "5.1"
y = 5.1

# Qui sommo y (int) e x (str) che sono due variabili di tipo differente
# Grazie al casting "trasformo" momentaneamente la y in una stringa
print(x + str(y))

# Operazione momentanea
print(type(y))

z = "5"
z = float(z) + 10
print(z)

# Altre operazioni di casting
z = int(y)
print(z)

x = str(x)
print(x)

x = 5
x = float(x)
print(x)

booleano = 0
x = bool(booleano)
print(x)