# Validare un dizionario di dati, sollevare eccezioni personalizzate per ogni campo non valido
# e accumulare tutti gli errori invece di fermare l’esecuzione al primo errore.

import re


# 1. Eccezioni personalizzate

class DatoNonValidoException(Exception):
    pass


class EmailNonValidaException(DatoNonValidoException):
    def __init__(self, email):
        super().__init__(f"Email non valida: '{email}'")


class EtaNonValidaException(DatoNonValidoException):
    def __init__(self, eta):
        super().__init__(f"Età non valida: '{eta}' (deve essere un numero intero tra 18 e 99)")


class UsernameNonValidoException(DatoNonValidoException):
    def __init__(self, username):
        super().__init__(f"Username non valido: '{username}' (lunghezza minima: 4 caratteri, solo lettere e numeri)")


# 2. Funzione di validazione

def valida_dati(dati: dict):
    errori = []

    # Validazione email
    email = dati.get("email", "")
    if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email):
        errori.append(EmailNonValidaException(email))

    # Validazione età
    eta = dati.get("eta")
    if not isinstance(eta, int) or not (18 <= eta <= 99):
        errori.append(EtaNonValidaException(eta))

    # Validazione username
    username = dati.get("username", "")
    if not re.match(r"^[a-zA-Z0-9]{4,}$", username):
        errori.append(UsernameNonValidoException(username))

    return errori


# 3. Esempio di utilizzo

utente = {
    "email": "utente@@dominio..com",
    "eta": 15,
    "username": "a!"
}

errori = valida_dati(utente)

if errori:
    print("⚠️ Sono stati trovati errori nei dati forniti:")
    for errore in errori:
        print(f" - {errore}")
else:
    print("✅ Tutti i dati sono validi!")
