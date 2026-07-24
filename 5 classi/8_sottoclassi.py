# Superclasse
class Persona:

    # Proprietà
    nome = 'Luca'
    cognome = 'Rossi'
    eta = 20
    codice_fiscale = ""
    luogo_di_nascita = ""

    # Costruttore
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.codice_fiscale = ""

    def imposta_luogo_di_nascita(self, luogo):
        self.luogo_di_nascita = luogo

    # Metodo della classe
    def saluta(self):
        print("Saluta di Persona")

    def __str__(self):
        stringa = f"Nome: {self.nome}, Cognome: {self.cognome}, Età: {self.eta}"
        return stringa


# Sottoclasse
class Studente(Persona):

    matricola = ""
    materie = []

    # Costruttore
    def __init__(self, nome, cognome, eta, matricola):
        super().__init__(nome, cognome, eta)
        self.matricola = matricola

    def vai_a_lezione(self):
        print("Lo studente va a lezione")

    def saluta(self):
        print("Saluta di Studente")

    def __str__(self):
        stringa = super().__str__()
        stringa += f", Matricola: {self.matricola}"
        return stringa


class Dipendente(Persona):

    id_azienda = ""

    def __init__(self, nome, cognome, eta, id_azienda):
        super().__init__(nome, cognome, eta)
        self.id_azienda = id_azienda

    def __str__(self):
        stringa = super().__str__()
        stringa += f", ID: {self.id_azienda}"
        return stringa


class Dirigente(Dipendente):

    ruolo_aziendale = ""

    def __init__(self, nome, cognome, eta, id_azienda, ruolo):
        super().__init__(nome, cognome, eta, id_azienda)
        self.ruolo_aziendale = ruolo


#
persona = Persona('Luca', 'Rossi', 20)
studente = Studente('Antonio', 'Rossi', 25, "01")
dipendente = Dipendente("Luca", "Verdi", 30, "m0111")
dirigente = Dirigente("Antonio", "Rossi", 30, "m0111", "Senior Sales Manager")

# Saluta e vai a lezione
persona.saluta()
studente.saluta()
dipendente.saluta()
dirigente.saluta()
print()
print()

# Print
print(persona)
print(studente)
print(dipendente)
print(dirigente)