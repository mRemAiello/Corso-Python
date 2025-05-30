# Creare un dizionario vuoto e assegnarlo a una variabile.
persona = {}
print(persona)
print()

# Creare un dizionario con le seguenti chiavi e valori: "nome" : "Mario", "cognome" : "Rossi", "età" : 30.

persona = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 30
}
print(persona)
print()

# Aggiungere un nuovo elemento "email" con valore "mario.rossi@email.com" al dizionario precedente.
persona.update({"email": "mario.rossi@email.com"})
persona["email"] = "mario.rossi@email.com"
print(persona)
print()

# Rimuovere l'elemento con chiave "cognome" dal dizionario precedente.
persona.pop("cognome")
print(persona)
print()


# Creare una nuova lista che contenga solo le chiavi del dizionario precedente.
chiavi = list(persona.keys())
print(chiavi)
print()


# Creare una nuova lista che contenga solo i valori del dizionario precedente.
valori = list(persona.values())
print(valori)
print()


# Aggiornare il valore dell'elemento con chiave "età" del dizionario precedente a 35.
persona["eta"] = 35
print(persona)
print()


# Contare il numero di elementi nel dizionario precedente.
lunghezza = len(persona)
print(lunghezza)
print()


# Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.
for chiave in persona:
    print(chiave)
print()


# Scrivere un programma che utilizzi un loop for per stampare tutti i valori di un dizionario.
for valore in persona.values():
    print(valore)
print()

# Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.
for chiave, valore in persona.items():
    print(chiave, ":", valore)
print()


# Creare un dict in cui le chiavi sono stringhe e i valori sono numeri interi.
# Stampare solo le coppie chiave-valore in cui il valore è maggiore di 5.
numeri = {
    "numero_1": 4,
    "numero_2": 6,
    "numero_3": 7,
    "numero_4": 8
}
for chiave, valore in numeri.items():
    if valore > 5:
        print(chiave, ":", valore)