# Scrivere una classe Docente che rappresenti le seguenti informazioni relative ad un docente: nome, cognome, codice ed età, e che
# contenga il costruttore parametrizzato ed i metodi getCodice, getCognome e getEta che restituiscono
# rispettivamente il codice, il cognome e l’età del docente.
# Scrivere poi una classe Universita, che rappresenti un insieme di docenti universitari tramite una lista di tipo Docente,
# e che contenga il costruttore parametrizzato ed un
# metodo GetEtaMinima che restituisce la minima età tra i docenti universitari.
# Inserire poi nella classe Universita il metodo TrovaGiovani che restituisca il cognome del docente che ha età minima.


class Docente:

    nome = ""
    cognome = ""
    cognome_2 = ""
    codice = ""
    eta = 0

    def __init__(self, nome, cognome, cognome_2, codice, eta):
        self.nome = nome
        self.cognome = cognome
        self.cognome_2 = cognome_2
        self.codice = codice
        self.eta = eta

    def getNome(self):
        return self.nome

    def getCognome(self):
        return self.cognome + " " + self.cognome_2

    def getCodice(self):
        return str(self.codice)

    def getEta(self):
        return int(self.eta)

    def __str__(self):
        string = "Nome: {}, Cognome: {}, Codice: {}, Età: {}"
        return string.format(self.getNome(), self.getCognome(), self.getCodice(), self.getEta())


class Universita:

    docenti = []

    def __init__(self):
        self.docenti = []

    def aggiungi_docente(self, docente):
        self.docenti.append(docente)

    def find_eta_minima(self):
        docente = self.docenti[0]
        for element in self.docenti:
            if element.getEta() < docente.getEta():
                docente = element

        return docente.getEta()

    def find_docente_piu_giovane(self):
        eta_minima = self.find_eta_minima()
        lista = []
        for docente in self.docenti:
            if docente.getEta() == eta_minima:
                lista.append(docente)

        return lista


"""docente_1 = Docente("Mirko", "Aiello", "Aiello 2", "1", 32)
docente_2 = Docente("Marco", "Rossi", "Rossi", "2", 32)
docente_3 = Docente("Mario", "Biondi", "", "3", 45)

universita = Universita()
universita.aggiungi_docente(docente_1)
universita.aggiungi_docente(docente_2)
universita.aggiungi_docente(docente_3)

lista = universita.find_docente_piu_giovane()
for docente in lista:
    print(docente.getCognome())"""



# Scrivete un programma per convertire la lettera di un voto scolastico nel numero corrispondente.
# Le lettere sono A, B, C, D e F, eventualmente seguite dai segni + o -. I loro valori numerici sono 4, 3, 2, 1 e 0. F+ e F- non esistono.
# Un segno + o – incrementa o decrementa il valore numerico di 0.3. Tuttavia, A+ è uguale a 4.0. Usate una classe Grade con un metodo getNumericGrade.
# Chiedere quindi voti all'utente all'ìnfinito finchè non scrive "Esci" (while)

class Grade:

    voti = {
        "A+": 4,
        "A-": 3.7,
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "F": 0
    }

    # Metodo migliore
    def getNumericGrade_2(self, voto):

        if not 1 <= len(voto) <= 2:
            return "Voto scritto in maniera errata"

        voto_2 = voto.upper()

        voto_numerico = 0
        if voto_2 in self.voti:
            return self.voti[voto_2]
        else:
            return "Voto scritto in maniera errata"

    # Metodo più articolato
    def getNumericGrade(self, voto):

        if not 1 <= len(voto) <= 2:
            return "Voto scritto in maniera errata"

        prima_lettera = voto.upper()
        prima_lettera = prima_lettera[0]

        voto_numerico = 0
        if prima_lettera in self.voti:
            voto_numerico = self.voti[prima_lettera]
        else:
            return "Voto scritto in maniera errata"

        if len(voto) == 1:
            return voto_numerico
        else:
            seconda_lettera = voto.upper()
            seconda_lettera = seconda_lettera[1]
            if seconda_lettera == "+":
                if not prima_lettera == "A" and not prima_lettera == "F":
                   voto_numerico += 0.3
            elif seconda_lettera == "-":
                if not prima_lettera == "F":
                    voto_numerico -= 0.3
            else:
                return "Voto scritto in maniera errata"

        return voto_numerico


"""grade = Grade()
comando = input("Scrivi un voto americano o Esci: ")
while not comando == "Esci":

    print(grade.getNumericGrade_2(comando))
    print()

    comando = input("Scrivi un voto americano o Esci: ")"""




# Realizzare 3 classi Chiave (Le chiavi possono essere meccaniche, magnetiche e con microchip) con le seguenti caratteristiche :
# descrizione, peso
# Le chiavi magnetiche sono caratterizzate dall'ampiezza, le chiavi meccaniche da un numero di dentelli.
# Sia le chiavi meccaniche che quelle magnetiche sono rappresentate dalla lunghezza.
# Inoltre, esiste un'operazione di aggiornamento per le chiavi con microchip.
# La chiave con microchip avrà un codice seriale (stringa), che verrà aggiornato dalla funzione sopra menzionata.
# Inserire, per ogni classe, una funzione che printa in maniera ordinata tutte le informazioni sulle chiavi
# Infine, inserire una funzione che verifica quale è la chiave più leggera
# Ogni chiave dovrà avere un costruttore che prenda in input tutti i parametri sopracitati.


class ChiaveMeccanica:

    descrizione = ""
    peso = 0
    numero_dentelli = 0
    lunghezza = 0

    def __init__(self, descrizione, peso, numero_dentelli, lunghezza):
        self.descrizione = descrizione
        self.peso = peso
        self.numero_dentelli = numero_dentelli
        self.lunghezza = lunghezza

    def __str__(self):
        stringa = "Descrizione: {}, Peso: {}, Dentelli: {}, Lunghezza: {}"
        return stringa.format(self.descrizione, self.peso, self.numero_dentelli, self.lunghezza)


class ChiaveMagnetica:

    descrizione = ""
    peso = 0
    ampiezza = 0
    lunghezza = 0

    def __init__(self, descrizione, peso, ampiezza, lunghezza):
        self.descrizione = descrizione
        self.peso = peso
        self.ampiezza = ampiezza
        self.lunghezza = lunghezza

    def __str__(self):
        stringa = "Descrizione: {}, Peso: {}, Ampiezza: {}, Lunghezza: {}"
        return stringa.format(self.descrizione, self.peso, self.ampiezza, self.lunghezza)


class ChiaveConMicrochip:

    descrizione = ""
    peso = 0
    codice_seriale = ""

    def __init__(self, descrizione, peso, codice_seriale):
        self.descrizione = descrizione
        self.peso = peso
        self.codice_seriale = codice_seriale

    def cambia_seriale(self, codice_seriale):
        self.codice_seriale = codice_seriale.strip().replace("\n", "").upper()

    def __str__(self):
        stringa = "Descrizione: {}, Peso: {}, Codice Seriale: {}"
        return stringa.format(self.descrizione, self.peso, self.codice_seriale)


def chiave_piu_leggera_2(lista):

    minimo = lista[0]
    for elemento in lista:
        if elemento.peso < minimo.peso:
            minimo = elemento

    lista_2 = lista.copy()
    lista_2.remove(minimo)
    secondo_minimo = lista_2[0]
    for elemento in lista_2:
        if elemento.peso < secondo_minimo.peso:
            secondo_minimo = elemento

    return minimo, secondo_minimo


# Sort e 0/1
def chiave_piu_leggera(lista):

    minimo = lista[0]
    secondo_minimo = lista[0]
    for element in lista:
        if element.peso < minimo.peso:
            secondo_minimo = minimo
            minimo = element
        elif element.peso < secondo_minimo.peso and not element.peso == minimo.peso:
            secondo_minimo = element

    return minimo, secondo_minimo


chiave_2 = ChiaveMagnetica("E' una chiave magnetica", 3, 3, 0.3)
chiave_3 = ChiaveConMicrochip("E' una chiave con microchip", 5, "XRT00001")
chiave_4 = ChiaveConMicrochip("Sblocca tutte le porte", 2, "02XXX2")
chiave_1 = ChiaveMeccanica("E' una chiave meccanica", 7, 3, 0.5)


"""print(chiave_1)
print(chiave_2)
print(chiave_3)
print()"""

# codice_seriale = input("Inserisci un nuovo seriale: ")
# chiave_3.cambia_seriale(codice_seriale)

lista = chiave_piu_leggera_2([chiave_2, chiave_1, chiave_4, chiave_3])
"""for element in lista:
    print(element)"""




# In questo esercizio, abbiamo definito due classi, Studente e Corso. La classe Studente rappresenta uno studente universitario con
# attributi come nome, cognome e matricola, oltre a un metodo per aggiungere corsi al suo elenco di corsi.
# La classe Corso rappresenta un corso universitario con attributi come nome e codice.
# Successivamente, abbiamo creato due oggetti Studente e tre oggetti Corso e abbiamo aggiunto i corsi agli studenti.txt.
# Infine, abbiamo stampato l'elenco dei corsi per ciascuno studente.


# In questo esempio, abbiamo definito due classi: Paziente e VisitaMedica.
# La classe Paziente rappresenta un paziente con attributi come nome, cognome, data di nascita e codice fiscale.
# Ha un metodo per aggiungere visite mediche all'elenco delle visite mediche del paziente e un metodo per elencare le visite mediche.
# La classe VisitaMedica rappresenta una visita medica con attributi come data, medico e diagnosi.
# La sua rappresentazione testuale è personalizzata tramite il metodo __str__.
# Abbiamo creato vari oggetti Paziente e VisitaMedica, aggiunto le visite mediche ai pazienti e poi stampato l'elenco delle visite mediche per ciascun paziente.


# Scrivere una classe Libro che rappresenti le seguenti informazioni relative ad un libro: titolo, autore, prezzo,
# e che contenga il costruttore parametrizzato ed
# i metodi getTitolo, getAutore e getPrezzo che restituiscono rispettivamente il titolo, l'autore e il prezzo del libro.
# Scrivere poi una classe Libreria, che rappresenti un insieme di libri tramite una lista di tipo Libro (che contenga il costruttore parametrizzato),
# ed un metodo Trova (che accetta in ingresso un autore a e intero k) e restituisce il numero di libri contenuti nella libreria aventi
# autore a e prezzo superiore a k.
# Aggiungere alla classe Libreria un metodo che accetti un autore a e restituisca i titoli di tutti i libri scritti dall’autore a.

class Libro:

    __titolo = ""
    __autore = ""
    __prezzo = 0

    def __init__(self, titolo, autore, prezzo):
        self.__titolo = titolo
        self.__autore = autore
        self.__prezzo = prezzo
        if self.__prezzo < 0:
            self.__prezzo = 0

    def get_titolo(self):
        return self.__titolo

    def get_autore(self):
        return self.__autore

    def get_prezzo(self):
        return float(self.__prezzo)

    def set_prezzo(self, prezzo):
        self.__prezzo = float(prezzo)
        if self.__prezzo < 0:
            self.__prezzo = 0

    def __str__(self):
        stringa = "Titolo: {}, Autore: {}, Prezzo: {}"
        return stringa.format(self.__titolo, self.__autore, self.__prezzo)


class Libreria:

    __libri = {}

    def __init__(self):
        self.__libri = {}

    def aggiungi_libro(self, libro):
        if libro.get_titolo() in self.__libri:
            return
        self.__libri[libro.get_titolo()] = libro

    def cerca_libro_per_autore_e_prezzo(self, autore, prezzo=-1):
        libri = []
        for libro in self.__libri.values():
            if libro.get_autore() == autore and libro.get_prezzo() > prezzo:
                libri.append(libro)

        return libri

    def cerca_libro_per_autore(self, autore):
        return self.cerca_libro_per_autore_e_prezzo(autore, -1)



libro_1 = Libro("Signore degli anelli", "Tolkien", 9.99)
libro_2 = Libro("Cronache del ghiaccio e del fuoco", "JRR Martin", 8.99)
libro_3 = Libro("XX", "Tolkien", 10.99)
libro_4 = Libro("XX2", "Tolkien", -1)

libreria = Libreria()
libreria.aggiungi_libro(libro_1)
libreria.aggiungi_libro(libro_2)
libreria.aggiungi_libro(libro_3)
libreria.aggiungi_libro(libro_4)

prezzo = libro_4.get_prezzo()
prezzo = 10
print(prezzo)

lista = libreria.cerca_libro_per_autore("Tolkien")
for element in lista:
    print(element)