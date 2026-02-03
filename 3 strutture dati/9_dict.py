# Dict
persona = {
    "nome": "Marco",
    "cognome": "Rossi",
    "eta": 32,
    "sposato": False,
    "altezza": 1.80,
    "materie_sostenute": [20, 25, 30]
}

#
print(persona)

# Tipo
print(type(persona))

# Lunghezza
print(len(persona))

# Singolo valore
print(persona["eta"])

# Ottengo tutte le chiavi
print(persona.keys())

# Ottengo i valori
print(persona.values())

# Controllare l'esistenza di una specifica chiave
if "nome" in persona:
    print("Il nome esiste")

# Aggiornare gli elementi
persona["nome"] = "Ugo"
persona["colore"] = "rosso"
print(persona)

# Rimozione elementi
nome = persona.pop("nome")
print(persona)
print(nome)
print()

# Pulisci il dizionario
# persona.clear()
# print(persona)

# Cancella elementi o tutto il dizionario
# del persona["colore"]
# print(persona)
# del persona
# print(persona)

# Loop per ciclare le chiavi del dizionario
for chiave in persona:
    print(chiave)
print()

for chiave in persona.keys():
    print(chiave)
print()

# Itero i valori
for chiave in persona:
    print(chiave, ":", persona[chiave])
print()

# Secondo modo
for value in persona.values():
    print(value)
print()

# Entrambi
# persona.items() -> ("nome", "Marco"), ("cognome", "Rossi")
for chiave, valore in persona.items():
    print(chiave, valore)