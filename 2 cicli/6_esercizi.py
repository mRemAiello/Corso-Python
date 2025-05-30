# Scrivere un programma che utilizzi un loop for (e while) per stampare tutte le lettere di una stringa.
# Scrivere un programma che utilizzi un loop for (e while) per contare quante volte una lettera compare in una stringa.
# Chiedere all'utente di inserire una stringa. Stampare solo le vocali della stringa usando un loop while e for.
# Chiedere all'utente di inserire una stringa. Stampare la stringa al contrario usando sia il while che il for.

stringa = "ciao"

# Proprietà del Python
i = 0
while i < len(stringa):
    print(stringa[i])
    i = i + 1


for lettera in stringa:
    print(lettera)