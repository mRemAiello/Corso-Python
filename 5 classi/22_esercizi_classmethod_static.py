# Progetta un sistema orientato agli oggetti per la gestione di un servizio di noleggio
# veicoli utilizzando classi, sottoclassi, metodi statici e class method.

# Simulare una piccola applicazione che permetta di creare diversi tipi di
# veicoli e calcolare il costo di noleggio in base a regole specifiche.

# Requisiti
# Classe base Veicolo
#
# Attributi: marca, modello, anno, prezzo_giornaliero.
# Metodo __str__() che restituisce una stringa con i dati del veicolo.

# Class method da_stringa(dati) che crei un oggetto partendo da una stringa formattata tipo:
# "Fiat;500;2022;35"

# Static method calcola_costo(prezzo_giornaliero, giorni) che restituisca il costo totale del noleggio.

# Sottoclassi
# Crea almeno due sottoclassi:

# Auto
# attributo extra: numero_porte

# Moto
# attributo extra: cilindrata

# Ogni sottoclasse deve:
# estendere il costruttore della classe base
# fare override del metodo descrizione() aggiungendo le proprie informazioni.

# Creare almeno 3 veicoli, uno usando la class method.
# Calcolare il costo di noleggio usando la static method.
# Stampare le descrizioni complete dei veicoli.
# Aggiungi una variabile di classe che tenga traccia del numero totale di veicoli creati.
# Inserisci un metodo che applichi uno sconto percentuale al prezzo giornaliero.