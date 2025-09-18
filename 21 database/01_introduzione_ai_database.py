"""
Introduzione ai database
=======================
Questo script introduce i concetti fondamentali dei database relazionali.
"""

# I database permettono di archiviare dati in modo strutturato e sicuro.
# Qui usiamo un semplice dizionario per simulare una tabella di utenti.
data = [
    {"id": 1, "nome": "Alice", "email": "alice@example.com"},
    {"id": 2, "nome": "Bob", "email": "bob@example.com"},
]

print("Elenco utenti (simulazione di una tabella):")
for utente in data:
    print(f"ID: {utente['id']}, Nome: {utente['nome']}, Email: {utente['email']}")

print("\nQuesto esempio mostra come i dati strutturati possano essere rappresentati")
print("e successivamente archiviati in un sistema di database relazionale.")
