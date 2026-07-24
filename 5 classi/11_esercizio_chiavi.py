# Realizzare 3 classi Chiave (Le chiavi possono essere meccaniche, magnetiche e con microchip)
# con le seguenti caratteristiche :
# descrizione, peso
# Le chiavi magnetiche sono caratterizzate dall'ampiezza, le chiavi meccaniche da un numero di dentelli.
# Sia le chiavi meccaniche che quelle magnetiche sono rappresentate dalla lunghezza.
# Inoltre, esiste un'operazione di aggiornamento per le chiavi con microchip.
# La chiave con microchip avrà un codice seriale (stringa), che verrà aggiornato dalla funzione sopra menzionata.
# Inserire, per ogni classe, una funzione che printa in maniera ordinata tutte le informazioni sulle chiavi
# Infine, inserire una funzione che verifica quale è la chiave più leggera
# Ogni chiave dovrà avere un costruttore che prenda in input tutti i parametri sopracitati.

class Chiave:

    __descrizione = ""
    __peso = 0

    def __init__(self, descrizione, peso):
        self.set_descrizione(descrizione)
        self.set_peso(peso)

    def get_descrizione(self):
        return self.__descrizione

    def set_descrizione(self, descrizione):
        self.__descrizione = str(descrizione)

    def get_peso(self):
        return self.__peso

    def set_peso(self, peso):
        if type(peso) == int:
            self.__peso = peso
        elif peso.isnumeric():
            self.__peso = int(peso)
        else:
            print("Il peso della chiave non è un numero")

    def __str__(self):
        stringa = "Descrizione: {}, Peso: {}"
        return stringa.format(self.get_descrizione(), self.get_peso())


class ChiaveConLunghezza(Chiave):

    __lunghezza = 0

    def __init__(self, descrizione, peso, lunghezza):
        super().__init__(descrizione, peso)
        self.set_lunghezza(lunghezza)

    def set_lunghezza(self, lunghezza):
        if type(lunghezza) == int:
            self.__lunghezza = lunghezza
        elif lunghezza.isnumeric():
            self.__lunghezza = int(lunghezza)
        else:
            print("La lunghezza della chiave non è un numero")

    def get_lunghezza(self):
        return self.__lunghezza

    def __str__(self):
        stringa = super().__str__() + ", Lunghezza: {}"
        return stringa.format(self.get_lunghezza())


class ChiaveMeccanica(ChiaveConLunghezza):

    numero_dentelli = 0

    def __init__(self, descrizione, peso, lunghezza, numero_dentelli):
        super().__init__(descrizione, peso, lunghezza)
        self.numero_dentelli = numero_dentelli

    def __str__(self):
        stringa = super().__str__() + ", Numero dentelli: {}"
        return stringa.format(self.numero_dentelli)


class ChiaveMagnetica(ChiaveConLunghezza):

    ampiezza = 0

    def __init__(self, descrizione, peso, lunghezza, ampiezza):
        super().__init__(descrizione, peso, lunghezza)
        self.ampiezza = ampiezza

    def __str__(self):
        stringa = super().__str__() + ", Ampiezza: {}"
        return stringa.format(self.ampiezza)


class ChiaveConMicrochip(Chiave):

    codice_seriale = ""

    def __init__(self, descrizione, peso, codice_seriale):
        super().__init__(descrizione, peso)
        self.codice_seriale = codice_seriale

    def cambia_seriale(self, codice):
        self.codice_seriale = codice
        print("Codice seriale aggiornato")

    def __str__(self):
        stringa = super().__str__() + ", Codice Seriale: {}"
        return stringa.format(self.codice_seriale)



chiave = ChiaveMagnetica("Chiave di casa", "ciao", 2, 5)
chiave_2 = ChiaveConMicrochip("Chiave cassaforte", 2, "DE44")
chiave_3 = ChiaveMeccanica("Chiave meccanica", 1, 20, 5)

chiave.set_peso("2")


print(chiave)
print(chiave_2)
print(chiave_3)