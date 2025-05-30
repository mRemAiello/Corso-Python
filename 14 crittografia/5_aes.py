from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


# Funzione per cifrare il messaggio con AES GCM
def encrypt_aes_gcm(key, plaintext):
    # Genera un IV (vettore di inizializzazione) casuale
    iv = os.urandom(12)

    # Crea il cifratore AES con modalità GCM
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    # Cifra il messaggio
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Restituisce il ciphertext, IV e il tag GCM per l'integrità
    return ciphertext, iv, encryptor.tag


# Funzione per decifrare il messaggio con AES GCM
def decrypt_aes_gcm(key, ciphertext, iv, tag):
    # Crea il cifratore AES per la decifratura
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    # Decifra il messaggio
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_text


# Esempio di utilizzo
# Genera una chiave AES a 256 bit (32 byte)
key = os.urandom(32)
print(key)
print()

# Messaggio da cifrare
message = b"Messaggio segreto 1234k3020230 !"
print("Messaggio originale:", message)
print()

# Cifra il messaggio
ciphertext, iv, tag = encrypt_aes_gcm(key, message)
print("IV:", iv)
print("Tag:", tag)
print("Messaggio cifrato:", ciphertext)
print()

# Decifra il messaggio
decrypted_message = decrypt_aes_gcm(key, ciphertext, iv, tag)
print("Messaggio decifrato:", decrypted_message)