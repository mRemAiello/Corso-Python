# Obiettivo
#
# Realizza un'applicazione desktop utilizzando Python e PySide6 che permetta di:
#
#     Aggiungere libri a una libreria
#     Visualizzare l’elenco dei libri presenti
#     Salvare i dati su file
#     Caricare i dati dal file all’avvio dell’app
#

# Specifiche Funzionali
#
#     Classe Libro
#         Attributi: titolo, autore, anno di pubblicazione, ISBN
#         Metodo __str__() per stampare il libro in formato leggibile


#     Classe Libreria
#
#         Attributo: lista di libri
#
#         Metodi:
#
#             aggiungi_libro(libro)
#
#             rimuovi_libro(isbn)
#
#             salva_su_file(percorso_file)
#
#             carica_da_file(percorso_file)


#     Interfaccia Grafica con PySide6


#         Campo di input per ciascun attributo del libro

#         Pulsanti:

#               "Aggiungi Libro"
#               "Modifica libro"
#               "Salva Libreria"
#               "Carica Libreria"

# Gestione Salvataggio e caricamento

# Finestre di QDialog per gestire la conferma delle operazioni

#         Elenco (QListWidget) che mostra i libri inseriti