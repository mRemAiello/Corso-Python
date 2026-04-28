# Si supponga che l’andamento della popolazione di un’alga si sviluppi nel seguente modo:
# un anno raddoppia l’anno successivo cala di un terzo.
# Creare un programma che dato un valore iniziale della popolazione e un valore da raggiungere
# di popolazione dica quanti anni ci mette quella popolazione a raggiungere o superare quel valore.

popolazione = 100
popolazione_soglia = 100000
anni = 0

while popolazione <= popolazione_soglia:

    if anni % 2 == 0:
        popolazione = popolazione * 2
    else:
        popolazione = popolazione - int((popolazione / 3))

    anni = anni + 1

    print("Nell'anno", anni, "la popolazione di alghe ammonta a", popolazione, "elementi")