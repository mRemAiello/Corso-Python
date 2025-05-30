from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# NB: Il pacchetto da installare si chiama pycryptodome, mentre PyCharm potrebbe installare crypto
# E questo porterebbe a dei conflitti, avendo 2 librerie diverse con lo stesso nome.

# Per risolvere aprire il terminale e digitare:
# pip uninstall crypto
# pip uninstall pycryptodome
# pip install pycryptodome


# Funzione per cifrare il messaggio con DES
def encrypt_des(key, plaintext):
    # Crea il cifratore DES con modalità ECB
    cipher = DES.new(key, DES.MODE_ECB)

    # Applica padding al messaggio per garantire che sia un multiplo di 8 byte
    padded_plaintext = pad(plaintext, DES.block_size)

    # Cifra il messaggio
    ciphertext = cipher.encrypt(padded_plaintext)

    return ciphertext


# Funzione per decifrare il messaggio con DES
def decrypt_des(key, ciphertext):
    # Crea il cifratore DES per la decifratura
    cipher = DES.new(key, DES.MODE_ECB)

    # Decifra il messaggio
    decrypted_padded_text = cipher.decrypt(ciphertext)

    # Rimuove il padding
    decrypted_text = unpad(decrypted_padded_text, DES.block_size)

    return decrypted_text


# Genera una chiave DES di 8 byte (56 bit effettivi)
key = get_random_bytes(8)  # DES utilizza chiavi a blocchi di 8 byte

# Messaggio da cifrare
message = b"Questo e' un segreto!"

print("Messaggio originale:", message)

# Cifra il messaggio
ciphertext = encrypt_des(key, message)
print("\nMessaggio cifrato:", ciphertext)

# Decifra il messaggio
decrypted_message = decrypt_des(key, ciphertext)
print("\nMessaggio decifrato:", decrypted_message)