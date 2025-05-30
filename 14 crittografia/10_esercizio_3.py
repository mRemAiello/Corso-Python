# Esercizio 3: Crittografia Asimmetrica con RSA
#
# Obiettivo: Applicare la crittografia asimmetrica per cifrare e decifrare messaggi utilizzando RSA.
#
# Istruzioni:
#
#     Genera una coppia di chiavi RSA (una chiave pubblica e una chiave privata).
#     Cifra un messaggio utilizzando la chiave pubblica e visualizza il risultato.
#     Decifra il messaggio cifrato utilizzando la chiave privata e visualizza il messaggio originale.
#     Salva le chiavi in formato PEM su file e recuperale per utilizzarle in sessioni future.
#
# Domande di riflessione:
#
#     Cosa succede se provi a decifrare un messaggio con la chiave pubblica?
#     Quali sono i vantaggi della crittografia asimmetrica rispetto a quella simmetrica?

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# === 1. Genera coppia di chiavi RSA ===
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# print(private_key)
# print(public_key)

# === 2. Salva le chiavi in formato PEM ===
with open("private_key.pem", "wb") as file:
    file.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
    ))

with open("public_key.pem", "wb") as file:
    file.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# === 3. Carica le chiavi dai file PEM ===
with open("private_key.pem", "rb") as file:
    private_key_loaded = serialization.load_pem_private_key(file.read(), password=None)

with open("public_key.pem", "rb") as file:
    public_key_loaded = serialization.load_pem_public_key(file.read())

# === 4. Cifra un messaggio con la chiave pubblica ===
message = b"Questo e' un messaggio segreto."
ciphertext = public_key_loaded.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Messaggio cifrato:", ciphertext)

# === 5. Decifra il messaggio con la chiave privata ===
decrypted_message = private_key_loaded.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
print("Messaggio decifrato:", decrypted_message.decode())

# === Domande di riflessione ===
# Cosa succede se provi a decifrare con la chiave pubblica?
# --> L'operazione fallisce: la chiave pubblica non può decifrare, ma solo cifrare.

# Vantaggi della crittografia asimmetrica:
# - Maggiore sicurezza nella trasmissione delle chiavi: non serve scambiarsi una chiave segreta.
# - Permette firme digitali (autenticazione + integrità).
# - Ideale per ambienti dove le parti non si conoscono in anticipo.
