import pandas as pd

# df = pd.read_csv("username.csv")
# print(df)
# print()

# Non funziona! Separator e delimiter
df = pd.read_csv("username.csv", sep=";")
print(df)
print()

# Posso fare lo slicing
print(df[0:2])
print()
print(df.head(3))
print()
print(df.tail(2))
print()


# Prendo solo colonne, e solo un tot di elementi
print(df["Username"][0:2])
print()

# Prendo più colonne
df2 = df
df = df[["First name", "Last name"]].head(2)
df2 = df2[["First name", "Last name"]].tail(2)

print(df)
print()
print(df2)