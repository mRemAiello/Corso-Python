class Persona:

    # Proprietà
    nome = ""
    cognome = ""
    codice_fiscale = ""
    eta = 0
    anno_di_nascita = 0

    # Costruttore
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.codice_fiscale = nome + cognome + str(eta)
        self.anno_di_nascita = 2025 - self.eta

    # Metodo della classe
    def saluta(self, altro_nome):
        print(self.nome + " sta salutando " + altro_nome)


# Persona(...) => __init__(...)
persona1 = Persona('Luca', 'Rossi', 20)
persona2 = Persona('Mirko', 'Verdi', 30)
persona3 = Persona('Antonio', 'Grigi', 25)

#
print(type(persona1))

#
print(persona1)

#
print(persona1.codice_fiscale)
print(persona2.codice_fiscale)


print(persona1.nome)
print(persona2.nome)
print(persona3.nome)

print(persona1.anno_di_nascita)
print(persona2.anno_di_nascita)


persona1.saluta(persona2.nome)
persona2.saluta(persona1.nome)
persona3.saluta(persona3.nome)