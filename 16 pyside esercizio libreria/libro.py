class Libro:
    titolo = ""
    autore = ""
    anno = None
    isbn = ""

    def __init__(self, titolo, autore, anno, isbn):
        self.titolo = titolo.strip().title().replace("\n", "")
        self.autore = autore.strip().title().replace("\n", "")
        self.anno = anno.strip().replace("\n", "")
        self.isbn = isbn.strip().upper().replace("\n", "")

    def __str__(self):
        stringa = f"Titolo: {self.titolo}\nAutore: {self.autore}\nAnno Di Pubblicazione: {self.anno}\nISBN: {self.isbn}"
        return stringa