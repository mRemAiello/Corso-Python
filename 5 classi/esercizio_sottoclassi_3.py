#     Item: La classe base che rappresenta un elemento generico della biblioteca.
#     Book: Una sottoclasse di Item che rappresenta un libro.
#     Magazine: Una sottoclasse di Item che rappresenta una rivista.
#     Library: Una classe che gestisce una collezione di Item, Book e Magazine.
#
#     Classe Item
#         Attributi: title (string), publication_year (Date)
#         Metodo: __str__() che restituisce una stringa con il titolo e l'anno di pubblicazione.
#
#     Classe Book (Sottoclasse di Item)
#         Attributi: author (string), isbn (string)
#         Metodo: __str__() che estende il metodo della classe base per includere l'autore e l'ISBN.
#
#     Classe Magazine (Sottoclasse di Item)
#         Attributi: issue_number (int)
#         Metodo: __str__() che estende il metodo della classe base per includere il numero dell'edizione.
#
#     Classe Library
#         Attributi: items (lista di oggetti Item)
#         Metodi: add_item(item), remove_item(title), find_item(title), __str__() per visualizzare l'intera collezione.


# # Immagina di dover creare un'applicazione per la gestione di una biblioteca.
# # L'applicazione dovrebbe consentire agli utenti di cercare libri nel catalogo, prendere in prestito libri, restituire libri
# # e tenere traccia dei prestiti attivi. Inoltre, dovrebbe essere possibile aggiungere nuovi libri al catalogo e rimuoverli
# # quando non sono più disponibili.
# # Gli utenti dovrebbero essere in grado di visualizzare un elenco dei libri disponibili e dei libri attualmente in prestito.