# ============================================================
# Strutture dati in Python: confronto tra List, Tuple, Set e Dict
# ============================================================

# --- Concetti chiave ---

# Ordinata     : gli elementi mantengono un ordine stabile di inserimento
# Indicizzata  : si accede agli elementi tramite indice (es. lista[0])
# Modificabile : si possono aggiungere, rimuovere o cambiare elementi dopo la creazione
# Immutabile   : una volta creata, la collezione non può essere modificata
# Duplicati    : la collezione può contenere più elementi con lo stesso valore

# --- Riepilogo ---
#
#  Tipo        | Ordinata | Indicizzata | Modificabile | Duplicati | Sintassi
#  ------------|----------|-------------|--------------|-----------|----------
#  list        |    Sì    |     Sì      |      Sì      |    Sì     |  [1, 2]
#  tuple       |    Sì    |     Sì      |      No      |    Sì     |  (1, 2)
#  set         |    No    |     No      |      Sì      |    No     |  {1, 2}
#  dict        |    Sì    |  per chiave |      Sì      |    No*    |  {"k": v}
#
#  * i dizionari non permettono chiavi duplicate (i valori possono ripetersi)

# --- Esempi rapidi ---

lista  = [1, 2, 2, 3]          # modificabile, duplicati ammessi
tupla  = (1, 2, 2, 3)          # immutabile,   duplicati ammessi
gruppo = {1, 2, 3}             # niente duplicati, niente indice
diz    = {"a": 1, "b": 2}      # accesso per chiave: diz["a"] → 1