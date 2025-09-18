"""
Inserire dati in MySQL
======================
Esempio di inserimento di righe in una tabella MySQL.
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

    studenti = [
        ("Carla", "carla@example.com"),
        ("Davide", "davide@example.com"),
    ]

    query = "INSERT INTO studenti (nome, email) VALUES (%s, %s)"

    cursor.executemany(query, studenti)
    conn.commit()
    print(f"Inserite {cursor.rowcount} righe nella tabella studenti.")
except Error as errore:
    print(f"Errore durante l'inserimento dei dati: {errore}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connessione chiusa.")
