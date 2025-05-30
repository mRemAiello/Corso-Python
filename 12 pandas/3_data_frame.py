import pandas as pd

ds = {
    "Mesi": ["Gennaio", "Febbraio", "Marzo", "Aprile"],
    "Giorni": [31, 28, 31, 30],
    "Stagione": ["Inverno", "Inverno", "Primavera", "Primavera"],
    "Festività": ["Capodanno", "Carnevale", "Festa X", "Festa Y"]
}

# Differenza tra dato standard e Data Frame
print(ds)
print()

# DF
df = pd.DataFrame(ds)
print(df)
print()