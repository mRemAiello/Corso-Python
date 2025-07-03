# Gestire un flusso in cui:
#
#     Un modulo interno solleva un'eccezione.
#     Un modulo intermedio la intercetta, la logga o la gestisce parzialmente.
#     Il modulo superiore decide se rilanciare o gestire definitivamente.


class ErroreElaborazioneDati(Exception):
    def __init__(self, messaggio):
        super().__init__(f"[ERRORE INTERNO] {messaggio}")


# livello 1: funzione interna che solleva l'eccezione
def livello_interno():
    # Simula un errore (es. parsing fallito, file corrotto, ecc.)
    raise ErroreElaborazioneDati("Il formato dei dati è invalido.")


# livello 2: modulo intermedio che intercetta e rilancia
def livello_intermedio():
    try:
        livello_interno()
    except ErroreElaborazioneDati as e:
        print(f"[LIVELLO INTERMEDIO] Errore intercettato: {e}")
        # Logica aggiuntiva: es. logging, trasformazione, wrapping
        raise  # Rilancia l'eccezione al chiamante superiore


# livello 3: modulo superiore che prende la decisione finale
def livello_superiore():
    try:
        livello_intermedio()
    except ErroreElaborazioneDati as e:
        print(f"[LIVELLO SUPERIORE] L'errore è stato rilevato: {e}")
        # Decisione finale: mostrare messaggio, terminare programma, fallback, ecc.
        print("[LIVELLO SUPERIORE] Operazione annullata.")


# Avvio
livello_superiore()