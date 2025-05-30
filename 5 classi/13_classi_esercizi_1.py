# Esercizi

# Creare una classe Persona che abbia i seguenti attributi: nome, età, sesso.
# Aggiungi un metodo “presentati” che stampi una frase di presentazione della persona,
# ad esempio “Ciao, mi chiamo Marco e ho 32 anni”.

class Persona:

    nome = ""
    eta = 0
    sesso = ""

    def __init__(self, nome, eta, sesso):
        self.nome = nome
        self.eta = eta
        self.sesso = sesso

    def presentati(self):

        stringa = "Ciao, mi chiamo {} e ho {} anni"
        print(stringa.format(self.nome, self.eta))


persona1 = Persona("Marco", 32, "Maschile")
persona2 = Persona("Mirko", 33, "Maschile")

persona1.presentati()
persona2.presentati()
print()




# Creare una classe Animale che abbia gli attributi “nome” e “specie”.
# Aggiungi un metodo “emetti_suono” che stampi un suono specifico per ogni specie.
# Ad esempio, se l’animale è un gatto dovrebbe stampare “Miao!”, se è un cane “Bau!”.

class Animale:

    dic = {
        "Cane": "Bau",
        "Gatto": "Miao"
    }

    nome = ""
    specie = ""

    def __init__(self, nome, specie):
        self.nome = nome
        self.specie = specie

    def emetti_suono(self):

        if self.specie in self.dic:
            print(self.dic[self.specie])


animale1 = Animale("Snoopy", "Cane")
animale2 = Animale("Bolt", "Gatto")

animale1.emetti_suono()
animale2.emetti_suono()
print()


# Creare una classe Automobile che abbia gli attributi “marca”, “modello” e “anno”.
# Aggiungi un metodo “descrivi” che stampi una descrizione dell’automobile, ad esempio “Questa è una Toyota Corolla del 2017”.


class Automobile:

    marca = ""
    modello = ""
    anno = 0

    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrivi(self):
        stringa = "Questa è una {} {} del {}"
        print(stringa.format(self.marca, self.modello, self.anno))


auto1 = Automobile("Toyota", "Corolla", 2017)
auto1.descrivi()

auto2 = Automobile("Lancia", "Delta", 2018)
auto2.descrivi()

print()



# Realizzare una classe PersonalComputer (con costruttore) con le seguenti caratteristiche :
# marca, modello, tipo di processore, quantità di ram, spazio memoria HD e tipo di scheda video.
# Creare una funzione che stampi le informazioni del pc.
# Creare poi nel Main una serie di PersonalComputer variando marca, modello, ecc.


# Realizzare una classe Calcolatrice con 6 funzioni: Somma, Sottrazione, Moltiplicazione, Divisione, DivisioneResto e Potenza.
# Poi, nel Main, istanziare la classe ed eseguire le operazioni, mostrando i risultati delle operazioni.


# Realizzare una classe Studente e un'altra classe Insegnante. La classe Studente avrà un metodo public chiamato vado_in_classe, che scriverà a schermo "Sto andando in classe"
# La classe Insegnante avrà un metodo pubblico "insegna", che scriverà a schermo "Sto insegnando".
# Infine, entrambe le classi avranno un metodo pubblico imposta_eta (che prende in input un valore numerico intero e imposta l’età) e mostra_eta, che visualizza l'età.


# Creare una classe Impiegato che abbia gli attributi “nome”, “cognome”, “matricola” e “stipendio”.
# Aggiungere un metodo “aumenta_stipendio” che aumenti lo stipendio dell’impiegato del 10% e un metodo aumenta_stipendio(x) che aumenta lo stipendio dell'x%.
# Inoltre inserire un metodo “stampa_dettagli” che stampi tutti i dettagli dell’impiegato,
# ad esempio “Impiegato: Marco Rossi, matricola: 12345, stipendio: 3000 Euro”.


class Impiegato:

    nome = ""
    cognome = ""
    matricola = 0
    stipendio = 0

    def __init__(self, nome, cognome, matricola, stipendio):
        self.nome = nome
        self.cognome = cognome
        self.matricola = matricola
        self.stipendio = stipendio

    def aumenta_stipendio(self, x=10):
        self.stipendio = self.stipendio + (self.stipendio * x / 100)

    def stampa_dettagli(self):
        stringa = "Impiegato: {} {}, matricola: {}, stipendio: {} Euro"
        print(stringa.format(self.nome, self.cognome, self.matricola, self.stipendio))


impiegato1 = Impiegato("Marco", "Rossi", 123, 1400)
impiegato1.stampa_dettagli()
impiegato1.aumenta_stipendio()
impiegato1.aumenta_stipendio(26)
impiegato1.stampa_dettagli()
print()



# Crea una classe Prodotto che abbia gli attributi “nome”, “prezzo” e “scorta”.
# Crea una classe GestoreMagazzino che gestisca un magazzino di prodotti. La classe dovrà avere i seguenti attributi:
#
#     Un dizionario “prodotti” che mappa i nomi dei prodotti ai rispettivi oggetti “Prodotto” (che descriverai in seguito)
#     Una variabile “costo_magazzinaggio” che indica il costo per magazzinare ogni prodotto per un mese
#
# La classe dovrà avere i seguenti metodi:
#
#     Un metodo “aggiungi_prodotto” che aggiunga un nuovo prodotto al magazzino
#     Un metodo “rimuovi_prodotto” che rimuova un prodotto dal magazzino
#     Un metodo “calcola_costi_magazzinaggio” che calcoli i costi di magazzinaggio per tutti i prodotti presenti nel magazzino
#
# Aggiungi poi la possibilità di inserire prodotti multipli (2 e una lista)


class Prodotto:

    nome = ""
    prezzo = ""
    scorta = ""

    def __init__(self, nome, prezzo, scorta):
        self.nome = nome
        self.prezzo = prezzo
        self.scorta = scorta


class GestoreMagazzinaggio:

    prodotti = {}
    costo = 0

    def __init__(self, costo):
        self.costo = costo
        self.prodotti = {}

    def aggiungi_prodotto(self, prodotto):
        if prodotto.nome in self.prodotti:
            if self.prodotti[prodotto.nome].prezzo == prodotto.prezzo:
                self.prodotti[prodotto.nome].scorta += prodotto.scorta
            else:
                string = "Il prodotto {} ha due prezzi differenti"
                print(string.format(prodotto.nome))
        else:
            self.prodotti[prodotto.nome] = prodotto

    def aggiungi_due_prodotti(self, prodotto_1, prodotto_2):
        self.aggiungi_prodotto(prodotto_1)
        self.aggiungi_prodotto(prodotto_2)

    def aggiungi_prodotti(self, lista):
        for prodotto in lista:
            self.aggiungi_prodotto(prodotto)


pera = Prodotto("Pera", 4.99, 5)
mela = Prodotto("Mela", 9.99, 10)
mela2 = Prodotto("Mela", 19.99, 10)

gestore = GestoreMagazzinaggio(10)
gestore.aggiungi_prodotti([pera, mela, mela2])

print([pera, mela, mela2])
print(gestore)
print(mela)