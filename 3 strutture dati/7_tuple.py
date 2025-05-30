# Tupla semplice
tupla = ("Milano", "Roma", "Udine", "Venezia")

# Tupla con costruttore, che ESPLICITA in maniera chiara che parliamo di una tupla
# x = tuple(("Milano", "Roma", "Udine", "Venezia"))

# Se voglio fare una tupla con un elemento devo mettere la ,
# x = ("Milano",)

# La tupla può anche avere tipi di variabili differenti
tupla_2 = ("Milano", 5, 4.5, False)

# Printa gli elementi della tupla
print(tupla)

# Tipo di tupla
print(type(tupla))

# Lunghezza
print(len(tupla))

# Accedere agli elementi
print(tupla[2])
print(tupla[-1])

# Range di elementi (secondo elemento non incluso)
print(tupla[:2])
print(tupla[1:])
print(tupla[1:2])

# Controllo se esiste un elemento
if "Milano" in tupla:
    print("La parola Milano è dentro la tupla")

# Se provo a modificare ottengo un errore. Idem non posso rimuovere elementi
# x[2] = "Roma2"
# y = list(x)
# y[0] = "Milano2"
# y.remove("Venezia")
# x = tuple(y)
# print(x)

# Unisco le tuple facendo x + y (non siamo limitati all'unione di soli due elementi)
tupla = ("Milano", "Roma")
tupla_2 = ("Brescia", "Torino", "Milano")
tupla_unita = tupla + tupla_2
print(tupla_unita)

# Per sapere dove si trova un elemento oppure quante volte è ripetuto, uso count e index
occorrenza_milano = tupla_unita.count("Milano")
primo_indice_milano = tupla_unita.index("Milano")
print(occorrenza_milano)
print(primo_indice_milano)

# Cancellare contenuti
# del tupla
# print(tupla)