from cryptography.fernet import Fernet

# Generazione di una chiave
key = Fernet.generate_key()
cipher_suite = Fernet(key)
print(key)


# Cripto una stringa
plain_text = bytes("Messaggio segreto", 'utf-8')
cipher_text = cipher_suite.encrypt(plain_text)
print(cipher_text)


# Decripto una stringa
decrypted_text = cipher_suite.decrypt(cipher_text)
print(plain_text)
print(decrypted_text)