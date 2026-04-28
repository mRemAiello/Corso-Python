# Ogni anno in banca sui conti deposito si accumula un interesse rispetto al saldo iniziale,
# l’interesse accumulato si somma al saldo precedente e concorrerà al calcolo dell’interesse sull’anno successivo.
# Dato un saldo iniziale, la percentuale di interesse e una soglia, verificare
# dopo quanti anni si raggiunge o supera la soglia.

saldo = 5000
interessi = 3.5
soglia_saldo = 40000
anni = 0

while saldo < soglia_saldo:

    cumulo = int(saldo * interessi / 100)
    anni = anni + 1

    print("Anno", anni, "saldo:", saldo, "interessi per quest'anno", cumulo)

    saldo = saldo + cumulo

print("Dopo", anni, "anni hai raggiunto un saldo di", saldo, "euro")