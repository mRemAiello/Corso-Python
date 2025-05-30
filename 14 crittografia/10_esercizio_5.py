# Esercizio 5: Firma Digitale con RSA
#
# Obiettivo: Creare e verificare una firma digitale utilizzando la crittografia asimmetrica.
#
# Istruzioni:
#
#     Genera una coppia di chiavi RSA.
#     Scrivi un programma che:
#         Crea una firma digitale di un messaggio utilizzando la chiave privata.
#         Verifica la firma utilizzando la chiave pubblica.
#     Modifica il programma per includere un hash (ad es. SHA256) come parte del processo di firma.
#
# Domande di riflessione:
#
#     Perché si usa una firma digitale in combinazione con un algoritmo di hashing?
#     Quali sono le applicazioni pratiche delle firme digitali?

from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# === Generazione chiavi RSA ===
private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
public_key = private_key.public_key()

# === Messaggio da firmare ===
message = bytes(input("Scrivi un messaggio:"), "utf8")

# === Creazione firma digitale con SHA256 ===
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("Firma digitale creata:", signature)

# === Verifica firma ===
try:
    # Firma digitale fake
    # signature = b"firma sbagliata"
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Firma verificata: il messaggio è autentico e integro.")
except InvalidSignature:
    print("Firma non valida: il messaggio è stato alterato o la firma non è corretta.")

# === Domande di riflessione ===
# Perché usare una firma digitale con hashing?
# - L'hash rende il processo di firma più efficiente e sicuro: si firma il digest, non l'intero messaggio.
# - Protegge l'integrità e garantisce che anche una minima modifica venga rilevata.

# Applicazioni pratiche delle firme digitali:
# - Firma di email e documenti elettronici
# - Certificati digitali e identità online
# - Transazioni bancarie e blockchain (es. firme nelle transazioni Bitcoin)
