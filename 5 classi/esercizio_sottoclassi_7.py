# Classe Veicolo

# Classe Veicolo Acquatico
# Classe Veicolo Terrestre
# Classe Veicolo Volante

# Veicolo Totale che ha le abilità dei 3 veicoli

class Veicolo:

    __nome = ""
    __modello = ""
    __marca = ""

    def __init__(self, nome, modello, marca):
        self.__nome = nome
        self.__modello = modello
        self.__marca = marca

    def __str__(self):
        return f"{self.__marca} {self.__modello} {self.__nome}"


class VeicoloAcquatico(Veicolo):

    __tipo_scafo = ""

    def __init__(self, nome, modello, marca, tipo_scafo):
        super().__init__(nome, modello, marca)
        self.__tipo_scafo = tipo_scafo

    def get_tipo_scafo(self):
        return self.__tipo_scafo

    def __str__(self):
        return f"{super().__str__()}, Scafo: {self.__tipo_scafo}"


class VeicoloTerrestre(Veicolo):

    __cilindrata = 0

    def __init__(self, nome, modello, marca, cilindrata):
        super().__init__(nome, modello, marca)
        self.__cilindrata = cilindrata

    def get_cilindrata(self):
        return self.__cilindrata

    def __str__(self):
        return f"{super().__str__()}, Cilindrata: {self.__cilindrata}"


class VeicoloVolante(Veicolo):

    __potenza_elica = ""

    def __init__(self, nome, modello, marca, potenza_elica):
        super().__init__(nome, modello, marca)
        self.__potenza_elica = potenza_elica

    def get_potenza_elica(self):
        return self.__potenza_elica

    def __str__(self):
        return f"{super().__str__()}, Potenza Elica: {self.__potenza_elica}"


class VeicoloTotale(Veicolo):

    __veicolo_terrestre = None
    __veicolo_acquatico = None
    __veicolo_volante = None

    def __init__(self, nome, modello, marca, tipo_scafo, cilindrata, potenza_elica):
        super().__init__(nome, modello, marca)
        self.__veicolo_terrestre = VeicoloTerrestre(nome, modello, marca, cilindrata)
        self.__veicolo_acquatico = VeicoloAcquatico(nome, modello, marca, tipo_scafo)
        self.__veicolo_volante = VeicoloVolante(nome, modello, marca, potenza_elica)

    def __str__(self):
        stringa = f"{super().__str__()}, Potenza Elica: {self.__veicolo_volante.get_potenza_elica()}"
        stringa += f", Cilindrata: {self.__veicolo_terrestre.get_cilindrata()}"
        stringa += f", Scafo: {self.__veicolo_acquatico.get_tipo_scafo()}"
        return stringa


veicolo1 = Veicolo("Sportiva", "Panda", "Fiat")
print(veicolo1)
veicolo2 = VeicoloAcquatico("Marino", "Panda", "Fiat", "Potente")
print(veicolo2)
veicolo3 = VeicoloTerrestre("Terra", "Panda", "Fiat", 1200)
print(veicolo3)
veicolo4 = VeicoloVolante("Volante", "Panda", "Fiat", 4000)
print(veicolo4)
veicolo5 = VeicoloTotale("Global", "Panda", "Fiat", "Medio", 1600, 4500)
print(veicolo5)