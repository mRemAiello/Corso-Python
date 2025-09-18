"""
Installare MySQL su Windows / PyCharm
=====================================
Questo script elenca i passaggi principali per installare MySQL su Windows e
configurarlo per l'utilizzo con PyCharm.
"""

import textwrap

passaggi = [
    "Scaricare MySQL Installer per Windows dal sito ufficiale (https://dev.mysql.com/downloads/installer/).",
    "Avviare l'installer, scegliere 'Developer Default' e completare la procedura guidata.",
    "Impostare una password sicura per l'utente root quando richiesto e annotarla.",
    "Aprire MySQL Workbench per verificare che il server si avvii correttamente e creare un database di prova.",
    "Aprire PyCharm, creare o selezionare un progetto Python e installare il pacchetto 'mysql-connector-python' dal terminale integrato (pip install mysql-connector-python).",
    "In PyCharm, utilizzare Database > Data Sources per aggiungere una nuova connessione MySQL con host localhost, porta 3306 e le credenziali impostate.",
]

print("Passaggi per installare e configurare MySQL su Windows / PyCharm:\n")
for indice, passaggio in enumerate(passaggi, start=1):
    print(textwrap.fill(f"{indice}. {passaggio}", width=88))
