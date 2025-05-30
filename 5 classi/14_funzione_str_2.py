class Prodotto:
    nome = "    Mela    "
    prezzo = 0
    scorta = 0
    prezzo_scontato = 0

    def __str__(self):
        return f"Nome: {self.nome.strip()} Prezzo: {self.prezzo} Prezzo Scontato: {self.prezzo_scontato} Scorta: {self.scorta}"


class GestoreMagazzino:

    nome = "Magazzino della frutta"

    dict = {
        "mela": Prodotto(),
        "pera": Prodotto()
    }

    def __str__(self):
        stringa = "Nome: " + self.nome + "\n"
        i = 0
        for elemento in self.dict.values():
            stringa += "ID: " + str(i) + " " + elemento.__str__() + "\n"
            i += 1
        return stringa


p1 = Prodotto()
print(p1)

g1 = GestoreMagazzino()
print(g1)