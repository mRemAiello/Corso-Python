# Esercizio 4: Hashing con SHA256
#
# Obiettivo: Comprendere il funzionamento delle funzioni di hashing utilizzando SHA256.
#
# Istruzioni:
#
#     Scrivi un programma che:
#         Chieda all'utente di inserire una stringa.
#         Generi l'hash della stringa utilizzando l'algoritmo SHA256.
#         Mostri l'hash generato all'utente.
#
#     Aggiungi una funzione che permetta all'utente di confrontare l'hash di un nuovo messaggio con quello
#     originale per verificare se i due messaggi sono uguali.

import hashlib


def generate_sha256_hash(message):
    return hashlib.sha512(message.encode()).hexdigest()


# Main
original_message = input("Inserisci una stringa: ")
original_hash = generate_sha256_hash(original_message)
print(f"L'hash generato è: {original_hash}")
print()

new_message = input("Inserisci un nuovo messaggio per confrontare l'hash: ")
new_hash = generate_sha256_hash(new_message)
print(f"L'hash generato è: {new_hash}")
print()


if original_hash == new_hash:
    print("I due messaggi sono uguali.")
else:
    print("I due messaggi sono diversi.")