# Esercizi


def sottostringhe_non_vuote(stringa):

    lista = stringa.split(" ")

    lista_ripulita = []
    for element in lista:
        if not element == "\n" and not element == "":
            lista_ripulita.append(element)

    return lista_ripulita


print(sottostringhe_non_vuote(" ciao  come  \n va "))






# Assegnare una stringa "ciao mondo" ad una variabile "stringa" e utilizzare il metodo upper()
# per convertirla in maiuscolo in una nuova variabile.


stringa = "ciao mondo"
print(stringa.upper())
print(stringa.lower())
print(stringa.capitalize())
print(stringa.title())



# Assegnare una stringa "Benvenuti a Roma" ad una variabile "stringa" e utilizzare il metodo lower() per
# convertirla in minuscolo in una nuova variabile.


# Assegnare una stringa "Il meglio deve ancora venire" ad una variabile "stringa" e utilizzare il metodo split()
# per dividere la stringa in una lista di parole.

stringa = "Il meglio deve ancora venire"
lista = stringa.split(" ")
print(lista)



# Assegnare una stringa "Hello World" ad una variabile "stringa" e utilizzare il metodo replace()
# per sostituire "World" con "Python".

stringa = "Hello World"
stringa = stringa.replace("World", "Python")
print(stringa)




# Assegnare una stringa " Ciao " ad una variabile "stringa" e utilizzare il metodo strip() per
# rimuovere gli spazi vuoti all'inizio e alla fine della stringa.

stringa = " Ciao "
stringa = stringa.strip()
print(stringa)






# Assegnare una stringa "abcdefg" ad una variabile "stringa" ed estrarre i primi tre caratteri.

stringa = "abcdefg"
if len(stringa) >= 3:
    stringa = stringa[0:3]
    print(stringa)




# Assegnare una stringa "Python" ad una variabile "stringa" e utilizzare il metodo startswith()
# per verificare se la stringa inizia con "Py".

stringa = "Python"
if stringa.startswith("Py"):
    print("La stringa inizia per Py")
if stringa.endswith("on"):
    print("La stringa termina con on")




# Assegnare una stringa "Ciao mondo" ad una variabile "stringa" e utilizzare il metodo count() per contare il numero
# di volte in cui la lettera "o" appare nella stringa.

stringa = "Ciao mondo"
print(stringa.count("o"))




# Assegnare una stringa "Ciao mondo" ad una variabile "stringa".
# Mandare quindi a schermo gli ultimi 5 caratteri della stringa in maiuscolo, sostituendo il carattere "o" con "k".


# Creare due variabili "nome" e "cognome" e concatenarle a schermo usando il format.
# Utilizzare la formattazione delle stringhe per ottenere "Il numero è: 42".

# Utilizzare la formattazione delle stringhe per ottenere "Il numero binario di 42 è 0b101010".
# Per il binario utilizzare bin(numero)
# Togliere lo 0b dal binario.

# Partendo dalla variabile "numero" uguale a 5, utilizzare le f-strings (interpolazione) per ottenere "Il quadrato di 5 è 25".


# Partendo da "nome" e "cognome" utilizzare la formattazione strighe per ottenere "Il mio nome è {nome} ed il cognome è {cognome}".
# Come da esempio dovete fare riferimento al nome delle variabili e non alla posizione usata dentro format.

"""stringa = "Il mio nome è {} ed il cognome è {}"
nome = input("Scrivi il tuo nome ")
cognome = input("Scrivi il tuo cognome ")
print(stringa.format(nome, cognome))"""



# Facendo riferimento all'esercizio precedente ottenere il seguente risultato modificando i valori
# nel format(): "Il mio nome è LUCA ed il cognome è RoKKi"


# Dato il seguente testo:
# testo = "python è un linguaggio fantastico e polivalente"
# Utilizza il metodo appropriato per cambiare in maiuscolo la prima lettera della frase.


# Prendi la frase dell'esercizio #1 e conta le lettere "a" presenti. Fallo due volte, con e senza loop.


# Dati dei codici dalla seguente forma:
# c1 = 'AFCDDR-CF-2020'
# c2 = 'SEDTYR-XC-2019'
# Crea una funzione appropriata, che controlli se una lista di codice finisce per 2020.
# Restituisci un dizionario dove la chiave è il codice e il valore è True / False.

def controllo(codice):
    if codice.endswith("2020"):
        return True
    return False


c1 = 'AFCDDR-CF-2020'
c2 = 'SEDTYR-XC-2019'
print(controllo(c1))
print(controllo(c2))



# Sono indicati i seguenti percorsi:
# p1 = 'youtube.com/channel/UCTzgW6OXZFNXV0-YVRMt9lA'
# p2 = 'google.com/search?q=tuttofaredigitale'
# Con il metodo appropriato verifica se i percorsi forniti si riferiscono a YouTube.


def controlla_url(url):
    if url.startswith("youtube.com/"):
        return True
    return False


p1 = 'youtube.com/channel/UCTzgW6OXZFNXV0-YVRMt9lA'
p2 = 'google.com/search?q=tuttofaredigitale'
print(controlla_url(p1))
print(controlla_url(p2))


# Sono indicati i seguenti percorsi:
# p1 = 'https://tuttofaredigitale.it/data-scientist-machine-learning'
# p2 = 'https://tuttofaredigitale.it/data-scientist-deep-learning'
# p3 = 'https://tuttofaredigitale.it/data-analyst'
# Usando il metodo appropriato trova la parola "scientist" nei percorsi indicati, restituendo la posizione (indice)
# per la prima lettera della parola trovata. Se la parola non è nel percorso, il metodo restituirà -1.

def controlla_url_2(url):

    if "https" in url:
        posizione = url.index("https")
        return posizione
    else:
        return -1


p1 = 'https://tuttofaredigitale.it/data-scientist-machine-learning'
p2 = 'https://tuttofaredigitale.it/data-scientist-deep-learning'
p3 = 'https://tuttofaredigitale.it/data-analyst'

print(controlla_url_2(p1))
print(controlla_url_2(p2))
print(controlla_url_2(p3))