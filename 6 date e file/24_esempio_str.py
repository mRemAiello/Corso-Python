x = ["  SIGNORE DEGLI ANELLI, Tolkien,   1900", "  trono di spade, martin, 2000"]

# 0  Nome                    Autore     Anno di uscita
# 1  Signore degli Anelli    Tolkien    1900
# 2  Trono di Spade          Martin     2000


for element in x:
    y = element.split(",")
    y[0] = y[0].strip().capitalize()
    y[1] = y[1].strip().capitalize()
    y[2] = int(y[2].strip())
    print(y)