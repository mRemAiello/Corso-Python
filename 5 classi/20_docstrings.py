"""Esempio di utilizzo delle DocStrings in una classe semplice."""


class Persona:
    """Rappresenta una persona generica."""

    def __init__(self, nome, eta):
        """Inizializza la persona con un nome e un'età."""
        self.nome = nome
        self.eta = eta

    def saluta(self):
        """Restituisce un messaggio di saluto."""
        return f"Ciao, sono {self.nome} e ho {self.eta} anni."


print("DocString del modulo:\n", __doc__)
print("\nDocString della classe Persona:\n", Persona.__doc__)
print("\nDocString del metodo saluta:\n", Persona.saluta.__doc__)