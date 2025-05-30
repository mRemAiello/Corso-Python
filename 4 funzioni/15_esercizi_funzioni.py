# Creare una funzione conta_carattere() che prende una lista di stringhe e un carattere.
# La funzione deve restituire il numero di ripetizioni del carattere nel testo.

def conta_carattere(lista, carattere):

    conta = 0
    for element in lista:
        for lettera in element:
            if lettera == carattere:
                conta = conta + 1

    return conta


def conta_carattere_while(lista, carattere):

    conta = 0
    i = 0
    while i < len(lista):
        j = 0
        element = lista[i]
        while j < len(element):
            lettera = element[j]
            if lettera == carattere:
                conta = conta + 1
            j = j + 1
        i = i + 1
    return conta



lista = ["Ciao", "Casa", "Pallone", "Albero"]
print(conta_carattere(lista, "c"))
print(conta_carattere_while(lista, "c"))



# Creare una funzione conta_caratteri() che prende una stringa, restituire un dizionario,
# in cui le chiavi sono i caratteri presenti nella stringa, e i valori sono le occorrenze.


def conta_caratteri(stringa):

    dict = {}
    for element in stringa:
        if not element == " " and not element == "\n":
            if element in dict:
                dict[element] = dict[element] + 1
            else:
                dict[element] = 1

    return dict



stringa = "Ciao Casa Pallone Albero"
print(conta_caratteri(stringa))



# Creare una funzione sottostringa() che date due stringhe ritorna True se la seconda e’ sottostringa della prima.

def sottostringa(prima_stringa, seconda_stringa):

    if seconda_stringa in prima_stringa:
        return True

    return False



print(sottostringa("Casa", "aso"))




# Creare una funzione sottostringhe_non_vuote() che data una stringa, restituisca la lista delle sue
# sottostringhe non vuote, inserite in una lista.
# Es. se una frase è "ciao come va" il programma deve restituire ["ciao", "come", "va"]


def sottostringhe_non_vuote(stringa):

    lista = []
    parola = ""
    for element in stringa:
        if element == " ":
            lista.append(parola)
            parola = ""
        else:
            parola = parola + element

    if not parola == "":
        lista.append(parola)

    for element in lista:
        if element == "":
            lista.remove(element)

    return lista


print(sottostringhe_non_vuote("ciao come va"))




# Creare una funzione conta_sottostringhe() che, date due stringhe pagliaio ed ago,
# ritorni il numero di ripetizioni di ago in pagliaio.

def conta_sottostringhe(pagliaio, ago):

    return pagliaio.count(ago)


pagliaio = "Ciao come va va"
ago = "Ciao"
print(conta_sottostringhe(pagliaio, ago))



# Creare una funzione sottostringa_piu_lunga() che date due stringhe restituisca la loro sottostringa comune piu’ lunga.

def sottostringa_piu_lunga(prima_stringa, seconda_stringa):

    sottostringa_prima = sottostringhe_non_vuote(prima_stringa)
    sottostringa_seconda = sottostringhe_non_vuote(seconda_stringa)

    sottostringhe_comuni = []
    for element in sottostringa_prima:
        if element in sottostringa_seconda:
            sottostringhe_comuni.append(element)

    massimo = sottostringhe_comuni[0]
    for element in sottostringhe_comuni:
        if len(element) > len(massimo):
            massimo = element

    return massimo


prima_stringa = "Ciao come va, comune, meno comune"
seconda_stringa = "va bene, comune, meno comune"

print(sottostringa_piu_lunga(prima_stringa, seconda_stringa))