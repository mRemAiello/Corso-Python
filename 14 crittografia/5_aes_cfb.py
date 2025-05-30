from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os


# Funzione per cifrare il messaggio con AES CFB
def encrypt_aes_cfb(key, plaintext):
    # Genera un IV (vettore di inizializzazione) casuale
    iv = os.urandom(16)

    # Crea il cifratore AES con modalità CFB
    encryptor = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend()).encryptor()

    # Cifra il messaggio
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    # Restituisce il ciphertext e l'IV
    return ciphertext, iv


# Funzione per decifrare il messaggio con AES CFB
def decrypt_aes_cfb(key, ciphertext, iv):
    # Crea il cifratore AES per la decifratura
    decryptor = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend()).decryptor()

    # Decifra il messaggio
    decrypted_text = decryptor.update(ciphertext) + decryptor.finalize()

    return decrypted_text


# Esempio di utilizzo
# Genera una chiave AES a 256 bit (32 byte)
key = os.urandom(16)
print("Key:", key)
print()

# Messaggio da cifrare
message = b"Messaggio segreto!"
print("Messaggio originale:", message)
print()

# Cifra il messaggio
ciphertext, iv = encrypt_aes_cfb(key, message)
print("IV:", iv)
print("Messaggio cifrato:", ciphertext)
print()

# Decifra il messaggio
decrypted_message = decrypt_aes_cfb(key, ciphertext, iv)
print("Messaggio decifrato:", decrypted_message)