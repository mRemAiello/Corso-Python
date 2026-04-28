# Si crei un programma che simula il caricamento di un cellulare
# fino a quando è completamente carico e comunichi ogni minuto il livello di carica,
# si consideri che per i primi 10 minuti ogni minuto la carica aumenta del 4%,
# per i 10 minuti successivi del 2% al minuto, per i minuti successivi dell’1% al minuto.

carica = 1
minuti = 0

while carica < 100:

    if minuti <= 10:
        print("Carica aumentata del 4%, Carica attuale:", carica)
        carica = carica + 4
    elif minuti <= 20:
        print("Carica aumentata del 2%, Carica attuale:", carica)
        carica = carica + 2
    else:
        print("Carica aumentata del 1%, Carica attuale:", carica)
        carica = carica + 1

    if carica >= 100:
        carica = 100

    minuti = minuti + 1

print("Telefono carico dopo", minuti, "minuti")