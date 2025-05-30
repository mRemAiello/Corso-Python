class Studente:

    # Public
    nome = ""

    # Protected
    _cognome = ""

    # Private
    __id = ""
    __materie = []

    # soldi sul conto
    __soldi = 0

    # constructor
    def __init__(self, id, nome, cognome, soldi):
        self.__id = id
        self.nome = nome
        self._cognome = cognome
        self.__soldi = soldi

    def aggiungi_materia(self, materia):
        self.__materie.append(materia)

    def preleva(self, soldi):
        if soldi <= 0:
            print("Non puoi prelevare soldi inferiori o uguali a 0")
            return

        if self.__soldi < soldi:
            print("Non hai abbastanza soldi sul conto")
            return

        self.__soldi -= soldi
        print(f"Hai prelevato {soldi} soldi")

    def get_nome_completo(self):
        return f"{self.nome} {self._cognome}"

    def get_soldi(self):
        return int(self.__soldi)

    def get_id(self):
        if len(self.__id) == 1:
            return "XXX00" + self.__id
        elif len(self.__id) == 2:
            return "XXX0" + self.__id
        return "XXX" + self.__id


studente = Studente("119", "Mirko", "Rossi", 1000)

print(studente.get_nome_completo())

# studente -> soldi -> -2000
# studente -> preleva(2000) -> soldi = 0 -> 1000

studente.preleva(500)
studente.preleva(-200)
print(studente.get_soldi())

#
print(studente.get_id())

# Public
studente.nome = "Mirko"
print(studente.nome)

# Protected
print(studente._cognome)

# Private
# print(studente.__id)