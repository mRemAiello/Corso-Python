import pandas as pd

# df = pd.read_csv("username.csv")
# print(df)
# print()

# Non funziona! Separator e delimiter
df = pd.read_csv("username.csv", sep=";")
print("Data Frame")
print(df)
print()

# Posso fare lo slicing
print("Slicing 0-1")
print(df[0:2])
print()

print("I primi 3 elementi")
print(df.head(3))
print()

print("Gli ultimi 2")
print(df.tail(2))
print()


# Prendo solo colonne, e solo un tot di elementi
print("Prendo solo gli username, e solo dei primi 2")
print(df["Username"][0:2])
print()

# Prendo più colonne
df2 = df
df = df[["First name", "Last name"]].head(2)
df2 = df2[["First name", "Last name"]].tail(2)

print("Prendo first name e last name dei primi 2")
print(df)
print()

print("Prendo first name e last name degli ultimi 2")
print(df2)