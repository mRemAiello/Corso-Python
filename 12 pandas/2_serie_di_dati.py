# Una serie di dati è una colonna (ex. Mesi o Giorni).
# L'insieme di tutte le colonne è un DataFrame

import pandas as pd

serie = [5, 10, 15, 20, 25]
serie_pandas = pd.Series(serie)
print(serie)
print()
print(serie_pandas)
print()


# Etichette
label = ["L1", "L2", "L3", "L4", "L5"]
serie_pandas = pd.Series(serie, index=label)
print(serie_pandas)
print()


#
# print(serie_pandas[0])
print(serie_pandas["L3"])
print()


# Serie di dati da un dict
dic = {
    "L1": 5,
    "L2": 10,
    "L3": 15,
    "L4": 20,
    "L5": 25
}
serie_pandas = pd.Series(dic, index=dic.keys())
print(serie_pandas)