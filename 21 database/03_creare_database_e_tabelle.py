"""
Creare database e tabelle
=========================
Questo script mostra i comandi SQL per creare un database e una tabella in MySQL.
"""

comandi_sql = [
    "CREATE DATABASE scuola;",
    "USE scuola;",
    """CREATE TABLE studenti (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE
    );""",
]

print("Comandi SQL per creare database e tabella:")
for comando in comandi_sql:
    print("\n" + comando)

print("\nEseguire questi comandi nella shell MySQL per configurare la struttura iniziale.")
