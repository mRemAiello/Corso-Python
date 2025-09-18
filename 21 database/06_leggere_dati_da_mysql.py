"""
Leggere dati da MySQL
=====================
Esempio di lettura di righe da una tabella MySQL.
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
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT id, nome, email FROM studenti")
    risultati = cursor.fetchall()

    print("Studenti registrati:")
    for studente in risultati:
        print(f"{studente['id']}: {studente['nome']} - {studente['email']}")
except Error as errore:
    print(f"Errore durante la lettura dei dati: {errore}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connessione chiusa.")
