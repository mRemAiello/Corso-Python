"""
Esercizio riepilogativo MySQL
============================
Script che riassume i passaggi principali di gestione di un database MySQL:
creazione tabella, inserimento, aggiornamento, lettura ed eliminazione dei dati.
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

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS corsi (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            docente VARCHAR(100) NOT NULL
        )
        """
    )
    print("Tabella 'corsi' pronta all'uso.")

    inserisci_query = "INSERT INTO corsi (nome, docente) VALUES (%s, %s)"
    corsi = [
        ("Programmazione Python", "Prof.ssa Bianchi"),
        ("Database relazionali", "Prof. Verdi"),
    ]
    cursor.executemany(inserisci_query, corsi)
    conn.commit()
    print(f"Inseriti {cursor.rowcount} corsi di esempio.")

    aggiorna_query = "UPDATE corsi SET docente = %s WHERE nome = %s"
    cursor.execute(aggiorna_query, ("Prof. Rossi", "Database relazionali"))
    conn.commit()
    print("Aggiornato il docente del corso di Database relazionali.")

    cursor.execute("SELECT id, nome, docente FROM corsi")
    for corso in cursor.fetchall():
        print(f"Corso #{corso[0]}: {corso[1]} - Docente: {corso[2]}")

    elimina_query = "DELETE FROM corsi WHERE nome = %s"
    cursor.execute(elimina_query, ("Programmazione Python",))
    conn.commit()
    print("Corso 'Programmazione Python' eliminato.")
except Error as errore:
    print(f"Si è verificato un errore MySQL: {errore}")
finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals() and conn.is_connected():
        conn.close()
        print("Connessione chiusa.")
