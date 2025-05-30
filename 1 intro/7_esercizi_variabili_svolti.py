# Esercizi

# Dichiarare una variabile "nome" e assegnargli il tuo nome. Mandare a schermo.
# Dichiarare una variabile "eta" e assegnargli la tua età. Mandare a schermo.
# Creare una variabile "eta_futura" e assegnargli il valore dell'età che avrai tra 10 anni (utilizzando la variabile età già esistente). Mandare a schermo.
# Dichiarare una variabile "pi" e assegnargli il valore di pi greco (3,14159). Mandare a schermo.
# Creare una variabile "lunghezza" e assegnargli un valore random. Castare la variabile a int. Mandare a schermo.
# Creare due variabili nome e cognome e una "nome_completo" con nome + cognome. Mandare a schermo.

import random

nome = "Mirko"
print(nome)
eta = 33
print(eta)
eta_futura = eta + 10
print(eta_futura)
pi = 3.14159
print(type(pi))
cognome = "Aiello"
nome_completo = nome + " " + cognome
print(nome_completo)


lunghezza = int(random.uniform(10, 20))
print(lunghezza)

# Presi in input due numeri, calcolarne la somma, la sottrazione, il prodotto, la divisione e div. resto.

a = int(input("Scrivi un numero: "))
b = int(input("Scrivi un altro numero: "))
#somma = a + b
#sottrazione = a - b
#prod = a * b
#div = a / b
#resto = a % b

#print(somma, sottrazione, prod, div, resto)


# Si scriva un programma che calcoli l’età media di una classe composta da 5 studenti con età random comprese tra 18 e 25.
# Fare il print delle età e della media. Trasformare anche in interi

studente_1 = int(random.uniform(18, 26))
studente_2 = int(random.uniform(18, 26))
studente_3 = int(random.uniform(18, 26))
studente_4 = int(random.uniform(18, 26))
studente_5 = int(random.uniform(18, 26))
# print(studente_1, studente_2, studente_3, studente_4, studente_5)

media = (studente_1 + studente_2 + studente_3 + studente_4 + studente_5) / 5
# print(media)


# Creare delle variabili "nome", "cognome" ed "anno_di_nascita" ed assegnargli dei valori. Mandare a schermo in un unico print.
# Sovrascrivere tutte le variabili e rimandare a schermo una seconda volta.

nome = "Mirko"
cognome = "Aiello"
anno_di_nascita = 1990

# print(nome, cognome, anno_di_nascita)


# Creare una variabile `eta_attuale` e assegnargli il valore dell'età che hai attualmente, calcolandola in base all'anno corrente.
# Mandare a schermo `eta_attuale`. Poi far decidere all'utente l'anno corrente.

# anno_corrente = int(input("Inserisci l'anno corrente: "))
# eta = anno_corrente - anno_di_nascita
# print(eta)


# Fare la media tra le 5 età dell'esercizio precedente e la tua età.

# media = (studente_1 + studente_2 + studente_3 + studente_4 + studente_5 + eta) / 6
# print(media)


# Si scriva un programma che, dato un valore intero definito dall’utente, ne visualizzi il valore intero precedente e il successivo.
# (es. il precedente e il successivo di 5 sono rispettivamente 4 e 6).

# valore = int(input("Scrivi un numero: "))
# print(valore + 1)
# print(valore - 1)



# Calcolare l’area del quadrato di lato D, l’area del cerchio di raggio R, l’area del triangolo di base B e altezza A.
# I dati del problema devono essere casuali.
# Area quadrato = lato * lato
# Area cerchio = pi greco * raggio * raggio
# Area triangolo = base * altezza / 2
# Trasformare in int le 3 aree.

# Genero casualmente dei dati per il calcolo
lato = int(random.uniform(10, 20))
raggio = int(random.uniform(20, 30))
base = int(random.uniform(40, 50))
altezza = int(random.uniform(60, 80))

# Calcolo aree
area_quadrato = lato * lato
area_cerchio = pi * raggio * raggio
area_triangolo = base * altezza / 2

print(area_quadrato, area_triangolo, area_cerchio)


# Il vostro gioco preferito è in sconto su Steam durante le festività natalizie.
# Utilizzare un float per rappresentare il prezzo (considerare anche i centesimi), e un float per la percentuale di sconto.
# Riportare quindi il prezzo totale, lo sconto, e il prezzo scontato.

prezzo = 24.99
percentuale = 20
sconto = prezzo * percentuale / 100
prezzo_scontato = prezzo - sconto
print(prezzo, sconto, prezzo_scontato)


# Si scriva un programma che dati due valori interi scelti dall’utente ne scambi i valori.
a = 5
b = 6

c = a
a = b
b = c

print(a, b)