import libro as lb

class Libreria:
    __lista_libri = {}
    __percorso_file = ""

    def __init__(self):
        self.carica_da_file()

    def aggiungi_libro(self, libro : lb.Libro):
        self.__lista_libri [libro.isbn] = libro
        self.salva_su_file()

    def trova_libro(self, isbn : str):
        for libro in self.__lista_libri.values():
            if isbn == libro.isbn:
                return libro
        return None

    def trova_libro_autore(self, autore : str):
        risult_autore = []
        for libro in self.__lista_libri.values():
            if autore.lower() in libro.autore.lower():
                risult_autore.append(libro)
        return risult_autore

    def trova_libro_titolo(self, titolo : str):
        risult_titolo = []
        for libro in self.__lista_libri.values():
            if titolo.lower() in libro.titolo.lower():
                risult_titolo.append(libro)
        return risult_titolo

    def rimuovi_libro(self, isbn : str):
        libro = self.trova_libro(isbn)
        if not libro is None:
            del self.__lista_libri [isbn]
        else:
            print(f"Non esiste")
        self.salva_su_file()

    def salva_su_file(self):
        try:
            file = open(self.__percorso_file, "w", encoding="utf-8")
            for libro in self.__lista_libri.values():
                file.write(f"{libro.isbn}, {libro.titolo}, {libro.autore}, {libro.anno}\n")
            file.close()
        except FileNotFoundError:
            print(f"Il file non esiste")
        except Exception as e:
            print(f"Error: {e}")

    def carica_da_file(self):
        try:
            self.__lista_libri = {}
            file = open(self.__percorso_file, "r", encoding="utf-8")
            for riga in file:
                if len(riga) <= 10:
                    continue
                element = riga.split(",")
                libro = lb.Libro(element[1], element[2], element[3], element[0])
                self.__lista_libri [libro.isbn] = libro
            file.close()
        except FileNotFoundError:
            print(f"Il file non esiste")
        except Exception as e:
            print(f"Error: {e}")

    def modifica(self, isbn, titolo="", autore="", anno=""):
        if isbn in self.__lista_libri:
            if titolo != "":
                self.__lista_libri[isbn].titolo = titolo
            if autore != "":
                self.__lista_libri[isbn].autore = autore
            if anno != "":
                self.__lista_libri[isbn].anno = anno
            self.salva_su_file()
            return "Libro modificato con successo"
        return "Libro non trovato"

    def getLibri(self):
        return self.__lista_libri.copy()

    def percorso_file(self, file):
        if file != self.__percorso_file:
            self.__percorso_file = file
            self.carica_da_file()

    def reset_lista(self):
        self.__lista_libri.clear()