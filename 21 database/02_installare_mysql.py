"""
Installare MySQL
================
Questo script descrive i passaggi principali per installare MySQL su sistemi
basati su Debian/Ubuntu utilizzando comandi shell all'interno di Python.
"""

import textwrap

comandi = [
    "sudo apt update",
    "sudo apt install mysql-server",
    "sudo systemctl status mysql",
]

print("Passaggi per installare MySQL su Debian/Ubuntu:\n")
for comando in comandi:
    print(f"- {comando}")

print("\nConfermare che il servizio sia attivo e proteggere l'installazione:")
print(textwrap.fill(
    "Eseguire 'sudo mysql_secure_installation' per configurare password, rimuovere gli utenti anonimi e migliorare la sicurezza.",
    width=80,
))
