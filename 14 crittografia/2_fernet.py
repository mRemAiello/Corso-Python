from cryptography.fernet import Fernet

# Generazione di una chiave
key = Fernet.generate_key()
print(key)


# Istanza del Fernet che cripterà / decripterà
cipher_suite = Fernet(key)


# Cripto una stringa
plain_text = bytes("ciao", 'utf-8')
print(plain_text)


# Criptazione
cipher_text = cipher_suite.encrypt(plain_text)
print(cipher_text)


# Decripto una stringa
decrypted_text = cipher_suite.decrypt(cipher_text)
print(decrypted_text)