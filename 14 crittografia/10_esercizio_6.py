# Esercizio 6: Utilizzo di IV (Initialization Vector) con AES
#
# Obiettivo: Capire l'importanza del vettore di inizializzazione (IV) nella crittografia simmetrica.
#
# Istruzioni:
#
#     Scrivi un programma che:
#         Generi una chiave AES e un IV.
#         Cifri un messaggio con la modalità CFB usando l'IV generato.
#         Decifri il messaggio usando la stessa chiave e IV.
#     Ripeti il processo usando un IV diverso per la decifratura e osserva cosa succede.
#
# Domande di riflessione:
#
#     Perché l'IV è importante nella crittografia?
#     Cosa succede se l'IV viene riutilizzato o condiviso in modo errato?

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# === Generazione chiave e IV ===
key = os.urandom(32)  # AES-256 richiede 32 byte
iv = os.urandom(16)   # IV deve essere di 16 byte per AES

# === Messaggio da cifrare ===
plaintext = bytes(input("Scrivi messaggio:"), "utf8")

# === Cifratura con AES-CFB ===
cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
ciphertext = encryptor.update(plaintext) + encryptor.finalize()
print("Testo cifrato:", ciphertext)
print()

# === Decifratura con stesso IV ===
decipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend()).decryptor()
decrypted = decipher.update(ciphertext) + decipher.finalize()
print("Testo decifrato (IV corretto):", decrypted.decode())
print()

# === Decifratura con IV errato ===
wrong_iv = os.urandom(16)
decipher_wrong_iv = Cipher(algorithms.AES(key), modes.CFB(wrong_iv), backend=default_backend()).decryptor()
decrypted_wrong = decipher_wrong_iv.update(ciphertext) + decipher_wrong_iv.finalize()
print("Testo decifrato (IV sbagliato):", decrypted_wrong.decode(errors="replace"))
print()

#
print("Key", key)
print("IV", iv)
print("Wrong IV", wrong_iv)

# === Domande di riflessione ===
# Perché l'IV è importante?
# - L'IV garantisce che messaggi identici cifrati con la stessa chiave producano output diversi.
# - Protegge dalla rivelazione di pattern nei dati cifrati.

# Cosa succede se l'IV viene riutilizzato?
# - Riutilizzare l'IV con la stessa chiave può compromettere la sicurezza del messaggio.
# - Può permettere ad un attaccante di dedurre informazioni sul contenuto cifrato (attacchi statistici).
