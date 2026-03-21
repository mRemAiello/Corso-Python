class Impiegato:

    nome = ""
    eta = 0
    id = 0

    # All'inizio sempre init
    def __init__(self, nome, eta, int_id):
        self.nome = nome
        self.eta = eta
        self.id = int_id

    # Qua le tue funzioni

    # Alla fine __str__
    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Età: {self.eta}"


impiegato1 = Impiegato('Marco', 20, 1101)
# print(impiegato1) -> impiegato.__str__() -> print
print(impiegato1)
impiegato2 = Impiegato("Luca", 30, 1102)
print(impiegato2)