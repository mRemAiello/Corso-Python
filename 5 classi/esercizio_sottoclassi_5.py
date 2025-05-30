# Scrivere una classe Veicolo che abbia le seguenti proprietà: marca, modello e anno e prezzo.
# Aggiungi poi i metodi accelera e frena. Creare poi una classe Auto che eredita da Veicolo ma aggiunge la proprietà
# colore ed il metodo cambia_colore().
# Modifica la classe Auto in modo che erediti anche il metodo __str__() dalla classe Veicolo, in modo da stampare le informazioni sull’auto
# in questo formato: “Marca: Ferrari, Modello: Enzo, Anno: 2004, Colore: Rosso”.
# Creare anche una classe Moto.
# Creare una classe chiamata Concessionario con le seguenti proprietà:
# nome (string): il nome del concessionario.
# inventario (lista di oggetti Veicolo): una lista che conterrà tutte le auto in vendita.
# Aggiungere un metodo aggiungi_veicolo(self, auto) alla classe Concessionario che consenta di aggiungere un'auto all'inventario.
# Aggiungere un metodo calcola_prezzo_totale(self) alla classe Concessionario che calcoli il prezzo totale di tutti i veicoli presenti nell'inventario.
# Aggiungere un metodo elenco_veicoli(self) alla classe Concessionario che stampi l'elenco delle auto disponibili, includendo marca, modello e prezzo di vendita.

class Veicolo:

    __marca = ""
    __modello = ""
    __anno = 0
    __prezzo = 0

    def __init__(self, marca, modello, anno, prezzo):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__prezzo = prezzo

    def accelera(self):
        print("Sto accelerando")

    def frena(self):
        print("Sto frenando")

    def get_prezzo(self):
        return self.__prezzo

    def __str__(self):
        string = "Marca: {}, Modello: {}, Anno: {}, Prezzo: {}"
        return string.format(self.__marca, self.__modello, self.__anno, self.__prezzo)


class Auto(Veicolo):

    __colore = ""

    def __init__(self, marca, modello, anno, prezzo, colore):
        super().__init__(marca, modello, anno, prezzo)
        self.__colore = colore

    def __str__(self):
        string = super().__str__() + ", Colore: {}"
        return string.format(self.__colore)


class Moto(Veicolo):

    __cilindrata = 0

    def __init__(self, marca, modello, anno, prezzo, cilindrata):
        super().__init__(marca, modello, anno, prezzo)
        self.__cilindrata = cilindrata

    def __str__(self):
        string = super().__str__() + ", Cilindrata: {}"
        return string.format(self.__cilindrata)


class Concessionario:

    __nome = ""
    __inventario = []

    def __init__(self, nome):
        self.__nome = nome

    def aggiungi_veicolo(self, auto):
        self.__inventario.append(auto)

    def calcola_prezzo_totale(self):
        prezzo_tot = 0
        for veicolo in self.__inventario:
            prezzo_tot += veicolo.get_prezzo()
        return prezzo_tot

    def elenco_veicoli(self):
        print("Concessionario: " + self.__nome)
        print("--- VEICOLI ---")
        for veicolo in self.__inventario:
            print(veicolo)
        print()


veicolo = Auto("Panda", "Fiat", 2000, 3000, "Rosso")
veicolo_2 = Moto("X", "Y", 1990, 35000, 1250)

concessionario = Concessionario("Auto & Moto")
concessionario.aggiungi_veicolo(veicolo)
concessionario.aggiungi_veicolo(veicolo_2)

print(concessionario.calcola_prezzo_totale())
concessionario.elenco_veicoli()