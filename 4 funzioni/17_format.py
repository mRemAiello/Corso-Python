# Concatenare
y = 1
str2 = " ciao sono MIRKO "
str3 = "e sono con " + str(y) + " studente"
print(str2 + str3)


# Format
# NON puoi concatenare string e int
# nome = "Mirko"
# prova = f"Ciao io sono " + nome + " e ho " + str(15) + " anni"



# Usa format
prova = "Ciao io sono {} e ho {} anni"
print(prova)
print(prova.format("Samuele", 20))
print(prova.format("Mirko", 34))


# Posso farlo più volte usando anche gli indici
nome = input("..")
altezza = int(input("..."))
eta = int(input("..."))
peso = int(input("..."))

prova = "Ciao sono {}, ho {} anni, sono alto {} e peso {} kg"
print(prova.format(nome, eta, altezza, peso))


# Format con numeri e media, min e massimo
minimo = -1
massimo = 1
quantita = 4
media = 2
prova = "La media dei {} numeri è: {}, il minimo è {}, il massimo è {}"
print(prova.format(quantita, media, minimo, massimo))
print(prova.format(2, 3, 3, 4))


# Meglio
print("La media dei", 2, "numeri è:", 5, ", il minimo è", minimo, ", il massimo è", massimo)


# Format
print(f"La media dei {2} numeri è: {5}, il minimo è {minimo}, il massimo è {massimo}")