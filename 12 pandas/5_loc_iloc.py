import pandas as pd

df = pd.read_csv("username.csv", index_col=0, sep=";")

print(df)
print()

# Loc
print(df.loc["grey07"])
print()
print(df.loc["booker12"])
print()

# Iloc
print(df.iloc[3])
print()

# Riga e colonna (Johnson)
print(df.iloc[2, 2])
print()

# Seleziono da punto A a punto B
print(df.loc["booker12": "johnson81"])
# print()