import pandas as pd

# CVS
# Mesi, Giorni
# Gennaio, 31
# Febbraio, 28
ds = {
    "Mesi": ["Gennaio", "Febbraio", "Marzo", "Aprile"],
    "Giorni": [31, 28, 31, 30]
}

df = pd.DataFrame(ds)
print(ds)
print()
print(df)
print()