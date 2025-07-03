# Esercizio 1: Scrivi un programma che chieda all'utente di inserire due numeri e calcoli la loro somma.
# Gestisci l'errore nel caso in cui l'utente non inserisca numeri validi (ad esempio una stringa o un carattere speciale).

try:
    numero1 = float(input("Inserisci il primo numero: "))
    numero2 = float(input("Inserisci il secondo numero: "))
    somma = numero1 + numero2
    print("La somma è:", somma)
except ValueError:
    print("Errore: inserisci solo numeri validi.")


# Esercizio 2: Crea una funzione che accetta due numeri e restituisce il risultato della divisione del primo per
# il secondo. Aggiungi la gestione delle eccezioni per evitare la divisione per zero.

def dividi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Errore: divisione per zero non permessa."


# Esempio d’uso
print(dividi(10, 2))
print(dividi(5, 0))

# Esercizio 3: Scrivi un programma che chieda all'utente di inserire una data (giorno, mese, anno).
# Utilizza una gestione delle eccezioni per rilevare eventuali errori di input
# (ad esempio, inserimento di lettere invece di numeri).

try:
    giorno = int(input("Inserisci il giorno: "))
    mese = int(input("Inserisci il mese: "))
    anno = int(input("Inserisci l'anno: "))
    print(f"Hai inserito la data: {giorno:02d}/{mese:02d}/{anno}")
except ValueError:
    print("Errore: devi inserire solo numeri per giorno, mese e anno.")


# Esercizio 4: Crea una funzione che accetti una lista di numeri e restituisca il loro quadrato.
# Gestisci l'errore nel caso in cui la lista contenga elementi non numerici.

def quadra_lista(lista):
    try:
        return [x ** 2 for x in lista]
    except TypeError:
        return "Errore: la lista deve contenere solo numeri."


# Esempio d’uso
print(quadra_lista([1, 2, 3]))
print(quadra_lista([1, 'a', 3]))  # Questo genererà un errore

# Esercizio 5: Scrivi un programma che apra un file di testo e ne stampi il contenuto.
# Se il file non esiste, gestisci l'errore usando un'eccezione.

try:
    with open("file.txt", "r") as file:
        contenuto = file.read()
        print("Contenuto del file:\n", contenuto)
except FileNotFoundError:
    print("Errore: il file non esiste.")


# Esercizio 6: Crea una funzione che converta una stringa in un numero intero.
# Aggiungi la gestione delle eccezioni per gestire i casi in cui la stringa non possa essere convertita.

def stringa_a_intero(s):
    try:
        return int(s)
    except ValueError:
        return "Errore: la stringa non può essere convertita in intero."


# Esempio
print(stringa_a_intero("42"))
print(stringa_a_intero("abc"))

# Esercizio 7: Scrivi un programma che chieda all'utente di inserire il proprio nome.
# Se l'utente preme invio senza inserire nulla, gestisci l'errore e chiedi di nuovo l'input.

while True:
    nome = input("Inserisci il tuo nome: ").strip()
    if nome:
        print(f"Ciao, {nome}!")
        break
    else:
        print("Errore: il nome non può essere vuoto. Riprova.")


# Esercizio 8: Crea una funzione che legga un numero da un file di testo e lo moltiplichi per 10.
# Gestisci eventuali errori nel caso in cui il file non contenga un numero valido o non sia accessibile.

def moltiplica_da_file(nome_file):
    try:
        with open(nome_file, "r") as f:
            numero = float(f.read())
            return numero * 10
    except FileNotFoundError:
        return "Errore: file non trovato."
    except ValueError:
        return "Errore: il contenuto del file non è un numero valido."


# Esempio d’uso
print(moltiplica_da_file("numero.txt"))

# Esercizio 9: Scrivi un programma che chieda all'utente di inserire un numero e verifichi se è pari o dispari.
# Gestisci le eccezioni se l'utente inserisce un valore non numerico.

try:
    numero = int(input("Inserisci un numero: "))
    if numero % 2 == 0:
        print("Il numero è pari.")
    else:
        print("Il numero è dispari.")
except ValueError:
    print("Errore: devi inserire un numero intero.")