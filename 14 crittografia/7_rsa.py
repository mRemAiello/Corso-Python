from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# Generazione di una chiave privata RSA
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)

# Estrazione della chiave pubblica
public_key = private_key.public_key()

# Serializzazione e salvataggio delle chiavi
pem_private = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

pem_public = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)


print(pem_private)
print(pem_public)