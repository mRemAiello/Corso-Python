class Libro:
    titolo = ""
    autore = ""
    anno = None
    isbn = ""

    def __init__(self, titolo, autore, anno, isbn):
        self.titolo = titolo.strip().title().replace("\n", "")
        self.autore = autore.strip().title().replace("\n", "")
        self.anno = str(anno).strip().replace("\n", "")
        self.isbn = isbn.strip().upper().replace("\n", "")

    def __str__(self):
        stringa = f"Titolo: {self.titolo}, "
        stringa += f"Autore: {self.autore}, "
        stringa += f"Anno Di Pubblicazione: {self.anno}, "
        stringa += f"ISBN: {self.isbn}"
        return stringa