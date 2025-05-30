#     Creare una classe Studente con la classe Date e file:
#     Definire una classe Studente con attributi come nome, cognome, data di nascita (utilizzando la classe Date)
#     e voto medio. Crea alcuni oggetti studente e stampa le loro informazioni.
#     Inoltre, salva le informazioni degli studenti.txt in un file di testo.
#
#     Calcolare l'età con la classe Date:
#     Aggiungi un metodo alla classe Studente che calcola l'età degli studenti in base alla data di nascita e
#     stampa l'età di ciascuno. Utilizza la classe Date per gestire le date in modo appropriato.
#
#     Creare una classe Libro con la classe Date e file:
#     Definire una classe Libro con attributi come titolo, autore, anno di pubblicazione (utilizzando la classe Date) e
#     genere. Crea alcuni oggetti libro e stampa le loro informazioni.
#     Inoltre, salva le informazioni dei libri in un file di testo.
#
#     Aggiungere metodi alle classi con file:
#     Aggiungi metodi alle classi Studente e Libro che consentano di aggiornare le informazioni degli oggetti e
#     salvarle in un file. Ad esempio, aggiungi un metodo per modificare il voto di uno studente o per cambiare
#     l'autore di un libro, quindi aggiorna il file corrispondente.
#
#     Leggere da un file e creare oggetti:
#     Scrivi una funzione che legga le informazioni degli studenti da un file e crei oggetti Studente in base ai dati letti.
#     Stampa le informazioni degli studenti così creati.
#
#     Calcolare l'anzianità del libro:
#     Aggiungi un metodo alla classe Libro che calcola l'anzianità di un libro in anni rispetto all'anno corrente.
#     Stampa l'anzianità dei libri.
#
#     Lettura e scrittura di oggetti in un file:
#     Implementa metodi per scrivere gli oggetti Studente e Libro in un file in un formato leggibile e
#     metodi per leggere gli oggetti da un file e crearli di nuovo.

import datetime


class Date:
    day = 0
    month = 0
    year = 0

    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

    def get_data_completa(self):
        ret_stringa = "{}/{}/{}"
        return ret_stringa.format(self.day, self.month, self.year)

    def __str__(self):
        ret_stringa = "{}/{}/{}"
        return ret_stringa.format(self.day, self.month, self.year)


class Studente:

    __nome = ""
    __cognome = ""
    __data_nascita = ""
    __voto_medio = 0

    def __init__(self, nome, cognome, data_nascita, voto_medio):
        self.__nome = nome
        self.__cognome = cognome
        self.__data_nascita = data_nascita
        self.__voto_medio = voto_medio

    def cambia_nome(self, nome):
        self.__nome = nome
        self.stampa_info_in_file()

    def cambia_cognome(self, cognome):
        self.__cognome = cognome
        self.stampa_info_in_file()

    def cambia_data_di_nascita(self, data_nascita):
        self.__data_nascita = data_nascita
        self.stampa_info_in_file()

    def cambia_voto_medio(self, voto_medio):
        self.__voto_medio = voto_medio
        self.stampa_info_in_file()

    def calcola_eta(self):
        oggi = datetime.date.today()
        data_nascita = datetime.date(self.__data_nascita.year, self.__data_nascita.month, self.__data_nascita.day)
        eta = oggi.year - data_nascita.year - ((oggi.month, oggi.day) < (data_nascita.month, data_nascita.day))
        return eta

    def stampa_info_in_file(self):
        nome_file = self.__nome + "_" + self.__cognome + "_" + str(self.__data_nascita.year) + ".txt"
        file = open(nome_file, "w", encoding="utf8")
        file.write("Nome: " + self.__nome + "\n")
        file.write("Cognome: " + self.__cognome + "\n")
        file.write("Data di nascita: " + self.__data_nascita.get_data_completa() + "\n")
        file.write("Voto Medio: " + str(self.__voto_medio) + "\n")
        file.write("Età: " + str(self.calcola_eta()) + " anni" + "\n")
        file.close()

    def stampa_info(self):
        print("Nome: ", self.__nome)
        print("Cognome: ", self.__cognome)
        print("Data di nascita: ", self.__data_nascita)
        print("Voto Medio: ", self.__voto_medio)
        print("Età: ", self.calcola_eta(), "anni")


class Libro:

    __titolo = ""
    __autore = ""
    __anno_pubblicazione = 0
    __genere = ""

    def __init__(self, titolo, autore, anno_pubblicazione, genere):
        self.__titolo = titolo
        self.__autore = autore
        self.__anno_pubblicazione = anno_pubblicazione
        self.__genere = genere

    def cambia_titolo(self, titolo):
        self.__titolo = titolo
        self.stampa_info_in_file()

    def cambia_autore(self, autore):
        self.__autore = autore
        self.stampa_info_in_file()

    def cambia_anno_pubblicazione(self, anno_pubblicazione):
        self.__anno_pubblicazione = anno_pubblicazione
        self.stampa_info_in_file()

    def cambia_genere(self, genere):
        self.__genere = genere
        self.stampa_info_in_file()

    def calcola_anzianita(self):
        oggi = datetime.date.today().year
        anzianita = oggi - self.__anno_pubblicazione.year
        return anzianita

    def stampa_info_in_file(self):
        nome_file = self.__titolo + "_" + self.__autore + "_" + str(self.__anno_pubblicazione.year) + ".txt"
        file = open(nome_file, "w", encoding="utf8")
        file.write("Titolo: " + self.__titolo + "\n")
        file.write("Autore: " + self.__autore + "\n")
        file.write("Anno di Pubblicazione: " + str(self.__anno_pubblicazione.year) + "\n")
        file.write("Genere: " + self.__genere + "\n")
        file.write("Anzianità: " + str(self.calcola_anzianita()) + "anni" + "\n")
        file.close()

    def stampa_info(self):
        print("Titolo:", self.__titolo)
        print("Autore:", self.__autore)
        print("Anno di Pubblicazione:", self.__anno_pubblicazione.year)
        print("Genere:", self.__genere)
        print("Anzianità:", self.calcola_anzianita(), "anni")


# Lettura di un file con studenti.txt
def leggi_studenti_da_file(nome_file):
    lista_studenti = []

    file = open(nome_file, "r")
    lines = file.readlines()

    for line in lines:
        line = line.strip()

        # La funzione split divide la stringa in una lista,
        info_studente = line.split(", ")
        nome = info_studente[0].strip()
        cognome = info_studente[1].strip()
        data_di_nascita = info_studente[2].strip().split("/")
        day = data_di_nascita[0]
        month = data_di_nascita[1]
        year = data_di_nascita[2]
        data_di_nascita = Date(day, month, year)
        voto_medio = int(info_studente[3])

        # Crea un oggetto Studente con le informazioni estratte
        nuovo_studente = Studente(nome, cognome, data_di_nascita, voto_medio)
        lista_studenti.append(nuovo_studente)

    return lista_studenti


# Creazione di due studenti.txt
studente1 = Studente("Mario", "Rossi", Date(10, 5, 2000), 28)
studente2 = Studente("Luigi", "Verdi", Date(15, 9, 1998), 30)

# Due libri
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", Date(1, 1, 1954), "Fantasy")
libro2 = Libro("1984", "George Orwell", Date(8, 6, 1949), "Distopia")

#
studente1.stampa_info_in_file()
studente1.cambia_nome("Antonio")

studente2.stampa_info_in_file()
studente2.cambia_nome("Marco")

#
libro1.stampa_info_in_file()
libro1.cambia_autore("George R. R. Martin")

# studenti
studenti = leggi_studenti_da_file("studenti.txt")
for studente in studenti:
    studente.stampa_info()
    print()