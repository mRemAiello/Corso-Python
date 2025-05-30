import pandas as pd

# Esercizio 1
data = {
    "Nome": ["Alice", "Bob", "Carlo", "Diana"],
    "Età": [25, 30, 22, 35],
    "Città": ["Milano", "Roma", "Napoli", "Torino"]
}
df = pd.DataFrame(data)

# Esercizio 2
print(df["Nome"])

# Esercizio 3
df_filtered = df[df["Età"] > 25]
print(df_filtered)

# Esercizio 4
df["Salario"] = [50000, 60000, 55000, 65000]

# Esercizio 5
media_eta = df["Età"].mean()
print(media_eta)

# Esercizio 6
df.rename(columns={"Città": "Località"}, inplace=True)

# Esercizio 7
df_sorted = df.sort_values(by="Età")
print(df_sorted)

# Esercizio 8
df.drop(columns=["Salario"], inplace=True)

# Esercizio 9
df.to_csv("dati.csv", index=False)

# Esercizio 10
df_loaded = pd.read_csv("dati.csv")
print(df_loaded)
