"""
Eliminare dati da MySQL
======================
Esempio di cancellazione di record in una tabella MySQL.
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

    query = "DELETE FROM studenti WHERE email = %s"
    dati = ("davide@example.com",)

    cursor.execute(query, dati)
    conn.commit()

    if cursor.rowcount == 0:
        print("Nessun record eliminato: controlla che i criteri siano corretti.")
    else:
        print(f"Eliminati {cursor.rowcount} record dalla tabella studenti.")
except Error as errore:
    print(f"Errore durante l'eliminazione dei dati: {errore}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connessione chiusa.")
