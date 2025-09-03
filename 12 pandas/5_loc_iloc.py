import pandas as pd

df = pd.read_csv("username.csv", index_col=0, sep=";")

print(df)
print()

# Loc
print("Cerco la persona con username grey07")
print(df.loc["grey07"])
print()

print("Ora cerco booker12")
print(df.loc["booker12"])
print()

# Iloc
print("Iloc prende la posizione numero 3")
print(df.iloc[3])
print()

# Riga e colonna (Johnson)
print("Prendo riga 2 (escludo username) e colonna 2")
print(df.iloc[2, 2])
print()

# Seleziono da punto A a punto B
print("Seleziono da booker12 e johnson (compreso)")
print(df.loc["booker12": "johnson81"])
# print()