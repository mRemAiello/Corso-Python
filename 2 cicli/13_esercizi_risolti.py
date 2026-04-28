# Leggere una serie di numeri interi passati dall’utente,
# fermandosi al primo numero che rende la serie non crescente e restituendo quanti numeri erano stati inseriti.

penultimo_numero = int(input("Scrivi un numero: "))
ultimo_numero = int(input("Scrivi un numero: "))
numeri = 2

while penultimo_numero < ultimo_numero:

    numero = int(input("Scrivi un numero: "))

    penultimo_numero = ultimo_numero
    ultimo_numero = numero

    numeri = numeri + 1

print("La serie è diventata non crescente dopo", numeri, "numeri")