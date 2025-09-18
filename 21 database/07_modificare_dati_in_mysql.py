"""
Modificare dati in MySQL
=======================
Esempio di aggiornamento di record esistenti in una tabella MySQL.
"""

import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password_di_esempio",
        database="scuola",
    )
    cursor = conn.cursor()

    query = (
        "UPDATE studenti "
        "SET email = %s "
        "WHERE nome = %s"
    )

    dati = ("carla.rossi@example.com", "Carla")

    cursor.execute(query, dati)
    conn.commit()

    if cursor.rowcount == 0:
        print("Nessun record aggiornato: controlla che lo studente esista.")
    else:
        print(f"Aggiornato l'indirizzo email di {cursor.rowcount} studente/i.")
except Error as errore:
    print(f"Errore durante l'aggiornamento dei dati: {errore}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connessione chiusa.")
