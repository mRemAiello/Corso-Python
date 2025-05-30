# Un Elemento Multimediale è una Immagine, un Filmato o una registrazione Audio identificato da un titolo (una stringa non vuota).
# Un elemento è riproducibile se ha una durata (un valore positivo di tipo int) e un metodo play().

# Una registrazione Audio è riproducibile e ha associato anche un volume (un valore positivo di tipo int) e i metodi weaker() e louder() per regolarlo.
# Se riprodotta, ripete per un numero di volte pari alla durata la stampa del titolo concatenato a una sequenza di punti esclamativi di lunghezza
# pari al volume (una stampa per riga).

# Una Immagine non è riproducibile, ma ha una luminosità regolabile analoga a quella dei filmati e un metodo show()
# che stampa il titolo concatenato a una sequenza di asterischi di lunghezza pari alla luminosità
# Eseguire un oggetto multimediale significa invocarne il metodo show() se è un'immagine o il metodo play() se è riproducibile.

# Un Filmato è riproducibile e ha associato un volume regolabile analogo a quello delle registrazioni audio e
# anche una luminosità (un valore positivo di tipo int) e i metodi brighter() e darker() per regolarla.
# Se riprodotta, ripete per un numero di volte pari alla durata la stampa del titolo concatenato a una sequenza
# di punti esclamativi di lunghezza pari al volume e poi a una sequenza di asterischi di lunghezza pari alla luminosità (una stampa per riga).

# Organizzare opportunamente il codice di un lettore multimediale
# che memorizza 5 elementi (creati con valori letti da tastiera) in un array e poi chiede ripetutamente
# all'utente quale oggetto eseguire (leggendo un intero da 1 a 5 oppure 0 per finire) e dopo ogni
# esecuzione fornisce la possibilità di regolarne eventuali parametri (volume / luminosità).

class ElementoMultimediale:

    __titolo = ""

    def __init__(self, titolo):
        self.set_titolo(titolo)

    def get_titolo(self):
        return self.__titolo

    def set_titolo(self, titolo):
        if titolo == "":
            print("Il titolo non può essere vuoto")
        else:
            self.__titolo = titolo

    def is_riproducibile(self):
        return False

    def esegui(self):
        return

    def __str__(self):
        stringa = "Titolo: {}"
        return stringa.format(self.get_titolo())


class ElementoRiproducibile(ElementoMultimediale):

    __durata = 1

    def __init__(self, titolo, durata):
        super().__init__(titolo)
        self.set_durata(durata)

    def get_durata(self):
        return self.__durata

    def set_durata(self, durata):
        if durata > 1:
            self.__durata = durata
        else:
            self.__durata = 1

    def is_riproducibile(self):
        return self.__durata > 0

    def __str__(self):
        stringa = super().__str__() + ", Durata: {}"
        return stringa.format(self.get_durata())


class Audio(ElementoRiproducibile):

    __volume = 0

    def __init__(self, titolo, durata, volume):
        super().__init__(titolo, durata)
        self.set_volume(volume)

    def get_volume(self):
        return self.__volume

    def set_volume(self, volume):
        self.__volume = volume
        if self.__volume < 0:
            self.__volume = 0
        if self.__volume > 100:
            self.__volume = 100

    def aumenta_volume(self, volume):
        self.__volume += volume
        if self.__volume > 100:
            self.__volume = 100

    def abbassa_volume(self, volume):
        self.__volume -= volume
        if self.__volume < 0:
            self.__volume = 0

    def esegui(self):
        print("Riproduco l'audio", self.get_titolo(), "a volume", self.get_volume())

    def __str__(self):
        stringa = super().__str__() + ", Volume: {}"
        return stringa.format(self.get_volume())


class Immagine(ElementoMultimediale):

    __luminosita = 1

    def __init__(self, titolo, luminosita):
        super().__init__(titolo)
        self.__luminosita = luminosita

    def get_luminosita(self):
        return self.__luminosita

    def set_luminosita(self, luminosita):
        self.__luminosita = luminosita
        if self.__luminosita > 100:
            self.__luminosita = 100
        if self.__luminosita < 1:
            self.__luminosita = 1

    def aumenta_luminosita(self, luminosita):
        self.__luminosita += luminosita
        if self.__luminosita > 100:
            self.__luminosita = 100

    def abbassa_luminosita(self, luminosita):
        self.__luminosita -= luminosita
        if self.__luminosita < 1:
            self.__luminosita = 1

    def is_riproducibile(self):
        return True

    def esegui(self):
        print("Mostro l'immagine", self.get_titolo(), "a luminosita", self.get_luminosita())

    def __str__(self):
        stringa = super().__str__() + ", Luminosita: {}"
        return stringa.format(self.get_luminosita())



class Filmato(ElementoRiproducibile):

    __immagine = Immagine("", 1)
    __audio = Audio("", 0, 0)

    def __init__(self, titolo, durata, volume, luminosita):
        super().__init__(titolo, durata)
        self.__immagine = Immagine(titolo, luminosita)
        self.__audio = Audio(titolo, durata, volume)

    def get_luminosita(self):
        return self.__immagine.get_luminosita()

    def get_volume(self):
        return self.__audio.get_volume()

    def aumenta_luminosita(self, luminosita):
        self.__immagine.aumenta_luminosita(luminosita)

    def abbassa_luminosita(self, luminosita):
        self.__immagine.abbassa_luminosita(luminosita)

    def aumenta_volume(self, volume):
        self.__audio.aumenta_volume(volume)

    def abbassa_volume(self, volume):
        self.__audio.abbassa_volume(volume)

    def esegui(self):
        print("Riproduco il filmato", self.get_titolo(), "a volume", self.get_volume(),
              "e luminosita", self.get_luminosita())

    def __str__(self):
        stringa = super().__str__() + ", Luminosità: {}, Volume: {}"
        return stringa.format(self.get_luminosita(), self.get_volume())



immagine = Immagine("Foto delle vacanze al mare", 70)
audio = Audio("Rock of Ages", 10, 80)
filmato = Filmato("Naruto", 80, 20, 100)

immagine.aumenta_luminosita(20)
immagine.esegui()

audio.aumenta_volume(30)
audio.esegui()

filmato.aumenta_luminosita(5)
filmato.aumenta_volume(5)
filmato.esegui()

print()
print(immagine)
print(audio)
print(filmato)