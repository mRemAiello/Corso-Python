# E' necessario scrivere una applicazione che simula il funzionamento di un frammento del sistema
# informativo di un operatore di telefonia cellulare.
# Si devono quindi rappresentare i dati relativi ad una carta SIM ed in particolare:
# il numero di telefono, il credito disponibile in euro, la lista delle telefonate effettuate (array)
# Per ciascuna telefonata deve essere rappresentata la durata in minuti
# La classe SIM dovrà fornire le seguenti funzionalità :
# un costruttore parametrizzato che crea una SIM con numero di telefono, un credito e
# la lista delle telefonate vuota (un array)
# un metodo per l'inserimento di una telefonata con i dati forniti dall'utente
# una funzione per il calcolo dei minuti totali di conversazione
# una funzione per il calcolo delle telefonate effettuate verso un certo numero
# una procedura per la stampa dei dati della SIM e l'elenco delle telefonate


class Telefonata:

    __numero_chiamato = ""
    __minuti_conversazione = 0

    def __init__(self, numero_chiamato, minuti_conversazione):

        self.__numero_chiamato = numero_chiamato
        self.__numero_chiamato = self.__numero_chiamato.replace(" ", "")
        self.__numero_chiamato = self.__numero_chiamato.replace("+39", "")

        self.__minuti_conversazione = int(minuti_conversazione)

    def get_minuti_conversazione(self):
        return self.__minuti_conversazione

    def get_numero_chiamato(self):
        return self.__numero_chiamato

    def __str__(self):
        string = "Numero: {}, Durata {}"
        return string.format(self.__numero_chiamato, self.__minuti_conversazione)


class CartaSim:

    __numero_telefono = ""
    __credito = 0
    __telefonate = []

    def __init__(self, numero_telefono, credito):

        self.__numero_telefono = self.__pulisci_numero_telefono(numero_telefono)
        self.__credito = credito
        self.__telefonate = []

    def __pulisci_numero_telefono(self, numero):
        numero_ripulito = numero
        numero_ripulito = numero_ripulito.replace(" ", "")
        numero_ripulito = numero_ripulito.replace("+39", "")

        return numero_ripulito

    def inserisci_telefonata(self, telefonata):

        self.__telefonate.append(telefonata)

    def calcolo_minuti_conversazione(self):
        minuti = 0
        for telefonata in self.__telefonate:
            minuti += telefonata.get_minuti_conversazione()

        return minuti

    def get_telefonate_verso_numero(self, numero_chiamato):

        numero_ripulito = self.__pulisci_numero_telefono(numero_chiamato)
        lista_telefonate = []
        for telefonata in self.__telefonate:
            if telefonata.get_numero_chiamato() == numero_ripulito:
                lista_telefonate.append(telefonata)

        return lista_telefonate


    def __str__(self):
        string = "--- Carta SIM ---\n"
        string += "Numero: {}, Credito: {}\n"
        string += "--- Chiamate ---\n"
        for telefonata in self.__telefonate:
            string += telefonata.__str__() + "\n"
        return string.format(self.__numero_telefono, self.__credito)


telefonata_1 = Telefonata("3408", 20.5)
telefonata_2 = Telefonata("+393802 ", 10)
telefonata_3 = Telefonata("+393802 ", 2)

sim = CartaSim("3501", 30)
sim.inserisci_telefonata(telefonata_1)
sim.inserisci_telefonata(telefonata_2)
sim.inserisci_telefonata(telefonata_3)

print(sim)

print(sim.calcolo_minuti_conversazione())
lista = sim.get_telefonate_verso_numero("+393802")
for element in lista:
    print(element)






# Si desidera simulare un ascensore in funzione in un palazzo. L'ascensore ospita persone ed esegue le loro prenotazioni di spostamento ad un certo piano.
# Costruire una classe Prenotazioni, con informazione su numero clienti prenotanti e numero piano prenotato.
# Sviluppare metodi di accesso ed un metodo toString che descriva la prenotazione stessa.
# Costruire inoltre una classe Ascensore con le seguenti info: max numero piani, piano corrente, max numero persone, numero persone corrente, e lista prenotazioni.
# La lista delle prenotazioni ha una capienza massima prefissata, usando un array di Prenotazioni. le prenotazioni vengono servite con la politica del primo arrivato
# primo servito, usare una sentinella come più volte spiegato in classe.
# Sviluppare i seguenti metodi:
# Entra: incrementa il numero di persone nell'ascensore e mette in coda la relativa prenotazione.
# Muovi: porta l'ascensore al piano specificato dalla prima prenotazione trovata, fa uscire le persone relative ed aggiorna la lista delle prenotazioni.
# ToString: restituisce una stringa con la descrizione dello stato attuale dell'ascensore. In tutti i casi in cui venga violata una condizione
# (troppe persone in ascensore, troppe prenotazioni, ecc.) stampare un messaggio di errore ed uscire dal metodo relativo.