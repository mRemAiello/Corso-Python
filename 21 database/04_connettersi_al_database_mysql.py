"""
Connettersi al database MySQL
=============================
Esempio di connessione a MySQL usando mysql-connector-python.
"""

import mysql.connector
from mysql.connector import Error

try:
    connessione = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password_di_esempio",
        database="scuola",
    )
    if connessione.is_connected():
        print("Connessione a MySQL avvenuta con successo!")
except Error as errore:
    print(f"Errore durante la connessione a MySQL: {errore}")
finally:
    if 'connessione' in locals() and connessione.is_connected():
        connessione.close()
        print("Connessione chiusa.")
