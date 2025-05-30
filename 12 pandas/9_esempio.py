# Importiamo la libreria pandas. Se non è installata, usa "pip install pandas" per installarla.
import pandas as pd

# Creazione di un DataFrame a partire da un dizionario
data = {
    'Nome': ['Anna', 'Luca', 'Marco', 'Giulia'],
    'Età': [23, 35, 29, 22],
    'Città': ['Roma', 'Milano', 'Napoli', 'Torino']
}

# Il DataFrame è una struttura dati bidimensionale simile a una tabella.
df = pd.DataFrame(data)

# Stampa del DataFrame
print("DataFrame originale:")
print(df)

# Accesso a una colonna specifica del DataFrame
print("\nAccesso alla colonna 'Nome':")
print(df['Nome'])

# Filtraggio dei dati: selezioniamo le righe dove l'età è maggiore di 25
print("\nRighe con età maggiore di 25:")
print(df[df['Età'] > 25])

# Aggiungere una nuova colonna al DataFrame
df['Salario'] = [50000, 60000, 55000, 48000]
print("\nDataFrame con la nuova colonna 'Salario':")
print(df)

# Descrizione statistica del DataFrame (solo colonne numeriche)
print("\nDescrizione statistica delle colonne numeriche:")
print(df.describe())

# Raggruppare i dati per una colonna e calcolare la media (utile per aggregare dati)
print("\nMedia dei salari per città:")
print(df.groupby('Città')['Salario'].mean())

# Ordinare i dati in base a una colonna (in questo caso, l'età)
print("\nDataFrame ordinato per età:")
print(df.sort_values(by='Età'))

# Scrivere il DataFrame su un file CSV
df.to_csv('output.csv', index=True)
print("\nIl DataFrame è stato salvato in 'output.csv'.")

# Leggere un file CSV e creare un DataFrame
df_from_csv = pd.read_csv('output.csv')
print("\nDataFrame letto dal file CSV:")
print(df_from_csv)

# Gestione dei valori mancanti (NaN). Creiamo un nuovo DataFrame con valori NaN.
data_with_nan = {
    'Nome': ['Anna', 'Luca', 'Marco', 'Giulia'],
    'Età': [23, None, 29, 22],
    'Città': ['Roma', None, 'Napoli', 'Torino']
}

df_nan = pd.DataFrame(data_with_nan)
print("\nDataFrame con valori NaN:")
print(df_nan)

# Riempire i valori NaN con un valore specifico (esempio: riempire con 0 o una stringa 'Sconosciuto')
df_nan_filled = df_nan.fillna({'Età': 0, 'Città': 'Sconosciuto'})
print("\nDataFrame con i valori NaN riempiti:")
print(df_nan_filled)

# Rimuovere le righe che contengono valori NaN
df_nan_dropped = df_nan.dropna()
print("\nDataFrame con le righe contenenti NaN rimosse:")
print(df_nan_dropped)

# Calcolare la media di una colonna, ignorando i NaN
print("\nMedia dell'età, ignorando i NaN:")
print(df_nan['Età'].mean())