# Funzione per dividere due numeri con gestione delle eccezioni
# La funzione farà:
# try -> gestione errori (ZeroDivionError, TypeError, else) -> finally -> return
def dividi(numeratore, denominatore):
    try:
        # Prova a eseguire la divisione
        risultato = numeratore / denominatore
    except ZeroDivisionError:
        # Gestisce l'errore di divisione per zero
        print("Errore: Non è possibile dividere per zero.")
        return 0
    except TypeError:
        # Gestisce l'errore di tipo, nel caso i dati forniti non siano numeri
        print("Errore: Sono accettati solo numeri.")
        return None
    else:
        # Se non ci sono errori, restituisce il risultato
        return risultato
    finally:
        # Blocco che viene sempre eseguito, indipendentemente dal risultato
        print("Operazione completata.")


# Esempi di chiamata della funzione
# Output: 5.0
print(dividi(10, 2))
print()

# Output: Errore: Non è possibile dividere per zero.
print(dividi(10, 0))
print()

# Output: Errore: Sono accettati solo numeri.
print(dividi(10, 'a'))
print()
print(dividi("c", "b"))