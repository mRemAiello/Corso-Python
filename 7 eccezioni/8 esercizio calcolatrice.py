# Esercizio 10: Crea una calcolatrice semplice che chieda all'utente due numeri e un'operazione
# (somma, sottrazione, moltiplicazione, divisione).
# Gestisci eventuali errori come divisione per zero o input non validi per i numeri o l'operazione.

try:
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))
    operazione = input("Inserisci l'operazione (+, -, *, /): ")

    if operazione == "+":
        risultato = num1 + num2
    elif operazione == "-":
        risultato = num1 - num2
    elif operazione == "*":
        risultato = num1 * num2
    elif operazione == "/":
        if num2 == 0:
            raise ZeroDivisionError
        risultato = num1 / num2
    else:
        raise ValueError("Operazione non valida.")

    print("Risultato:", risultato)

except ValueError as e:
    print("Errore:", e)
except ZeroDivisionError:
    print("Errore: divisione per zero.")