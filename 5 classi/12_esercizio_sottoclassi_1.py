#     Creare una classe chiamata Persona con le seguenti proprietà:
#         nome (string): il nome della persona.
#         cognome (string): il cognome della persona.
#         eta (int): l'età della persona.
#         email (string): l'indirizzo email della persona.
#
#     Creare una classe chiamata Studente che erediti dalla classe Persona e abbia le seguenti proprietà aggiuntive:
#         matricola (string): il numero di matricola dello studente.
#         anno_corso (int): l'anno di corso dello studente.
#
#     Creare due sottoclassi di Studente chiamate StudenteTriennale e StudenteMagistrale,
#     che abbiano proprietà specifiche come il corso di laurea e il voto di laurea (applicabile solo per studenti magistrali).
#
#     Creare una classe chiamata Docente con le seguenti proprietà:
#         id_docente (string): un identificatore unico per il docente.
#         materia_insegnata (string): la materia insegnata dal docente.
#
#     Creare una classe chiamata Inserviente con le seguenti proprietà:
#         id_inserviente (string): un identificatore unico per l'inserviente.
#         ruolo (string): il ruolo dell'inserviente (ad esempio, "custode", "segretaria", "tecnico").
#
# Creare una classe chiamata Segreteria con le seguenti funzioni:
#   registra_studente(studente): registra uno studente nel sistema universitario.
#   registra_docente(docente): registra un docente nel sistema universitario.
#   registra_inserviente(inserviente): registra un inserviente nel sistema universitario.
#   trova_persona(email): restituisce una persona (studente, docente o inserviente) in base all'indirizzo email fornito.
#   elenco_studenti(): stampa l'elenco di tutti gli studenti registrati.
#   elenco_docenti(): stampa l'elenco di tutti i docenti registrati.
#   elenco_inservienti(): stampa l'elenco di tutti gli inservienti registrati.


class Segreteria:

    studenti = []
    docenti = []
    inservienti = []

    def __init__(self):
        self.studenti = []
        self.docenti = []
        self.inservienti = []

    def registra_studente(self, studente):
        self.studenti.append(studente)

    def registra_studenti(self, studenti):
        for studente in studenti:
            self.registra_studente(studente)

    def registra_docente(self, doc):
        self.docenti.append(doc)

    def registra_inserviente(self, ins):
        self.inservienti.append(ins)

    def trova_persona(self, email):
        for studente in self.studenti:
            if studente.email == email:
                return studente

        for doc in self.docenti:
            if doc.email == email:
                return doc

        for ins in self.inservienti:
            if ins.email == email:
                return ins

        return "Persona non trovata"

    def elenco_studenti(self):
        for studente in self.studenti:
            studente.info()
            print()

    def elenco_docenti(self):
        for doc in self.docenti:
            doc.info()
            print()

    def elenco_inservienti(self):
        for ins in self.inservienti:
            ins.info()
            print()


class Persona:

    nome = ""
    cognome = ""
    eta = 0
    email = ""

    def __init__(self, nome, cognome, eta, email):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.email = email

    def info(self):
        print("Nome:", self.nome)
        print("Cognome:", self.cognome)
        print("Eta", self.eta)
        print("Email:", self.email)


class Studente(Persona):

    matricola = ""
    anno_corso = 0

    def __init__(self, nome, cognome, eta, email, matricola, anno_corso):
        super().__init__(nome, cognome, eta, email)
        self.matricola = matricola
        self.anno_corso = anno_corso

    def info(self):
        super().info()
        print("Matricola:", self.matricola)
        print("Anno di corso:", self.anno_corso)


class StudenteTriennale(Studente):

    corso_laurea = ""

    def __init__(self, nome, cognome, eta, email, matricola, anno_corso, corso_laurea):
        super().__init__(nome, cognome, eta, email, matricola, anno_corso)
        self.corso_laurea = corso_laurea

    def info(self):
        super().info()
        print("Corso di Laurea:", self.corso_laurea)


class StudenteMagistrale(StudenteTriennale):

    voto_laurea = 0

    def __init__(self, nome, cognome, eta, email, matricola, anno_corso, corso_laurea, voto_laurea):
        super().__init__(nome, cognome, eta, email, matricola, anno_corso, corso_laurea)
        self.voto_laurea = voto_laurea

    def info(self):
        super().info()
        print("Voto di laurea: ", self.voto_laurea)


class PersonaID(Persona):

    persona_id = 0

    def __init__(self, nome, cognome, eta, email, persona_id):
        super().__init__(nome, cognome, eta, email)
        self.persona_id = persona_id

    def info(self):
        super().info()
        print("ID:", self.persona_id)


class Docente(PersonaID):

    materia = ""

    def __init__(self, nome, cognome, eta, email, persona_id, materia):
        super().__init__(nome, cognome, eta, email, persona_id)
        self.materia = materia

    def info(self):
        super().info()
        print("Materia di insegnamento:", self.materia)


class Inserviente(PersonaID):

    ruolo = ""

    def __init__(self, nome, cognome, eta, email, persona_id, ruolo):
        super().__init__(nome, cognome, eta, email, persona_id)
        self.ruolo = ruolo

    def info(self):
        super().info()
        print("Ruolo:", self.ruolo)


stud_triennale = StudenteTriennale("Mirko", "Aiello", 20, "info@email.it", 1, 1, "Informatica")
stud_magistrale = StudenteMagistrale("Mirko", "Aiello", 25, "info@email.it", 1,
                                        1, "Informatica Magistrale", 110)

docente = Docente("Marco", "Rossi", 40, "marco.rossi@email.it", 10, "Informatica")
inserviente = Inserviente("Antonio", "Verdi", 45, "ant.verdi@email.it", 11, "Segretario")


segreteria = Segreteria()

segreteria.registra_studenti([stud_triennale, stud_magistrale])
segreteria.registra_docente(docente)
segreteria.registra_inserviente(inserviente)

segreteria.elenco_studenti()
segreteria.elenco_inservienti()
segreteria.elenco_docenti()

stud = segreteria.trova_persona("info@email.it")
stud.info()
print()

stud2 = segreteria.trova_persona("no@email.it")
print(stud2)