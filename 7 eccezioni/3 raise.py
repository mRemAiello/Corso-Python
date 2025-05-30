# Per avere la mia eccezione devo farmi la sottoclasse
class MyException(Exception):
    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super(MyException, self).__init__(message)

        # Now for your custom code...
        self.errors = errors


# Funzione che lancia la mia eccezione
def funzione_con_eccezione():
    raise MyException("Spiego l'errore che esce", "Er")


# Gestisco l'eccezione

try:
    funzione_con_eccezione()
except MyException:
    print("Uscito l'errore my ex")