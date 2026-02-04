def funzione(a, b, c, d):
    return (a + c) * (d + b)


# Equivalente
# funzione(4, 3, 2, 1)
funzione(c=2, a=4, b=3, d=1)


# Viene avviata così
a = 1
b = 2
c = 3
d = 4
funzione(d, b, c, a)

# funzione(4, 2, 3, 1) -> a = 4, b = 2, c = 3, d = 1