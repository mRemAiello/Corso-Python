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
#
# Domande di riflessione:
#
#     Qual è la differenza tra crittografia e hashing?
#     Perché non è possibile recuperare il messaggio originale da un hash?

import hashlib


def genera_hash_sha256(messaggio: str) -> str:
    hash_object = hashlib.sha256(messaggio.encode())
    return hash_object.hexdigest()


def confronta_hash(originale: str, confronto: str) -> bool:
    return genera_hash_sha256(originale) == genera_hash_sha256(confronto)


messaggio = input("Inserisci un messaggio da convertire in hash: ")
hash_messaggio = genera_hash_sha256(messaggio)
print("Hash SHA256 generato:", hash_messaggio)

nuovo_messaggio = input("Inserisci un altro messaggio per confrontarlo: ")
hash_messaggio = genera_hash_sha256(nuovo_messaggio)
print("Hash SHA256 generato:", hash_messaggio)

#
if confronta_hash(messaggio, nuovo_messaggio):
    print("I messaggi sono uguali.")
else:
    print("I messaggi sono diversi.")

# === Domande di riflessione ===
# Differenza tra crittografia e hashing:
# - La crittografia è reversibile (con la chiave giusta si può decifrare), l'hashing no.
# - L'hashing serve per integrità e verifica, la crittografia per riservatezza e sicurezza dei dati.

# Perché non è possibile recuperare il messaggio originale da un hash?
# - Perché l'hash è un processo unidirezionale: produce una rappresentazione fissa e non invertibile.
# - Gli hash sono progettati per essere resistenti alla preimmagine (cioè non si può risalire all'input).