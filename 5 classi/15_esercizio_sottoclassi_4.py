# Scrivi una classe Forma che abbia un metodo calcola_area() che calcoli l’area della forma.
# Poi crea le classi Quadrato, Cerchio, Triangolo che ereditino dalla classe Forma
# e che implementino il metodo calcola_area() e calcola_perimetro in modo appropriato per ogni forma.
# Utilizza le classi create per creare un quadrato e un cerchio, quindi stampa l’area di ognuno di essi.

class Forma:

    def calcola_area(self):
        return 0


class Quadrato(Forma):

    __lato = 0

    def __init__(self, lato):
        self.__lato = lato

    def calcola_area(self):
        return self.__lato * self.__lato

    def __str__(self):
        stringa = "Quadrato di lato {}, area: {}"
        return stringa.format(self.__lato, self.calcola_area())


class Cerchio(Forma):

    __raggio = 0

    def __init__(self, raggio):
        self.__raggio = raggio

    def calcola_area(self):
        return 3.14 * self.__raggio * self.__raggio

    def __str__(self):
        stringa = "Cerchio di raggio {}, area: {}"
        return stringa.format(self.__raggio, self.calcola_area())


class Triangolo(Forma):

    __base = 0
    __altezza = 0

    def __init__(self, base, altezza):
        self.__base = base
        self.__altezza = altezza

    def calcola_area(self):
        return self.__base * self.__altezza / 2

    def __str__(self):
        stringa = "Triangolo di base {} e altezza {}, area: {}"
        return stringa.format(self.__base, self.__altezza, self.calcola_area())


lato = int(input("Scrivi la grandezza di un lato: "))
raggio = int(input("Scrivi il raggio: "))
base = int(input("Scrivi una base: "))
altezza = int(input("Scrivi un'altezza: "))

quadrato = Quadrato(lato)
cerchio = Cerchio(raggio)
triangolo = Triangolo(base, altezza)

print(quadrato)
print(cerchio)
print(triangolo)