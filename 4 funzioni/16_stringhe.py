# Creare una stringa, singolo o doppio apice è uguale
x = "prova"
y = 'prova'

# Print
print(x)

# Multilinea, tripli apici
z = """Ciao
Io
Mi 
Chiamo
Mirko"""

print(z)

z = "Ciao\nIo\nMi\nChiamo\nMirko"

print(z)

# Le stringhe sono liste di caratteri, posso estrarli singolarmente
print(z[0])

# Lunghezza
print(len(z))

# Iterazione della stringa
for elemento in z:
    print(elemento)

# Prendere parte di una stringa
print(x[-3])
print(x[2:5])

# Modificare la stringa
stringa = "   mirko;    aiello;   20; +39 340 "
print(stringa)
stringa = stringa.strip()
print(stringa)

print(stringa.upper())
print(stringa.lower())
print(stringa.capitalize())
print(stringa.strip())
print(stringa.replace("\n", ""))

# Inserire split
x = stringa.split(";")
# x[0] = "   mirko"
# x[1] = "    aiello"
# x[2] = "   20"
# x[3] = " +39 340 "
print(x)

i = 0
while i < len(x):
    x[i] = x[i].replace("+39", "")
    x[i] = x[i].strip()
    x[i] = x[i].capitalize()
    i += 1

# Dopo il while x diventa
# x[0] = "Mirko"
# x[1] = "Aiello"
# x[2] = "20"
# x[3] = "340"

print(x)