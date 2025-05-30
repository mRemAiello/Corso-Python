# Creare un dizionario di partenza che contenga un nome ed un cognome. Dopo inserire la matricola, chiedendola
# in input (insieme a nome e cognome) e aggiungere poi gli esami sostenuti con il nome della materia
# ed il voto ottenuto. Calcola inoltre la media delle materie.

"""persona = {
    "nome": "Ugo",
    "cognome": "Rossi",
    "età": 25,
    "materie": []
}

matricola = input("Scrivi il tuo numero di matricola: ")
persona["matricola"] = matricola

numero_materie = int(input("Scrivi un numero di materie: "))

#
i = 0
while i < numero_materie:
    
    nome_materia = input("Scrivi il nome della materia: ")
    voto_materia = int(input("Scrivi il voto della materia: "))
    
    persona["materie"].append([nome_materia, voto_materia])
    
    i = i + 1

#
media = 0
for elemento in persona["materie"]:
    voto_materia = elemento[1]
    media += voto_materia

media = media / len(persona["materie"])
print("Media:", media)

print(persona)"""



# Crea un dizionario vuoto chiamato "rubrica" per memorizzare i contatti.
# Fornisci all'utente un menu con le opzioni di aggiungere un nuovo contatto, visualizzare i dettagli di un contatto o eliminare un contatto.
# Implementa la logica per ciascuna opzione del menu.
# Assicurati di gestire i casi in cui l'utente cerca di visualizzare o eliminare un contatto che non esiste.


"""rubrica = {}
comando = int(input("Inserisci un comando (0: Esci, 1 Aggiungi, 2 Elimina, 3 Visualizza): "))
while not comando == 0:

    if comando == 1:
        nome = input("Scrivi un nome: ")
        numero_di_telefono = int(input("Scrivi un numero di telefono: "))
        if nome in rubrica:
            rubrica[nome].append(numero_di_telefono)
        else:
            rubrica[nome] = [numero_di_telefono]
        print(nome, "inserito in rubrica")

    elif comando == 2:
        nome = input("Scrivi un nome: ")
        if nome in rubrica:
            del rubrica[nome]
            print(nome, "eliminato correttamente")
        else:
            print(nome, "non è presente in rubrica")

    elif comando == 3:
        for chiave, valore in rubrica.items():
            print(chiave, ":", valore)

    #
    comando = int(input("Inserisci un comando (0: Esci, 1 Aggiungi, 2 Elimina, 3 Visualizza): "))"""




# Creare un dizionario dove le chiavi sono dei semi (bastoni, coppe, denari, cuori) e i valori sono una lista da 1 a 13.
# Estrai una carta casuale a partire da un seme chiesto all'utente. Estrai anche una carta casuale senza chiedere nulla all'utente.

"""import random

carte = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "Donna", "Cavallo", "Re"]
semi = {
    "bastoni": carte,
    "coppe": carte,
    "denari": carte,
    "cuori": carte
}

# Estraggo una carta a partire da un seme chiesto all'utente
seme = input("Scrivi un seme (Bastoni, Coppe, Denari, Cuori): ")
if seme in semi:
    lista = semi[seme]
    carta = lista[int(random.uniform(0, len(lista)))]
    print("Ho estratto", carta, "di", seme)

# Estraggo casualmente anche il seme
lista = list(semi.keys())
seme = lista[int(random.uniform(0, len(lista)))]
lista = semi[seme]
carta = lista[int(random.uniform(0, len(lista)))]
print("Ho estratto", carta, "di", seme)"""



# Unisci 2 dizionari qualunque in un terzo.
a = {
    "nome": "Marco",
    "cognome": "Rossi"
}

b = {
    "eta": 20,
    "nome": "Mirko"
}

c = {}

for chiave, valore in a.items():
    c[chiave] = valore
for chiave, valore in b.items():
    if chiave in c:
        c[chiave + "_1"] = valore
    else:
        c[chiave] = valore

print(c)


# Prendi 2 dizionari e inverti le chiavi in valori e viceversa.
c = {}
d = {}

for chiave, valore in a.items():
    c[str(valore)] = chiave
for chiave, valore in b.items():
    d[str(valore)] = chiave

print(c)
print(d)